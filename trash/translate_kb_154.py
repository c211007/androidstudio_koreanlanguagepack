import json
from pathlib import Path

def update_missing_keys():
    file_path = Path("missing_translations/missing_keys_korean.json")

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    ko_dict = {
        "intentions.add.initializer": "초기화 구문 추가",
        "intentions.add.parameters.to.constructor": "''{0}''을(를) 생성자의 매개변수로 추가",
        "intentions.add.parameters.to.constructor.family": "필드를 생성자의 매개변수로 추가",
        "intentions.add.parameter.initWith": "'initWith...'의 매개변수로 추가",
        "intentions.check.raw.string": "원시 문자열 확인",
        "intentions.add.super.constructor.call": "누락된 기본 생성자 호출 추가",
        "intentions.add.super.protocol.by.class": "클래스에 의한 프로토콜 채택",
        "intentions.add.super.protocol.by.private.category": "프라이빗 카테고리에 의한 프로토콜 채택",
        "intentions.add.modifier": "''{0}'' 추가",
        "intentions.change.function.signature": "함수 시그니처 변경",
        "intentions.change.type.capitalized": "타입 변경",
        "intentions.change.type": "타입 변경",
        "intentions.change.visibility": "가시성 변경",
        "intentions.convert.id.to.instance": "'id' 반환 타입을 'instancetype'으로 변경",
        "intentions.replace.if.else.with.ternary": "'if else'를 '?:'로 바꾸기",
        "intentions.replace.ternary.with.if.else": "'?:'를 'if else'로 바꾸기",
        "intentions.convert.objc.literal": "Objective-C 리터럴로 전환",
        "intentions.convert.to.instance.variable": "인스턴스 변수로 변환",
        "intentions.convert.to.property": "프로퍼티로 변환",
        "intentions.convert.type": "타입 변환",
        "intentions.create.matching.constructor": "기본 클래스와 일치하는 생성자 생성",
        "intentions.create.matching.constructor.in": "{0}에 기본 생성자 생성",
        "intentions.create.new.matching.constructor": "{0}에 기본 클래스와 일치하는 새 생성자 생성",
        "intentions.create.new.constructor": "새 생성자 ''{0}()'' 생성",
        "intentions.predeclare.function": "{0} 사전 선언",
        "intentions.create.interface": "{0}의 인터페이스 생성",
        "intentions.create.missing.default.switch.case": "누락된 기본 케이스 생성",
        "intentions.create.missing.switch.cases": "누락된 switch 케이스 생성",
        "intentions.declare.method.in.interface": "인터페이스에 메서드 선언",
        "intentions.declare.method.in.private.category": "프라이빗 카테고리에 메서드 선언",
        "intentions.declare.method.in": "{0}에 메서드 선언",
        "intentions.declare.property.as.readwrite": "프라이빗 카테고리에서 프로퍼티를 'readwrite'로 선언",
        "intentions.replace.and.with.or": "'&&'를 '||'로 바꾸기",
        "intentions.replace.or.with.and": "'||'를 '&&'로 바꾸기",
        "intentions.deMorgan.law": "드 모르간의 법칙",
        "intentions.declare.member.in": "선언 위치: ",
        "intentions.remove.private.category.message": "빈 프라이빗 카테고리를 제거하시겠습니까?",
        "intentions.remove.private.category.title": "프라이빗 카테고리 제거",
        "intentions.extract.category": "이 클래스의 카테고리 추출",
        "intentions.extract.if": "'if' 추출",
        "intentions.extract.if.with.text": "''if ({0})'' 추출",
        "intentions.extract.private.category": "이 클래스의 프라이빗 카테고리 추출",
        "intentions.extract.protocol": "이 클래스의 프로토콜 추출",
        "intentions.extract.super.class": "상위 클래스 추출",
        "intentions.extract.super.protocol": "상위 프로토콜 추출",
        "intentions.flip.operator": "{0} 뒤집기",
        "intentions.flip.operator.to": "{0}을(를) {1}(으)로 뒤집기",
        "intentions.flip.binary.operation": "이항 연산 뒤집기",
        "intentions.generate.property": "프로퍼티 생성",
        "intentions.implement.required.methods": "인터페이스 ''{0}''의 필수 메서드 구현"
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
