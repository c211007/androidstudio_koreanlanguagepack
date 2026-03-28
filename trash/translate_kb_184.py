import json
from pathlib import Path

def update_missing_keys():
    file_path = Path("missing_translations/missing_keys_korean.json")

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    ko_dict = {
        "error.illegal.unsupported.escape.sequence": "잘못된/지원되지 않는 이스케이프 시퀀스",
        "error.invalid.group.name": "잘못된 그룹 이름",
        "error.look.behind.groups.are.not.supported.in.this.regex.dialect": "이 정규식 방언에서는 Look-behind 그룹이 지원되지 않습니다.",
        "error.lookaround.conditions.in.conditionals.not.supported.in.this.regex.dialect": "이 정규식 방언에서는 조건부에 대한 Lookaround 조건이 지원되지 않습니다.",
        "error.named.group.reference.not.allowed.inside.lookbehind": "lookbehind 내에서는 명명된 그룹 참조가 허용되지 않습니다.",
        "error.named.unicode.characters.are.not.allowed.in.this.regex.dialect": "이 정규식 방언에서는 명명된 유니코드 문자가 허용되지 않습니다.",
        "error.nested.quantifier.in.regexp": "정규식에 중첩된 수량자",
        "error.property.escape.sequences.are.not.supported.in.this.regex.dialect": "이 정규식 방언에서는 속성 이스케이프 시퀀스가 지원되지 않습니다.",
        "error.redundant.group.nesting": "중복된 그룹 중첩",
        "error.repetition.value.too.large": "반복 값이 너무 큽니다.",
        "error.this.boundary.is.not.supported.in.this.regex.dialect": "이 정규식 방언에서는 이 경계가 지원되지 않습니다.",
        "error.this.hex.character.syntax.is.not.supported.in.this.regex.dialect": "이 정규식 방언에서는 이 16진수 문자 구문이 지원되지 않습니다.",
        "error.this.kind.group.reference.condition.not.supported.in.this.regex.dialect": "이 정규식 방언에서는 이러한 종류의 그룹 참조 조건이 지원되지 않습니다.",
        "error.this.named.group.reference.syntax.is.not.supported.in.this.regex.dialect": "이 정규식 방언에서는 이 명명된 그룹 참조 구문이 지원되지 않습니다.",
        "error.this.named.group.syntax.is.not.supported.in.this.regex.dialect": "이 정규식 방언에서는 이 명명된 그룹 구문이 지원되지 않습니다.",
        "error.unequal.min.and.max.in.counted.quantifier.not.allowed.inside.lookbehind": "lookbehind 내에서는 counted 수량자의 min 및 max가 동일해야 합니다.",
        "error.unknown.character.category": "알 수 없는 문자 카테고리",
        "error.unknown.character.name": "알 수 없는 문자 이름",
        "error.unknown.inline.option.flag": "알 수 없는 인라인 옵션 플래그",
        "error.unknown.posix.character.class": "알 수 없는 POSIX 문자 클래스",
        "error.unknown.property.name": "알 수 없는 속성 이름",
        "error.unknown.property.value": "알 수 없는 속성 값",
        "error.unresolved.back.reference": "확인할 수 없는 루프백 참조",
        "error.unresolved.named.group.reference": "확인할 수 없는 명명된 그룹 참조",
        "error.unresolved.numbered.group.reference": "확인할 수 없는 번호가 매겨진 그룹 참조",
        "filetype.regular.expression.description": "정규 표현식",
        "inspection.group.name.regexp": "정규 표현식",
        "inspection.name.anonymous.group.or.numeric.back.reference": "익명 캡처 그룹 또는 숫자 루프백 참조",
        "inspection.name.begin.or.end.anchor.in.unexpected.position": "예상치 못한 위치에 시작 또는 끝 앵커가 있습니다.",
        "inspection.name.consecutive.spaces": "연속된 공백",
        "inspection.name.custom.regexp": "사용자 지정 정규 표현식 검사",
        "inspection.name.duplicate.branch.in.alternation": "교대(alternation)에 중복 분기(branch)가 있습니다.",
        "inspection.name.duplicate.character.in.class": "문자 클래스에 중복 문자가 있습니다.",
        "inspection.name.empty.branch.in.alternation": "교대(alternation)에 빈 분기(branch)가 있습니다.",
        "inspection.name.escaped.meta.character": "이스케이프된 메타 문자",
        "inspection.name.octal.escape": "8진수 이스케이프",
        "inspection.name.redundant.character.escape": "중복된 문자 이스케이프",
        "inspection.name.redundant.digit.class.element": "중복된 '\\\\d', '[:digit:]' 또는 '\\\\D' 클래스 요소",
        "inspection.name.redundant.nested.character.class": "중복된 중첩 문자 클래스",
        "inspection.name.simplifiable.expression": "정규 표현식을 간소화할 수 있습니다.",
        "inspection.name.single.character.alternation": "단일 문자 교대(alternation)",
        "inspection.name.suspicious.backref": "의심스러운 루프백 참조",
        "inspection.name.unnecessary.non.capturing.group": "불필요한 비캡처 그룹",
        "inspection.option.ignore.escaped.closing.brackets": "이스케이프된 닫는 대괄호 '}' 및 ']' 무시",
        "inspection.option.ignore.escaped.forward.slashes": "이스케이프된 슬래시 '/' 무시",
        "inspection.quick.fix.remove.duplicate.0.from.character.class": "문자 클래스에서 중복 ''{0}'' 제거",
        "inspection.quick.fix.remove.duplicate.branch": "중복 분기 제거",
        "inspection.quick.fix.remove.duplicate.element.from.character.class": "문자 클래스에서 중복 요소 제거",
        "inspection.quick.fix.remove.empty.branch": "빈 분기 제거",
        "inspection.quick.fix.remove.redundant.0.class.element": "중복된 ''{0}'' 제거"
    }

    filename = "RegExpBundle.properties"
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
