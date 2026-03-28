import json
from pathlib import Path

def update_missing_keys():
    file_path = Path("missing_translations/missing_keys_korean.json")

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    ko_dict = {
        "inspection.quick.fix.remove.redundant.class.element": "중복된 클래스 요소 제거",
        "inspection.quick.fix.remove.redundant.escape": "중복된 이스케이프 제거",
        "inspection.quick.fix.remove.unnecessary.non.capturing.group": "불필요한 비캡처 그룹 해제",
        "inspection.quick.fix.replace.alternation.with.character.class": "교대(alternation)를 문자 클래스로 바꾸기",
        "inspection.quick.fix.replace.redundant.character.class.with.contents": "중복된 문자 클래스를 내용으로 바꾸기",
        "inspection.quick.fix.replace.with.character.inside.class": "클래스 내의 문자로 교체",
        "inspection.quick.fix.replace.with.hexadecimal.escape": "16진수 이스케이프로 교체",
        "inspection.quick.fix.replace.with.space.and.repeated.quantifier": "공백과 반복 수량자로 교체",
        "inspection.warning.anchor.code.ref.code.in.unexpected.position": "예상치 못한 위치에 있는 제한자(Anchor) <code>#ref</code>",
        "inspection.warning.anonymous.capturing.group": "익명 캡처 그룹",
        "inspection.warning.can.be.removed": "<code>#ref</code>은(는) 중복됩니다",
        "inspection.warning.can.be.simplified": "<code>#ref</code>은(는) ''{0}''(으)로 간소화될 수 있습니다",
        "inspection.warning.consecutive.spaces.in.regexp": "정규식에 연속된 공백 {0}개",
        "inspection.warning.duplicate.branch.in.alternation": "교대(alternation)에 분기 중복",
        "inspection.warning.empty.branch.in.alternation": "교대(alternation)에 빈 분기",
        "inspection.warning.escaped.meta.character.0": "이스케이프된 메타 문자 <code>{0}</code>",
        "inspection.warning.group.back.reference.are.in.different.branches": "<code>{0}</code> 그룹과 이 루프백 참조는 다른 분기에 있습니다.",
        "inspection.warning.group.defined.after.back.reference": "<code>{0}</code> 그룹이 이 루프백 참조 이후에 정의되었습니다.",
        "inspection.warning.numeric.back.reference": "숫자 루프백 참조",
        "inspection.warning.octal.escape.code.ref.code.in.regexp": "정규식의 8진수 이스케이프 <code>#ref</code>",
        "inspection.warning.potential.exponential.backtracking": "기하급수적인 백트래킹 발생 가능성",
        "inspection.warning.redundant.character.escape.0.in.regexp": "정규식에 중복된 문자 이스케이프 <code>{0}</code>",
        "inspection.warning.redundant.class.element": "정규식에 중복된 ''{0}''",
        "inspection.warning.redundant.nested.character.class": "중복된 중첩 문자 클래스",
        "inspection.warning.single.character.alternation.in.regexp": "정규식의 단일 문자 교대(alternation)",
        "inspection.warning.unnecessary.non.capturing.group": "불필요한 비캡처 그룹 <code>{0}</code>",
        "inspection.tree.create.inspection": "정규식을 사용하여...",
        "inspection.tree.group.description": "도구 모음에서 + 버튼을 사용하여 새 정규식 검사를 만듭니다.<br>\n정규식 검사는 지정된 정규식과 일치하는 코드 스니펫을 강조 표시합니다. 그룹 참조(예: <code>$1</code>)를 포함할 수 있는 문자열 템플릿을 추가하여 퀵픽스를 제공할 수 있습니다.<br><br>\n<a href=\"action://regexp.profile.action.provider.add.group\">사용자 지정 정규식 검사 추가...</a>",
        "intention.family.name.replace": "바꾸기",
        "intention.name.check.regexp": "정규식 확인",
        "label.any": "아무거나",
        "label.regexp.patterns": "정규식 패턴:",
        "label.regexp": "정규식(&R):",
        "label.sample": "샘플(&S):",
        "no.description.provided.description": "제공된 설명이 없습니다.",
        "parse.error.category.shorthand.not.allowed.in.this.regular.expression.dialect": "이 정규식 방언에서는 범주 약어가 허용되지 않습니다.",
        "parse.error.character.class.expected": "문자 클래스가 필요합니다.",
        "parse.error.character.expected": "문자가 필요합니다.",
        "parse.error.character.or.mysql.character.name.expected": "문자 또는 MySQL 문자 이름이 필요합니다.",
        "parse.error.closing.brace.expected": "'}'가 필요합니다.",
        "parse.error.closing.brace.or.number.expected": "'}' 또는 숫자가 필요합니다.",
        "parse.error.comma.expected": "','가 필요합니다.",
        "parse.error.empty.property": "빈 속성",
        "parse.error.group.name.expected": "그룹 이름이 필요합니다.",
        "parse.error.group.name.or.number.expected": "그룹 이름 또는 번호가 필요합니다.",
        "parse.error.group.number.expected": "그룹 번호가 필요합니다.",
        "parse.error.illegal.category.shorthand": "잘못된 범주 약어",
        "parse.error.illegal.character.range": "잘못된 문자 범위",
        "parse.error.negating.a.property.not.allowed.in.this.regular.expression.dialect": "이 정규식 방언에서는 속성을 부정하는 것이 허용되지 않습니다.",
        "parse.error.number.expected": "숫자가 필요합니다."
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
