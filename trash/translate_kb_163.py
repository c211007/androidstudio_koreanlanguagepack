import json
from pathlib import Path

def update_missing_keys():
    file_path = Path("missing_translations/missing_keys_korean.json")

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    ko_dict = {
        "element.inherits.method": "{0}이(가) {1}에서 메서드를 상속합니다.",
        "cannot.inline.method.reference.in.selector.expression": "'@selector' 표현식에서 메서드 참조를 인라인화할 수 없습니다.",
        "cannot.inline.method.reference.in.xml.file": "XML 파일에서 메서드 참조를 인라인화할 수 없습니다.",
        "cannot.inline.method.reference.in.property.attribute": "속성 특성에서 메서드 참조를 인라인화할 수 없습니다.",
        "cannot.inline.function.reference.in.non.call.expression": "호출이 아닌 표현식에서 함수 참조를 인라인화할 수 없습니다.",
        "cannot.inline.usage.in.swift.code": "Swift 코드 내의 사용을 인라인화할 수 없습니다.",
        "cannot.inline.recursive": "재귀적 {0} 호출을 인라인화할 수 없습니다.",
        "dialog.message.elements.to": "{0}에 대한 요소",
        "top.level.namespace.placeholder": "최상위 최상위 네임스페이스"
    }

    filename = "OCRefactoringBundle.properties"
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
