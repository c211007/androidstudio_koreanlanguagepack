import json

translations = {
  "label.depth.empty": "비어 있음",
  "label.depth.files": "파일",
  "label.depth.immediates": "직접 요소(immediates)",
  "label.depth.infinity": "무한(infinity)",
  "label.depth.exclude": "제외",
  "label.depth.unknown": "알 수 없음",
  "undo.integrate.to.branch": "분기에 통합 실행 취소…",
  "undo.integrate.to.branch.description": "리비전에서 수행된 변경 사항을 분기에서 제거합니다.",
  "undo.integrate.to.branch.dialog.title": "분기에 통합 실행 취소",
  "merge.source.details.title": "{0} [{1}]의 소스 세부정보 병합",
  "repository.browser.edit.location.dialog.title": "위치 URL 편집",        
  "action.Subversion.TogglePropertiesDiff.text": "속성 표시",
  "action.Subversion.TogglePropertiesDiff.description": "SVN 속성의 차이점을 표시합니다.",
  "action.IntegrateChangeSetAction.text": "분기에 통합",
  "show.properties.diff.progress.text.revision.information": "리비전 {0}",    
  "show.properties.diff.progress.text2.property.information": "속성 {0}",   
  "checkbox.ignore.whitespace.when.merge.text": "공백 무시(&8)",
  "label.file.has.conflicts": "파일에 {0}개의 충돌이 있어 커밋할 수 없습니다.",
  "label.file.has.conflicts.before.or.after": "파일에 {0}개의 충돌이 있어 커밋할 수 없습니다.\\n\n {1}",
  "label.file.has.conflicts.before.and.after": "파일에 {0}개의 충돌이 있어 커밋할 수 없습니다.\\n\n 이전: {1}\\n\n 이후: {2}",
  "label.locally.deleted.file.has.conflicts": "파일에 {0}개의 충돌이 있습니다.",       
  "file.conflict.tree": "트리",
  "file.conflict.text": "텍스트",
  "file.conflict.property": "속성",
  "action.Subversion.MarkTreeResolved.text": "트리 충돌 해결됨으로 표시…",
  "dialog.message.mark.tree.conflict.resolved.confirmation": "트리 충돌을 해결됨으로 표시하시겠습니까?",
  "dialog.title.mark.tree.conflict.resolved": "트리 충돌 해결됨으로 표시",    
  "progress.title.mark.tree.conflict.resolved": "트리 충돌 해결됨으로 표시 중",  
  "svn.integrate.changelist.warning.unresolved.conflicts.text": "통합이 중단되었습니다. 해결되지 않은 충돌이나 건너뛴 항목이 있습니다.",
  "error.integration.was.canceled": "통합이 취소되었습니다.",
  "svn.option.ignore.whitespace.in.annotate": "어노테이션에서 공백 차이 무시",
  "annotation.show.merge.sources.default.text": "기록 및 어노테이션에 병합 소스 표시",
  "svn.cannot.save.credentials.store-auth-creds": "자격 증명을 저장할 수 없음: \"store-auth-creds = no\"에 의해 금지됨",
  "annotation.original.revision": "원본 리비전",
  "confirmation.resolve.tree.conflict.merge.moved": "로컬로 이동된 {1}에 {0}의 변경 사항을 적용하시겠습니까?",
  "confirmation.resolve.tree.conflict.merge.renamed": "로컬로 이름이 바뀐 {1}에 {0}의 변경 사항을 적용하시겠습니까?",
  "action.Subversion.Create.External.text": "외부 생성…",
  "action.Subversion.Create.External.description": "URL을 선택하고, svn:external 속성을 추가하고, 필요한 경우 체크아웃합니다.",
  "button.select": "선택",
  "dialog.title.select.target.for.external": "외부에 대한 대상 선택",      
  "dialog.message.target.file.already.exists": "대상 파일이 이미 있습니다.",    
  "progress.title.creating.external": "외부 생성 중",
  "tab.title.create.external": "외부 생성",
  "error.selected.destination.conflicts.with.existing": "선택한 대상이 기존 항목과 충돌합니다: {0}",
  "label.local.target": "로컬 대상:",
  "checkbox.checkout": "체크아웃",
  "svn.edit.commit.message.title": "리비전 #{0} 코멘트 편집",
  "svn.edit.commit.message.attention": "주의! 이전 메시지가 손실됩니다!",
  "svn.edit.commit.message.prompt": "새 리비전 코멘트:",
  "quick.merge.variants.merge.all": "모두 병합"
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
