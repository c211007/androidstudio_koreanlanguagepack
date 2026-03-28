import json

ko_dict = {
  "inspection.suspicious.collection.reassignment.display.name": "복합 할당(Augmented assignment)은 내부적으로 새 컬렉션을 생성합니다.",
  "inspection.redundant.else.in.if.display.name": "'if'에서 중복되는 'else'",
  "inspection.deferred.is.result.display.name": "Deferred를 직접 반환하는 함수",
  "inspection.map.get.with.not.null.assertion.operator.display.name": "not-null 어서션(assertion) 연산자(!!)를 사용한 'map.get()'",
  "inspection.delegation.to.var.property.display.name": "'var' 속성에 위임",
  "inspection.unused.main.parameter.display.name": "main 매개변수는 필요하지 않습니다.",
  "inspection.suspicious.var.property.display.name": "의심스러운 'var' 속성: setter가 getter 결과에 영향을 주지 않습니다.",
  "inspection.setter.backing.field.assignment.display.name": "할당 없는 기존 배킹 필드(backing field)",
  "inspection.unlabeled.return.inside.lambda.display.name": "람다 내부의 레이블 없는 반환(return)",
  "inspection.optional.expectation.display.name": "선택적 expected 주석에 actual 주석이 없습니다.",
  "inspection.remove.empty.parentheses.from.annotation.entry.display.name": "주석의 중복되는 괄호",
  "inspection.safe.cast.with.return.display.name": "보안 캐스트와 'return'을 'if' 유형 검사로 바꿔야 합니다.",
  "inspection.unsafe.cast.with.return.display.name": "안전하지 않은 캐스트와 'return'을 안전한 캐스트로 바꿔야 합니다.",
  "inspection.remove.unnecessary.parentheses.display.name": "중복되는 괄호",
  "inspection.remove.unnecessary.parentheses.quickfix.text": "중복되는 괄호 제거",
  "inspection.remove.unnecessary.parentheses.problem.description": "중복되는 괄호",
  "inspection.simplifiable.call.display.name": "라이브러리 함수 호출을 간소화할 수 있습니다.",
  "inspection.redundant.run.catching.display.name": "중복되는 'runCatching' 호출",
  "inspection.redundant.return.label.display.name": "중복되는 'return' 레이블",
  "inspection.replace.assert.boolean.with.assert.equality.display.name": "부울 검증(assert boolean)을 논리항 검증(assert equality)으로 바꿀 수 있습니다.",
  "inspection.suspicious.as.dynamic.display.name": "의심스러운 'asDynamic' 멤버 호출",
  "inspection.convert.call.chain.into.sequence.display.name": "성능을 향상시키기 위해 컬렉션의 호출 체인을 'Sequence'로 변환할 수 있습니다.",
  "inspection.redundant.with.display.name": "중복되는 'with' 호출",
  "inspection.add.kotlin.coroutines.display.name": "Kotlin Coroutines 라이브러리 추가",
  "inspection.obsolete.experimental.coroutines.display.name": "실험적 코루틴 사용은 1.3부터 더 이상 사용되지 않습니다(deprecated).",
  "inspection.obsolete.kotlin.js.packages.display.name": "'kotlin.browser' 및 'kotlin.dom' 패키지는 1.4부터 더 이상 사용되지 않습니다.",
  "inspection.warning.on.main.unused.parameter.migration.display.name": "1.4부터 'main'에서 사용되지 않는 'args'",
  "inspection.prohibit.repeated.use.site.target.annotations.migration.display.name": "'@Repeatable'로 표시되지 않은 반복되는 주석",
  "inspection.do.not.propagate.method.deprecation.through.overrides": "1.9부터 재정의(override)를 통해 메서드 사용 중단 상태를 전파하지 않음",
  "inspection.this.class.does.not.have.a.constructor": "금지된 생성자 호출",
  "inspection.deprecated.enum.declaring.class.property": "사용되지 않는(Deprecated) 'Enum.declaringClass' 속성",
  "inspection.non.exhaustive.when.statement.migration.display.name": "1.7부터 포괄적이지 않은 'when' 문은 금지됩니다.",
  "inspection.prohibit.use.site.target.annotations.on.super.types.migration.display.name": "슈퍼클래스에 무의미한 주석 대상이 있습니다.",
  "inspection.redundant.label.migration.display.name": "중복되는 레이블",
  "inspection.ambiguous.expression.when.branch.migration.display.name": "1.7부터 'when' 분기에서 모호한 논리 표현식",
  "inspection.progression.resolution.change.migration.display.name": "1.9부터 진행(Progression) 해결(resolution) 변경 사항",
  "inspection.enum.values.method.soft.deprecate.migration.display.name": "1.9부터 'Enum.values()'를 'Enum.entries'로 교체하는 것이 권장됩니다.",
  "inspection.enum.values.method.soft.deprecate.in.java.display.name": "Kotlin 1.9부터 'Enum.values()'를 'Enum.getEntries()'로 교체하는 것이 권장됩니다.",
  "inspection.add.conversion.call.display.name": "1.9부터 `Int`에서 명시적 변환이 필요합니다.",
  "inspection.deprecated.inline.classes.migration.display.name": "인라인 클래스는 1.5부터 더 이상 사용되지 않습니다.",
  "inspection.deprecated.inline.class.text": "더 이상 사용되지 않는 인라인 클래스",
  "inspection.restrict.return.statement.target.migration.display.name": "1.4부터 대상 레이블이 함수를 나타내지 않습니다.",
  "inspection.prohibit.jvm.overloads.on.constructors.of.annotation.classes.migration.display.name": "1.4부터 주석 클래스의 생성자에 '@JvmOverloads' 주석을 사용할 수 없습니다.",
  "inspection.prohibit.type.parameters.for.local.variables.migration.display.name": "유형 매개변수가 있는 지역 변수",
  "inspection.from.closed.range.migration.display.name": "1.3부터 fromClosedRange()의 MIN_VALUE 단계",
  "inspection.replace.to.string.with.string.template.display.name": "'toString' 호출을 문자열 템플릿으로 바꿀 수 있습니다.",
  "inspection.nested.lambda.shadowed.implicit.parameter.display.name": "중첩된 람다가 암시적 매개변수를 섀도잉(shadowing)합니다.",
  "inspection.for.each.parameter.not.used.display.name": "반복되는(Iterated) 요소가 forEach에서 사용되지 않습니다.",
  "inspection.replace.string.format.with.literal.display.name": "'String.format' 호출을 문자열 템플릿으로 바꿀 수 있습니다.",
  "inspection.deferred.result.unused.display.name": "'@Deferred' 결과가 사용되지 않습니다."
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
