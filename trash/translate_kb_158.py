import json
from pathlib import Path

def update_missing_keys():
    file_path = Path("missing_translations/missing_keys_korean.json")

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    ko_dict = {
        "inspection.unused.include.directive.completely.not.directly": "직접 사용되지 않는 항목 감지",
        "inspection.unused.include.directive.completely.not.required": "필요하지 않은 항목 감지",
        "inspection.null.dereference.display.name": "Null 역참조",
        "inspection.not.initialized.field.display.name": "초기화되지 않은 필드",
        "inspection.unreachable.code.display.name": "도달할 수 없는 코드",
        "inspection.unreachable.calls.display.name": "도달할 수 없는 함수의 호출",
        "inspection.endless.loop.display.name": "무한 루프",
        "inspection.infinite.recursion.display.name": "무한 재귀",
        "inspection.local.value.escapes.scope.display.name": "범위를 벗어나는 지역 값",
        "inspection.dangling.pointer.display.name": "현수 포인터(Dangling Pointer)",
        "inspection.memory.leak.display.name": "메모리 누수",
        "inspection.constant.parameter.display.name": "상수 매개변수",
        "inspection.constant.function.result.display.name": "상수 함수 결과",
        "inspection.array.index.out.of.bounds.display.name": "배열 인덱스가 범위를 벗어남",
        "inspection.not.initialized.variable.display.name": "초기화되지 않은 변수",
        "inspection.missing.return.display.name": "누락된 반환",
        "inspection.unused.local.variable.display.name": "사용되지 않는 지역 변수",
        "inspection.unused.parameter.display.name": "사용되지 않는 매개변수",
        "inspection.unused.value.display.name": "사용되지 않는 값",
        "inspection.not.implemented.functions.display.name": "구현되지 않은 함수",
        "inspection.unused.expression.result.display.name": "사용되지 않는 표현식 결과",
        "inspection.unused.concept.display.name": "사용되지 않는 개념",
        "inspection.unused.global.declaration.display.name": "사용되지 않는 전역 선언",
        "inspection.unused.macro.display.name": "사용되지 않는 매크로",
        "inspection.unused.struct.display.name": "사용되지 않는 구조체",
        "inspection.unused.template.parameter.display.name": "사용되지 않는 템플릿 매개변수",
        "inspection.unused.type.alias.display.name": "사용되지 않는 타입 별칭",
        "inspection.unused.directive.display.name": "사용되지 않는 포함 지시문",
        "inspection.dfa.group.display.name": "데이터 흐름 분석",
        "inspection.functions.group.display.name": "함수",
        "inspection.unused.import.statement.display.name": "사용되지 않는 Import 구문",
        "inspection.unused.localization.display.name": "사용되지 않는 현지화",
        "inspection.unused.class.display.name": "사용되지 않는 클래스",
        "inspection.unused.instance.variable.display.name": "사용되지 않는 인스턴스 변수",
        "inspection.unused.method.display.name": "사용되지 않는 메서드",
        "inspection.unused.property.display.name": "사용되지 않는 프로퍼티",
        "intention.suffix.called.from": "\\ ''{0}'' 함수에서 호출될 때",
        "intention.suffix.called.from.global.scope": "\\ 전역 범위에서 호출될 때",
        "dfa.message.preparing": "{0} 준비 중...",
        "dfa.batch.action.title": "전역 데이터 흐름 분석",
        "dfa.batch.action.subject": "분석",
        "inspections.memory.leak.allocating.functions": "할당 함수",
        "inspections.memory.leak.deallocating.functions": "할당 해제 함수"
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
