#!/usr/bin/env python3
"""
버전 간 Properties 파일 비교 스크립트

두 버전의 properties 파일을 비교하여 추가/변경/삭제된 키를 찾습니다.
"""

import os
from pathlib import Path
import argparse
from collections import defaultdict


def load_properties(file_path):
    """Properties 파일 로드"""
    properties = {}

    if not file_path.exists():
        return properties

    with open(file_path, 'r', encoding='utf-8') as f:
        for line_num, line in enumerate(f, 1):
            line = line.strip()

            # 주석이나 빈 줄 건너뛰기
            if not line or line.startswith('#'):
                continue

            # key=value 파싱
            if '=' in line:
                key, value = line.split('=', 1)
                properties[key.strip()] = value.strip()

    return properties


def compare_properties(old_props, new_props):
    """두 properties 딕셔너리 비교"""
    old_keys = set(old_props.keys())
    new_keys = set(new_props.keys())

    added = new_keys - old_keys
    removed = old_keys - new_keys
    common = old_keys & new_keys

    # 값이 변경된 키 찾기
    modified = set()
    for key in common:
        if old_props[key] != new_props[key]:
            modified.add(key)

    return {
        'added': sorted(added),
        'removed': sorted(removed),
        'modified': sorted(modified),
        'unchanged': sorted(common - modified)
    }


def compare_directories(old_dir, new_dir, output_dir=None, verbose=False):
    """두 디렉토리의 properties 파일들을 비교"""
    old_dir = Path(old_dir)
    new_dir = Path(new_dir)

    if not old_dir.exists():
        print(f"❌ 이전 버전 디렉토리를 찾을 수 없습니다: {old_dir}")
        return

    if not new_dir.exists():
        print(f"❌ 새 버전 디렉토리를 찾을 수 없습니다: {new_dir}")
        return

    print(f"이전 버전: {old_dir}")
    print(f"새 버전: {new_dir}")
    print()

    # properties 파일 목록 가져오기
    old_files = {f.name: f for f in old_dir.glob("*.properties")}
    new_files = {f.name: f for f in new_dir.glob("*.properties")}

    all_files = sorted(set(old_files.keys()) | set(new_files.keys()))

    # 전체 통계
    total_stats = {
        'added': 0,
        'removed': 0,
        'modified': 0,
        'unchanged': 0,
        'new_files': 0,
        'removed_files': 0
    }

    # 파일별 비교
    results = {}

    for filename in all_files:
        if filename not in old_files:
            # 새로 추가된 파일
            total_stats['new_files'] += 1
            new_props = load_properties(new_files[filename])
            total_stats['added'] += len(new_props)
            results[filename] = {
                'status': 'NEW',
                'added': sorted(new_props.keys()),
                'removed': [],
                'modified': [],
                'unchanged': []
            }
            if verbose:
                print(f"🆕 {filename} (새 파일, {len(new_props)} keys)")

        elif filename not in new_files:
            # 제거된 파일
            total_stats['removed_files'] += 1
            old_props = load_properties(old_files[filename])
            total_stats['removed'] += len(old_props)
            results[filename] = {
                'status': 'REMOVED',
                'added': [],
                'removed': sorted(old_props.keys()),
                'modified': [],
                'unchanged': []
            }
            if verbose:
                print(f"🗑️  {filename} (제거된 파일, {len(old_props)} keys)")

        else:
            # 기존 파일 비교
            old_props = load_properties(old_files[filename])
            new_props = load_properties(new_files[filename])

            diff = compare_properties(old_props, new_props)

            total_stats['added'] += len(diff['added'])
            total_stats['removed'] += len(diff['removed'])
            total_stats['modified'] += len(diff['modified'])
            total_stats['unchanged'] += len(diff['unchanged'])

            results[filename] = {
                'status': 'MODIFIED' if (diff['added'] or diff['removed'] or diff['modified']) else 'UNCHANGED',
                **diff
            }

            if verbose:
                changes = len(diff['added']) + len(diff['removed']) + len(diff['modified'])
                if changes > 0:
                    print(f"📝 {filename} (+{len(diff['added'])} -{len(diff['removed'])} ~{len(diff['modified'])})")

    # 결과 출력
    print()
    print("=" * 80)
    print("비교 결과 요약")
    print("=" * 80)
    print(f"파일:")
    print(f"  새 파일: {total_stats['new_files']}")
    print(f"  제거된 파일: {total_stats['removed_files']}")
    print(f"  수정된 파일: {sum(1 for r in results.values() if r['status'] == 'MODIFIED')}")
    print(f"  변경 없음: {sum(1 for r in results.values() if r['status'] == 'UNCHANGED')}")
    print()
    print(f"키:")
    print(f"  추가됨: {total_stats['added']}")
    print(f"  제거됨: {total_stats['removed']}")
    print(f"  수정됨: {total_stats['modified']}")
    print(f"  변경 없음: {total_stats['unchanged']}")
    print()

    # 출력 디렉토리가 지정된 경우 상세 리포트 저장
    if output_dir:
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)

        # 추가된 키 목록
        with open(output_path / "added_keys.txt", 'w', encoding='utf-8') as f:
            f.write(f"# 추가된 키 ({total_stats['added']}개)\n\n")
            for filename, result in sorted(results.items()):
                if result['added']:
                    f.write(f"# {filename}\n")
                    for key in result['added']:
                        f.write(f"{key}\n")
                    f.write("\n")

        # 제거된 키 목록
        with open(output_path / "removed_keys.txt", 'w', encoding='utf-8') as f:
            f.write(f"# 제거된 키 ({total_stats['removed']}개)\n\n")
            for filename, result in sorted(results.items()):
                if result['removed']:
                    f.write(f"# {filename}\n")
                    for key in result['removed']:
                        f.write(f"{key}\n")
                    f.write("\n")

        # 수정된 키 목록
        with open(output_path / "modified_keys.txt", 'w', encoding='utf-8') as f:
            f.write(f"# 수정된 키 ({total_stats['modified']}개)\n\n")
            for filename, result in sorted(results.items()):
                if result['modified']:
                    f.write(f"# {filename}\n")
                    for key in result['modified']:
                        f.write(f"{key}\n")
                    f.write("\n")

        # 전체 리포트
        with open(output_path / "diff_report.md", 'w', encoding='utf-8') as f:
            f.write("# 버전 비교 리포트\n\n")
            f.write(f"- 이전 버전: `{old_dir}`\n")
            f.write(f"- 새 버전: `{new_dir}`\n\n")

            f.write("## 요약\n\n")
            f.write(f"- 새 파일: {total_stats['new_files']}\n")
            f.write(f"- 제거된 파일: {total_stats['removed_files']}\n")
            f.write(f"- 수정된 파일: {sum(1 for r in results.values() if r['status'] == 'MODIFIED')}\n")
            f.write(f"- 추가된 키: {total_stats['added']}\n")
            f.write(f"- 제거된 키: {total_stats['removed']}\n")
            f.write(f"- 수정된 키: {total_stats['modified']}\n\n")

            f.write("## 파일별 변경사항\n\n")
            for filename, result in sorted(results.items()):
                if result['status'] == 'UNCHANGED':
                    continue

                f.write(f"### {filename}\n\n")
                f.write(f"- 상태: {result['status']}\n")
                if result['added']:
                    f.write(f"- 추가: {len(result['added'])}\n")
                if result['removed']:
                    f.write(f"- 제거: {len(result['removed'])}\n")
                if result['modified']:
                    f.write(f"- 수정: {len(result['modified'])}\n")
                f.write("\n")

        print(f"상세 리포트 저장 위치: {output_path}")
        print("  - added_keys.txt")
        print("  - removed_keys.txt")
        print("  - modified_keys.txt")
        print("  - diff_report.md")


def main():
    parser = argparse.ArgumentParser(
        description='두 버전의 properties 파일 비교'
    )
    parser.add_argument(
        'old',
        type=str,
        help='이전 버전 디렉토리'
    )
    parser.add_argument(
        'new',
        type=str,
        help='새 버전 디렉토리'
    )
    parser.add_argument(
        '-o', '--output',
        type=str,
        help='리포트 출력 디렉토리'
    )
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='상세 출력'
    )

    args = parser.parse_args()

    compare_directories(args.old, args.new, args.output, args.verbose)


if __name__ == "__main__":
    # 인수 없이 실행된 경우 도움말 표시
    import sys
    if len(sys.argv) == 1:
        print("=" * 80)
        print("Properties 파일 버전 비교 도구")
        print("=" * 80)
        print()
        print("사용법:")
        print("  python scripts/compare_versions.py <이전버전> <새버전> [-o 출력폴더] [-v]")
        print()
        print("예시:")
        print("  python scripts/compare_versions.py \\")
        print("    extracted_bundles/intellij/messages \\")
        print("    version_updates/android_studio/2024.1.1/bundles \\")
        print("    -o version_updates/android_studio/2024.1.1 \\")
        print("    -v")
        print()
    else:
        main()
