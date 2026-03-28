import json
from pathlib import Path

def update_missing_keys():
    file_path = Path("missing_translations/missing_keys_korean.json")
    
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    ko_dict = {
        "find.declaration.derived.interfaces.checkbox": "파생 인터페이스(&I)",        
        "find.usages.class": "클래스",
        "find.usages.companion.object": "동반 객체",
        "find.usages.constructor": "생성자",
        "find.usages.facade.class": "파사드 클래스",
        "find.usages.for.property": "프로퍼티에 대한 {0}",
        "find.usages.function": "함수",
        "find.usages.getter": "getter",
        "find.usages.import.alias": "가져오기 별칭",
        "find.usages.interface": "인터페이스",
        "find.usages.label": "레이블",
        "find.usages.lambda": "람다",
        "find.usages.object": "객체",
        "find.usages.parameter": "매개변수",
        "find.usages.property.accessor": "프로퍼티 접근자",
        "find.usages.property": "프로퍼티",
        "find.usages.setter": "setter",
        "find.usages.type.alias": "타입 별칭",
        "find.usages.type.parameter": "타입 매개변수",
        "find.usages.variable": "변수",
        "find.usages.checkbox.name.expected.classes": "예상되는 클래스",
        "find.usages.class.name.anonymous": "익명",
        "find.usages.checkbox.name.expected.functions": "예상되는 함수",
        "find.usages.text.find.usages.for.data.class.components.and.destruction.declarations": "<p>데이터 클래스 컴포넌트 및 구조 분해 선언에 대한 사용법 찾기를<br/><a href=\"{0}\">한 번 비활성화</a>하거나 <a href=\"{1}\">프로젝트에서 비활성화</a>할 수 있습니다.</p>",
        "find.usages.tool.tip.text.disable.search.for.data.class.components.and.destruction.declarations.project.wide.setting": "데이터 클래스 컴포넌트 및 구조 분해 선언에 대한 검색을 비활성화합니다. (프로젝트 전체 설정)",
        "find.usages.checkbox.text.fast.data.class.component.search": "빠른 데이터 클래스 컴포넌트 검색",
        "find.usages.checkbox.name.expected.properties": "예상되는 프로퍼티",       
        "find.usages.type.named.argument": "명명된 인수",
        "find.usages.type.type.alias": "타입 별칭",
        "find.usages.type.callable.reference": "호출 가능 참조",
        "find.usages.type.constructor.delegation.reference": "생성자 위임 참조",
        "find.usages.type.type.constraint": "타입 제약",
        "find.usages.type.value.parameter.type": "매개변수 타입",
        "find.usages.type.nonLocal.property.type": "클래스/객체 프로퍼티 타입",      
        "find.usages.type.function.return.type": "함수 반환 타입",
        "find.usages.type.superType": "상위 타입",
        "find.usages.type.is": "'is' 연산의 대상 타입",
        "find.usages.type.class.object": "중첩 클래스/객체",
        "find.usages.type.companion.object": "동반 객체",
        "find.usages.type.function.call": "함수 호출",
        "find.usages.type.implicit.get": "암시적 'get'",
        "find.usages.type.implicit.set": "암시적 'set'",
        "find.usages.type.implicit.invoke": "암시적 'invoke'",
        "find.usages.type.implicit.iteration": "암시적 반복",
        "find.usages.type.property.delegation": "프로퍼티 위임",
        "find.usages.type.extension.receiver.type": "확장 수신자 타입",        
        "find.usages.type.super.type.qualifier": "상위 타입 한정자",
        "find.usages.type.receiver": "수신자",
        "find.usages.type.delegate": "위임자",
        "find.usages.type.packageDirective": "패키지 지시문"
    }
    
    if "KotlinBundle.properties" not in data:
        data["KotlinBundle.properties"] = {}
        
    data["KotlinBundle.properties"].update(ko_dict)
    
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        
    print(f"Updated KotlinBundle.properties (Keys 2141-2190)")

if __name__ == "__main__":
    update_missing_keys()
