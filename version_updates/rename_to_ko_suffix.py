#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
기존 Properties 파일 이름을 _ko 접미사로 변경

messages/ 디렉토리의 모든 .properties 파일을 _ko.properties로 변경합니다.
예: ActionsBundle.properties → ActionsBundle_ko.properties
"""

import os
from pathlib import Path
import shutil
from datetime import datetime


def rename_files_to_ko_suffix(dry_run=True):
    """
    messages 디렉토리의 파일들을 _ko 접미사로 변경

    Args:
        dry_run: True이면 실제 변경하지 않고 미리보기만 수행
    """
    project_root = Path(__file__).parent.parent.parent.parent
    messages_dir = project_root / "src" / "main" / "resources" / "messages"

    if not messages_dir.exists():
        print(f"ERROR: messages 디렉토리를 찾을 수 없습니다: {messages_dir}")
        return False

    print("\n" + "=" * 80)
    print("Properties 파일 이름 변경: _ko 접미사 추가")
    print("=" * 80 + "\n")

    if dry_run:
        print("[DRY RUN] 실제 변경하지 않고 미리보기만 수행합니다.\n")

    # original 디렉토리는 제외
    files_to_rename = []

    for prop_file in messages_dir.glob("*.properties"):
        # 이미 _ko.properties로 끝나는 파일은 건너뛰기
        if prop_file.name.endswith("_ko.properties"):
            continue

        # 새 파일명 생성
        new_name = prop_file.name.replace(".properties", "_ko.properties")
        new_path = messages_dir / new_name

        files_to_rename.append((prop_file, new_path))

    if not files_to_rename:
        print("OK: 변경할 파일이 없습니다. 모든 파일이 이미 _ko 접미사를 가지고 있습니다.")
        return True

    print(f"[*] 대상 디렉토리: {messages_dir}")
    print(f"[*] 변경할 파일 수: {len(files_to_rename)}개\n")

    # 파일 목록 출력 (처음 10개만)
    print("변경될 파일 목록:")
    for i, (old_path, new_path) in enumerate(files_to_rename[:10], 1):
        print(f"  {i}. {old_path.name} → {new_path.name}")

    if len(files_to_rename) > 10:
        print(f"  ... 외 {len(files_to_rename) - 10}개 파일\n")
    else:
        print()

    # 충돌 검사
    conflicts = []
    for old_path, new_path in files_to_rename:
        if new_path.exists():
            conflicts.append((old_path.name, new_path.name))

    if conflicts:
        print("ERROR: 파일명 충돌 발견:")
        for old, new in conflicts:
            print(f"  - {old} -> {new} (이미 존재함)")
        print("\n충돌을 해결한 후 다시 실행하세요.")
        return False

    if dry_run:
        print("OK: DRY RUN 완료: 충돌 없음, 변경 준비 완료")
        print("\n실제 변경을 수행하려면 --execute 플래그로 다시 실행하세요.")
        return True

    # 실제 변경 수행
    print("[*] 파일 이름 변경 중...\n")

    success_count = 0
    error_count = 0

    for old_path, new_path in files_to_rename:
        try:
            old_path.rename(new_path)
            print(f"  [OK] {old_path.name} -> {new_path.name}")
            success_count += 1
        except Exception as e:
            print(f"  [ERROR] {old_path.name}: {e}")
            error_count += 1

    # 결과 요약
    print("\n" + "=" * 80)
    print("변경 완료")
    print("=" * 80)
    print(f"\n성공: {success_count}개")
    print(f"실패: {error_count}개")

    if error_count == 0:
        print("\n[OK] 모든 파일이 성공적으로 변경되었습니다.")

        # 백업 로그 생성
        log_file = messages_dir / f"_rename_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        with open(log_file, 'w', encoding='utf-8') as f:
            f.write(f"파일 이름 변경 로그\n")
            f.write(f"일시: {datetime.now()}\n")
            f.write(f"변경된 파일 수: {success_count}\n\n")

            for old_path, new_path in files_to_rename:
                f.write(f"{old_path.name} -> {new_path.name}\n")

        print(f"[*] 변경 로그 저장: {log_file.name}")
        return True
    else:
        print("\n[WARNING] 일부 파일 변경 중 오류가 발생했습니다.")
        return False


def main():
    """메인 함수"""
    import sys

    dry_run = True

    if len(sys.argv) > 1 and sys.argv[1] == "--execute":
        dry_run = False

    rename_files_to_ko_suffix(dry_run)

    if dry_run:
        print("\n" + "=" * 80)
        print("실제 변경을 수행하려면:")
        print("  python rename_to_ko_suffix.py --execute")
        print("=" * 80)


if __name__ == "__main__":
    main()
