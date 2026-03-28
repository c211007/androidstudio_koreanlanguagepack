import json
with open('missing_translations/missing_keys_korean.json', 'r', encoding='utf-8') as f:
    ko_data = json.load(f)

translations = {
  "0.already.contains.field.1": "{0}에 이미 {1} 필드가 포함되어 있습니다",
  "0.already.contains.inner.class.named.1": "{0}에 이름이 {1}인 내부 클래스가 이미 포함되어 있습니다",
  "0.already.has.parameter.named.1.use.this.name.anyway": "{0}에 이미 이름이 ''{1}''인 매개변수가 있습니다.\\n그래도 이 이름을 사용하시겠습니까?",
  "0.contains.call.with.null.argument.for.parameter.1": "{0}에 {1} 매개변수에 대해 null 인수를 사용하는 호출이 포함되어 있습니다",
  "0.implements.1": "{0}이(가) {1}을(를) 구현합니다.",
  "0.is.1.and.will.not.be.accessible.from.2.in.the.target.class": "{0}은(는) {1}이며 {2}에서 액세스할 수 없게 됩니다.",
  "dialog.message.0.would.hide.which.1.used.by.moved.2": "{0}은(는) 이동된 {2}에서 사용되는 {1}을(를) 숨깁니다.",
  "0.is.a.part.of.method.hierarchy.do.you.want.to.delete.multiple.parameters": "{0}은(는) 메서드 계층 구조의 일부입니다. 여러 매개변수를 삭제하시겠습니까?",
  "0.is.a.part.of.method.hierarchy.do.you.want.to.delete.multiple.type.parameters": "{0}은(는) 메서드 계층 구조의 일부입니다. 여러 타입 매개변수를 삭제하시겠습니까?",
  "0.is.an.interface.method.implementation.will.be.added.to.all.directly.implementing.classes": "{0}은(는) 인터페이스입니다.\\n메서드 구현이 직접 구현하는 모든 클래스에 추가됩니다.\\n계속하시겠습니까?",
  "0.is.an.interface.that.has.no.implementing.classes": "{0}은(는) 구현하는 클래스가 없는 인터페이스입니다",
  "0.is.not.a.legal.java.identifier": "''{0}''은(는) 유효한 Java 식별자가 아닙니다",
  "0.is.not.accessible.from.1.value.for.introduced.parameter.in.that.method.call.will.be.incorrect": "{1}에서 {0}에 액세스할 수 없습니다. 해당 메서드 호출에 도입된 매개변수의 값이 올바르지 않게 됩니다.",
  "0.is.not.initialized.in.declaration.such.fields.are.not.allowed.in.interfaces": "{0}이(가) 선언에서 초기화되지 않았습니다. 인터페이스에서는 이러한 필드가 허용되지 않습니다.",
  "0.is.not.static.it.cannot.be.moved.to.the.interface": "{0}은(는) 정적(static)이 아닙니다. 인터페이스로 이동할 수 없습니다.",
  "0.is.used.for.writing.in.1": "{0}이(가) {1}에 쓰기 작업으로 사용되었습니다",
  "0.refactoring.is.supported.only.for.final.fields": "{0} 리팩토링은 final 필드에 대해서만 지원됩니다",
  "0.upcasts.an.instance.of.1.to.2": "{0}이(가) {1}의 인스턴스를 {2}(으)로 업캐스트합니다",
  "0.uses.1.of.an.instance.of.a.2": "{0}이(가) {2} 인스턴스의 {1}을(를) 사용합니다",
  "0.uses.1.which.needs.class.instance": "{0}이(가) 클래스 인스턴스가 필요한 {1}을(를) 사용합니다",
  "0.uses.a.package.local.1": "{0}이(가) package-private(패키지 전용) {1}을(를) 사용합니다",
  "0.uses.non.static.1.which.is.not.passed.as.a.parameter": "{0}이(가) 매개변수로 전달되지 않는 비정적(non-static) {1}을(를) 사용합니다",
  "0.will.be.inaccessible.from.1": "{1}에서 {0}에 액세스할 수 없게 됩니다",
  "0.will.become.inaccessible.from.1": "{0}이(가) {1}에서 액세스할 수 없게 됩니다",
  "0.will.hide.renamed.1": "{0}이(가) 이름이 변경된 {1}을(를) 숨깁니다",
  "0.will.no.longer.override.1": "{0}이(가) 더 이상 {1}을(를) 재정의(override)하지 않습니다",
  "0.will.no.longer.be.record.component.accessor": "{0}이(가) 더 이상 {1}의 getter가 아닙니다",
  "0.will.no.longer.be.canonical.constructor": "생성자가 더 이상 정규(canonical) 생성자가 아닙니다",
  "0.will.not.be.accessible.from.1.after.inlining": "인라인 후 {1}에서 {0}에 액세스할 수 없게 됩니다",
  "0.will.override.renamed.1": "{0}이(가) 이름이 변경된 {1}을(를) 재정의(override)합니다",
  "a.package.local.class.0.will.no.longer.be.accessible.from.1": "package-local(패키지 전용) 클래스 {0}에 더 이상 {1}에서 액세스할 수 없게 됩니다",
  "accept.signature.change": "시그니처 변경 수락",
  "add.object.as.a.parameter.to.constructors.with.name": "이름이 지정된 생성자에 객체를 매개변수로 추가(&O):",
  "add.parameters.for.fields": "필드에 대한 매개변수 추가(&F):",
  "add.parameters.for.fields.to.constructors": "생성자에 필드에 대한 매개변수 추가(&F):",
  "all.candidate.variables.have.types.not.in.project": "모든 후보 변수(메서드 매개변수 및 포함된 클래스 필드)의 타입이 프로젝트에 없습니다",
  "all.candidate.variables.have.unknown.types": "모든 후보 변수(메서드 매개변수 및 포함된 클래스 필드)의 타입이 알 수 없는 타입입니다",
  "all.invocations.keep.the.method": "모든 사용 위치 인라인화 및 메서드 유지(&E)",
  "all.references.and.remove.super.class": "모든 참조 인라인화 및 클래스 제거(&A)",
  "all.references.and.remove.the.class": "모든 참조 인라인화 및 클래스 제거(&A)"
}

ko_error_bundle = next((x for x in ko_data['new_files'] if x['filename'] == 'JavaRefactoringBundle.properties'), None)
if not ko_error_bundle:
    ko_error_bundle = {'filename': 'JavaRefactoringBundle.properties', 'keys': {}, 'key_count': 0}
    ko_data['new_files'].append(ko_error_bundle)
ko_error_bundle['keys'].update(translations)
ko_error_bundle['key_count'] = len(ko_error_bundle['keys'])

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(ko_data, f, ensure_ascii=False, indent=2)

print("Updated JavaRefactoringBundle part 1")