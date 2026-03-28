import json

translations = {
  "action.LoadContextAction.Anonymous.text.load": "로드",
  "action.LoadContextAction.Anonymous.text.remove": "제거",
  "action.context.clear.text": "컨텍스트 지우기(_C)",
  "action.context.load.text": "컨텍스트 로드(_L)…",
  "action.context.save.text": "컨텍스트 저장(_S)…",
  "action.deadlock.with.certificate.dialog.text": "인증서 대화상자로 IDE 교착 상태(_D)",
  "action.show.certificate.text": "인증서 대화상자 표시(_S)",
  "action.tasks.analyze.stacktrace.text": "작업의 스택 트레이스 분석(_S)…",
  "action.tasks.close.text": "활성 작업 닫기(_C)…",
  "action.tasks.configure.servers.text": "서버 구성…",
  "action.tasks.create.changelist.text": "변경 목록 생성(_L)…",
  "action.tasks.edit.text": "작업 편집…",
  "action.tasks.open.in.browser.text": "브라우저에서 열기(_B)",
  "action.tasks.show.task.description.text": "설명 표시",
  "action.tasks.switch.text": "작업 전환(_S)…",
  "checkbox.restore.workspace.on.branch.switching": "분기 전환 시 작업 공간 복원(&B)",
  "checkbox.show.notification.with.ability.to.restore.previous.workspace": "이전 작업 공간을 복구할 수 있는 알림 표시(&N)",
  "workspace.associated.with.branch.has.been.restored": "''{0}'' 분기와 연결된 작업 공간이 복원되었습니다.",
  "branch.workspace.settings": "분기 작업 공간 설정",
  "switch.changelist.track.context.checkbox": "컨텍스트 추적(&T)",
  "switch.changelist.track.context.checkbox.tooltip": "변경 목록이 활성화될 때 컨텍스트(예: 열린 에디터)를 다시 로드합니다.",
  "progress.title.updating": "{0} 업데이트 중",
  "dialog.message.connection.successful": "연결에 성공했습니다.",
  "dialog.title.connection": "연결",
  "dialog.title.error": "오류",
  "progress.text.connecting.to": "{0}에 연결 중…",
  "task.save.context.action.name": "컨텍스트 저장",
  "task.save.context.action.message": "코멘트 입력(선택 사항):",
  "task.clear.context.action.name": "컨텍스트 지우기",
  "configure.servers.action.menu.text": "서버 구성…",
  "group.tasks.and.contexts.text": "작업 및 컨텍스트(&T)",
  "group.tasks.internal.text": "작업(&T)",
  "group.tasks.toolbar.text": "작업 도구 모음",
  "open.task.action.menu.text": "작업 열기…",
  "dialog.title.choose.stacktrace.to.analyze": "분석할 스택 트레이스 선택",  
  "label.description": "설명",
  "label.commented.by": "{0}({1})이(가) 코멘트를 남겼습니다.",
  "dialog.title.close.task": "작업 닫기",
  "close.task": "닫을 작업:",
  "task.description": "작업 설명",
  "update.issue.state": "이슈 상태 업데이트(&U)",
  "label.summary": "요약(&S)",
  "associated.branch": "연결된 분기(&B)",
  "associated.change.list": "연결된 변경 목록(&L)",
  "vcs.operations": "VCS 작업",
  "commit.changes": "변경 사항 커밋(&C)",
  "merge.branche.s": "분기 병합(&M)",
  "create.change.list": "변경 목록 생성(&L)",
  "s.helve.current.changes": "현재 변경 사항 선반에 넣기(&H)",
  "create.branch": "분기 생성(&B)"
}

with open("missing_translations/missing_keys_korean.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for file_info in data.get("new_files", []):
    if file_info.get("filename") == "TaskBundle.properties":
        keys_dict = file_info.get("keys", file_info.get("properties", {}))
        keys_dict.update(translations)
        file_info["keys"] = keys_dict
        break

with open("missing_translations/missing_keys_korean.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)
