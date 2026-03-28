import json
from pathlib import Path

def update_missing_keys():
    file_path = Path("missing_translations/missing_keys_korean.json")
    
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    ko_dict = {
        "error.text.different.kotlin.gradle.version": "Gradle을 사용한 빌드에 사용된 Kotlin 버전({0})이 IDE 플러그인({1})에서 제대로 지원되지 않습니다.", 
        "error.text.different.kotlin.library.version": "플러그인 버전({0})이 라이브러리 버전({1})과 다릅니다."
    }
    
    filename = "KotlinGroovyBundle.properties"
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
