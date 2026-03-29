import json

file_path = "missing_translations/missing_keys_korean.json"

with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

for file_obj in data.get('new_files', []):
    if 'filePath' in file_obj:
        file_obj['filename'] = file_obj.pop('filePath')
    if 'translations' in file_obj:
        file_obj['keys'] = file_obj.pop('translations')

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("JSON structure fixed.")
