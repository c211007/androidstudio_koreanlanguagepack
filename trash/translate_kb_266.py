import json

translations = {
  "create.new.task.0": "새 작업 ''{0}'' 생성",
  "command.name.load.context": "컨텍스트 {0} 로드",
  "progress.title.downloading.mantis.projects": "Mantis 프로젝트 다운로드 중…",
  "progress.title.downloading.redmine.projects": "Redmine 프로젝트 다운로드 중…",
  "progress.title.fetching.available.task.states": "사용 가능한 작업 상태 가져오는 중…",
  "progress.title.downloading.trello.boards": "Trello 보드 다운로드 중…",
  "progress.title.downloading.trello.lists": "Trello 목록 다운로드 중…", 
  "html.a.href.0.where.can.i.get.authorization.token.a.html": "<html><a href={0}>인증 토큰은 어디에서 받을 수 있나요?</a></html>",
  "more.features.available.in.youtrack.plugin": "<html><a href=\"https://plugins.jetbrains.com/plugin/8215-youtrack-integration\">YouTrack 플러그인</a>에서 더 많은 기능을 사용할 수 있습니다.<html>",
  "separator.recently.closed.tasks": "최근 닫힌 작업",
  "java.debugger.breakpoints": "Java 디버거 중단점",
  "popup.advertisement.html.press.shift.to.merge.with.current.context.br.pressing.would.show.task.description.comments.html": "<html>현재 컨텍스트와 병합하려면 Shift 키를 누르세요.<br/>{0}을(를) 누르면 작업 설명과 코멘트가 표시됩니다.</html>",
  "enter.task.name": "작업 이름 입력:",
  "label.include.closed.tasks": "닫힌 작업 포함",
  "name": "이름(&N):",
  "update.issue.state1": "이슈 상태 업데이트(&U)",
  "clear.current.context": "현재 컨텍스트 지우기(&C)",
  "login.url": "로그인 URL(&G):",
  "tasks.list.url": "작업 목록 URL(&L):",
  "single.task.url": "단일 작업 URL(&S):",
  "response.type": "응답 유형:",
  "text": "텍스트(&T)",
  "each.task.in.separate.request": "별도 요청의 각 작업:",
  "reset.to.defaults": "기본값으로 재설정(&R)",
  "manage.template.variables": "템플릿 변수 관리(&A)…",
  "test": "테스트(&S)",
  "notification.title.more.time.tracking.features": "더 많은 시간 추적 기능",
  "notification.content.time.tracking.in.youtrack.plugin": "<html><a href=\"https://plugins.jetbrains.com/plugin/8215-youtrack-integration\">YouTrack 플러그인</a>은 시간 추적을 보다 세밀하게 관리할 수 있는 기능을 제공합니다. 사용해 보세요!<html>",  
  "notification.content.do.not.show.again": "다시 표시 안 함",
  "notification.group.branch.context": "분기 컨텍스트가 전환됨",
  "notification.group.tasks": "작업 서버 연결 실패",
  "notification.group.context.corrupted": "작업 컨텍스트 데이터 손상됨",        
  "task.list.url.configuration.parameter.is.mandatory": "'작업 목록 URL' 구성 매개변수는 필수입니다.",
  "do.not.associate.branch": "분기 연결 안 함(&N)",
  "tasks.widget.accessible.name.prefix": "작업",
  "progress.title.saving.task.context": "작업 컨텍스트 저장 중…"
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
