#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Process all *_ko.properties files and replace decorative headers with simple headers
"""
import os
import re
from datetime import datetime
from pathlib import Path

def fix_header(file_path):
    """Fix header in a single .properties file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if file has decorative header (starts with # ╔)
        if not content.startswith('# ╔'):
            return False
        
        # Extract bundle name from filename
        bundle_name = Path(file_path).name.replace('_ko.properties', '.properties')
        
        # Get current date
        date = datetime.now().strftime('%Y-%m-%d')
        
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
    except Exception as e:
        print(f"Error: {e}")
        return False

# Main execution
if __name__ == '__main__':
    messages_dir = Path(r'c:\Users\klanary\Desktop\vscode 모음\android_korean\androidstudio_koreanlanguagepack\src\main\resources\messages')
    
    if not messages_dir.exists():
        print(f"Error: Directory not found: {messages_dir}")
        exit(1)
    
    # Get all *_ko.properties files
    files = list(messages_dir.glob('*_ko.properties'))
    
    print(f"Found {len(files)} Korean translation files")
    print("=" * 60)
    
    fixed_count = 0
    skipped_count = 0
    
    for file_path in sorted(files):
        result = fix_header(file_path)
        if result:
            print(f"✓ Fixed: {file_path.name}")
            fixed_count += 1
        else:
            skipped_count += 1
    
    print("=" * 60)
    print(f"Summary:")
    print(f"  ✓ Fixed: {fixed_count} files")
    print(f"  - Skipped: {skipped_count} files")
    print("=" * 60)
