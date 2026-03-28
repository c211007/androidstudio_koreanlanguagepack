import json

translations = {
  "insert.code.dialog.ai.sample.url.input.label": "처리할 샘플 URL",
  "insert.code.dialog.ai.sample.url.input.placeholder": "예: https://www.example.com/sample/path?param=123",
  "insert.code.dialog.starter.radio": "시작 코드 삽입",
  "insert.code.dialog.starter.description": "앱 링크 처리를 위한 시작 코드를 액티비티에 삽입하여 수동으로 코드를 추가할 수 있도록 합니다.",
  "insert.code.dialog.starter.description.link": "자세히 알아보기",
  "test.url.launch.url.panel.title": "앱 링크 테스트",
  "test.url.launch.url.null.module.error.message": "먼저 URL 매핑을 설정하세요.",
  "test.url.launch.url.empty.url.error.message": "유효한 URL이 제공되지 않았습니다.",
  "test.url.launch.url.description.text": "아래에 URL을 입력하고 '테스트 실행'을 클릭하여 앱이 설치된 기기에서 사용자가 URL을 클릭하는 상황을 시뮬레이션하세요. 쉽게 다시 테스트할 수 있도록 이 URL로 실행 구성을 자동으로 추가합니다.",
  "test.url.launch.url.field.hint": "URL을 입력하세요. 예: http://www.yourwebsite.com/app",
  "test.url.check.url.mapping.result": "이 URL은 {0}(으)로 매핑됩니다.",
  "test.url.malformed.url.error": "URL 형식이 잘못되었습니다. 다시 확인하세요.",
  "test.url.resolve.error": "URL 확인 충돌이 발생했습니다. 디지털 애셋 링크를 연결하고 확인하세요.",
  "test.url.resolve.success": "앱이 {0}에 올바르게 연결되었습니다.",
  "test.url.logcat.task.description": "기기에서 앱 링크 실행 확인 중",
  "test.url.no.app.module.found": "앱 모듈을 찾을 수 없습니다. 먼저 앱 모듈을 만드세요.",
  "test.url.activity": "액티비티",
  "test.url.activity.determine.automatically": "자동으로 결정",
  "test.url.activity.manually.selected": "수동으로 지정한 액티비티({0}) 실행 중",
  "play.dynamic.filters.inspection.id": "Play 동적 필터",
  "play.dynamic.filters.inspection.text": "<html><body>앱이 Google Play 스토어에서 설치된 경우, 앱이 Play 동적 필터를 사용하도록 선택했기 때문에 이 인텐트 필터는 무시됩니다. <br/><br/><a href=\"{0}\">Play 콘솔을 방문하여 이 액티비티로 전송될 URL을 확인하세요</a>.</body></html>",
  "play.dynamic.filters.info.text": "이 앱의 앱 링크는 Google Play Console에서 관리합니다. <a href=\"{0}\">자세히 알아보기</a>",
  "play.dynamic.filters.dismiss.banner": "이 배너 영구적으로 닫기",
  "intention.action.family.name": "앱 링크 도우미",
  "intention.action.call.to.action": "앱 링크 도우미 시작",
  "gemini.advertiser.description": "Gemini에 로그인하여 딥 링크 처리 코드를 생성하고, 제안된 변경 사항을 차이점 뷰에서 검토하여 프로젝트에 직접 적용하세요.",
  "missing.url.overview.column.status": "상태",
  "missing.url.overview.column.url": "URL",
  "missing.url.status.misconfigured": "잘못 구성됨",
  "missing.url.status.app.linked": "매핑됨",
  "missing.url.status.not.mapped": "매핑되지 않음",
  "missing.url.overview.loading": "누락된 URL 가져오는 중...",
  "url.assistant.agent.tool.urlSummarizer.running": "URL에서 콘텐츠 요약 중: {0}…",
  "url.assistant.agent.tool.urlSummarizer.completed": "URL에서 요약된 콘텐츠: {0}",
  "url.assistant.agent.tool.launchAppViaUrl.running": "연결된 에뮬레이터 또는 기기에서 URL({2})을 통해 {0}/{1} 실행 중…",
  "url.assistant.agent.tool.launchAppViaUrl.completed": "연결된 에뮬레이터 또는 기기에서 URL({2})을 통해 {0}/{1}을(를) 실행했습니다."
}

with open("missing_translations/missing_keys_korean.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for file_info in data.get("new_files", []):
    if file_info.get("filename") == "UrlAssistBundle.properties":
        keys_dict = file_info.get("keys", file_info.get("properties", {}))
        keys_dict.update(translations)
        file_info["keys"] = keys_dict
        break

with open("missing_translations/missing_keys_korean.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)
