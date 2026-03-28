import json
from pathlib import Path

def update_missing_keys():
    file_path = Path("missing_translations/missing_keys_korean.json")

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    ko_dict = {
        "create.type.parameter.from.usage.chooser.title": "타입 매개변수 추가 위치",
        "create.parameter.from.usage.family": "사용 위치에서 매개변수 만들기",
        "create.property.from.usage.family": "사용 위치에서 속성 만들기",
        "create.property.from.usage.text": "속성 ''{0}'' 만들기",
        "create.property.from.usage.full.text": "''{1}''에 속성 ''{0}'' 만들기",
        "create.read.only.property.from.usage.text": "읽기 전용 속성 ''{0}'' 만들기",
        "create.read.only.property.from.usage.full.text": "''{1}''에 읽기 전용 속성 ''{0}'' 만들기",
        "create.write.only.property.from.usage.text": "쓰기 전용 속성 ''{0}'' 만들기",
        "create.write.only.property.from.usage.full.text": "''{1}''에 쓰기 전용 속성 ''{0}'' 만들기",
        "create.getter": "Getter 만들기",
        "create.setter": "Setter 만들기",
        "create.getter.setter": "Getter/Setter 만들기",
        "create.annotation.family": "선언에 어노테이션 추가",
        "create.annotation.text": "@{0}(으)로 어노테이션 추가",
        "defer.final.assignment.with.temp.family": "임시 변수를 사용하여 최종 할당 지연",
        "defer.final.assignment.with.temp.text": "임시 변수를 사용하여 ''{0}''에 대한 할당 지연",
        "delete.catch.family": "catch 삭제",
        "delete.catch.text": "''{0}''에 대한 catch 삭제",
        "delete.body.text": "메서드 본문 삭제",
        "enable.optimize.imports.on.the.fly": "'설정 | 편집기 | 일반 | 자동 가져오기 | 즉시 가져오기 최적화' 사용",
        "implement.methods.fix": "메서드 구현",
        "import.class.fix": "클래스 가져오기",
        "replace.type.new.expression.family.name": "생성자 호출 타입 교체",
        "replace.type.new.expression.name": "생성자 호출 타입을 ''{0}''(으)로 교체",
        "replace.type.variable.name": "변수 타입을 ''{0}''(으)로 교체",
        "insert.new.fix": "new 삽입",
        "insert.super.constructor.call.family": "기본 클래스 생성자 호출 삽입",
        "make.class.an.interface.family": "클래스를 인터페이스로 만들기",
        "make.class.an.interface.text": "''{0}''을(를) 인터페이스로 만들기",
        "make.interface.an.class.text": "''{0}''을(를) 클래스로 만들기",
        "make.vararg.parameter.last.family": "vararg 매개변수를 마지막으로 만들기",
        "make.vararg.parameter.last.text": "''{0}''을(를) 목록의 끝으로 이동하기",
        "make.receiver.parameter.first.family": "수신자 매개변수를 첫 번째로 만들기",
        "make.receiver.parameter.first.text": "'this'를 목록의 시작 부분으로 이동하기",
        "fix.parameter.type.family": "매개변수 타입 수정",
        "fix.parameter.type.text": "여기서 ''{0}''이(가) ''{1}'' 타입의 매개변수를 사용하도록 만들기",
        "fix.return.type.family": "반환 타입 수정",
        "fix.return.type.or.predecessor.text": "''{0}''이(가) ''{1}'' 또는 조상을 반환하게 만들기",
        "fix.return.type.text": "''{0}''이(가) ''{1}''을(를) 반환하게 만들기",
        "fix.throws.list.family": "throws 목록 수정",
        "fix.throws.list.add.exception": "''{1}'' throws 목록에 ''{0}'' 추가",
        "fix.throws.list.remove.exception": "''{1}'' throws 목록에서 ''{0}'' 제거",
        "fix.modifiers.family": "한정자 수정",
        "anonymous.class.presentation": "{0}에서 파생된 익명 클래스",
        "class.initializer.presentation": "{0} 클래스 초기화 구문",
        "add.modifier.fix": "''{0}'' {1}(으)로 만들기",
        "remove.modifier.fix": "''{0}'' {1} 되지 않도록 만들기",
        "remove.one.modifier.fix": "''{0}'' 한정자 제거",
        "add.modifier.fix.family": "{0}(으)로 만들기",
        "remove.modifier.fix.family": "{0} 되지 않도록 만들기"
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
