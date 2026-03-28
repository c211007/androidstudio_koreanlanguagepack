import json
from pathlib import Path

def update_missing_keys():
    file_path = Path("missing_translations/missing_keys_korean.json")
    
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    ko_dict = {
        "local.studiobot.settings.description.title": "설명:",
        "local.studiobot.settings.port.title": "포트:",
        "local.studiobot.settings.warning": "<head></head><p>타사(third-party) 모델을 사용하면 코드 및 기타 입력 데이터를 해당 제공업체로 전송하는 데 동의하게 됩니다. Google은 타사 모델과의 상호 작용에 액세스하거나 이를 처리하지 않습니다.<br><br>파일, 프롬프트 및 모델의 응답을 포함한 모든 데이터는 타사 모델 제공업체로 직접 전송됩니다.</p>",
        "local.studiobot.settings.warning.note": "<head></head><p>참고로, 일부 Android 스튜디오 기능은 외부 모델에서 예상대로 작동하지 않을 수 있습니다.</p>",
        "local.studiobot.settings.warning.link": "자세히 알아보기",
        "local.studiobot.settings.error.empty.port": "로컬 모델 제공업체의 포트는 비워둘 수 없습니다.",
        "local.studiobot.settings.error.duplicate.port": "로컬 모델 제공업체의 포트는 고유해야 합니다.",
        "local.studiobot.settings.error.invalid.port": "로컬 모델 제공업체의 포트는 1에서 65535 사이의 숫자여야 합니다."
    }
    
    filename = "LocalProviderBundle.properties"
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
