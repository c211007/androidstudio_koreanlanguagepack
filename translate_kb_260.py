import json

translations = {
  "svn.create.external.below.action": "외부 생성…",
  "svn.create.external.below.description": "URL을 선택하고 svn:external 속성을 추가하고 필요에 따라 체크아웃합니다."
}

with open("missing_translations/missing_keys_korean.json", "r", encoding="utf-8") as f:
    data = json.load(f)

found = False
for file_info in data.get("new_files", []):
    if file_info.get("filename") == "SvnDeprecatedMessagesBundle.properties":
        keys_dict = file_info.get("keys", file_info.get("properties", {}))
        keys_dict.update(translations)
        file_info["keys"] = keys_dict
        found = True
        break

if not found:
    data.setdefault("new_files", []).append({
        "filename": "SvnDeprecatedMessagesBundle.properties",
        "keys": translations
    })

with open("missing_translations/missing_keys_korean.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)
