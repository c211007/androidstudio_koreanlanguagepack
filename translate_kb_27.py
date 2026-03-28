import json

ko_dict = {
  "remove.var.keyword.text": "'var' 제거",
  "delegating.to.var.property.does.not.take.its.changes.into.account": "'var' 속성에 위임하면 해당 변경 사항이 고려되지 않습니다.",
  "add.replacewith.argument.to.specify.replacement.pattern": "'replaceWith' 인수를 추가하여 대체 패턴 지정",
  "deprecated.annotation.without.replacewith.argument": "'replaceWith' 인수가 없는 '@Deprecated' 주석",
  "variable.name.0.matches.the.name.of.a.different.component": "변수 이름 ''{0}''이(가) 다른 구성 요소의 이름과 일치합니다.",
  "this.range.is.empty.did.you.mean.to.use.0": "이 범위는 비어 있습니다. ''{0}''을(를) 사용하려고 하셨습니까?",
  "this.range.is.empty": "이 범위는 비어 있습니다.",
  "until.can.be.replaced.with.rangeUntil.operator": "'until'은 '..<' 연산자로 바꿀 수 있습니다.",
  "equals.hashcode.in.object.declaration": "객체 선언의 'equals()'/'hashCode()'",
  "hash.code.text": "'hashCode()' 생성",
  "equals.text": "'equals()' 생성",
  "specify.super.type": "상위 유형 ''{0}''을(를) 명시적으로 지정",
  "delete.equals.and.hash.code.fix.text": "equals()/hashCode() 삭제",
  "redundant.explicit.this": "중복 명시적 this",
  "explicit.this.expression.fix.family.name": "중복 ''{0}'' 제거",
  "use.of.non.const.kotlin.property.as.java.constant.is.incorrect.will.be.forbidden.in.1.4": "const가 아닌 Kotlin 속성을 Java 상수로 사용하는 것은 잘못되었습니다. 1.4에서는 금지됩니다.",
  "replace.if.with.elvis.operator": "'if'를 엘비스 연산자로 바꾸기",
  "if.null.return.break.foldable.to": "If-Null return/break/...를 '?:'로 접을 수 있음",
  "loop.parameter.0.is.unused": "루프 매개변수 ''{0}''이(가) 사용되지 않습니다.",
  "replace.with.repeat.fix.family.name": "'repeat()'로 바꾸기",
  "introduce.anonymous.parameter.fix.family.name": "익명 매개변수 도입",
  "wrap.run.fix.text": "run { ... }으로 변환",
  "remove.braces.fix.text": "중괄호 제거",
  "report.for.types.with.platform.arguments": "플랫폼 인수가 있는 유형에 대해 보고",
  "apply.only.to.public.or.protected.members": "비공개(public) 또는 보호된(protected) 멤버에만 적용",
  "declaration.has.type.inferred.from.a.platform.call.which.can.lead.to.unchecked.nullability.issues": "선언에 플랫폼 호출에서 유추된 유형이 있어 검사되지 않은 null 허용 여부 문제가 발생할 수 있습니다. 유형을 명시적으로 null을 허용하거나 허용하지 않도록 지정하세요.",
  "callable.reference.fix.family.name": "명시적 ''{0}'' 추가",
  "java.collections.static.method.call.should.be.replaced.with.kotlin.stdlib": "Java Collections의 정적 메서드 호출을 Kotlin 표준 라이브러리(stdlib)로 바꿔야 합니다.",
  "replace.with.std.lib.fix.text": "{0}.{1}(으)로 바꾸기",
  "call.of.java.mutator.0.on.immutable.kotlin.collection.1": "불변 Kotlin 컬렉션 ''{1}''에 대한 Java mutator ''{0}'' 호출",
  "replace.with.kotlin.s.foreach": "Kotlin의 forEach로 바꾸기",
  "java.map.foreach.method.call.should.be.replaced.with.kotlin.s.foreach": "Java Map.forEach 메서드 호출을 Kotlin의 forEach로 바꿔야 합니다.",
  "remove.deprecated.symbol.import": "더 이상 사용되지 않는 기호 가져오기 제거",
  "usage.of.redundant.or.deprecated.syntax.or.deprecated.symbols": "중복되거나 중단된 구문 또는 시간 경과에 따라 사용되지 않는 기호 사용",
  "equals.should.take.any.as.its.argument": "'equals'는 인수로 'Any?'를 취해야 합니다.",
  "double.negation.fix.text": "중복 부정 제거",
  "redundant.double.negation": "중복 이중 부정",
  "equals.between.objects.of.inconvertible.types": "변환할 수 없는 유형의 객체 간 'equals()'",
  "usage.of.kotlin.internal.declaration.from.different.module": "다른 모듈의 Kotlin 내부 선언 사용",
  "inheritance.of.kotlin.sealed": "Java {0,choice,0#인터페이스|1#클래스}는 Kotlin 봉인 계층 구조의 일부가 될 수 없습니다.",
  "junit.static.methods": "JUnit 정적 메서드",
  "redundant.override.fix.text": "중복 재정의 메서드 제거",
  "redundant.overriding.method": "중복 재정의 메서드",
  "throwable.instance.0.is.not.thrown": "Throwable 인스턴스 ''{0}''이(가) throw되지 않았습니다.",
  "result.of.0.call.is.not.thrown": "''{0}'' 호출 결과가 throw되지 않았습니다.",
  "optimize.imports": "가져오기 최적화",
  "remove.unused.imports.quickfix.text": "사용하지 않는 가져오기 제거",
  "unused.import.directive": "사용하지 않는 가져오기 지시문",
  "title.lateinit.var.overrides.lateinit.var": "'lateinit var'가 상위 'lateinit var'를 재정의합니다.",
  "leaking.this.in.constructor.of.non.final.class.0": "final이 아닌 클래스 {0}의 생성자에서 ''this'' 유출됨"
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
