import json

ko_dict = {
  "add.explicit.parameter.to.outer.lambda.fix.text": "외부 람다에 명시적 매개변수 이름 추가",
  "implicit.parameter.it.of.enclosing.lambda.is.shadowed": "둘러싸는 람다의 암시적 매개변수 'it'이 가려집니다",
  "equality.check.0.be.used.instead.of.elvis.for.nullable.boolean.check": "null 허용 부울 검사를 위해 엘비스 연산자 대신 동등성 검사 {0}을(를) 사용해야 합니다.",
  "replace.with.equality.check.fix.text": "동등성 검사로 바꾸기",
  "null.checks.to.safe.call.check.fix.text": "연결된 null 검사를 안전한 호출(safe-call)로 바꾸기",
  "null.checks.replaceable.with.safe.calls": "null 검사를 안전한 호출(safe-call)로 바꿀 수 있습니다.",
  "optionally.expected.annotation.has.no.actual.annotation.in.module.0.for.platform.1": "선택적으로 예상된(expected) 주석에는 플랫폼 {1}의 모듈 {0}에 실제(actual) 주석이 없습니다.",
  "call.of.inline.function.with.nullable.extension.receiver.can.cause.npe.in.kotlin.1.2": "null 허용 수신자가 있는 'inline fun' 호출은 Kotlin 1.2 이전까지 'NPE'를 일으킬 수 있습니다.",
  "make.open.fix.text": "클래스를 open으로 만들기",
  "make.private.fix.text": "비공개(private)로 만들기",
  "protected.visibility.is.effectively.private.in.a.final.class": "final 클래스에서 'protected' 가시성은 실질적으로 'private'입니다.",
  "apply.also.to.private.members": "비공개(private) 멤버에도 적용",
  "apply.also.to.internal.members": "내부(internal) 멤버에도 적용",
  "for.api.stability.it.s.recommended.to.specify.explicitly.declaration.types": "API 안정성을 위해 선언 유형을 명시적으로 지정하는 것이 좋습니다.",
  "for.api.stability.it.s.recommended.to.specify.explicitly.public.protected.declaration.types": "API 안정성을 위해 비공개(public) 및 보호된(protected) 선언 유형을 명시적으로 지정하는 것이 좋습니다.",
  "recursive.equals.call": "재귀적인 equals 호출",
  "replace.with.field.fix.text": "'field'로 바꾸기",
  "recursive.synthetic.property.accessor": "재귀적인 합성 속성 접근자",
  "recursive.property.accessor": "재귀적인 속성 접근자",
  "remove.redundant.companion.reference.fix.text": "중복 Companion 참조 제거",
  "redundant.companion.reference": "중복 Companion 참조",
  "remove.redundant.else.fix.text": "중복 'else' 제거",
  "redundant.else": "중복 'else'",
  "print.should.be.replaced.with.logging.display.name": "'print()' 또는 'println()' 호출",
  "uses.of.should.be.replaced.with.logging": "<code>{0}</code>의 사용은 더 강력한 로깅으로 바꾸는 것이 좋습니다.",
  "remove.initializer.block.fix.text": "초기화자 블록 제거",
  "redundant.empty.initializer.block": "중복인 빈 초기화자 블록",
  "remove.enum.constructor.invocation.fix.text": "enum 생성자 호출 제거",
  "redundant.enum.constructor.invocation": "중복 enum 생성자 호출",
  "explicitly.given.type.is.redundant.here": "명시적으로 지정된 유형이 여기에 중복됩니다.",
  "remove.redundant.getter.fix.text": "중복 getter 제거",
  "remove.redundant.getter.body.fix.text": "중복 getter 본문 제거",
  "redundant.getter": "중복 getter",
  "redundant.getter.body": "중복 getter 본문",
  "remove.redundant.constructor.keyword.fix.text": "중복 'constructor' 키워드 제거",
  "redundant.constructor.keyword": "중복 'constructor' 키워드",
  "remove.redundant.if.text": "중복 'if' 문 제거",
  "remove.redundant.if.may.change.semantics.with.floating.point.types": "중복 'if' 문 제거 (부동 소수점 유형의 의미가 변경될 수 있음)",
  "redundant.if.statement": "중복 'if' 문",
  "redundant.if.option.ignore.chained": "연결된 'if' 문 무시",
  "redundant.if.statement.analyzing.type": "조건 유형 분석 중\\u2026",
  "delete.fix.family.name": "화살표 제거",
  "redundant.lambda.arrow": "중복 람다 화살표",
  "remove.let.call": "'let' 호출 제거",
  "redundant.let.call.could.be.removed": "중복 'let' 호출을 제거할 수 있습니다.",
  "redundant.modality.modifier": "중복 양상(modality) 한정자",
  "this.type.probably.can.be.changed.to.nullable": "이 유형은 null 허용으로 변경될 수 있습니다.",
  "redundant.type.checks.for.object": "객체에 대한 중복 유형 검사",
  "replace.with.equality.fix.text": "''{0}''을(를) ''{1}''(으)로 바꾸기",
  "redundant.0.call": "중복 ''{0}'' 호출"
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

print(f"Updated {filename} (Keys 1141-1190)")

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
