import json
from pathlib import Path

def update_missing_keys():
    file_path = Path("missing_translations/missing_keys_korean.json")

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    ko_dict = {
        "file.0.already.exists.in.the.project": "''{0}'' 파일이 프로젝트에 이미 존재합니다.",
        "refactoring.rename.0.already.exists.in.1": "{1}에 {0}이(가) 이미 존재합니다.",
        "refactoring.rename.0.already.exists.in.the.scope": "해당 범위에 {0}이(가) 이미 존재합니다.",
        "dialog.message.name.invalid": "{0}의 이름이 잘못되었습니다.",
        "dialog.message.return.type.invalid": "{0}의 반환 타입이 잘못되었습니다.",
        "dialog.message.no.selector.parts.for": "{0}에 대한 선택자 부분이 없습니다.",
        "dialog.message.containing.class.invalid": "포함하는 클래스 \"{0}\"이(가) 잘못되었습니다.",
        "dialog.message.containing.class.outside.project": "포함하는 클래스 \"{0}\"이(가) 프로젝트 외부에 있습니다.",
        "dialog.message.selector.part.invalid": "선택자 부분 ''{0}''이(가) 잘못되었습니다.",
        "dialog.message.parameter.name.invalid": "매개변수 이름 ''{0}''이(가) 잘못되었습니다.",
        "dialog.message.paramer.default.value.invalid": "''{0}''은(는) 표현식이 아닙니다.",
        "selected.expression.should.be.inside.a.block.statement": "선택한 표현식은 블록 구문 내부에 있어야 합니다.",
        "can.t.refactor.the.compound.initializer": "복합 초기화 구문을 리팩터링할 수 없습니다.",
        "cannot.determine.type.of.the.selected.expression": "선택한 표현식의 타입을 결정할 수 없습니다.",
        "cannot.perform.refactoring.selected.expression.has.void.type": "선택한 표현식이 void 타입이므로 리팩터링을 수행할 수 없습니다.",
        "selected.expression.cannot.be.a.constant.initializer": "선택한 표현식은 상수 초기화 구문일 수 없습니다.",
        "selected.expression.should.be.inside.an.instance.method": "선택한 표현식은 인스턴스 메서드 내부에 있어야 합니다.",
        "selected.expression.should.be.inside.a.function.or.method": "선택한 표현식은 함수 또는 메서드 내부에 있어야 합니다.",
        "can.t.introduce.parameter.to.a.function.with.default.parameter.values": "기본 매개변수 값이 있는 함수에 매개변수를 도입할 수 없습니다.",
        "selected.expression.should.be.inside.an.instance.method1": "선택한 표현식은 인스턴스 메서드 내부에 있어야 합니다.",
        "property.inplace.introducer.label.semantics": "의미론",
        "declaration.must.have.one.declarator.to.introduce.the.type": "선언은 타입을 도입할 선언자가 하나 있어야 합니다.",
        "namespace.qualifier.should.be.resolved.to.the.class": "네임스페이스 한정자는 클래스로 해석되어야 합니다.",
        "the.type.is.empty": "타입이 비어 있습니다.",
        "can.t.extract.type.of.0.definition": "추출할 수 없습니다: {0} 정의의 타입",
        "dialog.message.can.t.move.to.itself": "''{0}''을(를) 자기 자신으로 이동할 수 없습니다.",
        "dialog.message.can.t.copy.to.itself": "''{0}''을(를) 자기 자신으로 복사할 수 없습니다.",
        "dialog.message.directory.already.exists.at": "''{0}''에 디렉터리가 이미 존재합니다.",
        "dialog.message.file.already.exists.at": "''{0}''에 파일이 이미 존재합니다.",
        "dialog.message.file.already.exists": "파일이 이미 존재합니다.",
        "extract.dialog.button.extract": "추출(&R)",
        "escalate.visibility.member.column": "멤버",
        "escalate.visibility.current.visibility.column": "현재 가시성",
        "escalate.visibility.required.visibility.column": "필요한 가시성",
        "push.down.inheritor.column": "상속자",
        "text.parameter.initializer.not.available.in": "{0}에서 매개변수 초기화 구문을 사용할 수 없습니다: {1}.",
        "cannot.inline.function.type": "함수 타입을 인라인화할 수 없습니다.",
        "cannot.inline.constructor.expression": "생성자 표현식을 인라인화할 수 없습니다.",
        "can.t.inline.definition": "인라인화할 수 없습니다: {0} 정의",
        "cannot.inline.the.macro.inside.another.macro.definition": "다른 매크로 정의 내부의 매크로를 인라인화할 수 없습니다.",
        "cannot.find.the.method.function": "메서드/함수를 찾을 수 없습니다.",
        "there.are.usages.in.other.blocks": "다른 블록에 사용이 있습니다.",
        "0.was.not.initialized": "{0}이(가) 초기화되지 않았습니다.",
        "there.are.several.definitions.of": "{0}의 정의가 여러 개 있습니다.",
        "the.address.of.is.taken": "{0}의 주소를 얻었습니다.",
        "element.is.written.in.the.block": "{0}이(가) 블록에 작성되었습니다.",
        "several.definitions.of.0": "{0}의 정의가 여러 개 있습니다.",
        "element.is.accessed.for.writing": "{0}이(가) 쓰기 위해 액세스되었습니다.",
        "cannot.inline.usages.inside.the.macro.substitutions": "대체된 매크로 내부의 사용을 인라인화할 수 없습니다.",
        "element.has.inheritor": "{0}에 상속자 {1, choice, 0#메서드|1#함수}가 있습니다."
    }

    filename = "OCRefactoringBundle.properties"
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
