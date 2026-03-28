import json

translations = {
  "action.com.android.studio.ml.aida.SignInAction.text": "AIDA 로그인",     
  "action.com.android.studio.ml.aida.SignOutAction.text": "AIDA 로그아웃", 
  "aiplugin.product.name": "Gemini Code Assist",
  "aiplugin.completion.status.bar.prefix": "Gemini Code Assist",
  "test.mode.metrics.environment.notification.title": "CLOUD CODE: 측정항목 테스트 모드",
  "test.mode.metrics.environment.notification.contents": "모든 측정항목이 테스트 환경으로 전송됩니다.",
  "aiplugin.analytics.action.SelectMetricsEnvironmentAction.text": "측정항목 환경 설정(현재: {0})",
  "aiplugin.analytics.action.SelectMetricsEnvironmentAction.title": "측정항목 환경 설정",
  "aiplugin.feedback.privacynotice.label": "이 신고서를 제출하면 개인정보처리방침 이용약관에 동의하는 것으로 간주됩니다.",
  "aiplugin.feedback.privacynotice.expandedlabel": "이 신고서를 제출하면 개인정보처리방침 이용약관에 동의하는 것으로 간주됩니다.",
  "aiplugin.feedback.privacypolicy": "<html>법적인 사유로 콘텐츠 변경을 요청하려면 <a href='https://support.google.com/legal/answer/3110420'>법률 도움말\n  페이지</a>로 이동하세요. 일부 <a href='https://myaccount.google.com/#info'>계정\n  및 시스템 정보</a>가 Google로 전송될 수 있습니다. 사용자가 제공하는 정보는 기술 문제를 해결하고 서비스를 개선하는 데 도움이 되도록 사용되며\n  Google <a href='https://myaccount.google.com/privacypolicy'>개인정보처리방침</a> 및\n  <a href='https://www.google.com/intl/ko/policies/terms/'>서비스 약관</a>이 적용됩니다.</html>",
  "aiplugin.feedback.allowfeedback.checkbox.text": "다음 이름으로 의견 보내기",
  "aiplugin.feedback.userconsent.checkbox.text": "자세한 정보나 업데이트를 이메일로 보내도 됩니다.",
  "aiplugin.feedback.email.validation.message": "이메일 주소를 지정해 주세요.",    
  "aiplugin.feedback.description.validation.message": "의견 또는 재현 단계를 제공해 주세요.",
  "aiplugin.feedback.message": "의견 제출",
  "aiplugin.feedback.error.message": "Google에 신고",
  "aiplugin.feedback.loading": "첨부파일을 가져오는 중...",
  "aiplugin.feedback.unknownsubmissionerror": "보고서 제출 중 알 수 없는 오류가 발생했습니다.\n  다시 시도해 주세요.",
  "aiplugin.feedback.submit.notification.title": "의견이 제출됨",
  "aiplugin.feedback.submit.notification.description": "의견을 보내주셔서 감사합니다!",
  "aiplugin.feedback.dialog.title": "Google에 의견 제출",
  "aiplugin.feedback.dialog.description.placeholder": "버그를 설명하는 자유 형식 의견 / 재현 단계를 추가하세요.",
  "aiplugin.feedback.dialog.description.prefix.diff.error": "[MissingFileChange] :",
  "aiplugin.feedback.dialog.description.prefix": "Gemini -",
  "aiplugin.feedback.block.title": "의견 사용 중지됨",
  "aiplugin.feedback.block.message": "관리자가 의견 양식을 사용 중지했습니다.",
  "aiplugin.feedback.block.tooltip.message": "관리자가 파트너의 의견 제출을 사용 중지했습니다.",
  "ai.plugin.settings.usage.tracking": "사용 통계",
  "ai.plugin.settings.usage.tracking.blocked": "관리자가 이 기능을 사용 중지했습니다.",
  "ai.plugin.settings.sharing.usage.data": "사용 통계 사용 설정",
  "ai.plugin.settings.google.privacy.policy": "Google에서 자사 제품 및 서비스를 개선할 수 있도록 사용 통계 및 비정상 종료 보고서를 보내는 것에 동의합니다.<br><br>사용 통계에는 <a href=\"http://www.google.com/policies/privacy\"/>Google 개인정보처리방침</a>이 적용됩니다.<br><br><b>이 설정은 AI 모델을 학습시키는 데 프롬프트, 컨텍스트 코드, 응답을 사용한다는 의미가 아닙니다.</b><br><br> Gemini Code Assist Standard 및 Enterprise 버전은 머신러닝 모델을 학습시키기 위해 프롬프트, 컨텍스트 코드 또는 응답을 <b>절대</b> 사용하지 않습니다.",
  "ai.plugin.settings.google.privacy.policy.userTier": "<br><br>{0}을(를) 사용하는 경우 <a href=\"{1}\"/>{0} 개인정보 보호 설정</a>에서 Google이 AI 모델 학습을 위해 프롬프트, 컨텍스트 코드 및 응답을 사용하는 것을 선택 해제할 수 있습니다.",
  "ai.plugin.settings.cloud.project": "Google Cloud 프로젝트",
  "ai.plugin.settings.gcp.project.to.use": "Gemini Code Assist Standard 또는 Enterprise에 사용할 Google Cloud 프로젝트를 입력하세요.",
  "ai.plugin.settings.advanced": "고급 설정",
  "ai.plugin.settings.api.endpoint.override.invalid.url": "{0}에 연결하지 못했습니다. URL을 확인하고 다시 시도해 주세요.",
  "ai.plugin.settings.api.endpoint.override": "API 엔드포인트 재정의",
  "ai.plugin.settings.api.endpoint.override.comment": "기본값: {0}",        
  "ai.plugin.settings.api.endpoint.override.optional.comment": "선택사항, 기본값: {0}",
  "ai.plugin.settings.oauth2.api.override.label": "OAuth 2.0 엔드포인트:",        
  "ai.plugin.settings.resourcemanager.api.override.label": "Cloud Resource Manager 엔드포인트:",
  "ai.plugin.settings.openidconnect.api.override.label": "OpenID 연결 엔드포인트:",
  "ai.plugin.settings.cloudcodepa.api.override.label": "Cloud Code API 엔드포인트:",
  "ai.plugin.settings.recitation.warning": "코드 사용에 주의하세요. 추천된 코드에는 라이선스가 적용될 수 있습니다.",
  "ai.plugin.settings.recitation": "인용 로그 파일 재정의 경로",
  "ai.plugin.settings.recitation.description": "인용 로그 파일이 있는 디렉터리 위치의 경로를 재정의합니다. 비워 두면 기본적으로 캐시 폴더로 설정됩니다.<br>인용 로그 기본 위치: <a href=\"{0}\">{1}</a>",
  "ai.plugin.settings.recitation.browse.title": "인용 로그 파일 경로로 이동",
  "ai.plugin.settings.recitation.notification.title": "인용 로깅",       
  "ai.plugin.settings.recitation.notification.fail.create.log.message": "인용 로그 파일 {0}을(를) 만들지 못했습니다.<br>이유: {1}"
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
