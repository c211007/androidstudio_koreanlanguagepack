import json

translations = {
  "ai.plugin.settings.recitation.notification.fail.log.message": "{0} 파일에 인용을 기록하지 못했습니다.<br>이유: {1}",
  "ai.plugin.settings.prompt.recitation.tooltip": "코드 블록: {0}:{1}-{2}:{3}이(가) {4} 파일에서 참조되었습니다: {5}\\n라이선스: 알 수 없음\\n<br>",
  "ai.plugin.settings.block.cited.code.suggestion": "외부 인용 소스와 일치하는 제안 차단",
  "ai.plugin.settings.block.cited.code.suggestion.blocked": "관리자가 이 기능을 사용 중지했습니다.",
  "ai.plugin.settings.streaming.chat.enable": "Gemini 채팅 응답 스트리밍(권장)",
  "ai.plugin.settings.next.edit.enable.title": "다음 수정 예측 사용",  
  "ai.plugin.settings.next.edit.enable.message": "입력하는 동안 Gemini가 현재 줄 이외의 향후 수정사항을 제안하도록 허용합니다.",
  "ai.plugin.settings.outlines": "개요",
  "ai.plugin.settings.outlines.enable.title": "개요 자동 생성",   
  "ai.plugin.settings.outlines.enable.message": "개요 패널이 열려 있을 때 열려 있는 모든 파일의 개요를 자동으로 만듭니다. <a href=\"{0}\"/>자세히 알아보기.</a>",
  "aiplugin.onboarding.auth.introBlurb.html": "<html><head><style>%%STYLE%%</style></head><body>{0}의 Gemini Code Assist에 오신 것을 환영합니다.\n  <p><p>AI 기반 채팅, 코드 완성, 코드 생성 등의 기능을 사용하여 워크플로를 강화해 보세요.",    
  "aiplugin.onboarding.auth.introBlurb.markdown": "{0}의 Gemini Code Assist에 오신 것을 환영합니다.\\n\\n\n  AI 기반 채팅, 코드 완성, 코드 생성 등의 기능을 사용하여 워크플로를 강화해 보세요.",
  "aiplugin.onboarding.auth.cta.login": "로그인",
  "aiplugin.onboarding.auth.cta.description": "로그인할 브라우저 열기",     
  "aiplugin.onboarding.auth.cta.login.copylink": "링크 복사",
  "aiplugin.onboarding.auth.cta.login.comment": "링크가 자동으로 열리지 않으면 복사하여 브라우저에 붙여넣으세요.",
  "aiplugin.onboarding.auth.logged.in": "로그인됨: {0}",
  "aiplugin.onboarding.gcpProject.welcome.html": "<html><head><style>%%STYLE%%</style></head><body>설정이 완료되었습니다.\n  <p><p>GCA에 오신 것을 환영합니다...",
  "aiplugin.onboarding.gcpProject.introBlurb.html": "<html><head><style>%%STYLE%%</style></head><body><b>Gemini Code Assist Standard 또는 Enterprise</b>를 사용하려면 Google Cloud 프로젝트를 선택해야 합니다.\n  <p><p>계속하면 Google이 사용자를 대신하여 선택한 프로젝트에 대해 Google Cloud에서 Gemini Code Assist를 사용하는 데 필요한 API를 사용 설정하도록 허용하는 데 동의하는 것으로 간주됩니다.",
  "aiplugin.onboarding.gcpProject.introBlurb.markdown": "**Gemini Code Assist Standard 또는 Enterprise**를 사용하려면 Google Cloud 프로젝트를 선택해야 합니다.\n  \\n\\n계속하면 Google이 사용자를 대신하여 선택한 프로젝트에 대해 Google Cloud에서 Gemini Code Assist를 사용하는 데 필요한 API를 사용 설정하도록 허용하는 데 동의하는 것으로 간주됩니다.",   
  "aiplugin.onboarding.gcpProject.introBlurbStandardTier.html": "<html><head><style>%%STYLE%%</style></head><body>현재 계정은 무료 버전인\n  개인용 Gemini Code Assist에 적합하지 않습니다. <a href=\"https://developers.google.com/gemini-code-assist/ui/onboarding/different-version\">자세히 알아보기</a> \n  <p><p>로그아웃하고 다른 개인 Google 계정으로 다시 로그인해 보세요.",
  "aiplugin.onboarding.gcpProject.introBlurbStandardTier.markdown": "현재 계정은 무료 버전인\n  개인용 Gemini Code Assist에 적합하지 않습니다. [자세히 알아보기](https://developers.google.com/gemini-code-assist/ui/onboarding/different-version)\n  \\n\\n로그아웃하고 다른 개인 Google 계정으로 다시 로그인해 보세요.",
  "aiplugin.onboarding.gcpProject.select": "Google Cloud 프로젝트 선택",     
  "aiplugin.onboarding.gcpProject.switchAccount": "계정 전환",
  "aiplugin.onboarding.gcpProject.signOut": "로그아웃",
  "aipligin.onboarding.gcpProject.intro.subtext.html": "<html><head><body> \n  <p>다른 버전의 Gemini Code Assist를 찾고 계신가요? <a href=\"https://developers.google.com/gemini-code-assist/ui/onboarding/different-version\">자세히 알아보기</a></p></body></html>",
  "aipligin.onboarding.gcpProject.intro.subtext.markdown": "다른 버전의 Gemini Code Assist를 찾고 계신가요? [자세히 알아보기](https://developers.google.com/gemini-code-assist/ui/onboarding/different-version)",
  "aipligin.onboarding.gcpProject.intro.selectProject.subtext.html": "<html><head><body> \n  <p>Gemini Code Assist Standard 또는 Enterprise를 계속 사용하려면 <a href=\"#\">Google Cloud 프로젝트를 선택</a>하세요.</p></body></html>",      
  "aipligin.onboarding.gcpProject.intro.selectProject.subtext.markdown": "Gemini Code Assist Standard 또는 Enterprise를 계속 사용하려면 [Google Cloud 프로젝트를 선택](#)하세요.",
  "aiplugin.onboarding.gcpProject.selected.label": "선택한 프로젝트: {0}",     
  "aiplugin.onboarding.tier.introBlurb.html.wrapper": "<html><head><style>%%STYLE%%</style></head><body>{0}",
  "aiplugin.onboarding.tier.introBlurb.html": "<html><head><style>%%STYLE%%</style></head><body>요구사항에 더 적합한 제품을 선택하세요.",
  "aiplugin.onboarding.tierBlocked.default.message.markdown": "현재 계정은 무료 버전인\n  개인용 Gemini Code Assist에 적합하지 않습니다. [자세히 알아보기](https://developers.google.com/gemini-code-assist/ui/onboarding/different-version)\n  \\n\\n다른 개인 Google 계정으로 로그인해 보세요.",
  "aiplugin.onboarding.tierBlocked.message.markdown": "{0} [자세히 알아보기](https://developers.google.com/gemini-code-assist/ui/onboarding/different-version)",     
  "aiplugin.onboarding.tierBlocked.switchAccount.markdown": "{0} [자세히 알아보기](https://developers.google.com/gemini-code-assist/ui/onboarding/different-version)\n  \\n\\n다른 개인 Google 계정으로 로그인해 보세요.",
  "aiplugin.onboarding.tierBlocked.selectGcpProject.markdown": "{0} [자세히 알아보기](https://developers.google.com/gemini-code-assist/ui/onboarding/different-version)\n  \\n\\nStandard 또는 Enterprise를 계속 사용하려면 Google Cloud 프로젝트를 선택하세요.",
  "aiplugin.onboarding.validationRequired.markdown": "Gemini Code Assist를 사용 설정하려면 추가 작업이 필요합니다. 계속하려면 계정을 확인하고 다시 로그인해 주세요.",
  "action.aiplugin.chat.generateunittests.text": "단위 테스트 생성",
  "aiplugin.enablement.enable.gemini.api": "API 사용 설정",
  "aiplugin.enablement.enable.gemini.api.success": "API가 성공적으로 사용 설정되었습니다.", 
  "aiplugin.timeline.welcome.instructions.html": "<html><div>{0}의 Gemini Code Assist는 고품질 앱을 더 빠르게 빌드하는 데 도움이 되는 AI 코딩 도우미입니다. 사용해 볼 수 있는 프롬프트 예는 다음과 같습니다.</div></html>",
  "aiplugin.timeline.dynamic.instructions.html.wrapper": "<html><div> {0} </div></html>",
  "aiplugin.timeline.agentModePreviewBanner.learnMore": "[자세히 알아보기](https://developers.google.com/gemini-code-assist/docs/agent-mode)",
  "aiplugin.timeline.tipsCard.markdown": "* Gemini에 내 환경설정을 알려주는 규칙 추가\\n\n* 프롬프트 라이브러리에 자주 사용하는 프롬프트를 저장하고 `@`를 통해 액세스\\n\n* 편집기에서 코드를 선택하고 `{0}`을(를) 눌러 인라인으로 Gemini에 질문",
  "aiplugin.timeline.tipsCard.next.edit": "\\n\\ * 설정에서 '다음 수정 예측'을 사용 설정하면 파일 전체에서 코드 제안을 받을 수 있습니다.",
  "aiplugin.timeline.tipsCard.finishchanges": "\\n\\ * 코드를 초안하고 완료 작업 또는 `{0}`을(를) 사용하여 Gemini가 변경을 완료하도록 하세요.",
  "aiplugin.timeline.emptyState.sampleQuery1": "내 코드에 주석 추가",       
  "aiplugin.timeline.emptyState.sampleQuery2": "내 코드에 대한 단위 테스트 구현",
  "aiplugin.timeline.emptyState.sampleQuery3": "코드를 더 읽기 쉽게 만들기",      
  "aiplugin.timeline.emptyState.sampleQuery4": "Gemini Code Assist 사용 방법 알려줘"
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
