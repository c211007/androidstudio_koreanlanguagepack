import json
from pathlib import Path

def update_missing_keys():
    file_path = Path("missing_translations/missing_keys_korean.json")

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    ko_dict = {
        "configurable.naming.convention.header.guard.style": "헤더 가드 스타일:",
        "configurable.naming.convention.several.rules.hint": "하나의 엔터티 유형에 대해 여러 규칙이 있는 경우 목록의 마지막 규칙이 사용됩니다.",
        "inspection.clangd.general": "Clangd 오류 및 경고",
        "inspection.naming.convention.edit.settings.link": "코드 스타일 설정 편집",
        "inspection.naming.convention.rename.fix": "{0}(으)로 이름 바꾸기",
        "inspection.naming.convention.rename.header.guard.fix": "헤더 가드를 {0}(으)로 이름 바꾸기",
        "inspection.context.sensitive.analysis": "컨텍스트를 인식하는 분석",
        "inspection.global.unused.analysis": "전역 사용되지 않은 항목 분석",
        "inspection.inconsistent.naming": "일관되지 않은 명명",
        "inspection.modern.syntax": "최신 구문을 사용할 수 있음",
        "inspection.loop.condition.is.not.updated": "루프 내에서 루프 조건이 업데이트되지 않음",
        "inspection.arc.issues": "ARC 문제",
        "inspection.sending.dealloc": "직접 전송된 'dealloc'",
        "inspection.assign.in.condition.with.self": "'self'를 사용한 조건식에 '=' 사용",
        "inspection.usage.of.api.unavailable": "사용할 수 없는 API 사용",
        "inspection.deprecated.api": "더 이상 사용되지 않는 API 사용",
        "inspection.assign.in.condition": "조건식에 '=' 사용",
        "inspection.kr.unspecified.parameters": "K&R 지정되지 않은 매개변수 구문을 사용하여 함수에 인수 전달",
        "inspection.hiding.non.virtual.function": "가상이 아닌 함수 숨기기",
        "inspection.constant.conditions": "상수 조건",
        "inspection.non.localized.string": "현지화되지 않은 문자열",
        "inspection.simplifiable.statement": "단순화할 수 있는 구문",
        "inspection.simplify": "{0} 단순화",
        "inspection.replace.enable_if.with.require": "enable_if를 require로 바꿈",
        "inspection.simplify.condition": "\"condition == true\" 단순화",
        "inspection.simplify.ternary": "\"condition1 ? true : condition2\" 단순화",
        "inspection.not.released.var": "'dealloc' 또는 그 호출자에서 해제(release)되어야 합니다.",
        "unused.inspection.run.in.headers": "헤더 파일에서 검사 실행",
        "clang.based.inspection.arc.and.properties": "ARC 및 @properties",
        "clang.based.inspection.lexical.or.preprocessor.issue": "어휘 또는 전처리기 문제",
        "clang.based.inspection.api.notes.issue": "API 참고 사항 문제",
        "clang.based.inspection.openmp.issue": "OpenMP 문제",
        "clang.based.inspection.vtable.issue": "VTable ABI 문제",
        "clang.based.inspection.coroutines.issue": "코루틴 문제",
        "clang.based.inspection.concepts.issue": "개념 문제",
        "clang.based.inspection.dependency.directive.source.minimization.issue": "종속 요소 지시문 소스 최소화 문제",
        "inspection.message.modern.syntax.can.be.used": "최신 구문을 사용할 수 있습니다.",
        "inspection.message.non.localized.string": "현지화되지 않은 문자열: {0}",
        "inspection.message.not.released.in.dealloc.method": "''dealloc'' 메서드에서 {0}이(가) 해제되지 않았습니다.",
        "intention.family.name.add.call.to.super.dealloc": "[super dealloc]에 대한 호출 추가",
        "intention.family.name.delete.method": "메서드 삭제",
        "inspection.message.never.used": "{0}이(가) {1, choice, 0#할당되었지만 액세스되지 않았습니다|1#사용되지 않습니다}",
        "inspection.display.name.simplifiable.statement": "단순화할 수 있는 구문",
        "checkbox.simplify.if.true.while.false": "\"if (true)\", \"while (false)\" 단순화",
        "checkbox.simplify.condition.true": "\"condition == true\" 단순화",
        "checkbox.simplify.condition1.true.condition2": "\"condition1 ? true : condition2\" 단순화",
        "checkbox.simplify.if.condition1.return.true.return.condition2": "\"if (condition1) return true; return condition2;\" 단순화",
        "intention.family.name.simplify": "{0} 단순화",
        "intention.family.name.simplify.expression": "표현식 단순화",
        "intention.name.simplify": "{0} 단순화"
    }

    filename = "OCInspectionsBundle.properties"
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
