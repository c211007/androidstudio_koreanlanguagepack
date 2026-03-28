import json

translations = {
  "aiplugin.error.resource.exhausted.text.managedProject": "현재 사용량이 많아 일시적으로 사용량이 한도에 도달했습니다. 나중에 다시 시도해 주세요.",
  "aiplugin.error.unauthenticated.text": "서버에 인증 오류가 발생했습니다. 로그인해 주세요.",
  "aiplugin.error.unavailable.text": "서버를 사용할 수 없다는 오류가 발생했습니다. 연결 상태를 확인해 주세요. 버그라고 생각되면 보고서를 제출해 주세요.",
  "aiplugin.error.unimplemented.text": "서버에 구현되지 않음 오류가 발생했습니다. 보고서를 제출해 주세요.",
  "aiplugin.error.unknown.text": "알 수 없는 오류가 발생했습니다. 보고서를 제출해 주세요.",
  "aiplugin.error.for.managed.project": "Gemini Code Assist에 연결할 수 없습니다. 몇 분 후에 다시 시도해 주세요.",
  "aiplugin.error.onboarding.text": "Gemini Code Assist에 연결할 수 없습니다. 몇 분 후에 다시 시도해 주세요.",
  "aiplugin.error.fail.enable.api.title.text": "API를 사용 설정하지 못했습니다.",
  "aiplugin.error.message.banner.prefix": "Gemini Code Assist",
  "aiplugin.error.action.learnMore.text": "자세히 알아보기",
  "aiplugin.notification.group.analytics": "Gemini - 분석",
  "aiplugin.notification.group.recitation": "Gemini - 인용",
  "aiplugin.notification.group.feedback": "Gemini - 의견",
  "aiplugin.notification.group.general": "Gemini - 일반",
  "aiplugin.notification.group.license": "Gemini - 라이선스",
  "aiplugin.notification.group.login": "Gemini - 로그인",
  "aiplugin.notification.group.hats": "Gemini - 설문조사",
  "aiplugin.freetier.error.loadCodeAssist.retry.text": "다시 시도",
  "aiplugin.freetier.onboarding.gcpProject.loadCodeAssistSpinner.html": "<html><head><style>%%STYLE%%</style></head><body>Gemini Code Assist에 연결하는 중입니다.<p><p>몇 분 정도 걸릴 수 있습니다.",
  "aiplugin.freetier.onboarding.gcpProject.loadCodeAssistSpinner.markdown": "Gemini Code Assist에 연결하는 중입니다.\\n\\n몇 분 정도 걸릴 수 있습니다.",
  "aiplugin.freetier.privacy.optIn.text": "<html><body>Google 머신러닝 모델을 개발하고 개선하기 위해 Google에서 이 데이터를 사용하도록 허용합니다.<p>이 설정이 적용되기까지 최대 1분 정도 걸릴 수 있습니다.</p></body></html>",
  "aiplugin.freetier.privacy.optIn.error": "계정 설정을 로드하지 못했습니다. 나중에 다시 시도해 주세요.",
  "aiplugin.freetier.privacy.banner.markdown": "[Google 서비스 약관](https://policies.google.com/terms) 및 [사용 정책](https://policies.google.com/terms/generative-ai/use-policy)이 적용됩니다. \n  [개인정보처리방침]({0})은 대화, 코드 및 기타 데이터를 검토하고 Google AI를 개선하는 데 사용하는 방법을 설명합니다.\\n\\n\n  Gemini는 실수를 할 수 있으므로 다시 확인하고 [생성된 코드는 주의해서 사용하세요](https://g.co/legal/generative-code).",
  "aiplugin.freetier.privacy.minor.banner.markdown": "[Google 서비스 약관](https://policies.google.com/terms) 및 [사용 정책](https://policies.google.com/terms/generative-ai/use-policy)이 적용됩니다. \\n\\n\n  Gemini는 실수를 할 수 있으므로 다시 확인하고 [생성된 코드는 주의해서 사용하세요](https://g.co/legal/generative-code).",       
  "aiplugin.freetier.privacy.banner.learnMoreAction.title": "자세히 알아보기",       
  "aiplugin.freetier.privacy.banner.dismiss": "닫기",
  "aiplugin.freetier.privacy.dialog.title": "{0} 개인정보처리방침",
  "aiplugin.completion.statusBarWidget.status.gcpProjectNotSelected": "완성 비활성: Google Cloud 프로젝트가 선택되지 않음",
  "aiplugin.completion.statusBarWidget.status.loggedOut": "완성 비활성: 사용자가 로그인하지 않음",
  "aiplugin.completion.statusBarWidget.status.flagsNotUpdated": "완성 비활성: 로드 중...",
  "aiplugin.completion.statusBarWidget.status.userTierStateOnboarding": "완성 비활성: 온보딩이 완료되지 않음",
  "aiplugin.completion.statusBarWidget.status.userTierStateError": "완성 비활성: 오류 발생",
  "aiplugin.completion.statusBarWidget.status.userTierStateUnknown": "완성 비활성: 로드 중...",
  "aiplugin.completion.statusBarWidget.status.usageLimitExceeded": "완성 비활성: 사용 한도 초과",
  "aiplugin.completion.statusBarWidget.status.subscriptionRequired": "완성 비활성: 액세스 제한됨",
  "aiplugin.completion.statusBarWidget.tooltip.usageLimitExceeded": "{0}: 사용 한도 초과",
  "aiplugin.completion.statusBarWidget.status.network.error.general": "네트워크 오류",
  "aiplugin.completion.statusBarWidget.status.network.error.detailed": "Gemini Code Assist에 연결할 수 없습니다. 네트워크 설정을 확인하세요.",
  "aiplugin.gotItTour.statusbar.header": "설정 열기",
  "aiplugin.gotItTour.statusbar.message": "상태 표시줄에서 Gemini Code Assist 설정에 빠르게 액세스하세요.",
  "aiplugin.gotItTour.chatWindow.header": "Gemini에게 질문하기",
  "aiplugin.gotItTour.chatWindow.message": "코드에 관한 질문이 있나요? Gemini에게 물어보세요.",
  "aiplugin.gotItTour.editorSelection.header": "코드 변환",
  "aiplugin.gotItTour.editorSelection.message": "{0}을(를) 눌러 편집기에서 Gemini를 엽니다.",
  "aiplugin.gotItTour.inlineCompletion.header": "코드 제안 및 완성 검토",
  "aiplugin.gotItTour.inlineCompletion.message": "제안을 수락하려면 {0}을(를) 누르고<br>\n제안을 건너뛰려면 {1}을(를) 누르고<br>\n다른 제안을 보려면 {2}을(를) 누르세요.",  
  "aiplugin.gotItTour.finishchanges.header": "{0}을(를) 사용하여 변경 완료",       
  "aiplugin.gotItTour.finishchanges.message": "완성되지 않은 코드, 의사 코드, 일반 텍스트 또는 주석을 사용하여 파일에서 바로 Gemini에게 지시한 다음, {0}을(를) 사용하여 Gemini가 변경사항을 완료하도록 하세요.",
  "aiplugin.release.notes.link": "https://developers.google.com/gemini-code-assist/ui/release_notes",
  "aiplugin.release.notes.notification.title": "{0} 업데이트됨"
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
