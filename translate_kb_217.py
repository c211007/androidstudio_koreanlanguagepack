import json

translations = {
  "sml.studiobot.codeBlock.action.functionName.text": "newFunction",
  "sml.studiobot.codeBlock.action.applyChanges.text": "diff 모드에서 미리보기",   
  "sml.studiobot.codeBlock.action.acceptChanges.text": "변경사항 수락",        
  "sml.studiobot.codeBlock.action.rollbackChanges.text": "변경사항 롤백",    
  "sml.studiobot.codeBlock.action.insertAtCursor.text": "커서 위치에 삽입",     
  "sml.studiobot.codeBlock.action.insertDependencies.text": "프로젝트에 종속 항목 추가",
  "sml.studiobot.codeBlock.action.insertDependency.text": "프로젝트에 {0} 추가", 
  "sml.studiobot.codeBlock.action.insertManifest.text": "매니페스트에 병합",  
  "sml.studiobot.codeBlock.action.insertInScratch.text": "플레이그라운드에서 탐색",
  "sml.studiobot.codeBlock.action.insertIntoNewFile.text": "새 파일에 삽입",
  "sml.studiobot.codeBlock.action.insertIntoNewFileType.text": "새 {0} 파일에 삽입",
  "sml.studiobot.codeBlock.action.insertIntoNewFile.chooseModuleDialog.message": "{0} 파일을 추가할 모듈 선택:",
  "sml.studiobot.codeBlock.action.mergeCode.text": "제안 병합",
  "sml.studiobot.codeBlock.action.mergeResources.text": "리소스 병합",      
  "sml.studiobot.codeBlock.action.methodName.text": "newMethod",
  "sml.studiobot.codeBlock.action.nameSuggestions.text": "{0} 이름 바꾸기?",
  "sml.studiobot.codeBlock.action.showTopicDocs.text": "{0} 문서 표시",
  "sml.studiobot.codeBlock.action.diffToggle.tooltip.formattedDiff": "서식이 지정된 diff 표시",
  "sml.studiobot.codeBlock.action.diffToggle.tooltip.rawText": "원본 diff 표시", 
  "sml.studiobot.codeBlock.action.fixCode.jvm.progress.description": "가져오기 검색 중\\u2026",
  "sml.studiobot.codeBlock.expandable.expand": "전체 코드 블록 표시",
  "sml.studiobot.codeBlock.expandable.collapse": "코드 블록 접기",
  "sml.studiobot.feedback.downvote": "이 응답에 반대",
  "sml.studiobot.feedback.upvote": "이 응답에 찬성",
  "sml.studiobot.feedback.moreFeedback": "의견 제공",
  "sml.studiobot.feedback.moreFeedback.description": "이 응답이 유용하지 않은 이유를 알려주시면 개선에 도움이 됩니다.",
  "sml.studiobot.feedback.dialog.title": "선택사항 의견 제공",
  "sml.studiobot.feedback.dialog.submit.text": "제출",
  "sml.studiobot.feedback.dialog.question.text": "이 평가를 선택한 이유는 무엇인가요?",
  "sml.studiobot.feedback.dialog.issueType.wrong": "부정확함",
  "sml.studiobot.feedback.dialog.issueType.toxic": "불쾌감을 주거나 안전하지 않음",       
  "sml.studiobot.feedback.dialog.issueType.irrelevant": "관련 없음",
  "sml.studiobot.feedback.dialog.comments.hint": "응답을 개선할 수 있도록 자세한 내용을 알려주세요.",
  "sml.studiobot.citations.title": "외부 참조",
  "sml.studiobot.prompt.citations.title": "코드베이스 참조",
  "sml.studiobot.includedFiles.title": "포함된 파일",
  "group.sml.studiobot.internal.group.text": "Gemini",
  "sml.studiobot.internal.chatModelSelect.textWithoutName": "채팅 백엔드 설정", 
  "sml.studiobot.internal.chatModelSelect.text": "채팅 백엔드 설정(현재: {0})",
  "sml.studiobot.internal.completionModelSelect.textWithoutName": "완성 모델 설정",
  "sml.studiobot.internal.completionModelSelect.text": "완성 모델 설정(현재: {0})",
  "sml.studiobot.internal.modelSelect.textWithoutName": "Gemini 백엔드 설정",   
  "sml.studiobot.internal.modelSelect.text": "Gemini 백엔드 설정(현재: {0})",
  "sml.studiobot.internal.modelSelect.dialogTitle": "Gemini 백엔드 설정",       
  "sml.studiobot.internal.resetOnboarding.text.toNotCompleted": "Gemini 온보딩을 '완료되지 않음'으로 설정",
  "sml.studiobot.internal.resetOnboarding.text.toCompleted": "Gemini 온보딩을 '완료됨'으로 설정",
  "sml.studiobot.internal.resetOnboarding.text.generic": "Gemini 온보딩 완료 여부 전환",
  "sml.studiobot.internal.resetOnboarding.dialogTitle": "Gemini 온보딩 상태 설정",
  "sml.studiobot.internal.resetOnboarding.dialogMessage.toNotCompleted": "온보딩 상태를 '완료되지 않음'으로 설정하시겠습니까?",
  "sml.studiobot.internal.resetOnboarding.dialogMessage.toCompleted": "온보딩 상태를 '완료됨'으로 설정하시겠습니까?"
}

with open("missing_translations/missing_keys_korean.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for file_info in data.get("new_files", []):
    if file_info.get("filename") == "SmlBundle.properties":
        file_info["keys"].update(translations)
        break

with open("missing_translations/missing_keys_korean.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)
