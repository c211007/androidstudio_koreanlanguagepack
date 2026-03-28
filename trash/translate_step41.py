import json
with open('missing_translations/missing_keys_korean.json', 'r', encoding='utf-8') as f:
    ko_data = json.load(f)

translations = {
  "action.structureview.show.non.public": "비공개(Non-public)",
  "action.structureview.show.properties": "속성(Properties)",
  "file.structure.toggle.show.anonymous.classes": "익명 클래스",
  "file.structure.toggle.show.anonymous.classes.check.box.text": "익명 클래스",
  "file.structure.toggle.show.collapse.show.lambdas": "람다(Lambdas)",
  "static.class.initializer": "{0}클래스 초기화자"
}

ko_error_bundle = next((x for x in ko_data['new_files'] if x['filename'] == 'JavaStructureViewBundle.properties'), None)
if ko_error_bundle is None:
    ko_error_bundle = {'filename': 'JavaStructureViewBundle.properties', 'keys': {}, 'key_count': 0}
    ko_data['new_files'].append(ko_error_bundle)

ko_error_bundle['keys'].update(translations)
ko_error_bundle['key_count'] = len(ko_error_bundle['keys'])

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(ko_data, f, ensure_ascii=False, indent=2)

print("Updated JavaStructureViewBundle.properties (Final)")