import json
from pathlib import Path

def update_missing_keys():
    file_path = Path("missing_translations/missing_keys_korean.json")

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    ko_dict = {
        "action.close.panel.text": "무시",
        "action.ignore.plugin.text": "문제 숨기기",
        "notification.content.freeze.detected": "{0} 속도가 느려졌습니다",
        "notification.content.plugin.caused.freeze": "''{0}'' 플러그인이 속도를 늦추고 있을 수 있습니다",
        "action.report.text": "문제 보고",
        "action.ignore.plugin.tooltip": "향후 이러한 성능 문제 무시",
        "action.dismiss.tooltip": "알림 무시"
    }

    filename = "PluginFreezeBundle.properties"
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
