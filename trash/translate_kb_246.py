import json

translations = {
  "label.target.name": "대상 이름:",
  "label.target.url": "대상 URL:",
  "label.export": "내보내기:",
  "checkbox.replace.existing.files": "기존 파일 바꾸기",
  "label.destination": "대상:",
  "checkbox.include.externals.locations": "외부 위치 포함",        
  "label.override.native.eols.with": "'네이티브' EOL 재정의:",
  "combobox.crlf.none": "없음",
  "checkbox.include.ignored.resources": "무시된 리소스 포함",
  "label.import.from": "가져오기 소스:",
  "label.import.to": "가져오기 대상:",
  "label.repositories": "저장소:",
  "label.point.to.repository.location": "저장소 위치를 가리킵니다.",
  "dialog.title.select.share.target": "공유 대상 선택",
  "button.share": "공유",
  "label.define.share.target": "공유 대상 정의",
  "radio.share.target.at.selected.repository.location": "선택한 저장소 위치에",
  "radio.share.target.in.new.folder": "선택한 저장소 위치의 새 \"{0}\" 폴더에",
  "checkbox.create.tags.branches": "/tags 및 /branches 만들기",
  "separator.commit.comment.prefix": "커밋 주석 접두사",
  "toolwindow.stripe.SVN_Repositories": "SVN 저장소",
  "label.auth.authentication.realm": "인증 영역: ''{0}''",
  "label.auth.user.name": "사용자 이름(&U):",
  "label.auth.password": "비밀번호(&P):",
  "checkbox.auth.keep.for.current.session": "자격 증명 저장(&S)",
  "dialog.title.authentication.required": "인증 필요",
  "notification.content.unknown.certificate.type.from.url": "Subversion: {0}의 알 수 없는 인증서 유형",
  "notification.content.authentication.failed": "인증 실패: {0}",   
  "popup.content.already.checking": "이미 확인 중\\u2026",
  "progress.title.svn.roots.authorization.checker": "SVN VCS 루트 권한 검사기",
  "progress.title.looking.for.file.working.copy.root": "''{0}'' 작업 사본 루트 찾는 중",
  "progress.text.clearing.stored.credentials": "{0}에 저장된 자격 증명 지우는 중",
  "notification.title.not.logged.into.subversion": "Subversion에 로그인되어 있지 않음",
  "notification.content.not.logged.into.subversion": "Subversion ''{0}''({1})에 로그인되어 있지 않습니다.",
  "notification.action.click.to.fix": "클릭하여 수정하세요.",
  "progress.title.clear.authentication.cache": "인증 캐시 지우기(&C)",
  "label.specify.ssl.protocol.manually": "수동으로 SSL 프로토콜 선택해 보세요(SSLv3 또는 TLSv1).",
  "popup.content.failed.to.authenticate.to.proxy.change.credentials": "프록시 인증 실패. \n  HTTP 프록시 설정에서 프록시 자격 증명을 변경할 수 있습니다.",
  "popup.content.failed.to.authenticate.to.proxy": "프록시 인증에 실패했습니다.",
  "error.server.ssl.certificate.rejected": "서버 SSL 인증서가 거부되었습니다.",   
  "progress.text2.collecting.history": "''{0}''의 리비전 기록 수집 중",
  "checkbox.changes.filter.filter.by.author": "작성자(&U):",
  "progress.text2.processing.revision": "''{0}'' 리비전 처리 중",
  "progress.text.changes.collecting.changes": "변경사항 정보 수집 중",
  "progress.text2.changes.establishing.connection": "''{0}''에 대한 연결 설정 중",
  "progress.text2.revision.processed": "''{0}'' 리비전 처리됨",
  "action.Subversion.ShowMergeSourceDetails.text": "병합 소스 세부정보 표시",
  "action.Subversion.ShowIntegratePanel.text": "통합 패널 표시",
  "progress.title.loading.working.copies.data": "Subversion: 작업 사본 데이터 로드 중\\u2026",
  "progress.title.edit.revision.comment": "리비전 커밋 편집"
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
