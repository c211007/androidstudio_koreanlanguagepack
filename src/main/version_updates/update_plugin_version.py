#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
플러그인 버전 업데이트 스크립트

gradle.properties 파일의 플러그인 버전 정보를 업데이트합니다.
"""

import os
import re
from pathlib import Path


def read_gradle_properties():
    """gradle.properties 파일 읽기"""
    # version_updates 폴더에서 프로젝트 루트로 이동 (3단계 위)
    project_root = Path(__file__).parent.parent.parent.parent
    gradle_file = project_root / "gradle.properties"

    if not gradle_file.exists():
        return None, None

    properties = {}
    lines = []

    with open(gradle_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    for line in lines:
        line = line.strip()
        if '=' in line and not line.startswith('#'):
            key, value = line.split('=', 1)
            properties[key.strip()] = value.strip()

    return properties, lines


def update_gradle_properties(updates):
    """gradle.properties 파일 업데이트"""
    # version_updates 폴더에서 프로젝트 루트로 이동 (3단계 위)
    project_root = Path(__file__).parent.parent.parent.parent
    gradle_file = project_root / "gradle.properties"

    if not gradle_file.exists():
        print(f"❌ gradle.properties 파일을 찾을 수 없습니다.")
        return False

    properties, lines = read_gradle_properties()

    if not properties:
        print("❌ gradle.properties 파일을 읽을 수 없습니다.")
        return False

    # 새 내용 생성
    new_lines = []
    updated_keys = set()

    for line in lines:
        line_stripped = line.strip()
        updated = False

        for key, new_value in updates.items():
            if line_stripped.startswith(key + '='):
                old_value = properties.get(key, '')
                new_lines.append(f"{key}={new_value}\n")
                updated_keys.add(key)
                updated = True
                print(f"  {key}: {old_value} → {new_value}")
                break

        if not updated:
            new_lines.append(line)

    # 업데이트되지 않은 키 추가
    for key, new_value in updates.items():
        if key not in updated_keys:
            new_lines.append(f"{key}={new_value}\n")
            print(f"  {key}: (새로 추가) → {new_value}")

    # 파일 쓰기
    try:
        with open(gradle_file, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)

        print(f"\n✅ gradle.properties 파일이 업데이트되었습니다.")
        return True

    except Exception as e:
        print(f"❌ 파일 쓰기 오류: {e}")
        return False


def calculate_platform_version(major_build):
    """
    major build number로부터 platform version 계산

    Args:
        major_build: 빌드 번호의 major 부분 (예: "242")

    Returns:
        str: platform version (예: "2024.2")
    """
    try:
        build_num = int(major_build)

        # 빌드 번호 패턴: YYX 형식
        # 예: 242 → 2024.2, 241 → 2024.1, 233 → 2023.3
        year_part = build_num // 10  # 24
        version_part = build_num % 10  # 2

        year = 2000 + year_part  # 2024

        return f"{year}.{version_part}"
    except:
        return None


def increment_patch_version(current_version):
    """
    플러그인 버전의 패치 번호 증가

    Args:
        current_version: 현재 버전 (예: "1.0.5")

    Returns:
        str: 증가된 버전 (예: "1.0.6")
    """
    try:
        parts = current_version.split('.')
        if len(parts) >= 3:
            major, minor, patch = parts[0], parts[1], parts[2]
            new_patch = int(patch) + 1
            return f"{major}.{minor}.{new_patch}"
        else:
            # 패치가 없으면 .1 추가
            return f"{current_version}.1"
    except:
        return current_version


def auto_update_from_studio_version(studio_version_info):
    """
    Android Studio 버전 정보로부터 자동으로 gradle.properties 업데이트

    Args:
        studio_version_info: check_version.main()에서 반환된 버전 정보 딕셔너리

    Returns:
        bool: 성공 여부
    """
    print("\n" + "=" * 80)
    print("플러그인 버전 자동 업데이트")
    print("=" * 80 + "\n")

    if not studio_version_info:
        print("❌ 버전 정보가 없습니다.")
        return False

    studio_version = studio_version_info.get('studio_version')
    plugin_version = studio_version_info.get('plugin_version')
    parsed_build = studio_version_info.get('parsed_build')

    if not studio_version or not parsed_build:
        print("❌ Android Studio 버전 정보를 파싱할 수 없습니다.")
        return False

    # 버전 정보 계산
    major_build = parsed_build.get('majorBuild')

    if not major_build:
        print("❌ 빌드 번호를 파싱할 수 없습니다.")
        return False

    # platformVersion 계산
    platform_version = calculate_platform_version(major_build)

    if not platform_version:
        print("❌ 플랫폼 버전을 계산할 수 없습니다.")
        return False

    # pluginSinceBuild: major build 사용
    plugin_since_build = major_build

    # pluginUntilBuild: major build.* 형식
    plugin_until_build = f"{major_build}.*"

    # pluginVersion: 패치 버전 증가
    current_plugin_version = plugin_version.get('pluginVersion', '1.0.0')
    new_plugin_version = increment_patch_version(current_plugin_version)

    print("Android Studio 버전 정보:")
    print(f"  버전: {studio_version.get('version', 'N/A')}")
    print(f"  빌드 번호: {studio_version.get('buildNumber', 'N/A')}")
    print(f"  Major Build: {major_build}")
    print()

    print("자동 계산된 플러그인 설정:")
    print(f"  platformVersion: {platform_version}")
    print(f"  pluginSinceBuild: {plugin_since_build}")
    print(f"  pluginUntilBuild: {plugin_until_build}")
    print(f"  pluginVersion: {current_plugin_version} → {new_plugin_version}")
    print()

    # 업데이트할 항목
    updates = {
        'platformVersion': platform_version,
        'pluginSinceBuild': plugin_since_build,
        'pluginUntilBuild': plugin_until_build,
        'pluginVersion': new_plugin_version
    }

    print("다음 항목이 업데이트됩니다:")
    for key, value in updates.items():
        old_value = plugin_version.get(key.replace('plugin', '').replace('platform', 'platform'), 'N/A')
        if key == 'platformVersion':
            old_value = plugin_version.get('platformVersion', 'N/A')
        elif key == 'pluginVersion':
            old_value = plugin_version.get('pluginVersion', 'N/A')
        elif key == 'pluginSinceBuild':
            old_value = plugin_version.get('sinceBuild', 'N/A')

        print(f"  {key}: {old_value} → {value}")

    print("\n이 설정으로 업데이트하시겠습니까? (y/n): ", end="")
    confirm = input().strip().lower()

    if confirm == 'y':
        print()
        return update_gradle_properties(updates)
    else:
        print("\n취소되었습니다.")
        return False


def main():
    """메인 함수"""
    print("\n" + "=" * 80)
    print("플러그인 버전 업데이트")
    print("=" * 80 + "\n")

    properties, _ = read_gradle_properties()

    if not properties:
        print("❌ gradle.properties 파일을 읽을 수 없습니다.")
        return

    print("현재 설정:")
    print(f"  platformVersion: {properties.get('platformVersion', 'N/A')}")
    print(f"  pluginVersion: {properties.get('pluginVersion', 'N/A')}")
    print(f"  pluginSinceBuild: {properties.get('pluginSinceBuild', 'N/A')}")
    print(f"  pluginUntilBuild: {properties.get('pluginUntilBuild', 'N/A')}")

    print("\n업데이트할 항목을 선택하세요:")
    print("  1. platformVersion (IntelliJ 플랫폼 버전)")
    print("  2. pluginVersion (플러그인 버전)")
    print("  3. pluginSinceBuild (최소 지원 빌드)")
    print("  4. pluginUntilBuild (최대 지원 빌드)")
    print("  5. 전체 업데이트")
    print("  0. 취소")

    choice = input("\n선택 (0-5): ").strip()

    updates = {}

    if choice == '0':
        print("취소되었습니다.")
        return

    if choice == '1' or choice == '5':
        new_value = input(f"새 platformVersion (현재: {properties.get('platformVersion', '')}): ").strip()
        if new_value:
            updates['platformVersion'] = new_value

    if choice == '2' or choice == '5':
        new_value = input(f"새 pluginVersion (현재: {properties.get('pluginVersion', '')}): ").strip()
        if new_value:
            updates['pluginVersion'] = new_value

    if choice == '3' or choice == '5':
        new_value = input(f"새 pluginSinceBuild (현재: {properties.get('pluginSinceBuild', '')}): ").strip()
        if new_value:
            updates['pluginSinceBuild'] = new_value

    if choice == '4' or choice == '5':
        new_value = input(f"새 pluginUntilBuild (현재: {properties.get('pluginUntilBuild', '')}): ").strip()
        if new_value:
            updates['pluginUntilBuild'] = new_value

    if not updates:
        print("\n변경 사항이 없습니다.")
        return

    print("\n다음 항목이 업데이트됩니다:")
    for key, value in updates.items():
        print(f"  {key} = {value}")

    confirm = input("\n계속하시겠습니까? (y/n): ").strip().lower()

    if confirm == 'y':
        print()
        update_gradle_properties(updates)
    else:
        print("\n취소되었습니다.")


if __name__ == "__main__":
    main()
