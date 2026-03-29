#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
누락된 번역 키 추출 스크립트
Android Studio IDE에서 원본 properties를 재추출하고
현재 번역된 파일과 비교하여 누락된 키를 찾아 JSON으로 출력합니다.
"""

import os
import re
import json
from pathlib import Path
from collections import defaultdict


def parse_properties_file(filepath):
    """
    properties 파일을 파싱하여 key-value 쌍을 반환합니다.
    줄바꿈이 있는 값도 올바르게 처리합니다.

    Returns:
        dict: {key: value} 형식의 딕셔너리
    """
    properties = {}

    if not os.path.exists(filepath):
        return properties

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        i = 0
        while i < len(lines):
            line = lines[i].rstrip('\n\r')

            # 공백만 있는 줄이나 주석은 건너뛰기
            if not line.strip() or line.strip().startswith('#') or line.strip().startswith('!'):
                i += 1
                continue

            # key=value 형식 파싱
            match = re.match(r'^([^=:]+?)[\s]*[=:](.*)$', line)
            if match:
                key = match.group(1).strip()
                value = match.group(2)

                # 줄바꿈 처리: 백슬래시로 끝나면 다음 줄과 연결
                while value.rstrip().endswith('\\') and i + 1 < len(lines):
                    # 백슬래시 제거하고 다음 줄 추가
                    value = value.rstrip()[:-1]  # 마지막 백슬래시 제거
                    i += 1
                    next_line = lines[i].rstrip('\n\r')
                    value += '\n' + next_line

                properties[key] = value

            i += 1

    except Exception as e:
        print(f"⚠️  파일 읽기 오류: {filepath}")
        print(f"   에러: {e}")

    return properties


def find_source_directories():
    """
    원본 properties 파일이 있는 디렉토리들을 찾습니다.
    extracted_bundles 폴더 내의 intellij와 android 디렉토리를 검색합니다.
    """
    script_dir = Path(__file__).parent
    extracted_bundles = script_dir / 'extracted_bundles'

    source_dirs = []

    # intellij, android 등의 하위 폴더에서 messages 디렉토리 찾기
    if extracted_bundles.exists():
        for subdir in extracted_bundles.iterdir():
            if subdir.is_dir():
                messages_dir = subdir / 'messages'
                if messages_dir.exists():
                    source_dirs.append(messages_dir)

    return source_dirs


def extract_missing_keys():
    """
    원본 디렉토리들과 번역 디렉토리를 비교하여 누락된 키를 추출합니다.
    """
    script_dir = Path(__file__).parent
    translated_dir = script_dir / 'src' / 'main' / 'resources' / 'messages'

    print("\n" + "="*80)
    print("🔍 누락된 번역 키 추출 시작")
    print("="*80 + "\n")

    # 원본 디렉토리 찾기
    source_dirs = find_source_directories()

    if not source_dirs:
        print("❌ 오류: 원본 디렉토리를 찾을 수 없습니다.")
        print("   extracted_bundles 폴더를 확인하세요.")
        return None

    print(f"📂 원본 디렉토리 ({len(source_dirs)}개):")
    for src_dir in source_dirs:
        print(f"   - {src_dir}")
    print(f"\n📂 번역 디렉토리: {translated_dir}\n")

    # 모든 원본 파일 수집
    all_source_files = {}
    for source_dir in source_dirs:
        for filepath in source_dir.glob('*.properties'):
            filename = filepath.name

            # 이미 다른 소스에서 발견한 파일이면 병합
            if filename in all_source_files:
                existing_keys = all_source_files[filename]
                new_keys = parse_properties_file(filepath)
                # 기존 키와 새 키 병합 (새 키가 우선)
                existing_keys.update(new_keys)
            else:
                all_source_files[filename] = parse_properties_file(filepath)

    print(f"✅ 원본 파일 발견: {len(all_source_files)}개\n")

    # 번역 파일 수집
    translated_files = {}
    if translated_dir.exists():
        for filepath in translated_dir.glob('*.properties'):
            filename = filepath.name
            translated_files[filename] = parse_properties_file(filepath)

    print(f"✅ 번역 파일 발견: {len(translated_files)}개\n")

    # 누락된 키 찾기
    missing_data = {
        'new_files': [],      # 아예 번역되지 않은 파일
        'missing_keys': {},   # 각 파일별 누락된 키-값 쌍
        'stats': {
            'total_source_files': len(all_source_files),
            'total_translated_files': len(translated_files),
            'new_files_count': 0,
            'files_with_missing_keys': 0,
            'total_missing_keys': 0
        }
    }

    # 번역되지 않은 새 파일 찾기
    for filename in all_source_files:
        if filename not in translated_files:
            source_keys = all_source_files[filename]
            missing_data['new_files'].append({
                'filename': filename,
                'keys': source_keys,
                'key_count': len(source_keys)
            })
            missing_data['stats']['new_files_count'] += 1
            missing_data['stats']['total_missing_keys'] += len(source_keys)

    # 기존 파일에서 누락된 키 찾기
    for filename in all_source_files:
        if filename in translated_files:
            source_keys = all_source_files[filename]
            translated_keys = translated_files[filename]

            # 누락된 키 찾기
            missing_keys = {}
            for key, value in source_keys.items():
                if key not in translated_keys:
                    missing_keys[key] = value

            if missing_keys:
                missing_data['missing_keys'][filename] = missing_keys
                missing_data['stats']['files_with_missing_keys'] += 1
                missing_data['stats']['total_missing_keys'] += len(missing_keys)

    return missing_data


def save_missing_keys_json(missing_data, output_file):
    """
    누락된 키 데이터를 JSON 파일로 저장합니다.
    """
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(missing_data, f, ensure_ascii=False, indent=2)

    print(f"\n💾 누락된 키 데이터가 저장되었습니다: {output_file}")


def save_translation_template(missing_data, output_file):
    """
    번역 작업을 위한 템플릿 파일을 생성합니다.
    사용자가 번역하기 쉽도록 포맷팅된 파일을 생성합니다.
    """
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("# " + "="*76 + "\n")
        f.write("# 번역 작업 템플릿\n")
        f.write("# " + "="*76 + "\n")
        f.write("# 이 파일은 누락된 번역 키들을 번역하기 위한 템플릿입니다.\n")
        f.write("# \n")
        f.write("# 작업 방법:\n")
        f.write("# 1. 각 키의 원본 값(영어)을 확인합니다\n")
        f.write("# 2. 'TRANSLATE:' 뒤에 한국어 번역을 작성합니다\n")
        f.write("# 3. 번역 완료 후 apply_translations.py를 실행합니다\n")
        f.write("# \n")
        f.write("# 주의사항:\n")
        f.write("# - {0}, {1} 같은 플레이스홀더는 그대로 유지하세요\n")
        f.write("# - _X 같은 단축키 표시는 한국어 뒤 괄호에 넣으세요 (예: 복사(_C))\n")
        f.write("# - ... (말줄임표)는 유지하세요\n")
        f.write("# - 특수문자는 백슬래시로 이스케이프하세요 (예: \\:, \\=)\n")
        f.write("# " + "="*76 + "\n\n")

        # 새 파일들
        if missing_data['new_files']:
            f.write(f"\n{'='*80}\n")
            f.write(f"새로 추가된 파일 ({len(missing_data['new_files'])}개)\n")
            f.write(f"{'='*80}\n\n")

            for file_info in missing_data['new_files']:
                f.write(f"\n### 파일: {file_info['filename']} ###\n")
                f.write(f"# 총 {file_info['key_count']}개의 키\n\n")

                for key, value in list(file_info['keys'].items())[:5]:  # 처음 5개만 샘플로
                    f.write(f"KEY: {key}\n")
                    f.write(f"ORIGINAL: {value}\n")
                    f.write(f"TRANSLATE: \n\n")

                if file_info['key_count'] > 5:
                    f.write(f"... 외 {file_info['key_count'] - 5}개의 키\n")
                    f.write(f"(전체 내용은 missing_keys.json 파일을 참조하세요)\n\n")

        # 누락된 키들
        if missing_data['missing_keys']:
            f.write(f"\n{'='*80}\n")
            f.write(f"기존 파일에서 누락된 키 ({len(missing_data['missing_keys'])}개 파일)\n")
            f.write(f"{'='*80}\n\n")

            for filename, keys in list(missing_data['missing_keys'].items())[:10]:  # 처음 10개 파일만
                f.write(f"\n### 파일: {filename} ###\n")
                f.write(f"# 누락된 키: {len(keys)}개\n\n")

                for key, value in list(keys.items())[:3]:  # 각 파일당 3개씩만 샘플로
                    f.write(f"KEY: {key}\n")
                    f.write(f"ORIGINAL: {value}\n")
                    f.write(f"TRANSLATE: \n\n")

                if len(keys) > 3:
                    f.write(f"... 외 {len(keys) - 3}개의 키\n\n")

    print(f"📝 번역 템플릿이 생성되었습니다: {output_file}")


def print_summary(missing_data):
    """
    추출 결과 요약을 출력합니다.
    """
    stats = missing_data['stats']

    print("\n" + "="*80)
    print("📊 추출 결과 요약")
    print("="*80)
    print(f"\n원본 파일 수: {stats['total_source_files']}개")
    print(f"번역 파일 수: {stats['total_translated_files']}개")
    print(f"\n🆕 새로 추가된 파일: {stats['new_files_count']}개")
    print(f"⚠️  누락된 키가 있는 파일: {stats['files_with_missing_keys']}개")
    print(f"📝 총 누락된 키: {stats['total_missing_keys']}개")

    if stats['new_files_count'] > 0:
        print(f"\n새로 추가된 파일 목록:")
        for file_info in missing_data['new_files'][:10]:
            print(f"  - {file_info['filename']} ({file_info['key_count']}개 키)")
        if len(missing_data['new_files']) > 10:
            print(f"  ... 외 {len(missing_data['new_files']) - 10}개")

    if stats['files_with_missing_keys'] > 0:
        print(f"\n누락된 키가 있는 파일 목록:")
        for filename, keys in list(missing_data['missing_keys'].items())[:10]:
            print(f"  - {filename} ({len(keys)}개 키 누락)")
        if len(missing_data['missing_keys']) > 10:
            print(f"  ... 외 {len(missing_data['missing_keys']) - 10}개")

    print("\n" + "="*80)
    print("\n다음 단계:")
    print("1. translation_template.txt 파일을 열어서 번역을 진행하세요")
    print("2. 또는 missing_keys.json 파일을 직접 편집하세요")
    print("3. 번역 완료 후 apply_translations.py를 실행하세요")
    print("="*80 + "\n")


def main():
    """
    메인 함수
    """
    script_dir = Path(__file__).parent

    # 누락된 키 추출
    missing_data = extract_missing_keys()

    if missing_data is None:
        return

    # 결과 요약 출력
    print_summary(missing_data)

    # JSON 파일로 저장
    json_file = script_dir / 'missing_keys.json'
    save_missing_keys_json(missing_data, json_file)

    # 번역 템플릿 생성
    template_file = script_dir / 'translation_template.txt'
    save_translation_template(missing_data, template_file)

    print(f"✅ 작업 완료!")


if __name__ == '__main__':
    main()
