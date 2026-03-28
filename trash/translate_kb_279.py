import json

translations = {
  "tab.all.links.title": "모든 링크",
  "tab.all.links.tooltip": "매니페스트에서 앱 링크를 관리할 수 있습니다.",
  "tab.missing.urls.title": "누락된 URL",
  "tab.missing.urls.tooltip": "딥 링크되지 않은 웹 URL을 가져옵니다.",
  "overview.table.description": "이 도우미는 앱에서 앱 링크 및 사용자 지정 스킴 딥 링크를 진단하는 데 유용합니다. 앱 검사를 통해 매니페스트의 인텐트 필터 유효성을 확인합니다.",
  "overview.table.description.with.web.checks": "이 도우미는 앱에서 앱 링크 및 사용자 지정 스킴 딥 링크를 진단하는 데 유용합니다. 앱 검사를 통해 매니페스트의 인텐트 필터 유효성을 확인하고, 웹 검사를 통해 앱 링크 도메인의 디지털 애셋 링크 파일 유효성을 확인합니다.",
  "overview.ai.assistance.available.tooltip": "새로운 기능! AI가 앱 링크 로직을 작성하도록 도와줍니다. 시작하려면 \"앱 링크 만들기\"를 클릭하세요.",
  "ai.assistance.banner.text": "이제 AI가 2단계를 위한 코드 생성을 도와줄 수 있습니다.",
  "overview.search.emptyText": "링크 검색",
  "overview.create.applink": "앱 링크 만들기",
  "overview.create.waiting.project.sync": "앱 링크 만들기 기능은 프로젝트 동기화 이후에 사용할 수 있습니다.",
  "overview.test.applink": "앱 링크 테스트",
  "overview.refresh.tooltip": "유효성 검사 새로고침",
  "overview.search.action.name": "검색",
  "overview.fixall.manifest": "모든 매니페스트 문제 수정",
  "overview.column.select.description": "표시할 열 선택",
  "overview.loading": "앱 링크 로드 중...",
  "overview.update.links": "앱 링크 유효성 검사 업데이트 중",
  "overview.autofix.links": "매니페스트 문제 자동 수정",
  "overview.autofix.links.tooltip.running": "매니페스트 문제 자동 수정 진행 중",
  "overview.autofix.links.tooltip.waiting.project.sync": "매니페스트 문제 자동 수정은 프로젝트 동기화 이후에 사용할 수 있습니다.",
  "app.links.assistant.notification.group.name": "앱 링크 도우미",
  "overview.modal.fixed.all.content": "매니페스트의 모든 문제가 수정되었습니다.",
  "overview.modal.fix.failed": "일부 매니페스트 문제를 자동으로 수정하지 못했습니다. 이 문제들을 확인하세요.",
  "overview.modal.all.web.checks.failed": "모든 도메인에 대해 웹 검사를 실행하지 못했습니다. 인터넷 연결을 확인하고 다시 시도하세요.",
  "overview.modal.some.web.checks.failed": "하나 이상의 도메인에 대해 웹 검사를 실행하지 못했습니다. 디지털 애셋 링크 JSON 파일이 올바르게 호스팅되었는지 확인하세요. 문제가 발생한 도메인은 {0}, {1} 등입니다.",
  "overview.modal.one.web.check.failed": "{0}에 대해 웹 검사를 실행하지 못했습니다. 디지털 애셋 링크 JSON 파일이 올바르게 호스팅되었는지 확인하세요.",
  "overview.modal.project.not.synced": "웹 검사는 프로젝트 동기화 이후에만 실행할 수 있습니다. 웹 검사 결과를 얻으려면 프로젝트를 동기화한 후 다시 시도하세요.",
  "overview.webfix": "모든 웹 문제 수정",
  "overview.webfix.tooltip.waiting.project.sync": "웹 문제 자동 수정은 프로젝트 동기화 이후에 사용할 수 있습니다.",
  "overview.webfix.tooltip.not.consented": "웹 문제 자동 수정 기능은 Google의 도메인 유효성 검사 및 JSON 생성 API 사용 지침에 동의하지 않으면 사용할 수 없습니다.",
  "overview.webfix.tooltip.api.deprecated": "이 버전의 Android Studio는 더 이상 사용되지 않는 버전의 API를 호출합니다. 이 기능을 사용하려면 Android Studio를 최신 버전으로 업데이트하세요.",
  "overview.webfix.tooltip.no.domains": "이 프로젝트는 http(s) 스킴의 도메인을 사용하지 않습니다.",
  "overview.webfix.tooltip.no.issues": "모든 웹 문제가 수정되었습니다.",
  "overview.filter.all": "모든 링크",
  "overview.filter.app.errors": "앱 검사에 실패한 링크",
  "overview.filter.web.errors": "웹 검사에 실패한 링크",
  "overview.column.scheme": "스킴",
  "overview.column.host": "호스트",
  "overview.column.path": "경로",
  "overview.column.activity.name": "액티비티 이름",
  "overview.column.app.check.failures": "앱 검사 실패",
  "overview.column.web.check.failures": "웹 검사 실패",
  "overview.column.links.with.same.domain": "동일한 도메인을 가진 링크 수",
  "overview.table.all.columns.deselected": "선택된 열이 없습니다. 데이터를 보려면 하나 이상의 열을 선택하세요.",
  "overview.space.to.view.link.details": "링크 세부정보를 보려면 스페이스바를 누르세요.",
  "link.checks.never.run": "링크 검사가 아직 실행되지 않았습니다.",
  "link.checks.last.run": "링크 검사의 마지막 실행 시간은 {0}입니다.",
  "refresh.checks": "검사 새로고침",
  "data.information.overview": "설정 및 앱 성능을 올바르게 검증하기 위해 이 플러그인은 Google과 데이터를 공유합니다."
}

with open("missing_translations/missing_keys_korean.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for file_info in data.get("new_files", []):
    if file_info.get("filename") == "UrlAssistBundle.properties":
        keys_dict = file_info.get("keys", file_info.get("properties", {}))
        keys_dict.update(translations)
        file_info["keys"] = keys_dict
        break
else:
    data.setdefault("new_files", []).append({
        "filename": "UrlAssistBundle.properties",
        "keys": translations
    })

with open("missing_translations/missing_keys_korean.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)
