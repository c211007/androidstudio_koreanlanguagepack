#!/usr/bin/env python3
"""
Android Studio 버전 확인 스크립트

Android Studio 설치 경로에서 현재 버전을 확인하고,
현재 프로젝트가 지원하는 버전과 비교합니다.
"""

import os
import json
import re
from pathlib import Path
import platform


def find_android_studio_path():
    """Android Studio 설치 경로 찾기"""
    system = platform.system()

    common_paths = []
    if system == "Windows":
        common_paths = [
            Path(os.environ.get("ProgramFiles", "C:\\Program Files")) / "Android" / "Android Studio",
            Path(os.environ.get("ProgramFiles(x86)", "C:\\Program Files (x86)")) / "Android" / "Android Studio",
            Path(os.environ.get("LOCALAPPDATA", "")) / "Programs" / "Android Studio",
        ]
    elif system == "Darwin":  # macOS
        common_paths = [
            Path("/Applications/Android Studio.app"),
            Path.home() / "Applications" / "Android Studio.app",
        ]
    elif system == "Linux":
        common_paths = [
            Path("/opt/android-studio"),
            Path.home() / "android-studio",
            Path("/usr/local/android-studio"),
        ]

    for path in common_paths:
        if path.exists():
            return path

    return None


def get_version_from_build_txt(studio_path):
    """build.txt 파일에서 버전 정보 읽기"""
    build_file = studio_path / "build.txt"

    if not build_file.exists():
        # macOS의 경우 다른 경로
        build_file = studio_path / "Contents" / "Resources" / "build.txt"

    if build_file.exists():
        with open(build_file, 'r') as f:
            build_number = f.read().strip()
            return build_number

    return None


def get_version_from_product_info(studio_path):
    """product-info.json에서 버전 정보 읽기 (최신 버전)"""
    product_info = studio_path / "product-info.json"

    if not product_info.exists():
        # macOS의 경우
        product_info = studio_path / "Contents" / "Resources" / "product-info.json"

    if product_info.exists():
        with open(product_info, 'r') as f:
            data = json.load(f)
            return {
                'version': data.get('version'),
                'buildNumber': data.get('buildNumber'),
                'versionSuffix': data.get('versionSuffix', ''),
                'productCode': data.get('productCode'),
            }

    return None


def get_current_plugin_version():
    """현재 플러그인이 지원하는 버전 확인 (gradle.properties)"""
    gradle_props = Path("gradle.properties")

    if not gradle_props.exists():
        return None

    version_info = {}
    with open(gradle_props, 'r') as f:
        for line in f:
            line = line.strip()
            if line.startswith('platformVersion'):
                version_info['platformVersion'] = line.split('=')[1].strip()
            elif line.startswith('pluginSinceBuild'):
                version_info['sinceBuild'] = line.split('=')[1].strip()
            elif line.startswith('pluginVersion'):
                version_info['pluginVersion'] = line.split('=')[1].strip()

    return version_info


def parse_build_number(build_number):
    """빌드 번호 파싱 (예: AI-242.21829.142.2421.12550806)"""
    # 형식: <Product Code>-<Build Number>.<Patch>
    parts = build_number.split('-')
    if len(parts) >= 2:
        product_code = parts[0]
        build_parts = parts[1].split('.')
        return {
            'productCode': product_code,
            'majorBuild': build_parts[0] if len(build_parts) > 0 else None,
            'minorBuild': build_parts[1] if len(build_parts) > 1 else None,
            'full': build_number
        }
    return None


def check_compatibility(studio_version, plugin_version):
    """버전 호환성 확인"""
    if not studio_version or not plugin_version:
        return None

    studio_build = parse_build_number(studio_version.get('buildNumber', ''))
    plugin_since = plugin_version.get('sinceBuild', '')

    if studio_build and plugin_since:
        studio_major = studio_build.get('majorBuild')
        if studio_major and plugin_since:
            if studio_major >= plugin_since:
                return True
            else:
                return False

    return None


def main():
    print("=" * 80)
    print("Android Studio 버전 확인")
    print("=" * 80)
    print()

    # Android Studio 설치 경로 찾기
    studio_path = find_android_studio_path()

    if not studio_path:
        print("❌ Android Studio를 찾을 수 없습니다.")
        print("   수동으로 설치 경로를 지정하세요.")
        return

    print(f"✓ Android Studio 경로: {studio_path}")
    print()

    # 버전 정보 가져오기
    studio_version = get_version_from_product_info(studio_path)

    if not studio_version:
        build_number = get_version_from_build_txt(studio_path)
        if build_number:
            studio_version = {'buildNumber': build_number}

    if studio_version:
        print("설치된 Android Studio 버전:")
        print(f"  버전: {studio_version.get('version', 'N/A')}")
        print(f"  빌드: {studio_version.get('buildNumber', 'N/A')}")
        if studio_version.get('versionSuffix'):
            print(f"  타입: {studio_version.get('versionSuffix')}")
        print()
    else:
        print("❌ 버전 정보를 가져올 수 없습니다.")
        return

    # 현재 플러그인 버전 확인
    plugin_version = get_current_plugin_version()

    if plugin_version:
        print("현재 플러그인 지원 버전:")
        print(f"  플랫폼 버전: {plugin_version.get('platformVersion', 'N/A')}")
        print(f"  최소 빌드: {plugin_version.get('sinceBuild', 'N/A')}")
        print(f"  플러그인 버전: {plugin_version.get('pluginVersion', 'N/A')}")
        print()
    else:
        print("❌ 플러그인 버전 정보를 가져올 수 없습니다.")
        return

    # 호환성 확인
    compatible = check_compatibility(studio_version, plugin_version)

    print("호환성 확인:")
    if compatible is True:
        print("  ✅ 호환됨 - 현재 플러그인을 사용할 수 있습니다.")
    elif compatible is False:
        print("  ⚠️  호환되지 않음 - 플러그인 업데이트가 필요할 수 있습니다.")
    else:
        print("  ❓ 확인 불가 - 수동으로 호환성을 확인하세요.")

    print()

    # 버전 업데이트 폴더 확인
    version_folder = Path("version_updates/android_studio")
    build_number = studio_version.get('buildNumber', '')
    parsed = parse_build_number(build_number)

    if parsed:
        version_string = studio_version.get('version', parsed['majorBuild'])
        version_dir = version_folder / version_string

        print(f"버전 폴더 확인:")
        if version_dir.exists():
            print(f"  ✓ 폴더 존재: {version_dir}")
            # 폴더 내용 확인
            files = list(version_dir.iterdir())
            if files:
                print(f"  파일 수: {len(files)}")
        else:
            print(f"  ℹ️  폴더 없음: {version_dir}")
            print(f"     새 버전 추출이 필요할 수 있습니다.")

    print()
    print("=" * 80)


if __name__ == "__main__":
    main()
