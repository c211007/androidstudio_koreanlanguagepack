#!/usr/bin/env python3
"""
Restore all properties files to English originals with updated header
"""

import os
from pathlib import Path

# Paths
EXTRACTED_DIR = Path("extracted_bundles")
TARGET_DIR = Path("src/main/resources/messages")

# Updated header template
HEADER_TEMPLATE = """# ╔═══════════════════════════════════════════════════════════════════════════════╗
# ║  {bundle_name} - Korean Translation
# ║  Android Studio 한국어 언어팩
# ╠═══════════════════════════════════════════════════════════════════════════════╣
# ║  수정 시 유의사항 (Translation Guidelines)
# ║  ─────────────────────────────────────────────────────────────────────────────
# ║  1. 키(key)는 절대 변경하지 마세요. = 왼쪽 부분은 수정 금지!
# ║     Do NOT modify keys (text before =)
# ║
# ║  2. {{0}}, {{1}}, {{2}} 같은 플레이스홀더는 그대로 유지하세요.
# ║     Keep placeholders like {{0}}, {{1}}, {{2}} unchanged
# ║     예: "파일 {{0}}을(를) 저장했습니다" (O)
# ║         "파일을 저장했습니다" (X) - {{0}} 누락
# ║
# ║  3. _(언더바) 바로 뒤에 있는 문자가 키보드 단축키입니다.
# ║     원래의 단축키를 한국어 번역 뒤 괄호 안에 넣으세요.
# ║     Undersc_ore marks keyboard shortcuts
# ║     예: "_Copy" → "복사(_C)"
# ║
# ║  4. ... (말줄임표)는 추가 작업이 필요함을 의미합니다. 유지하세요.
# ║     Keep ... (ellipsis) as it indicates additional action needed
# ║
# ║  5. 특수문자 앞에는 백슬래시(\\)를 붙여야 합니다.
# ║     Escape special characters with backslash
# ║     예: 콜론(:) → \\:  등호(=) → \\=
# ║
# ║  6. 주석(#으로 시작하는 줄)은 번역에 영향을 주지 않습니다.
# ║     Comments (lines starting with #) don't affect translation
# ╚═══════════════════════════════════════════════════════════════════════════════╝


"""


def find_original_file(bundle_name):
    """Find the original English properties file"""
    # Try intellij first, then android
    intellij_path = EXTRACTED_DIR / "intellij" / "messages" / bundle_name
    android_path = EXTRACTED_DIR / "android" / "messages" / bundle_name

    if intellij_path.exists():
        return intellij_path
    elif android_path.exists():
        return android_path
    else:
        return None


def process_file(target_file):
    """Process a single properties file"""
    bundle_name = target_file.name

    # Find original file
    original_file = find_original_file(bundle_name)
    if not original_file:
        print(f"[WARNING] Original file not found for {bundle_name}")
        return False

    try:
        # Read original content
        with open(original_file, 'r', encoding='utf-8') as f:
            original_content = f.read()

        # Remove any existing header (everything before the first non-comment, non-empty line with =)
        lines = original_content.split('\n')
        content_start = 0
        for i, line in enumerate(lines):
            stripped = line.strip()
            if stripped and not stripped.startswith('#') and '=' in stripped:
                content_start = i
                break

        # Get content without header
        content_lines = lines[content_start:]
        content = '\n'.join(content_lines)

        # Create new file with updated header
        new_content = HEADER_TEMPLATE.format(bundle_name=bundle_name.replace('.properties', ''))
        new_content += content

        # Write to target
        with open(target_file, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"[OK] Processed: {bundle_name}")
        return True

    except Exception as e:
        print(f"[ERROR] Error processing {bundle_name}: {e}")
        return False


def main():
    """Main function"""
    if not EXTRACTED_DIR.exists():
        print(f"Error: {EXTRACTED_DIR} directory not found!")
        return

    if not TARGET_DIR.exists():
        print(f"Error: {TARGET_DIR} directory not found!")
        return

    # Get all target properties files
    target_files = list(TARGET_DIR.glob("*.properties"))

    print(f"Found {len(target_files)} properties files to process\n")

    success_count = 0
    for target_file in sorted(target_files):
        if process_file(target_file):
            success_count += 1

    print(f"\n{'='*80}")
    print(f"Summary: {success_count}/{len(target_files)} files processed successfully")
    print(f"{'='*80}")


if __name__ == "__main__":
    main()
