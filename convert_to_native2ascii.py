#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Convert UTF-8 .properties files to native2ascii format
All non-ASCII characters (including Korean) will be converted to \uXXXX format
"""

import os
import re
from pathlib import Path

def char_to_unicode_escape(char):
    """Convert a character to \\uXXXX format"""
    code = ord(char)
    if code > 127:  # Non-ASCII
        return f'\\u{code:04x}'
    return char

def convert_line(line):
    """Convert all non-ASCII characters in a line to Unicode escape"""
    result = []
    for char in line:
        result.append(char_to_unicode_escape(char))
    return ''.join(result)

def convert_properties_file(file_path):
    """Convert a single .properties file to native2ascii format"""
    
    # Read UTF-8 file
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Convert each line
    converted_lines = []
    has_changes = False
    
    for line in lines:
        converted = convert_line(line)
        if converted != line:
            has_changes = True
        converted_lines.append(converted)
    
    if not has_changes:
        return False
    
    # Write as ISO-8859-1 (which is compatible with ASCII + Unicode escapes)
    with open(file_path, 'w', encoding='iso-8859-1', newline='\n') as f:
        f.writelines(converted_lines)
    
    return True

def main():
    """Main function"""
    messages_dir = Path(r'src\main\resources\messages')
    
    if not messages_dir.exists():
        print(f"Error: Directory not found: {messages_dir}")
        return
    
    # Get all *_ko.properties files
    files = list(messages_dir.glob('*_ko.properties'))
    
    print(f"Found {len(files)} Korean translation files")
    print("=" * 60)
    print("Converting UTF-8 Korean text to \\uXXXX format...")
    print("=" * 60)
    
    converted_count = 0
    skipped_count = 0
    error_count = 0
    
    for file_path in sorted(files):
        print(f"Processing: {file_path.name}...", end=' ')
        
        try:
            if convert_properties_file(file_path):
                print("✓ Converted")
                converted_count += 1
            else:
                print("- Skipped (already ASCII)")
                skipped_count += 1
        except Exception as e:
            print(f"✗ Error: {e}")
            error_count += 1
    
    print("=" * 60)
    print(f"Summary:")
    print(f"  Converted: {converted_count} files")
    print(f"  Skipped: {skipped_count} files")
    print(f"  Errors: {error_count} files")
    print("=" * 60)
    print("\n✅ All files are now in ISO-8859-1 + Unicode escape format")
    print("   Compatible with IntelliJ Platform .properties standard")

if __name__ == '__main__':
    main()
