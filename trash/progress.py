import json

with open('missing_keys.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

with open('missing_translations/missing_keys_korean.json', 'r', encoding='utf-8') as f:
    korean_data = json.load(f)

total_new = 0
total_new_done = 0
total_existing = 0
total_existing_done = 0

for file_entry in data.get('new_files', []):
    keys = file_entry.get('keys', {})
    total_new += len(keys)
    korean_file_entry = next((f for f in korean_data.get('new_files', []) if f['filename'] == file_entry['filename']), {})
    korean_keys = korean_file_entry.get('keys', {})
    total_new_done += len(korean_keys)

for file_entry in data.get('existing_files', []):
    keys = file_entry.get('missing_keys', {})
    total_existing += len(keys)
    korean_file_entry = next((f for f in korean_data.get('existing_files', []) if f['filename'] == file_entry['filename']), {})
    korean_keys = korean_file_entry.get('missing_keys', {})
    total_existing_done += len(korean_keys)

print(f"New Files Progress: {total_new_done} / {total_new}")
print(f"Existing Files Progress: {total_existing_done} / {total_existing}")
