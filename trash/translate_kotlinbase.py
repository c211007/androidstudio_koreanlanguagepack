import json

ko_dict = {
  "searching.for.implicit.usages": "암시적 사용 검색 중…",
  "kotlin.repair.indices.group.name": "Kotlin 색인 무효화",
  "kotlin.indices.corrupted": "Kotlin 색인이 손상되었습니다.",
  "dialog.message.collect.usages": "사용 검색 중"
}

with open('missing_translations/missing_keys_korean.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

filename = "KotlinBaseAnalysisBundle.properties"
found = False
for file_entry in data.get('new_files', []):
    if file_entry['filename'] == filename:
        file_entry['keys'].update(ko_dict)
        found = True
        break
if not found:
    data.setdefault('new_files', []).append({"filename": filename, "keys": ko_dict})

print(f"Updated {filename} (Keys 1-4)")

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
