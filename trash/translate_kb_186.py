import json
from pathlib import Path

def update_missing_keys():
    file_path = Path("missing_translations/missing_keys_korean.json")

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    ko_dict = {
        "parse.error.opening.brace.expected": "'{'가 필요합니다.",
        "parse.error.opening.brace.or.category.shorthand.expected": "'{' 또는 범주 약어가 필요합니다.",
        "parse.error.pattern.expected": "패턴이 필요합니다.",
        "parse.error.posix.character.class.name.expected": "POSIX 문자 클래스 이름이 필요합니다.",
        "parse.error.property.name.expected": "속성 이름이 필요합니다.",
        "parse.error.property.value.expected": "속성 값이 필요합니다.",
        "parse.error.unclosed.character.class": "닫히지 않은 문자 클래스",
        "parse.error.unclosed.group.name": "닫히지 않은 그룹 이름",
        "parse.error.unclosed.group.reference": "닫히지 않은 그룹 참조",
        "parse.error.unclosed.group": "')'가 필요합니다.",
        "parse.error.unclosed.mysql.character.equivalence.class": "닫히지 않은 MySQL 문자 동등 클래스",
        "parse.error.unclosed.mysql.character.expression": "닫히지 않은 MySQL 문자 표현식",
        "parse.error.unclosed.options.group": "닫히지 않은 옵션 그룹",
        "parse.error.unclosed.posix.bracket.expression": "닫히지 않은 POSIX 대괄호 표현식",
        "parse.error.unclosed.property": "닫히지 않은 속성",
        "parse.error.unicode.character.name.expected": "유니코드 문자 이름이 필요합니다.",
        "parse.error.unmatched.closing.bracket": "일치하지 않는 닫는 ''{0}''",
        "regexp.dialog.language": "언어(&L):",
        "regexp.dialog.regexp.flags": "정규식 플래그",
        "regexp.dialog.flag.unix.lines": "Unix 줄바꿈",
        "regexp.dialog.flag.unix.lines.description": "<code>.</code>, <code>^</code>, <code>$</code>의 동작에서 <code>\\\\n</code> 줄 종결자만 인식됩니다.",
        "regexp.dialog.flag.case.insensitive": "대소문자 무시",
        "regexp.dialog.flag.case.insensitive.description": "기본적으로 대소문자 무시는 US-ASCII 문자 집합에 대해서만 지원됩니다. \n  유니코드를 인식하는 대소문자 무시 일치를 위해 Unicode 대소문자를 활성화하세요.",
        "regexp.dialog.flag.comments": "주석",
        "regexp.dialog.flag.comments.description": "일치 시 공백 및 <code>#</code> 주석을 줄 끝까지 무시합니다.",
        "regexp.dialog.flag.multiline": "여러 줄",
        "regexp.dialog.flag.multiline.description": "여러 줄 모드에서 <code>^</code> 및 <code>$</code>는 줄의 시작과 끝과 일치합니다.\n기본적으로 전체 파일의 시작과 끝과만 일치합니다.",
        "regexp.dialog.flag.literal": "리터럴",
        "regexp.dialog.flag.literal.description": "패턴은 리터럴 문자의 시퀀스로 처리됩니다. 메타 문자 및 이스케이프 시퀀스는 특별한 의미를 갖지 않습니다.",
        "regexp.dialog.flag.dotall": "Dotall",
        "regexp.dialog.flag.dotall.description": "Dotall 모드에서 <code>.</code>는 줄 바꿈 문자를 포함한 모든 문자와 일치합니다.\n  기본적으로 줄 바꿈 문자와는 일치하지 않습니다.",
        "regexp.dialog.flag.unicode.case": "유니코드 대소문자",
        "regexp.dialog.flag.unicode.case.description": "유니코드를 인식하는 대소문자를 구분하지 않는 일치입니다.",
        "regexp.dialog.flag.canonical.equivalence": "표준 동등성",
        "regexp.dialog.flag.canonical.equivalence.description": "문자는 일치 전에 유니코드 정규화된 형식으로 변환됩니다.",
        "regexp.dialog.flag.unicode.character.class": "유니코드 문자 클래스",
        "regexp.dialog.flag.unicode.character.class.description": "유니코드를 지원하는 사전 정의된 문자 클래스 및 POSIX 문자 클래스 사용.",
        "regexp.dialog.replace.template": "교체:",
        "regexp.dialog.search.template": "검색 정규식:",
        "regexp.dialog.title": "정규식",
        "surrounder.atomic.group.pattern": "원자적 그룹 (?:패턴)",
        "surrounder.capturing.group.pattern": "캡처 그룹 (패턴)",
        "surrounder.negative.lookahead.pattern": "부정형 전방 탐색 (?!패턴)",
        "surrounder.negative.lookbehind.pattern": "부정형 후방 탐색 (?<!패턴)",
        "surrounder.non.capturing.group.pattern": "비캡처 그룹 (?:패턴)",
        "surrounder.positive.lookahead.pattern": "긍정형 전방 탐색 (?=패턴)",
        "surrounder.positive.lookbehind.pattern": "긍정형 후방 탐색 (?<=패턴)",
        "tooltip.bad.pattern": "잘못된 정규 표현식 패턴",
        "tooltip.found.multiple": "예제에서 표현식을 {0}번 발견했습니다.",
        "tooltip.found": "예제에서 표현식을 발견했습니다."
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
