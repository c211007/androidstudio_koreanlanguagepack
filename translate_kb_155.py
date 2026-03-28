import json
from pathlib import Path

def update_missing_keys():
    file_path = Path("missing_translations/missing_keys_korean.json")

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    ko_dict = {
        "intentions.create.implementation": "{0}의 구현 생성",
        "intentions.implement.method": "{0} 구현",
        "intentions.implement.accessor.methods": "접근자 메서드 구현",
        "intentions.implement.accessor.methods.for": "{0}에 대한 접근자 메서드 구현",
        "intentions.cast.expression": "표현식 캐스트",
        "intentions.introduce.typedef": "typedef 도입",
        "intentions.introduce.typedef.for.type": "{0} 타입에 대한 typedef 도입",
        "intentions.invert.if.condition": "'if' 조건 반전",
        "intentions.merge.if.else": "'if else' 병합",
        "intentions.merge.nested.ifs": "중첩된 'if' 병합",
        "intentions.add.braces.statement.family": "구문에 중괄호 추가",
        "intentions.add.braces.statement": "''{0}'' 구문에 중괄호 추가",
        "intentions.remove.braces.statement.family": "구문에서 중괄호 제거",
        "intentions.remove.braces.statement": "''{0}'' 구문에서 중괄호 제거",
        "intentions.move.instance.variables": "구현으로 인스턴스 변수 이동",
        "intentions.move.to.interface": "인터페이스로 이동",
        "intentions.move.to.private.category": "프라이빗 카테고리로 이동",
        "intentions.import.predeclare.symbol": "심볼 가져오기/사전 선언",
        "intentions.release.variables": "변수 해제",
        "intentions.remove.suppression": "메시지 표시 안 함 삭제",
        "intentions.remove.subj": "''{0}'' 제거",
        "intentions.remove.unnecessary.parentheses": "불필요한 괄호 제거",
        "intentions.rename.reference": "참조 이름 바꾸기",
        "intentions.rename.symbol": "심볼 이름 바꾸기",
        "intentions.replace.type.with.auto": "타입을 'auto'로 바꾸기",
        "intentions.reuse.declaration": "선언 재사용",
        "intentions.change.superclass": "상위 클래스 변경",
        "intentions.split.declaration": "선언과 할당으로 분할",
        "intentions.split.function": "함수를 선언과 정의로 분할",
        "intentions.split.into.separate.declarations": "별도의 선언으로 분할",
        "intentions.suppress.for": "{0}에 대해 메시지 표시 안 함",
        "intentions.suppress.option.for": "{1}에 대해 \"{0}\" 메시지 표시 안 함",
        "intentions.suppress.for.statement": "구문에 대해 메시지 표시 안 함",
        "intentions.suppress.for.method": "메서드/함수에 대해 메시지 표시 안 함",
        "intentions.suppress.for.file": "파일에 대해 메시지 표시 안 함",
        "intentions.suppress.all.for.file": "파일의 모든 {0} 진단 메시지 표시 안 함",
        "intentions.surround.with.if.responds": "\"if ([ respondsToSelector: ])\"로 래핑",
        "intentions.switch.property.dot.method": "'.'과 메서드 표기법 전환",
        "intentions.switch.to.getter.notation": "getter 메서드 표기법으로 전환",
        "intentions.switch.to.setter.notation": "setter 메서드 표기법으로 전환",
        "intentions.switch.to.dot.notation": "'.' 표기법으로 전환",
        "intentions.synthesize.property": "프로퍼티 synthesize",
        "intentions.wrap.with.stringFormat": "'stringWithFormat'으로 래핑",
        "intentions.insert.cast.use.modern": "C++ 캐스트 연산자 사용",
        "intentions.split.function.progress.text": "정의 위치를 확인하는 중\\u2026",
        "intentions.change.function.const.action": "const 한정자 변경",
        "intentions.change.function.volatile.action": "volatile 한정자 변경",
        "intentions.change.gcc.attribute.action": "''{0}'' 특성 변경",
        "intentions.change.method.signature.add.parameters": "매개변수 추가",
        "intentions.change.property.attribute.action": "프로퍼티 특성 변경"
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
