#!/usr/bin/env python3
"""
Translation Key Comparison Tool

이 스크립트는 pro_location 폴더와 src/main/resources/messages 폴더의 
.properties 파일들을 비교하여 빠진 키를 찾습니다.
"""

import os
import re
from pathlib import Path
from collections import defaultdict


def parse_properties_file(file_path):
    """
    .properties 파일을 파싱하여 키 집합을 반환합니다.
    
    여러 줄로 이어지는 value를 올바르게 처리합니다:
    - 백슬래시(\)로 끝나는 줄은 다음 줄과 연결
    - 연속되는 줄들은 하나의 key-value 쌍으로 처리
    
    Args:
        file_path: .properties 파일 경로
        
    Returns:
        파일 내의 모든 키의 집합
    """
    keys = set()
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        i = 0
        while i < len(lines):
            line = lines[i].rstrip('\r\n')
            
            # 백슬래시로 끝나는 경우 다음 줄들을 모두 연결
            while line.endswith('\\') and i + 1 < len(lines):
                # 백슬래시 제거하고 다음 줄 추가
                line = line[:-1] + lines[i + 1].rstrip('\r\n')
                i += 1
            
            # 양쪽 공백 제거
            line = line.strip()
            
            # 빈 줄이나 주석은 무시
            if not line or line.startswith('#') or line.startswith('!'):
                i += 1
                continue
            
            # key=value 또는 key:value 형식에서 key 추출
            # = 또는 : 중 먼저 나오는 것을 구분자로 사용
            separator_pos = -1
            for char_idx, char in enumerate(line):
                if char in ('=', ':'):
                    # 이스케이프되지 않은 = 또는 : 찾기
                    if char_idx == 0 or line[char_idx - 1] != '\\':
                        separator_pos = char_idx
                        break
            
            if separator_pos > 0:
                key = line[:separator_pos].strip()
                keys.add(key)
            
            i += 1
            
    except Exception as e:
        print(f"❌ 파일 읽기 오류: {file_path}")
        print(f"   {e}")
    
    return keys


def get_properties_files(directory):
    """
    지정된 디렉토리에서 모든 .properties 파일을 찾습니다.
    
    Args:
        directory: 검색할 디렉토리 경로
        
    Returns:
        .properties 파일 경로의 딕셔너리 {파일명: 전체경로}
    """
    properties_files = {}
    directory_path = Path(directory)
    
    if not directory_path.exists():
        print(f"⚠️  경로가 존재하지 않습니다: {directory}")
        return properties_files
    
    for file_path in directory_path.glob('*.properties'):
        properties_files[file_path.name] = str(file_path)
    
    return properties_files


def compare_keys(source_keys, target_keys):
    """
    두 키 집합을 비교하여 차이를 반환합니다.
    
    Args:
        source_keys: 원본 키 집합
        target_keys: 대상 키 집합
        
    Returns:
        source에는 있지만 target에는 없는 키들의 집합
    """
    return source_keys - target_keys


def main():
    # 기본 경로 설정
    script_dir = Path(__file__).parent
    pro_location_dir = script_dir / 'pro_location'
    messages_dir = script_dir / 'src' / 'main' / 'resources' / 'messages'
    
    print("=" * 80)
    print("🔍 번역 키 비교 도구")
    print("=" * 80)
    print(f"원본 폴더: {pro_location_dir}")
    print(f"번역 폴더: {messages_dir}")
    print()
    
    # 두 폴더에서 .properties 파일 목록 가져오기
    print("📂 파일 목록 수집 중...")
    pro_files = get_properties_files(pro_location_dir)
    msg_files = get_properties_files(messages_dir)
    
    print(f"   원본 폴더: {len(pro_files)}개 파일")
    print(f"   번역 폴더: {len(msg_files)}개 파일")
    print()
    
    # 전체 통계
    total_missing_keys = 0
    total_files_with_missing = 0
    total_files_checked = 0
    files_only_in_pro = set(pro_files.keys()) - set(msg_files.keys())
    files_only_in_msg = set(msg_files.keys()) - set(pro_files.keys())
    
    # 빠진 파일 확인
    if files_only_in_pro:
        print("⚠️  원본에는 있지만 번역 폴더에 없는 파일:")
        for filename in sorted(files_only_in_pro):
            print(f"   - {filename}")
        print()
    
    if files_only_in_msg:
        print("ℹ️  번역 폴더에만 있는 파일 (원본에 없음):")
        for filename in sorted(files_only_in_msg):
            print(f"   - {filename}")
        print()
    
    # 공통 파일들에 대해 키 비교
    common_files = set(pro_files.keys()) & set(msg_files.keys())
    
    if not common_files:
        print("❌ 비교할 공통 파일이 없습니다!")
        return
    
    print("=" * 80)
    print(f"📊 {len(common_files)}개 파일 비교 중...")
    print("=" * 80)
    print()
    
    # 결과를 저장할 딕셔너리
    missing_keys_by_file = {}
    
    for filename in sorted(common_files):
        total_files_checked += 1
        pro_path = pro_files[filename]
        msg_path = msg_files[filename]
        
        # 각 파일에서 키 추출
        pro_keys = parse_properties_file(pro_path)
        msg_keys = parse_properties_file(msg_path)
        
        # 빠진 키 찾기
        missing_keys = compare_keys(pro_keys, msg_keys)
        
        if missing_keys:
            total_files_with_missing += 1
            total_missing_keys += len(missing_keys)
            missing_keys_by_file[filename] = sorted(missing_keys)
            
            print(f"📄 {filename}")
            print(f"   원본 키: {len(pro_keys)}개")
            print(f"   번역 키: {len(msg_keys)}개")
            print(f"   ❌ 빠진 키: {len(missing_keys)}개")
            
            # 처음 5개만 미리보기
            preview_count = min(5, len(missing_keys))
            for key in sorted(missing_keys)[:preview_count]:
                print(f"      - {key}")
            
            if len(missing_keys) > preview_count:
                print(f"      ... 외 {len(missing_keys) - preview_count}개 더")
            
            print()
    
    # 최종 요약
    print("=" * 80)
    print("📊 최종 요약")
    print("=" * 80)
    print(f"총 검사한 파일: {total_files_checked}개")
    print(f"빠진 키가 있는 파일: {total_files_with_missing}개")
    print(f"총 빠진 키 개수: {total_missing_keys}개")
    print()
    
    # 상세 결과를 파일로 저장
    output_file = script_dir / 'missing_keys_report.txt'
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("번역 누락 키 상세 보고서\n")
        f.write("=" * 80 + "\n")
        f.write(f"생성일시: {Path(__file__).stat().st_mtime}\n")
        f.write(f"원본 폴더: {pro_location_dir}\n")
        f.write(f"번역 폴더: {messages_dir}\n")
        f.write("\n")
        f.write(f"총 검사한 파일: {total_files_checked}개\n")
        f.write(f"빠진 키가 있는 파일: {total_files_with_missing}개\n")
        f.write(f"총 빠진 키 개수: {total_missing_keys}개\n")
        f.write("\n")
        f.write("=" * 80 + "\n\n")
        
        for filename, missing_keys in sorted(missing_keys_by_file.items()):
            f.write(f"\n파일: {filename}\n")
            f.write(f"빠진 키 개수: {len(missing_keys)}개\n")
            f.write("-" * 80 + "\n")
            for key in missing_keys:
                f.write(f"{key}\n")
            f.write("\n")
    
    print(f"✅ 상세 보고서가 저장되었습니다: {output_file}")
    print()
    
    if total_missing_keys == 0:
        print("🎉 모든 키가 번역되었습니다!")
    else:
        print(f"⚠️  {total_missing_keys}개의 키가 번역되지 않았습니다.")


if __name__ == '__main__':
    main()
