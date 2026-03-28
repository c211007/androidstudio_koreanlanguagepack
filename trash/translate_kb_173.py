import json
from pathlib import Path

def update_missing_keys():
    file_path = Path("missing_translations/missing_keys_korean.json")

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    ko_dict = {
        "add.import": "가져오기 추가",
        "class.to.import.chooser.title": "가져올 클래스",
        "method.to.import.chooser.title": "가져올 메서드",
        "field.to.import.chooser.title": "가져올 필드",
        "access.static.via.class.reference.family": "클래스 참조를 사용하여 정적 멤버 액세스 한정",
        "access.static.via.class.reference.title": "클래스 참조를 사용하여 정적 멤버 액세스 한정",
        "access.static.method.via.class.reference.text": "클래스 ''{1}''에 대한 참조를 사용하여 정적 ''{0}'' 호출 한정",
        "access.static.field.via.class.reference.text": "클래스 ''{1}''에 대한 참조를 사용하여 정적 ''{0}'' 액세스 한정",
        "add.default.constructor.family": "기본 생성자 추가",
        "add.default.constructor.text": "{1}에 인수 없는 {0} 생성자 추가",
        "add.catch.clause.family": "catch 절에 예외 추가",
        "add.catch.clause.text": "'catch' 절 추가",
        "add.finally.block.family": "'finally' 블록 추가",
        "add.exception.to.throws.text": "메서드 시그니처에 {0, choice, 0#예외|2#예외} 추가",
        "add.exception.to.throws.family": "메서드 시그니처에 예외 추가",
        "add.exception.to.throws.header": "메서드 시그니처에 {0, choice, 0#예외|2#예외} 추가",
        "add.exception.to.throws.hierarchy": "계층 구조의 모든 메서드 변경",
        "add.exception.to.throws.only.this": "이 메서드만 변경",
        "add.exception.to.existing.catch.family": "기존 catch 절에 예외 추가",
        "add.exception.to.existing.catch.generic": "기존 catch 절에 예외 추가",
        "add.exception.to.existing.catch.replacement": "''{0}''을(를) 좀 더 일반적인 ''{1}''(으)로 대체",
        "add.exception.to.existing.catch.no.replacement": "''{0}''이(가) 포함된 catch에 ''{1}'' 추가",
        "add.exception.to.existing.catch.chooser.title": "Catch 블록 선택",
        "add.method.body.text": "메서드 본문 추가",
        "add.method.family": "메서드 추가",
        "add.method.text": "클래스 ''{1}''에 메서드 ''{0}'' 추가",
        "add.new.array.family": "누락된 new 표현식 추가",
        "add.new.array.text": "''new {0}[]'' 추가",
        "add.return.statement.text": "'return' 구문 추가",
        "add.runtime.exception.to.throws.text": "메서드 시그니처에 ''{0}'' 추가",
        "add.runtime.exception.to.throws.family": "메서드 시그니처에 런타임 예외 추가",
        "add.runtime.exception.to.throws.header": "메서드 시그니처에 런타임 예외 추가",
        "add.typecast.family": "타입 변환 추가",
        "add.typecast.text": "''{0}''(으)로 변환",
        "add.typecast.cast.text": "{1}을(를) ''{0}''(으)로 매핑",
        "add.typecast.convert.text": "{1}을(를) ''{0}''(으)로 변환",
        "fix.expression.role.qualifier": "한정자",
        "fix.expression.role.literal": "리터럴",
        "fix.expression.role.expression": "표현식",
        "fix.expression.role.argument": "인수",
        "fix.expression.role.nth.argument": "{0, choice, 1#1번째|2#2번째|3#3번째|4#{0,number}번째} 인수",
        "fix.expression.role.lambda.return": "람다 반환",
        "add.docTag.to.custom.tags": "사용자 지정 태그에 ''@{0}'' 추가",
        "add.docTag.to.custom.tags.preview": "이 검사에서 무시할 사용자 지정 태그 목록에 이 태그를 추가합니다.",
        "fix.javadoc.family": "Javadoc 수정",
        "adjust.package.family": "패키지 이름 조정",
        "adjust.package.text": "패키지 이름을 ''{0}''(으)로 설정",
        "bring.variable.to.scope.family": "변수를 범위 내로 가져오기",
        "bring.variable.to.scope.text": "''{0}''을(를) 범위 내로 가져오기",
        "add.type.arguments.text": "{0, choice, 1#1번째|2#2번째|3#3번째|4#{0,number}번째} 인수에 명시적 타입 인수 추가"
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
