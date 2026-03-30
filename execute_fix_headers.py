#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script to fix .properties file headers
Removes decorative box headers and replaces with simple comments
"""

import os
import re
from datetime import datetime
from pathlib import Path

def fix_header(file_path):
    """Fix header in a single .properties file"""
    
    # Read file content
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if file has decorative header (starts with # ╔)
    if not content.startswith('# ╔'):
        return False
    
    # Extract bundle name from filename
    bundle_name = Path(file_path).name.replace('_ko.properties', '.properties')
    
    # Get current date
    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # Create simple header
    simple_header = f"""# Auto-generated Korean translation file
# Generated: {date}
# Original file: {bundle_name}

"""
    
    # Remove decorative header using regex
    # Pattern: from start (# ╔) to after (# ╚) line, including subsequent blank lines
    pattern = r'^# ╔.*?# ╚[^\n]*\n+'
    new_content = re.sub(pattern, simple_header, content, flags=re.DOTALL)
    
    # Write back to file
    with open(file_path, 'w', encoding='utf-8', newline='\n') as f:
        f.write(new_content)
    
    return True

# 현재 디렉토리를 작업 디렉토리로 설정
os.chdir(r'c:\Users\klanary\Desktop\vscode 모음\android_korean\androidstudio_koreanlanguagepack')

# Main function
messages_dir = Path(r'src\main\resources\messages')

if not messages_dir.exists():
    print(f"Error: Directory not found: {messages_dir}")
else:
    # Get all *_ko.properties files
    files = list(messages_dir.glob('*_ko.properties'))
    
    print(f"Found {len(files)} Korean translation files")
    print("=" * 50)
    
    fixed_count = 0
    skipped_count = 0
    
    for file_path in sorted(files):
        print(f"Processing: {file_path.name}...", end=' ')
        
        try:
            if fix_header(file_path):
                print("✓ Fixed")
                fixed_count += 1
            else:
                print("- Skipped (no decorative header)")
                skipped_count += 1
        except Exception as e:
            print(f"✗ Error: {e}")
    
    print("=" * 50)
    print(f"Summary:")
    print(f"  Fixed: {fixed_count} files")
    print(f"  Skipped: {skipped_count} files")
    print("=" * 50)
