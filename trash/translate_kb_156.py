import json
from pathlib import Path

def update_missing_keys():
    file_path = Path("missing_translations/missing_keys_korean.json")

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    ko_dict = {
        "intention.name.make.function.volatile": "{0}을(를) {1, choice, 0#volatile|1#non-volatile}(으)로 만들기",
        "intention.name.change.type": "{1}의 {0, choice, 0#반환 |1#}타입을 ''{2}''{3}(으)로 변경",
        "intention.name.initialize": "{0} 초기화",
        "intention.name.remove.type.modifier": "{0}을(를) {1}(이)가 아닌 것으로 만들기",
        "intention.name.add.constructor.initializer": "{0}의 생성자 초기화 구문 추가",
        "intention.name.change.superclass": "{0}의 상위 클래스를 ''{1}''에서 ''{2}''(으)로 변경",
        "intention.name.add.last.parameter": "마지막 ''{0}'' 매개변수를 {1}에 추가",
        "intention.name.remove.last.parameter": "{1}에서 마지막 ''{0}'' 매개변수 제거",
        "intention.name.change.signature": "{0}의 시그니처를 ''{1}''(으)로 변경",
        "intention.dialog.message.existing.default.values.removed": "{0}의 매개변수에 대한 기존 기본값이 제거됩니다. 계속하시겠습니까?",
        "intention.family.name.remove.declaration": "{1, choice, 0#{0}|1#선언|2#이름} 제거",
        "intention.name.safe.delete": "{0} 안전하게 삭제",
        "intention.family.name.safe.delete": "안전하게 삭제",
        "intention.name.remove": "{0} 제거",
        "intention.family.name.remove": "{0} 제거",
        "intention.name.leave.initializer": "{0}하고 초기화 구문을 남겨둠",
        "intention.family.name.leave.initializer": "{0}하고 초기화 구문을 남겨둠",
        "intention.name.add.type.modifier": "{0}을(를) {1}(으)로 만들기",
        "intention.name.reuse.previous.declaration": "{0}의 이전 선언 재사용",
        "intention.name.rename": "{0} 이름 바꾸기",
        "intention.name.rename.reference": "참조 이름 바꾸기",
        "intention.name.predeclare.protocol.class": "{0, choice, 0#프로토콜|1#클래스|2#구조체} ''{1}'' 사전 선언",
        "intention.name.change.visibility": "{0}을(를) {1}(으)로 변경",
        "intention.name.cast.expression.to": "표현식을 ''{0}''(으)로 캐스트",
        "intention.family.name.extract.assignment": "선언 추출",
        "intention.name.class": "클래스",
        "intention.name.static": "정적",
        "intention.name.cpp.class": "C++ 클래스",
        "intention.name.create.new.category": "{1}을(를) 지정하여 {0}에 새 카테고리 생성",
        "intention.name.create.new": "새 {0} 생성",
        "intention.name.add.suffix": "접미사 추가",
        "intention.name.add.call.to.base.constructor": "''{0}''의 기본 생성자에 대한 호출 추가",
        "intention.name.make": "{0}을(를) {1}(으)로 만들기",
        "intention.name.choice.enable.disable": "{2}에 대해 ''{1}'' {0, choice, 0#활성화|1#비활성화}",
        "intention.name.add.parameters": "{0}에 매개변수 추가",
        "intention.name.make.class.method.instance.method": "''{0}''을(를) {1, choice, 0#클래스 메서드로 만들기|1#인스턴스 메서드로 만들기}",
        "intention.dialog.message.change.type.as.well": "{0}의 타입도 변경하시겠습니까?",
        "intention.family.name.convert.literal.type": "리터럴 타입 변환: '@' 추가",
        "intention.name.call": "{0} 호출",
        "intention.name.import.which": "''{1}'' {0, choice, 0#|1#심볼}",
        "intention.name.import": "{0} 가져오기",
        "intention.name.import.from": "{0}에서",
        "intention.import.popup.title": "가져올 심볼",
        "intention.import.command.name": "{0} 가져오기",
        "intention.name.make.function.virtual": "{0}::{1}을(를) {2, choice, 0#순수 가상으로 만들기|1#가상으로 만들기}",
        "intention.name.move.declaration": "{0}의 선언 이동{1}",
        "intention.family.name.remove.extra.initializers": "여분의 초기화 구문 제거",
        "intention.family.name.remove.initializer": "초기화 구문 제거",
        "intention.family.name.send.message": "''{0}'' 메시지 보내기",
        "intention.family.name.add.return.statement": "반환 구문 추가"
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
