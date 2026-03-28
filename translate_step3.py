import json
with open('missing_translations/missing_keys_korean.json', 'r', encoding='utf-8') as f:
    ko_data = json.load(f)

translations = {
  "multiple.non.overriding.abstract.methods.found.in.interface.0": "인터페이스 {0}에서 오버라이딩되지 않은 여러 추상 메서드를 발견했습니다",
  "no.target.method.found": "대상 메서드를 찾을 수 없습니다",
  "target.type.of.a.lambda.conversion.must.be.an.interface": "람다 변환의 대상 유형은 인터페이스여야 합니다",
  "incompatible.parameter.types.in.lambda": "람다 표현식의 매개변수 유형이 호환되지 않습니다: {0}이(가) 필요하지만 {1}을(를) 발견했습니다",
  "incompatible.parameter.types.in.lambda.wrong.number.of.parameters": "람다 표현식의 매개변수 유형이 호환되지 않습니다: 잘못된 매개변수 개수: {0}개가 필요하지만 {1}개를 발견했습니다",
  "an.enclosing.instance.of.type.not.in.scope.method.reference.context": "유형이 {0}인 바깥쪽(enclosing) 인스턴스가 범위에 없습니다",
  "parameterized.qualifier.on.static.method.reference.context": "정적(static) 메서드 참조의 매개변수화된 지정자(qualifier)",
  "static.method.referenced.through.receiver.method.reference.context": "수신자를 통해 참조된 정적(static) 메서드",
  "static.method.referenced.through.non.static.qualifier.method.reference.context": "정적이지 않은 지정자를 통해 참조된 정적(static) 메서드",
  "non.static.method.cannot.be.referenced.from.a.static.context.method.reference.context": "정적이지 않은 메서드는 정적(static) 컨텍스트에서 참조할 수 없습니다",
  "abstract.method.0.cannot.be.accessed.directly.method.reference.context": "추상 메서드 ''{0}''에 직접 액세스할 수 없습니다",
  "error.interface.member.clashes": "@interface 멤버가 {1}의 ''{0}''과(와) 충돌합니다",
  "anonymous.class.implements.interface.cannot.have.type.arguments": "익명 클래스가 인터페이스를 구현합니다. 유형 인수를 가질 수 없습니다",
  "formal.varargs.element.type.inaccessible.here": "가변 인수(varargs) 요소 유형 {0}에 여기서 액세스할 수 없습니다",
  "unexpected.type.class.expected": "예기치 못한 유형: 클래스가 필요합니다",
  "repeated.interface": "반복된 인터페이스",
  "class.cannot.be.inherited.with.different.arguments": "{0}은(는) 다른 인수({1})로 상속될 수 없습니다",
  "bad.type.in.switch.expression": "switch 표현식의 잘못된 유형: {0}을(를) {1}(으)로 변환할 수 없습니다",
  "switch.expression.cannot.be.void": "switch 표현식의 대상 유형은 void일 수 없습니다",
  "annotation.on.static.member.qualifying.type.family.name": "유형 어노테이션 이동",
  "not.inner.class": "상위 클래스 ''{0}''이(가) 정적이지 않은 내부 클래스가 아니므로 지정자가 허용되지 않습니다",
  "anonymous.class.implements.interface.cannot.have.qualifier": "익명 클래스가 인터페이스를 구현합니다. new에 대한 지정자를 가질 수 없습니다",
  "qualified.class.reference.not.allowed.in.qualified.new": "지정된 new에서는 지정된 클래스 참조가 허용되지 않습니다",
  "actual.type.argument.contradict.inferred.type": "실제 유형 인수와 추론된 유형이 서로 모순됩니다",
  "default.method.overrides.object.member": "기본(default) 메서드 ''{0}''이(가) ''java.lang.Object''의 멤버를 오버라이딩합니다",
  "two.methods.are.inherited.with.same.signature": "{1}의 {0} 및 {3}의 {2} 메서드가 동일한 시그니처로 상속되었습니다",
  "cannot.select.from.parameterized.type": "매개변수화된 유형의 클래스 객체에 액세스할 수 없습니다",
  "safevarargs.not.allowed.non.final.instance.methods": "final이 아닌 인스턴스 메서드에서는 @SafeVarargs가 허용되지 않습니다",
  "safevarargs.not.suppress.potentially.unsafe.operations": "@SafeVarargs는 잠재적으로 안전하지 않은 작업을 표시하지 않도록(suppress) 할 수 없습니다",
  "safevarargs.not.applicable.for.reifiable.types": "@SafeVarargs는 구체화 가능한(reifiable) 유형에는 적용할 수 없습니다"
}

ko_error_bundle = next((x for x in ko_data['new_files'] if x['filename'] == 'JavaErrorBundle.properties'), None)
ko_error_bundle['keys'].update(translations)
ko_error_bundle['key_count'] = len(ko_error_bundle['keys'])

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(ko_data, f, ensure_ascii=False, indent=2)

print("Updated keys.")
