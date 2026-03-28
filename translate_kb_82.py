import json
from pathlib import Path

def update_missing_keys():
    file_path = Path("missing_translations/missing_keys_korean.json")
    
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    ko_dict = {
        "override.declaration.x.overrides.y.in.class.list": "{0}은(는) 다음 클래스/인터페이스의 선언을 오버라이드합니다: {1} 기본 선언을 {2}하시겠습니까?",
        "resolving.super.methods.progress.title": "상위 메서드 확인 중?",
        "safe.delete.implements.conflict.message": "{0}은(는) {1}을(를) 구현합니다."
    }
    
    filename = "KotlinK2RefactoringsBundle.properties"
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
