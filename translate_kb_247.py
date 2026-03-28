import json

translations = {
  "tab.title.edit.revision.comment": "리비전 커밋 편집",
  "progress.title.getting.latest.repository.revision": "최신 저장소 리비전 가져오는 중",
  "notification.content.revision.commit.message.changed.to": "#{0} 리비전 주석이 변경되었습니다.\\n''{1}''",
  "column.name.merge.sources": "병합 소스",
  "status.text.merge.sources": "병합 소스",
  "label.no.subversion.1.5.working.copies": "프로젝트에 1.5 저장소에 대한 Subversion 1.5\\n작업 사본이 없습니다.",
  "label.merge.from.url": "보낸사람:",
  "label.merge.to.branch": "대상:",
  "label.mixed.revision.working.copy": "혼합 리비전 작업 사본",
  "label.select.target.working.copy": "대상 작업 사본의 경로 선택", 
  "configurable.name.svn.general": "Subversion",
  "configurable.name.svn.presentation": "프리젠테이션",
  "configurable.name.svn.network": "네트워크",
  "configurable.name.svn.ssh": "SSH",
  "dialog.title.select.configuration.directory": "구성 디렉터리 선택",
  "action.title.select.configuration.directory": "구성 디렉터리 변경",
  "dialog.description.select.configuration.directory": "Subversion 구성 디렉터리를 선택하거나 새로 만듭니다.",
  "button.text.clear.authentication.cache": "인증 캐시 지우기(&C)",
  "label.text.delete.stored.credentials": "'http', 'svn', 'svn+ssh' 프로토콜에 대해 저장된 모든 자격 증명을 삭제합니다.",
  "button.text.edit.proxies": "네트워크 옵션 편집(&O)\\u2026",
  "dialog.title.edit.http.proxies.settings": " 네트워크 계층과 관련된 Subversion 옵션 변경",
  "dialog.edit.http.proxies.settings.error.same.group.names.text": "동일한 이름을 가진 그룹 감지됨: ''{0}''",
  "dialog.edit.http.proxies.settings.error.ambiguous.group.patterns.text": "여러 그룹과 일치하는 저장소 URL 찾음: {0}",
  "dialog.edit.http.proxies.settings.error.ambiguous.group.patterns.to.text": "{0} URL이 {1}과(와) 일치함\\n",
  "dialog.edit.http.proxies.settings.tab.edit.user.file.title": "사용자 파일",    
  "dialog.edit.http.proxies.settings.tab.edit.system.file.title": "시스템 파일",
  "dialog.edit.http.proxies.settings.port.must.be.number.error": "포트는 숫자여야 합니다(''{0}'' 그룹).",
  "dialog.edit.http.proxies.settings.timeout.must.be.number.error": "HTTP 제한 시간은 숫자여야 합니다(''{0}'' 그룹).",
  "dialog.edit.http.proxies.settings.dialog.select.ssl.client.certificate.path.title": "인증서 경로 선택",
  "dialog.edit.http.proxies.settings.panel.proxy.title": "HTTP 프록시 설정", 
  "dialog.edit.http.proxies.settings.panel.ssl.title": "SSL 설정",
  "dialog.edit.http.proxies.settings.panel.repositories.title": "저장소", 
  "dialog.edit.http.proxies.settings.patterns.text": "URL 패턴(&R):",
  "dialog.edit.http.proxies.settings.exceptions.text": "예외(&X):",
  "dialog.edit.http.proxies.settings.server.text": "서버(&S):",
  "dialog.edit.http.proxies.settings.user.text": "사용자(&U):",
  "dialog.edit.http.proxies.settings.port.text": "포트(&O):",
  "dialog.edit.http.proxies.settings.password.text": "비밀번호(&W):",
  "dialog.edit.http.proxies.settings.connection.timeout.text": "연결 제한 시간(&I):",
  "dialog.edit.http.proxies.settings.seconds.text": "초",
  "dialog.edit.http.proxies.settings.paths.to.authority.certificates.text": "CA 인증서 파일에 대한 쉼표로 구분된 경로(&P):",
  "dialog.edit.http.proxies.settings.ssl.client.certificate.file.text": "SSL 클라이언트 인증서 파일(&C):",
  "dialog.edit.http.proxies.settings.client.certificate.passphrase.text": "SSL 클라이언트 인증서 비밀번호(&H):",
  "dialog.edit.http.proxies.settings.trust.default.cas.text": "기본 CA 신뢰(&A)",
  "dialog.edit.http.proxies.settings.test.connection.button.text": "연결 테스트(&T)",
  "dialog.edit.http.proxies.settings.test.connection.settings.will.be.stored.title": "경고",
  "dialog.edit.http.proxies.settings.test.connection.settings.will.be.stored.text": "설정이 저장됩니다.",
  "dialog.edit.http.proxies.settings.test.connection.error.title": "연결 테스트 실패",
  "dialog.edit.http.proxies.settings.test.connection.success.title": "연결 테스트 성공",
  "dialog.edit.http.proxies.settings.test.connection.success.text": "연결 테스트가 완료되었습니다."
}

with open("missing_translations/missing_keys_korean.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for file_info in data.get("new_files", []):
    if file_info.get("filename") == "SvnBundle.properties":
        keys_dict = file_info.get("keys", file_info.get("properties", {}))
        keys_dict.update(translations)
        file_info["keys"] = keys_dict
        break

with open("missing_translations/missing_keys_korean.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)
