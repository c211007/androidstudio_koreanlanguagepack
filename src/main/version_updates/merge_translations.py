#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
번역 병합 스크립트

사용자가 번역한 누락 키들을 기존 번역 파일에 병합합니다.
"""

import os
import re
import json
import shutil
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
        print(f"[WARNING] 파일 읽기 오류: {filepath.name} - {e}")

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
        print(f"[ERROR] JSON 파일 읽기 오류: {e}")
        return None


def parse_plugin_xml(plugin_xml_path):
    """
    plugin.xml에서 등록된 resource-bundle 목록 추출

    Returns:
        set: 등록된 번들 이름 집합 (예: {'messages.ActionsBundle', 'messages.IdeBundle', ...})
    """
    import xml.etree.ElementTree as ET

    if not plugin_xml_path.exists():
        return set()

    try:
        tree = ET.parse(plugin_xml_path)
        root = tree.getroot()

        # <resource-bundle> 태그 찾기
        bundles = set()
        for bundle_elem in root.findall('.//resource-bundle'):
            bundle_name = bundle_elem.text
            if bundle_name:
                bundles.add(bundle_name.strip())

        return bundles

    except Exception as e:
        print(f"[WARNING] plugin.xml 파싱 오류: {e}")
        return set()


def get_bundles_from_messages_dir(messages_dir):
    """
    messages 디렉토리에서 모든 번들 파일 이름 수집

    Returns:
        set: 번들 이름 집합 (예: {'messages.ActionsBundle', 'messages.IdeBundle', ...})
    """
    bundles = set()

    # _ko.properties 파일들을 스캔
    for prop_file in messages_dir.glob("*_ko.properties"):
        # _ko.properties 제거하여 base name 생성
        base_name = prop_file.name.replace("_ko.properties", "")
        bundle_name = f"messages.{base_name}"
        bundles.add(bundle_name)

    # .properties 파일도 스캔 (아직 _ko로 변경 안 된 경우 대비)
    for prop_file in messages_dir.glob("*.properties"):
        # _ko.properties는 이미 위에서 처리했으므로 건너뛰기
        if prop_file.name.endswith("_ko.properties"):
            continue

        base_name = prop_file.name.replace(".properties", "")
        bundle_name = f"messages.{base_name}"
        bundles.add(bundle_name)

    return bundles


def update_plugin_xml(plugin_xml_path, missing_bundles, dry_run=False):
    """
    plugin.xml에 누락된 resource-bundle 추가

    Args:
        plugin_xml_path: plugin.xml 경로
        missing_bundles: 추가할 번들 이름 리스트
        dry_run: True면 실제 수정하지 않고 미리보기만

    Returns:
        bool: 성공 여부
    """
    if not missing_bundles:
        print("[OK] plugin.xml 업데이트 불필요 (모든 번들이 이미 등록됨)")
        return True

    print(f"\n{'=' * 80}")
    print("plugin.xml 업데이트")
    print(f"{'=' * 80}\n")

    print(f"추가할 번들: {len(missing_bundles)}개\n")

    for bundle in sorted(missing_bundles):
        print(f"  + {bundle}")

    if dry_run:
        print("\n[WARNING] DRY RUN 모드: 실제 수정하지 않습니다.")
        return True

    try:
        # XML 파일 읽기
        with open(plugin_xml_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # 삽입 위치 찾기
        # "<!-- Language bundle extension" 주석 바로 앞에 추가
        # 또는 마지막 </resource-bundle> 다음에 추가

        insert_marker = "<!-- Language bundle extension"

        if insert_marker in content:
            insert_pos = content.find(insert_marker)
        else:
            # 대체 방법: 마지막 </resource-bundle> 찾기
            last_bundle_end = content.rfind("</resource-bundle>")
            if last_bundle_end != -1:
                # </resource-bundle> 다음 줄에 삽입
                insert_pos = content.find("\n", last_bundle_end) + 1
            else:
                print("[ERROR] plugin.xml에서 삽입 위치를 찾을 수 없습니다.")
                return False

        # 새 번들 XML 생성
        # 기존 들여쓰기 스타일 맞추기 (4칸 스페이스)
        new_bundles_xml = ""
        for bundle in sorted(missing_bundles):
            new_bundles_xml += f"    <resource-bundle>{bundle}</resource-bundle>\n"

        # 주석 추가
        new_section = f"\n    <!-- Auto-added bundles - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} -->\n"
        new_section += new_bundles_xml

        # 삽입
        updated_content = content[:insert_pos] + new_section + content[insert_pos:]

        # 백업 생성
        backup_path = plugin_xml_path.parent / f"plugin.xml.backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        shutil.copy2(plugin_xml_path, backup_path)
        print(f"\n[*] 백업 생성: {backup_path.name}")

        # 파일 쓰기
        with open(plugin_xml_path, 'w', encoding='utf-8') as f:
            f.write(updated_content)

        print(f"[OK] plugin.xml 업데이트 완료: {len(missing_bundles)}개 번들 추가\n")
        return True

    except Exception as e:
        print(f"[ERROR] plugin.xml 업데이트 실패: {e}")
        return False


def check_and_update_plugin_xml(messages_dir, project_root, dry_run=False):
    """
    messages 디렉토리와 plugin.xml을 비교하여 누락된 번들을 업데이트

    Returns:
        bool: 성공 여부
    """
    plugin_xml_path = project_root / "src" / "main" / "resources" / "META-INF" / "plugin.xml"

    if not plugin_xml_path.exists():
        print(f"[ERROR] plugin.xml을 찾을 수 없습니다: {plugin_xml_path}")
        return False

    # 1. plugin.xml에서 등록된 번들 수집
    registered_bundles = parse_plugin_xml(plugin_xml_path)
    print(f"[*] plugin.xml 등록된 번들: {len(registered_bundles)}개")

    # 2. messages 디렉토리에서 실제 파일 수집
    actual_bundles = get_bundles_from_messages_dir(messages_dir)
    print(f"[*] messages 디렉토리 번들: {len(actual_bundles)}개")

    # 3. 누락된 번들 찾기
    missing_bundles = actual_bundles - registered_bundles

    if not missing_bundles:
        print("[OK] 모든 번들이 plugin.xml에 등록되어 있습니다.\n")
        return True

    print(f"\n[WARNING] plugin.xml에 누락된 번들: {len(missing_bundles)}개")

    # 4. plugin.xml 업데이트
    return update_plugin_xml(plugin_xml_path, missing_bundles, dry_run)


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
        print("[ERROR] missing_keys.json 파일을 찾을 수 없습니다.")
        print("   먼저 작업 3(Key 비교)를 실행하세요.")
        return False

    print(f"[*] 번역 데이터: {json_file}")

    # 번역 데이터 로드
    missing_data = load_translations_from_json(json_file)

    if not missing_data:
        print("[ERROR] 번역 데이터를 로드할 수 없습니다.")
        return False

    # messages 디렉토리
    messages_dir = project_root / "src" / "main" / "resources" / "messages"

    if not messages_dir.exists():
        print(f"[ERROR] messages 디렉토리를 찾을 수 없습니다: {messages_dir}")
        return False

    print(f"[*] 대상 디렉토리: {messages_dir}\n")

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

    print("[WARNING] 참고: 이 스크립트는 missing_keys.json의 원본(영어) 키를 추가합니다.")
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

        print(f"[NEW] 새 파일 생성: {ko_filename}")

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
            print(f"  [ERROR] 오류: {e}")
            stats['errors'] += 1

    # 기존 파일에 누락 키 추가
    for filename, missing_keys in missing_data.get('missing_keys', {}).items():
        # _ko.properties 파일명 생성
        if filename.endswith('.properties'):
            ko_filename = filename.replace('.properties', '_ko.properties')
        else:
            ko_filename = filename + '_ko.properties'

        target_file = messages_dir / ko_filename

        print(f"[UPDATE] 업데이트: {ko_filename} (+{len(missing_keys)}개 키)")

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
            print(f"  [ERROR] 오류: {e}")
            stats['errors'] += 1

    # 결과 출력
    print("\n" + "=" * 80)
    print("병합 완료")
    print("=" * 80)
    print(f"\n처리된 파일: {stats['files_processed']}개")
    print(f"생성된 파일: {stats['files_created']}개")
    print(f"추가된 키: {stats['keys_added']}개")
    print(f"오류: {stats['errors']}개\n")

    # ===== plugin.xml 자동 업데이트 =====
    # Auto-update plugin.xml
    print("\n" + "=" * 80)
    print("plugin.xml 확인 및 업데이트")
    print("=" * 80 + "\n")

    plugin_xml_updated = check_and_update_plugin_xml(messages_dir, project_root, dry_run=False)

    if not plugin_xml_updated:
        print("[WARNING] plugin.xml 업데이트 중 문제가 발생했습니다.")
        print("    수동으로 확인해주세요.")
    # ===== 끝 =====

    if stats['errors'] == 0 and plugin_xml_updated:
        print("[OK] 병합 및 plugin.xml 업데이트가 성공적으로 완료되었습니다.")
        return True
    elif stats['errors'] == 0:
        print("[OK] 병합 완료 (plugin.xml 업데이트는 수동 확인 필요)")
        return True
    else:
        print("[WARNING] 일부 오류가 발생했습니다.")
        return False


def main():
    """메인 함수"""
    merge_translations()


if __name__ == "__main__":
    main()
