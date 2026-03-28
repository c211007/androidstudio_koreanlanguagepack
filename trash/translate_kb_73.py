import json
from pathlib import Path

def update_missing_keys():
    file_path = Path("missing_translations/missing_keys_korean.json")
    
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    ko_dict = {
        "action.InvalidateK2CachesInternalAction.text": "Kotlin 플러그인 K2 모드 캐시 무효화",
        "internal.kotlin.plugin.actions.notification.group": "내부 Kotlin 플러그인 작업",
        "notification.content.kotlin.internal.resolution.caches.were.invalidated.title": "Kotlin 캐시가 무효화되었습니다.",
        "dialog.title.invalidate.caches": "캐시 무효화",
        "button.source.library.caches": "소스 및 라이브러리 캐시",
        "button.source.caches": "소스 캐시",
        "notification.content.source.caches": "소스 캐시",
        "notification.content.source.library.caches": "소스 및 라이브러리 캐시",    
        "invalidate.source.caches.tooltip": "모든 K2 플러그인 소스 및 스크립트 캐시를 무효화합니다.<br/>\n 라이브러리 캐시는 그대로 유지됩니다.<br/>\n 이 작업을 호출하는 것은 각 모듈에서 동시에 블록 외부 수정(Out-of-block modification)을 수행하는 것과 같아야 합니다.<br/>",
        "invalidate.source.library.caches.tooltip": "모든 K2 플러그인 소스, 스크립트, 내장 및 라이브러리 캐시를 무효화합니다.<br/>\n 이 작업을 호출하는 것은 모든 프로젝트 라이브러리를 제거하고 다시 추가하는 것뿐만 아니라, \n 각 모듈에서 동시에 블록 외부(Out-of-block) 수정을 수행하는 것과 같아야 합니다."
    }
    
    filename = "KotlinInternalBundle.properties"
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
