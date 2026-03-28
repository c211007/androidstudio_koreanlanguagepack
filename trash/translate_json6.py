import json

ko_dict = {
  "schema.validation.string.longer.than": "문자열이 {0}자보다 깁니다.",
  "schema.validation.invalid.string.pattern": "오류 కారణంగా 패턴으로 문자열을 검사할 수 없습니다: {0}",
  "schema.validation.string.violates.pattern": "문자열이 패턴을 위반합니다: ''{0}''",
  "schema.validation.actual": "실제: ",
  "schema.validation.incompatible.types": "호환되지 않는 유형입니다.",
  "schema.validation.required.one": "필수: {0}.{1}",
  "schema.validation.required.one.of": "다음 중 하나가 필요합니다: {0}.{1}",
  "schema.validation.to.more.than.one": "두 개 이상의 변형에 대해 유효성을 검사합니다.",
  "schema.validation.one.of.property.sets.required": "다음 속성 세트 중 하나가 필요합니다: {0}",
  "schema.validation.at.least.one.of.property.sets.required": "다음 속성 세트 중 하나 이상이 있어야 합니다: {0}",
  "schema.add.mapping.kind.text": "{0} 추가",
  "notification.group.json.schema": "JSON 스키마 로드 실패",
  "new.schema": "새 스키마",
  "action.JsonJacksonReformatAction.text": "JSON 서식 다시 지정",
  "JsonJacksonReformatAction.progress.title.json.reformatting": "JSON 서식 다시 지정 중",
  "JsonJacksonReformatAction.command.name.json.reformat": "JSON 서식 다시 지정",
  "JsonJacksonReformatAction.dialog.title.json.reformatting": "JSON 서식 다시 지정",
  "JsonJacksonReformatAction.dialog.message.this.action.not.undoable.do.you.want.to.reformat.document": "이 작업은 되돌릴 수 없습니다. 문서의 서식을 다시 지정하시겠습니까?",
  "folding.collapsed.array.text": "[ {0}개 {0,choice,0#요소|1#요소|2#요소} ]",
  "folding.collapsed.object.text": "'{' {0}개 {0,choice,0#키|1#키|2#키} '}'",
  "JsonFoldingSettings.title": "JSON",
  "JsonFoldingSettings.show.key.count": "접힌 JSON에 키 개수 표시",
  "JsonFoldingSettings.show.first.key": "접힌 JSON에 첫 번째 키 표시",
  "JsonFoldingSettings.show.first.key.description": "접힌 JSON 객체에 항상 첫 번째 키를 표시합니다. 그렇지 않으면 \"id\" 또는 \"name\" 키가 있을 경우 표시됩니다."
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

print(f"Updated {filename} (Keys 201-224)")

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
