#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
번역 병합 스크립트

사용자가 번역한 누락 키들을 기존 번역 파일에 병합합니다.
"""

import os
import re
import json
from pathlib import Path
from datetime import datetime


def parse_properties_file(filepath):
    """Properties 파일 파싱 (키-값 쌍 및 원본 라인 유지)"""
    properties = {}
    lines = []

    if not filepath.exists():
        return properties, lines

    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            lines = content.split('\n')

        i = 0
        while i < len(lines):
            line = lines[i].rstrip('\r')

            # 주석이나 빈 줄
            if not line.strip() or line.strip().startswith('#') or line.strip().startswith('!'):
                i += 1
                continue

            # key=value 파싱
            match = re.match(r'^([^=:]+?)[\s]*[=:](.*)$', line)
            if match:
                key = match.group(1).strip()
                value = match.group(2)

                # 줄바꿈 처리
                full_value = value
                line_start = i
                while value.rstrip().endswith('\\') and i + 1 < len(lines):
                    i += 1
                    next_line = lines[i].rstrip('\r')
                    full_value += '\n' + next_line

                properties[key] = full_value

            i += 1

    except Exception as e:
        print(f"⚠️  파일 읽기 오류: {filepath.name} - {e}")

    return properties, lines


def load_translations_from_json(json_path):
    """JSON 파일에서 번역 데이터 로드"""
    if not json_path.exists():
        return None

    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    except Exception as e:
        print(f"❌ JSON 파일 읽기 오류: {e}")
        return None


def merge_translations():
    """번역 병합 수행"""
    project_root = Path(__file__).parent.parent.parent.parent  # src/main/version_updates → main → src → root

    print("\n" + "=" * 80)
    print("번역 병합")
    print("=" * 80 + "\n")

    # missing_translations 폴더에서 데이터 로드
    missing_dir = project_root / "missing_translations"
    json_file = missing_dir / "missing_keys.json"

    if not json_file.exists():
        print("❌ missing_keys.json 파일을 찾을 수 없습니다.")
        print("   먼저 작업 3(Key 비교)를 실행하세요.")
        return False

    print(f"📂 번역 데이터: {json_file}")

    # 번역 데이터 로드
    missing_data = load_translations_from_json(json_file)

    if not missing_data:
        print("❌ 번역 데이터를 로드할 수 없습니다.")
        return False

    # messages 디렉토리
    messages_dir = project_root / "src" / "main" / "resources" / "messages"

    if not messages_dir.exists():
        print(f"❌ messages 디렉토리를 찾을 수 없습니다: {messages_dir}")
        return False

    print(f"📂 대상 디렉토리: {messages_dir}\n")

    # 통계
    stats = {
        'files_processed': 0,
        'keys_added': 0,
        'files_created': 0,
        'errors': 0
    }

    # 사용자가 번역한 파일이 있는지 확인
    # 여기서는 단순히 missing_keys.json의 데이터를 병합
    # 실제로는 사용자가 translated_keys.json 같은 파일을 만들어야 함

    print("⚠️  참고: 이 스크립트는 missing_keys.json의 원본(영어) 키를 추가합니다.")
    print("실제 번역본을 병합하려면 translated_keys.json 파일을 만들어야 합니다.\n")

    # 새 파일 생성
    for file_info in missing_data.get('new_files', []):
        filename = file_info['filename']

        # _ko.properties 파일명 생성
        if filename.endswith('.properties'):
            ko_filename = filename.replace('.properties', '_ko.properties')
        else:
            ko_filename = filename + '_ko.properties'

        target_file = messages_dir / ko_filename

        print(f"🆕 새 파일 생성: {ko_filename}")

        try:
            with open(target_file, 'w', encoding='utf-8') as f:
                f.write(f"# Auto-generated Korean translation file\n")
                f.write(f"# Generated: {datetime.now()}\n")
                f.write(f"# Original file: {filename}\n\n")

                for key, value in file_info['keys'].items():
                    # 여기서는 원본 값을 그대로 사용
                    # 실제로는 번역된 값을 사용해야 함
                    f.write(f"{key}={value}\n")

            stats['files_created'] += 1
            stats['keys_added'] += len(file_info['keys'])

        except Exception as e:
            print(f"  ❌ 오류: {e}")
            stats['errors'] += 1

    # 기존 파일에 누락 키 추가
    for filename, missing_keys in missing_data.get('missing_keys', {}).items():
        # _ko.properties 파일명 생성
        if filename.endswith('.properties'):
            ko_filename = filename.replace('.properties', '_ko.properties')
        else:
            ko_filename = filename + '_ko.properties'

        target_file = messages_dir / ko_filename

        print(f"📝 업데이트: {ko_filename} (+{len(missing_keys)}개 키)")

        try:
            # 기존 파일 읽기 (없으면 빈 딕셔너리)
            existing_props = {}
            if target_file.exists():
                existing_props, _ = parse_properties_file(target_file)

            # 누락된 키 추가
            with open(target_file, 'a', encoding='utf-8') as f:
                if not target_file.exists() or target_file.stat().st_size == 0:
                    f.write(f"# Korean translation file\n")
                    f.write(f"# Updated: {datetime.now()}\n\n")

                f.write(f"\n# Added missing keys - {datetime.now()}\n")

                for key, value in missing_keys.items():
                    if key not in existing_props:
                        # 여기서는 원본 값을 그대로 사용
                        # 실제로는 번역된 값을 사용해야 함
                        f.write(f"{key}={value}\n")
                        stats['keys_added'] += 1

            stats['files_processed'] += 1

        except Exception as e:
            print(f"  ❌ 오류: {e}")
            stats['errors'] += 1

    # 결과 출력
    print("\n" + "=" * 80)
    print("병합 완료")
    print("=" * 80)
    print(f"\n처리된 파일: {stats['files_processed']}개")
    print(f"생성된 파일: {stats['files_created']}개")
    print(f"추가된 키: {stats['keys_added']}개")
    print(f"오류: {stats['errors']}개\n")

    if stats['errors'] == 0:
        print("✅ 병합 작업이 성공적으로 완료되었습니다.")
        return True
    else:
        print("⚠️  일부 오류가 발생했습니다.")
        return False


def main():
    """메인 함수"""
    merge_translations()


if __name__ == "__main__":
    main()
