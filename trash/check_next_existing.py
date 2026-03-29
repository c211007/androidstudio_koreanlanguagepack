import json

with open('missing_keys.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

with open('missing_translations/missing_keys_korean.json', 'r', encoding='utf-8') as f:
    korean_data = json.load(f)

for file_entry in data.get('existing_files', []):
    filename = file_entry['filename']
    keys = file_entry.get('missing_keys', {})
    
    korean_file_entry = next((f for f in korean_data.get('existing_files', []) if f['filename'] == filename), {})
    korean_keys = korean_file_entry.get('missing_keys', {})
    
    missing_keys = {k: v for k, v in keys.items() if k not in korean_keys}
    
    if missing_keys:
        print(f"Next existing file: {filename} (Missing {len(missing_keys)}/{len(keys)} keys)")
        print(json.dumps(dict(list(missing_keys.items())[:40]), indent=2, ensure_ascii=False))
        break
else:
    print("All existing files caught up too!")
