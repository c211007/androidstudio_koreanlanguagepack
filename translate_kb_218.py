import json

translations = {
  "sml.studiobot.internal.debugLogging.text.generic": "Gemini 디버그 로깅 전환",
  "sml.studiobot.internal.debugLogging.text.enable": "Gemini 디버그 로깅 사용",
  "sml.studiobot.internal.debugLogging.text.disable": "Gemini 디버그 로깅 사용 안함",
  "sml.studiobot.internal.debugToolCalls.text.enable": "도구 호출 디버그 정보 표시",
  "sml.studiobot.internal.debugToolCalls.text.disable": "도구 호출 디버그 정보 숨기기",
  "sml.completion.statusBarWidget.displayName": "Gemini",
  "sml.completion.statusBarWidget.tooltip.active": "{0}: 활성",
  "sml.completion.statusBarWidget.tooltip.inactive": "{0}: 비활성",
  "sml.completion.statusBarWidget.configureAction.text": "Gemini 구성\\u2026",
  "sml.completion.statusBarWidget.enableCompletionAction.text": "AI 코드 완성 사용",
  "sml.completion.statusBarWidget.loginAction.text.login": "Gemini에 로그인\\u2026",
  "sml.completion.statusBarWidget.loginAction.text.authorize": "Gemini 승인\\u2026",
  "sml.completion.statusBarWidget.status.disabled": "완성 비활성: 설정에서 사용 안함으로 지정됨",
  "sml.completion.statusBarWidget.status.contextSharingDisabled": "완성 비활성: 컨텍스트 인식 꺼짐",
  "sml.completion.statusBarWidget.status.loggedOut": "완성 비활성: 사용자가 로그인하지 않음",
  "sml.completion.statusBarWidget.status.notAuthorized": "완성 비활성: Gemini가 승인되지 않음",
  "sml.completion.statusBarWidget.status.indexing": "완성 비활성: 색인 생성 중에는 사용할 수 없음",
  "sml.completion.statusBarWidget.status.unsupportedFileType": "완성 비활성: 지원되지 않는 파일 형식",
  "sml.completion.statusBarWidget.status.aiexclude": "완성 비활성: 파일이 .aiexclude에 의해 차단됨",
  "sml.completion.statusBarWidget.status.gitignore": "완성 비활성: 파일이 .gitignore에 의해 차단됨",
  "sml.completion.statusBarWidget.status.notInProjectOrVcs": "완성 비활성: 파일이 프로젝트의 일부가 아니거나 버전 제어 루트 아래에 없음",
  "sml.completion.statusBarWidget.status.onboardingNotComplete": "완성 비활성: 온보딩이 완료되지 않음",
  "sml.completion.statusBarWidget.logoutAction.text": "로그아웃 ({0})",
  "sml.completion.statusBarWidget.openDocumentationAction.text": "문서 열기",
  "sml.completion.statusBarWidget.openReleaseNotes.text": "새로운 기능(출시 노트)",
  "sml.studiobot.diff.unifiedView.name": "통합(Unified)",
  "sml.studiobot.diff.splitView.name": "나란히(Side-by-side)",
  "sml.studiobot.diff.acceptAllChanges": "변경사항 수락",
  "sml.studiobot.diff.acceptFileChanges": "수락",
  "sml.studiobot.diff.acceptFileChangesAndClose": "수락 \\\\&\\\\& 닫기",    
  "sml.studiobot.diff.refinePrompt": "미세 조정",
  "sml.studiobot.diff.regenerate": "다시 생성",
  "sml.studiobot.diff.back": "뒤로",
  "sml.studiobot.diff.forward": "앞으로",
  "sml.studiobot.diff.random.access": "{0}: {1}",
  "sml.studiobot.diff.history.title": "프롬프트 {0}: {1}",
  "sml.studiobot.diff.browse.popup.name": "변환 방문 기록",
  "sml.aiplugin.submit.feedback.action.text": "의견 제출",
  "sml.aiplugin.statusBarWidget.action.text": "개인정보 보호 설정",
  "sml.slash.command.unrecognized": "알 수 없는 명령어 `/{0}`입니다.  \\n슬래시로 시작하는 질문은 로컬 명령어로 해석됩니다.  \\n지원되는 명령어:  \\n{1}",
  "group.sml.studiobot.gemini.library.group.text": "프롬프트 라이브러리",
  "sml.studiobot.settings.prompt.templates.enabled": "프롬프트 라이브러리 메뉴에 표시",
  "sml.studiobot.settings.prompt.templates.enabled.in.slash.commands": "편집기 내 프롬프트에 표시",
  "sml.studiobot.settings.prompt.templates.display.name": "프롬프트 라이브러리",     
  "sml.studiobot.settings.prompt.templates.add.new": "새 프롬프트 템플릿",     
  "sml.studiobot.settings.prompt.templates.error.empty.name": "프롬프트 이름을 지정하세요.",
  "sml.studiobot.settings.prompt.templates.error.empty.prompt": "프롬프트 텍스트를 추가하세요.",
  "sml.studiobot.settings.prompt.templates.error.duplicate.name": "{0} 템플릿이 이미 존재합니다. 다른 템플릿 이름을 지정해 주세요.",
  "sml.studiobot.settings.prompt.templates.error.name.too.long": "프롬프트 템플릿 이름이 너무 깁니다.",
  "sml.studiobot.settings.prompt.templates.group.hint": "<html><body><center>'+' 버튼을 클릭하여 프롬프트를 만들거나 기존 프롬프트를 선택하세요.</center></body></html>"
}

with open("missing_translations/missing_keys_korean.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for file_info in data.get("new_files", []):
    if file_info.get("filename") == "SmlBundle.properties":
        file_info["keys"].update(translations)
        break

with open("missing_translations/missing_keys_korean.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)
