import json
from pathlib import Path

def update_missing_keys():
    file_path = Path("missing_translations/missing_keys_korean.json")

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    ko_dict = {
        "dialog.message.variable.must.be.const": "\"{0}\" 변수는 const여야 합니다.",
        "dialog.message.cannot.find.method.function": "메서드/함수를 찾을 수 없습니다.",
        "dialog.message.cannot.inline.parameters.blocks": "블록의 매개변수를 인라인화할 수 없습니다.",
        "dialog.message.cannot.inline.parameters.lambdas": "람다의 매개변수를 인라인화할 수 없습니다.",
        "dialog.message.several.call.sites.with.different.parameter.initializers": "다른 매개변수 초기화 구문을 가진 호출 사이트가 여러 개 있습니다.",
        "dialog.message.there.are.no.usages": "{0}의 사용이 없습니다.",
        "dialog.message.cannot.inline.blocks": "블록을 인라인화할 수 없습니다.",
        "dialog.message.cannot.inline.protocol.method": "프로토콜 메서드를 인라인화할 수 없습니다.",
        "dialog.message.interface.was.not.implemented": "{0} 인터페이스가 구현되지 않았습니다.",
        "dialog.message.cannot.inline.with.empty.body": "본문이 빈 {0}을(를) 인라인화할 수 없습니다.",
        "dialog.message.there.are.no.calls.in.project": "프로젝트에 {0}의 호출이 없습니다.",
        "dialog.message.cannot.inline.methods.with.return.statements.interrupting.execution.flow": "실행 흐름을 방해하는 반환 구문이 있는 메서드를 인라인화할 수 없습니다.",
        "question.inline.usage": "{2}의 {0}개 사용{1, choice, 0#|1#들}을(를) 인라인화하시겠습니까?",
        "message.never.used": "{0}이(가) 사용되지 않습니다.",
        "dialog.message.accessed.for.writing": "{0}이(가) 쓰기 위해 액세스되었습니다.",
        "dialog.message.accessed.for.address": "{0}이(가) 주소를 얻기 위해 액세스되었습니다.",
        "dialog.title.inline": "인라인 {0}",
        "button.inline.current.usage": "현재 사용 인라인(&U)",
        "button.inline.all.usages.file": "모든 사용 인라인{0, choice, 0# (파일 내)|1#}(&A)",
        "button.view.usages": "사용 표시(&S)",
        "button.cancel": "취소(&C)",
        "button.inline": "인라인(&I)",
        "button.rename": "이름 바꾸기(&R)",
        "button.rename.code": "코드 사용만 이름 바꾸기(&C)",
        "button.rename.all": "모든 사용 이름 바꾸기(&R)",
        "dialog.message.must.have.initializer": "{0}에는 초기화 구문이 있어야 합니다.",
        "rename.reference.command.name": "참조 이름 바꾸기",
        "rename.reference.invalid.dialog.title": "잘못된 식별자",
        "rename.reference.invalid.dialog.button.yes": "계속 편집",
        "rename.multiple.macro.usages.message": "{0}에 \"{1}\"에 대한 서로 다른 매핑의 여러 사용이 있습니다. 이름을 바꾸면 코드가 손상될 수 있습니다. 진행하시겠습니까?",
        "rename.non.code.usages.message": "{0}개의 사용이 주석 및 코드가 아닌 파일에서 발견되었습니다.\\n이름을 바꾸시겠습니까?",
        "dialog.title.extract.method": "메서드 추출",
        "dialog.title.extract.function": "함수 추출",
        "dialog.title.extract.block.parameter": "블록 매개변수 추출",
        "dialog.title.extract.lambda.parameter": "람다 매개변수 추출",
        "dialog.message.lambdas.not.supported": "현재 언어 표준에서 람다를 지원하지 않습니다.",
        "dialog.message.lambdas.cant.extract.initializer.list": "초기화 구문 목록을 람다 매개변수로 추출할 수 없습니다.",
        "dialog.message.lambdas.cant.extract.functional.type": "함수형 타입의 표현식을 람다 매개변수로 추출할 수 없습니다.",
        "dialog.message.lambdas.cant.extract.dependent.types": "종속 타입이 있는 표현식을 람다 매개변수로 추출할 수 없습니다.",
        "dialog.message.cant.refactor.operators": "C++ 연산자 함수를 리팩터링할 수 없습니다.",
        "button.extract": "추출",
        "dialog.message.cannot.extract.there.are.multiple.exit.points.in.selected.code.fragment": "{0}을(를) 추출할 수 없습니다.\\n선택한 코드 조각에 종료 지점이 여러 개 있습니다.",
        "dialog.message.selected.statements.should.be.inside.function.choice.or.method": "선택한 구문은 함수{0, choice, 0# 또는 메서드|1#} 내부에 있어야 합니다.",
        "dialog.message.can.t.refactor.with.variable.arguments": "가변 인수가 있는 {0}을(를) 리팩터링할 수 없습니다.",
        "dialog.message.overrides.in.choice.which.out.project": "{0}이(가) {2}{3, choice, 0# (프로젝트 외부에 있음)|1#}에서 {1}을(를) 재정의합니다.",
        "dialog.message.do.you.want.to.proceed.refactoring": "리팩터링을 진행하시겠습니까?",
        "dialog.message.do.you.want.to.refactor.base.s": "기본 {0}을(를) 리팩터링하시겠습니까?",
        "label.declaration.place": "선언 위치:",
        "refactoring.rename.command.name": "이름 바꾸기",
        "trying.to.rename.0.to.existing.file.name.1": "{0}을(를) 기존 파일 이름 {1}(으)로 이름 바꾸기를 시도 중입니다."
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
