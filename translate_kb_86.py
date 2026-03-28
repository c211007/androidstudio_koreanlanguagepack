import json
from pathlib import Path

def update_missing_keys():
    file_path = Path("missing_translations/missing_keys_korean.json")
    
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    ko_dict = {
        "template.context.type.generic": "Kotlin",
        "template.context.type.top.level": "최상위(Top-level)",
        "template.context.type.object": "객체 선언(Object declaration)",
        "template.context.type.class": "클래스",
        "template.context.type.expression": "표현식",
        "template.context.type.statement": "문(Statement)",
        "template.context.type.comment": "주석"
    }
    
    filename = "KotlinLiveTemplatesBundle.properties"
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
