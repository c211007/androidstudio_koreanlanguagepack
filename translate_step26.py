import json
with open('missing_translations/missing_keys_korean.json', 'r', encoding='utf-8') as f:
    ko_data = json.load(f)

translations = {
  "inline.method.multiline.method.in.ctor.call": "생성자 호출에 있는 여러 줄의 메서드에는 인라인을 적용할 수 없습니다",
  "inline.method.multiline.method.in.loop.condition": "반복문 조건에 있는 여러 줄의 메서드에는 인라인을 적용할 수 없습니다",
  "inline.method.object.action.name": "객체 인라인",
  "inline.method.object.suggestion.message": "객체와 그 후속 호출을 인라인하시겠습니까?",
  "inline.method.qualifier.usage.side.effect": "인라인 메서드가 한정자에 부작용이 있는 메서드 참조에 사용되었습니다",
  "inline.method.used.in.javadoc": "인라인 메서드가 Javadoc에 사용되었습니다",
  "inline.method.used.in.reflection": "인라인 메서드가 리플렉션으로 사용되었습니다",
  "inline.parameter.action.name": "매개변수 인라인...",
  "inline.parameter.cannot.find.initializer.warning.message": "매개변수에 대한 상수 초기화자를 찾을 수 없습니다",
  "inline.parameter.confirmation": "초기화자가 ''{1}''인 ''{0}'' 매개변수를 인라인하시겠습니까?",
  "inline.parameter.error.hierarchy": "메서드가 상속 계층 구조의 일부일 때 매개변수 인라인은 지원되지 않습니다",
  "inline.parameter.error.non.project.method": "프로젝트 외부 메서드에 대해서는 인라인이 지원되지 않습니다",
  "inline.parameter.error.varargs": "가변 인수(varargs) 매개변수에 대한 인라인은 지원되지 않습니다",
  "inline.parameter.dependency.unavailable.in.parameter.method": "매개변수 초기화자가 해당 매개변수의 메서드 내부에서는 접근할 수 없는 {0}에 의존합니다",
  "inline.parameter.depends.on.caller.parameter": "매개변수 초기화자가 호출자의 {0}에 의존합니다",
  "inline.parameter.depends.on.non.static": "매개변수 초기화자가 static이 아닌 {0}에 의존하며, 해당 매개변수의 메서드 내부에서 인스턴스를 사용할 수 없습니다",
  "inline.parameter.depends.on.non.static.class": "매개변수 초기화자가 해당 매개변수의 메서드 내부에서는 접근할 수 없는 static이 아닌 {0}에 의존합니다",
  "inline.parameter.initializer.depends.on.inaccessible.value": "매개변수 초기화자에 대한 쓰기 접근은 인라인 할 수 없습니다",
  "inline.parameter.method.usages.progress": "메서드 사용 검색 중",
  "inline.parameter.no.usages.warning.message": "메서드가 사용되지 않았습니다",
  "inline.parameter.not.accessible.warning.message": "상수 초기화자가 메서드 본문에서 액세스할 수 없습니다",
  "inline.parameter.refactoring": "매개변수 인라인",
  "inline.parameter.replace.with.local.checkbox": "로컬 변수로 바꾸기(&E)",
  "inline.parameter.write.usages.warning.message": "쓰기 사용이 있는 매개변수의 인라인은 지원되지 않습니다",
  "inline.pattern.variable.title": "패턴 변수 인라인",
  "inline.super.class": "슈퍼 클래스 인라인",
  "inline.super.class.action.name": "슈퍼 클래스 인라인...",
  "inline.super.class.label": "클래스 {0}",
  "inline.super.ctor.can.be.replaced": "{0} 생성자는 {1} 중 하나로 교체할 수 있습니다",
  "inline.super.doc.panel.title": "인라인 맴버에 대한 JavaDoc",
  "inline.super.expr.can.be.replaced": "{0}은(는) {1} 중 하나로 교체할 수 있습니다",
  "inline.super.no.anonymous.class": "익명 클래스에는 인라인할 수 없습니다.",
  "inline.super.no.ctor": "Super와 일치하는 생성자를 찾을 수 없습니다",
  "inline.super.no.inner.class": "내부 클래스에는 인라인할 수 없습니다. ''{0}''을(를) 상위 수준으로 이동하세요",
  "inline.super.no.substitution": "{0}에 대해 일관된 대체를 찾지 못했습니다. ''{1}''이(가) 예상되었지만 ''{2}''을(를) 찾았습니다.",
  "inline.super.no.return.in.super.ctor": "반환문(return statement)이 슈퍼 생성자의 실행 흐름을 방해하는 경우 리팩터링이 지원되지 않습니다",
  "inline.super.non.project.class.warning.message": "프로젝트 외부 클래스는 인라인할 수 없습니다",
  "inline.super.static.import.can.be.replaced": "정적 가져오기(Static import)는 {0} 중 하나로 바꿀 수 있습니다",
  "inline.super.target.instead.of.super.class": "슈퍼 클래스가 필요한 위치에 대상 유형의 인스턴스가 전달되었습니다.",
  "inline.super.type.element.can.be.replaced": "{0}은(는) {1} 중 하나로 교체할 수 있습니다"
}

ko_error_bundle = next((x for x in ko_data['new_files'] if x['filename'] == 'JavaRefactoringBundle.properties'), None)
ko_error_bundle['keys'].update(translations)
ko_error_bundle['key_count'] = len(ko_error_bundle['keys'])

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(ko_data, f, ensure_ascii=False, indent=2)

print("Updated JavaRefactoringBundle part 9")