import json

translations = {
  "action.Terminal.SendShortcut.text": "터미널로 단축키 전송",
  "action.Terminal.SendShortcut.detailed.text": "터미널로 {0} 전송",
  "action.Terminal.NewTab.text": "새 탭",
  "action.Terminal.NewTab.description": "새 탭에서 새 세션 생성",        
  "action.Terminal.CloseTab.text": "탭 닫기",
  "action.Terminal.SwitchFocusToEditor.text": "에디터로 포커스 전환",
  "action.Terminal.MoveToolWindowTabRight.text": "오른쪽으로 탭 이동",
  "action.Terminal.MoveToolWindowTabLeft.text": "왼쪽으로 탭 이동",
  "action.Terminal.MoveToEditor.text": "에디터로 이동",
  "action.Terminal.RenameSession.text": "세션 이름 바꾸기",
  "action.Terminal.OpenInTerminal.text": "터미널에서 열기",
  "action.Terminal.OpenInTerminal.RevealInPopup.text": "터미널",
  "action.Terminal.OpenInReworkedTerminal.text": "터미널에서 열기",
  "action.Terminal.OpenInReworkedTerminal.RevealInPopup.text": "터미널",      
  "action.Terminal.OpenInTerminal.description": "터미널에서 현재 파일 위치를 엽니다.",
  "action.Terminal.CopySelectedText.text": "복사",
  "action.Terminal.CopySelectedText.description": "선택한 텍스트를 클립보드에 복사",
  "action.Terminal.Paste.text": "붙여넣기",
  "action.Terminal.Paste.description": "클립보드에서 붙여넣기",
  "action.Terminal.PasteSelection.text": "선택 영역 클립보드에서 붙여넣기",      
  "action.Terminal.PasteSelection.GoToAction.text": "선택 영역 클립보드에서 붙여넣기(터미널)",
  "action.Terminal.PasteSelection.description": "사용 가능한 경우 선택 영역 클립보드에서 붙여넣거나, 일반 클립보드에서 붙여넣습니다.",
  "action.Terminal.SelectAll.text": "모두 선택",
  "action.Terminal.SelectAll.GoToAction.text": "모두 선택(터미널)",
  "action.Terminal.SelectAll.description": "모두 선택",
  "action.Terminal.SmartCommandExecution.Run.text": "IDE를 사용하여 강조 표시된 명령 실행",
  "action.Terminal.SmartCommandExecution.Run.description": "관련 IDE 기능을 사용하여 강조 표시된 작업을 실행합니다.",
  "action.Terminal.SmartCommandExecution.Debug.text": "IDE를 사용하여 강조 표시된 명령 디버그",
  "action.Terminal.SmartCommandExecution.Debug.description": "디버거 아래에서 관련 IDE 기능을 사용하여 강조 표시된 작업을 수행합니다.",
  "action.RenameSession.newSessionName.label": "세션 이름:",
  "action.TerminalNewPredefinedSession.text": "새로운 사전 정의된 세션",
  "action.Terminal.Find.text": "찾기",
  "action.Terminal.Find.GoToAction.text": "찾기(터미널)",
  "action.Terminal.ClearBuffer.text": "터미널 지우기",
  "action.Terminal.CommandCompletion.text": "명령어 완성",
  "action.Terminal.CommandCompletion.Invoke.text": "명령어 완성 호출",   
  "action.Terminal.CommandCompletion.Invoke.GoToAction.text": "명령어 완성 호출(터미널)",
  "action.Terminal.CommandCompletion.InsertSuggestion.text": "명령어 완성 제안 삽입",
  "action.Terminal.CommandCompletion.InsertSuggestion.GoToAction.text": "명령어 완성 제안 삽입(터미널)",
  "action.Terminal.CommandCompletion.SelectSuggestionAbove.text": "위의 제안 선택",
  "action.Terminal.CommandCompletion.SelectSuggestionAbove.GoToAction.text": "위의 제안 선택(터미널)",
  "action.Terminal.CommandCompletion.SelectSuggestionBelow.text": "아래 제안 선택",
  "action.Terminal.CommandCompletion.SelectSuggestionBelow.GoToAction.text": "아래 제안 선택(터미널)",
  "action.Terminal.InsertInlineCompletion.text": "인라인 제안 삽입",      
  "action.Terminal.InsertInlineCompletion.GoToAction.text": "인라인 제안 삽입(터미널)",
  "action.Terminal.ShowDocumentation.text": "문서 표시",
  "action.Terminal.Escape.text": "이스케이프(Escape)",
  "action.Terminal.CloseSession.text": "세션 닫기",
  "action.Terminal.CloseSession.description": "프롬프트가 비어 있는 경우 세션 닫기",
  "action.Terminal.ClearPrompt.text": "명령 프롬프트 지우기"
}

with open("missing_translations/missing_keys_korean.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for file_info in data.get("new_files", []):
    if file_info.get("filename") == "TerminalBundle.properties":
        keys_dict = file_info.get("keys", file_info.get("properties", {}))
        keys_dict.update(translations)
        file_info["keys"] = keys_dict
        break
else:
    data.setdefault("new_files", []).append({
        "filename": "TerminalBundle.properties",
        "keys": translations
    })

with open("missing_translations/missing_keys_korean.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)
