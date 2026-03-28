import json
from pathlib import Path

def update_missing_keys():
    file_path = Path("missing_translations/missing_keys_korean.json")
    
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    ko_dict = {
        "generate.comparison.operators.member.chooser.title": "사용할 필드 선택",
        "generate.comparison.operators.as.member.option": "클래스 멤버로 생성(&M)",
        "generate.comparison.operators.use.std.tie": "std::tie 사용(&T)",
        "generate.comparison.operators.additional.eq.option": "==와 함께 != 생성(&W)",
        "generate.comparison.operators.additional.eq.option.desc": "==와 함께 != 생성",
        "generate.comparison.operators.additional.rel.option": "<와 함께 >, <=, >= 생성(&W)",
        "generate.comparison.operators.additional.rel.option.desc": "<와 함께 >, <=, >= 생성",
        "generate.comparison.operators.usages.all.defined": "모든 연산자가 이미 정의되었습니다.",
        "generate.comparison.operators.usages.some.defined": "일부 연산자가 이미 정의되었습니다.",
        "generate.comparison.operators.usages.existing.text": "기존 연산자",
        "generate.getter.add.prefix": "Getter에 get/is 접두사 추가",
        "generate.setter.add.prefix": "Setter에 set 접두사 추가",
        "generate.stream.output.action.title": "스트림 출력 연산자 생성",
        "generate.stream.output.member.chooser.title": "사용할 필드 선택",
        "generate.stream.output.usages.all.defined": "스트림 출력 연산자가 이미 정의되었습니다.",
        "generate.stream.output.usages.existing.text": "기존 연산자",
        "generate.configurable.retain.parameters": "initWith\\u2026에 객체 매개변수 유지",
        "generate.configurable.use.property.setters": "initWith\\u2026에 프로퍼티 Setter 사용",
        "generate.configurable.put.ivars": "가능한 경우 구현에 ivar 배치",
        "generate.configurable.semicolon.after.method": "구현의 메서드 시그니처 뒤의 세미콜론",
        "generate.configurable.use.nsinteger.and.cgfloat": "변수 도입에 NSInteger 및 CGFloat 사용",
        "generate.configurable.instance.variable.prefix": "인스턴스 변수 접두사:",
        "generate.configurable.instance.variable.suffix": "인스턴스 변수 접미사:",
        "generate.configurable.add.brief.tag": "@brief 태그 추가",
        "generate.configurable.const.volatile.placement": "const/volatile 한정자 위치",
        "generate.configurable.top.level.declarations.order": "최상위 선언 순서",
        "generate.configurable.ivars.release.style": "Ivar 릴리스 스타일('dealloc'용)",
        "generate.configurable.ivars.generation": "프로퍼티에 대한 ivar 선언 생성",
        "generate.configurable.ivars.generation.always": "항상 생성",
        "generate.configurable.ivars.generation.never": "생성 안 함",
        "generate.configurable.ivars.generation.ask": "매번 묻기",
        "generate.configurable.tag.prefix.comments": "줄 주석의 태그 접두사:",
        "generate.configuralble.tag.prefix.block.comments": "블록 주석의 태그 접두사:",
        "generate.configurable.documentation.title": "문서 주석",
        "inspections.templateArguments.tooFew": "템플릿 인수가 너무 적습니다. {0}개가 필요합니다.",
        "inspections.templateArguments.tooFewAtLeast": "템플릿 인수가 너무 적습니다. 최소 {0}개가 필요합니다.",
        "inspections.templateArguments.tooMany": "템플릿 인수가 너무 많습니다. {0}개가 필요합니다.",
        "inspections.templateArguments.tooManyAtMost": "템플릿 인수가 너무 많습니다. 최대 {0}개가 필요합니다.",
        "inspections.templateArguments.valueInsteadOfType": "형식 대신 값이 필요합니다.",
        "inspections.templateArguments.typeInsteadOfValue": "값 대신 형식이 필요합니다.",
        "inspections.typeChecks.volatileConflict": "volatile이 아닌 구조체를 volatile에 할당 중",
        "inspections.duplicate.explicitInstantiation": "중복된 명시적 인스턴스화",
        "inspections.typeChecks.neitherNumericNorPointer": "''{0}'' 형식의 표현식은 숫자도 포인터도 아닙니다.",
        "inspections.typeChecks.notNumeric": "''{0}'' 형식의 표현식은 숫자가 아닙니다.",
        "inspections.fileChecks.allContextsUnloaded": "이 대상에 사용 가능한 모든 확인 컨텍스트에 대해 인덱싱이 비활성화되어 있습니다. 코드 인사이트 기능이 제대로 작동하지 않을 수 있습니다.",
        "inspections.fileChecks.sourceTooLarge": "파일 크기({0})가 {1}에 대해 구성된 제한({2})을 초과합니다. 코드 인사이트 기능을 사용할 수 없습니다.",
        "inspections.fileChecks.headerTooLarge": "파일에 포함된 인라인 헤더({3})의 길이({0})가 {1}에 대해 구성된 제한({2})을 초과하여 헤더가 구문 분석되지 않습니다.",
        "inspections.fileChecks.headerTooLargePlatform": "파일에 포함된 인라인 헤더({2})의 길이({0})가 구성된 제한({1})을 초과하여 헤더가 구문 분석되지 않습니다.",
        "checkbox.allow.import.in.completion": "완성 시 자동 가져오기",
        "checkbox.local.files.with.quotes": "따옴표가 있는 로컬 파일 자동 가져오기"
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
