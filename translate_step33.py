import json
with open('missing_translations/missing_keys_korean.json', 'r', encoding='utf-8') as f:
    ko_data = json.load(f)

translations = {
  "rename.tests.with.the.following.names.to": "다음 이름을 가진 테스트 이름 변경:",
  "rename.variables": "변수 이름 변경(&V)",
  "rename.variables.title": "변수 이름 변경",
  "title.rename.variables.with.the.following.names.to": "다음 이름을 가진 변수 이름 변경:",
  "rename.accessors": "접근자 이름 변경(&A)",
  "rename.accessors.title": "Getter/Setter 이름 변경",
  "rename.accessors.with.the.following.names.to": "다음 이름을 가진 접근자 이름 변경:",
  "renamed.class.will.hide.0.in.1": "이름이 바뀐 클래스가 {1}의 {0}을(를) 숨깁니다",
  "renaming.method.will.override.final.0": "메서드가 슈퍼 {1}의 final {0}을(를) 재정의(override)합니다",
  "rename.test.method": "테스트 메서드 이름 변경",
  "rename.test.method.title": "테스트 메서드 이름 변경",
  "rename.test.method.description": "다음 이름을 가진 테스트 메서드 이름 변경:",
  "rename.test.method.entity.name": "테스트 메서드",
  "replace.all.fields": "모든 필드 바꾸기(&R)",
  "replace.all.occurrences.of.expression.0.occurrences": "모든 항목 바꾸기 ({0})(&A)",
  "replace.constructor.0.with.a.factory.method": "생성자 {0}을(를) 팩터리 메서드로 바꾸기",
  "replace.constructor.builder.create.new": "새로 만들기(&C)",
  "replace.constructor.builder.use.existing": "기존 항목 사용(&U)",
  "replace.constructor.existing.builder.fqn": "빌더(Builder) 클래스 이름 (정규화된 이름)(&B)",
  "replace.constructor.new.builder.class.name": "빌더(Builder) 클래스 이름(&N)",
  "replace.constructor.new.builder.package": "새 빌더를 위한 패키지(&P)",
  "replace.constructor.with.factory.method": "생성자를 팩터리 메서드로 바꾸기",
  "replace.constructor.with.factory.method.title": "생성자를 팩터리 메서드로 교체",
  "replace.constructor.with.factory.target.fq.name": "위치 (정규화된 이름):",
  "replace.default.constructor.of.0.with.a.factory.method": "{0}의 기본 생성자를 팩터리 메서드로 바꾸기",
  "replace.default.constructor.with.factory.method": "기본 생성자를 팩터리 메서드로 바꾸기",
  "replace.fields.inaccessible.in.usage.context": "사용 컨텍스트에서 액세스할 수 없는 필드 교체(&I)",
  "replace.fields.used.in.expressions.with.their.getters": "표현식에서 사용된 필드를 getter로 교체(&U)",
  "replace.inheritance.from": "상속을 다음으로부터의 위임으로 교체(&R):",
  "replace.inheritance.with.delegation.command": "{0}에서 상속을 위임(delegation)으로 교체하는 중",
  "replace.inheritance.with.delegation.delegate.members.title": "멤버 위임",
  "replace.inheritance.with.delegation.elements.header": "상속을 위임으로 교체",
  "replace.inheritance.with.delegation.invalid.field": "''{0}''은(는) 위임에 유효하지 않은 필드 이름입니다",
  "replace.inheritance.with.delegation.invalid.inner.class": "''{0}''은(는) 위임에 유효하지 않은 내부 클래스 이름입니다",
  "replace.inheritance.with.delegation.title": "상속을 위임(Delegation)으로 교체",
  "replace.instance.qualifiers.with.class.references": "인스턴스 한정자(qualifiers)를 클래스 참조로 바꿈",
  "replace.method.code.duplicates.title": "코드 중복 교체",
  "replace.method.duplicates.scope.chooser.message": "분석 범위",
  "replace.method.duplicates.scope.chooser.title": "{0} 범위 지정",
  "replace.this.code.fragment.and.change.signature": "\\n메서드 시그니처가 다음과 같이 변경됩니다:\\n{0}"
}

ko_error_bundle = next((x for x in ko_data['new_files'] if x['filename'] == 'JavaRefactoringBundle.properties'), None)
ko_error_bundle['keys'].update(translations)
ko_error_bundle['key_count'] = len(ko_error_bundle['keys'])

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(ko_data, f, ensure_ascii=False, indent=2)

print("Updated JavaRefactoringBundle part 16")