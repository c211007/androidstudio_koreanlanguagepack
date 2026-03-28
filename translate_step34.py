import json
with open('missing_translations/missing_keys_korean.json', 'r', encoding='utf-8') as f:
    ko_data = json.load(f)

translations = {
  "replace.this.code.fragment.and.make.method.static": "(메서드가 정적(static)으로 변경됩니다)",
  "replace.this.code.fragment.and.make.method.static.visible": "(메서드가 정적(static) 및 {0}(으)로 변경됩니다)",
  "replace.this.code.fragment.and.make.method.visible": "(메서드가 {0}(으)로 변경됩니다)",
  "replace.with.method.call.does.not.work.for.constructors": "메서드 호출로 바꾸기는 생성자에 대해 작동하지 않습니다",
  "replace.write.access.occurrences": "쓰기 접근 발생 바꾸기(&L)",
  "replacing.inheritance.with.delegation": "상속을 위임으로 교체하는 중",
  "safe.delete.search.for.caller.method.usages.progress": "호출자 메서드 사용 검색 중...",
  "safe.delete.select.members.to.propagate.dialog.title": "안전 삭제를 파급할 멤버 선택",
  "safe.delete.select.methods.to.propagate.delete.parameters.dialog.title": "매개변수 삭제를 파급할 메서드 선택",
  "safe.delete.parameter.usage.warning": "{0}에 안전하게 삭제할 수 없는 호출 측 사용(call-side usage)이 있습니다.",
  "select.source.root.chooser.title": "소스 루트 선택",
  "selected.block.contains.invocation.of.another.class.constructor": "선택한 블록에 다른 클래스 생성자의 호출이 포함되어 있습니다",
  "selected.block.contains.statement.outside.of.class": "선택한 블록이 클래스 외부에 있는 문(statement)을 포함하고 있습니다",
  "selected.block.should.represent.an.expression": "선택한 블록은 표현식을 나타내야 합니다",
  "selected.expression.cannot.be.extracted": "선택한 표현식은 추출할 수 없습니다",
  "selected.expression.cannot.be.a.constant.initializer": "선택한 표현식은 상수 초기화자가 될 수 없습니다",
  "selected.expression.has.void.type": "선택한 표현식의 타입이 'void'입니다",
  "selected.expression.introduces.pattern.variable": "선택한 표현식이 패턴 변수 ''{0}''을(를) 도입합니다",
  "popup.title.choose.class.to.introduce.constant": "상수를 도입할 클래스 선택",
  "popup.title.choose.class.to.introduce.field": "필드를 도입할 클래스 선택",
  "setter.method.found.for.the.field.0": "{0} 필드에 대한 setter 메서드를 찾았습니다. \\n이 setter도 {1}하시겠습니까?",
  "source.folder.0.has.package.prefix.1": "소스 폴더 {0}에 패키지 접두사 ''{1}''이(가) 있습니다.\\n해당 위치에 ''{2}'' 패키지를 생성할 수 없습니다.",
  "static.initializer.description": "{0}의 정적 초기화자",
  "class.initializer.description": "{0, choice, 0#정적(static)|1#인스턴스} 초기화자",
  "superclass.cannot.be.accessed.in.subclass": "하위 클래스에서는 슈퍼 클래스에 접근할 수 없습니다",
  "superclass.cannot.be.extracted.from.an.enum": "Enum에서 슈퍼 클래스를 추출할 수 없습니다",
  "superclass.cannot.be.extracted.from.a.record": "레코드(record)에서 슈퍼 클래스를 추출할 수 없습니다",
  "synthetic.jsp.class.is.referenced.in.the.method": "메서드에서 합성(synthetic) JSP 클래스가 참조되었습니다",
  "target.0.is.not.accessible.from.1": "{1}에서 대상 {0}에 액세스할 수 없습니다",
  "there.are.going.to.be.multiple.destination.files.with.the.same.name": "이름이 같은 대상 파일이 여러 개 생성될 예정입니다",
  "there.are.multiple.exit.points.in.the.selected.code.fragment": "선택한 코드 조각에 종료 지점이 여러 개 있습니다",
  "there.are.multiple.output.values.for.the.selected.code.fragment": "선택한 코드 조각의 출력값이 여러 개 있습니다:",
  "there.are.no.variables.that.have.reference.type": "참조 타입(reference type)을 가진 메서드 매개변수나 포함된 클래스 필드가 없습니다.",
  "there.are.unused.methods.that.override.methods.you.delete": "<html>삭제할 메서드의 재정의(override) 메서드 중 사용되지 않는 항목이 있습니다. 같이 삭제하시겠습니까?</html>",
  "there.is.already.a.0.in.1": "{1}에 이미 {0}이(가) 있습니다",
  "there.is.already.a.0.it.will.conflict.with.an.introduced.parameter": "이미 {0}이(가) 있습니다. 이로 인해 도입된 매개변수와 충돌합니다",
  "there.is.already.a.0.it.will.conflict.with.the.renamed.1": "이름이 동일한 {0}이(가) 이미 존재합니다",
  "there.is.already.a.0.it.will.conflict.with.the.renamed.short": "''{0}'' 변수가 이미 존재합니다",
  "there.is.already.type.parameter.in.0.with.name.1": "{0}에 이름이 {1}인 타입 매개변수가 이미 존재합니다",
  "this.method": "이 메서드"
}

ko_error_bundle = next((x for x in ko_data['new_files'] if x['filename'] == 'JavaRefactoringBundle.properties'), None)
ko_error_bundle['keys'].update(translations)
ko_error_bundle['key_count'] = len(ko_error_bundle['keys'])

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(ko_data, f, ensure_ascii=False, indent=2)

print("Updated JavaRefactoringBundle part 17")