import json
from pathlib import Path

def update_missing_keys():
    file_path = Path("missing_translations/missing_keys_korean.json")
    
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    ko_dict = {
        "text.converting.java.to.kotlin": "Java를 Kotlin으로 변환하는 중",
        "text.files.count.0": "{0}개의 파일",
        "text.pass.of.3": "3개 중 {0}번째 단계(pass)",
        "text.searching.usages.to.update": "업데이트할 사용법(usages) 검색 중\\u2026"
    }
    
    filename = "KotlinJ2KBundle.properties"
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
