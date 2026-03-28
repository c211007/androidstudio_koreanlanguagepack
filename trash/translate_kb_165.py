import json
from pathlib import Path

def update_missing_keys():
    file_path = Path("missing_translations/missing_keys_korean.json")

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    ko_dict = {
        "button.text.cancel": "나중에",
        "task.title.executing.performance.script": "성능 스크립트 실행 중",
        "dumping.project.files": "프로젝트 파일 덤프 중...",
        "comparing.project.files": "프로젝트 파일 비교 중...",
        "comparing.project.files.for.0": "{0}에 대한 프로젝트 파일 비교 중...",
        "action.CaptureMemorySnapShot.text": "메모리 스냅샷 캡처",
        "action.CaptureMemorySnapShot.description": "메모리 스냅샷 캡처",
        "notification.group.performance.plugin": "IDE 자체 프로파일링",
        "performancePlugin.can.not.be.unloaded": "재생 실행 중에는 플러그인을 언로드할 수 없습니다."
    }

    filename = "PerformanceTestingBundle.properties"
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
