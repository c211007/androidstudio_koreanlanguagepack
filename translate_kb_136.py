import json
from pathlib import Path

def update_missing_keys():
    file_path = Path("missing_translations/missing_keys_korean.json")
    
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    ko_dict = {
        "color.local.variable": "변수//로컬",
        "color.struct.union.oc": "구조체/열거형/공용체",
        "color.struct.union": "클래스/구조체/열거형/공용체",
        "color.struct.field": "구조체 필드",
        "color.concept": "템플릿//컨셉",
        "color.template.type": "템플릿//형식",
        "color.template.value": "템플릿//값",
        "color.namespace": "네임스페이스",
        "color.enum.const": "열거형 상수",
        "color.function.declaration": "함수//선언",
        "color.function.call": "함수//호출",
        "color.overloaded.operator": "중괄호 및 연산자//오버로드된 연산자",
        "color.typedef": "Typedef",
        "color.label": "레이블",
        "color.dependent_code": "템플릿//종속 코드",
        "color.deduction_guide": "템플릿//추론 가이드",
        "color.this.keywords.oc": "키워드//'self','super','this'",
        "color.instance.variable.oc": "인스턴스 변수",
        "color.method.declaration.oc": "메서드 선언",
        "color.method.call.oc": "메서드 호출",
        "color.property.oc": "프로퍼티",
        "color.property.attribute.oc": "프로퍼티 속성",
        "color.class.reference.oc": "클래스",
        "color.protocol.reference.oc": "프로토콜",
        "color.generic.parameter.oc": "제네릭 매개변수",
        "color.doxygen.comment": "주석//Doxygen//텍스트",
        "color.doxygen.tag": "주석//Doxygen//태그",
        "color.doxygen.tag.value": "주석//Doxygen//태그 값",
        "color.std.initializer.list.oc": "중괄호 및 연산자//초기화 목록",
        "indent.namespace": "네임스페이스 멤버 들여쓰기",
        "indent.interface.protocol": "'@interface' 및 '@protocol' 멤버 들여쓰기",
        "indent.not.ivar": "인스턴스 변수 목록 제외",
        "indent.implementation": "'@implementation' 멤버 들여쓰기",
        "indent.visibility.keywords": "클래스/구조체의 가시성 키워드 들여쓰기",
        "indent.block": "람다 내부 들여쓰기",
        "indent.block.oc": "블록 및 람다 내부 들여쓰기",
        "indent.c.struct": "일반 구조체 및 열거형 멤버 들여쓰기",
        "indent.class": "클래스 멤버 들여쓰기",
        "indent.class.oc": "C++ 클래스 멤버 들여쓰기",
        "indent.preprocessor.directive": "전처리기 지시문 들여쓰기",
        "indent.preprocessor.directive.as.code": "코드 들여쓰기 따르기",
        "inline.handler.check.for.validness": "유효성 검사 중\\u2026",
        "checkbox.block.comment.indent": "블록 주석의 새 줄 들여쓰기",
        "override.implement.show.no.optional.members": "선택적 멤버 표시(선택 사항 없음)",
        "override.implement.show.only.optional.members": "선택적 멤버 표시(선택 사항만)",
        "override.implement.show.no.synthesized.accessors": "합성 접근자 표시(접근자 없음)",
        "override.implement.show.only.synthesized.accessors": "합성 접근자 표시(접근자만)",
        "override.implement.cpp.action.title": "함수 재정의/구현",
        "override.implement.cpp.action.name": "함수 재정의\\u2026",
        "override.implement.cpp.action.memberChooserTitle": "재정의/구현할 함수 선택"
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
