import json

translations = {
  "parsing.error.expecting.by": "'by'가 필요합니다.",
  "label.project.id": "프로젝트 ID:",
  "popup.title.load.context": "컨텍스트 로드",
  "popup.advertisement.press.shift.to.merge.with.current.context": "현재 컨텍스트와 병합하려면 Shift 키를 누르세요.",
  "popup.title.merge.with.current.context": "현재 컨텍스트와 병합",       
  "dialog.title.template.variables": "템플릿 변수",
  "status.text.no.variables": "변수 없음",
  "column.name.value": "값",
  "column.name.show.on.first.tab": "첫 번째 탭에 표시",
  "tooltip.whether.this.template.variable.will.be.shown.in.general.tab": "이 템플릿 변수를 '일반 탭'에 표시할지 여부",
  "column.name.hide": "숨기기",
  "tooltip.whether.this.template.variable.will.be.hidden.like.password.field": "이 템플릿 변수를 비밀번호 필드처럼 숨길지 여부",
  "label.login.first": "먼저 로그인하세요.",
  "login": "로그인",
  "label.filter": "필터:",
  "dialog.title.open.task": "작업 열기",
  "dialog.message.task.name.should.not.be.empty": "작업 이름은 비워둘 수 없습니다.",
  "action.open.in.browser.text": "브라우저에서 ''{0}'' 열기(_B)",
  "label.set.url.password.token.first": "먼저 URL 및 비밀번호/토큰을 설정하세요.",     
  "label.html.task.pattern.should.be.regexp.with.two.matching.groups.id.summary": "<html>작업 패턴은 일치하는 두 그룹({id}.+?) 및 ({summary}.+?)이 있는 정규 표현식이어야 합니다.",
  "label.task.pattern": "작업 패턴:",
  "action.show.description.text": "''{0}'' 설명 표시(_D)",
  "popup.title.switch.to.task": "작업으로 전환",
  "action.switch.to.text": "전환(&S)",
  "action.edit.text.with.mnemonic": "편집(&E)",
  "action.remove.text": "제거(&R)",
  "dialog.message.default.task.cannot.be.removed": "기본 작업은 제거할 수 없습니다.",
  "dialog.title.cannot.remove": "제거할 수 없음",
  "dialog.message.changelist.associated.with.not.empty": "''{0}''와(과) 연결된 변경 목록이 비어 있지 않습니다.\\n제거하고 변경 사항을 활성 변경 목록으로 이동하시겠습니까?",
  "dialog.title.changelist.not.empty": "비어 있지 않은 변경 목록",
  "popup.title.add.server": "서버 추가",
  "notification.content.p.href.configure.server.p": "<p><a href=\"\">서버 구성...</a></p>",
  "notification.title.cannot.connect.to": "{0}에 연결할 수 없습니다.",
  "pressing.up.or.down.arrows.while.in.editor.changes.the.state": "에디터에서 위쪽 또는 아래쪽 화살표를 누르면 상태가 변경됩니다.",
  "label.set.token.first": "먼저 토큰을 설정하세요.",
  "label.closed": "\\ (닫힘)",
  "label.select.board.first": "먼저 보드를 선택하세요.",
  "label.archived.moved": "\\ (보관됨,이동됨)",
  "label.moved": "\\ (이동됨)",
  "label.archived": "\\ (보관됨)",
  "label.board": "보드:",
  "label.list": "목록:",
  "dialog.message.can.t.create.branch.if.no.commit.exists.create.commit.first": "커밋이 없으면 분기를 만들 수 없습니다.\\n먼저 커밋을 만드세요.",
  "dialog.title.cannot.create.branch": "분기를 만들 수 없음",
  "dialog.message.branch.name.should.not.be.empty": "분기 이름은 비워둘 수 없습니다.",
  "dialog.message.branch.name.not.valid.check.your.vcs.branch.name.restrictions": "분기 이름이 유효하지 않습니다. vcs 분기 이름 제한 사항을 확인하세요.",
  "dialog.message.branch.name.should.not.contain.spaces": "분기 이름에는 공백을 포함할 수 없습니다.",
  "dialog.message.changelist.name.should.not.be.empty": "변경 목록 이름은 비워둘 수 없습니다.",
  "filetype.youtrack.query.description": "YouTrack 쿼리",
  "progress.title.downloading.gitlab.projects": "Gitlab 프로젝트 다운로드 중…"
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
