import json

translations = {
  "aiplugin.outlines.banner.action.text": "개요 생성",
  "aiplugin.finishchanges.editor.hint.empty.text": "팁: 완성되지 않은 코드, 의사 코드, 일반 텍스트 또는 주석을 사용하여 파일에서 바로 Gemini에게 지시한 다음, {0}을(를) 사용하여 Gemini가 변경사항을 완료하도록 하세요.",
  "aiplugin.finishchanges.editor.hint.editing.text": "{0} 파일 변경 완료 | {1} 닫기",
  "aiplugin.finishchanges.banner.text": "{0}을(를) 사용하여 이 파일의 변경 완료"
}

with open("missing_translations/missing_keys_korean.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for file_info in data.get("new_files", []):
    if file_info.get("filename") == "SmlIjBundle.properties":
        keys_dict = file_info.get("keys", file_info.get("properties", {}))
        keys_dict.update(translations)
        file_info["keys"] = keys_dict
        break

with open("missing_translations/missing_keys_korean.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)
