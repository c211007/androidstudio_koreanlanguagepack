#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import re
from datetime import datetime
from pathlib import Path

def fix_header(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if not content.startswith('# ╔'):
            return False
        
        bundle_name = Path(file_path).name.replace('_ko.properties', '.properties')
        date = datetime.now().strftime('%Y-%m-%d')
        
        simple_header = f"""# Auto-generated Korean translation file
# Generated: {date}
# Original file: {bundle_name}

"""
        
        pattern = r'^# ╔.*?# ╚[^\n]*\n+'
        new_content = re.sub(pattern, simple_header, content, flags=re.DOTALL)
        
        with open(file_path, 'w', encoding='utf-8', newline='\n') as f:
            f.write(new_content)
        
        return True
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False

messages_dir = Path(r'c:\Users\klanary\Desktop\vscode 모음\android_korean\androidstudio_koreanlanguagepack\src\main\resources\messages')
files = list(messages_dir.glob('*_ko.properties'))

print(f"Found {len(files)} Korean translation files")
print("=" * 50)

fixed_count = 0
skipped_count = 0

for file_path in sorted(files):
    if fix_header(file_path):
        fixed_count += 1
    else:
        skipped_count += 1

print("=" * 50)
print(f"Summary:")
print(f"  Fixed: {fixed_count} files")
print(f"  Skipped: {skipped_count} files")
print("=" * 50)
