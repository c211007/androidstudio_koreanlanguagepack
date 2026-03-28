import json

translations = {
  "failure.login": "로그인에 실패했습니다. 자격 증명을 확인하세요.",
  "failure.permissions": "요청에 실패했습니다. 권한을 확인하세요.",
  "failure.server.message": "요청에 실패했습니다. 이유: {0}",
  "failure.http.error": "HTTP 오류로 인해 요청이 실패했습니다. {0,number} {1}.",      
  "failure.configuration": "구성되지 않았습니다.",
  "jira.default.query": "assignee = currentUser() and resolution = Unresolved order by updated",
  "jira.failure.no.REST": "4.2.0 이전 버전의 JIRA에는 REST API가 없으며 더 이상 지원되지 않습니다.",
  "jira.failure.no.state.update": "4.2 이전 버전의 JIRA에서는 작업 상태를 업데이트할 수 없습니다.",
  "jira.failure.no.time.spent": "5.0 이전 버전의 JIRA에서는 소요 시간을 업데이트할 수 없습니다.",
  "jira.failure.captcha": "로그인에 실패했습니다. 웹 인터페이스에 보안 문자를 입력하세요.",      
  "jira.failure.email.address": "로그인에 실패했습니다. 이메일 주소를 확인하세요.",      
  "bugzilla.failure.malformed.response": "서버 응답을 디코딩할 수 없습니다. XML-RPC 플러그인이 활성화되어 있는지 확인하세요.",
  "bugzilla.failure.no.version": "Bugzilla 버전을 찾을 수 없습니다. URL이 \"xmlrpc.cgi\"로 끝나는지 확인하세요.",
  "trello.failure.write.access.required": "이 작업에는 계정에 대한 쓰기 권한이 필요합니다. 설정에서 권한 부여 토큰을 업데이트하세요.",
  "configurable.TaskConfigurable.display.name": "작업",
  "configurable.TaskRepositoriesConfigurable.display.name": "서버",
  "settings.changelist.name.format": "변경 목록 이름 형식(&C):",
  "settings.feature.branch.name.format": "기능 분기 이름 형식(&F):",        
  "settings.lowercased": "소문자(&W)",
  "settings.replace.spaces.with": "공백을 다음으로 바꾸기(&R)",
  "settings.task.history.length": "작업 기록 길이(&L):",
  "settings.connection.timeout": "연결 시간 초과(&T):",
  "settings.milliseconds": "밀리초",
  "settings.always.display.task.combo.in.toolbar": "활성 작업이 없으면 작업 위젯 표시(&W)",
  "settings.save.context.on.commit": "커밋 시 컨텍스트 저장(&S)",
  "settings.issue.cache": "이슈 캐시",
  "settings.enable.cache": "캐시 활성화(&E)",
  "settings.Update": "업데이트(&U)",
  "settings.issues.every": "이슈 가져오기 간격(&V):",
  "settings.minutes": "분",
  "settings.change.list.name.format.should.not.be.empty": "변경 목록 이름 형식은 비워둘 수 없습니다.",
  "settings.Branch.name.format.should.not.be.empty": "분기 이름 형식은 비워둘 수 없습니다.",
  "settings.add.placeholder": "자리 표시자 추가",
  "settings.placeholders": "자리 표시자",
  "settings.configured.servers": "구성된 서버(&C):",
  "settings.no.server.selected": "선택된 서버 없음",
  "settings.no.servers": "서버 없음",
  "settings.new.server": "새 {0} 서버",
  "settings.enable.time.tracking": "시간 추적 활성화(&E)",
  "settings.time.tracking.settings": "시간 추적 설정",
  "settings.suspend.delay": "일시 중지 지연:",
  "settings.seconds": "초",
  "checkbox.include.issues.not.assigned.to.me": "나에게 할당되지 않은 이슈 포함",
  "checkbox.include.cards.not.assigned.to.me": "나에게 할당되지 않은 카드 포함",
  "action.Anonymous.text.configure.tree.dots": "구성…",
  "action.Anonymous.text.rollback": "롤백",
  "action.BranchContextTracker.Anonymous.description": "작업 공간은 열려 있는 파일, 현재 실행 구성 및 중단점의 집합입니다.",
  "action.BranchContextTracker.Anonymous.text.what.is.a.workspace": "작업 공간이란 무엇인가요?",
  "action.DumbAware.TasksToolWindowPanel.description.remove.selected.task": "선택한 작업 제거",
  "action.DumbAware.TasksToolWindowPanel.text.remove.task": "작업 제거"       
}

with open("missing_translations/missing_keys_korean.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for file_info in data.get("new_files", []):
    if file_info.get("filename") == "TaskBundle.properties":
        keys_dict = file_info.get("keys", file_info.get("properties", {}))
        keys_dict.update(translations)
        file_info["keys"] = keys_dict
        break
else:
    data.setdefault("new_files", []).append({
        "filename": "TaskBundle.properties",
        "keys": translations
    })

with open("missing_translations/missing_keys_korean.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)
