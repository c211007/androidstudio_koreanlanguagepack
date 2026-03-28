import json
from pathlib import Path

def update_missing_keys():
    file_path = Path("missing_translations/missing_keys_korean.json")

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    ko_dict = {
        "inspection.name.unconstrained.variable.type": "제한되지 않은 변수 타입",
        "no.suggestions.for.properties.of.class": "{0} 클래스의 프로퍼티에 대한 제안이 없습니다.",
        "no.suggestions.for.members": "{0}의 멤버에 대한 제안이 없습니다.",
        "quick.fix.place.parentheses.around": "다음을 괄호로 묶기",
        "quick.fix.send.release.message.instead.dealloc": "\"dealloc\" 대신 \"release\" 메시지 보내기",
        "quick.fix.append.nil.argument": "\"nil\" 인수 추가",
        "quick.fix.remove.extra.declarators": "여분의 선언자 제거",
        "quick.fix.remove.statement": "구문 제거",
        "quick.fix.remove.pure.specifier": "순수 지정자 제거",
        "quick.fix.change.pure.specifier": "순수 지정자를 '= 0'으로 변경",
        "quick.fix.remove.from.base.classes.list": "기본 클래스 목록에서 ''{0}'' 제거",
        "quick.fix.remove.redundant.cast": "중복된 캐스트 제거",
        "quick.fix.remove.initializer": "초기화 구문 제거",
        "quick.fix.insert.keyword": "''{0}'' 삽입",
        "quick.fix.remove.property": "프로퍼티 제거",
        "quick.fix.remove.declaration": "선언 제거",
        "inspection.message.unterminated.string.literal": "종결되지 않은 문자열 리터럴",
        "inspection.message.invalid.suffix.on.raw.string": "원시 문자열의 유효하지 않은 접미사",
        "quick.fix.remove.attribute": "속성 제거",
        "quick.fix.remove.useless.import": "쓸모없는 가져오기 제거",
        "quick.fix.remove.useless.include": "쓸모없는 포함 제거",
        "quick.fix.optimize.imports": "가져오기 최적화",
        "quick.fix.optimize.includes": "포함 최적화",
        "quick.fix.change.format.specifier": "포맷 지정자 변경",
        "quick.fix.remove.arguments": "인수 제거",
        "quick.fix.copy.superclass.from.interface": "인터페이스에서 상위 클래스 복사",
        "quick.fix.copy.superclass.to.interface": "상위 클래스를 인터페이스로 복사",
        "quick.fix.remove.superclass": "상위 클래스 제거",
        "quick.fix.remove.user.defined.getter.method": "사용자 정의 getter 메서드 제거",
        "quick.fix.remove.user.defined.setter.method": "사용자 정의 setter 메서드 제거",
        "quick.fix.remove.superclass.reference": "상위 클래스 참조 제거",
        "quick.fix.remove.instance.variable.list": "인스턴스 변수 목록 제거",
        "quick.fix.remove.protocols.list": "프로토콜 목록 제거",
        "quick.fix.remove.method.body": "메서드 본문 제거",
        "quick.fix.remove.synthesize.dynamic.statement": "'@synthesize'/'@dynamic' 구문 제거",
        "quick.fix.remove.synthesize.statement": "'@synthesize' 구문 제거",
        "quick.fix.remove.accessor": "접근자 제거",
        "inspection.message.error.after.macro.substitution": "매크로 대체 후 오류: ",
        "inspection.message.was.not.declared.in": "{0}이(가) {1}에 선언되지 않았습니다.",
        "inspection.message.hides.non.virtual.function": "{0}이(가) {1}의 가상이 아닌 함수를 숨깁니다.",
        "intention.name.make.function.const": "{0}을(를) {1, choice, 0#const|1#non-const}(으)로 만들기",
        "quick.fix.make_default": "{0}을(를) 기본값으로 설정",
        "quick.fix.add_return_statement": "반환 구문 추가",
        "intentions.group": "C 및 C++",
        "intentions.group.definition": "C 및 C++/정의",
        "intentions.group.declarations": "C 및 C++/선언",
        "intentions.group.operators": "C 및 C++/연산자",
        "intentions.group.control.flow": "C 및 C++/제어 흐름",
        "intentions.group.objc": "Objective-C",
        "intentions.add.constructor.initializer.for.field": "필드의 생성자 초기화 구문 추가"
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
