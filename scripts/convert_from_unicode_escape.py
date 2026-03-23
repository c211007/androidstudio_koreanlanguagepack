#!/usr/bin/env python3
"""
Convert Unicode escaped properties files back to UTF-8.
Reverses the conversion done by convert_to_unicode_escape.py

Usage:
    python convert_from_unicode_escape.py              # Convert all files
    python convert_from_unicode_escape.py file.properties  # Convert specific file
"""

import os
import sys
import re
from pathlib import Path


def unescape_unicode(text):
    """Convert Unicode escapes (\\uXXXX) back to actual characters."""
    def replace_unicode(match):
        code_point = int(match.group(1), 16)
        return chr(code_point)

    # Match \uXXXX pattern (4 hex digits)
    pattern = r'\\u([0-9a-fA-F]{4})'
    return re.sub(pattern, replace_unicode, text)


def convert_file(input_path, output_path=None):
    """Convert a single properties file from escaped format to UTF-8."""
    if output_path is None:
        output_path = input_path

    try:
        # Read as ISO-8859-1 (ASCII compatible, preserves escape sequences)
        with open(input_path, 'r', encoding='iso-8859-1') as f:
            content = f.read()

        # Convert unicode escapes back to actual characters
        unescaped_content = unescape_unicode(content)

        # Write as UTF-8
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(unescaped_content)

        print(f"[OK] Converted: {input_path}")
        return True
    except Exception as e:
        print(f"[ERROR] Error converting {input_path}: {e}", file=sys.stderr)
        return False


def main():
    """Convert properties files from Unicode escape to UTF-8."""

    # Check for command line argument (specific file)
    if len(sys.argv) > 1:
        file_path = Path(sys.argv[1])
        if not file_path.exists():
            print(f"Error: File not found: {file_path}", file=sys.stderr)
            sys.exit(1)
        convert_file(file_path)
        return

    # Default: convert all files in messages directory
    resources_dir = Path(__file__).parent / 'src' / 'main' / 'resources' / 'messages'

    if not resources_dir.exists():
        print(f"Error: Directory not found: {resources_dir}", file=sys.stderr)
        sys.exit(1)

    properties_files = list(resources_dir.glob('*.properties'))

    if not properties_files:
        print(f"No .properties files found in {resources_dir}")
        sys.exit(0)

    print(f"Converting {len(properties_files)} properties files to UTF-8...")
    print("-" * 50)

    success_count = 0
    for prop_file in properties_files:
        if convert_file(prop_file):
            success_count += 1

    print("-" * 50)
    print(f"Completed: {success_count}/{len(properties_files)} files converted successfully")

    if success_count < len(properties_files):
        sys.exit(1)


if __name__ == '__main__':
    main()
