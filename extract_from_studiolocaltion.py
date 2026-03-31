#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Android Studio IntelliJ Platform에서 Properties 파일 추출

.intellijPlatform\ides\AI-2025.3.2.6\android-studio 경로에서
properties 파일을 추출하고 루트 폴더의 pro_location에 저장합니다.
각 properties 파일 맨 위에 원본 경로를 주석으로 추가합니다.
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


def extract_properties_from_jar(jar_path, output_dir, relative_jar_path, verbose=False):
    """JAR 파일에서 properties 파일 추출하고 경로 주석 추가"""
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

                # JAR 파일 내부의 전체 경로
                full_path = f"{relative_jar_path}!/{prop_file}"
                
                # 원본 내용 읽기
                content = jar.read(prop_file)
                
                # UTF-8로 디코딩
                try:
                    content_text = content.decode('utf-8')
                except UnicodeDecodeError:
                    try:
                        content_text = content.decode('iso-8859-1')
                    except:
                        content_text = content.decode('utf-8', errors='ignore')
                
                # 경로 주석 추가
                header_comment = f"# Original path: {full_path}\n# Extracted on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
                final_content = header_comment + content_text

                # 파일이 이미 존재하면 크기 비교
                if output_path.exists():
                    existing_size = output_path.stat().st_size
                    if len(final_content.encode('utf-8')) > existing_size:
                        with open(output_path, 'w', encoding='utf-8') as f:
                            f.write(final_content)
                        if verbose:
                            print(f"  ↻ {filename} (업데이트: {len(content)} bytes)")
                else:
                    with open(output_path, 'w', encoding='utf-8') as f:
                        f.write(final_content)
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


def extract_from_intellij_platform(verbose=True):
    """IntelliJ Platform 경로에서 properties 추출"""
    # 프로젝트 루트 경로
    project_root = Path(__file__).parent
    
    # IntelliJ Platform 경로
    # platform_path = project_root / ".intellijPlatform" / "ides" / "AI-2025.3.2.6" / "android-studio"
    platform_path = Path("C:/Program Files/Android/Android Studio")
    if not platform_path.exists():
        print(f"❌ IntelliJ Platform 경로를 찾을 수 없습니다: {platform_path}")
        return None

    print("\n" + "=" * 80)
    print("Android Studio IntelliJ Platform Properties 추출")
    print("=" * 80 + "\n")

    print(f"📍 Platform 경로: {platform_path}\n")

    # 출력 디렉토리 생성
    output_dir = project_root / "pro_location"
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"📁 출력 디렉토리: {output_dir}\n")

    # JAR 파일 찾기
    jar_files = find_jar_files(platform_path)

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

        # JAR 파일의 상대 경로 계산
        try:
            relative_jar_path = jar_path.relative_to(project_root)
        except ValueError:
            relative_jar_path = jar_path

        extracted = extract_properties_from_jar(jar_path, output_dir, str(relative_jar_path), verbose)

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
        f.write(f"Platform 경로: {platform_path}\n")
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
    extract_from_intellij_platform(verbose=True)


if __name__ == "__main__":
    main()
