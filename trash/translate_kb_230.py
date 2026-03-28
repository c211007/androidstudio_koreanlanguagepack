import json

translations = {
  "typo.severity.capitalized": "오타",
  "typo.severity.count.message": "{0}개의 {0, choice, 0#오타|1#오타|2#오타}",     
  "dictionary.name.application.level": "애플리케이션 수준",
  "dictionary.name.project.level": "프로젝트 수준",
  "dictionary.name.not.specified": "지정되지 않음",
  "dictionary.generator.progress.title": "사전 생성 중",
  "dictionary.generator.processing.title": "사전 처리 중: {0}",        
  "dictionary.generator.scanning.folder.title": "폴더 스캔 중: {0}"
}

with open("missing_translations/missing_keys_korean.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for file_info in data.get("new_files", []):
    if file_info.get("filename") == "SpellCheckerBundle.properties":
        keys_dict = file_info.get("keys", file_info.get("properties", {}))
        keys_dict.update(translations)
        file_info["keys"] = keys_dict
        break

with open("missing_translations/missing_keys_korean.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)
