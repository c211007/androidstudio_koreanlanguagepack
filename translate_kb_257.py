import json

translations = {
  "progress.title.resolve.tree.conflict": "트리 충돌 해결 중",
  "dialog.title.resolve.tree.conflict": "트리 충돌 해결",
  "dialog.message.keep.newly.created.files.in.their.original.place": "새로 생성한 파일을 원본 위치에 유지하시겠습니까?",
  "dialog.message.accept.theirs.for.path": "{0}에 대해 다른 수정본을 수락하시겠습니까?",
  "dialog.message.accept.yours.for.path": "{0}에 대해 내 수정본을 수락하시겠습니까?",
  "progress.title.accepting.theirs.for.path": "{0}에 대해 다른 수정본 수락 중",      
  "progress.title.accepting.yours.for.path": "{0}에 대해 내 수정본 수락 중",        
  "dialog.message.select.binary.files.to.patch": "패치할 바이너리 파일 선택",
  "dialog.message.merge.from.theirs.delete.binary.file": "(다른 수정본의 변경 사항에 따라) 바이너리 파일 {0}을(를) 삭제하시겠습니까?",
  "dialog.message.merge.from.theirs.create.binary.file": "(다른 수정본의 변경 사항에 따라) 바이너리 파일 {0}을(를) 생성하시겠습니까?",
  "dialog.message.merge.from.theirs.modify.binary.file": "(다른 수정본의 변경 사항에 따라) 바이너리 파일 {0}에 변경 사항을 적용하시겠습니까?",
  "button.keep": "유지",
  "button.move": "이동",
  "button.resolve.conflict.merge": "병합",
  "button.resolve.conflict.accept.yours": "내 수정본 수락",
  "button.resolve.conflict.accept.theirs": "다른 수정본 수락",
  "label.path.revisions.info": "{0}(현재: {1}, 커밋됨: {2})",
  "label.conflict.left.side": "왼쪽: {0}",
  "label.conflict.right.side": "오른쪽: {0}",
  "label.conflict.directory.added": "(디렉터리) 추가됨",
  "label.conflict.file.added": "(파일) 추가됨",
  "label.conflict.directory.unversioned": "(디렉터리) 버전 관리되지 않음",
  "label.conflict.file.unversioned": "(파일) 버전 관리되지 않음",
  "label.before.accepting.theirs.for.path": "{0}에 대해 다른 수정본을 수락하기 전",  
  "label.after.accepting.theirs.for.path": "{0}에 대해 다른 수정본을 수락한 후",    
  "message.theirs.changes.merged.for.file": "{0}의 다른 수정본 변경 사항이 병합되었습니다.",    
  "message.theirs.accepted.for.file": "{0}에 대해 다른 수정본이 수락되었습니다.",
  "message.yours.accepted.for.file": "{0}에 대해 내 수정본이 수락되었습니다.",
  "value.patch.file.name": "TheirsChanges.patch",
  "error.can.not.load.theirs.content.for.file": "파일 {0}에 대해 다른 수정본 콘텐츠를 로드할 수 없습니다.",
  "tree.conflict.description": "{2}에 로컬 {0}, 수신 중인 {1}",
  "conflict.reason.edited": "편집",
  "conflict.reason.obstructed": "차단됨",
  "conflict.reason.deleted": "삭제",
  "conflict.reason.missing": "누락",
  "conflict.reason.unversioned": "버전 관리되지 않음",
  "conflict.reason.added": "추가",
  "conflict.reason.replaced": "바뀜",
  "conflict.reason.moved.away": "이동됨",
  "conflict.reason.moved.here": "여기로 이동됨",
  "conflict.action.edit": "편집",
  "conflict.action.add": "추가",
  "conflict.action.delete": "삭제",
  "conflict.action.replace": "바뀜",
  "conflict.operation.update": "업데이트",
  "conflict.operation.switch": "전환",
  "conflict.operation.merge": "병합",
  "conflict.operation.none": "없음",
  "dialog.create.branch.or.tag.from.working.copy.warning": "<html><b>로컬 변경 사항이 있는</b> 분기를 생성하려면 이 변형(Variant)을 사용하세요.\n  <br/>일반적으로 대상 디렉터리뿐만 아니라 여러 항목이 '기록과 함께 추가'됩니다.\n  <br/><br/>리비전이 루트와 다른 각 파일은 개별적으로 복사됩니다.\n  <br/>따라서 분기를 만들기 전에 작업 사본을 업데이트하는 것이 좋습니다.</html>", 
  "exportable.SvnDiffSettings.presentable.name": "Svn Diff"
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
