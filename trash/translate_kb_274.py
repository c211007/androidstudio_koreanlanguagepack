import json

translations = {
  "group.names.testng.issues": "TestNG",
  "action.text.tests.for": "{0} 에 대한 테스트",
  "action.text.unknown.test.object": "알 수 없음",
  "action.text.temp.suite": "임시 스위트",
  "action.text.tests.in.package": "\"{0}\" 내 테스트",
  "dialog.message.file.not.found": "''{0}'' 파일을 찾을 수 없습니다.",
  "async.stack.trace.for.exceptions.label": "예외에 대한 비동기 스택 트레이스"
}

with open("missing_translations/missing_keys_korean.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for file_info in data.get("new_files", []):
    if file_info.get("filename") == "TestngBundle.properties":
        keys_dict = file_info.get("keys", file_info.get("properties", {}))
        keys_dict.update(translations)
        file_info["keys"] = keys_dict
        break

with open("missing_translations/missing_keys_korean.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)
