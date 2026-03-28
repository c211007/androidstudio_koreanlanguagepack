import json

translations = {
  "sml.studiobot.timeline.newChat.warningDialog.changesMessage": "다른 채팅을 시작해도 현재 변경사항은 유지됩니다.",
  "sml.studiobot.timeline.newChat.warningDialog.stopResponseMessage": "다른 채팅을 시작하면 현재 응답이 중지됩니다.",
  "sml.studiobot.timeline.newChat.warningDialog.continue": "계속하시겠습니까?",
  "sml.studiobot.timeline.newChat.warningDialog.dontAskAgain": "다시 묻지 않음",
  "sml.studiobot.timeline.newChat.action.title": "새 채팅",
  "sml.studiobot.timeline.newChat.action.description": "새 채팅 세션 만들기",
  "sml.studiobot.timeline.showRecentChats.action.title": "최근 채팅",        
  "sml.studiobot.timeline.showRecentChats.action.description": "최근 채팅 세션 표시",
  "sml.studiobot.timeline.showRecentChats.dialog.title": "대화 삭제", 
  "sml.studiobot.timeline.showRecentChats.dialog.description": "이 대화는 기록에서 영구적으로 삭제됩니다.\\n\\n계속하시겠습니까?",     
  "sml.studiobot.timeline.showRecentChats.popup.title": "최근 채팅",
  "sml.studiobot.timeline.error.generic.title": "예기치 않은 오류",
  "sml.studiobot.timeline.error.generic.message": "나중에 다시 시도해 주세요.\\n\\n\n  오류: `{0}`",
  "sml.studiobot.timeline.error.network.generic.title": "예기치 않은 네트워크 오류",
  "sml.studiobot.timeline.error.network.generic.message": "나중에 다시 시도해 주세요.\\n\\n\n  오류: `상태 {0}`{1}",
  "sml.studiobot.timeline.error.network.clientSideRateLimit.title": "요청 한도 초과",
  "sml.studiobot.timeline.error.network.clientSideRateLimit.noCapSpecified.message": "시간당 대화 한도를 초과했습니다. 나중에 다시 시도해 주세요.",
  "sml.studiobot.timeline.error.network.clientSideRateLimit.message": "시간당 대화 한도({0}회)를 초과했습니다. 나중에 다시 시도해 주세요.",     
  "sml.studiobot.timeline.error.network.resourceExhausted.title": "네트워크 오류: 리소스 소진됨",
  "sml.studiobot.timeline.error.network.resourceExhausted.message": "시간당 프롬프트 요청 한도를 초과했습니다. 나중에 다시 시도해 주세요.",
  "sml.studiobot.timeline.error.network.permissionDenied.title": "네트워크 오류: 권한 거부됨",
  "sml.studiobot.timeline.error.network.permissionDenied.message": "다음 중 하나의 이유로 예기치 않은 인증 문제가 발생했습니다:\\n\\n\n  1. 로그인 인증 범위가 부족합니다. IDE를 다시 시작하고 Google 계정에 다시 로그인해 보세요.\\n\n  2. 아직 Gemini가 지원되지 않는 지역에서 사용 중입니다.",
  "sml.studiobot.timeline.error.network.unauthenticated.title": "인증 오류",
  "sml.studiobot.timeline.error.network.unauthenticated.message": "세션이 만료되었습니다. 다시 로그인해 주세요.",
  "sml.studiobot.timeline.error.network.timeout.title": "시간 초과",
  "sml.studiobot.timeline.error.network.timeout.message": "요청 시간이 초과되었습니다.", 
  "sml.studiobot.timeline.error.commands.title": "명령어 오류",
  "sml.studiobot.timeline.blocked.code.html": "<html><body>코드 스니펫이 차단되었습니다. <a href=\"https://d.android.com/r/studio-ui/gemini/code-blocked-error-message\">자세히 알아보기</a></body></html>",
  "sml.studiobot.timeline.blocked.code": "코드 스니펫이 차단되었습니다.",
  "sml.studiobot.timeline.queryState.isRunning": "Gemini가 응답 중\\u2026", 
  "sml.assistance.timeline.queryState.isRunning": "응답을 생성하는 중\\u2026", 
  "sml.studiobot.timeline.queryState.isRunning.thinking.generic": "생각하는 중\\u2026",
  "sml.studiobot.timeline.queryState.isRunning.thinking.template": "{0}\\u2026",
  "sml.studiobot.timeline.queryState.plan.current": "현재 계획",
  "sml.studiobot.timeline.queryState.plan.completed": "완료된 계획",
  "sml.studiobot.timeline.queryState.plan.stepNumber": "단계 {0}/{1}",
  "sml.studiobot.timeline.queryState.plan.stepNumber.variant": "{0}/{1}단계", 
  "sml.studiobot.timeline.queryState.isRunning.searching": "코드베이스 검색 중\\u2026",
  "sml.studiobot.timeline.queryState.isRunning.reading": "파일 읽는 중\\u2026",
  "sml.studiobot.timeline.queryState.isRunning.writing": "파일 수정 중\\u2026",
  "sml.studiobot.timeline.queryState.isRunning.analyzing": "코드 분석 중\\u2026",
  "sml.studiobot.timeline.queryState.isRunning.runningTool": "도구 실행 중\\u2026",
  "sml.studiobot.timeline.queryState.isRunning.waitingForAcceptReject": "변경사항 수락 또는 거부 대기 중\\u2026",
  "sml.studiobot.timeline.queryState.isRunning.waitingForPermission": "권한 부여(또는 거부) 대기 중\\u2026",
  "sml.studiobot.timeline.queryState.isStopping": "응답 중단 중\\u2026",   
  "sml.studiobot.timeline.error.userCancel.title": "응답 중단됨",
  "sml.studiobot.timeline.error.userCancel.text": "Gemini 응답이 중단되었습니다.",
  "sml.assistance.timeline.error.userCancel.text": "AI 응답이 중단되었습니다.",
  "sml.studiobot.codeBlock.action.extractToFunction.text": "이 위치에 스니펫을 추가할 수 없습니다. 새 함수로 추출하시겠습니까?",
  "sml.studiobot.codeBlock.action.extractToMethod.text": "이 위치에 스니펫을 추가할 수 없습니다. 새 메서드로 추출하시겠습니까?"
}

with open("missing_translations/missing_keys_korean.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for file_info in data.get("new_files", []):
    if file_info.get("filename") == "SmlBundle.properties":
        file_info["keys"].update(translations)
        break

with open("missing_translations/missing_keys_korean.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)
