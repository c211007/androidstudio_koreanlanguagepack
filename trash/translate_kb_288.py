import json

translations = {
  "progress.text.applying.fixes": "수정 사항 적용 중…",
  "progress.text.reformatting.code": "코드 서식 재지정 중…",
  "progress.text.rearranging.code": "코드 재정렬 중…",
  "progress.text.optimizing.imports": "import 최적화 중…",
  "progress.text.analyzing.code": "코드 분석 중…",
  "progress.text.checking.for.todo": "TODO 항목 확인 중…",
  "progress.text.searching.for.modified.files": "수정된 파일 찾는 중",
  "button.text.overwrite.modified.file": "수정된 파일 덮어쓰기(&O)",
  "button.text.overwrite.modified.files": "수정된 파일 덮어쓰기(&O)",
  "message.text.file.locally.modified": "{0} 파일이 로컬에서 수정되었습니다.",
  "message.text.several.files.locally.modified": "일부 파일이 로컬에서 수정되었습니다.",
  "update.group.name.updated.from.server": "서버에서 업데이트됨",
  "update.group.name.updated": "업데이트됨",
  "update.group.name.created": "생성됨",
  "update.group.name.deleted": "삭제됨",
  "update.group.name.restored": "복원됨",
  "update.group.name.modified": "수정됨",
  "update.group.name.skipped": "건너뜀",
  "update.group.name.merged.with.property.conflicts": "속성 충돌과 함께 병합됨",
  "update.group.name.merged.with.tree.conflicts": "트리 충돌과 함께 병합됨",
  "update.group.name.merged.with.conflicts": "충돌과 함께 병합됨",
  "update.group.name.merged": "병합됨",
  "update.group.name.not.in.repository": "저장소에 없음",
  "update.group.name.locally.added": "로컬에 추가됨",
  "update.group.name.locally.removed": "로컬에서 제거됨",
  "update.group.name.switched": "전환됨",
  "status.group.name.changed.on.server": "서버에서 변경됨",
  "status.group.name.changed": "변경됨",
  "status.group.name.created": "생성됨",
  "status.group.name.deleted": "삭제됨",
  "status.group.name.modified": "수정됨",
  "status.group.name.skipped": "건너뜀",
  "status.group.name.will.be.restored": "복원 예정",
  "status.group.name.will.be.merged.with.property.conflicts": "속성 충돌과 함께 병합 예정",
  "status.group.name.will.be.merged.with.tree.conflicts": "트리 충돌과 함께 병합 예정",
  "status.group.name.will.be.merged.with.conflicts": "충돌과 함께 병합 예정",
  "status.group.name.will.be.merged": "병합 예정",
  "status.group.name.not.in.repository": "저장소에 없음",
  "status.group.name.locally.added": "로컬에 추가됨",
  "status.group.name.locally.removed": "로컬에서 제거됨",
  "status.group.name.switched": "전환됨",
  "border.changes.filter.change.number.filter": "변경",
  "border.changes.filter.date.filter": "날짜",
  "checkbox.show.changes.after.num": "시작(&F)",
  "checkbox.show.changes.before.num": "끝(&T):",
  "checkbox.show.changes.before.date": "이전(&B)",
  "checkbox.show.changes.after.date": "이후(&A)",
  "exception.text.internal.errror.could.not.implement.method": "구현할 수 없음",
  "message.text.could.not.load.virtual.file.content": "{0} 파일의 콘텐츠를 로드할 수 없습니다: {1}",
  "message.title.could.not.load.content": "콘텐츠를 로드할 수 없음"
}

with open("missing_translations/missing_keys_korean.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for file_info in data.get("new_files", []):
    if file_info.get("filename") == "VcsBundle.properties":
        keys_dict = file_info.get("keys", file_info.get("properties", {}))
        keys_dict.update(translations)
        file_info["keys"] = keys_dict
        break

with open("missing_translations/missing_keys_korean.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)
