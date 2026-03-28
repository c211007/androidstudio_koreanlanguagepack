import json

translations = {
  "data.information.dialog.title": "앱 링크 도우미 데이터 공유",
  "data.information.dialog.content": "앱 링크 도우미는 다음 데이터를 Google과 공유합니다:\\n\\u2022 Gradle 파일의 패키지 이름\\n\\u2022 AndroidManifest.xml 파일의 인텐트 필터에 포함된 호스트, 스킴 및 경로 속성",
  "app.links.assistant.settings.displayname": "앱 링크 도우미",
  "dal.api.consent.settings.checkbox.label": "이 프로젝트({0})에 대해 패키지 이름 및 관련 도메인을 Google과 공유하는 데 동의합니다.",
  "dal.api.not.consented.warning": "웹 검사를 사용할 수 없습니다.",
  "dal.api.deprecation.warning": "웹 검사를 사용하려면 Android Studio를 최신 버전으로 업데이트하세요.",
  "dal.api.open.consent.settings": "설정...",
  "dal.api.consent.description": "앱 링크 구성을 완전히 검증하기 위해 이 플러그인은 Google Play의 앱 서명 인증서 SHA256 지문과 도메인 소유권을 확인하기 위해 웹사이트에 게시된 디지털 애셋 링크 JSON 파일에 액세스하는 Google API를 사용합니다(<a href=\"https://developer.android.com/training/app-links/verify-android-applinks#web-assoc\">자세히 알아보기</a>). 도우미의 웹 검사 결과 및 수정 사항은 이 기능을 선택한 후 사용할 수 있습니다.",
  "back.to.list": "링크로 돌아가기",
  "app.link.details.header": "앱 링크 세부정보",
  "app.link.more.details": "추가 세부정보...",
  "app.link.hide.details": "세부정보 숨기기",
  "app.link.details.always.visible": "호스트: {0}\\n경로: {1}",
  "app.link.extra.details": "경로 유형: {0}\\n액티비티: {1}\\n순서: {2}\\n우선순위: {3}",
  "link.passed.all.checks": "이 링크는 모든 검사를 통과했습니다.",
  "link.failed.one.check": "이 링크는 하나의 검사를 통과하지 못했습니다.",
  "link.failed.number.checks": "이 링크는 {0}개의 검사를 통과하지 못했습니다.",
  "this.link.last.checked.time": "이 링크가 마지막으로 검사된 시간은 {0}입니다.",
  "fix.app.checks": "앱 검사 실패 수정",
  "no.app.checks.to.fix": "수정할 앱 검사 실패가 없습니다.",
  "fix.web.checks": "웹 검사 문제 수정",
  "tooltip.json.generation.not.helpful": "새 JSON을 생성하여 해결할 수 있는 웹 검사 문제가 없습니다.",
  "app.checks.header": "앱에 대한 검사",
  "app.checks.description": "이 검사는 매니페스트의 앱 링크가 올바르게 구성되어 있는지 확인합니다.",
  "web.checks.header": "도메인에 대한 검사",
  "web.checks.description": "이 검사는 도메인의 디지털 애셋 링크 파일이 올바르게 구성되어 있는지 확인합니다.",
  "accordion.button.expand.accessible.label": "콘텐츠 패널 확장",
  "accordion.button.collapse.accessible.label": "콘텐츠 패널 축소",
  "accordion.header.data.tags": "<data> 태그",
  "accordion.header.order": "Order 속성",
  "accordion.header.priority": "Priority 속성",
  "accordion.header.non.redirect": "서드파티 리디렉션 링크",
  "accordion.header.web.check.existence": "디지털 애셋 링크 JSON 파일 존재 여부",
  "accordion.header.web.check.app.identifier": "앱의 패키지 이름(또는 앱 ID) 포함 여부",
  "accordion.header.web.check.fingerprint": "앱의 지문 포함 여부",
  "accordion.header.web.check.content.type": "콘텐츠 유형이 application/json인지 여부",
  "accordion.header.web.check.https.accessibility": "HTTPS를 사용하여 액세스 가능 여부",
  "accordion.header.web.check.non.redirect": "리디렉션 없이 액세스 가능 여부",
  "accordion.header.web.check.host.formed.properly": "호스트 구성의 적절성",
  "accordion.header.web.check.other.checks": "기타 검사",
  "accordion.content.data.scheme.failed": "이 링크의 인텐트 필터에는 android:scheme 속성을 포함하는 <data> 태그가 없습니다.",
  "accordion.content.data.host.failed": "이 링크의 인텐트 필터는 호스트를 지정하지 않고 <data> 태그에서 경로를 지정하거나, 호스트를 지정하지 않고 <data> 태그에서 http 또는 https 스킴을 사용합니다.",
  "accordion.content.data.scheme.webschemehashost.failed": "이 링크는 http 또는 https 스킴을 사용하지만 호스트를 지정하지 않습니다.",
  "accordion.content.data.path.hashost.failed": "이 링크는 경로를 정의하지만 호스트를 지정하지 않습니다.",
  "accordion.content.data.path.failed": "이 링크의 인텐트 필터는 <data> 태그에 경로(path)를 지정하지만 \"/\"로 시작하지 않습니다.",
  "accordion.content.data.path.prefix.failed": "이 링크의 인텐트 필터는 <data> 태그에 pathPrefix를 지정하지만 \"/\"로 시작하지 않습니다.",
  "accordion.content.data.path.pattern.failed": "이 링크의 인텐트 필터는 <data> 태그에 pathPattern을 지정하지만 \".*\" 또는 \"/\"로 시작하지 않습니다.",
  "accordion.content.data.port.failed": "이 링크의 포트가 0에서 65535(포함) 사이의 정수가 아닙니다.",
  "accordion.content.action.view.failed": "이 링크의 인텐트 필터는 ACTION_VIEW 인텐트 작업을 지정하지 않아, Google 검색에서 인텐트 필터에 도달할 수 없습니다.",
  "accordion.content.default.category.failed": "이 링크의 인텐트 필터에는 DEFAULT 카테고리가 포함되어 있지 않아, 앱이 암시적 인텐트에 응답할 수 없습니다."
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
