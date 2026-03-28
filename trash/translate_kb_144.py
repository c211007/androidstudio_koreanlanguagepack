import json

ko_dict = {
  "goto.super.type.name2": "{0}의 기본 함수로 이동",
  "goto.super.type.name3": "상위 타입으로 이동",
  "goto.subclass": "하위 클래스로 이동",
  "goto.subclass.title": "하위 클래스로 이동",
  "goto.overridden": "재정의된 {0}으(로) 이동...",
  "goto.overridden.title": "재정의된 {0}(으)로 이동",
  "goto.overridden.methods": "재정의된 메서드로 이동...",
  "goto.overridden.methods.title": "재정의된 메서드로 이동",
  "goto.overridden.functions": "재정의된 함수로 이동...",
  "goto.overridden.functions.title": "재정의된 함수로 이동",
  "saving.symbols": "심볼 저장 중\\u2026",
  "progress.text.updating.symbols": "심볼 업데이트 중\\u2026",
  "inspection.message.function.not.implemented": "{0}이(가) 구현되지 않았습니다.",
  "command.name.add.parameter.to.constructor": "생성자에 매개변수 추가",
  "dialog.title.select.constructor.to.update": "업데이트할 생성자 선택",
  "command.name.add.parameter.to.initwith": "'initWith...'에 매개변수 추가",
  "dialog.title.select.initwith.method.to.update": "업데이트할 'initWith...' 메서드 선택",
  "dialog.message.objc.do.you.want.to.generate.instance.variables.for.chosen.properties": "선택한 프로퍼티의 인스턴스 변수를 생성하시겠습니까?",
  "dialog.title.objc.generate.instance.variables": "인스턴스 변수 생성",
  "dialog.message.do.you.want.to.move.class.member.definitions": "클래스 멤버 정의를 이동하시겠습니까?",
  "dialog.title.move.refactoring.adding.imports": "가져오기 추가",
  "filetype.qt.ui.designer.form.description": "Qt UI 디자이너 양식",
  "statement.name": "구문",
  "expression.name": "표현식",
  "declaration.name": "선언",
  "surround.with.block.expression.template": "^{ return expr; }",
  "surround.with.do.while.template": "do / while",
  "surround.with.for.template": "for",
  "surround.with.while.template": "while",
  "surround.with.if.else.template": "if / else",
  "surround.with.if.template": "if",
  "surround.with.not.expr.template": "!(expr)",
  "surround.with.parenthesis.template": "(expr)",
  "surround.with.if.respondsToSelector.template": "if respondsToSelector",
  "refactoring.dialog.no.target.file.selected": "대상 파일이 선택되지 않았습니다.",
  "refactoring.dialog.file.name.invalid": "파일 이름이 유효하지 않습니다.",
  "refactoring.dialog.file.not.located.inside.project": "\"{0}\" 파일이 프로젝트 내에 있지 않습니다.",
  "refactoring.dialog.source.and.target.should.be.different": "소스와 대상은 달라야 합니다.",
  "refactoring.dialog.target.namespace.name.invalid": "대상 네임스페이스 이름이 유효하지 않습니다.",
  "refactoring.dialog.target.ns.is.part.of.qualified.ns": "대상 네임스페이스는 한정된 네임스페이스의 일부입니다.",
  "refactoring.dialog.can.t.move.to.itself": "{0}을(를) 자기 자신에게 이동할 수 없습니다.",
  "inspection.name.is.never.used": "{0}이(가) 사용되지 않습니다.",
  "element.description.provider.symbol.of.parent": "{1}의 {0}",
  "element.description.provider.predefinition.of": "{0}의 사전 정의",
  "qdoc.definition": "정의:",
  "qdoc.declared.in": "선언 위치:",
  "qdoc.replacement": "대체:",
  "qdoc.description.copied.from": "설명 복사본 출처:",
  "qdoc.offset": "오프셋",
  "qdoc.size": "크기"
}

with open("missing_translations/missing_keys_korean.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for item in data.get("new_files", []):
    if item["filename"] == "OCBundle.properties":
        item["keys"].update(ko_dict)
        print("Updated OCBundle.properties")
        break

with open("missing_translations/missing_keys_korean.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
