import json

translations = {
  "title.textmate.bundle.error": "TextMate 번들 오류",
  "message.textmate.bundle.error": "다음 번들을 읽을 수 없습니다:\\n{0}",
  "button.add.bundle": "번들 추가",
  "textmate.live.template.name": "TextMate 스니펫",
  "textmate.expand.live.template.command.name": "템플릿 확장",
  "title.built.in": "기본 제공",
  "textmate.bundle.load.error": "TextMate 번들 {0}을(를) 로드할 수 없습니다.",
  "textmate.cant.register.bundle": "`{0}` 번들의 형식을 알 수 없습니다.",
  "textmate.disable.bundle.notification.action": "`{0}` 번들 비활성화",
  "textmate.remove.title": "{0,choice,1#번들|2#번들}을 삭제하시겠습니까?",
  "filetype.textmate.description": "TextMate 번들을 통해 지원되는 파일",
  "textmate.loading.bundles.title": "TextMate 번들 로드 중",
  "textmate.configuration.description": "이 페이지를 사용하여 {0}에서 기본적으로 지원하지 않는 언어에 대한 TextMate 번들을 추가하세요.",
  "notification.group.textmate.bundles": "TextMate 번들 로드 실패"
}

with open("missing_translations/missing_keys_korean.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for file_info in data.get("new_files", []):
    if file_info.get("filename") == "TextMateBundle.properties":
        keys_dict = file_info.get("keys", file_info.get("properties", {}))
        keys_dict.update(translations)
        file_info["keys"] = keys_dict
        break
else:
    data.setdefault("new_files", []).append({
        "filename": "TextMateBundle.properties",
        "keys": translations
    })

with open("missing_translations/missing_keys_korean.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)
