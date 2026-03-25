#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Android Studio 한국어 번역 플러그인 워크플로우 관리자

전체 번역 작업 프로세스를 관리하는 통합 스크립트입니다.
"""

import os
import sys
import importlib.util
from pathlib import Path

# 프로젝트 루트 및 스크립트 경로 설정
SCRIPT_DIR = Path(__file__).parent  # src/main/version_updates 폴더
PROJECT_ROOT = SCRIPT_DIR.parent.parent.parent  # 프로젝트 루트


def load_module_from_file(module_name, file_path):
    """파일에서 모듈을 동적으로 로드"""
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module


def print_header(title):
    """헤더 출력"""
    print("\n" + "=" * 80)
    print(f"  {title}")
    print("=" * 80 + "\n")


def print_menu():
    """메뉴 출력"""
    print_header("Android Studio 한국어 번역 플러그인 워크플로우")
    print("다음 작업을 선택하세요:\n")
    print("  1. Android Studio 버전 확인 및 플러그인 버전 수정")
    print("  2. Android Studio에서 Properties Key 재추출")
    print("  3. 재추출한 Key와 기존 Key 비교 및 차이점 확인")
    print("  4. 번역본 백업 후 병합")
    print("  5. 이전 백업으로 롤백")
    print("  0. 종료")
    print("\n" + "=" * 80)


def task_check_version():
    """작업 1: Android Studio 버전 확인 및 플러그인 버전 수정"""
    print_header("작업 1: Android Studio 버전 확인")

    try:
        # check_version 모듈 로드 (version_updates 폴더 내부)
        check_version_path = SCRIPT_DIR / "check_version.py"
        check_version = load_module_from_file("check_version", check_version_path)

        # 사용자에게 선택지 제공
        print("Android Studio 경로 선택:")
        print("  1. 자동으로 찾기")
        print("  2. 직접 경로 입력")
        print("\n선택 (1-2): ", end="")

        choice = input().strip()
        studio_path = None

        if choice == '1':
            # 자동으로 찾기
            print("\n🔍 Android Studio 경로를 자동으로 검색 중...")
            auto_path = check_version.find_android_studio_path()

            if auto_path:
                print(f"✅ 발견: {auto_path}")
                print("\n이 경로를 사용하시겠습니까? (y/n): ", end="")
                confirm = input().strip().lower()

                if confirm == 'y':
                    studio_path = auto_path
                else:
                    print("\n직접 경로를 입력하세요.")
            else:
                print("❌ 자동으로 찾을 수 없습니다.")
                print("\n직접 경로를 입력하세요.")

        # 자동 검색 실패하거나 선택 2번인 경우 수동 입력
        if studio_path is None:
            print("\nAndroid Studio 설치 경로를 입력하세요:")
            print("\n경로 입력 예시:")
            print("  Windows: C:\\Program Files\\Android\\Android Studio")
            print("  macOS:   /Applications/Android Studio.app")
            print("  Linux:   /opt/android-studio")
            print("\n경로: ", end="")

            input_path = input().strip()

            if not input_path:
                print("❌ 경로가 입력되지 않았습니다.")
                return

            studio_path = Path(input_path)

        # 경로 유효성 확인
        if not studio_path.exists():
            print(f"❌ 경로를 찾을 수 없습니다: {studio_path}")
            return

        # 버전 확인 실행
        check_version.main(studio_path)

        # 버전 업데이트 옵션
        print("\n플러그인 버전을 업데이트하시겠습니까? (y/n): ", end="")
        choice = input().strip().lower()

        if choice == 'y':
            update_plugin_version_path = SCRIPT_DIR / "update_plugin_version.py"
            update_plugin_version = load_module_from_file("update_plugin_version", update_plugin_version_path)
            update_plugin_version.main()

        print("\n✅ 작업 1 완료!")

    except Exception as e:
        print(f"\n❌ 오류 발생: {e}")
        import traceback
        traceback.print_exc()


def task_extract_keys():
    """작업 2: Android Studio에서 Properties Key 재추출"""
    print_header("작업 2: Properties Key 재추출")

    try:
        # extract_from_studio 모듈 로드
        extract_from_studio_path = SCRIPT_DIR / "extract_from_studio.py"
        extract_from_studio = load_module_from_file("extract_from_studio", extract_from_studio_path)

        # 사용자에게 선택지 제공
        print("Android Studio 경로 선택:")
        print("  1. 자동으로 찾기")
        print("  2. 직접 경로 입력")
        print("\n선택 (1-2): ", end="")

        choice = input().strip()
        studio_path = None

        if choice == '1':
            # 자동으로 찾기
            print("\n🔍 Android Studio 경로를 자동으로 검색 중...")
            auto_path = extract_from_studio.find_android_studio_path()

            if auto_path:
                print(f"✅ 발견: {auto_path}")
                print("\n이 경로를 사용하시겠습니까? (y/n): ", end="")
                confirm = input().strip().lower()

                if confirm == 'y':
                    studio_path = auto_path
                else:
                    print("\n직접 경로를 입력하세요.")
            else:
                print("❌ 자동으로 찾을 수 없습니다.")
                print("\n직접 경로를 입력하세요.")

        # 자동 검색 실패하거나 선택 2번인 경우 수동 입력
        if studio_path is None:
            print("\nAndroid Studio 설치 경로를 입력하세요:")
            print("\n경로 입력 예시:")
            print("  Windows: C:\\Program Files\\Android\\Android Studio")
            print("  macOS:   /Applications/Android Studio.app")
            print("  Linux:   /opt/android-studio")
            print("\n경로: ", end="")

            input_path = input().strip()

            if not input_path:
                print("❌ 경로가 입력되지 않았습니다.")
                return

            studio_path = Path(input_path)

        # 경로 유효성 확인
        if not studio_path.exists():
            print(f"❌ 경로를 찾을 수 없습니다: {studio_path}")
            return

        # 추출 실행
        extract_from_studio.extract_from_android_studio(studio_path)

        print("\n✅ 작업 2 완료!")

    except Exception as e:
        print(f"\n❌ 오류 발생: {e}")
        import traceback
        traceback.print_exc()


def task_compare_keys():
    """작업 3: 재추출한 Key와 기존 Key 비교"""
    print_header("작업 3: Key 비교 및 차이점 확인")

    try:
        # compare_extracted_keys 모듈 로드
        compare_extracted_keys_path = SCRIPT_DIR / "compare_extracted_keys.py"
        compare_extracted_keys = load_module_from_file("compare_extracted_keys", compare_extracted_keys_path)

        # 비교 실행
        compare_extracted_keys.main()

        print("\n✅ 작업 3 완료!")
        print("\n다음 단계:")
        print("  1. missing_translations 폴더의 파일들을 확인하세요")
        print("  2. 누락된 키들을 번역하세요")
        print("  3. 번역 완료 후 작업 4를 실행하세요")

    except Exception as e:
        print(f"\n❌ 오류 발생: {e}")
        import traceback
        traceback.print_exc()


def task_merge_translations():
    """작업 4: 번역본 백업 후 병합"""
    print_header("작업 4: 번역본 병합")

    try:
        # backup_manager와 merge_translations 모듈 로드
        backup_manager_path = SCRIPT_DIR / "backup_manager.py"
        backup_manager = load_module_from_file("backup_manager", backup_manager_path)

        merge_translations_path = SCRIPT_DIR / "merge_translations.py"
        merge_translations = load_module_from_file("merge_translations", merge_translations_path)

        # 현재 플러그인 확인
        messages_dir = PROJECT_ROOT / "src" / "main" / "resources" / "messages"
        if not messages_dir.exists():
            print(f"❌ messages 디렉토리를 찾을 수 없습니다: {messages_dir}")
            return

        print("⚠️  주의: 이 작업은 현재 번역 파일을 수정합니다.")
        print("\n현재 플러그인이 Android Studio에 제대로 적용되어 있습니까?")
        print("(플러그인을 설치하고 테스트한 후 진행하세요)")
        print("\n계속하시겠습니까? (yes/no): ", end="")

        confirm = input().strip().lower()
        if confirm != 'yes':
            print("❌ 작업이 취소되었습니다.")
            return

        # 백업 생성
        print("\n백업 생성 중...")
        backup_path = backup_manager.create_backup()
        print(f"✅ 백업 완료: {backup_path}")

        # 번역 병합
        print("\n번역 병합 중...")
        merge_translations.main()

        print("\n✅ 작업 4 완료!")
        print(f"\n백업 위치: {backup_path}")
        print("문제가 있을 경우 작업 5(롤백)를 실행하세요.")

    except Exception as e:
        print(f"\n❌ 오류 발생: {e}")
        print("백업이 생성되었다면 작업 5(롤백)를 실행하세요.")
        import traceback
        traceback.print_exc()


def task_rollback():
    """작업 5: 이전 백업으로 롤백"""
    print_header("작업 5: 백업 롤백")

    try:
        # backup_manager 모듈 로드
        backup_manager_path = SCRIPT_DIR / "backup_manager.py"
        backup_manager = load_module_from_file("backup_manager", backup_manager_path)

        # 백업 목록 확인
        backups = backup_manager.list_backups()

        if not backups:
            print("❌ 사용 가능한 백업이 없습니다.")
            return

        print("사용 가능한 백업 목록:\n")
        for i, backup in enumerate(backups, 1):
            print(f"  {i}. {backup['name']} ({backup['date']})")

        print("\n롤백할 백업 번호를 선택하세요 (0: 취소): ", end="")
        choice = input().strip()

        try:
            choice = int(choice)
            if choice == 0:
                print("❌ 작업이 취소되었습니다.")
                return

            if choice < 1 or choice > len(backups):
                print("❌ 잘못된 선택입니다.")
                return

            selected_backup = backups[choice - 1]

            print(f"\n⚠️  '{selected_backup['name']}' 백업으로 복원하시겠습니까?")
            print("현재 파일들은 모두 덮어씌워집니다.")
            print("\n계속하시겠습니까? (yes/no): ", end="")

            confirm = input().strip().lower()
            if confirm != 'yes':
                print("❌ 작업이 취소되었습니다.")
                return

            # 롤백 실행
            backup_manager.restore_backup(selected_backup['path'])

            print("\n✅ 작업 5 완료!")
            print("파일들이 복원되었습니다.")

        except ValueError:
            print("❌ 숫자를 입력하세요.")

    except Exception as e:
        print(f"\n❌ 오류 발생: {e}")
        import traceback
        traceback.print_exc()


def main():
    """메인 함수"""
    while True:
        try:
            print_menu()
            choice = input("선택 (0-5): ").strip()

            if choice == '0':
                print("\n프로그램을 종료합니다.")
                break
            elif choice == '1':
                task_check_version()
            elif choice == '2':
                task_extract_keys()
            elif choice == '3':
                task_compare_keys()
            elif choice == '4':
                task_merge_translations()
            elif choice == '5':
                task_rollback()
            else:
                print("\n❌ 잘못된 선택입니다. 0-5 사이의 숫자를 입력하세요.")

            input("\n계속하려면 Enter를 누르세요...")

        except KeyboardInterrupt:
            print("\n\n프로그램을 종료합니다.")
            break
        except Exception as e:
            print(f"\n❌ 예상치 못한 오류: {e}")
            import traceback
            traceback.print_exc()
            input("\n계속하려면 Enter를 누르세요...")


if __name__ == '__main__':
    main()
