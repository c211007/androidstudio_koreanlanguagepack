import json
from pathlib import Path

def update_missing_keys():
    file_path = Path("missing_translations/missing_keys_korean.json")
    
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    ko_dict = {
        "action.DecompileKotlinToJava.text": "Java로 디컴파일",
        "action.decompile.busy.text": "Kotlin 클래스 파일",
        "internal.action.text.decompile.kotlin.bytecode": "Kotlin 바이트코드 디컴파일",
        "internal.error.text.cannot.decompile": "{0}을(를) 디컴파일할 수 없습니다.",
        "internal.indicator.text.decompiling": "{0} 디컴파일 중\\u2026",
        "internal.title.decompiler.error": "디컴파일 실패"
    }
    
    filename = "KotlinJvmDecompilerBundle.properties"
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
