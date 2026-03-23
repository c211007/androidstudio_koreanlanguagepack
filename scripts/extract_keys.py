#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Android Studio Properties Key Extractor"""

import os
import re
from pathlib import Path
from collections import defaultdict

# 작업 디렉토리
WORK_DIR = Path(r"c:\Users\klanary\Desktop\vscode 모음\android_korean\androidstudio_koreanlanguagepack")
OUTPUT_DIR = WORK_DIR / "extracted_keys"
OUTPUT_DIR.mkdir(exist_ok=True)

print("=" * 60)
print("Android Studio Properties Key Extractor")
print("=" * 60)
print()

def extract_keys_from_file(file_path):
    """Properties 파일에서 키 추출"""
    keys = []
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            for line in f:
                line = line.strip()
                # 주석이나 빈 줄 제외
                if line and not line.startswith('#') and '=' in line:
                    key = line.split('=', 1)[0].strip()
                    if key:
                        keys.append(key)
    except Exception as e:
        print(f"    ⚠ Error reading {file_path}: {e}")
    return sorted(set(keys))

def process_directory(directory, label):
    """디렉토리의 모든 properties 파일 처리"""
    print(f"[{label}] {directory} 처리 중...")
    all_keys = {}

    messages_dir = directory / "messages"
    if not messages_dir.exists():
        print(f"  ⚠ {messages_dir} 디렉토리가 존재하지 않습니다.")
        return all_keys

    for props_file in messages_dir.glob("*.properties"):
        bundle_name = props_file.stem
        print(f"  Processing: {bundle_name}...")

        keys = extract_keys_from_file(props_file)
        if keys:
            # 키 목록 저장
            output_file = OUTPUT_DIR / f"{bundle_name}_keys.txt"
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write('\n'.join(keys))

            all_keys[bundle_name] = keys
            print(f"    → {len(keys)} keys extracted")
        else:
            print(f"    → No keys found")

    return all_keys

# IntelliJ Platform 번들 처리
intellij_dir = WORK_DIR / "extracted_bundles" / "intellij"
intellij_keys = process_directory(intellij_dir, "IntelliJ Platform")

print()

# Android 번들 처리
android_dir = WORK_DIR / "extracted_bundles" / "android"
android_keys = process_directory(android_dir, "Android")

print()
print("[병합] 모든 키 병합 중...")

# 모든 키 수집
all_unique_keys = set()
for keys_dict in [intellij_keys, android_keys]:
    for keys in keys_dict.values():
        all_unique_keys.update(keys)

all_unique_keys = sorted(all_unique_keys)

# 모든 키를 파일에 저장
all_keys_file = OUTPUT_DIR / "all_keys.txt"
with open(all_keys_file, 'w', encoding='utf-8') as f:
    f.write('\n'.join(all_unique_keys))

print(f"  총 고유 키 개수: {len(all_unique_keys)}")

# 키 패턴 분석
print()
print("[분석] 키 명명 규칙 분석 중...")

patterns = {
    'action.*': 0,
    'group.*': 0,
    '*.error': 0,
    '*.warning': 0,
    '*.text': 0,
    '*.title': 0,
    '*.description': 0,
    '*.intention.*': 0,
    '*.dialog.*': 0,
    '*.command.*': 0,
}

for key in all_unique_keys:
    if key.startswith('action.'):
        patterns['action.*'] += 1
    if key.startswith('group.'):
        patterns['group.*'] += 1
    if key.endswith('.error'):
        patterns['*.error'] += 1
    if key.endswith('.warning'):
        patterns['*.warning'] += 1
    if key.endswith('.text'):
        patterns['*.text'] += 1
    if key.endswith('.title'):
        patterns['*.title'] += 1
    if key.endswith('.description'):
        patterns['*.description'] += 1
    if '.intention.' in key:
        patterns['*.intention.*'] += 1
    if '.dialog.' in key:
        patterns['*.dialog.*'] += 1
    if '.command.' in key:
        patterns['*.command.*'] += 1

# 분석 결과 저장
analysis_file = OUTPUT_DIR / "key_analysis.txt"
with open(analysis_file, 'w', encoding='utf-8') as f:
    f.write("=" * 60 + "\n")
    f.write("Android Studio Properties 키 명명 규칙\n")
    f.write("=" * 60 + "\n\n")

    f.write("1. 액션 관련 (Actions)\n")
    f.write("   - action.<ActionId>.text = 메뉴/버튼 텍스트\n")
    f.write("   - action.<ActionId>.description = 도구 설명\n")
    f.write("   예: action.NewProject.text=새 프로젝트...\n\n")

    f.write("2. 그룹 관련 (Groups)\n")
    f.write("   - group.<GroupId>.text = 메뉴 그룹 이름\n")
    f.write("   예: group.FileMenu.text=파일(&F)\n\n")

    f.write("3. 오류/경고 메시지\n")
    f.write("   - <문제>.error = 오류 메시지\n")
    f.write("   - <문제>.warning = 경고 메시지\n\n")

    f.write("4. 인텐션 (Intention Actions)\n")
    f.write("   - <기능>.intention.text = 인텐션 텍스트\n\n")

    f.write("5. 다이얼로그/명령\n")
    f.write("   - <기능>.dialog.title = 다이얼로그 제목\n")
    f.write("   - <기능>.command.name = 명령 이름\n\n")

    f.write("\n" + "=" * 60 + "\n")
    f.write("키 패턴 통계\n")
    f.write("=" * 60 + "\n")
    for pattern, count in patterns.items():
        f.write(f"{pattern:20s}: {count:5d} 개\n")

print("  키 패턴 통계:")
for pattern, count in patterns.items():
    print(f"    {pattern:20s}: {count:5d} 개")

# 번들별 통계
print()
print("=" * 60)
print("번들별 통계")
print("=" * 60)

bundle_stats = []
for bundle_name, keys in {**intellij_keys, **android_keys}.items():
    bundle_stats.append((bundle_name, len(keys)))

bundle_stats.sort(key=lambda x: x[1], reverse=True)

print("상위 20개 번들:")
for i, (bundle, count) in enumerate(bundle_stats[:20], 1):
    print(f"{i:2d}. {bundle:40s}: {count:5d} keys")

# 번들 통계 저장
stats_file = OUTPUT_DIR / "bundle_stats.txt"
with open(stats_file, 'w', encoding='utf-8') as f:
    f.write("번들별 키 개수 통계\n")
    f.write("=" * 60 + "\n\n")
    for bundle, count in bundle_stats:
        f.write(f"{bundle:40s}: {count:5d} keys\n")

print()
print("=" * 60)
print("완료!")
print("=" * 60)
print(f"결과 파일 위치: {OUTPUT_DIR}")
print("  - all_keys.txt: 모든 고유 키 목록")
print("  - key_analysis.txt: 키 명명 규칙 분석")
print("  - bundle_stats.txt: 번들별 통계")
print("  - *_keys.txt: 각 번들별 키 목록")
