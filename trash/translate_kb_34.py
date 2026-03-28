import json

ko_dict = {
  "copy.concatenation.text.to.clipboard": "연결 텍스트를 클립보드에 복사",
  "split.property.declaration": "속성 선언 분할",
  "replace.with.stdlib.operations.with.use.of.assequence": "'asSequence()'를 사용하여 stdlib 연산으로 바꾸기",
  "replace.with.stdlib.operations": "stdlib 연산으로 바꾸기",
  "use.withindex.instead.of.manual.index.increment": "수동으로 인덱스를 증가시키는 대신 withIndex() 사용",
  "add.braces": "중괄호 추가",
  "add.indices.to.for.loop": "'for' 루프에 indices 추가",
  "add.jvmoverloads.annotation": "'@JvmOverloads' 주석 추가",
  "add.jvmstatic.annotation": "'@JvmStatic' 주석 추가",
  "make.member.static.quickfix": "''{0}''을(를) static으로 만들기",
  "making.member.static": "멤버를 static으로 만드는 중\\u2026",
  "add.jvminline.annotation": "'@JvmInline' 주석 추가",
  "add.labeled.return.to.last.expression.in.a.lambda": "람다의 마지막 표현식에 레이블이 지정된 return 추가",
  "add.missing.component": "누락된 구조 분해(destructuring) 구성 요소 추가",
  "add.names.to.call.arguments": "호출 인수에 이름 추가",
  "add.names.in.comment.to.call.arguments": "호출 인수의 주석에 이름 추가",
  "add.names.to.this.argument.and.following.arguments": "이 인수와 뒤따르는 모든 인수에 이름 추가",
  "add.name.to.argument": "인수에 이름 추가",
  "make.open": "'open'으로 만들기",
  "add.throws.annotation": "'@Throws' 주석 추가",
  "add.remaining.branches": "나머지 분기 추가",
  "convert.anonymous.function.to.lambda.expression": "익명 함수를 람다 표현식으로 변환",
  "convert.to.lambda.expression": "람다 표현식으로 변환",
  "put.arguments.on.separate.lines": "인수를 별도의 줄에 배치",
  "put.parameters.on.separate.lines": "매개변수를 별도의 줄에 배치",
  "put.expressions.on.separate.lines": "표현식을 별도의 줄에 배치",
  "put.calls.on.separate.lines": "호출을 별도의 줄에 배치",
  "add.kotlin.coroutines": "Kotlin coroutines 라이브러리 추가",
  "add.kotlin.coroutines.description": "Kotlin Coroutines 라이브러리 추가",
  "add.0.library": "''{0}'' 라이브러리 추가",
  "demorgan.law": "드모르간의 법칙",
  "replace.with.end.of.line.comment": "줄 끝 주석으로 바꾸기",
  "convert.collection.constructor.to.function": "Collection 생성자를 함수로 변환",
  "convert.to.sealed.class": "sealed 클래스로 변환",
  "replace.with.a.for.loop": "'for' 루프로 바꾸기",
  "convert.function.to.property": "함수를 속성으로 변환",
  "convert.function.type.parameter.to.receiver": "함수 유형 매개변수를 수신자로 변환",
  "convert.function.type.receiver.to.parameter": "함수 유형 수신자를 매개변수로 변환",
  "convert.to.nullable.var": "null을 허용하는 var로 변환",
  "convert.to.ordinary.property": "일반 속성으로 변환",
  "replace.with.block.comment": "블록 주석으로 바꾸기",
  "convert.to.lateinit.var": "lateinit var로 변환",
  "convert.object.literal.to.class": "객체 리터럴을 클래스로 변환",
  "convert.to.lazy.property": "lazy 속성으로 변환",
  "convert.parameter.to.receiver": "매개변수를 수신자로 변환",
  "convert.to.secondary.constructor": "보조 생성자로 변환",
  "convert.property.getter.to.initializer": "속성 getter를 초기화자로 변환",
  "convert.property.initializer.to.getter": "속성 초기화자를 getter로 변환",
  "convert.property.to.function": "속성을 함수로 변환",
  "convert.to.multi.dollar.string": "다중 달러 문자열로 변환"
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

print(f"Updated {filename} (Keys 1391-1440)")

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
