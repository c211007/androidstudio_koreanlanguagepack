import json
from pathlib import Path

def update_missing_keys():
    file_path = Path("missing_translations/missing_keys_korean.json")
    
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    ko_dict = {
        "method": "메서드",
        "function": "함수",
        "block": "블록",
        "lambda": "람다",
        "callable.type.title": "호출 가능한 형식",
        "annotator.type.literals.are.not.supported": "컴파일러에서 {0} 리터럴을 지원하지 않습니다.",
        "extract.category.dialog": "카테고리 추출",
        "extract.category.unable.create.file": "파일을 생성할 수 없습니다.",
        "extract.unavailable.for.protocols": "프로토콜에서는 이 작업을 사용할 수 없습니다.",
        "extract.method.selected.block.hint": "선택한 블록은 문장 또는 표현식의 집합을 나타내야 합니다.",
        "extract.method.cannot.determine.hint": "선택한 표현식의 형식을 확인할 수 없습니다.",
        "extract.class.use.protocol.instead": "대신 \"상위 프로토콜 추출\"을 사용하세요.",
        "extract.class.element.not.located.hint": "선택한 요소는 프로젝트 내에 있지 않은 클래스의 카테고리입니다.",
        "extract.subclass.dialog.title": "하위 클래스 추출",
        "extract.symbol.already.exist": "{0}이(가) 이미 존재합니다.",
        "create.file.title": "파일",
        "create.file.description": "새 파일 생성",
        "create.field.name.category": "카테고리 이름(&N):",
        "create.field.language": "언어(&L):",
        "create.field.class": "클래스(&C):",
        "create.class.title": "Objective-C 클래스",
        "create.class.dialog.title": "새 Objective-C 클래스",
        "create.class.objc": "Objective-C (.m)",
        "create.class.objcpp": "Objective-C++ (.mm)",
        "create.class.description": "새 Objective-C 클래스 및 헤더 파일 생성",
        "create.protocol.title": "Objective-C 프로토콜",
        "create.protocol.description": "새 Objective-C 프로토콜 생성",
        "create.protocol.dialog.title": "새 Objective-C 프로토콜",
        "create.category.title": "Objective-C 카테고리",
        "create.category.description": "새 Objective-C 카테고리 생성",
        "create.category.dialog.title": "새 Objective-C 카테고리",
        "create.checkbox.category.interface": "인터페이스 파일 생성(&I)",
        "create.category.no.class.dialog": "''{0}'' 클래스를 찾을 수 없습니다.\\n카테고리를 생성하시겠습니까?",
        "create.category.no.class.dialog.title": "잘못된 클래스",
        "create.implementation.title": "구현",
        "create.implementation.description": "새 구현 생성",
        "create.interface.title": "인터페이스",
        "create.interface.description": "새 인터페이스 생성",
        "codeassists.surroundwith.expression": "다음으로 둘러싸기",
        "copy.files.handler.fail": "''{0}''(으)로 파일을 복사하지 못했습니다.",
        "code.style.remember.choice": "선택 사항 기억",
        "refactoring.categoryElement.not.in.project": "선택한 요소는 프로젝트 내에 있지 않은 클래스의 카테고리에 있습니다.",
        "refactoring.category.not.in.project": "선택한 요소는 프로젝트 내에 있지 않은 클래스의 카테고리입니다.",
        "navigation.import.hierarchy.including.title": "{0}을(를) 포함하는 파일",
        "navigation.import.hierarchy.including.action": "포함하는 계층",
        "navigation.import.hierarchy.including.action.description": "포함하는 계층으로 전환",
        "navigation.import.hierarchy.included.title": "{0}에 포함된 파일",
        "navigation.import.hierarchy.included.action": "포함된 계층",
        "navigation.import.hierarchy.included.action.description": "포함된 계층으로 전환",
        "navigation.import.hierarchy.next.occurence": "다음 파일로 이동"
    }
    
    filename = "OCBundle.properties"
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
