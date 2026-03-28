import json

translations = {
  "action.Subversion.Unlock.text": "잠금 해제(_O)",
  "action.Subversion.Unlock.description": "파일 잠금을 해제합니다.",
  "action.name.refresh": "새로고침",
  "action.Subversion.ImportToSVNRepository.text": "Subversion으로 가져오기(_M)\\u2026",
  "action.Subversion.Share.text": "디렉터리 공유(_S)\\u2026",
  "action.Subversion.ConfigureBranches.text": "브랜치 구성\\u2026",      
  "action.Subversion.CompareWithBranch.text": "브랜치와 비교\\u2026",     
  "action.Subversion.Relocate.text": "재배치\\u2026",
  "action.Subversion.Relocate.description": "작업 사본을 다른 URL로 재배치합니다.",
  "action.Subversion.CleanupProject.text": "프로젝트 정리",
  "action.Subversion.CleanupProject.description": "프로젝트의 모든 작업 사본 디렉터리에 대해 정리를 수행합니다.",
  "action.Svn.Show.Working.Copies.text": "작업 사본 표시",
  "action.Svn.Show.Working.Copies.description": "작업 사본 형식 및 URL과 같은 정보를 표시합니다.",
  "action.Svn.RefreshWorkingCopies.text": "새로고침",
  "action.Svn.RefreshWorkingCopies.description": "작업 사본 정보를 새로고침합니다.",
  "action.EditCommitMessage.text": "리비전 커밋 편집",
  "action.EditCommitMessage.description": "리비전 커밋을 편집합니다. 이전 메시지를 덮어씁니다.",
  "action.Subversion.ShareWholeProject.text": "프로젝트 공유(Subversion)\\u2026",
  "dialog.title.new.remote.folder": "새 원격 폴더",
  "label.remote.folder.url": "원격 폴더 URL:",
  "label.remote.folder.name": "원격 폴더 이름:",
  "label.commit.message": "커밋 메시지:",
  "label.recent.messages": "최근 메시지:",
  "value.new.folder.name": "NewFolder",
  "button.copy": "복사",
  "action.new.remote.folder.text": "새 원격 폴더\\u2026",
  "dialog.title.branch": "브랜치 또는 태그 만들기",
  "label.copy.from": "복사 원본",
  "label.copy.to": "복사 위치",
  "label.copy.from.revision": "리비전(&V):",
  "label.branch.base.url": "기본 URL:",
  "label.branch.name": "이름:",
  "value.new.branch.name": "new_branch",
  "tooltip.use.project.location": "프로젝트 위치 사용",
  "radio.copy.working.copy": "작업 사본(&W)",
  "radio.copy.repository.location": "저장소 위치(&R):",
  "radio.copy.to.branch.or.tag": "브랜치 또는 태그",
  "radio.copy.to.any.location": "모든 위치",
  "label.copy.comment": "주석(&C)",
  "label.copy.select.location.dialog.copy.as": "다음으로 복사(&A):",
  "notification.content.branches.load.error": "브랜치 로드 오류: {0}",       
  "progress.title.checking.target.folder": "대상 폴더 확인 중",
  "dialog.message.repository.path.does.not.exist": "''{0}'' 저장소 경로가 존재하지 않습니다. 새로 만드시겠습니까?",
  "dialog.title.select.working.copy.location": "작업 사본 위치 선택",  
  "label.select.location.to.copy.from": "복사할 원본 위치 선택:",        
  "dialog.message.branch.name.is.empty": "브랜치 이름이 비어 있습니다.",
  "dialog.message.invalid.branch.name": "잘못된 브랜치 이름",
  "dialog.message.invalid.branch.url": "잘못된 브랜치 URL",
  "dialog.message.no.branch.base.location.selected": "브랜치 기준 위치가 선택되지 않았습니다.",
  "dialog.message.invalid.revision": "잘못된 리비전"
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
