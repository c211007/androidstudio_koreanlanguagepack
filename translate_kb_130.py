import json
from pathlib import Path

def update_missing_keys():
    file_path = Path("missing_translations/missing_keys_korean.json")
    
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    ko_dict = {
        "action.ShowNavBar.text": "탐색 모음으로 이동(_J)",
        "action.ShowNavBar.ShortText": "탐색 모음",
        "group.NavBarActions.text": "탐색 모음 작업",
        "action.NavBar-selectHome.text": "첫 번째 항목 선택",
        "action.NavBar-selectEnd.text": "마지막 항목 선택",
        "action.NavBar-selectUp.text": "해당 팝업 메뉴 열기",
        "action.NavBar-selectDown.text": "해당 팝업 메뉴 열기",
        "action.NavBar-selectLeft.text": "이전 항목 선택",
        "action.NavBar-selectRight.text": "다음 항목 선택",
        "action.NavBar-return.text": "선택한 항목에 대한 작업 수행"
    }
    
    filename = "NavBarFrontendBundle.properties"
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
