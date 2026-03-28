import json
from pathlib import Path

def update_missing_keys():
    file_path = Path("missing_translations/missing_keys_korean.json")
    
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    ko_dict = {
        "checkbox.try.to.sort": "include 정렬",
        "checkbox.try.to.sort.tooltip": ".clang-format 코드 스타일을 통해 활성화",
        "group.option.predefine": ".h에서 선언/.m에서 가져오기",
        "group.option.import": ".h에서 가져오기",
        "progressbar.long.resolve.description": "확인 작업에 시간이 더 필요합니다...\\n취소하면 확인에 의존하는 편집기 작업을 사용할 수 없습니다.",
        "action.invalid.title": "잘못됨",
        "change.signature.convert.action": "{0}(으)로 변환할 구현 선택",
        "header.source.looking.for.the.best.file": "연관된 파일 찾는 중",
        "resolve.contexts.select.automatically": "자동으로 선택",
        "resolve.contexts.edit.json.config": "''{0}'' 편집",
        "resolve.contexts.create.json.config": "'c_cpp_properties.json' 생성",
        "oc.inlay.hints.blacklist.pattern.explanation": "메서드에 대한 힌트를 비활성화하려면 적절한 패턴을 사용하세요: \n<p> \n  <code><b>(*info)<b></code> - 매개변수 이름이 info로 끝나는 단일 매개변수 메서드<br> \n  <code><b>(key, value)<b></code> - key 및 value 매개변수가 있는 메서드<br> \n  <code><b>*::put(key, value)<b></code> - key 및 value 매개변수가 있는 put 메서드<br> \n</p>",
        "oc.inlay.hints.show.hints.for.enum.constants": "열거형 상수에 대한 힌트 표시",
        "inlay.parameters.oc.clangd.namehints.enums": "열거형 상수에 대한 힌트를 표시합니다.",
        "oc.inlay.hints.show.hints.for.constructors": "생성자 표현식에 대한 힌트 표시",
        "inlay.parameters.oc.clangd.namehints.construct.expr": "(...) , {...}, ... 등 다양한 형태의 초기화 생성자 표현식에 대한 힌트를 표시합니다.",
        "oc.inlay.hints.show.amp.nonconst.references": "const가 아닌 참조에 '\\\\&' 표시",
        "inlay.parameters.oc.clangd.namehints.non.const.references": "매개변수 이름 대신 '\\\\&'를 표시합니다. 이 옵션은 둘 사이를 토글하지만 이전 주석 등의 이유로 매개변수 이름이 숨겨질 수 있는 반면 '\\\\&'는 항상 표시됩니다.",
        "oc.inlay.hints.show.array.indices": "배열 인덱스에 대한 힌트 표시",
        "inlay.parameters.oc.clangd.namehints.array.indices": "배열 인덱스를 표시합니다. 지정된 이니셜라이저에는 힌트가 제공되지 않습니다.",
        "oc.inlay.hints.show.settings": "힌트 설정\\u2026",
        "oc.inlay.hints.disable.function": "{0, choice, 0#메서드|1#함수|2#생성자} ''{1}'' 힌트 비활성화",
        "oc.inlay.hints.type.name": "형식",
        "oc.inlay.hints.type.for.variables": "변수",
        "oc.inlay.hints.type.for.variables.description": "변수",
        "inlay.oc.type.hints.variables": "추론된 형식이 있는 변수에 대한 힌트를 표시합니다.",
        "oc.inlay.hints.type.for.lambdas": "람다",
        "oc.inlay.hints.type.for.lambdas.description": "람다",
        "inlay.oc.type.hints.lambdas": "람다의 호출 연산자 시그니처에 대한 힌트를 표시합니다.",
        "oc.inlay.hints.type.deduced.return.types": "추론된 반환 형식",
        "oc.inlay.hints.type.deduced.return.types.description": "추론된 반환 형식",
        "oc.inlay.hints.type.deduced.parameter.types": "추론된 매개변수 형식",
        "oc.inlay.hints.type.deduced.parameter.types.description": "추론된 매개변수 형식",
        "inlay.oc.type.hints.return.types": "함수에 대해 추론된 반환 형식에 대한 힌트를 표시합니다. 생략된 람다 반환 형식에도 영향을 줍니다.",
        "inlay.oc.type.hints.parameter.types": "추론된 매개변수 형식에 대한 힌트를 표시합니다.",
        "oc.inlay.hints.type.obvious.types": "명백한 형식",
        "oc.inlay.hints.type.obvious.types.description": "명백한 형식",
        "inlay.oc.type.hints.obvious.types": "명백한 형식에 대한 힌트를 표시합니다. 여기에는 생성자 유사 표현식, 명시적 캐스트, 리터럴, new 표현식, 범위가 지정된 열거형 값, 일반 int 형식이 포함됩니다.",
        "oc.inlay.hints.type.main.checkbox": "다음에 대한 형식 힌트 표시:",
        "include.cpp.message": "''#include <C++>''는 C++에 관심 있는 개발자를 위한 글로벌하고 포용적이며 다양한 커뮤니티입니다.",
        "include.cpp.url": "https://www.includecpp.org/",
        "include.cpp.intention.text": "자세히 알아보기",
        "usage.properties.search.message.delete": "{0}도 삭제하시겠습니까?",
        "usage.properties.search.message.find.usages": "{0}의 사용도 찾으시겠습니까?",
        "usage.properties.search.title": "프로퍼티 검색",
        "usage.instance.variables.search.message.delete": "{0}도 삭제하시겠습니까?",
        "usage.instance.variables.search.message.find.usages": "{0}의 사용도 찾으시겠습니까?",
        "usage.instance.variables.search.title": "인스턴스 변수 검색",
        "usage.method.search.title": "메서드 검색",
        "usage.method.search.message.delete": "{0}\\n\\n기본 {1}을(를) 삭제하시겠습니까?"
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
