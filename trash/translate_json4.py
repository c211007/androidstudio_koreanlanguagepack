import json

ko_dict = {
  "qualified.name.pointer": "JSON 포인터",
  "schema.of.version": "JSON 스키마 {0}",
  "schema.of.version.deprecated": "JSON 스키마 버전 {0}",
  "schema.configuration.error.empty.file.path": "빈 파일 경로는 항목과 일치하지 않습니다.",
  "schema.configuration.error.empty.pattern": "빈 패턴은 항목과 일치하지 않습니다.",
  "schema.configuration.error.unknown.mapping": "알 수 없는 매핑 종류",
  "schema.configuration.project.directory": "{0}[프로젝트 디렉터리]",
  "schema.configuration.error.empty.path": "스키마 경로가 비어 있습니다.",
  "schema.configuration.error.invalid.url": "잘못된 스키마 URL",
  "schema.configuration.error.invalid.url.resource": "잘못된 URL 리소스",
  "schema.configuration.error.file.does.not.exist": "스키마 파일이 존재하지 않습니다.",
  "schema.configuration.error.empty.name": "스키마 이름이 비어 있습니다.",
  "schema.configuration.error.duplicate.name": "중복된 스키마 이름: ''{0}''",
  "schema.configuration.error.conflicting.mappings.title": "충돌하는 매핑:\\n{0}",
  "schema.configuration.error.conflicting.mappings.desc": "''{1}'' 스키마에 대한 ''{0}'', ''{3}'' 스키마에 대한 ''{2}''",
  "schema.configuration.mapping.empty.area.string": "볼 JSON 스키마를 선택하세요.",
  "schema.configuration.mapping.empty.area.alt.string": "JSON 스키마 파일을 추가하고 사용을 구성하세요.",
  "schema.configuration.mapping.remote": "원격 스키마 URL",
  "schema.mapping.file": "파일",
  "schema.mapping.pattern": "파일 경로 패턴",
  "schema.mapping.directory": "디렉터리",
  "schema.catalog.hint": "<a href=\"https://schemastore.org/json/\">SchemaStore API</a>를 사용하여 스키마가 다운로드되고 할당됩니다.",
  "schema.catalog.remote.hint": "스키마 중 일부가 IDE와 함께 번들로 제공되더라도 스키마는 항상 SchemaStore에서 다운로드됩니다.",
  "schema.widget.registered.schemas": "등록된 스키마",
  "schema.widget.store.schemas": "SchemaStore.org 스키마",
  "schema.widget.add.mapping": "새 스키마 매핑…",
  "schema.widget.no.mapping": "파일에 대한 JSON 스키마 무시",
  "schema.widget.stop.ignore.file": "파일에 대한 JSON 스키마 무시 중지",
  "schema.widget.edit.mappings": "스키마 매핑 편집…",
  "schema.widget.load.mappings": "SchemaStore 매핑 로드",
  "schema.widget.prefix.json.files": "JSON: ",
  "schema.widget.prefix.other.files": "스키마: ",
  "schema.widget.display.name": "JSON 스키마",
  "schema.widget.tooltip.json.files": "JSON 스키마: ",
  "schema.widget.tooltip.other.files": "JSON 스키마의 유효성 검사됨: ",
  "schema.widget.service": "JSON 스키마 서비스",
  "schema.widget.conflict.message.prefix": "이 파일에 매핑된 JSON 스키마가 여러 개 있습니다.<br/>",
  "schema.widget.conflict.message.postfix": "스키마 (!)",
  "schema.widget.download.in.progress.tooltip": "다운로드가 예약되어 있거나 진행 중입니다.",
  "schema.widget.download.in.progress.label": "JSON 스키마 다운로드 중"
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

print(f"Updated {filename} (Keys 121-160)")

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
