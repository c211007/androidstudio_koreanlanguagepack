import json
from pathlib import Path

def update_missing_keys():
    file_path = Path("missing_translations/missing_keys_korean.json")

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    ko_dict = {
        "intention.family.name.simplify.condition": "조건을 ''{0}''(으)로 단순화",
        "intention.name.change.format.specifier": "포맷 지정자를 ''{0}''(으)로 변경",
        "intention.family.name.remove.statement": "구문 제거",
        "intention.family.name.remove.directive": "지시문 제거",
        "intention.family.name.simplify.choice": "{1, choice, 0#표현식|1#{0}} 단순화",
        "intention.family.name.change.type.to.auto": "''{0}'' 타입을 ''auto''로 변경",
        "intention.family.name.change.to.nil": "'nil'로 변경",
        "intention.name.use.constant": "상수 ''{0}'' 사용",
        "intention.family.name.use.enum.constant": "열거형 상수 사용",
        "intention.name.add": "\"{0}\" 추가",
        "intention.family.name.add.bridge.cast": "브리지 캐스트 추가",
        "intention.family.name.make.default": "{0}을(를) 기본값으로 설정",
        "inspection.message.condition.always.true": "조건이 항상 true입니다.",
        "inspection.message.condition.always.false": "조건이 항상 false입니다.",
        "inspection.message.condition.always.true.when.reached": "도달했을 때 조건이 항상 true입니다.",
        "inspection.message.condition.always.false.when.reached": "도달했을 때 조건이 항상 false입니다.",
        "inspection.message.reference.may.be.choice.null": "포인터가 null일 수 있습니다.",
        "inspection.message.not.initialized.field.usage": "초기화되지 않은 {0}이(가) 사용되었습니다.",
        "inspection.message.infinite.recursion": "무한 재귀",
        "inspection.message.value.never.used": "값이 사용되지 않습니다.",
        "inspection.message.file.too.complex.to.perform.data.flow.analysis": "파일이 너무 복잡하여 데이터 흐름 분석을 수행할 수 없습니다.",
        "inspection.message.unreachable.code": "도달할 수 없는 코드",
        "inspection.message.endless.loop": "무한 루프",
        "inspection.group.name.general": "일반",
        "progress.text.evaluating.unused.symbols": "사용되지 않는 심볼 평가 중",
        "intention.name.delete": "{0} 삭제",
        "intention.name.choice.superclass": "{2}의 {1, choice, 0#{0} |1#}상위 클래스",
        "intention.name.set.superclass": "''{0}''을(를) {1}(으)로 설정",
        "inspection.message.if.statement.has.identical.branches": "'if' 구문에 동일한 브랜치가 있습니다.",
        "inspection.message.statement.can.be.simplified": "구문을 단순화할 수 있습니다.",
        "inspection.message.expression.can.be.simplified.to": "표현식을 ''{0}''(으)로 단순화할 수 있습니다.",
        "intention.family.name.inline.parameter": "매개변수 인라인화",
        "intention.name.inline": "{0} 인라인화",
        "inspection.message.not.updated.in.loop": "루프 조건에 사용된 {0}이(가) 루프 내에서 업데이트되지 않습니다.",
        "inspection.message.address.local.variable.may.escape.function": "{0}의 주소가 함수를 벗어날 수 있습니다.",
        "inspection.message.address.local.object.may.escape.function": "지역 임시 객체의 주소가 함수를 벗어날 수 있습니다.",
        "inspection.message.may.point.to.invalidated.memory": "{0}이(가) 무효화된 메모리를 가리킬 수 있습니다.",
        "inspection.message.may.point.to.out.of.scope.memory": "{0}이(가) 범위를 벗어난 메모리를 가리킬 수 있습니다.",
        "inspection.message.may.point.to.deallocated.memory": "{0}이(가) 할당 해제된 메모리를 가리킬 수 있습니다.",
        "inspection.message.memory.leak": "''{0}'' 함수에 할당된 메모리 누수 발생",
        "inspection.message.allocated.memory.leaked": "할당된 메모리 누수 발생",
        "inspection.message.is.never.used": "{0}이(가) 사용되지 않습니다.",
        "inspection.message.only.assigned.but.never.accessed": "{0}이(가) 할당만 되고 액세스되지 않았습니다.",
        "inspection.message.calls.unreachable": "{0}의 모든 호출에 도달할 수 없습니다.",
        "inspection.not.implements.protocol": "구현되지 않은 프로토콜",
        "inspection.not.in.hierarchy.message": "계층 구조에 없는 메시지",
        "inspection.hides.class.scope": "숨겨진 클래스 범위",
        "inspection.method.is.later.in.the.scope": "메서드 선언이 범위에서 나중에 있습니다.",
        "inspection.accessors.were.overridden": "재정의된 접근자",
        "inspection.unused.include.directive.completely.unused": "완전히 사용되지 않는 항목 감지"
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
