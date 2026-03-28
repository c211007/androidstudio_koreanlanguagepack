import json

translations = {
  "dialog.message.invalid.repository.location": "잘못된 저장소 위치",  
  "checkbox.switch.to.newly.created.branch.or.tag": "새로 만든 브랜치 또는 태그로 {0} 전환",
  "error.can.not.find.url.for.file": "파일에 대한 URL을 찾을 수 없음: {0}",
  "error.can.not.find.working.copy.for.file": "파일에 대한 작업 사본을 찾을 수 없음: {0}",
  "progress.title.svn.branches.preloader": "Subversion 브랜치 프리로더",     
  "dialog.title.relocate.working.copy": "작업 사본 재배치",
  "label.from.url": "원본 URL:",
  "label.to.url": "대상 URL:",
  "dialog.message.error.relocating.working.copy": "작업 사본 재배치 오류: {0}",
  "progress.title.relocating.working.copy": "작업 사본 재배치 중",
  "dialog.title.lock.files": "파일 잠금",
  "dialog.title.lock.file": "파일 잠금",
  "label.lock.comment": "잠금 주석(&L):",
  "label.locl.steal.existing": "기존 잠금 가져오기(&S)",
  "label.ssh.key.file": "키 파일(&F):",
  "label.ssh.passphrase": "비밀번호(&R):",
  "label.ssl.certificate.path": "인증서 경로:",
  "label.ssl.certificate.password": "인증서 비밀번호:",
  "checkbox.ssl.keep.for.current.session": "자격 증명 저장(&S)",
  "progress.text.create.remote.folder": "원격 폴더 만들기",
  "dialog.title.error": "오류",
  "progress.text.deleting": "{0} 삭제 중",
  "progress.title.browser.delete": "삭제",
  "progress.text.browser.creating": "{0} 만들기",
  "progress.text.browser.moving": "{0} 이동 중",
  "progress.text.browser.copying": "{0} 복사 중",
  "progress.text.browser.remote.destination": "대상 {0}",
  "progress.title.browser.move": "이동",
  "progress.title.browser.copy": "복사",
  "dialog.message.could.not.parse.url": "URL을 구문 분석할 수 없음",
  "dialog.title.changes.in.url": "{0}의 변경사항",
  "action.Subversion.RepositoryBrowser.Checkout.text": "체크아웃(_C)\\u2026",      
  "dialog.title.svn.repository.browser": "SVN 저장소 브라우저",
  "action.Subversion.RepositoryBrowser.CompareWith.text": "비교 대상\\u2026",
  "dialog.message.confirm.move.folder": "이름이 ''{0}''인 폴더를 이동하려고 합니다. 계속하시겠습니까?",
  "action.Subversion.RepositoryBrowser.CopyUrl.text": "URL 복사\\u2026",        
  "action.Subversion.RepositoryBrowser.Export.text": "내보내기(_E)\\u2026",
  "dialog.title.import.directory": "디렉터리 가져오기",
  "label.select.directory.to.import.into.repository": "저장소로 가져올 디렉터리 선택",
  "dialog.title.destination.directory": "대상 디렉터리",
  "label.select.checkout.destination.directory": "체크아웃할 대상 디렉터리 선택",
  "label.select.export.destination.directory": "내보낼 대상 디렉터리 선택",
  "progress.title.loading.child.entries": "하위 항목 로드 중",
  "dialog.title.svn.import.options": "SVN 가져오기 옵션",
  "dialog.title.svn.export.options": "SVN 내보내기 옵션",
  "dialog.title.export.directory": "디렉터리 내보내기",
  "label.select.directory.to.export.from.subversion": "Subversion에서 내보낼 디렉터리 선택",
  "dialog.title.svn.delete": "SVN 삭제",
  "label.source.url": "소스 URL:",
  "label.target.location": "대상 위치:"
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
