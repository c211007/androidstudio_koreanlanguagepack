import json

ko_dict = {
  "feature.is.not.fully.supported.0": "K2 모드: {0}이(가) 완전히 지원되지 않습니다.",
  "incomplete.project.state.pending.reference": "프로젝트가 완전히 로드될 때까지 확인되지 않음"
}

with open('missing_translations/missing_keys_korean.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

filename = "K2HighlightingBundle.properties"
found = False
for file_entry in data.get('new_files', []):
    if file_entry['filename'] == filename:
        file_entry['keys'].update(ko_dict)
        found = True
        break
if not found:
    data.setdefault('new_files', []).append({"filename": filename, "keys": ko_dict})

print(f"Updated {filename} (Keys 1-2)")

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
