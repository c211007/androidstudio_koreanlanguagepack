#!/usr/bin/env python3
"""
JAR 파일에서 Properties 파일 추출 스크립트

Android Studio나 플러그인의 jar 파일에서 properties 파일을 추출합니다.
"""

import os
import zipfile
import shutil
from pathlib import Path
import argparse


def find_jar_files(directory, pattern="*.jar"):
    """디렉토리에서 jar 파일 찾기"""
    jar_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.jar'):
                jar_files.append(Path(root) / file)
    return jar_files


def extract_properties_from_jar(jar_path, output_dir, verbose=False):
    """jar 파일에서 properties 파일 추출"""
    extracted_files = []

    try:
        with zipfile.ZipFile(jar_path, 'r') as jar:
            # jar 내의 모든 파일 목록
            all_files = jar.namelist()

            # properties 파일만 필터링
            properties_files = [f for f in all_files if f.endswith('.properties')]

            if not properties_files:
                return extracted_files

            # 추출
            for prop_file in properties_files:
                # messages/ 폴더 안의 파일만 추출
                if 'messages/' in prop_file:
                    # 파일명만 추출 (경로 제거)
                    filename = Path(prop_file).name

                    # 출력 경로
                    output_path = output_dir / filename

                    # 파일 내용 읽기
                    content = jar.read(prop_file)

                    # 파일 쓰기
                    with open(output_path, 'wb') as f:
                        f.write(content)

                    extracted_files.append((jar_path.name, filename, len(content)))

                    if verbose:
                        print(f"  ✓ {filename} ({len(content)} bytes)")

    except zipfile.BadZipFile:
        if verbose:
            print(f"  ✗ 손상된 jar 파일: {jar_path.name}")
    except Exception as e:
        if verbose:
            print(f"  ✗ 오류: {jar_path.name} - {e}")

    return extracted_files


def extract_from_directory(source_dir, output_dir, verbose=False):
    """디렉토리의 모든 jar 파일에서 properties 추출"""
    print(f"소스 디렉토리: {source_dir}")
    print(f"출력 디렉토리: {output_dir}")
    print()

    # 출력 디렉토리 생성
    output_dir.mkdir(parents=True, exist_ok=True)

    # jar 파일 찾기
    print("JAR 파일 검색 중...")
    jar_files = find_jar_files(source_dir)

    if not jar_files:
        print("❌ jar 파일을 찾을 수 없습니다.")
        return

    print(f"✓ {len(jar_files)}개의 jar 파일을 찾았습니다.")
    print()

    # 각 jar 파일에서 properties 추출
    all_extracted = []
    for i, jar_path in enumerate(jar_files, 1):
        if verbose:
            print(f"[{i}/{len(jar_files)}] {jar_path.name}")

        extracted = extract_properties_from_jar(jar_path, output_dir, verbose)
        all_extracted.extend(extracted)

        if verbose and extracted:
            print()

    # 결과 요약
    print("=" * 80)
    print("추출 완료")
    print("=" * 80)
    print(f"총 jar 파일: {len(jar_files)}")
    print(f"추출된 properties 파일: {len(all_extracted)}")
    print(f"출력 위치: {output_dir}")
    print()

    # 추출된 파일 목록 (중복 제거)
    unique_files = {}
    for jar_name, prop_file, size in all_extracted:
        if prop_file not in unique_files:
            unique_files[prop_file] = (jar_name, size)

    if unique_files:
        print("추출된 파일 목록:")
        for prop_file, (jar_name, size) in sorted(unique_files.items()):
            print(f"  - {prop_file} (from {jar_name}, {size} bytes)")


def main():
    parser = argparse.ArgumentParser(
        description='Android Studio/플러그인 jar 파일에서 properties 파일 추출'
    )
    parser.add_argument(
        'source',
        type=str,
        help='Android Studio 설치 경로 또는 jar 파일이 있는 디렉토리'
    )
    parser.add_argument(
        '-o', '--output',
        type=str,
        default='extracted_properties',
        help='출력 디렉토리 (기본값: extracted_properties)'
    )
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='상세 출력'
    )

    args = parser.parse_args()

    source_dir = Path(args.source)
    output_dir = Path(args.output)

    if not source_dir.exists():
        print(f"❌ 소스 디렉토리를 찾을 수 없습니다: {source_dir}")
        return

    if not source_dir.is_dir():
        print(f"❌ 소스가 디렉토리가 아닙니다: {source_dir}")
        return

    extract_from_directory(source_dir, output_dir, args.verbose)


if __name__ == "__main__":
    # 인수 없이 실행된 경우 도움말 표시
    import sys
    if len(sys.argv) == 1:
        print("=" * 80)
        print("JAR 파일에서 Properties 추출 도구")
        print("=" * 80)
        print()
        print("사용법:")
        print("  python scripts/extract_from_jar.py <Android Studio 경로> [-o 출력폴더] [-v]")
        print()
        print("예시:")
        print("  # Windows")
        print("  python scripts/extract_from_jar.py \"C:\\Program Files\\Android\\Android Studio\" -o extracted_properties -v")
        print()
        print("  # macOS")
        print("  python scripts/extract_from_jar.py \"/Applications/Android Studio.app\" -o extracted_properties")
        print()
        print("  # Linux")
        print("  python scripts/extract_from_jar.py /opt/android-studio -o extracted_properties")
        print()
        print("옵션:")
        print("  -o, --output   출력 디렉토리 (기본값: extracted_properties)")
        print("  -v, --verbose  상세 출력")
        print("  -h, --help     도움말 표시")
        print()
    else:
        main()
