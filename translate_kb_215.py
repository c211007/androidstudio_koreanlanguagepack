import json

translations = {
  "sml.studiobot.timeline.changesDrawer.inEditor.revert": "되돌리기",
  "sml.studiobot.timeline.changesDrawer.inEditor.revert.description": "이 파일의 모든 변경사항 되돌리기",
  "sml.studiobot.timeline.changesDrawer.inEditor.changeNavigation": "{1}개 중 {0}번째",
  "sml.studiobot.timeline.context.geminiDisabled": "프로젝트 컨텍스트 사용 중지됨",  
  "sml.studiobot.timeline.context.geminiFilesCount": "파일 {0}개",
  "sml.studiobot.timeline.context.suggestedHeader": "추천",
  "sml.studiobot.timeline.context.header": "컨텍스트 ({0})",
  "sml.studiobot.timeline.context.remove": "컨텍스트에서 파일 제거",
  "sml.studiobot.timeline.context.removeAll": "지우기",
  "sml.studiobot.timeline.context.userHeader": "사용자가 첨부함",
  "sml.studiobot.timeline.plan.cancel": "취소",
  "sml.studiobot.timeline.plan.step.status.working": "작업 중\\u2026",
  "sml.studiobot.timeline.plan.dismiss": "닫기",
  "sml.studiobot.timeline.plan.step.status.completed": "작업 완료!",       
  "sml.studiobot.timeline.plan.step.status.files.changed": "파일 변경됨",     
  "sml.studiobot.timeline.query.emptyText": "Gemini에게 질문",
  "sml.studiobot.timeline.query.emptyText.withContextAttachmentHint": "Gemini에게 질문. 소스 파일을 첨부하려면 @filename을 사용하고, 저장된 프롬프트를 불러오려면 @prompt를 사용하세요.",  
  "sml.studiobot.timeline.query.emptyText.withFolderContextAttachmentHint": "Gemini에게 질문. 소스 파일이나 폴더를 첨부하려면 @name을 사용하고, 저장된 프롬프트를 불러오려면 @prompt를 사용하세요.",
  "sml.studiobot.timeline.query.emptyText.withQueueHint": "다른 프롬프트 대기열에 추가",
  "sml.studiobot.timeline.query.emptyText.withPendingToolCallHint": "대기 중인 도구 호출 수정 또는 관련 질문",
  "sml.studiobot.timeline.query.nonEmptyText.queueHintGhostText": "대기열에 추가하려면\\u00A0{0}\\u00A0누르기",
  "sml.studiobot.timeline.queue.remove": "대기열에서 제거",
  "sml.studiobot.timeline.queue.send": "이 프롬프트 보내기",
  "sml.ai.assistance.timeline.query.emptyText": "AI에게 질문",
  "sml.ai.assistance.timeline.query.emptyText.withContextAttachmentHint": "AI에게 질문. 소스 파일을 첨부하려면 @filename을 사용하고, 저장된 프롬프트를 불러오려면 @prompt를 사용하세요.",  
  "sml.ai.assistance.timeline.query.emptyText.withFolderContextAttachmentHint": "AI에게 질문. 소스 파일이나 폴더를 첨부하려면 @name을 사용하고, 저장된 프롬프트를 불러오려면 @prompt를 사용하세요.",
  "sml.studiobot.timeline.query.submitButton.text": "제출",
  "sml.studiobot.timeline.query.stopQuery": "중지",
  "sml.studiobot.timeline.query.optionsPopup.title": "에이전트 옵션",
  "sml.studiobot.timeline.query.optionsPopup.autoApprove.title": "변경사항 자동 수락",
  "sml.studiobot.timeline.query.optionsPopup.askToEdit.title": "파일 수정 요청",
  "sml.studiobot.timeline.query.modelPicker.addApiKey": "API 키 추가\\u2026",   
  "sml.studiobot.timeline.query.modelPicker.manageModels": "모델 관리\\u2026",
  "sml.studiobot.timeline.query.modelPicker.signInToGoogle": "Google에 로그인\\u2026",
  "sml.studiobot.timeline.query.modelPicker.setUpGemini": "Gemini 설정\\u2026",
  "sml.studiobot.timeline.query.historyPopup.title": "쿼리 방문 기록",
  "sml.studiobot.timeline.query.historyAction.title": "쿼리 방문 기록 표시",     
  "sml.studiobot.timeline.deleteMessage.button.tooltip": "메시지 쌍 삭제", 
  "sml.studiobot.timeline.deleteMessage.dialog.title": "메시지 쌍 삭제",   
  "sml.studiobot.timeline.deleteMessage.dialog.message": "메시지와 응답이 영구적으로 삭제됩니다.",
  "sml.studiobot.timeline.editMessage.button.tooltip": "수정",
  "sml.studiobot.timeline.editMessage.button.cancel.text": "취소",
  "sml.studiobot.timeline.editMessage.button.update.text": "업데이트",
  "sml.studiobot.timeline.regenerateMessage.button.tooltip": "응답 다시 생성",
  "sml.studiobot.timeline.regenerateMessage.button.contentDescription": "다시 생성",
  "sml.studiobot.timeline.clearHistory.action.title": "대화 기록 지우기",
  "sml.studiobot.timeline.clearHistory.action.description": "이전 대화를 모두 지웁니다.",
  "sml.studiobot.timeline.clearHistory.dialog.title": "대화 기록 지우기",
  "sml.studiobot.timeline.clearHistory.dialog.message": "이 작업은 대화 기록을 영구적으로 삭제합니다.\\n\\n계속하시겠습니까?",
  "sml.studiobot.timeline.newChat.warningDialog.title": "채팅 전환"
}

with open("missing_translations/missing_keys_korean.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for file_info in data.get("new_files", []):
    if file_info.get("filename") == "SmlBundle.properties":
        file_info["properties"].update(translations)
        break

with open("missing_translations/missing_keys_korean.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)
