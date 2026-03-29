#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
번역 파일 Key 검사 스크립트
원본 properties 파일과 번역된 properties 파일을 비교하여 누락된 key를 찾습니다.
"""

import os
import re
from pathlib import Path
from collections import defaultdict


def parse_properties_file(filepath):
    """
    properties 파일을 파싱하여 key 목록을 반환합니다.
    주석과 빈 줄은 무시하고, key=value 형식에서 key만 추출합니다.
    줄바꿈이 있는 value도 올바르게 처리합니다 (백슬래시로 이어진 줄).
    """
    keys = set()

    if not os.path.exists(filepath):
        return keys

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        i = 0
        while i < len(lines):
            # 줄 끝의 개행문자 제거
            line = lines[i].rstrip('\n\r')

            # 앞뒤 공백 제거하여 체크
            stripped = line.strip()

            # 빈 줄이나 주석은 건너뛰기
            if not stripped or stripped.startswith('#') or stripped.startswith('!'):
                i += 1
                continue

            # key=value 형식에서 key 추출
            # 이스케이프된 = 는 무시하고 첫 번째 = 를 찾음
            match = re.match(r'^([^=:]+?)[\s]*[=:]', stripped)
            if match:
                key = match.group(1).strip()
                keys.add(key)

                # value 부분 가져오기 (줄바꿈 처리를 위해)
                value_part = stripped[match.end():]

                # 백슬래시로 끝나면 다음 줄과 연결된 것
                # 백슬래시가 연속되는 동안 계속 읽기
                while value_part.rstrip().endswith('\\') and i + 1 < len(lines):
                    i += 1
                    next_line = lines[i].rstrip('\n\r')
                    # 다음 줄이 주석이나 빈 줄이 아니면 value에 포함
                    value_part = next_line.strip()

            i += 1

    except Exception as e:
        print(f"⚠️  파일 읽기 오류: {filepath}")
        print(f"   에러: {e}")

    return keys


def compare_translation_keys(original_dir, translated_dir):
    """
    원본 디렉토리와 번역 디렉토리를 비교하여 누락/추가된 key를 찾습니다.
    """
    original_path = Path(original_dir)
    translated_path = Path(translated_dir)

    # 원본 파일 목록
    original_files = {f.name: f for f in original_path.glob('*.properties')}
    # 번역 파일 목록
    translated_files = {f.name: f for f in translated_path.glob('*.properties')}

    results = {
        'missing_files': [],      # 번역되지 않은 파일
        'extra_files': [],        # 원본에 없는 번역 파일
        'missing_keys': {},       # 각 파일별 누락된 key
        'extra_keys': {},         # 각 파일별 추가된 key
        'perfect_files': []       # 완벽하게 번역된 파일
    }

    # 번역되지 않은 파일 찾기
    for filename in original_files:
        if filename not in translated_files:
            results['missing_files'].append(filename)

    # 원본에 없는 번역 파일 찾기
    for filename in translated_files:
        if filename not in original_files:
            results['extra_files'].append(filename)

    # 공통 파일에 대해 key 비교
    common_files = set(original_files.keys()) & set(translated_files.keys())

    for filename in sorted(common_files):
        original_keys = parse_properties_file(original_files[filename])
        translated_keys = parse_properties_file(translated_files[filename])

        # 누락된 key (원본에는 있지만 번역에는 없음)
        missing = original_keys - translated_keys
        # 추가된 key (번역에만 있고 원본에는 없음)
        extra = translated_keys - original_keys

        if missing:
            results['missing_keys'][filename] = sorted(missing)

        if extra:
            results['extra_keys'][filename] = sorted(extra)

        # 완벽한 파일
        if not missing and not extra:
            results['perfect_files'].append(filename)

    return results


def print_results(results):
    """
    검사 결과를 보기 좋게 출력합니다.
    """
    print("\n" + "="*80)
    print("📋 번역 파일 Key 검사 결과")
    print("="*80 + "\n")

    # 통계 요약
    total_files = len(results['missing_files']) + len(results['extra_files']) + \
                  len(results['missing_keys']) + len(results['extra_keys']) + \
                  len(results['perfect_files'])

    print(f"📊 전체 요약:")
    print(f"   - 전체 파일 수: {total_files}")
    print(f"   - ✅ 완벽한 번역: {len(results['perfect_files'])} 파일")
    print(f"   - ⚠️  Key 누락 있음: {len(results['missing_keys'])} 파일")
    print(f"   - ℹ️  Key 추가 있음: {len(results['extra_keys'])} 파일")
    print(f"   - ❌ 번역 파일 없음: {len(results['missing_files'])} 파일")
    print(f"   - 🔍 원본에 없는 파일: {len(results['extra_files'])} 파일")
    print()

    # 번역되지 않은 파일
    if results['missing_files']:
        print("\n" + "-"*80)
        print(f"❌ 번역 파일이 없는 원본 파일 ({len(results['missing_files'])}개):")
        print("-"*80)
        for filename in sorted(results['missing_files']):
            print(f"   - {filename}")

    # 원본에 없는 번역 파일
    if results['extra_files']:
        print("\n" + "-"*80)
        print(f"🔍 원본에 없는 번역 파일 ({len(results['extra_files'])}개):")
        print("-"*80)
        for filename in sorted(results['extra_files']):
            print(f"   - {filename}")

    # 누락된 key가 있는 파일들
    if results['missing_keys']:
        print("\n" + "-"*80)
        print(f"⚠️  번역에서 누락된 Key가 있는 파일 ({len(results['missing_keys'])}개):")
        print("-"*80)

        total_missing_keys = sum(len(keys) for keys in results['missing_keys'].values())
        print(f"   총 누락된 Key 수: {total_missing_keys}\n")

        for filename in sorted(results['missing_keys'].keys()):
            missing_keys = results['missing_keys'][filename]
            print(f"\n   📄 {filename}")
            print(f"      누락된 Key: {len(missing_keys)}개")
            for key in missing_keys[:10]:  # 처음 10개만 표시
                print(f"      - {key}")
            if len(missing_keys) > 10:
                print(f"      ... 외 {len(missing_keys) - 10}개")

    # 추가된 key가 있는 파일들
    if results['extra_keys']:
        print("\n" + "-"*80)
        print(f"ℹ️  번역에 추가된 Key가 있는 파일 ({len(results['extra_keys'])}개):")
        print("-"*80)
        print("   (원본에는 없지만 번역에 있는 Key - 확인 필요)\n")

        for filename in sorted(results['extra_keys'].keys()):
            extra_keys = results['extra_keys'][filename]
            print(f"\n   📄 {filename}")
            print(f"      추가된 Key: {len(extra_keys)}개")
            for key in extra_keys[:5]:  # 처음 5개만 표시
                print(f"      - {key}")
            if len(extra_keys) > 5:
                print(f"      ... 외 {len(extra_keys) - 5}개")

    # 완벽한 파일들
    if results['perfect_files']:
        print("\n" + "-"*80)
        print(f"✅ 완벽하게 번역된 파일 ({len(results['perfect_files'])}개):")
        print("-"*80)
        for filename in sorted(results['perfect_files'])[:20]:  # 처음 20개만 표시
            print(f"   - {filename}")
        if len(results['perfect_files']) > 20:
            print(f"   ... 외 {len(results['perfect_files']) - 20}개")

    print("\n" + "="*80 + "\n")


def main():
    """
    메인 함수
    """
    # 경로 설정
    script_dir = Path(__file__).parent
    messages_dir = script_dir / 'src' / 'main' / 'resources' / 'messages'
    original_dir = messages_dir / 'original'
    translated_dir = messages_dir

    print(f"\n🔍 번역 파일 검사 시작...")
    print(f"   원본 디렉토리: {original_dir}")
    print(f"   번역 디렉토리: {translated_dir}")

    # 디렉토리 존재 확인
    if not original_dir.exists():
        print(f"\n❌ 오류: 원본 디렉토리를 찾을 수 없습니다: {original_dir}")
        return

    if not translated_dir.exists():
        print(f"\n❌ 오류: 번역 디렉토리를 찾을 수 없습니다: {translated_dir}")
        return

    # Key 비교 수행
    results = compare_translation_keys(original_dir, translated_dir)

    # 결과 출력
    print_results(results)

    # 상세 보고서 파일 생성
    report_file = script_dir / 'translation_check_report.txt'
    with open(report_file, 'w', encoding='utf-8') as f:
        f.write("="*80 + "\n")
        f.write("번역 파일 Key 검사 상세 보고서\n")
        f.write("="*80 + "\n\n")

        # 누락된 key 상세 정보
        if results['missing_keys']:
            f.write("\n누락된 Key 상세 목록:\n")
            f.write("-"*80 + "\n")
            for filename in sorted(results['missing_keys'].keys()):
                f.write(f"\n[{filename}]\n")
                for key in results['missing_keys'][filename]:
                    f.write(f"  {key}\n")

        # 추가된 key 상세 정보
        if results['extra_keys']:
            f.write("\n\n추가된 Key 상세 목록:\n")
            f.write("-"*80 + "\n")
            for filename in sorted(results['extra_keys'].keys()):
                f.write(f"\n[{filename}]\n")
                for key in results['extra_keys'][filename]:
                    f.write(f"  {key}\n")

    print(f"📝 상세 보고서가 생성되었습니다: {report_file}")


if __name__ == '__main__':
    main()
