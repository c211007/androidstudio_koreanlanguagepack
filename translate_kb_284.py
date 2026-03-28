import json

translations = {
  "dal.package.id.hint": "예: com.example.app",
  "dal.sign.in.url.hint": "예: https://signin.example.com",
  "dal.verify.success": "성공! 앱이 선택한 도메인과 연결되었습니다.",
  "dal.verify.failure": "웹사이트 연결 유효성 검사에 실패했습니다.",
  "dal.verify.error.invalid.query": "서버 오류가 발생했습니다. 나중에 다시 시도하세요.",
  "dal.verify.error.fetch.error": "<a href={0}>{0}</a>에서 디지털 애셋 링크 파일을 찾을 수 없습니다.",
  "dal.verify.error.failed.ssl.validation": "디지털 애셋 링크 파일을 호스팅하는 웹사이트는 유효한 인증서와 함께 HTTPS를 지원해야 합니다. <a href={0}>{0}</a>에서 DAL 파일에 액세스할 수 있는지 확인하세요.",
  "dal.verify.error.secure.include.insecure": "디지털 애셋 링크 파일에 안전하지 않은 애셋이 포함되어 있습니다. 모두 유효한 인증서와 함께 HTTPS를 지원하는지 확인하세요.",
  "dal.verify.error.too.large": "디지털 애셋 링크 파일이 너무 큽니다. 파일 크기가 100KB를 초과하지 않는지 확인하세요.",
  "dal.verify.error.wrong.content.type": "올바르지 않은 Content-Type으로 디지털 애셋 링크 파일을 호스팅하고 있는 것 같습니다. Content-Type이 application/json인지 확인하세요.",
  "dal.verify.error.network.error": "네트워크 오류. 네트워크 연결을 확인하세요.",
  "dal.verify.error.malformed.content": "JSON 파일의 형식이 잘못되어 앱을 선택한 <a href={0}>도메인</a>과 연결할 수 없습니다. 디지털 애셋 링크 파일이 올바른 <a href={0}>도메인</a>에 업로드되었는지 확인하세요.",
  "dal.verify.error.malformed.http.response": "HTTP 응답의 형식이 잘못되어 앱을 선택한 <a href={0}>도메인</a>과 연결할 수 없습니다. 디지털 애셋 링크 파일이 올바른 <a href={0}>도메인</a>에 업로드되었는지 확인하세요.",
  "dal.verify.error.not.associated": "앱을 선택한 <a href={0}>도메인</a>과 연결할 수 없습니다. 디지털 애셋 링크 파일이 올바른 <a href={0}>도메인</a>에 업로드되었는지 확인하세요.",
  "download.json": "JSON 파일 다운로드",
  "download.success": "{0} 파일이 {1}에 저장되었습니다.",
  "fix.all.web.issues.tab.header": "모든 웹 문제 수정",
  "fix.all.web.issues.description": "업데이트가 필요한 도메인이 여러 개 있습니다. 모든 도메인에 대해 일괄 해결 및 .zip으로 다운로드하거나, 개별적으로 해결 및 다운로드하거나, 다운로드하기 전에 파일을 수동으로 비교할 수 있습니다. 압축을 푼 후 각 파일을 올바른 도메인에 업로드해야 합니다. 그런 다음 검사를 새로고침하여 모든 것이 작동하는지 확인할 수 있습니다. <a href=\"https://developer.android.com/training/app-links/verify-android-applinks#web-assoc\">자세히 알아보기</a>",
  "fix.all.web.issues.successful.blank.description": "모든 도메인이 성공적으로 연결되었습니다.",
  "fix.all.web.issues.rpc.failed": "모든 도메인에 대해 디지털 애셋 링크 파일을 생성할 수 없습니다. 인터넷 연결을 확인하고 다시 시도하세요.",
  "fix.all.web.issues.no.links.description": "프로젝트에 앱 링크가 없습니다.",
  "fix.all.web.issues.no.autofix.domains.description": "업데이트가 필요한 도메인이 여러 개 있습니다. 실패한 검사 항목을 살펴보고 수정하세요. 그런 다음 검사를 새로고침하여 모든 것이 작동하는지 확인할 수 있습니다. <a href=\"https://developer.android.com/training/app-links/verify-android-applinks#web-assoc\">자세히 알아보기</a>",
  "fix.all.web.issues.newer.json.section.header": "최신 assetlinks.json을 사용할 수 있는 도메인",
  "fix.all.web.issues.download.all": "모두 .zip으로 다운로드",
  "fix.all.web.issues.view.diff": "JSON 파일 차이점 보기",
  "fix.all.web.issues.manual.fix.section.header": "수동 수정이 필요한 도메인",
  "single.domain.json.generation.title": "디지털 애셋 링크 JSON",
  "single.domain.json.fix.tab.header": "{0}의 웹 검사 문제 수정",
  "single.domain.json.fix.description": "assetlinks.json 파일의 권장 변경 사항을 검토한 후 다운로드하세요. 다운로드한 파일을 https://{0}/.well-known/assetlinks.json에 저장한 후, 검사를 새로고침하여 제대로 작동하는지 확인하세요. <a href=\"https://developer.android.com/training/app-links/verify-android-applinks#web-assoc\">자세히 알아보기<a/>",
  "json.generation.overwrite.warning": "기존의 유효한 DAL 파일이 없기 때문에 밑바닥부터 새로 생성했습니다. 자동 생성된 이 파일이 기존 assetlinks.json을 덮어쓰지 않는지 확인하세요.",
  "new.domain.json.generation.tab.header": "디지털 애셋 링크 JSON 생성",
  "new.domain.json.generation.description": "도메인용 새 assetlinks.json 파일을 생성한 다음 다운로드하세요. 다운로드한 후 파일을 .well-known/assetlinks.json에 저장하고 검사를 새로고침하여 모든 것이 작동하는지 확인히세요. <a href=\"https://developer.android.com/training/app-links/verify-android-applinks#web-assoc\">자세히 알아보기<a/>",
  "new.domain.json.generation.domain.textfield.label": "도메인",
  "new.domain.json.generation.domain.textfield.instructions": "http(s)가 없는 도메인, 예: example.com",
  "new.domain.json.generation.package.name.textfield.label": "패키지 이름",
  "new.domain.json.generation.domain.cannot.be.empty": "도메인은 비워둘 수 없습니다.",
  "new.domain.json.generation.domain.cannot.contain.slashes": "http(s)나 슬래시를 제외한 도메인만 입력하세요.",
  "new.domain.json.generation.domain.not.valid": "도메인 이름이 유효하지 않습니다.",
  "new.domain.json.generation.package.name.cannot.be.empty": "패키지 이름은 비워둘 수 없습니다.",
  "new.domain.json.generation.package.name.not.valid": "유효한 패키지 이름을 입력하세요.",
  "new.domain.json.generation.create": "JSON 생성",
  "insert.code.dialog.title": "액티비티 선택",
  "insert.code.dialog.ok": "코드 삽입",
  "insert.code.dialog.cancel": "취소",
  "insert.code.dialog.conflict.error": "앱 링크 인텐트 처리 코드가 이 액티비티에 이미 존재하므로 중복된 코드를 추가할 수 없습니다.",
  "insert.code.dialog.no.oncreate.error": "액티비티 클래스에 onCreate 메서드가 정의되어 있지 않아 코드를 삽입할 수 없습니다.",
  "insert.code.dialog.language.not.supported": "액티비티에 앱 링크 처리 코드 삽입은 Kotlin 및 Java에서만 지원됩니다.",
  "insert.code.dialog.app.link.missing.error": "유효한 앱 링크가 있는 액티비티를 찾을 수 없습니다. 먼저 앱 링크를 생성하세요.",
  "insert.code.dialog.ai.radio": "AI 지원을 사용하여 코드 생성(권장)",
  "insert.code.dialog.ai.description": "액티비티에서 처리해야 할 매개변수를 포함하여 딥 링크하려는 샘플 URL을 입력하세요."
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
