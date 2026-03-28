import json

translations = {
  "color.settings.toml.keys": "키(Keys)",
  "color.settings.toml.comments": "주석",
  "color.settings.toml.boolean": "부울(Boolean)",
  "color.settings.toml.date": "날짜(Date)",
  "filetype.toml.description": "TOML",
  "inspection.group.toml": "TOML",
  "inspection.toml.message.inline.tables.on.single.line": "인라인 테이블은 한 줄에 표시되어야 합니다.",
  "inspection.toml.message.trailing.commas.in.inline.tables": "인라인 테이블에서는 후행 쉼표(trailing comma)가 허용되지 않습니다.",
  "inspection.toml.unresolved.reference.display.name": "해결되지 않은 참조",
  "intention.category.toml": "TOML",
  "intention.toml.name.expand.into.separate.table": "별도의 테이블로 확장",
  "intention.toml.name.remove.trailing.comma": "후행 쉼표 제거"
}

with open("missing_translations/missing_keys_korean.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for file_info in data.get("new_files", []):
    if file_info.get("filename") == "TomlBundle.properties":
        keys_dict = file_info.get("keys", file_info.get("properties", {}))
        keys_dict.update(translations)
        file_info["keys"] = keys_dict
        break
else:
    data.setdefault("new_files", []).append({
        "filename": "TomlBundle.properties",
        "keys": translations
    })

with open("missing_translations/missing_keys_korean.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)
