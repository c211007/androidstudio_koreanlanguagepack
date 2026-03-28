import json

ko_dict = {
  "leaking.this.in.constructor.of.enum.class.0.with.overridable.members": "재정의 가능한 멤버가 있는 enum 클래스 {0}의 생성자에서 ''this'' 유출됨",
  "accessing.non.final.property.0.in.constructor": "생성자에서 final이 아닌 속성 {0}에 접근함",
  "calling.non.final.function.0.in.constructor": "생성자에서 final이 아닌 함수 {0} 호출함",
  "text.can": "수 있음",
  "text.should": "해야 함",
  "text.Assignment": "할당",
  "text.Return": "반환",
  "text.return": "반환",
  "0.1.be.lifted.out.of.2": "''{0}''을(를) ''{1}'' 밖으로 추출할 수 있습니다.",
  "lift.assignment.out.fix.text.0": "''{0}'' 밖으로 할당 추출",
  "lift.return.out.fix.text.0": "''{0}'' 밖으로 반환 추출",
  "change.main.function.return.type.to.unit.fix.text": "명시적 Unit 반환 유형 추가",
  "change.main.function.return.type.to.unit.fix.text2": "반환 유형을 Unit으로 변경",
  "0.should.return.unit": "{0}은(는) Unit을 반환해야 합니다.",
  "map.get.with.not.null.assertion.operator": "null이 아닌 어설션 연산자 '(!!)'를 사용하는 'map.get()'",
  "replace.with.get.or.else.fix.text": "'getOrElse' 호출로 바꾸기",
  "replace.with.get.value.call.fix.text": "'getValue' 호출로 바꾸기",
  "replace.with.elvis.error.fix.text": "'?: error(\"\")'로 바꾸기",
  "might.be.const": "'const'일 수 있음",
  "const.might.be.used.instead.of.jvmfield": "'@JvmField' 대신 'const'를 사용할 수 있습니다.",
  "text.Function": "함수",
  "text.Property": "속성",
  "0.1.could.be.private": "{0} ''{1}''은(는) 비공개(private)일 수 있습니다.",
  "diagnostic.name.should.be.replaced.by.the.new.one": "진단 이름은 새 이름으로 바꿔야 합니다.",
  "replace.diagnostic.name.fix.text": "{0}을(를) {1}(으)로 조치",
  "replace.diagnostic.name.fix.family.name": "진단 이름 바꾸기",
  "lambda.argument.0.be.moved.out": "람다 인수를 괄호 밖으로 옮길 수 {0,choice,0#있습니다|1#있어야 합니다}.",
  "move.lambda.argument.out.of.parentheses": "괄호 밖으로 람다 인수 이동",
  "suspicious.callable.reference.as.the.only.lambda.element": "의심스러운 콜러블 참조가 유일한 람다 요소로 있습니다.",
  "inline.variable": "변수 인라인",
  "move.variable.declaration.into.when": "변수 선언을 'when'으로 이동",
  "nothing.to.do": "수행할 작업 없음",
  "variable.declaration.could.be.inlined": "변수 선언을 인라인할 수 있습니다.",
  "variable.declaration.could.be.moved.into.when": "변수 선언을 'when'으로 이동할 수 있습니다.",
  "may.contain.only.letters.digits.or.underscores": "문자, 숫자, 밑줄만 포함할 수 있습니다.",
  "may.contain.only.letters.and.digits": "문자와 숫자만 포함할 수 있습니다.",
  "should.not.contain.underscores.in.the.middle.or.the.end": "중간이나 끝에 밑줄을 포함할 수 없습니다.",
  "should.not.contain.underscores.with.camel.case": "카멜 표기법을 사용할 때 밑줄을 포함할 수 없습니다.",
  "should.not.start.with.an.underscore": "밑줄로 시작할 수 없습니다.",
  "should.not.start.with.an.uppercase.letter": "대문자로 시작할 수 없습니다.",
  "should.not.contain.underscores": "밑줄을 포함할 수 없습니다.",
  "should.start.with.a.lowercase.letter": "소문자로 시작해야 합니다.",
  "should.start.with.an.uppercase.letter": "대문자로 시작해야 합니다.",
  "should.not.contain.lowercase.letter": "소문자를 포함할 수 없습니다.",
  "doesn.t.match.regex.0": "정규식 ''{0}''과(와) 일치하지 않습니다.",
  "text.pattern": "패턴:",
  "package.name": "패키지 이름",
  "text.part": "부분",
  "text.name": "이름",
  "text.Package": "패키지"
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

print(f"Updated {filename} (Keys 1191-1240)")

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
