#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
추출된 Properties 비교 스크립트

temp_extracted 폴더의 최신 추출본과 extracted_bundles의 기존 파일을 비교하여
누락된 키를 찾습니다.
"""

import os
import re
import json
from pathlib import Path
from collections import defaultdict
from datetime import datetime


def parse_properties_file(filepath):
    """Properties 파일 파싱"""
    properties = {}

    if not os.path.exists(filepath):
        return properties

    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()

        i = 0
        while i < len(lines):
            line = lines[i].rstrip('\n\r')

            # 주석이나 빈 줄 건너뛰기
            if not line.strip() or line.strip().startswith('#') or line.strip().startswith('!'):
                i += 1
                continue

            # key=value 파싱
            match = re.match(r'^([^=:]+?)[\s]*[=:](.*)$', line)
            if match:
                key = match.group(1).strip()
                value = match.group(2)

                # 줄바꿈 처리 (백슬래시로 끝나는 경우)
                while value.rstrip().endswith('\\') and i + 1 < len(lines):
                    value = value.rstrip()[:-1]
                    i += 1
                    next_line = lines[i].rstrip('\n\r')
                    value += '\n' + next_line

                properties[key] = value

            i += 1

    except Exception as e:
        print(f"⚠️  파일 읽기 오류: {filepath.name} - {e}")

    return properties


def find_latest_extraction():
    """가장 최근의 추출 디렉토리 찾기"""
    project_root = Path(__file__).parent.parent.parent.parent  # src/main/version_updates → main → src → root
    temp_dir = project_root / "temp_extracted"

    if not temp_dir.exists():
        return None

    # studio_* 형식의 디렉토리 찾기
    extraction_dirs = [d for d in temp_dir.iterdir() if d.is_dir() and d.name.startswith('studio_')]

    if not extraction_dirs:
        return None

    # 가장 최근 디렉토리 (이름으로 정렬, 타임스탬프 포함)
    latest = sorted(extraction_dirs, reverse=True)[0]

    return latest


def compare_with_existing():
    """최신 추출본과 기존 extracted_bundles 비교"""
    project_root = Path(__file__).parent.parent.parent.parent  # src/main/version_updates → main → src → root

    print("\n" + "=" * 80)
    print("Properties 비교 및 누락 키 확인")
    print("=" * 80 + "\n")

    # 최신 추출본 찾기
    latest_extraction = find_latest_extraction()

    if not latest_extraction:
        print("❌ temp_extracted 폴더에 추출된 데이터가 없습니다.")
        print("   먼저 작업 2(Properties Key 재추출)를 실행하세요.")
        return None

    print(f"📂 최신 추출본: {latest_extraction.name}\n")

    # 기존 extracted_bundles 디렉토리
    extracted_bundles = project_root / "extracted_bundles"

    if not extracted_bundles.exists():
        print("❌ extracted_bundles 디렉토리를 찾을 수 없습니다.")
        return None

    # 기존 파일 수집 (intellij, android 등 하위 폴더에서)
    existing_files = {}
    for subdir in extracted_bundles.iterdir():
        if subdir.is_dir():
            messages_dir = subdir / "messages"
            if messages_dir.exists():
                for prop_file in messages_dir.glob("*.properties"):
                    filename = prop_file.name
                    if filename not in existing_files:
                        existing_files[filename] = parse_properties_file(prop_file)
                    else:
                        # 여러 소스에서 같은 파일 발견 시 병합
                        new_keys = parse_properties_file(prop_file)
                        existing_files[filename].update(new_keys)

    print(f"📂 기존 파일 수: {len(existing_files)}개\n")

    # 새로 추출된 파일 수집
    new_files = {}
    for prop_file in latest_extraction.glob("*.properties"):
        filename = prop_file.name
        new_files[filename] = parse_properties_file(prop_file)

    print(f"📂 새 추출 파일 수: {len(new_files)}개\n")

    # 비교 수행
    print("🔍 비교 수행 중...\n")

    missing_data = {
        'extraction_date': latest_extraction.name,
        'new_files': [],           # 완전히 새로운 파일
        'missing_keys': {},        # 기존 파일에서 누락된 키
        'modified_keys': {},       # 값이 변경된 키
        'stats': {
            'total_new_files': len(new_files),
            'total_existing_files': len(existing_files),
            'completely_new_files': 0,
            'files_with_missing_keys': 0,
            'files_with_modified_keys': 0,
            'total_missing_keys': 0,
            'total_modified_keys': 0
        }
    }

    # 완전히 새로운 파일 찾기
    for filename, new_keys in new_files.items():
        if filename not in existing_files:
            missing_data['new_files'].append({
                'filename': filename,
                'keys': new_keys,
                'key_count': len(new_keys)
            })
            missing_data['stats']['completely_new_files'] += 1
            missing_data['stats']['total_missing_keys'] += len(new_keys)

    # 기존 파일에서 누락/변경된 키 찾기
    for filename, new_keys in new_files.items():
        if filename in existing_files:
            existing_keys = existing_files[filename]

            missing = {}
            modified = {}

            for key, new_value in new_keys.items():
                if key not in existing_keys:
                    # 누락된 키
                    missing[key] = new_value
                elif existing_keys[key] != new_value:
                    # 값이 변경된 키
                    modified[key] = {
                        'old': existing_keys[key],
                        'new': new_value
                    }

            if missing:
                missing_data['missing_keys'][filename] = missing
                missing_data['stats']['files_with_missing_keys'] += 1
                missing_data['stats']['total_missing_keys'] += len(missing)

            if modified:
                missing_data['modified_keys'][filename] = modified
                missing_data['stats']['files_with_modified_keys'] += 1
                missing_data['stats']['total_modified_keys'] += len(modified)

    # 결과 출력
    print_comparison_summary(missing_data)

    # 결과 저장
    save_comparison_results(missing_data, project_root)

    return missing_data


def print_comparison_summary(data):
    """비교 결과 요약 출력"""
    stats = data['stats']

    print("\n" + "=" * 80)
    print("비교 결과 요약")
    print("=" * 80)
    print(f"\n새 추출본 파일 수: {stats['total_new_files']}개")
    print(f"기존 파일 수: {stats['total_existing_files']}개\n")
    print(f"🆕 완전히 새로운 파일: {stats['completely_new_files']}개")
    print(f"⚠️  누락된 키가 있는 파일: {stats['files_with_missing_keys']}개")
    print(f"📝 값이 변경된 키가 있는 파일: {stats['files_with_modified_keys']}개\n")
    print(f"총 누락된 키: {stats['total_missing_keys']}개")
    print(f"총 변경된 키: {stats['total_modified_keys']}개")

    if data['new_files']:
        print(f"\n완전히 새로운 파일 목록:")
        for file_info in data['new_files'][:10]:
            print(f"  - {file_info['filename']} ({file_info['key_count']}개 키)")
        if len(data['new_files']) > 10:
            print(f"  ... 외 {len(data['new_files']) - 10}개")

    if data['missing_keys']:
        print(f"\n누락된 키가 있는 파일:")
        for filename, keys in list(data['missing_keys'].items())[:10]:
            print(f"  - {filename} ({len(keys)}개 키 누락)")
        if len(data['missing_keys']) > 10:
            print(f"  ... 외 {len(data['missing_keys']) - 10}개")

    print("\n" + "=" * 80)


def save_comparison_results(data, base_dir):
    """비교 결과를 파일로 저장"""
    output_dir = base_dir / "missing_translations"
    output_dir.mkdir(exist_ok=True)

    # JSON 파일로 전체 데이터 저장
    json_file = output_dir / "missing_keys.json"
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"\n💾 상세 데이터 저장: {json_file}")

    # 번역 작업용 템플릿 생성
    template_file = output_dir / "translation_template.txt"
    with open(template_file, 'w', encoding='utf-8') as f:
        f.write("# " + "=" * 76 + "\n")
        f.write("# 번역 작업 템플릿\n")
        f.write(f"# 생성 일시: {datetime.now()}\n")
        f.write(f"# 추출본: {data['extraction_date']}\n")
        f.write("# " + "=" * 76 + "\n\n")

        # 새 파일들
        if data['new_files']:
            f.write(f"\n{'=' * 80}\n")
            f.write(f"완전히 새로운 파일 ({len(data['new_files'])}개)\n")
            f.write(f"{'=' * 80}\n\n")

            for file_info in data['new_files']:
                f.write(f"\n### 파일: {file_info['filename']} ###\n")
                f.write(f"# 총 {file_info['key_count']}개의 키\n\n")

                # 처음 5개만 샘플로 표시
                for i, (key, value) in enumerate(list(file_info['keys'].items())[:5], 1):
                    f.write(f"KEY: {key}\n")
                    f.write(f"ORIGINAL: {value}\n")
                    f.write(f"TRANSLATE: \n\n")

                if file_info['key_count'] > 5:
                    f.write(f"... 외 {file_info['key_count'] - 5}개의 키\n")
                    f.write(f"(전체 내용은 missing_keys.json 파일 참조)\n\n")

        # 누락된 키들
        if data['missing_keys']:
            f.write(f"\n{'=' * 80}\n")
            f.write(f"기존 파일에서 누락된 키 ({len(data['missing_keys'])}개 파일)\n")
            f.write(f"{'=' * 80}\n\n")

            for filename, keys in list(data['missing_keys'].items())[:10]:
                f.write(f"\n### 파일: {filename} ###\n")
                f.write(f"# 누락된 키: {len(keys)}개\n\n")

                for i, (key, value) in enumerate(list(keys.items())[:3], 1):
                    f.write(f"KEY: {key}\n")
                    f.write(f"ORIGINAL: {value}\n")
                    f.write(f"TRANSLATE: \n\n")

                if len(keys) > 3:
                    f.write(f"... 외 {len(keys) - 3}개의 키\n\n")

        # 변경된 키들
        if data['modified_keys']:
            f.write(f"\n{'=' * 80}\n")
            f.write(f"값이 변경된 키 ({len(data['modified_keys'])}개 파일)\n")
            f.write(f"{'=' * 80}\n\n")

            for filename, keys in list(data['modified_keys'].items())[:5]:
                f.write(f"\n### 파일: {filename} ###\n")
                f.write(f"# 변경된 키: {len(keys)}개\n\n")

                for i, (key, values) in enumerate(list(keys.items())[:3], 1):
                    f.write(f"KEY: {key}\n")
                    f.write(f"OLD: {values['old']}\n")
                    f.write(f"NEW: {values['new']}\n")
                    f.write(f"TRANSLATE: \n\n")

                if len(keys) > 3:
                    f.write(f"... 외 {len(keys) - 3}개의 키\n\n")

    print(f"📝 번역 템플릿 저장: {template_file}")

    print(f"\n다음 단계:")
    print(f"  1. {output_dir} 폴더의 파일들을 확인하세요")
    print(f"  2. translation_template.txt 또는 missing_keys.json을 사용하여 번역하세요")
    print(f"  3. 번역 완료 후 작업 4(번역본 병합)를 실행하세요")


def main():
    """메인 함수"""
    compare_with_existing()


if __name__ == "__main__":
    main()
