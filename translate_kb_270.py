import json

translations = {
  "advanced.setting.new.terminal.output.capacity.kb": "새로운 터미널 출력 용량",
  "advanced.setting.new.terminal.output.capacity.kb.trailingLabel": "KB",       
  "search.in.block": "블록에서 검색(&E)",
  "new.terminal.promotion.text": "이 메뉴를 사용하여 명령어 완성, 개선된 이력, 그리고 각 명령어 출력에 대한 시각적 블록 기능이 제공되는 새 터미널(New Terminal)의 베타 버전을 활성화할 수 있습니다.",
  "new.terminal.promotion.text.header": "새 터미널 사용해 보기",
  "exit.code.label": "종료 코드 {0}",
  "terminal.prompt.lang.description": "터미널 프롬프트(내부)",
  "doc.popup.alias.text": "\"{0}\"의 별칭",
  "terminal.output.editor.title": "터미널 출력",
  "feedback.notification.title": "터미널에 대한 피드백 공유",
  "feedback.notification.text": "터미널 사용 경험에 대한 몇 가지 질문에 답해 주세요.",
  "feedback.dialog.title": "터미널 피드백",
  "feedback.dialog.header": "터미널을 사용해 주셔서 감사합니다!",
  "feedback.dialog.description": "여러분의 소중한 피드백은 터미널의 미래를 형성하며, 호환성, 성능, 사용성에 대한 사용자의 요구를 충족하는 데 큰 도움이 됩니다.",   
  "feedback.dialog.rating.title": "전반적으로 터미널에 얼마나 만족하시나요? (1 = 매우 불만족, 5 = 매우 만족)",
  "feedback.dialog.issues": "예상대로 작동하지 않는 기능이 있다면, 어떤 문제가 있는지 알려주세요.",
  "feedback.dialog.improvement": "터미널에서 개선해야 할 가장 중요한 부분은 무엇이라고 생각하시나요?",
  "feedback.dialog.improvement.compatibility": "앱 호환성(Vim, tmux 등)",
  "feedback.dialog.improvement.performance": "속도/지연 시간",
  "feedback.dialog.improvement.shell.support": "쉘 지원(Bash, Zsh, PowerShell 등)",
  "feedback.dialog.improvement.ai.integration": "AI 통합",
  "feedback.dialog.improvement.ide.integration": "IDE 통합, 퀘이크/전체 화면 모드",
  "feedback.dialog.other": "터미널에 대해 더 나눌 의견이 있으신가요?",        
  "feedback.dialog.other.placeholder": "예: 버그, 누락된 기능 또는 제안 사항",
  "feedback.system.info.shell": "선택한 쉘:",
  "feedback.system.info.commands.number": "실행한 명령어 수:",       
  "feedback.system.info.moment": "피드백 작성 시점:",
  "completion.feedback.notification.text": "터미널 명령어 완성 사용 경험에 대한 몇 가지 질문에 답해 주세요.",
  "completion.feedback.dialog.header": "터미널 피드백",
  "completion.feedback.dialog.description": "터미널 명령어 완성 기능을 한동안 사용해 보셨습니다. 이 기능에 대한 의견을 공유해 주시면 감사하겠습니다.",
  "completion.feedback.dialog.rating": "터미널 명령어 완성 기능에 얼마나 만족하시나요? (1 = 매우 불만족, 5 = 매우 만족)",
  "completion.feedback.dialog.experience.label": "터미널 명령어 완성 기능에 대한 경험을 자세히 들려주세요.",
  "completion.feedback.dialog.experience.placeholder": "예: 제안의 관련성, 전반적인 사용성, 단축키 등",
  "psreadline.update.line.1": "{0} PSReadLine 모듈 버전({1})이 최신 버전이 아니어서 \n 터미널 화면에 검은 줄이 생기는 문제가 발생할 수 있습니다.",
  "psreadline.update.line.2": "다음 명령을 실행하여 최신 버전을 설치하세요. {0}",     
  "psreadline.update.line.3": "설치 후 새 터미널 탭을 여세요.",
  "cd.command.description": "쉘 작업 디렉터리를 변경합니다.",
  "cd.command.arg.displayName": "경로",
  "cd.command.arg.dash.description": "마지막으로 사용한 폴더로 전환",
  "cd.command.arg.tilda.description": "홈 디렉터리로 전환",
  "make.command.description": "Makefile 대상을 실행합니다.",
  "make.command.arg.displayName": "대상(target)"
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
