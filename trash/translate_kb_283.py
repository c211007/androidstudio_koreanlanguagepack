import json

translations = {
  "dal.panel.instruction": "웹사이트를 앱과 연결하려면 아래 정보를 입력하여 디지털 애셋 링크 파일을 생성하고 웹사이트에 업로드하세요.",
  "dal.select.module": "작업할 모듈 선택",
  "dal.site.domain.textfield.label": "사이트 도메인:",
  "dal.application.id.textfield.label": "애플리케이션 ID:",
  "dal.sha.title": "서명 인증서의 SHA256 지문 (선택 사항)",
  "dal.sha.description": "디지털 애셋 링크 생성기는 항상 Google Play의 지문을 우선 사용하려고 시도합니다. 앱이 출시되었거나 Play 앱 서명에 등록된 경우 Google Play 지문을 사용할 수 있습니다.",
  "dal.add.fingerprint": "새 지문 추가",
  "dal.android.studio.signing.key.config": "Android Studio 서명 키 구성",
  "dal.local.keystore": "로컬 키스토어 파일",
  "dal.enter.manually": "지문 직접 입력",
  "dal.generate.file": "디지털 애셋 링크 파일 생성",
  "dal.current.manifest": "현재 매니페스트",
  "dal.fixed.manifest": "수정된 매니페스트",
  "dal.complete.association.title": "연결 완료",
  "dal.complete.association.description": "디지털 애셋 링크 파일을 앱에 연결하고 파일이 올바른 위치에 업로드되었는지 확인하세요.",
  "dal.add.statements.success": "<a href=\"\">strings.xml</a>에 애셋 선언(asset statement)을 추가했습니다.",
  "dal.add.statements.fail": "애셋 선언을 추가하지 못했습니다.",
  "dal.linked.strings.success": "<a href=\"1\">AndroidManifest.xml</a>에 문자열을 연결했습니다.",
  "dal.linked.strings.success.multiple": "다음 파일에 문자열을 연결했습니다.",
  "dal.linked.strings.fail": "AndroidManifest 파일에 문자열을 연결하지 못했습니다.",
  "dal.add.autoverify.success": "인텐트 필터 요소에 autoVerify를 추가했습니다.",
  "dal.add.autoverify.fail": "인텐트 필터 요소에 autoVerify를 추가하지 못했습니다.",
  "dal.alias.choose.label": "별칭(Alias)",
  "dal.keystore.dialog.title": "로컬 키스토어 파일",
  "dal.keystore.dialog.description": "로컬 키스토어 파일을 선택하세요.",
  "dal.keystore.no.alias": "키스토어 파일에서 해당 이름의 별칭을 찾을 수 없습니다.",
  "dal.keystore.not.found": "키스토어 파일을 찾을 수 없습니다.",
  "dal.keystore.check.password": "키스토어 파일을 디코딩하지 못했습니다. 키스토어 비밀번호를 올바르게 입력했는지 확인하세요.",
  "dal.keystore.generate.fingerprint.fail": "키스토어 파일의 SHA-256 지문을 가져오는 중 오류가 발생했습니다. 키스토어 파일이 올바른지 확인하세요.",
  "dal.file.save.fail": "디지털 애셋 링크 파일을 저장할 수 없습니다.",
  "dal.file.save.overwrite.title": "기존 선언 덮어쓰기 확인",
  "dal.file.save.overwrite.message": "프로젝트의 기존 애셋 선언을 새 구성으로 덮어씁니다. 계속하시겠습니까?",
  "dal.could.not.generate": "디지털 애셋 링크 파일을 생성할 수 없습니다.",
  "dal.empty.package.id": "패키지 ID를 지정하세요.",
  "dal.empty.domain": "도메인을 입력하세요.",
  "dal.empty.sign.in.url": "로그인 URL을 입력하세요.",
  "dal.invalid.sign.in.url": "유효한 로그인 URL을 입력하세요.",
  "dal.empty.keystore.file": "키스토어 파일을 선택하세요.",
  "dal.debug.keystore.warning": "알림: 디버그 키스토어를 사용하여 DAL 파일을 생성하면 릴리스 빌드에서 작동하지 않습니다.",
  "dal.support.smart.lock.checkbox.text": "앱과 웹사이트 간에 사용자 인증 정보 공유 지원",
  "dal.what.is.smart.lock.text": "이것은 무엇인가요?",
  "dal.what.is.smart.lock.url": "https://developer.android.com/r/studio-ui/links-assistant/what-is-smartlock.html",
  "dal.support.smart.lock.full.text": "앱과 웹사이트 간에 사용자 인증 정보 공유 지원 <hyperlink>이것은 무엇인가요?</hyperlink>",
  "dal.save.file": "파일 저장",
  "dal.save.file.as.json": "DAL 파일을 *.json으로 저장",
  "dal.save.file.message": "앱을 웹사이트에 연결하는 과정을 완료하려면, 위의 파일을 <a href={0}>{0}</a>에 저장하세요.",
  "dal.save.file.message.nolink": "앱을 웹사이트에 연결하는 과정을 완료하려면, 위의 파일을 {0}에 저장하세요.",
  "dal.save.file.two.places.message": "앱을 웹사이트에 연결하는 과정을 완료하려면, 위의 파일을 <a href={0}>{0}</a> 및 <a href={1}>{1}</a> 양쪽 모두에 저장하세요.",
  "dal.link.and.verify": "연결 및 확인",
  "dal.domain.hint": "예: https://www.example.com"
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
