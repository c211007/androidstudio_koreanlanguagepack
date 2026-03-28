import json

ko_dict = {
  "intention.suppress.family": "경고 억제",
  "intention.suppress.text": "{1} {2}에 대한 ''{0}'' 억제",
  "progress.title.calculating.names": "제안할 이름 계산 중…",
  "progress.title.shortening.references": "참조 축소 중…"
}

with open('missing_translations/missing_keys_korean.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

filename = "KotlinBaseFe10CodeInsightBundle.properties"
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
