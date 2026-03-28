import json
with open('missing_translations/missing_keys_korean.json', 'r', encoding='utf-8') as f:
    ko_data = json.load(f)

translations = {
  "type.parameter.has.incompatible.upper.bounds": "유형 매개변수 {0}에 호환되지 않는 상한(upper bounds)이 있습니다: {1}",
  "safevarargs.not.allowed.on.methods.with.fixed.arity": "고정된 인수 개수(arity)를 가진 메서드에서는 @SafeVarargs가 허용되지 않습니다",
  "safevararg.annotation.cannot.be.applied.for.record.component": "레코드 구성요소에는 @SafeVarargs 어노테이션을 적용할 수 없습니다",
  "functional.interface.must.not.be.sealed.error.description": "함수형 인터페이스는 ''{0}''(으)로 선언할 수 없습니다",
  "sealed.type.inheritor.expected.modifiers": "''{0}'', ''{1}'' 또는 ''{2}'' 제어자(modifier)가 필요합니다",
  "sealed.type.inheritor.expected.modifiers2": "''{0}'' 또는 ''{1}'' 제어자(modifier)가 필요합니다",
  "not.allowed.in.sealed.hierarchy": "''{0}''은(는) sealed 계층 구조에서 허용되지 않습니다",
  "invalid.permits.clause": "잘못된 permits 절: ''{0}''은(는) sealed여야 합니다",
  "invalid.permits.clause.direct.implementation": "잘못된 permits 절: ''{0}''은(는) 직접 ''{2}''을(를) {1, choice, 1#extend(확장)|2#implement(구현)}해야 합니다",
  "sealed.must.have.inheritors": "sealed 클래스는 하위 클래스를 가져야 합니다",
  "permit.list.must.contain.outside.inheritors": "sealed 클래스의 permits 절은 모든 하위 클래스를 포함해야 합니다",
  "permitted.subclass.must.have.modifier": "허용된 모든 하위 클래스는 final, sealed 또는 non-sealed 중 하나여야 합니다",
  "permits.list.generics.are.not.allowed": "permits 목록에서는 제네릭을 사용할 수 없습니다",
  "sealed.cannot.be.functional.interface": "sealed 클래스는 함수형 인터페이스로 사용할 수 없습니다",
  "local.classes.must.not.extend.sealed.classes": "로컬 클래스는 sealed 클래스를 확장할 수 없습니다",
  "anonymous.classes.must.not.extend.sealed.classes": "익명 클래스는 sealed 클래스를 확장할 수 없습니다",
  "class.not.allowed.to.extend.sealed.class.from.another.package": "클래스는 다른 패키지의 sealed 클래스를 확장할 수 없습니다",
  "class.not.allowed.to.extend.sealed.class.from.another.module": "클래스는 다른 모듈의 sealed 클래스를 확장할 수 없습니다",
  "annotation.cannot.be.local": "로컬 어노테이션은 허용되지 않습니다",
  "create.class.action.this.not.valid.java.qualified.name": "이것은 유효한 Java의 정규화된 이름(qualified name)이 아닙니다",
  "text.class.inherits.abstract.and.default": "{0}이(가) 유형 {2} 및 {3}에서 {1}에 대한 abstract 및 default를 상속합니다",
  "text.class.inherits.unrelated.defaults": "{0}이(가) 유형 {2}에서 {1}에 대한 관련 없는 default를 상속합니다",
  "text.improper.formed.type": "잘못 형성된 유형입니다. 일부 유형 매개변수가 누락되었습니다",
  "text.class.is.not.accessible": "현재 컨텍스트에서 {0}에 액세스할 수 없습니다",
  "text.class.cannot.access": "{0}에 액세스할 수 없습니다",
  "auto.closeable.resource": "자동 닫기 가능(auto-closeable) 리소스",
  "annotation.type.permits": "어노테이션 유형에는 permits 절이 허용되지 않습니다",
  "too.many.array.dimensions": "배열 차원이 너무 많습니다",
  "error.cannot.infer.pattern.type": "패턴 유형을 추론할 수 없습니다: {0}",
  "error.extra.semicolons.between.import.statements.not.allowed": "import 문 사이의 추가 세미콜론은 허용되지 않습니다",
  "error.guard.allowed.after.patterns.only": "가드(guard)는 패턴 뒤에서만 허용됩니다",
  "error.implicit.class.contains.no.main.method": "암시적으로 선언된 클래스에 'main' 메서드가 없습니다",
  "error.implicit.class.has.invalid.file.name": "암시적으로 선언된 클래스의 파일 이름이 유효한 식별자가 아닙니다",
  "error.package.statement.not.allowed.for.implicit.class": "암시적으로 선언된 클래스에서는 패키지 선언(package statement)이 허용되지 않습니다",
  "error.initializers.are.not.allowed.in.implicit.classes": "암시적으로 선언된 클래스에서는 이니셜라이저가 허용되지 않습니다",
  "remove.unused.imports.quickfix.text": "사용되지 않는 import 제거"
}

ko_error_bundle = next((x for x in ko_data['new_files'] if x['filename'] == 'JavaErrorBundle.properties'), None)
ko_error_bundle['keys'].update(translations)
ko_error_bundle['key_count'] = len(ko_error_bundle['keys'])

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(ko_data, f, ensure_ascii=False, indent=2)

print("Updated final keys for JavaErrorBundle.properties.")
