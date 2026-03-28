import json

translations = {
  "error.could.not.find.separating.space": "구분하는 공백을 찾을 수 없습니다.",   
  "error.latest.existing.revision.found.for.url": "{0}에 대해 기존 최신 리비전을 찾았습니다.",
  "error.could.not.get.relative.path.for.parent.and.child": "{0} 및 {1}의 상대 경로를 가져올 수 없습니다.",
  "error.could.not.parse.svn.version": "svn 버전을 파싱할 수 없음: {0}",      
  "error.could.not.get.svn.version": "종료 코드: {0}, 오류: {1}",
  "error.parse.file.status.unknown.state.on.line": "{0}번째 줄의 알 수 없는 상태", 
  "error.svn.exited.with.error.code": "Svn 프로세스가 오류 코드 {0}을(를) 반환하고 종료되었습니다.",
  "error.authentication.canceled.for.repository": "저장소에 대한 인증 취소됨: {0}",
  "error.svn.status.with.no.output": "명령에 대해 상태 요청이 아무것도 반환하지 않음: {0}",
  "error.svn.status.not.in.working.copy": "작업 사본 외부에 요청된 상태: {0}",
  "toolwindow.working.copies.info.title": "Subversion 작업 사본 정보",
  "svn.short.name.with.mnemonic": "SVN(_S)",
  "svn.name.with.mnemonic": "Subversion(_S)",
  "notification.group.svn.roots": "Subversion 루트 감지 실패",
  "global.group": "전역"
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
