import json

translations = {
  "sml.studiobot.timeline.agent.tool.build.title": "빌드",
  "sml.plugin.settings.skills.title": "스킬",
  "sml.plugin.settings.skills.use.prebundled": "사전 번들된 스킬 사용",        
  "sml.plugin.settings.skills.use.prebundled.comment": "사용으로 설정하면 플러그인에서 제공하는 사전 번들된 스킬을 사용할 수 있습니다.",
  "sml.studiobot.settings.compression.title": "컨텍스트 압축",
  "sml.studiobot.settings.compression.auto_compress_at": "자동 압축 기준:",   
  "sml.studiobot.settings.compression.percent": "비율(%):",
  "sml.studiobot.settings.compression.tokens": "토큰:",
  "sml.studiobot.suggestCommitMessage.unavailable.amend": "커밋 메시지 제안 (amend 커밋을 지원하지 않음)",
  "sml.studiobot.suggestCommitMessage.unavailable.changed": "커밋 메시지 제안 (선택된 변경 파일이 1개 이상 필요함)",
  "sml.studiobot.suggestCommitMessage.unavailable.context": "커밋 메시지 제안 (Gemini 컨텍스트 사용 설정이 필요함)",
  "sml.studiobot.suggestCommitMessage.unavailable.enabled": "커밋 메시지 제안 (Gemini 사용 설정이 필요함)",
  "sml.studiobot.settings.modelProviders.remote.schema.openai": "OpenAI 호환",
  "sml.studiobot.settings.modelProviders.remote.schema.anthropic": "Anthropic 호환",
  "sml.studiobot.editor.changes.toolbar.next.file": "다음 파일 비교",        
  "sml.studiobot.editor.changes.toolbar.next.file.description": "다음 파일의 변경사항 확인",
  "sml.studiobot.editor.changes.toolbar.previous.file": "이전 파일 비교",
  "sml.studiobot.editor.changes.toolbar.previous.file.description": "이전 파일의 변경사항 확인",
  "sml.studiobot.editor.changes.toolbar.files.count": "{1}개 파일 중 {0}번째",       
  "sml.studiobot.notification.waitingForUserInput.title": "에이전트 대기 중",   
  "sml.studiobot.notification.waitingForUserInput.message": "채팅 창에서 작업이 필요합니다.",
  "sml.studiobot.notification.conversationFinished.title": "에이전트 대화 완료됨",
  "sml.studiobot.notification.conversationFinished.message": "에이전트가 {0}에 완료됨",
  "sml.studiobot.notification.conversationStopped.message": "에이전트가 {0} 후 중지됨",
  "sml.studiobot.notification.action.open": "에이전트 창 열기",
  "sml.studiobot.notification.group.agent": "Gemini 에이전트 알림",       
  "sml.studiobot.deprecation.action.updateStudio": "Android 스튜디오 업데이트",     
  "sml.studiobot.timeline.thought.title.completed.withTime": "{0} 동안 생각함", 
  "sml.studiobot.timeline.thought.title.completed.withoutTime": "잠시 생각함"
}

with open("missing_translations/missing_keys_korean.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for file_info in data.get("new_files", []):
    if file_info.get("filename") == "SmlBundle.properties":
        file_info["keys"].update(translations)
        break

with open("missing_translations/missing_keys_korean.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)
