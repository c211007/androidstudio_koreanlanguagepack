import json

ko_dict = {
  "action.JsonCopyPointer.text": "JSON 포인터 복사",
  "cannot.sort.properties": "속성을 정렬할 수 없음",
  "file.is.readonly": "파일이 읽기 전용입니다.",
  "not.applicable.in.batch.mode": "일괄 모드에서는 적용할 수 없습니다.",
  "sorry.this.fix.is.not.available.in.batch.mode": "죄송합니다, 이 수정 사항은 일괄 모드에서 사용할 수 없습니다.",
  "replace.with.allowed.value": "허용된 값으로 바꾸기",
  "json.schema": "JSON 스키마",
  "remove.prohibited.property": "금지된 속성 제거",
  "fix.property.name.spelling": "''{0}''(으)로 맞춤법 조정",
  "add.missing.0": "누락된 {0} 추가",
  "add.missing.properties": "누락된 속성 추가",
  "remove.duplicated.items": "중복된 항목 제거",
  "intention.add.not.required.properties.text": "JSON 스키마에서 모든 속성 채우기",
  "intention.add.not.required.properties.family.name": "선택적 속성 누락됨",
  "path.to.file.or.directory.relative.to.project.root.or.file.name": "프로젝트 루트를 기준으로 한 파일이나 디렉터리의 경로 또는 *.config.json과 같은 파일 이름 패턴",
  "json.property.keys": "JSON 속성 키",
  "json.string.values": "JSON 문자열 값",
  "property.0.is.deprecated.1": "''{0}'' 속성은 지원 중단되었습니다: {1}",
  "add.mapping.for.a": "다음에 대한 매핑 추가: ",
  "no.schema.mappings.defined": "스키마 매핑이 정의되지 않았습니다.",
  "filetype.json5.description": "JSON5",
  "unnamed.desc": "<이름 없음>",
  "navigate.to.duplicates": "중복으로 이동",
  "navigate.to.duplicates.header": "''{0}''의 중복",
  "navigate.to.duplicates.desc": "#{1}번째 줄의 ''{0}''",
  "annotation.property.key": "속성 키",
  "color.page.attribute.keyword": "키워드",
  "color.page.attribute.string": "문자열",
  "color.page.attribute.number": "숫자",
  "color.page.attribute.colon": "콜론",
  "color.page.attribute.comma": "쉼표",
  "color.page.attribute.brackets": "대괄호",
  "color.page.attribute.braces": "중괄호",
  "color.page.attribute.block.comment": "블록 주석",
  "color.page.attribute.line.comment": "줄 주석",
  "color.page.attribute.property.key": "속성 키",
  "color.page.attribute.invalid.escape.sequence": "잘못된 이스케이프 시퀀스",
  "color.page.attribute.valid.escape.sequence": "유효한 이스케이프 시퀀스",
  "color.page.attribute.parameter": "매개변수",
  "qualified.name.qualified": "정규화된 이름"
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

print(f"Updated {filename} (Keys 81-120)")

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
