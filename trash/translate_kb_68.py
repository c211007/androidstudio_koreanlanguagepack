import json
from pathlib import Path

def update_missing_keys():
    file_path = Path("missing_translations/missing_keys_korean.json")
    
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    ko_dict = {
        "action.text.implement.as.constructor.parameters": "생성자 매개변수로 구현",
        "implement.members.handler.family": "멤버 구현",
        "implement.members.handler.no.members.hint": "구현할 멤버를 찾을 수 없습니다.",
        "override.members.handler.no.members.hint": "오버라이드할 멤버를 찾을 수 없습니다.",
        "implement.members.handler.title": "멤버 구현",
        "override.members.handler.title": "멤버 오버라이드/구현",
        "fix.enable.feature.support.family": "{0} 지원 활성화",
        "fix.enable.feature.support.text": "기능에 대한 인수 구성: {0}" 
    }
    
    filename = "KotlinIdeaCoreBundle.properties"
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
