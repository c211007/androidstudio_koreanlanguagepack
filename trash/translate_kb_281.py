import json

translations = {
  "accordion.content.browsable.category.failed": "이 링크의 인텐트 필터에는 BROWSABLE 카테고리가 포함되어 있지 않아, 웹 브라우저에서 인텐트 필터에 액세스할 수 없습니다.",
  "accordion.content.auto.verify.failed": "이 링크의 호스트 구성 요소에는 autoVerify 속성이 \"true\"로 설정되고 http(s) 스킴만 있는 해당 인텐트 필터가 없어, 사용자 메시지 없이 앱에서 자동으로 확인하고 열 수 없습니다. 참고로 Android는 http(s) 스킴을 사용하고 사용자 지정 스킴이 없는 인텐트 필터에서 사용된 도메인에 대해서만 도메인 확인을 요청합니다. 올바른 동작을 위해 인텐트 필터를 여러 개로 분할해야 할 수도 있습니다.",
  "accordion.content.order.failed": "이 링크의 순서(order)가 정수가 아닙니다.",
  "accordion.content.priority.failed": "이 링크의 우선순위(priority)가 정수가 아닙니다.",
  "accordion.content.redirect.failed": "이 링크는 리디렉션을 사용하며, 이는 Google Ads에서 지원되지 않습니다.",
  "accordion.content.data.scheme.passed": "이 링크의 인텐트 필터에는 android:scheme 속성이 포함된 <data> 태그가 있습니다.",
  "accordion.content.data.host.passed": "이 링크의 인텐트 필터는 경로가 비어 있지 않을 때 호스트를 포함하고 스킴이 http 또는 https일 때 호스트를 포함하는 <data> 태그가 있습니다.",
  "accordion.content.data.scheme.webschemehashost.passed": "이 링크는 http 또는 https 스킴을 사용하며 필요한 호스트를 정의합니다.",
  "accordion.content.data.path.hashost.passed": "이 링크는 경로 및 필수 호스트를 정의합니다.",
  "accordion.content.data.path.passed": "이 링크의 <data> 태그 내의 경로는 \"/\"로 시작합니다.",
  "accordion.content.data.path.prefix.passed": "이 링크의 <data> 태그 내의 pathPrefix는 \"/\"로 시작합니다.",
  "accordion.content.data.path.pattern.passed": "이 링크의 <data> 태그 내의 pathPattern은 \"/\" 또는 \".*\"로 시작합니다.",
  "accordion.content.data.port.passed": "이 링크의 포트는 0에서 65535(포함) 사이의 정수입니다.",
  "accordion.content.action.view.passed": "이 링크의 인텐트 필터는 ACTION_VIEW 인텐트 작업을 지정하여, Google 검색에서 인텐트 필터에 도달할 수 있도록 합니다.",
  "accordion.content.default.category.passed": "이 링크의 인텐트 필터에는 DEFAULT 카테고리가 포함되어 있어, 앱이 암시적 인텐트에 응답할 수 있습니다.",
  "accordion.content.browsable.category.passed": "이 링크의 인텐트 필터에는 BROWSABLE 카테고리가 포함되어 있어, 웹 브라우저에서 인텐트 필터에 액세스할 수 있습니다.",
  "accordion.content.auto.verify.passed": "이 링크의 호스트 구성 요소에는 autoVerify 속성이 \"true\"로 설정되고 http(s) 스킴만 있는 해당 인텐트 필터가 있어, 링크를 확인하고 사용자 프롬프트 없이 앱에서 자동으로 열 수 있습니다.",
  "accordion.content.order.passed": "이 링크의 순서(order)가 정수입니다.",
  "accordion.content.priority.passed": "이 링크의 우선순위(priority)가 정수입니다.",
  "accordion.content.redirect.passed": "이 링크는 리디렉션을 사용하지 않으므로 Google Ads에서 지원됩니다.",
  "web.check.existence.failed": "도메인의 ./well-known/assetlinks.json에서 파일을 찾을 수 없습니다.",
  "web.check.app.identifier.failed": "DAL 파일의 package_name 필드에 패키지 이름이 포함되어 있지 않습니다.",
  "web.check.fingerprint.failed": "DAL 파일의 sha256_cert_fingerprints 필드에 매칭되는 앱의 지문(Google Play에 게시된 앱 기준)이 포함되어 있지 않습니다.",
  "web.check.content.type.failed": "DAL 파일이 application/json 콘텐츠 유형으로 제공되지 않았습니다.",
  "web.check.https.accessibility.failed": "DAL 파일에 HTTPS를 통해 액세스할 수 없습니다.",
  "web.check.non.redirect.failed": "DAL 파일이 리디렉션과 함께 제공되었습니다.",
  "web.check.host.formed.properly.failed": "호스트 형식이 잘못되었습니다.",
  "web.check.play.signing.key.failed": "앱에 Google Play 서명 키가 없습니다.",
  "web.check.json.failed.fetch": "assetlinks.json 파일을 가져올 수 없습니다.",
  "web.check.json.invalid": "assetlinks.json 파일은 유효한 디지털 애셋 링크 파일이 아닙니다.",
  "web.check.json.invalid.schema": "assetlinks.json 파일은 유효한 JSON 배열이 아니거나 유효한 디지털 애셋 링크 파일이 아닙니다.",
  "web.check.json.invalid.syntax": "assetlinks.json 파일을 JSON으로 파싱할 수 없습니다.",
  "web.check.json.empty": "assetlinks.json 파일이 비어 있습니다.",
  "web.check.existence.passed": "도메인의 ./well-known/assetlinks.json에서 파일을 찾았습니다.",
  "web.check.app.identifier.passed": "DAL 파일의 package_name 필드에 패키지 이름이 포함되어 있습니다.",
  "web.check.fingerprint.passed": "DAL 파일의 sha256_cert_fingerprints 필드에 매칭되는 앱의 지문(Google Play에 게시된 앱 기준)이 포함되어 있습니다.",
  "web.check.content.type.passed": "DAL 파일이 application/json 콘텐츠 유형으로 제공되었습니다.",
  "web.check.https.accessibility.passed": "DAL 파일에 HTTPS를 통해 액세스할 수 있습니다.",
  "web.check.non.redirect.passed": "DAL 파일이 리디렉션 없이 제공되었습니다.",
  "web.check.host.formed.properly.passed": "호스트 형식이 올바릅니다.",
  "web.check.fingerprint.ignored": "해당 없음. 지문 자동 확인은 Google Play에 게시된 앱에서만 사용할 수 있습니다.",
  "app.link.does.not.exist": "Android 매니페스트의 변경 사항으로 인해, 이 링크는 더 이상 존재하지 않습니다.",
  "app.link.updating.details": "앱 링크 세부정보 업데이트 중",
  "web.check.results.not.run": "웹 검사를 실행할 수 없습니다.",
  "web.check.results.not.run.desc": "웹 검사를 실행할 수 없습니다. 인터넷 연결을 확인하고 다시 시도하세요.",
  "reference.link.text": "자세히 알아보기",
  "manual.fix.explanation": "아래 링크는 자동으로 수정할 수 없습니다. 문제를 해결하는 방법에 대한 자세한 내용과 안내를 보려면 링크를 클릭하세요.",
  "manual.fix.scheme": "앱 링크의 인텐트 필터에는 scheme 속성이 있는 <data> 태그가 있어야 합니다.",
  "manual.fix.webscheme.nohost": "앱 링크의 인텐트 필터는 http 또는 https 스킴을 사용할 경우 호스트를 지정해야 합니다.",
  "manual.fix.host": "앱 링크의 인텐트 필터는 경로를 지정하거나 http 또는 https 스킴을 사용할 경우 호스트를 지정해야 합니다."
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
