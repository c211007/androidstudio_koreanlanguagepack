import json

translations = {
  "settings.font.size": "크기:",
  "settings.line.height": "줄 높이:",
  "settings.column.width": "열 너비:",
  "settings.colors": "색상 구성…",
  "settings.audible.bell": "경고음(벨소리)",
  "settings.close.session.when.it.ends": "세션이 끝나면 닫기",
  "settings.mouse.reporting": "마우스 이벤트 보고",
  "settings.copy.to.clipboard.on.selection": "선택 시 클립보드에 복사",  
  "settings.paste.on.middle.mouse.button.click": "가운데 마우스 버튼 클릭 시 붙여넣기",
  "settings.override.ide.shortcuts": "IDE 단축키 재정의",
  "settings.configure.terminal.keybindings": "터미널 키 바인딩 구성",  
  "settings.keymap.plugins.terminal": "키맵 | 플러그인 | 터미널",
  "settings.shell.integration": "쉘 통합",
  "settings.enable.cloud.completion.suggestions": "인라인 AI 자동 완성 제안 활성화",
  "settings.enable.cloud.completion.suggestions.comment": "AI Assistant에서 제공하는 클라우드 자동 완성 모델",
  "settings.highlight.hyperlinks": "하이퍼링크 강조 표시",
  "settings.use.option.as.meta.key.label": "Option을 메타(Meta) 키로 사용",
  "settings.cursor.shape.label": "커서 모양:",
  "settings.terminal.project.settings": "프로젝트 설정",
  "settings.terminal.font.settings": "글꼴 설정",
  "settings.terminal.application.settings": "애플리케이션 설정",
  "settings.terminal.shell.executable.path.browseFolder.description": "쉘 실행 파일 경로",
  "settings.shell.language": "쉘 스크립트",
  "settings.terminal.engine": "터미널 엔진:",
  "terminal.engine.reworked": "개선됨(2025)",
  "terminal.engine.classic": "클래식",
  "terminal.engine.new.terminal": "실험적(2024, 사용 중단됨)",
  "terminal.command.completion": "명령어 완성",
  "terminal.command.completion.show": "입력할 때 완성 팝업 표시:",   
  "terminal.command.completion.show.parameters": "매개변수만",
  "terminal.command.completion.show.always": "항상",
  "terminal.command.completion.show.never": "안 함",
  "terminal.command.completion.shortcut.insert": "제안 삽입 키:",     
  "terminal.command.completion.shortcut.trigger": "완성 팝업 표시 키:",
  "terminal.command.completion.shortcut.change": "변경",
  "terminal.command.completion.shortcut.custom": "사용자 지정…",
  "terminal.command.completion.insertion.shortcut.hint": "{0} 삽입",
  "terminal.command.completion.execution.shortcut.hint": "{0} 실행",
  "terminal.command.completion.popup.promotion": "터미널 명령어 완성",
  "settings.terminal.smart.command.handling": "IDE를 사용하여 명령어 실행",
  "smart_command_execution.notification.title": "IDE를 사용하여 강조 표시된 명령어 실행",
  "smart_command_execution.notification.text": "관련 IDE 기능을 사용하여 명령어를 실행하려면 {0}을(를) 누르세요.<p/>적용 가능한 경우 디버그하려면 {1}을(를) 누르세요.",        
  "smart_command_execution.notification.configure_link.text": "구성…",
  "toolwindow.stripe.Terminal": "터미널",
  "progress.title.running.terminal": "터미널 실행 중",
  "progress.text.running.terminal": "터미널을 실행하는 중…",
  "session.terminated.text": "세션 완료됨",
  "see.ide.log.error.description": "자세한 내용은 IDE 로그(도움말 | {0})를 참조하세요.", 
  "group.advanced.settings.terminal": "터미널",
  "advanced.setting.terminal.character.encoding": "터미널 문자 인코딩" 
}

with open("missing_translations/missing_keys_korean.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for file_info in data.get("new_files", []):
    if file_info.get("filename") == "TerminalBundle.properties":
        keys_dict = file_info.get("keys", file_info.get("properties", {}))
        keys_dict.update(translations)
        file_info["keys"] = keys_dict
        break

with open("missing_translations/missing_keys_korean.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)
