import json

ko_dict = {
  "highlighting.for.0.is.suspended": "내부 오류로 인해 {0} 파일에서 구문 강조 표시가 일시적으로 꺼졌습니다.",
  "highlighting.action.text.ignore": "무시",
  "highlighting.action.text.try.k2": "K2 모드 사용해 보기…",
  "automatically.declared.based.on.the.expected.type": "예상되는 유형에 따라 자동으로 선언됨",
  "extension.implicit.receiver": "암시적 확장 수신자",
  "implicit.receiver": "암시적 수신자",
  "0.smart.cast.to.1": "{1}(으)로 {0} 스마트 변환",
  "smart.cast.to.0": "{0}(으)로 스마트 변환",
  "inspection.message.never.used": "{0}이(가) 사용되지 않았습니다.",
  "safe.delete.family": "안전하게 삭제",
  "safe.delete.text.0": "''{0}'' 안전하게 삭제",
  "safe.delete.secondary.ctor.text.0": "보조 생성자 ''{0}'' 안전하게 삭제",
  "safe.delete.primary.ctor.text.0": "기본 생성자 ''{0}'' 안전하게 삭제",
  "safe.delete.parameter.text.0": "매개변수 ''{0}'' 안전하게 삭제"
}

with open('missing_translations/missing_keys_korean.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

filename = "KotlinBaseHighlightingBundle.properties"
found = False
for file_entry in data.get('new_files', []):
    if file_entry['filename'] == filename:
        file_entry['keys'].update(ko_dict)
        found = True
        break
if not found:
    data.setdefault('new_files', []).append({"filename": filename, "keys": ko_dict})

print(f"Updated {filename} (Keys 1-14)")

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
