import json
from pathlib import Path

def update_missing_keys():
    file_path = Path("missing_translations/missing_keys_korean.json")

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    ko_dict = {
        "module.info.add.uses.name": "module-info.java에 ''uses {0}'' 지시문 추가",
        "collection.to.array.text": "''.toArray({0})'' 변환 적용",
        "collection.to.array.family.name": "'.toArray()' 변환 적용",
        "insert.sam.method.call.fix.name": "함수형 인터페이스 메서드를 호출하기 위해 ''.{0}'' 삽입",
        "insert.sam.method.call.fix.family.name": "단일 추상 메서드 호출 삽입",
        "wrap.with.adapter.call.family.name": "호출 또는 새 객체를 사용하여 조정",
        "wrap.with.adapter.text": "''{0}''을(를) 사용하여 조정",
        "wrap.with.adapter.text.role": "''{0}''을(를) 사용하여 {1} 조정",
        "wrap.with.adapter.parameter.single.text": "''{0}''을(를) 사용하여 인수 조정",
        "wrap.with.adapter.parameter.multiple.text": "''{1}''을(를) 사용하여 {0, choice, 1#1번째|2#2번째|3#3번째|4#{0,number}번째} 인수 조정",
        "java.9.merge.module.statements.fix.family.name": "다른 ''{0}'' 지시문과 병합",
        "java.9.merge.module.statements.fix.name": "다른 ''{0} {1}'' 지시문과 병합",
        "adjust.method.accepting.functional.expression.fix.family.name": "함수형 표현식을 허용하는 메서드 조정",
        "adjust.method.accepting.functional.expression.fix.text": "''{0}()''을(를) ''{1}()''(으)로 교체",
        "add.compiler.option.fix.name": "모듈 컴파일러 옵션에 ''{0}'' 추가",
        "create.service.implementation.fix.family.name": "서비스 구현 클래스 만들기",
        "create.service.implementation.fix.name": "클래스 ''{0}'' 만들기",
        "create.service.interface.fix.family.name": "서비스 만들기",
        "create.service.interface.fix.name": "서비스 ''{0}'' 만들기",
        "convert.variable.to.field.in.anonymous.class.fix.name": "익명 객체 내로 ''{0}'' 이동",
        "change.method.parameters.text": "메서드 매개변수를 ''{0}''(으)로 변경",
        "change.method.parameters.family": "메서드 매개변수 변경",
        "change.type.family": "타입 변경",
        "change.type.text": "타입을 ''{0}''(으)로 변경",
        "add.default.branch.to.variable.initializing.switch.fix.name": "''{0}''을(를) 초기화하는 ''switch'' 구문에 ''default'' 분기 추가",
        "insert.empty.parenthesis": "'()' 삽입",
        "remove.parameter.list": "매개변수 목록 제거",
        "convert.primitive.to.boxed.type": "원시 타입을 박스형 타입으로 변환",
        "choose.class.to.move.popup.title": "이동할 클래스 선택",
        "move.0.in.1": "''{1}''에서 ''{0}'' 이동...",
        "move.0.from.module.1.to.2": "모듈 ''{1}''에서 ''{2}''(으)로 ''{0}'' 이동",
        "add.0.to.classpath": "클래스 경로에 ''{0}'' 추가",
        "iterate.iterable": "반복",
        "choose.fields.to.generate.constructor.parameters.for": "생성자 매개변수를 생성할 필드 선택",
        "choose.constructors.to.add.parameter.to": "매개변수를 추가할 생성자 선택",
        "add.constructor.parameters": "생성자 매개변수 추가",
        "add.annotation.attribute.name.family.name": "어노테이션 속성 이름 추가",
        "add.annotation.attribute.name": "''{0}='' 추가",
        "replace.with.getter.setter": "getter/setter로 교체",
        "replace.with.getter": "getter로 교체",
        "replace.with.setter": "setter로 교체",
        "replace.import.module.fix.text": "'import module'을 단일 클래스 가져오기로 교체",
        "wrap.with.block": "블록으로 래핑",
        "create.block": "블록 생성",
        "replace.for.each.loop.with.iterator.for.loop": "'for each' 루프를 반복자 'for' 루프로 교체",
        "surround.annotation.parameter.value.with.quotes": "어노테이션 매개변수 값을 따옴표로 묶기",
        "surround.with.array.initialization": "배열 초기화로 둘러싸기",
        "create.service.implementation": "서비스 구현 클래스 만들기",
        "create.service": "서비스 만들기",
        "choose.default.value.parameters.popup.title": "기본값 매개변수 선택"
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
