#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""프로젝트 정리 스크립트"""

from pathlib import Path
import shutil

WORK_DIR = Path(r"c:\Users\klanary\Desktop\vscode 모음\android_korean\androidstudio_koreanlanguagepack")
MESSAGES_DIR = WORK_DIR / "src" / "main" / "resources" / "messages"

print("=" * 60)
print("프로젝트 정리 시작")
print("=" * 60)
print()

# 1. _ko가 없는 잘못된 properties 파일들 삭제
print("[1/5] 잘못된 properties 파일 삭제 중...")
deleted_count = 0
for props_file in MESSAGES_DIR.glob("*.properties"):
    if not props_file.stem.endswith("_ko"):
        print(f"  삭제: {props_file.name}")
        props_file.unlink()
        deleted_count += 1
print(f"  총 {deleted_count}개 파일 삭제됨")

# 2. kotlin 소스 파일 확인 및 정리
print()
print("[2/5] Kotlin 소스 파일 정리 중...")
kotlin_dir = WORK_DIR / "src" / "main" / "kotlin" / "com" / "github" / "c211007" / "androidstudiokoreanlanguagepack"

# MyBundle.kt 삭제 (허구의 번들)
mybundle_kt = kotlin_dir / "MyBundle.kt"
if mybundle_kt.exists():
    print(f"  삭제: MyBundle.kt")
    mybundle_kt.unlink()

# KoreanLocalizationProvider.kt는 유지 (실제 필요할 수 있음)
print("  KoreanLocalizationProvider.kt 유지")

# 3. 추출 디렉토리 중 불필요한 것만 삭제
print()
print("[3/5] 불필요한 추출 디렉토리 정리 중...")
# bin 디렉토리 삭제
bin_dir = WORK_DIR / "bin"
if bin_dir.exists():
    print(f"  삭제: bin/")
    shutil.rmtree(bin_dir)

# 4. 불필요한 파일들 삭제
print()
print("[4/5] 불필요한 파일 삭제 중...")
unnecessary_files = [
    "android.zip",  # 이미 추출했음
    "build.log",
    "build_full.log",
    "PLAN.md",  # 임시 파일
]

for filename in unnecessary_files:
    file_path = WORK_DIR / filename
    if file_path.exists():
        print(f"  삭제: {filename}")
        file_path.unlink()

# 5. 남은 한국어 번들 파일 확인
print()
print("[5/5] 한국어 번들 파일 확인...")
ko_files = list(MESSAGES_DIR.glob("*_ko.properties"))
print(f"  남은 한국어 번들: {len(ko_files)}개")
for ko_file in sorted(ko_files):
    print(f"    - {ko_file.name}")

print()
print("=" * 60)
print("정리 완료!")
print("=" * 60)
print()
print("유지된 디렉토리:")
print("  - extracted_android/     (원본 Android 번들)")
print("  - extracted_bundles/     (원본 IntelliJ 번들)")
print("  - extracted_keys/        (추출된 키 목록)")
print()
print("삭제된 항목:")
print("  - 허구의 키가 포함된 _ko가 없는 properties 파일들")
print("  - MyBundle.kt 파일")
print("  - bin/ 디렉토리")
print("  - android.zip (이미 추출됨)")
print("  - 로그 파일들")
