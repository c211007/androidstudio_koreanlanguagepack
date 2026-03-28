import json

with open('missing_translations/missing_keys_korean.json', 'r', encoding='utf-8') as f:
    korean_data = json.load(f)

total_new_done = 0
for file_entry in korean_data.get('new_files', []):
    total_new_done += len(file_entry.get('keys', {}))

total_existing_done = 0
for file_entry in korean_data.get('existing_files', []):
    total_existing_done += len(file_entry.get('missing_keys', {}))

print(f"Korean New Files Total translated keys: {total_new_done}")
print(f"Korean Existing Files Total translated keys: {total_existing_done}")
