import json
from pathlib import Path

def update_missing_keys():
    file_path = Path("missing_translations/missing_keys_korean.json")

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    ko_dict = {
        "action.add.pattern.text": "패턴 추가...",
        "action.add.regexp.replace.template.text": "정규 표현식 교체 템플릿 추가...",
        "action.add.regexp.search.template.text": "정규 표현식 검색 템플릿 추가...",
        "action.add.regexp.replace.inspection.text": "정규 표현식 교체 검사 추가...",
        "action.add.regexp.search.inspection.text": "정규 표현식 검색 검사 추가...",
        "button.enable.replace": "교체 사용",
        "button.search.only": "검색만",
        "checker.sample.text": "샘플 텍스트",
        "color.settings.bad.character": "잘못된 문자",
        "color.settings.brace": "중괄호",
        "color.settings.bracket": "대괄호",
        "color.settings.character.class": "문자 클래스",
        "color.settings.comma": "쉼표",
        "color.settings.comment": "주석",
        "color.settings.dot": "점",
        "color.settings.escaped.character": "이스케이프된 문자",
        "color.settings.inline.option": "인라인 옵션",
        "color.settings.invalid.escape.sequence": "잘못된 이스케이프 시퀀스",
        "color.settings.matched.groups": "일치하는 그룹",
        "color.settings.name": "이름",
        "color.settings.operator.character": "연산자 문자",
        "color.settings.parenthesis": "괄호",
        "color.settings.plain.character": "일반 문자",
        "color.settings.quantifier": "수량자",
        "color.settings.quote.character": "따옴표 이스케이프",
        "color.settings.redundant.escape.sequence": "중복된 이스케이프 시퀀스",
        "color.settings.title.regexp": "정규 표현식",
        "dialog.message.inspection.with.name.exists.warning": "이름이 ''{0}''인 검사가 이미 존재합니다.",
        "doc.property.block.stands.for.0": "속성 블록은 {0}을(를) 나타냅니다.",
        "doc.property.block.stands.for.characters.not.matching.0": "속성 블록은 {0}와일치하지 않는 문자를 나타냅니다.",
        "edit.metadata.button": "메타데이터 편집...",
        "error.0.repetition.not.allowed.inside.lookbehind": "lookbehind 내에서는 {0} 반복이 허용되지 않습니다.",
        "error.alternation.alternatives.needs.to.have.the.same.length.inside.lookbehind": "교대(alternation) 대안은 lookbehind 내에서 길이가 같아야 합니다.",
        "error.atomic.groups.are.not.supported.in.this.regex.dialect": "이 정규식 방언에서는 원자 그룹이 지원되지 않습니다.",
        "error.back.reference.is.nested.into.the.capturing.group.it.refers.to": "루프백 참조가 참조하는 캡처 그룹에 중첩되어 있습니다.",
        "error.conditional.group.reference.not.allowed.inside.lookbehind": "lookbehind 내에서는 조건부 그룹 참조가 허용되지 않습니다.",
        "error.conditionals.are.not.supported.in.this.regex.dialect": "이 정규식 방언에서는 조건부가 지원되지 않습니다.",
        "error.dangling.metacharacter": "유효하지 않은 위치의 수량자 ''{0}''",
        "error.dangling.opening.bracket": "예상치 못한 수량자 시작 '{'",
        "error.define.subpattern.contains.more.than.one.branch": "DEFINE 하위 패턴에 분기(branch)가 둘 이상 포함되어 있습니다.",
        "error.embedded.comments.are.not.supported.in.this.regex.dialect": "이 정규식 방언에서는 포함된(embedded) 주석이 지원되지 않습니다.",
        "error.empty.group": "빈 그룹",
        "error.group.reference.is.nested.into.the.named.group.it.refers.to": "그룹 참조가 참조하는 명명된 그룹에 중첩되어 있습니다.",
        "error.group.reference.not.allowed.inside.lookbehind": "lookbehind 내에서는 그룹 참조가 허용되지 않습니다.",
        "error.group.with.name.0.already.defined": "이름이 ''{0}''인 그룹이 이미 정의되어 있습니다.",
        "error.illegal.character.range.to.from": "잘못된 문자 범위 (to < from)",
        "error.illegal.hexadecimal.escape.sequence": "잘못된 16진수 이스케이프 시퀀스",
        "error.illegal.octal.escape.sequence": "잘못된 8진수 이스케이프 시퀀스",
        "error.illegal.repetition.range.min.max": "잘못된 반복 범위 (min > max)",
        "error.illegal.unicode.escape.sequence": "잘못된 유니코드 이스케이프 시퀀스"
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
