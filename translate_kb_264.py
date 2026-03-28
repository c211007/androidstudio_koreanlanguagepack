import json

translations = {
  "from": "시작(&F)",
  "u.se.branch": "분기 사용(&S)",
  "bookmarks": "북마크",
  "open.editors.and.positions": "열린 에디터 및 위치",
  "project.view.state": "프로젝트 뷰 상태",
  "run.configurations": "실행 구성",
  "dialog.message.unknown.error": "알 수 없는 오류",
  "dialog.message.unknown.host": "알 수 없는 호스트: {0}",
  "default.task": "기본 작업",
  "dialog.title.test.connection": "연결 테스트",
  "notification.title.context.data.corrupted": "컨텍스트 데이터가 손상됨",        
  "notification.content.context.information.history": "{0}에 대한 컨텍스트 정보 기록이 손상되었습니다.\\n기록이 지워졌습니다.",
  "xdebugger.breakpoints": "XDebugger 중단점",
  "debugger.watches": "디버거 조사식",
  "bugzilla.label.product": "제품:",
  "bugzilla.label.component": "구성요소:",
  "dialog.title.cannot.set.state.for.issue": "이슈에 대한 상태를 설정할 수 없음",      
  "action.create.changelist.for.text": "''{0}''에 대한 변경 목록 생성",        
  "action.add.changelist.for.text": "''{0}''에 대한 변경 목록 추가",
  "dialog.message.changelist.name": "변경 목록 이름:",
  "dialog.title.create.changelist": "변경 목록 생성",
  "dialog.message.this.dialog.may.not.be.shown": "이 대화상자는 MediaTracker 및 CertificateManager로 인한 교착 상태 때문에 표시되지 않을 수 있습니다. 다행히 교착 상태는 발생하지 않았습니다.",
  "dialog.title.deadlocking.dialog": "교착 상태를 일으키는 대화상자",
  "action.edit.text": "''{0}'' 편집",
  "dialog.title.edit.task.choice": "{1, choice, 0#{0}|1#} 작업 편집",
  "server.configuration": "서버 구성",
  "label.search": "검색:",
  "label.token": "토큰:",
  "label.project": "프로젝트:",
  "label.set.server.url.token.first": "먼저 서버 URL과 토큰을 설정하세요.",
  "column.name.name": "이름",
  "column.name.path": "경로",
  "label.jql.search.cannot.be.used.in.jira.versions.prior.your.version": "4.2 이전 버전의 JIRA에서는 JQL 검색을 사용할 수 없습니다. 현재 버전: {0}",
  "label.email": "이메일:",
  "label.api.token": "API 토큰:",
  "label.username": "사용자 이름:",
  "label.password": "비밀번호:",
  "inspection.message.not.expecting.s.here": "여기에 '%s'가 올 수 없습니다.",
  "inspection.message.not.expecting.list.values.here": "여기에 값 목록이 올 수 없습니다.",
  "inspection.message.expecting.list.values.here": "여기에 값 목록이 와야 합니다.",
  "inspection.message.expecting.empty.or.null.here": "여기에 'empty' 또는 'null'이 와야 합니다.",
  "filetype.jira.query.description": "JIRA 쿼리",
  "parsing.error.illegal.query.part": "잘못된 쿼리 부분",
  "parsing.error.expecting.clause": "절(clause)이 필요합니다.",
  "parsing.error.expecting": "')'가 필요합니다.",
  "parsing.error.expecting.in": "'in'이 필요합니다.",
  "parsing.error.expecting.operator": "연산자가 필요합니다.",
  "parsing.error.expecting.either.literal.list.or.function.call": "리터럴, 목록 또는 함수 호출 중 하나가 필요합니다.",
  "parsing.error.expecting.field.name": "필드 이름이 필요합니다.",
  "parsing.error.expecting.argument": "인수가 필요합니다."
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
