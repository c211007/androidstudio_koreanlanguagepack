import json
from pathlib import Path

def update_missing_keys():
    file_path = Path("missing_translations/missing_keys_korean.json")
    
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    ko_dict = {
        "surround.with.try.catch.finally.template": "try / catch / finally",
        "surround.with.try.catch.template": "try / catch",
        "class.initializer": "<클래스 초기화자>",
        "object.0": "object{0}",
        "show.non.public": "Non-public",
        "show.properties": "Properties",
        "kmp.wasm.support.availability.name": "WASM 모듈용 Kotlin Multiplatform",
        "slice.nullness.progress.title.expanding.all.nodes": "모든 노드 확장 중\\u2026 (시간이 오래 걸릴 수 있습니다)",
        "slice.nullness.tab.title.grouped.by.nullness": "\\ Null 허용 여부로 그룹화"      
    }
    
    filename = "KotlinCodeInsightBundle.properties"
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
