import json

ko_dict = {
  "inspection.redundant.async.display.name": "중복되는 'async' 호출",
  "inspection.main.function.return.unit.display.name": "Main 함수는 'Unit'을 반환해야 합니다.",
  "inspection.move.variable.declaration.into.when.display.name": "변수 선언을 'when' 내부로 이동할 수 있습니다.",
  "inspection.move.lambda.outside.parentheses.display.name": "괄호 안의 람다 인수",
  "inspection.no.actual.for.expect.display.name": "expect 선언에 대한 actual이 없습니다.",
  "inspection.can.sealed.subclass.be.object.display.name": "상태가 없고 equals가 재정의(overridden)된 sealed 하위 클래스",
  "inspection.public.api.implicit.type.display.name": "암시적 반환 유형이 있는 Public API 선언",
  "inspection.redundant.companion.reference.display.name": "중복된 'Companion' 참조",
  "inspection.convert.pair.constructor.to.to.function.display.name": "Pair 생성자를 'to' 함수로 변환",
  "inspection.redundant.not.null.extension.receiver.of.inline.display.name": "Kotlin 1.2까지 'inline fun' 확장 수신자는 명시적으로 null을 허용할 수 있습니다.",
  "inspection.platform.extension.receiver.of.inline.display.name": "Kotlin 1.2까지 수신자가 null을 허용할 수 있는 'inline fun'",
  "inspection.scope.function.conversion.display.name": "범위(Scope) 함수를 다른 함수로 변환할 수 있습니다.",
  "inspection.redundant.object.type.check.display.name": "객체에 대한 관용적이지 않은 'is' 유형 검사",
  "inspection.fake.jvm.field.constant.display.name": "Java 상수로 사용되는 Kotlin의 const가 아닌 속성",
  "inspection.may.be.constant.display.name": "'const'일 수 있습니다.",
  "inspection.sort.modifiers.display.name": "정식(Canonical)이 아닌 제어자 순서",
  "inspection.redundant.suspend.modifier.display.name": "중복되는 'suspend' 제어자",
  "inspection.replace.put.with.assignment.display.name": "'map.put()'을 할당으로 변환할 수 있습니다.",
  "inspection.replace.addAll.with.mapTo.display.name": "'addAll(map/filter {})'를 'mapTo/filterTo'로 바꿀 수 있습니다.",
  "inspection.replace.to.with.infix.form.display.name": "'to' 호출을 중위(infix) 형태로 바꿔야 합니다.",
  "inspection.recursive.equals.call.display.name": "재귀적인 equals 호출",
  "inspection.java.collections.static.method.on.immutable.list.display.name": "불변(immutable) Kotlin 컬렉션에 대한 Java mutator 메서드 호출",
  "inspection.java.collections.static.method.display.name": "Java Collections 정적 메서드 호출을 Kotlin stdlib로 바꿀 수 있습니다.",
  "inspection.simplify.when.with.boolean.constant.condition.display.name": "간소화 가능한 'when'",
  "inspection.implicit.nullable.nothing.type.display.name": "암시적 'Nothing?' 유형",
  "inspection.self.assignment.display.name": "중복되는 할당",
  "inspection.redundant.unit.expression.display.name": "중복되는 'Unit'",
  "inspection.implicit.this.display.name": "암시적 'this'",
  "inspection.implicit.this.action.name": "명시적 'this' 추가",
  "inspection.explicit.this.display.name": "중복되는 명시적 'this'",
  "inspection.migrate.diagnostic.suppression.display.name": "진단 이름을 교체해야 합니다.",
  "inspection.redundant.setter.display.name": "중복되는 속성 setter",
  "inspection.remove.redundant.qualifier.name.display.name": "중복되는 한정자 이름",
  "inspection.remove.redundant.backticks.display.name": "중복되는 백틱(backtick)",
  "inspection.redundant.getter.display.name": "중복되는 속성 getter",
  "inspection.suspicious.equals.combination.display.name": "== 및 ===의 의심스러운 조합",
  "inspection.kotlin.redundant.override.display.name": "중복되는 재정의(override) 메서드",
  "inspection.kotlin.redundant.suppression.display.name": "중복되는 진단 숨김(suppression)",
  "inspection.package.name.display.name": "패키지 명명 규칙",
  "inspection.local.variable.name.display.name": "지역 변수 명명 규칙",
  "inspection.const.property.name.display.name": "Const 속성 명명 규칙",
  "inspection.private.property.name.display.name": "Private 속성 명명 규칙",
  "inspection.object.property.name.display.name": "객체 속성 명명 규칙",
  "inspection.object.private.property.name.display.name": "객체 private 속성 명명 규칙",
  "inspection.property.name.display.name": "속성 명명 규칙",
  "inspection.test.function.name.display.name": "테스트 함수 명명 규칙",
  "inspection.function.name.display.name": "함수 명명 규칙",
  "inspection.enum.entry.name.display.name": "Enum 항목 명명 규칙",
  "inspection.class.name.display.name": "클래스 명명 규칙",
  "inspection.redundant.lambda.arrow.display.name": "중복되는 람다 화살표"
}

with open('missing_translations/missing_keys_korean.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

filename = "KotlinBundle.properties"
found = False
for file_entry in data.get('new_files', []):
    if file_entry['filename'] == filename:
        file_entry['keys'].update(ko_dict)
        found = True
        break
if not found:
    data.setdefault('new_files', []).append({"filename": filename, "keys": ko_dict})

print(f"Updated {filename} (Keys 1791-1840)")

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
