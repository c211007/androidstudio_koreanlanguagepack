import json

translations = {
  "action.Terminal.CopyBlock.text": "블록 복사",
  "action.Terminal.InterruptCommand.text": "명령어 중단",
  "action.Terminal.SelectLastBlock.text": "마지막 블록 선택",
  "action.Terminal.SelectPrompt.text": "프롬프트 선택",
  "action.Terminal.SelectBlockAbove.text": "위 블록 선택",
  "action.Terminal.SelectBlockBelow.text": "아래 블록 선택",
  "action.Terminal.ExpandBlockSelectionAbove.text": "블록 선택 위로 확장",
  "action.Terminal.ExpandBlockSelectionBelow.text": "블록 선택 아래로 확장",
  "action.Terminal.MoveCaretToLineStart.text": "캐럿을 줄 시작으로 이동",      
  "action.Terminal.MoveCaretToLineEnd.text": "캐럿을 줄 끝으로 이동",
  "action.Terminal.DeletePreviousWord.text": "이전 단어 삭제",
  "action.Terminal.SearchInCommandHistory.text": "명령어 이력에서 검색",   
  "action.Terminal.LineUp.text": "위로 줄 이동",
  "action.Terminal.LineUp.GoToAction.text": "위로 줄 이동(터미널)",
  "action.Terminal.LineDown.text": "아래로 줄 이동",
  "action.Terminal.LineDown.GoToAction.text": "아래로 줄 이동(터미널)",
  "action.Terminal.PageUp.text": "위로 페이지 이동",
  "action.Terminal.PageUp.GoToAction.text": "위로 페이지 이동(터미널)",
  "action.Terminal.PageDown.text": "아래로 페이지 이동",
  "action.Terminal.PageDown.GoToAction.text": "아래로 페이지 이동(터미널)",
  "action.Terminal.ShowFeedbackNotification.text": "개선된 터미널 피드백 알림 표시",
  "action.Terminal.Completion.ShowFeedbackNotification.text": "터미널 명령어 완성 피드백 알림 표시",
  "action.Terminal.Feedback.text": "피드백 공유",
  "action.Terminal.Feedback.GoToAction.text": "터미널에 대한 피드백 공유",
  "group.Terminal.PromptStyle.text": "프롬프트 스타일",
  "action.Terminal.UseSingleLinePrompt.text": "IDE 한 줄 프롬프트",
  "action.Terminal.UseDoubleLinePrompt.text": "IDE 두 줄 프롬프트",
  "action.Terminal.UseShellPrompt.text": "쉘 프롬프트(PS1)",
  "group.Terminal.Engine.text": "터미널 엔진",
  "action.Terminal.Settings.text": "설정",
  "action.Terminal.CommandCompletionSettings.text": "명령어 완성 설정",
  "local.terminal.default.name": "로컬",
  "remote.terminal.default.name": "원격",
  "settings.enable.new.ui": "새 터미널 활성화",
  "settings.enforce.minimum.contrast.ratio": "최소 명암비 강제 적용:", 
  "settings.enforce.minimum.contrast.ratio.description": "활성화되면 지정된 명암비를 충족하도록 텍스트 전경색을 조정합니다. \n 사용 가능한 값은 [1; 21]이며 여기서 1은 명암 대비 조정 없음을, 21은 흑백 모드를 의미합니다. \n 기본값은 4.5입니다.",
  "settings.show.separators.between.blocks": "실행된 명령어 사이에 구분선 표시",
  "settings.prompt.style": "프롬프트 스타일:",
  "settings.singleLine.prompt": "IDE 한 줄 프롬프트",
  "settings.doubleLine.prompt": "IDE 두 줄 프롬프트",
  "settings.shell.prompt": "쉘 프롬프트(PS1)",
  "settings.shell.prompt.description": "쉘에서 구성된 프롬프트를 사용합니다. 실험적인 기능이므로 \n 일부 프롬프트(특히 PowerLevel10K)가 제대로 표시되지 않을 수 있습니다.",
  "settings.start.directory": "시작 디렉터리(&D):",
  "settings.start.directory.browseFolder.description": "시작 디렉터리",    
  "settings.environment.variables": "환경 변수(&E):",
  "settings.shell.path": "쉘 경로(&S):",
  "settings.shell.path.detecting.default": "기본 쉘 경로를 감지하는 중…",
  "settings.tab.name": "기본 탭 이름(&T):",
  "settings.font.name": "글꼴(&F):",
  "settings.fallback.font.name": "대체(Fallback):"
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
