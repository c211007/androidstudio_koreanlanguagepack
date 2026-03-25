#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
번역 적용 스크립트
extract_missing_keys.py에서 추출한 누락된 키들을 번역한 후
이 스크립트를 실행하면 해당 번역을 properties 파일에 자동으로 적용합니다.
"""

import os
import re
import json
from pathlib import Path
from datetime import datetime


class PropertiesUpdater:
    """
    Properties 파일을 업데이트하는 클래스
    """

    def __init__(self, messages_dir):
        self.messages_dir = Path(messages_dir)
        self.backup_dir = self.messages_dir.parent.parent.parent / 'translation_backups'
        self.stats = {
            'files_created': 0,
            'files_updated': 0,
            'keys_added': 0,
            'errors': []
        }

    def create_backup(self, filepath):
        """
        파일 백업 생성
        """
        if not filepath.exists():
            return

        # 백업 디렉토리 생성
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        backup_subdir = self.backup_dir / timestamp
        backup_subdir.mkdir(parents=True, exist_ok=True)

        # 파일 백업
        backup_file = backup_subdir / filepath.name
        import shutil
        shutil.copy2(filepath, backup_file)
        print(f"   💾 백업 생성: {backup_file}")

    def read_properties_with_structure(self, filepath):
        """
        Properties 파일을 읽되, 주석과 빈 줄 등 구조를 유지합니다.

        Returns:
            list: 각 줄의 정보를 담은 리스트 [{type, content, key, value}, ...]
        """
        lines_info = []

        if not filepath.exists():
            return lines_info

        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                lines = f.readlines()

            i = 0
            while i < len(lines):
                line = lines[i]
                stripped = line.strip()

                # 빈 줄
                if not stripped:
                    lines_info.append({'type': 'empty', 'content': line})
                    i += 1
                    continue

                # 주석
                if stripped.startswith('#') or stripped.startswith('!'):
                    lines_info.append({'type': 'comment', 'content': line})
                    i += 1
                    continue

                # key=value 파싱
                match = re.match(r'^([^=:]+?)[\s]*[=:](.*)$', line.rstrip('\n\r'))
                if match:
                    key = match.group(1).strip()
                    value = match.group(2)

                    # 여러 줄에 걸친 value 처리
                    full_value = value
                    original_lines = [line]

                    while full_value.rstrip().endswith('\\') and i + 1 < len(lines):
                        i += 1
                        next_line = lines[i]
                        original_lines.append(next_line)
                        full_value += '\n' + next_line.rstrip('\n\r')

                    lines_info.append({
                        'type': 'property',
                        'content': ''.join(original_lines),
                        'key': key,
                        'value': full_value
                    })
                else:
                    # 파싱 실패한 줄은 그대로 유지
                    lines_info.append({'type': 'unknown', 'content': line})

                i += 1

        except Exception as e:
            print(f"⚠️  파일 읽기 오류: {filepath}")
            print(f"   에러: {e}")

        return lines_info

    def format_property_line(self, key, value):
        """
        key-value를 properties 파일 형식으로 포맷팅합니다.
        여러 줄 값은 백슬래시로 연결합니다.
        """
        # 값이 여러 줄인 경우
        if '\n' in value:
            lines = value.split('\n')
            # 마지막 줄을 제외하고 각 줄 끝에 백슬래시 추가
            formatted_lines = []
            for i, line in enumerate(lines):
                if i < len(lines) - 1:
                    # 마지막이 아닌 줄: 백슬래시 추가
                    formatted_lines.append(line.rstrip() + ' \\')
                else:
                    # 마지막 줄
                    formatted_lines.append(line.rstrip())
            return f"{key}={formatted_lines[0]}\n" + '\n'.join(formatted_lines[1:]) + '\n'
        else:
            return f"{key}={value}\n"

    def update_properties_file(self, filename, new_keys):
        """
        Properties 파일을 업데이트하거나 새로 생성합니다.

        Args:
            filename: 파일 이름
            new_keys: {key: value} 형식의 딕셔너리
        """
        filepath = self.messages_dir / filename
        file_existed = filepath.exists()

        try:
            if file_existed:
                # 기존 파일 업데이트
                self.create_backup(filepath)
                lines_info = self.read_properties_with_structure(filepath)

                # 기존 키 목록
                existing_keys = {
                    line['key'] for line in lines_info
                    if line['type'] == 'property'
                }

                # 새로운 키만 추가
                keys_to_add = {
                    k: v for k, v in new_keys.items()
                    if k not in existing_keys
                }

                if not keys_to_add:
                    print(f"   ℹ️  {filename}: 이미 모든 키가 존재합니다.")
                    return

                # 파일 쓰기
                with open(filepath, 'a', encoding='utf-8') as f:
                    # 파일 끝에 빈 줄 추가 (구분을 위해)
                    f.write('\n')
                    f.write('# ─────────────────────────────────────────────────────────────\n')
                    f.write(f'# 자동 추가된 번역 ({datetime.now().strftime("%Y-%m-%d %H:%M:%S")})\n')
                    f.write('# ─────────────────────────────────────────────────────────────\n')

                    for key, value in keys_to_add.items():
                        f.write(self.format_property_line(key, value))

                self.stats['files_updated'] += 1
                self.stats['keys_added'] += len(keys_to_add)
                print(f"   ✅ {filename}: {len(keys_to_add)}개 키 추가됨")

            else:
                # 새 파일 생성
                self.messages_dir.mkdir(parents=True, exist_ok=True)

                with open(filepath, 'w', encoding='utf-8') as f:
                    # 파일 헤더 작성
                    f.write('# ' + '═'*77 + '\n')
                    f.write(f'# {filename[:-11]}Bundle - Korean Translation\n')
                    f.write('# Android Studio 한국어 언어팩\n')
                    f.write('# ' + '═'*77 + '\n')
                    f.write(f'# 생성일: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n')
                    f.write('# 자동 생성된 파일입니다.\n')
                    f.write('# ' + '═'*77 + '\n\n')

                    # 키-값 쓰기
                    for key, value in new_keys.items():
                        f.write(self.format_property_line(key, value))

                self.stats['files_created'] += 1
                self.stats['keys_added'] += len(new_keys)
                print(f"   🆕 {filename}: 새 파일 생성 ({len(new_keys)}개 키)")

        except Exception as e:
            error_msg = f"{filename}: {str(e)}"
            self.stats['errors'].append(error_msg)
            print(f"   ❌ 오류: {error_msg}")

    def apply_translations(self, missing_keys_data):
        """
        missing_keys.json 형식의 데이터를 받아서 번역을 적용합니다.

        Args:
            missing_keys_data: extract_missing_keys.py가 생성한 JSON 데이터
        """
        print("\n" + "="*80)
        print("📝 번역 적용 시작")
        print("="*80 + "\n")

        # 새 파일들 처리
        if missing_keys_data.get('new_files'):
            print(f"🆕 새 파일 처리 중... ({len(missing_keys_data['new_files'])}개)\n")
            for file_info in missing_keys_data['new_files']:
                filename = file_info['filename']
                keys = file_info['keys']
                self.update_properties_file(filename, keys)

        # 누락된 키들 처리
        if missing_keys_data.get('missing_keys'):
            print(f"\n⚠️  누락된 키 처리 중... ({len(missing_keys_data['missing_keys'])}개 파일)\n")
            for filename, keys in missing_keys_data['missing_keys'].items():
                self.update_properties_file(filename, keys)

        # 결과 요약
        self.print_stats()

    def print_stats(self):
        """
        작업 통계 출력
        """
        print("\n" + "="*80)
        print("📊 작업 완료 통계")
        print("="*80)
        print(f"\n✅ 새로 생성된 파일: {self.stats['files_created']}개")
        print(f"✅ 업데이트된 파일: {self.stats['files_updated']}개")
        print(f"✅ 추가된 키: {self.stats['keys_added']}개")

        if self.stats['errors']:
            print(f"\n❌ 오류 발생: {len(self.stats['errors'])}건")
            for error in self.stats['errors']:
                print(f"   - {error}")

        if self.stats['files_updated'] > 0:
            print(f"\n💾 백업 위치: {self.backup_dir}")

        print("\n" + "="*80 + "\n")


def load_translations_from_json(json_file):
    """
    JSON 파일에서 번역 데이터를 로드합니다.
    """
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        print(f"❌ 오류: {json_file} 파일을 찾을 수 없습니다.")
        print("   extract_missing_keys.py를 먼저 실행하세요.")
        return None
    except json.JSONDecodeError as e:
        print(f"❌ 오류: JSON 파일 파싱 실패")
        print(f"   {e}")
        return None


def load_translations_from_template(template_file):
    """
    translation_template.txt 파일에서 번역 데이터를 로드합니다.

    파일 형식:
    KEY: action.Something.text
    ORIGINAL: Some text
    TRANSLATE: 번역된 텍스트
    """
    translations = {
        'new_files': [],
        'missing_keys': {}
    }

    current_file = None
    current_key = None
    current_original = None

    try:
        with open(template_file, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.rstrip('\n')

                # 파일 섹션 구분
                if line.startswith('### 파일:'):
                    match = re.search(r'### 파일: (.+?) ###', line)
                    if match:
                        current_file = match.group(1).strip()

                # KEY 라인
                elif line.startswith('KEY:'):
                    current_key = line[4:].strip()

                # ORIGINAL 라인
                elif line.startswith('ORIGINAL:'):
                    current_original = line[9:].strip()

                # TRANSLATE 라인
                elif line.startswith('TRANSLATE:'):
                    translation = line[10:].strip()

                    # 번역이 입력되었으면 추가
                    if translation and current_file and current_key:
                        if current_file not in translations['missing_keys']:
                            translations['missing_keys'][current_file] = {}

                        translations['missing_keys'][current_file][current_key] = translation

                    # 초기화
                    current_key = None
                    current_original = None

    except FileNotFoundError:
        print(f"❌ 오류: {template_file} 파일을 찾을 수 없습니다.")
        return None

    return translations


def main():
    """
    메인 함수
    """
    script_dir = Path(__file__).parent
    messages_dir = script_dir / 'src' / 'main' / 'resources' / 'messages'
    json_file = script_dir / 'missing_keys.json'
    template_file = script_dir / 'translation_template.txt'

    print("\n" + "="*80)
    print("🌏 번역 적용 스크립트")
    print("="*80)

    # 어떤 파일을 사용할지 선택
    print("\n번역 데이터를 로드할 파일을 선택하세요:")
    print("1. missing_keys.json (JSON 파일 직접 편집한 경우)")
    print("2. translation_template.txt (템플릿 파일에서 번역한 경우)")

    # 기본값: JSON 파일 사용
    choice = input("\n선택 (1 또는 2, 기본값=1): ").strip() or "1"

    if choice == "2":
        print(f"\n📖 템플릿 파일 로드 중: {template_file}")
        translations = load_translations_from_template(template_file)
    else:
        print(f"\n📖 JSON 파일 로드 중: {json_file}")
        translations = load_translations_from_json(json_file)

    if translations is None:
        return

    # 번역 데이터 확인
    total_keys = sum(
        len(keys) for keys in translations.get('missing_keys', {}).values()
    )
    if translations.get('new_files'):
        total_keys += sum(
            file_info.get('key_count', len(file_info.get('keys', {})))
            for file_info in translations['new_files']
        )

    if total_keys == 0:
        print("\n⚠️  번역된 키가 없습니다.")
        print("   번역을 완료한 후 다시 실행하세요.")
        return

    print(f"\n✅ 번역 데이터 로드 완료: 총 {total_keys}개 키")

    # 확인
    confirm = input("\n번역을 적용하시겠습니까? (y/N): ").strip().lower()
    if confirm != 'y':
        print("❌ 취소되었습니다.")
        return

    # 번역 적용
    updater = PropertiesUpdater(messages_dir)
    updater.apply_translations(translations)

    print("✨ 모든 작업이 완료되었습니다!")
    print("\n다음 단계:")
    print("1. 플러그인을 빌드하고 테스트하세요")
    print("2. check_translation_keys.py로 번역 상태를 확인하세요")


if __name__ == '__main__':
    main()
