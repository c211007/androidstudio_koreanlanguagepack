import json

ko_dict = {
  "suspicious.asdynamic.member.invocation": "의심스러운 'asDynamic' 멤버 호출",
  "0.on.a.readonly.1.creates.a.new.1.under.the.hood": "읽기 전용 {1}에 대한 ''{0}''은(는) 내부적으로 새 {1}을(를) 생성합니다.",
  "replace.with.filter.fix.text": "filter로 바꾸기",
  "change.type.to.mutable.fix.text": "변경 가능한(mutable) 유형으로 변경",
  "replace.with.assignment.fix.text": "할당으로 바꾸기(원본이 비어 있음)",
  "join.with.initializer.fix.text": "초기화자와 결합",
  "suspicious.combination.of.and": "== 및 ===의 의심스러운 조합",
  "unlabeled.return.inside.lambda": "람다 내부의 레이블 없는 반환",
  "suspicious.var.property.its.setter.does.not.influence.its.getter.result": "의심스러운 'var' 속성: setter가 getter 결과에 영향을 주지 않습니다.",
  "flow.constructed.but.not.used": "Flow가 생성되었지만 사용되지 않음",
  "variable.used.only.in.following.return.and.should.be.inlined": "변수가 뒤따르는 반환에서만 사용되며 인라인될 수 있습니다.",
  "variable.is.same.as.0.and.should.be.inlined": "변수가 ''{0}''과(와) 동일하며 인라인될 수 있습니다.",
  "implicit.unsafe.cast.from.dynamic.to.0": "dynamic에서 {0}(으)로의 암시적(안전하지 않은) 캐스트",
  "cast.explicitly.fix.text": "명시적으로 캐스트",
  "unused.equals.expression": "사용되지 않는 equals 표현식",
  "since.kotlin.1.3.main.parameter.is.not.necessary": "Kotlin 1.3부터 main 매개변수는 필요하지 않습니다.",
  "remove.token.from.function.declaration": "함수 선언에서 '=' 토큰 제거",
  "unused.return.value.of.a.function.with.lambda.expression.body": "람다 표현식 본문이 있는 함수의 사용되지 않는 반환 값",
  "safe.delete.constructor": "안전하게 생성자 삭제",
  "remove.unary.operator.fix.text": "사용되지 않는 단항 연산자 제거",
  "move.unary.operator.to.previous.line.fix.text": "단항 연산자를 이전 줄로 이동",
  "unused.unary.operator": "사용되지 않는 단항 연산자",
  "one.line.return": "한 줄 반환",
  "return.when": "'return when'",
  "block.body": "블록 본문",
  "use.expression.body.instead.of.0": "{0} 대신 표현식 본문 사용",
  "convert.to.expression.body.fix.text": "표현식 본문으로 변환",
  "when.has.only.else.branch.and.should.be.simplified": "'when'에 'else' 분기만 있으므로 간소화해야 합니다.",
  "wrap.unary.operator.quickfix.text": "단항 연산자와 값을 ()로 묶기",
  "make.0.1": "''{0}''을(를) {1}(으)로 만들기",
  "replace.with.0.operator": "''{0}'' 연산자로 바꾸기",
  "do.you.want.to.make.new.extension.an.expected.declaration": "새 확장을 예상되는(expected) 선언으로 만드시겠습니까?",
  "loop.to.call.fix.family.name": "stdlib 연산으로 바꾸기",
  "loop.to.call.fix.family.name2": "'asSequence()'를 사용하여 stdlib 연산으로 바꾸기",
  "loop.can.be.replaced.with.stdlib.operations": "루프를 stdlib 연산으로 바꿀 수 있습니다.",
  "text.add.setter": "setter 추가",
  "text.add.getter": "getter 추가",
  "text.add.getter.and.setter": "getter 및 setter 추가",
  "text.add.use.site.target.0": "사용 지점(use-site) 대상 ''{0}'' 추가",
  "text.change.use.site.target.0": "사용 지점대상을 ''{0}''(으)로 변경",
  "text.enable.annotation.target.feature": "컴파일러 인수 추가: {0}",
  "title.choose.use.site.target": "사용 지점 대상 선택",
  "add.use.site.target": "사용 지점 대상 추가",
  "add.full.qualifier": "전체 한정자 추가",
  "add.braces.to.0.statement": "''{0}'' 문에 중괄호 추가",
  "add.braces.to.when.entry": "'when' 항목에 중괄호 추가",
  "add.braces.to.all.branches": "모든 분기에 중괄호 추가",
  "add.braces.to.if.all.statements": "모든 'if'문에 중괄호 추가",
  "add.braces.to.when.all.entries": "모든 'when' 항목에 중괄호 추가",
  "add.jvmoverloads.annotation.to.0": "{0}에 ''@JvmOverloads'' 주석 추가"
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

print(f"Updated {filename} (Keys 1291-1340)")

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
