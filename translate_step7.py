import json
with open('missing_translations/missing_keys_korean.json', 'r', encoding='utf-8') as f:
    ko_data = json.load(f)

translations = {
  "psi.search.inheritors.of.class.progress": "{0}의 하위 항목을 검색하는 중\\u2026",
  "psi.search.inheritors.progress": "하위 항목을 검색하는 중\\u2026"
}

ko_error_bundle = next((x for x in ko_data['new_files'] if x['filename'] == 'JavaIndexingBundle.properties'), None)
if not ko_error_bundle:
    ko_error_bundle = {'filename': 'JavaIndexingBundle.properties', 'keys': {}, 'key_count': 0}
    ko_data['new_files'].append(ko_error_bundle)
ko_error_bundle['keys'].update(translations)
ko_error_bundle['key_count'] = len(ko_error_bundle['keys'])

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(ko_data, f, ensure_ascii=False, indent=2)

print("Updated JavaIndexingBundle.properties")
