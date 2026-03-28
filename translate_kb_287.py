import json

translations = {
  "none.vcs.presentation": "<없음>",
  "vcs.command.name.add": "추가(Add)",
  "vcs.command.name.remove": "제거",
  "vcs.command.name.checkin": "커밋(&I)",
  "vcs.command.name.edit": "편집",
  "vcs.command.name.checkout": "체크아웃(Checkout)",
  "vcs.command.name.status": "상태(Status)",
  "vcs.command.name.update": "업데이트(Update)",
  "vcs.settings.path": "설정 | 버전 관리",
  "vcs.settings.path.mac": "환경설정 | 버전 관리",
  "history.empty": "이력이 비어 있습니다",
  "history.loading.revisions": "영향을 받는 리비전 로드 중…",
  "exception.text.unknown.error": "알 수 없는 오류",
  "exception.text.internal.error.method.should.not.be.called": "호출하면 안 됩니다.",
  "vcs.revision.name.current": "현재",
  "error.no.changes.to.commit": "커밋할 파일을 선택하세요.",
  "error.no.commit.message": "커밋 메시지를 지정하세요.",
  "error.no.changes.no.commit.message": "커밋할 파일을 선택하고 커밋 메시지를 지정하세요.",
  "label.commit.checks.not.available.during.indexing": "프로젝트 분석 중에는 일부 커밋 검사를 사용할 수 없습니다.",
  "commit.checks.on.commit.progress.text": "커밋 중…",
  "commit.checks.on.commit.progress.text.with.context": "커밋 중: {0}",
  "commit.checks.only.progress.text": "커밋 검사 실행 중…",
  "commit.checks.only.progress.text.with.context": "커밋 검사 실행 중: {0}",
  "commit.checks.failed.notification.title": "{0}개의 검사에 실패했습니다.",
  "commit.checks.failed.notification.commit.anyway.action": "무시하고 {0}",
  "commit.checks.failed.notification.show.details.action": "세부 정보 표시",
  "post.commit.checks.progress.text": "커밋된 파일 검사 중",
  "post.commit.checks.progress.step.collecting.commits.text": "영향을 받는 커밋 수집 중…",
  "post.commit.checks.failed.notification.title": "커밋에 문제가 포함되어 있습니다.",
  "post.commit.checks.failed.push.dialog.notification.text": "커밋에 문제가 포함되어 있음: {0}",
  "post.commit.checks.not.finished.push.dialog.notification.text": "커밋 검사가 아직 진행 중입니다.",
  "post.commit.checks.failed.notification.ignore.action": "무시",
  "label.commit.checks.failed.unknown.reason": "검사에 실패했습니다.",
  "tooltip.rerun.commit.checks": "커밋 검사 다시 실행",
  "action.commit.anyway.text": "무시하고 {0}",
  "error.text.check.in.with.empty.comment": "커밋 메시지 입력란에 변경 사항에 대한 요약을 추가하세요.",
  "error.title.check.in.with.empty.comment": "커밋 메시지 없음",
  "amend.action.name": "{0} 수정(Amend)",
  "action.amend.commit.anyway.text": "무시하고 수정(Amend Anyway)",
  "commit.message.placeholder": "커밋 메시지",
  "commit.message.editor.accessible.name": "커밋 메시지",
  "label.commit.comment": "커밋 메시지(&C)",
  "commit.checks.group": "{0} 검사",
  "commit.checks.group.post": "고급 {0} 검사",
  "border.standard.after.checkin.options.group": "{0} 이후",
  "checkbox.checkin.options.optimize.imports": "import 최적화(&O)",
  "checkbox.checkin.options.reformat.code": "코드 서식 재지정(&R)",
  "checkbox.checkin.options.rearrange.code": "코드 재정렬(&N)",
  "progress.title.commit.checks": "커밋 검사",
  "progress.text.inspecting.code": "코드 검사 중…"
}

with open("missing_translations/missing_keys_korean.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for file_info in data.get("new_files", []):
    if file_info.get("filename") == "VcsBundle.properties":
        keys_dict = file_info.get("keys", file_info.get("properties", {}))
        keys_dict.update(translations)
        file_info["keys"] = keys_dict
        break
else:
    data.setdefault("new_files", []).append({
        "filename": "VcsBundle.properties",
        "keys": translations
    })

with open("missing_translations/missing_keys_korean.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)
