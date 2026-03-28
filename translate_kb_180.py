import json
from pathlib import Path

def update_missing_keys():
    file_path = Path("missing_translations/missing_keys_korean.json")

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    ko_dict = {
        "generate.overloaded.method.or.constructor.with.default.parameter.values": "기본 매개변수 값으로 오버로드된 {0} 생성",
        "generate.overloaded.method.with.default.parameter.values": "기본 매개변수 값으로 오버로드된 메서드 생성",
        "remove.unreachable.branches": "도달할 수 없는 분기 제거",
        "simplify.boolean.expression.extracting.side.effects": "\\ 부작용 추출",
        "intention.move.parenthesis.name": "닫는 괄호 배치 수정",
        "extend.sealed.title": "''{0}''이(가) ''{2}''을(를) {1, choice, 1#상속|2#구현}하게 만들기 및",
        "extend.sealed.name": "''{0}''이(가) ''{2}''을(를) {1, choice, 1#상속|2#구현}하게 만들기",
        "implement.or.extend.fix.family": "필수 기본 클래스 구현/상속",
        "seal.class.from.permits.list.fix": "상속자 봉인(seal)",
        "unwrap.array.initializer.fix": "배열 초기화 구문을 요소로 교체",
        "replace.with.type.pattern.fix": "타입 패턴으로 교체",
        "make.annotation.applicable.to.0.fix": "{0}에 어노테이션을 적용할 수 있게 만들기",
        "merge.duplicate.attributes.family": "중복 속성 병합",
        "move.switch.branch.up.family": "switch 분기를 위로 이동",
        "move.switch.branch.up.text": "switch 분기 ''{0}''을(를) ''{1}'' 앞으로 이동",
        "qualify.method.call.fix": "''{0}''(으)로 호출 한정",
        "qualify.method.call.family": "메서드 호출 한정",
        "remove.redundant.nested.patterns.fix.text": "중복된 중첩 패턴 제거",
        "add.missing.nested.patterns.fix.text": "누락된 중첩 패턴 추가",
        "add.missing.str.processor": "'STR.' 프로세서 추가",
        "record.delegate.to.canonical.constructor.fix.name": "표준 생성자에 위임",
        "lift.throw.out.of.switch.expression.fix.name": "'throw'를 'switch' 표현식 밖으로 끌어올리기",
        "change.to.similar.keyword.fix.family.name": "유사한 키워드로 변경",
        "change.to.similar.keyword.fix.name": "오타 ''{0}''을(를) ''{1}''(으)로 수정"
    }

    filename = "QuickFixBundle.properties"
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
