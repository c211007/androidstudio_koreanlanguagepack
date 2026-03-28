import json
from pathlib import Path

def update_missing_keys():
    file_path = Path("missing_translations/missing_keys_korean.json")

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    ko_dict = {
        "cannot.perform.the.refactoring": "리팩터링을 수행할 수 없습니다.\\n",
        "extract.class.title": "대리자 추출",
        "extract.class.from.label": "{0}에서 대리자 추출",
        "name.for.new.class.label": "새 클래스 이름(&N):",
        "choose.destination.package.label": "대상 패키지 선택",
        "package.for.new.class.label": "패키지 이름(&P):",
        "members.to.extract.label": "추출할 멤버(&B):",
        "there.already.exists.a.class.with.the.chosen.name": "선택한 이름을 가진 클래스가 이미 존재합니다.",
        "introduce.parameter.object": "매개변수 객체 도입",
        "the.caret.should.be.positioned.within.a.class.to.be.refactored": "리팩터링은 리팩터링할 클래스나 멤버에서 호출되어야 합니다.",
        "the.selected.class.is.an.enumeration": "선택한 클래스는 enum 클래스입니다.",
        "the.caret.should.be.positioned.within.a.method.declaration.to.be.refactored": "캐럿은 리팩터링할 메서드 선언 내에 있어야 합니다.",
        "the.selected.class.is.an.interface": "선택한 클래스는 인터페이스입니다.",
        "the.selected.class.is.an.annotation.type": "선택한 클래스는 어노테이션 인터페이스입니다.",
        "the.refactoring.is.not.supported.on.non.static.inner.classes": "정적이 아닌 내부 클래스에서는 리팩터링이 지원되지 않습니다.",
        "the.selected.class.has.no.members.to.extract": "선택한 클래스에는 추출할 멤버가 없습니다.",
        "the.selected.class.should.belong.to.project.sources": "선택한 클래스는 프로젝트 소스에 속해야 합니다.",
        "refactoring.cannot.be.done.in.implicit.class": "컴팩트 소스 파일을 리팩터링할 수 없습니다.",
        "references.to.extract": "추출할 참조({0, choice, 0#(찾을 수 없음)|1#{0}개의 참조|2#{0}개의 참조}{1, choice, 0#|1# - {1}개의 파일|2# - {1}개의 파일})",
        "extract.class.as.enum.column.title": "Enum으로",
        "extract.class.depends.on.0.from.1.tooltip": "{1}의 {0}에 종속됨",
        "extract.class.depends.on.0.from.new.class": "새 클래스 {1}의 {0}에 종속됨",
        "extracting.from.class": "다음 클래스에서 추출 중:",
        "extracted.class.command.name": "추출된 클래스 {0}",
        "extracted.class.not.accessible.in.0": "추출된 클래스에 {0}에서 접근할 수 없습니다.",
        "method.selected.has.no.parameters": "선택한 메서드에 매개변수가 없습니다.",
        "the.selected.method.cannot.be.wrapped.because.it.is.defined.in.a.non.project.class": "선택한 메서드는 프로젝트 외의 클래스에 정의되어 있으므로 래핑할 수 없습니다.",
        "select.wrapper.class": "매개변수 클래스 선택",
        "field.needs.getter": "필드 ''{0}''에 getter가 필요합니다.",
        "field.needs.setter": "필드 ''{0}''에 setter가 필요합니다.",
        "initializer.requires.moved.members": "클래스 초기화 구문에 이동된 멤버가 필요합니다.",
        "constructor.requires.moved.members": "생성자에 이동된 멤버가 필요합니다.",
        "case.value.can.not.be.replaced.with.enum": "{0}을(를) enum으로 바꿀 수 없습니다.",
        "referenced.element.out.of.project": "{0}이(가) 프로젝트 외부에 있습니다.",
        "unable.to.migrate.statement.to.enum": "구문을 enum 상수로 마이그레이션할 수 없습니다.{0}",
        "codestyle.settings.extractor.command.name": "코드 스타일 설정 추출기"
    }

    filename = "RefactorJBundle.properties"
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
