import json

translations = {
  "aiplugin.timeline.emptyState.sampleQuery4.answer": "Gemini Code Assist는 다음을 도와드릴 수 있습니다.\\n\\n* 프로젝트의 코드 및 테스트 생성\\n* 코드로 수행하려는 작업에 대한 지침 제공\\n* 로컬 코드베이스의 컨텍스트를 사용하여 채팅에서 정확한 응답 제공\\n* 코드 설명\\n* 코드 제안 및 완성 표시\\n* 버그 찾기 및 수정 제안\\n\\nIDE에서 Gemini를 사용하는 방법에 대한 자세한 내용은 다음을 참조하세요.\\n\\n* [Gemini의 지원을 받아 IntelliJ에서 코드 작성](https://developers.google.com/gemini-code-assist/ui/write-code)\\n* [Codelab 보기](https://codelabs.developers.google.com/codelabs/cloud-developer-duetai?hl=ko#0)",
  "aiplugin.timeline.emptyState.agentMode.sampleQuery1": "편집기의 경고 및 오류 수정",
  "aiplugin.timeline.emptyState.agentMode.sampleQuery2": "프로젝트에서 빌드 오류 찾기 및 해결",
  "aiplugin.timeline.emptyState.sampleQuery1.html": "<html>내 코드에 주석 추가</html>",
  "aiplugin.timeline.emptyState.sampleQuery2.html": "<html>내 코드에 대한 단위 테스트 구현</html>",
  "aiplugin.timeline.emptyState.sampleQuery3.html": "<html>코드를 더 읽기 쉽게 만들기</html>",
  "aiplugin.timeline.emptyState.sampleQuery4.html": "<html>Gemini Code Assist 사용 방법 알려줘</html>",
  "aiplugin.timeline.experimentalNotice.html": "<html><head><style>%%STYLE%%</style></head><body><div><center>Gemini Code Assist는 Google의 의견을 대변하지 않는 부정확한 정보를 표시할 수 있습니다.</center></div></body></html>",       
  "aiplugin.timeline.experimentalNotice.markdown": "Gemini는 실수를 할 수 있으므로 다시 한번 확인하시고 [코드 사용에 주의](https://cloud.google.com/gemini/docs/discover/works#how-when-gemini-cites-sources)하시기 바랍니다.",
  "aiplugin.timeline.changesDrawer.keepChange": "변경사항 수락",
  "aiplugin.timeline.changesDrawer.keepAll": "모두 수락",
  "aiplugin.timeline.changesDrawer.revertChange": "변경사항 거부",
  "aiplugin.timeline.changesDrawer.revertAll": "모두 거부",
  "aiplugin.timeline.changesDrawer.inEditor.keep": "수락",
  "aiplugin.timeline.changesDrawer.inEditor.keep.description": "이 파일의 모든 변경사항 수락",
  "aiplugin.timeline.changesDrawer.inEditor.revert": "거부",
  "aiplugin.timeline.changesDrawer.inEditor.revert.description": "이 파일의 모든 변경사항 거부",
  "aiplugin.notification.gcpProject.select.message": "Google Cloud 프로젝트를 선택하지 않았습니다. Gemini를 계속 사용하려면 프로젝트를 하나 선택하세요.",
  "aiplugin.notification.gcpProject.select.option": "Google Cloud 프로젝트 선택",
  "aiplugin.notification.login.message": "Gemini Code Assist에 로그인되어 있지 않습니다. Gemini를 계속 사용하려면 로그인해 주세요.",
  "aiplugin.notification.shortcut.information": "참고: JetBrains에서 변경한 기본 단축키를 수용하기 위해 Gemini를 사용한 코드 생성 단축키가 이제 {0}입니다.",
  "aiplugin.notification.access.restricted.notification.title": "{0}: 액세스 제한됨",
  "aiplugin.notification.access.restricted.notification.message.fallback": "구독 필요",
  "aiplugin.notification.upsell.freetier.content": "에이전트 모드 및 Gemini CLI를 통해 하루 1,500개의 요청을 수행하고, Google Cloud에서 Gemini에 액세스하고, $1,000의 Google Cloud 크레딧을 받으려면 업그레이드하세요.",
  "aiplugin.notification.upsell.freetier.action": "자세히 알아보기",
  "aiplugin.notification.upgrade.done.content": "업그레이드되었습니다. 이제 Gemini CLI 및 Gemini Code Assist 전반에서 일일 한도가 더 높아집니다.",
  "aiplugin.notification.upgrade.done.action": "구독 관리",
  "aiplugin.notification.downgrade.done.content": "현재 무료 버전인 개인용 Gemini Code Assist를 사용 중입니다.",
  "aiplugin.notification.downgrade.done.action": "업그레이드",
  "hats.notification.title": "Gemini Code Assist 설문조사",
  "hats.notification.message": "1분 정도 시간을 내어 의견을 남겨주시겠습니까?",
  "hats.notification.answer.yes": "예",
  "hats.notification.answer.no": "아니요(나중에)",
  "hats.notification.answer.dont.ask": "다시 묻지 않음",
  "hats.notification.action.menu.title": "설문조사 참여...",
  "hats.dialog.title": "Gemini Code Assist 만족도 설문조사",
  "hats.dialog.next.button.text": "다음",
  "hats.dialog.submit.button.text": "제출",
  "hats.dialog.close.button.text": "닫기",
  "hats.dialog.question.csat": "<html>전반적으로 Gemini Code Assist에 어느 정도 만족하시나요?",
  "hats.dialog.question.nps": "<html>Gemini Code Assist를 친구나 동료에게<br>추천할 의향이 얼마나 있으신가요?",
  "hats.dialog.question.improve": "<html>Gemini Code Assist 개선을 위한 아이디어가<br>있다면 알려주실 수 있나요?",
  "hats.dialog.question.does.well": "<html>Gemini Code Assist에서 가장 훌륭하다고<br>생각하는 점은 무엇인가요?",
  "hats.dialog.thank.you.title": "설문조사에 참여해 주셔서 감사합니다.",
  "hats.dialog.thank.you.message": "설문조사에 소중한 시간을 할애해 주셔서 진심으로 감사합니다.",
  "hats.dialog.question.1": "1. Gemini Code Assist를 친구나 동료에게 추천할 의향이 얼마나 있으신가요?",
  "hats.dialog.question.2": "2. 전반적으로 Gemini Code Assist에 어느 정도 만족하시나요?",
  "hats.dialog.question.3": "3. Gemini Code Assist 개선을 위한 아이디어가 있다면 알려주실 수 있나요?",
  "hats.dialog.question.4": "4. Gemini Code Assist에서 가장 훌륭하다고 생각하는 점은 무엇인가요?",
  "hats.dialog.question.5": "5. 추가 질문이 있는 경우 비정기적으로 연락을 드려도 괜찮습니까?"
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
