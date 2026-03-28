import json

ko_dict = {
  "text.primary.constructor": "기본 생성자",
  "function.0": "함수 ''{0}''",
  "looking.for.usages.in.java.files": "Java 파일에서 사용법을 찾는 중\\u2026",
  "add.return.at.0": "''return@{0}'' 추가",
  "add.0.to.argument": "인수에 ''{0} ='' 추가",
  "add.val.var.to.parameter.0": "''{0}'' 매개변수에 ''val'' 또는 ''var'' 추가",
  "add.val.to.parameter.0": "''{0}'' 매개변수에 ''val'' 추가",
  "add.val.var.to.primary.constructor.parameter": "기본 생성자 매개변수에 'val' 또는 'var' 추가",
  "make.primary.constructor.0": "기본 생성자를 {0}(으)로 만들기",
  "change.visibility": "가시성 변경",
  "change.visibility.popup": "가시성 변경",
  "change.visibility.modifier": "가시성 제어자 변경",
  "0.may.break.code": "{0} (코드가 손상될 수 있음)",
  "convert.to.vararg.parameter": "가변 인자(vararg) 매개변수로 변환",
  "replace.||.with.&&": "'||'를 '\\\\&\\\\&'로 바꾸기",
  "replace.&&.with.||": "'\\\\&\\\\&'를 '||'로 바꾸기",
  "can.t.modify.0": "{0}을(를) 수정할 수 없습니다.",
  "0.already.exists": "{0}이(가) 이미 존재합니다.",
  "type.arguments.will.be.lost.after.conversion.0": "변환 후 유형 인수가 손실됩니다: {0}",
  "call.with.arguments.will.be.skipped.0": "인수가 있는 호출을 건너뜁니다: {0}",
  "looking.for.usages.and.conflicts": "사용법 및 충돌을 찾는 중\\u2026",
  "following.expression.won.t.be.processed.since.refactoring.can.t.preserve.its.semantics.0": "리팩터링이 해당 의미 체계를 보존할 수 없기 때문에 다음 표현식은 처리되지 않습니다: {0}",
  "callable.reference.transformation.is.not.supported.0": "호출 가능한 참조 변환이 지원되지 않습니다: {0}",
  "can.t.replace.non.kotlin.reference.with.call.expression.0": "Kotlin이 아닌 참조를 호출 표현식으로 바꿀 수 없습니다: {0}",
  "convert.0.to.1": "''{0}''을(를) ''{1}''(으)로 변환",
  "convert.lambda.to.reference.before.text": "람다를 참조로 변환할 수 있습니다.",
  "convert.lambda.to.reference": "람다를 참조로 변환",
  "select.target.code.block.file": "대상 코드 블록/파일 선택",
  "select.target.file": "대상 파일 선택",
  "replace.expression.with.if.expression": "'!!' 표현식을 'if' 표현식으로 바꾸기",
  "inline.when.argument": "'when' 인수 인라인화",
  "replace.elvis.expression.with.if.expression": "Elvis 표현식을 'if' 표현식으로 바꾸기",
  "flatten.when.expression": "'when' 표현식 병합(Flatten)",
  "replace.if.expression.with.return": "'if' 표현식을 return으로 바꾸기",
  "lift.return.out.of.if.expression": "'if' 표현식 밖으로 return 리프트(Lift)",
  "replace.if.with.when": "'if'를 'when'으로 바꾸기",
  "replace.if.with.when.changes.semantics": "'if'를 'when'으로 바꾸기(의미 체계 변경됨)",
  "add.clarifying.braces.to.nested.else.statement": "중첩된 'else' 문에 명확성을 위한 중괄호 추가",
  "replace.safe.access.expression.with.if.expression": "안전한 접근(safe access) 표현식을 'if' 표현식으로 바꾸기",
  "replace.assignment.with.if.expression": "할당을 'if' 표현식으로 바꾸기",
  "replace.assignment.with.when.expression": "할당을 'when' 표현식으로 바꾸기",
  "replace.property.initializer.with.if.expression": "속성 초기화자를 'if' 표현식으로 바꾸기",
  "replace.property.initializer.with.when.expression": "속성 초기화자를 'when' 표현식으로 바꾸기",
  "replace.return.with.if.expression": "return을 'if' 표현식으로 바꾸기",
  "replace.return.with.when.expression": "return을 'when' 표현식으로 바꾸기",
  "replace.when.with.if": "'when'을 'if'로 바꾸기",
  "replace.call.with.unary.operator": "호출을 단항 연산자로 바꾸기",
  "replace.contains.call.with.in.operator": "'contains' 호출을 'in' 연산자로 바꾸기",
  "replace.contains.call.with.in.operator.description": "Kotlin의 관용적인 'in' 연산자 대신 Java 'contains' 호출 사용",
  "replace.invoke.with.direct.call": "'invoke'를 직접 호출로 바꾸기"
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

print(f"Updated {filename} (Keys 1341-1390)")

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
