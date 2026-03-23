#!/usr/bin/env python3
"""
Convert UTF-8 properties files to ISO-8859-1 with Unicode escapes.
This is required for IntelliJ Platform ResourceBundle to correctly load Korean translations.
"""

import os
import sys
from pathlib import Path

def escape_unicode(text):
    """Convert text to ASCII with Unicode escapes for non-ASCII characters."""
    result = []
    for char in text:
        if ord(char) > 127:
            result.append(f'\\u{ord(char):04x}')
        else:
            result.append(char)
    return ''.join(result)

def convert_file(input_path, output_path):
    """Convert a single properties file from UTF-8 to escaped format."""
    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Convert to unicode escapes
        escaped_content = escape_unicode(content)

        # Write as ISO-8859-1 (which is ASCII-compatible)
        with open(output_path, 'w', encoding='iso-8859-1') as f:
            f.write(escaped_content)

        print(f"[OK] Converted: {input_path}")
        return True
    except Exception as e:
        print(f"[ERROR] Error converting {input_path}: {e}", file=sys.stderr)
        return False

def main():
    """Convert all properties files in the messages directory."""
    resources_dir = Path(__file__).parent / 'src' / 'main' / 'resources' / 'messages'

    if not resources_dir.exists():
        print(f"Error: Directory not found: {resources_dir}", file=sys.stderr)
        sys.exit(1)

    properties_files = list(resources_dir.glob('*.properties'))

    if not properties_files:
        print(f"No .properties files found in {resources_dir}")
        sys.exit(0)

    print(f"Converting {len(properties_files)} properties files...")

    success_count = 0
    for prop_file in properties_files:
        if convert_file(prop_file, prop_file):
            success_count += 1

    print(f"\nCompleted: {success_count}/{len(properties_files)} files converted successfully")

    if success_count < len(properties_files):
        sys.exit(1)

if __name__ == '__main__':
    main()
