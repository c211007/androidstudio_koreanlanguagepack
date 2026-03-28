import json
from pathlib import Path

def update_missing_keys():
    file_path = Path("missing_translations/missing_keys_korean.json")

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    ko_dict = {
        "dialog.message.no.inheritors.are.selected": "상속자가 선택되지 않았습니다.",
        "progress.title.inplace.rename.appending.additional.elements": "추가 요소 추가 중",
        "progress.title.inplace.rename.preparing": "이름 바꾸기 준비 중",
        "extract.invalid.name.for.class.type.error": "{0}의 이름이 유효하지 않습니다.",
        "refactoring.introduce.constant.name": "상수 도입",
        "refactoring.introduce.define.name": "정의 도입",
        "refactoring.introduce.typedef.name": "Typedef 도입",
        "refactoring.introduce.variable.name": "변수 도입",
        "refactoring.introduce.ivar.name": "Ivar 도입",
        "refactoring.introduce.property.name": "프로퍼티 도입",
        "refactoring.introduce.instance.variable.name": "인스턴스 변수 도입",
        "refactoring.introduce.parameter.name": "매개변수 도입",
        "refactoring.move.no.members.are.selected.error": "멤버가 선택되지 않았습니다.",
        "refactoring.move.members.ok.button.text": "이동(&M)",
        "refactoring.move.pull.up.ok.button.text": "풀업(&U)",
        "refactoring.move.push.down.ok.button.text": "푸시다운(&U)",
        "refactoring.move.escalate.visibility.declare.in.interface": "인터페이스에 선언",
        "refactoring.move.namespace.has.no.members": "\"{0}\" 네임스페이스에 이동할 멤버가 없습니다.",
        "refactoring.move.file.has.no.members": "\"{0}\" 파일에 이동할 멤버가 없습니다.",
        "refactoring.symbol.has.no.members.to.move": "{0}에 이동할 멤버가 없습니다.",
        "refactoring.move.caret.position": "캐럿은 클래스 내부에 위치해야 합니다.",
        "refactoring.move.cant.find.symbol": "선택한 클래스의 심볼을 찾을 수 없습니다.",
        "refactoring.move.members.error.no.target.class.selected": "대상 클래스가 선택되지 않았습니다.",
        "refactoring.move.members.error.class.name.invalid": "클래스 이름이 유효하지 않습니다.",
        "refactoring.move.members.error.not.in.project.sources": "{0}이(가) 프로젝트 내에 있지 않습니다.",
        "refactoring.move.members.error.the.same.source.and.target": "소스와 대상 클래스는 확연하게 달라야 합니다.",
        "refactoring.move.members.message.target.does.not.exist": "대상 클래스 \"{0}\"이(가) 아직 없습니다.",
        "refactoring.extract.super.protocol.title": "상위 프로토콜 추출",
        "refactoring.extract.subclass.title": "하위 클래스 추출",
        "refactoring.extract.category.title": "카테고리 추출",
        "refactoring.introduce.block.expression.represent.error": "선택한 블록은 {0}을(를) 나타내야 합니다.",
        "refactoring.introduce.expressions.choose.dialog.title": "표현식",
        "refactoring.introduce.put.to.header": "헤더에 넣기(&H)",
        "refactoring.change.signature.target.symbols.panel": "대상:",
        "refactoring.rename": "{0} 이름 바꾸기(&R)",
        "refactoring.rename.class.aliases": "클래스 별칭 이름 바꾸기(&R)",
        "refactoring.rename.associated.file": "연결된 파일 이름 바꾸기",
        "refactoring.introduce.constant.static.declaration": "static 선언(&S)",
        "refactoring.introduce.constant.constexpr.declaration": "constexpr 선언(&C)",
        "refactoring.introduce.constant.auto.declaration": "auto 선언(&A)",
        "refactoring.ivar.inplace.introducer.generate.property": "프로퍼티 생성(&P)",
        "refactoring.ivar.inplace.introducer.declare.interface": "인터페이스에 선언(&I)",
        "refactoring.introducer.declare.const": "const 선언(&C)",
        "refactoring.introducer.declare.auto": "auto 선언(&A)",
        "refactoring.parameter.introducer.refactor.super.method": "super {0} 리팩터링(&S)",
        "refactoring.property.introducer.make.readonly": "읽기 전용으로 만들기(&R)",
        "refactoring.property.introducer.generate.synthesize": "@synthesize 생성(&S)",
        "refactoring.property.introducer.generate.instance.variable": "인스턴스 변수 생성(&I)",
        "refactoring.property.introducer.put.to.private.category": "프라이빗 카테고리에 넣기(&P)",
        "dialog.title.choose.containing.class": "포함하는 클래스 선택"
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
