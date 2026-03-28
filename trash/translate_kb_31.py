import json

ko_dict = {
  "replace.index.loop.with.collection.loop.quick.fix.text": "요소를 통한 루프로 바꾸기",
  "replace.manual.range.with.indices.call.quick.fix.text": "indices로 바꾸기",
  "range.could.be.replaced.with.indices.call": "범위를 '.indices' 호출로 바꿀 수 있습니다.",
  "for.loop.over.indices.could.be.replaced.with.loop.over.elements": "인덱스에 대한 for 루프를 요소에 대한 루프로 바꿀 수 있습니다.",
  "replace.negated.0.with.1": "부정된 ''{0}''을(를) ''{1}''(으)로 바꾸기",
  "replace.with.elvis.return.fix.text": "''?: return{0}''으로 바꾸기",
  "replace.with.return": "'!!'를 '?: return'으로 바꾸기",
  "convert.put.to.assignment": "put을 할당으로 변환",
  "map.put.should.be.converted.to.assignment": "map.put()을 할당으로 변환해야 합니다.",
  "add.all.should.be.replaced.with.map.to": "''{0}({1} '{}')''은(는) ''{1}''(으)로 바꿔야 합니다.",
  "plus.assign.should.be.replaced.with.map.to": "''+= {0} '{}'''은(는) ''{0}''(으)로 바꿔야 합니다.",
  "replace.with.map.to": "''{0}''(으)로 바꾸기",
  "replace.int.range.end.inclusive.with.last.quick.fix.text": "'endInclusive'를 'last'로 바꾸기",
  "replace.int.range.start.with.first.quick.fix.text": "'start'를 'first'로 바꾸기",
  "could.be.replaced.with.unboxed.last": "언박싱된 'last'로 바꿀 수 있습니다.",
  "could.be.replaced.with.unboxed.first": "언박싱된 'first'로 바꿀 수 있습니다.",
  "replace.with.until.quick.fix.text": "'until'로 바꾸기",
  "replace.with.rangeUntil.quick.fix.text": "'..<'로 바꾸기",
  "replace.with.string.literal.fix.family.name": "문자열 템플릿으로 바꾸기",
  "replace.tostring.with.string.template": "'toString'을 문자열 템플릿으로 바꾸기",
  "replace.to.with.infix.form.quickfix.text": "'to'를 중위 형식으로 바꾸기",
  "replace.with.enum.map.fix.text": "'EnumMap'으로 바꾸기",
  "replaceable.with.enummap": "'EnumMap'으로 바꿀 수 있습니다.",
  "replace.with.operator.assignment": "연산자 할당으로 바꾸기",
  "replaceable.with.operator.assignment": "연산자 할당으로 바꿀 수 있습니다.",
  "replace.with.if.fix.text": "'if' 유형 검사로 바꾸기",
  "replace.with.safe.cast.text": "안전한 캐스트로 바꾸기",
  "should.be.replaced.with.if.type.check": "'if' 유형 검사로 바꿔야 합니다.",
  "replace.unsafe.cast.with.safe.one.text": "안전하지 않은 캐스트를 안전한 캐스트로 바꾸기",
  "call.is.replaceable.with.another.scope.function": "호출을 다른 범위 함수로 바꿀 수 있습니다.",
  "convert.scope.function.fix.family.name": "''{0}''(으)로 변환",
  "variable.0.is.assigned.to.itself": "변수 ''{0}''이(가) 자신에게 할당되었습니다.",
  "remove.self.assignment.fix.text": "자체 할당 제거",
  "convert.to.nullable.type.fix.text": "null 허용 유형으로 변환",
  "constructor.has.non.null.self.reference.parameter": "생성자에 null이 아닌 자체 참조 매개변수가 있습니다.",
  "assign.backing.field.fix.text": "지원 필드 할당",
  "existing.backing.field.is.not.assigned.by.the.setter": "기존 지원 필드가 setter에 의해 할당되지 않았습니다.",
  "replace.with.error": "'?: error(...)'로 바꾸기",
  "replace.assert.with.operator": "assert를 연산자로 바꾸기",
  "assert.should.be.replaced.with.operator": "assert를 연산자로 바꿔야 합니다.",
  "simplify.negated.operation": "부정 연산 간소화",
  "negated.operation.can.be.simplified": "부정 연산을 간소화할 수 있습니다.",
  "replace.negated.0.operation.with.1": "부정된 ''{0}'' 연산을 ''{1}''(으)로 바꾸기",
  "replace.negated.0.operation.with.1.may.change.semantics.with.floating.point.types": "부정된 ''{0}'' 연산을 ''{1}''(으)로 바꾸기 (부동 소수점 유형에서 의미가 변경될 수 있음)",
  "simplify.when.fix.text": "'when' 간소화",
  "this.when.is.simplifiable": "이 'when'은 간소화할 수 있습니다.",
  "sort.modifiers": "한정자 정렬",
  "non.canonical.modifiers.order": "비표준 한정자 순서",
  "modifiers.should.follow.annotations": "한정자는 주석 뒤에 와야 합니다.",
  "remove.as.dynamic.call.fix.text": "'asDynamic' 호출 제거"
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

print(f"Updated {filename} (Keys 1241-1290)")

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
