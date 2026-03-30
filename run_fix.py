import re
from pathlib import Path
from datetime import datetime

# 작업 디렉토리
messages_dir = Path(r'c:\Users\klanary\Desktop\vscode 모음\android_korean\androidstudio_koreanlanguagepack\src\main\resources\messages')

# 모든 *_ko.properties 파일 찾기
files = list(messages_dir.glob('*_ko.properties'))
print(f"Found {len(files)} files")
print("="*70)

fixed = 0
skipped = 0
errors = 0

for file_path in sorted(files):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if not content.startswith('# ╔'):
            skipped += 1
            continue
        
        bundle_name = file_path.name.replace('_ko.properties', '.properties')
        date = datetime.now().strftime('%Y-%m-%d')
        
        simple_header = f"""# Auto-generated Korean translation file
# Generated: {date}
# Original file: {bundle_name}

"""
        
        pattern = r'^# ╔.*?# ╚[^\n]*\n+'
        new_content = re.sub(pattern, simple_header, content, flags=re.DOTALL)
        
        with open(file_path, 'w', encoding='utf-8', newline='\n') as f:
            f.write(new_content)
        
        print(f"✓ {file_path.name}")
        fixed += 1
        
    except Exception as e:
        print(f"✗ {file_path.name}: {e}")
        errors += 1

print("="*70)
print(f"✓ Fixed: {fixed}")
print(f"- Skipped: {skipped}")
print(f"✗ Errors: {errors}")
print("="*70)
