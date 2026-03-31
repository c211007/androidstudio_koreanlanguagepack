#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Android Studio에서 직접 Properties 파일 추출

사용자가 지정한 Android Studio 설치 경로에서 properties 파일을 추출하고
임시 디렉토리에 저장합니다.
"""

import os
import zipfile
import shutil
import platform
import re
from pathlib import Path
from datetime import datetime


def is_english_base_file(filename):
    """
    Check if a properties file is an English base file (no language suffix).

    Returns True only for base files like 'ActionsBundle.properties'
    Returns False for language-specific files like:
    - ActionsBundle_ja.properties (Japanese)
    - ActionsBundle_zh_CN.properties (Chinese Simplified)
    - ActionsBundle_zh_TW.properties (Chinese Traditional)
    - ActionsBundle_ko.properties (Korean)
    - ActionsBundle_en.properties (English explicit)
    """
    # Language suffix patterns to exclude
    language_suffixes = [
        '_ja',      # Japanese
        '_zh_CN',   # Chinese Simplified
        '_zh_TW',   # Chinese Traditional
        '_zh_HK',   # Chinese Hong Kong
        '_ko',      # Korean
        '_kr',      # Korean (alternative)
        '_en',      # English (explicit)
        '_fr',      # French
        '_de',      # German
        '_es',      # Spanish
        '_pt',      # Portuguese
        '_ru',      # Russian
        '_it',      # Italian
    ]

    # Check if filename ends with any language suffix before .properties
    filename_lower = filename.lower()
    for suffix in language_suffixes:
        if filename_lower.endswith(suffix + '.properties'):
            return False

    # Also check for pattern _XX.properties or _XX_YY.properties
    # where XX is 2 lowercase letters and YY is 2 uppercase letters
    pattern = r'_[a-z]{2}(_[A-Z]{2})?\.properties$'
    if re.search(pattern, filename):
        return False

    return True


def find_android_studio_path():
    """Android Studio 설치 경로 자동 검색"""
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


def find_jar_files(directory):
    """디렉토리에서 jar 파일 재귀적으로 찾기"""
    jar_files = []

    print(f"📂 JAR 파일 검색 중: {directory}")

    try:
        for root, dirs, files in os.walk(directory):
            # 불필요한 디렉토리 제외
            dirs[:] = [d for d in dirs if not d.startswith('.')]

            for file in files:
                if file.endswith('.jar'):
                    jar_files.append(Path(root) / file)

        return jar_files

    except Exception as e:
        print(f"⚠️  디렉토리 검색 중 오류: {e}")
        return []


def extract_properties_from_jar(jar_path, output_dir, verbose=False):
    """JAR 파일에서 properties 파일 추출"""
    extracted_count = 0

    try:
        with zipfile.ZipFile(jar_path, 'r') as jar:
            all_files = jar.namelist()

            # properties 파일만 필터링
            properties_files = [
                f for f in all_files
                if f.endswith('.properties') and 'messages/' in f
            ]

            if not properties_files:
                return 0

            # 추출
            for prop_file in properties_files:
                filename = Path(prop_file).name

                # ONLY include English base files (no language suffix)
                if not is_english_base_file(filename):
                    if verbose:
                        print(f"  ⊘ Skipped (non-English): {filename}")
                    continue

                output_path = output_dir / filename

                # 파일이 이미 존재하면 건너뛰기 (중복 방지)
                if output_path.exists():
                    # 크기가 더 큰 파일로 교체
                    existing_size = output_path.stat().st_size
                    content = jar.read(prop_file)
                    if len(content) > existing_size:
                        with open(output_path, 'wb') as f:
                            f.write(content)
                        if verbose:
                            print(f"  ↻ {filename} (업데이트: {len(content)} bytes)")
                else:
                    content = jar.read(prop_file)
                    with open(output_path, 'wb') as f:
                        f.write(content)
                    if verbose:
                        print(f"  ✓ {filename} ({len(content)} bytes)")

                extracted_count += 1

    except zipfile.BadZipFile:
        if verbose:
            print(f"  ✗ 손상된 JAR: {jar_path.name}")
    except Exception as e:
        if verbose:
            print(f"  ✗ 오류: {jar_path.name} - {e}")

    return extracted_count


def extract_from_android_studio(studio_path, verbose=True):
    """Android Studio 설치 경로에서 properties 추출"""
    studio_path = Path(studio_path)

    if not studio_path.exists():
        print(f"❌ Android Studio 경로를 찾을 수 없습니다: {studio_path}")
        return None

    print("\n" + "=" * 80)
    print("Android Studio Properties 추출")
    print("=" * 80 + "\n")

    print(f"📍 Android Studio 경로: {studio_path}\n")

    # 출력 디렉토리 생성 (타임스탬프 포함)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    project_root = Path(__file__).parent.parent.parent.parent  # src/main/version_updates → main → src → root
    output_base = project_root / "temp_extracted"
    output_dir = output_base / f"studio_{timestamp}"
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"📁 출력 디렉토리: {output_dir}\n")

    # JAR 파일 찾기
    jar_files = find_jar_files(studio_path)

    if not jar_files:
        print("❌ JAR 파일을 찾을 수 없습니다.")
        return None

    print(f"✅ {len(jar_files)}개의 JAR 파일 발견\n")

    # 각 JAR에서 properties 추출
    total_extracted = 0
    processed_jars = 0

    print("🔍 Properties 파일 추출 중...\n")

    for i, jar_path in enumerate(jar_files, 1):
        if verbose:
            print(f"[{i}/{len(jar_files)}] {jar_path.name}")

        extracted = extract_properties_from_jar(jar_path, output_dir, verbose)

        if extracted > 0:
            total_extracted += extracted
            processed_jars += 1

        if verbose and extracted > 0:
            print()

    # 결과 요약
    print("\n" + "=" * 80)
    print("추출 완료")
    print("=" * 80)
    print(f"\n검색한 JAR 파일: {len(jar_files)}개")
    print(f"Properties가 포함된 JAR: {processed_jars}개")
    print(f"추출된 Properties 파일: {len(list(output_dir.glob('*.properties')))}개")
    print(f"\n📁 출력 위치: {output_dir}\n")

    # 추출된 파일 목록 저장
    file_list_path = output_dir / "_extracted_files.txt"
    with open(file_list_path, 'w', encoding='utf-8') as f:
        f.write(f"추출 일시: {datetime.now()}\n")
        f.write(f"Android Studio 경로: {studio_path}\n")
        f.write(f"추출된 파일 수: {len(list(output_dir.glob('*.properties')))}\n")
        f.write("\n추출된 파일 목록:\n")
        f.write("=" * 60 + "\n")

        for prop_file in sorted(output_dir.glob('*.properties')):
            size = prop_file.stat().st_size
            f.write(f"{prop_file.name:50s} {size:>10,} bytes\n")

    print(f"📄 파일 목록 저장: {file_list_path}")

    return output_dir


def main():
    """메인 함수"""
    import sys

    if len(sys.argv) > 1:
        studio_path = sys.argv[1]
    else:
        print("Android Studio 설치 경로를 입력하세요:")
        print("(예: C:\\Program Files\\Android\\Android Studio)")
        print("\n경로: ", end="")
        studio_path = input().strip()

    if not studio_path:
        print("❌ 경로가 입력되지 않았습니다.")
        return

    extract_from_android_studio(studio_path)


if __name__ == "__main__":
    main()
