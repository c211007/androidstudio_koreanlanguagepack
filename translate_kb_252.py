import json

translations = {
  "configure.branches.trunk.location": "트렁크 위치:",
  "configure.branches.branch.locations": "분기 위치:",
  "refresh.branches.item": "분기 새로고침…",
  "copy.column.title": "복사",
  "copy.column.tooltip": "{0}에서 별도로 복사됨",
  "progress.title.loading.branches": "분기 로드 중",
  "compare.with.branch.progress.loading.content": "콘텐츠 로드 중",
  "compare.with.branch.diff.title": "분기와 비교",
  "compare.with.branch.error.title": "분기와 비교",
  "compare.with.branch.popup.title": "분기와 비교",
  "compare.with.branch.location.error": "''{1}'' 분기 아래 ''{0}'' 파일의 저장소 위치를 찾을 수 없습니다.\\n분기 구성을 확인하세요.",   
  "action.name.switch": "전환",
  "import.dialog.title": "Subversion으로 가져오기",
  "import.dialog.button": "가져오기",
  "repository.browser.add.location.action.text": "저장소 위치 추가",     
  "repository.browser.add.location.action.description": "저장소 위치를 추가합니다",
  "repository.browser.no.locations.added.info": "추가된 저장소 위치가 없습니다.",
  "repository.browser.add.location.prompt": "저장소 URL:",
  "repository.browser.add.location.title": "새 저장소 위치",
  "repository.browser.details.action": "세부정보 표시/숨기기",
  "repository.browser.refresh.action": "선택한 트리 노드 새로고침",
  "repository.browser.add.location.menu.item": "저장소 위치(_R)…",   
  "repository.browser.edit.location.menu.item": "위치 URL 편집(_U)…",   
  "repository.browser.discard.location.action": "위치 폐기(_L)",
  "repository.browser.discard.location.prompt": "''{0}'' 위치를 폐기하시겠습니까?",
  "repository.browser.discard.location.title": "위치 폐기",
  "repository.browser.new.folder.action": "원격 폴더(_F)…",
  "action.repository.browser.history.text": "기록 표시",
  "action.repository.browser.history.description": "기록을 표시합니다.",
  "repository.browser.import.action": "가져오기(_I)…",
  "diff.options.title": "분기 또는 태그와 비교",
  "diff.options.label.compare": "비교 대상:",
  "diff.options.label.with": "비교할 항목:",
  "diff.options.label.compare.type": "비교 유형",
  "diff.options.checkbox.reverse.diff": "Diff 반전",
  "diff.options.radio.graphical.compare": "그래픽 비교",
  "diff.options.radio.unified.diff": "통합(Unified) Diff",
  "diff.options.no.url.error": "비교할 URL을 선택하세요.",
  "diff.options.same.url.error": "비교할 다른 URL을 선택하세요.",     
  "diff.options.no.patch.file.error": "패치 파일을 저장할 경로를 지정하세요.",
  "dialog.title.save.unified.diff": "패치 파일",
  "label.select.file.to.save.unified.diff": "통합 Diff를 저장할 파일 선택",
  "diff.cant.get.properties.changes": "SVN 속성을 표시할 수 없습니다.",
  "repository.browser.browse.changes.action": "변경 사항 찾아보기(_B)…",
  "repository.browser.browse.changes.description": "선택한 노드에서 변경된 내역을 봅니다.",
  "repository.browser.compare.title": "''{0}'' 및 ''{1}'' 비교",
  "error.could.not.compare.local.file.and.remote.url.with.executable.for.svn.version": "svn {0}의 실행 파일로 로컬 파일과 원격 URL을 비교할 수 없습니다.",
  "cleanup.action.name": "정리",
  "changes.browser.revision.term": "리비전",
  "dialog.title.computing.difference": "차이점 계산 중"
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
