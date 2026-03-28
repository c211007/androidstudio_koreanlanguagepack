import json

file_path = "missing_translations/missing_keys_korean.json"

with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

vcs_keys = {}
files_to_keep = []

# Merge all keys for VcsBundle.properties
for file_obj in data.get('new_files', []):
    if file_obj.get('filename') in ("VcsBundle.properties", "intellij/vcs-release/VcsBundle.properties"):
        vcs_keys.update(file_obj.get('keys', {}))
    else:
        files_to_keep.append(file_obj)

# Add the merged back
if vcs_keys:
    files_to_keep.append({
        "filename": "VcsBundle.properties",
        "keys": vcs_keys
    })

data['new_files'] = files_to_keep

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Merged VcsBundle keys. Total keys for VcsBundle.properties: {len(vcs_keys)}")
