import json
from pathlib import Path

def update_missing_keys():
    file_path = Path("missing_translations/missing_keys_korean.json")
    
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    ko_dict = {
        "replace.0.with.1": "''{0}''을(를) ''{1}''(으)로 바꾸기",
        "library.should.be.updated.to.be.compatible.with.kotlin.1.3": "Kotlin 1.3과 호환되도록 라이브러리를 업데이트해야 합니다.",
        "fix.change.feature.support.family": "{0} 지원 활성화/비활성화",
        "fix.change.feature.support.enabled": "{0} 지원 활성화",
        "fix.change.feature.support.enabled.warning": "{0} 지원 활성화(경고 포함)",
        "fix.change.feature.support.disabled": "{0} 지원 비활성화"
    }
    
    filename = "KotlinInspectionsBundle.properties"
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
