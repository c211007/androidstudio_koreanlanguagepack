import json

with open('missing_translations/missing_keys_korean.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

if "KotlinBundle.properties" in data:
    ko_dict = data.pop("KotlinBundle.properties")
    filename = "KotlinBundle.properties"
    found = False
    for file_entry in data.get('new_files', []):
        if file_entry['filename'] == filename:
            file_entry['keys'].update(ko_dict)
            found = True
            break
    if not found:
        data.setdefault('new_files', []).append({"filename": filename, "keys": ko_dict})
    
    with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print("Repaired KotlinBundle.properties.")
else:
    print("No repair needed.")
