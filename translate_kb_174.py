import json
from pathlib import Path

def update_missing_keys():
    file_path = Path("missing_translations/missing_keys_korean.json")

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    ko_dict = {
        "add.type.arguments.single.argument.text": "명시적 타입 인수 추가",
        "change.class.signature.text": "''{0}''의 시그니처를 ''{1}''과(와) 일치하도록 변경",
        "change.class.signature.family": "클래스 시그니처 변경",
        "uidesigner.change.bound.field.type": "바인딩된 필드 타입 변경",
        "cannot.change.field.exception": "필드 ''{0}'' 타입을 변경할 수 없습니다.\\n이유: {1}",
        "exchange.extends.implements.keyword": "''{0} {2}''을(를) ''{1} {2}''(으)로 변경",
        "uidesigner.change.gui.component.type": "GUI 구성 요소 타입 변경",
        "change.method.signature.from.usage.family": "사용 위치에서 메서드 시그니처 변경",
        "change.method.signature.from.usage.text": "''{0}''의 시그니처를 ''{1}({2})''(으)로 변경",
        "add.parameter.from.usage.text": "''{0}''을(를) {2} ''{3}''의 {1,number,ordinal} {2}(으)로 추가",
        "remove.parameter.from.usage.text": "{2} ''{3}''에서 {0,number,ordinal} {1} 제거",
        "change.parameter.from.usage.text": "{2} ''{3}''의 {0,number,ordinal} {1}을(를) ''{4}''에서 ''{5}''(으)로 변경",
        "searching.for.usages.progress.title": "사용 검색 중...",
        "create.class.from.new.family": "New에서 클래스 만들기",
        "create.class.from.usage.family": "사용 위치에서 클래스 만들기",
        "create.class.from.usage.text": "{0} ''{1}'' 만들기",
        "create.inner.class.from.usage.text": "내부 {0} ''{1}'' 만들기",
        "create.element.in.class": "''{2}''에 {0} ''{1}'' 만들기",
        "create.constant.from.usage.family": "사용 위치에서 상수 만들기",
        "create.constructor.from.new.family": "New에서 생성자 만들기",
        "create.constructor.from.new.text": "생성자 만들기",
        "create.constructor.from.super.call.family": "super() 호출에서 생성자 만들기",
        "create.constructor.from.this.call.family": "this() 호출에서 생성자 만들기",
        "create.constructor.family": "생성자 만들기",
        "create.constructor.text": "''{0}''에 생성자 만들기",
        "create.constructor.body.command": "생성자 본문 만들기",
        "create.constructor.matching.super": "super와 일치하는 생성자 만들기",
        "super.class.constructors.chooser.title": "슈퍼 클래스 생성자 선택",
        "create.field.from.usage.family": "사용 위치에서 필드 만들기",
        "target.class.chooser.title": "대상 클래스 선택",
        "target.method.chooser.title": "대상 메서드 선택",
        "new.method.body.template.error.text": "\"새 메서드 본문\" 템플릿을 수정하세요.",
        "new.method.body.template.error.title": "파일 템플릿 오류",
        "cannot.create.java.file.error.text": "{1}에 {0}.java를 만들 수 없습니다: {2}",
        "cannot.create.java.file.error.title": "파일 생성 실패",
        "cannot.create.java.package.error.text": "{1}에 {0}을(를) 만들 수 없습니다: {2}",
        "cannot.create.java.package.error.title": "패키지 생성 실패",
        "create.accessor.for.unused.field.family": "사용하지 않는 필드에 대한 접근자 만들기",
        "create.getter.for.field": "''{0}''에 대한 getter 만들기",
        "create.setter.for.field": "''{0}''에 대한 setter 만들기",
        "create.getter.and.setter.for.field": "''{0}''에 대한 getter 및 setter 만들기",
        "create.local.from.usage.family": "사용 위치에서 로컬 만들기",
        "create.local.from.instanceof.usage.family": "instanceof 사용 위치에서 로컬 변수 만들기",
        "create.local.from.instanceof.usage.text": "''({0}){1}'' 선언 삽입",
        "create.member.from.usage.family": "사용 위치에서 멤버 만들기",
        "create.method.from.usage.family": "사용 위치에서 메서드 만들기",
        "create.method.body": "메서드 본문 만들기",
        "create.method.from.usage.text": "메서드 ''{0}'' 만들기",
        "create.type.parameter.from.usage.family": "사용 위치에서 타입 매개변수 만들기",
        "create.type.parameter.from.usage.text": "타입 매개변수 ''{0}'' 만들기"
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
