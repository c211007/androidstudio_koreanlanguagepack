import json

ko_dict = {
  "invert.if.condition": "'if' 조건 반전",
  "iterate.over.0": "''{0}''에 대해 반복(Iterate)하기",
  "iterate.over.collection": "컬렉션에 대해 반복하기",
  "join.declaration.and.assignment": "선언과 할당 결합",
  "can.be.joined.with.assignment": "할당과 결합할 수 있습니다.",
  "put.arguments.on.one.line": "인수를 한 줄에 배치",
  "put.parameters.on.one.line": "매개변수를 한 줄에 배치",
  "convert.lambda.expression.to.anonymous.function": "람다 표현식을 익명 함수로 변환",
  "convert.to.anonymous.function": "익명 함수로 변환",
  "merge.else.if": "'else if' 병합",
  "merge.if.s": "'if' 병합",
  "move.lambda.argument.into.parentheses": "람다 인수를 괄호 안으로 이동",
  "class.0.already.contains.1": "''{0}'' 클래스에 이미 {1}이(가) 포함되어 있습니다.",
  "0.in.1.will.require.class.instance": "{1}의 ''{0}''에는 클래스 인스턴스가 필요합니다.",
  "the.package.0.does.not.match.the.implicit.prefix.1": "선택한 패키지 ''{0}''이(가) 대상의 암시적 패키지 접두사 ''{1}''과(와) 호환되지 않습니다. 리팩터링을 수행하면 암시적 패키지 접두사가 손상됩니다.",
  "searching.for.0": "{0} 검색 중",
  "move.out.of.companion.object": "companion object 밖으로 이동",
  "calls.with.explicit.extension.receiver.won.t.be.processed.0": "명시적 확장 수신자가 있는 호출은 처리되지 않습니다: {0}",
  "usages.of.outer.class.instance.inside.of.property.0.won.t.be.processed": "''{0}'' 속성 내에서 외부 클래스 인스턴스 사용은 처리되지 않습니다.",
  "usages.of.outer.class.instance.inside.declaration.0.won.t.be.processed": "선언 ''{0}'' 내에서 외부 클래스 인스턴스 사용은 처리되지 않습니다.",
  "usages.of.nested.declarations.from.non.kotlin.code.won.t.be.processed": "Kotlin이 아닌 코드의 중첩된 선언 사용은 처리되지 않습니다.",
  "companion.object.already.contains.0": "companion object에 이미 {0}이(가) 포함되어 있습니다.",
  "0.references.type.parameters.of.the.containing.class": "{0}이(가) 포함하는(containing) 클래스의 유형 매개변수를 참조합니다.",
  "0.is.overridden.by.declaration.s.in.a.subclass": "{0}이(가) 하위 클래스의 선언에 의해 재정의(override)되었습니다.",
  "move.to.companion.object": "companion object로 이동",
  "move.to.companion.object.command": "보조(Companion) 객체로 이동",
  "moving.to.companion.object": "companion object로 이동하는 중\\u2026",
  "move.to.top.level": "최상위(top level)로 이동",
  "package.0.already.contains.1": "''{0}'' 패키지에 이미 {1}이(가) 포함되어 있습니다.",
  "move.to.class.body": "클래스 본문으로 이동",
  "move.to.constructor": "생성자로 이동",
  "convert.boolean.const.to.elvis": "Boolean? == const를 elvis로 변환",
  "convert.object.literal.to.lambda": "객체 리터럴을 람다로 변환",
  "convert.to.lambda": "람다로 변환",
  "replace.by.0": "''{0}''(으)로 바꾸기",
  "replace.by.reconstructed.type": "재구성된 유형으로 바꾸기",
  "remove.argument.name": "인수 이름 제거",
  "remove.all.argument.names": "모든 인수 이름 제거",
  "remove.braces.from.when.entry": "'when' 항목에서 중괄호 제거",
  "remove.braces.from.0.statement": "''{0}'' 문에서 중괄호 제거",
  "remove.braces": "중괄호 제거",
  "remove.braces.from.all.branches": "모든 분기에서 중괄호 제거",
  "remove.braces.from.if.all.statements": "모든 'if' 문에서 중괄호 제거",
  "remove.braces.from.when.all.entries": "모든 'when' 항목에서 중괄호 제거",
  "redundant.empty.class.body": "중복되는 빈 클래스 본문",
  "remove.redundant.empty.class.body": "중복되는 빈 클래스 본문 제거",
  "remove.unnecessary.parentheses.from.function.call.with.lambda": "람다가 있는 함수 호출에서 불필요한 괄호 제거",
  "remove.empty.primary.constructor": "빈 기본 생성자 제거",
  "remove.empty.constructor.body": "빈 생성자 본문 제거",
  "remove.explicit.lambda.parameter.types.may.break.code": "명시적 람다 매개변수 유형 제거(코드가 손상될 수 있음)"
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

print(f"Updated {filename} (Keys 1491-1540)")

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
