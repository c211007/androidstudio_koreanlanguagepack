import json
from pathlib import Path

def update_missing_keys():
    file_path = Path("missing_translations/missing_keys_korean.json")
    
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    ko_dict = {
        "manifest.colon.expected": "':'이(가) 필요합니다.",
        "manifest.whitespace.expected": "공백이 필요합니다.",
        "manifest.header.expected": "헤더가 필요합니다.",
        "header.name.invalid": "잘못된 헤더 이름입니다.",
        "header.reference.invalid": "잘못된 참조입니다.",
        "header.main.class.invalid": "잘못된 기본 클래스입니다.",
        "header.pre-main.class.invalid": "잘못된 사전 기본(pre-main) 클래스입니다.",
        "header.agent.class.invalid": "잘못된 에이전트 클래스입니다.",
        "inspection.group": "매니페스트",
        "inspection.newline.message": "매니페스트 파일이 마지막 줄 바꿈으로 끝나지 않습니다.",
        "inspection.newline.fix": "줄 바꿈 추가",
        "inspection.header.message": "헤더 이름을 알 수 없거나 철자가 틀렸습니다.",
        "inspection.header.ui.label": "사용자 지정 헤더:",
        "inspection.header.rename.fix.family.name": "헤더 이름 수정",
        "inspection.header.rename.fix": "''{0}''(으)로 변경",
        "inspection.header.remember.fix": "사용자 지정 헤더에 ''{0}'' 추가",
        "filetype.manifest.description": "매니페스트",
        "inspection.misspelled.header.display.name": "알 수 없거나 철자가 틀린 헤더 이름",
        "inspection.missing.final.newline.display.name": "마지막 줄 바꿈 누락"
    }
    
    filename = "ManifestBundle.properties"
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
