import json

translations = {
  "progress.searching.for.files.with.conflicts": "충돌이 있는 파일 검색 중",
  "add.files.errors.title": "파일 추가 오류",
  "move.files.errors.title": "파일 이동 오류",
  "error.target.of.move.operation.is.already.under.version.control": "이동 작업의 대상이 이미 버전 관리 중입니다.",
  "error.move.have.not.been.performed": "Subversion 이동이 수행되지 않았습니다.",
  "delete.files.errors.title": "파일 삭제 오류",
  "progress.title.adding.files.to.subversion": "Subversion에 파일 추가 중",    
  "progress.title.deleting.files.from.subversion": "Subversion에서 파일 삭제 중",
  "progress.title.moving.files.in.subversion": "Subversion에서 파일 이동 중",    
  "copy.dialog.title": "분기 또는 태그",
  "move.dialog.title": "이동 또는 이름 바꾸기",
  "select.location.invalid.url.message": "잘못된 Subversion 저장소 URL: ''{0}''",
  "share.directory.action": "디렉터리 공유…",
  "share.directory.commit.message": "{2}\\n{1}이(가) ''{0}'' 디렉터리를 만들었습니다.",   
  "share.directory.title": "디렉터리 공유",
  "dialog.message.share.to.not.empty.directory": "\"{0}\" 원격 폴더가 비어 있지 않습니다.\\n공유를 계속하시겠습니까?",
  "share.directory.info.message": "공유 작업을 완료하려면 ''{0}''을(를) 커밋하세요.",
  "share.directory.create.dir.progress.text": "{0} 원격 폴더 생성 중",     
  "share.directory.checkout.back.progress.text": "{0} 체크아웃 중",
  "share.or.import.add.progress.text": "{0} 추가 예약 중",
  "progress.title.share.directory": "디렉터리 공유",
  "progress.title.check.remote.folder.contents": "원격 폴더 콘텐츠 확인 중",
  "tab.title.failed.to.share.project": "프로젝트 공유 실패",
  "action.share.whole.project.text": "프로젝트 공유(Subversion)…",       
  "action.Subversion.integrate.changes.select.working.copy.text": "작업 사본에 통합:",
  "dialog.title.integrate.to.branch": "분기에 통합",
  "action.Subversion.integrate.changes.message.not.under.control.text": "선택한 대상이 Subversion의 통제를 받지 않습니다. 계속하시겠습니까?",
  "action.Subversion.integrate.changes.message.another.wc.text": "선택한 대상이 다른 저장소의 작업 사본 안에 있습니다. 계속하시겠습니까?",
  "action.Subversion.integrate.changes.branch.info.source.label.text": "소스 분기 URL: {0}",
  "action.Subversion.integrate.changes.branch.info.target.label.text": "대상 분기 URL: {0}",
  "action.Subversion.integrate.changes.actionname": "분기에 통합…",
  "action.Subversion.integrate.changes.description": "선택한 변경 목록/변경 집합을 선택한 분기에 통합합니다.",
  "action.Subversion.integrate.changes.messages.title": "분기에 통합",  
  "dialog.message.integrate.changes.error.no.available.files": "통합할 수 있는 파일이 없습니다.",
  "popup.title.select.branch.to.integrate.to": "통합할 분기 선택…",
  "dialog.message.integrate.changes.error.same.source.and.target": "통합을 시작할 수 없음: 대상 분기와 소스 분기가 동일합니다.",
  "dialog.message.integrate.changes.error.target.not.dir": "통합을 시작할 수 없음: 대상 디렉터리가 없거나 디렉터리가 아닙니다.",
  "dialog.message.integrate.changes.error.not.versioned": "통합을 시작할 수 없음: 대상 디렉터리가 Subversion 제어 하에 있지 않거나 선택한 분기에 속하지 않습니다.",
  "action.Subversion.integrate.changes.dialog.add.wc.text": "추가",
  "action.Subversion.integrate.changes.dialog.remove.wc.text": "제거",        
  "action.Subversion.integrate.changes.message.files.up.to.date.text": "모든 파일이 최신 상태입니다.",
  "action.Subversion.integrate.changes.collecting.changes.to.commit.task.title": "커밋할 변경 사항 수집 중",
  "action.Subversion.integrate.changes.error.unable.to.collect.changes.text": "커밋할 변경 사항을 수집하는 중 오류 발생: {0}",
  "error.cannot.load.revisions": "리비전 목록을 로드할 수 없음",
  "action.Subversion.integrate.changes.progress.integrating.text": "변경 사항 병합 중",
  "update.switch.to.branch.text": "사용할 분기:",
  "popup.title.select.branch": "분기 선택",
  "progress.live.provider.loading.revisions.text": "서버에서 리비전 로드 중",
  "progress.live.provider.loading.revisions.details.text": "서버에서 리비전 로드 중…",
  "dialog.show.svn.map.title": "Subversion 작업 사본 정보"
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
