import json

ko_dict = {
  "json.schema.add.schema.chooser.title": "JSON 스키마 파일 선택",
  "json.schema.annotation.not.allowed.property": "''{0}'' 속성은 허용되지 않습니다.",
  "json.schema.annotation.not.allowed.property.possibly.typo": "''{0}'' 속성은 허용되지 않습니다. 오타가 아닌가요?",
  "json.schema.conflicting.mappings": "경고: 매핑이 충돌합니다. <a href=\"#\">세부 정보 표시</a>",
  "json.schema.file.selector.title": "스키마 파일 또는 URL:",
  "json.schema.version.selector.title": "스키마 버전:",
  "json.schema.file.not.found": "파일을 찾을 수 없음",
  "json.schema.inspection.compliance.name": "JSON 스키마 준수",
  "json.schema.inspection.deprecation.name": "지원 중단된 JSON 속성",
  "json.schema.inspection.case.insensitive.enum": "열거형 값의 대소문자를 구분하지 않는 일치",
  "json.schema.ref.refs.inspection.name": "해결되지 않은 '$ref' 및 '$schema' 참조",
  "json.schema.ref.file.not.found": "''{0}'' 파일을 찾을 수 없습니다.",
  "json.schema.ref.cannot.resolve.path": "''{0}'' 경로를 확인할 수 없습니다.",
  "json.schema.ref.cannot.resolve.id": "''{0}'' ID를 확인할 수 없습니다.",
  "json.schema.ref.no.array.element": "배열에 인덱스가 ''{0}''인 요소가 포함되어 있지 않습니다.",
  "json.schema.ref.no.property": "''{0}'' 속성을 찾을 수 없습니다.",
  "settings.display.name.json": "JSON",
  "settings.json.schema.add.mapping": "매핑 추가",
  "settings.json.schema.edit.mapping": "매핑 편집",
  "settings.json.schema.remove.mapping": "매핑 제거",
  "json.intention.category.name": "JSON",
  "json.intention.sort.properties": "속성을 알파벳순으로 정렬",
  "configurable.JsonSmartKeysConfigurable.display.name": "JSON",
  "configurable.JsonSchemaMappingsConfigurable.display.name": "JSON 스키마 매핑",
  "configurable.JsonSchemaCatalogConfigurable.display.name": "원격 JSON 스키마",
  "settings.smart.keys.insert.missing.comma.on.enter": "Enter를 누를 때 누락된 쉼표 삽입",
  "settings.smart.keys.insert.missing.comma.after.matching.braces.and.quotes": "일치하는 중괄호 및 따옴표 뒤에 누락된 쉼표 삽입",
  "settings.smart.keys.automatically.manage.commas.when.pasting.json.fragments": "JSON 조각을 붙여넣을 때 자동으로 쉼표 관리",
  "settings.smart.keys.escape.text.on.paste.in.string.literals": "문자열 리터럴에 붙여넣을 때 텍스트 이스케이프",
  "settings.smart.keys.automatically.add.quotes.to.property.names.when.typing.comma": "':'를 입력할 때 속성 이름에 자동으로 따옴표 추가",
  "settings.smart.keys.automatically.add.whitespace.when.typing.comma.after.property.names": "속성 이름 뒤에 ':'를 입력할 때 자동으로 공백 추가",
  "settings.smart.keys.automatically.move.comma.after.the.property.name.if.typed.inside.quotes": "따옴표 안에 입력한 경우 자동으로 속성 이름 뒤로 ':' 이동",
  "settings.smart.keys.automatically.move.comma.after.the.property.value.or.array.element.if.inside.quotes": "따옴표 안에 있는 경우 속성 값 또는 배열 요소 뒤에 자동으로 쉼표 이동",
  "checkbox.use.schemastore.org.json.schema.catalog": "schemastore.org JSON 스키마 카탈로그 사용",
  "checkbox.allow.downloading.json.schemas.from.remote.sources": "원격 소스에서 JSON 스키마 다운로드 허용",
  "checkbox.always.download.the.most.recent.version.of.schemas": "항상 최신 버전의 스키마 다운로드",
  "action.DumbAware.JsonSchemaMappingsConfigurable.text.add": "추가",
  "action.DumbAware.JsonSchemaMappingsConfigurable.description.add": "추가",
  "filetype.json.description": "JSON",
  "filetype.json_lines.description": "JSON 라인"
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

print(f"Updated {filename} (Keys 41-80)")

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
