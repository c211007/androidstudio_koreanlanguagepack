import json

ko_dict = {
  "kotlin.javascript.meta.file": "Kotlin JavaScript 메타 파일",
  "klib.metadata.short": "Klib 메타데이터",
  "kotlin.built.in.file.type": "\"Kotlin 내장 선언\""
}

with open('missing_translations/missing_keys_korean.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

filename = "KotlinBasePsiBundle.properties"
found = False
for file_entry in data.get('new_files', []):
    if file_entry['filename'] == filename:
        file_entry['keys'].update(ko_dict)
        found = True
        break
if not found:
    data.setdefault('new_files', []).append({"filename": filename, "keys": ko_dict})

print(f"Updated {filename}")

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
