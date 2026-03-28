import json

ko_dict = {
  "inspection.redundant.sam.constructor.display.name": "중복되는 SAM 생성자",
  "inspection.kotlin.unused.import.display.name": "사용되지 않는 가져오기(import) 지시문",
  "inspection.kotlin.unused.variable.display.name": "사용되지 않는 변수",
  "inspection.unused.receiver.parameter.display.name": "사용되지 않는 수신자 매개변수",
  "inspection.unused.symbol.display.name": "사용되지 않는 기호(symbol)",
  "inspection.unused.flow.display.name": "사용되지 않는 flow",
  "inspection.use.property.access.syntax.display.name": "속성 접근 구문으로 바꿀 수 있는 접근자 호출",
  "inspection.simplify.boolean.with.constants.display.name": "부울 표현식을 간소화할 수 있습니다.",
  "inspection.remove.curly.braces.from.template.display.name": "문자열 템플릿의 중복되는 중괄호",
  "inspection.introduce.when.subject.display.name": "인수를 도입하여 간소화할 수 있는 'when'",
  "inspection.replace.with.operator.assignment.display.name": "할당을 연산자 할당으로 바꿀 수 있습니다.",
  "inspection.simplify.negated.binary.expression.display.name": "부정된 이항 표현식을 간소화할 수 있습니다.",
  "inspection.remove.explicit.super.qualifier.display.name": "불필요한 상위 유형 한정자",
  "inspection.remove.explicit.type.arguments.display.name": "불필요한 유형 인수",
  "inspection.fold.initializer.and.if.to.elvis.display.name": "'?:' 로 접을 수 있는 If-Null 반환/break/...",
  "inspection.if.then.to.safe.access.display.name": "'?.' 로 접을 수 있는 If-Then",
  "inspection.if.then.to.elvis.display.name": "'?:' 로 접을 수 있는 If-Then",
  "inspection.map.can.be.replaced.with.for.each.display.name": "'map' 호출을 'forEach'로 바꿀 수 있습니다.",
  "inspection.map.can.be.replaced.with.for.each.warning": "''{0}'' 호출을 'forEach'로 바꿀 수 있습니다.",
  "inspection.redundant.return.keyword.display.name": "중복되는 'return' 키워드",
  "inspection.redundant.return.keyword.action.name": "'return' 키워드 제거",
  "inspection.replace.manual.range.with.indices.calls.display.name": "범위를 indices 또는 반복(iteration)으로 변환할 수 있습니다.",
  "inspection.replace.until.with.rangeUntil.operator.display.name": "'until'을 '..<' 연산자로 바꾸기",
  "inspection.replace.get.or.set.display.name": "명시적 'get' 또는 'set' 호출",
  "inspection.convert.to.string.template.display.name": "문자열 템플릿으로 변환할 수 있는 문자열 연결",
  "inspection.deprecated.callable.add.replace.with.display.name": "'replaceWith' 인수가 없는 @Deprecated 주석",
  "inspection.replace.collection.count.with.size.display.name": "컬렉션 개수(count)를 크기(size)로 변환할 수 있습니다.",
  "inspection.simplify.assert.not.null.display.name": "'assert' 호출을 '!!' 또는 '?:'로 바꿀 수 있습니다.",
  "inspection.object.literal.to.lambda.display.name": "객체 리터럴을 람다로 변환할 수 있습니다.",
  "inspection.object.exception.to.class.display.name": "Exception은 객체(object)이면 안 됩니다.",
  "inspection.object.exception.to.class.warning": "Exception은 객체(object)이면 안 됩니다.",
  "inspection.object.exception.to.class.quick.fix.name": "Exception 객체를 클래스로 변경",
  "remove.redundant.elvis.return.null.text": "중복되는 '?: return null' 제거",
  "inspection.redundant.elvis.return.null.descriptor": "중복되는 '?: return null'",
  "inspection.redundant.elvis.return.null.display.name": "중복되는 '?: return null'",
  "inspection.redundant.inner.class.modifier.descriptor": "중복되는 'inner' 제어자",
  "inspection.redundant.inner.class.modifier.display.name": "중복되는 'inner' 제어자",
  "inspection.redundant.interpolation.prefix.display.name": "중복되는 보간(interpolation) 접두사",
  "inspection.redundant.interpolation.prefix.problem.description": "중복되는 보간 접두사",
  "inspection.redundant.interpolation.prefix.quick.fix.text": "중복되는 보간 접두사 제거",
  "inspection.remove.interpolation.prefix.display.name": "제거 가능한 다중 달러(multi-dollar) 보간 접두사",
  "inspection.remove.interpolation.prefix.problem.description": "문자열 접두사를 제거할 수 있습니다.",
  "inspection.remove.interpolation.prefix.quick.fix.text": "다중 달러 접두사 제거",
  "inspection.unused.lambda.expression.inspection.display.name": "사용되지 않는 람다 표현식",
  "inspection.unused.lambda.expression.inspection.problem.description": "람다 표현식이 호출되지 않았습니다. 범위 지정 블록을 만들려면 'run { ... }'을 사용하세요.",
  "inspection.unused.expression.display.name": "사용되지 않는 표현식",
  "inspection.unused.expression.problem.description": "표현식이 사용되지 않습니다.",
  "fix.remove.annotation.text": "주석 제거",
  "inspection.trailing.comma.display.name": "후행 쉼표 권장 사항",
  "inspection.trailing.comma.report.also.a.missing.comma": "누락된 쉼표 또는 줄바꿈도 보고"
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

print(f"Updated {filename} (Keys 1891-1940)")

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
