import json
from pathlib import Path

def update_missing_keys():
    file_path = Path("missing_translations/missing_keys_korean.json")
    
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    ko_dict = {
        "exclude.0.from.completion": "자동 완성에서 ''{0}'' 제외",
        "insert.lambda.template": "람다 템플릿 삽입",
        "presentation.tail.for.0": "\\ for {0}",
        "presentation.tail.for.0.in.1": "\\ {1}의 {0}에 대해",
        "presentation.tail.from.0": "\\ ({0}에서)",
        "presentation.tail.in.0": "in {0}",
        "inspection.message.never.used": "{0}이(가) 사용되지 않았습니다.",
        "formatting.settings.dialog.message.formatterkind": "포맷터 종류 = {0}",   
        "find.usage.provider.0.of.1": "{1}의 {0}",
        "find.usage.provider.0": "{0}"
    }
    
    filename = "KotlinIdeaCompletionBundle.properties"
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
