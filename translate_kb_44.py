import json

ko_dict = {
  "inspection.redundant.lambda.or.anonymous.function.display.name": "람다 또는 익명 함수의 중복 생성",
  "inspection.redundant.lambda.description": "중복된 람다 생성",
  "inspection.redundant.anonymous.function.description": "중복된 익명 함수 생성",
  "inspection.redundant.lambda.or.anonymous.function.fix": "본문을 인라인으로 표시",
  "inspection.when.with.only.else.display.name": "'when'에 'else' 분기만 있으며 간소화할 수 있습니다.",
  "inspection.when.with.only.else.action.name": "'else' 분기만 있는 'when' 간소화",
  "inspection.kotlin.double.negation.display.name": "중복되는 이중 부정",
  "inspection.kotlin.double.negation.action.name": "중복되는 이중 부정 제거",
  "inspection.unnecessary.variable.display.name": "불필요한 지역 변수",
  "inspection.unnecessary.variable.option.report.immediately.returned.variables": "즉시 반환되는 변수 보고",
  "inspection.constant.condition.if.display.name": "'if' 표현식의 조건이 상수입니다.",
  "inspection.null.checks.to.safe.call.display.name": "Null 검사를 안전한 호출(safe-call)로 바꿀 수 있습니다.",
  "inspection.cascade.if.display.name": "계단식(Cascade) 'if'를 'when'으로 바꿀 수 있습니다.",
  "inspection.lift.return.or.assignment.display.name": "return 또는 할당을 리프트(lift)할 수 있습니다.",
  "inspection.lift.return.or.assignment.option.only.single.statement": "각 분기가 단일 문일 경우에만 보고",
  "inspection.use.expression.body.display.name": "여기서는 표현식 본문 구문이 더 적합합니다.",
  "inspection.simplifiable.call.chain.display.name": "컬렉션 유형의 호출 체인을 간소화할 수 있습니다.",
  "inspection.redundant.call.on.collection.display.name": "컬렉션 유형에 대한 중복 호출",
  "inspection.redundant.explicit.type.display.name": "명확한 명시적 유형",
  "inspection.redundant.call.on.not.null.display.name": "not-null 유형에 대한 중복 호출",
  "inspection.remove.redundant.spread.operator.display.name": "중복되는 스프레드(spread) 연산자 제거",
  "inspection.empty.range.display.name": "시작이 endInclusive보다 큰 범위는 비어 있습니다.",
  "inspection.wrap.unary.operator.display.name": "숫자 상수와 단항 연산자를 모호하게 사용",
  "inspection.nullable.boolean.elvis.display.name": "null을 허용하는 부울 검사를 위해 elvis 대신 동등성 검사(equality check)를 사용할 수 있습니다.",
  "inspection.nullable.boolean.elvis.action.name": "null을 허용하는 부울 검사를 위해 elvis 대신 동등성 검사 사용",
  "inspection.member.visibility.can.be.private.display.name": "클래스 멤버가 'private' 가시성을 가질 수 있습니다.",
  "inspection.replace.range.to.with.until.display.name": "'rangeTo' 또는 '..' 호출을 'until'로 바꿔야 합니다.",
  "inspection.replace.range.to.with.rangeUntil.display.name": "'rangeTo' 또는 '..' 호출을 '..<'로 바꿔야 합니다.",
  "inspection.recursive.property.accessor.display.name": "재귀적인 속성 접근자",
  "inspection.replace.array.of.with.literal.display.name": "'arrayOf' 호출을 배열 리터럴 [...]로 바꿀 수 있습니다.",
  "inspection.copy.without.named.arguments.display.name": "데이터 클래스의 'copy' 메서드가 명명된 인수 없이 호출되었습니다.",
  "inspection.move.suspicious.callable.reference.into.parentheses.display.name": "람다 결과로 사용되는 의심스러운 호출 가능 참조",
  "inspection.kotlin.internal.in.java.display.name": "Java에서 Kotlin internal 선언 사용",
  "inspection.kotlin.sealed.in.java.display.name": "Java에서 Kotlin sealed 인터페이스/클래스 상속",
  "inspection.unused.lambda.expression.body.display.name": "람다 표현식 본문이 있는 함수의 사용되지 않는 반환 값",
  "inspection.destructuring.wrong.name.display.name": "구조 분해(destructuring) 선언의 변수가 잘못된 데이터 클래스 속성의 이름을 사용합니다.",
  "inspection.data.class.private.constructor.display.name": "Private 데이터 클래스 생성자가 'copy' 메서드를 통해 공개되었습니다.",
  "inspection.replace.with.enum.map.display.name": "'HashMap'을 'EnumMap'으로 바꿀 수 있습니다.",
  "inspection.unused.equals.display.name": "사용되지 않는 equals 표현식",
  "inspection.convert.na.n.equality.display.name": "'NaN'과의 동등성 검사를 'isNaN' 호출로 변환",
  "inspection.convert.two.comparisons.to.range.check.display.name": "두 개의 비교를 범위 검사로 변환해야 합니다.",
  "inspection.convert.try.finally.to.use.call.display.name": "try / finally를 use() 호출로 변환",
  "inspection.join.declaration.and.assignment.display.name": "선언과 할당 결합",
  "inspection.remove.empty.secondary.constructor.body.display.name": "중복되는 보조 생성자 본문",
  "inspection.remove.empty.primary.constructor.display.name": "중복되는 빈 기본 생성자",
  "inspection.remove.redundant.calls.of.conversion.methods.display.name": "중복되는 변환 메서드 호출",
  "inspection.remove.empty.class.body.display.name": "빈 클래스 본문 교체(제거)",
  "inspection.replace.size.zero.check.with.is.empty.display.name": "크기가 0인지 확인하는 코드를 'isEmpty()'로 바꿀 수 있습니다.",
  "inspection.replace.size.check.with.is.not.empty.display.name": "크기 확인을 'isNotEmpty()'로 바꿀 수 있습니다.",
  "inspection.convert.secondary.constructor.to.primary.display.name": "기본 생성자로 변환"
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

print(f"Updated {filename} (Keys 1841-1890)")

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
