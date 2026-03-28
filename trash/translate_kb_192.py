import json
from pathlib import Path

def update_missing_keys():
    file_path = Path("missing_translations/missing_keys_korean.json")

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    ko_dict = {
        "notification.content.cannot.pause": "일시 중지할 수 없습니다.",
        "notification.content.paused.in.debugger": "디버거에서 일시 중지됨",
        "debug.vm.title.main.thread": "메인 스레드",
        "full.evaluator.invoke.getter": "\\u2026 (getter 호출)",
        "scope.variables.exception": "예외",
        "scope.variables.group.functions": "함수"
    }

    filename = "ScriptDebuggerBundle.properties"
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
