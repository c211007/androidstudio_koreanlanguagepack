import json
from pathlib import Path

def update_missing_keys():
    file_path = Path("missing_translations/missing_keys_korean.json")

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    ko_dict = {
        "group.CIDR.Interactive.Cling.text": "Cling",
        "action.CIDR.Interactive.StartClingSession.text": "새 Cling 세션 시작\\u2026",
        "action.CIDR.Interactive.SendToCling.text": "Cling으로 보내기",
        "action.CIDR.Interactive.SendIncludesToCling.text": "포함된 헤더를 Cling으로 보내기",
        "interactive.action.send.selection.to.cling.text": "선택 영역을 Cling으로 보내기",
        "interactive.action.send.selection.to.cling.sentence": "선택 영역을 Cling으로 보내기",
        "interactive.action.send.current.line.to.cling.text": "현재 줄을 Cling으로 보내기",
        "interactive.action.send.current.line.to.cling.sentence": "현재 줄을 Cling으로 보내기",
        "interactive.path.to.cling.binary": "Cling 실행 파일 경로:",
        "interactive.action.reset.text": "초기화",
        "interactive.action.load.current.file.text": "현재 파일 로드",
        "interactive.auto.detected.cling.path": "자동 감지됨: {0}",
        "dialog.message.interactive.process.0.not.created": "Cling 프로세스 ''{0}''을(를) 생성할 수 없습니다.",
        "intentions.group": "C 및 C++",
        "notification.group.cling.interactive": "Cling 대화형 실행 실패"
    }

    filename = "OCInteractiveBundle.properties"
    found = False
    for file_entry in data.get('new_files', []):
        if file_entry['filename'] == filename:
            file_entry['keys'].update(ko_dict)
            found = True
            break
    if not found:
        data.setdefault('new_files', []).append({"filename": filename, "keys": ko_dict})

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"Updated {filename}")

if __name__ == "__main__":
    update_missing_keys()
