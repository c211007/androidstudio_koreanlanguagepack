import json

ko_dict = {
  "schema.widget.error.label": "JSON 스키마 오류",
  "schema.widget.error.not.a.schema": "파일이 스키마가 아닙니다.",
  "schema.widget.error.cant.download": "스키마 다운로드 오류",
  "schema.widget.bundled.postfix": " (번들로 제공됨)",
  "schema.widget.no.schema.label": "JSON 스키마 없음",
  "schema.widget.no.schema.tooltip": "정의된 JSON 스키마 없음",
  "schema.widget.package.postfix": "(패키지: ''{0}'')",
  "schema.widget.conflict.popup.title": "JSON 스키마 충돌 매핑",
  "schema.widget.checking.state.text": "{0}분석 중…",
  "schema.widget.checking.state.tooltip": "분석 중…",
  "schema.reader.cant.load.file": "JSON 스키마 파일 ''{0}''을(를) 로드할 수 없습니다.",
  "schema.reader.cant.load.model": "JSON 스키마 파일 ''{0}''의 코드 모델을 로드할 수 없습니다.",
  "schema.reader.file.too.large": "넘 커서(파일 크기가 {1}바이트임) ''{0}''에서 JSON 스키마가 로드되지 않았습니다.",
  "schema.reader.file.empty": "''{0}''에서 JSON 스키마가 로드되지 않았습니다. 파일이 비어 있습니다.",
  "schema.reader.file.not.found.or.error": "JSON 스키마를 찾을 수 없거나 ''{0}''에 오류가 포함되어 있습니다: {1}",
  "schema.documentation.deprecated.postfix": " (지원 중단됨)",
  "schema.validation.property": "{0} 속성",
  "schema.validation.properties": "{0} 속성",
  "schema.validation.array.shorter.than": "배열이 {0}보다 짧습니다.",
  "schema.validation.array.longer.than": "배열이 {0}보다 깁니다.",
  "schema.validation.array.not.contains": "'contains' 규칙과 일치하지 않습니다.",
  "schema.validation.array.no.extra": "추가 항목은 허용되지 않습니다.",
  "schema.validation.array.no.unevaluated": "평가되지 않은 항목은 허용되지 않습니다.",
  "schema.validation.not.unique": "항목이 고유하지 않습니다.",
  "schema.validation.constant.schema": "속성이 허용되지 않습니다.",
  "schema.validation.enum.mismatch": "값은 다음 중 하나여야 합니다: {0}",
  "schema.validation.against.not": "'not' 스키마에 대해 유효성을 검사합니다.",
  "schema.validation.integer.expected": "정수 값이 필요합니다.",
  "schema.validation.number.expected": "Double 값이 필요합니다.",
  "schema.validation.not.multiple.of": "{0}의 배수가 아닙니다.",
  "schema.validation.greater.than.exclusive.maximum": "제외 최댓값 {0}보다 큽니다.",
  "schema.validation.greater.than.maximum": "최댓값 {0}보다 큽니다.",
  "schema.validation.less.than.exclusive.minimum": "제외 최솟값 {0}보다 작습니다.",
  "schema.validation.less.than.minimum": "최솟값 {0}보다 작습니다.",
  "schema.validation.missing.required.property.or.properties": "필수 항목 누락됨: {0}",
  "schema.validation.missing.not.required.property.or.properties": "선택 항목 누락됨: {0}",
  "schema.validation.number.of.props.less.than": "속성 수가 {0}개보다 적습니다.",
  "schema.validation.number.of.props.greater.than": "속성 수가 {0}개보다 많습니다.",
  "schema.validation.violated.dependency": "종속성이 위반되었습니다: ''{1}''이(가) 지정되었으므로 {0}을(를) 지정해야 합니다.",
  "schema.validation.string.shorter.than": "문자열이 {0}자보다 짧습니다."
}

with open('missing_translations/missing_keys_korean.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

filename = "JsonBundle.properties"
found = False
for file_entry in data.get('new_files', []):
    if file_entry['filename'] == filename:
        file_entry['keys'].update(ko_dict)
        found = True
        break
if not found:
    data.setdefault('new_files', []).append({"filename": filename, "keys": ko_dict})

print(f"Updated {filename} (Keys 161-200)")

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
