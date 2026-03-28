import json

translations = {
  "settings.files.with.ignored.conflicts.list.title": "무시된 충돌이 있는 파일:",
  "settings.inactive.changelist.group.title": "비활성 변경 목록",
  "settings.changelist.conflicts.group.title": "충돌",
  "action.name.show.files.as.tree": "트리로 표시",
  "label.selected.revision.commit.message": "커밋 메시지",
  "column.name.revision.version": "버전",
  "column.name.revision.date": "날짜",
  "action.name.compare": "비교",
  "action.description.compare": "버전 비교",
  "message.text.cannot.show.differences": "차이점을 표시할 수 없: {0}",
  "message.title.show.differences": "차이점 표시",
  "action.name.refresh": "새로고침",
  "action.description.refresh": "파일 이력 새로고침",
  "action.name.get.file.content.from.repository": "리비전에서 가져오기",
  "action.name.refresh.compare.with.local.panel": "새로고침",
  "action.description.refresh.compare.with.local.panel": "변경 사항 새로고침",
  "acton.name.get.revision": "리비전 가져오기",
  "action.name.create.patch": "패치 생성…",
  "action.description.create.patch.for.selected.revisions": "선택한 리비전에 대한 패치를 생성합니다.",
  "message.title.get.version": "버전 가져오기",
  "message.text.cannot.load.revision": "리비전을 로드할 수 없습니다: {0}",
  "message.text.cannot.save.content": "콘텐츠를 저장할 수 없습니다: {0}",
  "message.title.get.revision.content": "리비전 콘텐츠 가져오기",
  "column.name.revision.list.date": "날짜",
  "checkbox.show.changed.revisions.only": "변경 사항만",
  "progress.text.loading.patch.base.revision": "패치 기본 리비전 로드 중",
  "diff.content.title.revision.number": "리비전 {0}",
  "command.name.open.error.message.view": "오류 메시지 뷰 열기",
  "message.text.cannot.edit.file": "파일을 편집할 수 없습니다: {0}",
  "message.title.edit.files": "파일 편집",
  "vcs.console.toolwindow.display.name": "콘솔",
  "handle.ro.file.status.type.using.vcs": "{0} 사용",
  "message.text.file.is.up.to.date": "파일이 최신 상태입니다.",
  "message.text.all.files.are.up.to.date": "모든 파일이 최신 상태입니다.",
  "progress.text.synchronizing.files": "파일 동기화 중…",
  "progress.text.updating.done": "업데이트 완료",
  "progress.text.updating.canceled": "업데이트 취소됨",
  "message.title.vcs.update.errors": "{0} 오류",
  "update.tree.node.size.statistics": "{0,choice, 0#항목 없음|1#1개 항목|2#{0, number}개 항목}",
  "toolwindow.title.update.project": "프로젝트 업데이트({0})",
  "action.name.group.by.packages": "패키지별로 그룹화",
  "message.text.cannot.save.settings": "작업을 수행할 수 없습니다: {0}",
  "action.name.check.status": "상태 확인(&K)",
  "action.name.check.scope.status": "{0} 상태 확인(&K)",
  "action.display.name.check.scope.status": "{0} 상태 확인",
  "action.name.update": "업데이트(&U)",
  "action.display.name.update": "업데이트",
  "action.name.update.scope": "{0} 업데이트(&U)",
  "action.display.name.update.scope": "{0} 업데이트",
  "action.name.integrate": "통합(&G)"
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
