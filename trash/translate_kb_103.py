import json
from pathlib import Path

def update_missing_keys():
    file_path = Path("missing_translations/missing_keys_korean.json")
    
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    ko_dict = {
        "group.advanced.settings.kotlin": "Kotlin",
        "advanced.setting.kotlin.compiler.ref.index": "컴파일러 참조 인덱스",
        "advanced.setting.kotlin.compiler.ref.index.description": "컴파일러 인덱스의 참조를 사용하여 사용 위치 찾기를 활성화합니다.",
        "action.KotlinCompilerReferenceIndexVerifierAction.text": "컴파일러 인덱스 상태 표시",
        "dialog.title.invalid.data": "잘못된 데이터",
        "dialog.message.psielement.not.found": "PsiElement를 찾을 수 없음",
        "dialog.message.project.not.found": "프로젝트를 찾을 수 없음",
        "dialog.title.compiler.index.status": "컴파일러 인덱스 상태"
    }
    
    filename = "KotlinReferenceIndexBundle.properties"
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
