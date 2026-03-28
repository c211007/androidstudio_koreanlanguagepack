#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
classify_bundle_file 함수 테스트
"""

import sys
from pathlib import Path

# merge_translations 모듈 임포트를 위한 경로 추가
sys.path.insert(0, str(Path(__file__).parent / "src" / "main" / "version_updates"))

from merge_translations import classify_bundle_file

# 테스트 케이스
test_files = [
    # 새로 추가된 파일들 (missing_keys_korean.json에서)
    ("AgentsCoreBundle.properties", "android"),
    ("AndroidDesignerActionsBundle.properties", "android"),
    ("AndroidNdkBundle.properties", "android"),
    
    # 기존 Android 번들들
    ("AndroidBundle.properties", "android"),
    ("AndroidTestBundle_ko.properties", "android"),
    ("AndroidLintBundle.properties", "android"),
    ("AgpUpgradeBundle.properties", "android"),
    ("DatabaseInspectorBundle.properties", "android"),
    ("DeviceManagerBundle.properties", "android"),
    ("LayoutInspectorBundle_ko.properties", "android"),
    ("LogcatBundle.properties", "android"),
    ("WearDwfBundle.properties", "android"),
    
    # IntelliJ 번들들 (Android 패턴 없음)
    ("ActionsBundle.properties", "intellij"),
    ("IdeBundle_ko.properties", "intellij"),
    ("VcsBundle.properties", "intellij"),
    ("JavaBundle.properties", "intellij"),
    ("PlatformBundle.properties", "intellij"),
]

print("=" * 80)
print("Bundle Classification Test")
print("=" * 80 + "\n")

passed = 0
failed = 0
errors = []

for filename, expected in test_files:
    result = classify_bundle_file(filename)
    status = "✅ PASS" if result == expected else "❌ FAIL"
    
    print(f"{status} | {filename:45s} → {result:8s} (expected: {expected})")
    
    if result == expected:
        passed += 1
    else:
        failed += 1
        errors.append(f"  - {filename}: got '{result}', expected '{expected}'")

print("\n" + "=" * 80)
print(f"Results: {passed} passed, {failed} failed out of {len(test_files)} tests")
print("=" * 80)

if errors:
    print("\nFailed tests:")
    for error in errors:
        print(error)
    sys.exit(1)
else:
    print("\n✅ All tests passed!")
    sys.exit(0)
