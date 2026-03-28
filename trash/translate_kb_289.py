import json

translations = {
  "message.text.commit.progress": "커밋 중…",
  "message.text.commit.failed.with.error": "{0,choice,1#오류|2#오류}로 인해 커밋에 실패했습니다.",
  "message.text.commit.finished.with.warning": "{0,choice,1#경고|2#경고}와 함께 커밋이 완료되었습니다.",
  "message.text.background.tasks": "백그라운드 VCS 작업이 완료될 때까지 기다리는 중…",
  "diff.title.local": "로컬",
  "diff.title.local.with.number": "로컬({0})",
  "message.title.annotate": "어노테이션 추가",
  "action.name.checkin.directory": "{0} {1,choice,1#디렉터리|2#디렉터리}",
  "action.name.checkin.file": "{0} {1,choice,1#파일|2#파일}",
  "action.for.file.with.dialog.text": "{0} {1,choice,1#파일|2#파일}…",
  "column.name.revision.list.author": "작성자",
  "column.name.revisions.list.filter": "날짜",
  "column.name.revisions.list.branch": "브랜치",
  "column.name.revision.list.revision": "리비전",
  "lookup.title.vcs.file.revisions": "파일 리비전",
  "border.selected.revision.commit.message": "커밋 메시지",
  "loading.file.history.progress": "파일 이력 로드 중",
  "loading.text2.file.history.progress": "파일 이력을 로드하는 중",
  "loading.file.history.status": "{0}의 이력 로드 중…",
  "loading.file.history.up.to.revision.status": "{1}까지의 {0} 이력 로드 중…",
  "message.title.could.not.load.file.history": "파일 이력을 로드하는 중 문제 발생",
  "group.name.version.control": "VCS(&V)",
  "message.text.cannot.open.editor": "{0} 파일에 대한 텍스트 편집기를 열 수 없습니다.",
  "message.title.cannot.open.editor": "편집기를 열 수 없음",
  "configuration.project.not.trusted.label": "안전 모드, 버전 관리를 사용할 수 없습니다. 전체 IDE 기능에 액세스하려면 프로젝트를 신뢰하세요.",
  "column.info.configure.vcses.directory": "디렉터리",
  "column.name.configure.vcses.vcs": "VCS",
  "settings.general.show.options.before.command.label": "다음 이전 옵션 표시:",
  "checkbox.show.clear.read.only.status.dialog": "읽기 전용으로 설정된 파일을 편집하려고 시도할 때 파일 잠금을 해제할지 묻기",
  "show.patch.in.explorer.after.creation.label": "패치가 생성되었을 때:",
  "show.patch.in.explorer.after.creation.combobox.text.ask": "묻기",
  "show.patch.in.explorer.after.creation.combobox.text.show.in.file.manager": "{0}에서 표시",
  "show.patch.in.explorer.after.creation.combobox.text.no": "아무 작업도 하지 않음",
  "radio.after.deletion.do.not.remove": "제거하지 않음",
  "radio.after.deletion.show.options": "묻기",
  "radio.after.deletion.remove.silently": "조용히 제거",
  "radio.after.creation.do.not.add": "추가하지 않음",
  "radio.after.creation.add.silently": "조용히 추가",
  "radio.after.creation.show.options": "묻기",
  "checkbox.clear.initial.commit.message": "최초 커밋 메시지 지우기(&I)",
  "description.text.option.applicable.to.vcses": "{0}에 적용 가능",
  "version.control.main.configurable.name": "버전 관리",
  "version.control.main.configurable.description": "<html><body>\n  프로젝트에서 사용되는 버전 관리 관련 설정을 구성합니다.",
  "action.name.show.difference": "차이점 표시",
  "settings.filter.update.project.info.by.scope": "범위별로 프로젝트 업데이트 정보 필터링",
  "settings.changelists.create.automatically.checkbox": "변경 목록 자동 생성(&A)",
  "settings.partial.changelists.enable.checkbox": "하나의 파일 내에 있는 변경 사항을 다른 변경 목록에 넣도록 허용(&P)",
  "settings.show.conflict.resolve.dialog.checkbox": "비활성 변경 목록의 파일을 편집하려고 시도할 때 대화상자 표시(&D)",
  "settings.highlight.files.with.conflicts.checkbox": "변경 목록 충돌이 있는 파일 강조 표시(&H)",
  "settings.highlight.files.from.non.active.changelist.checkbox": "비활성 변경 목록의 파일 강조 표시(&I)"
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
