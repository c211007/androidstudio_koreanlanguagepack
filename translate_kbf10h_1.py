import json

ko_dict = {
  "kotlin.compiler.error": "Kotlin 컴파일러 오류",
  "kotlin.compiler.warning": "Kotlin 컴파일러 경고",
  "the.following.declarations.have.the.same.jvm.signature.code.0.1.code.br.ul.2.ul": "다음 선언의 JVM 시그니처가 동일합니다(<code>{0}{1}</code>):<br/>\\n<ul>\\n{2}</ul>",
  "unknown.receiver": "알 수 없는 수신자",
  "always.null": "항상 null",
  "smart.cast.to.0.for.1.call": "{0}(으)로 스마트 변환({1} 호출의 경우)",
  "wrapped.into.a.reference.object.to.be.modified.when.captured.in.a.closure": "클로저에서 캡처될 때 수정할 참조 객체로 래핑됨",
  "value.captured.in.a.closure": "클로저에서 캡처된 값",
  "type.parameters.where": "Where:",
  "cannot.be.inferred": "유추할 수 없음",
  "i.for.i.br.0": "<i> for </i><br/>{0}",
  "defined.in": "정의 위치:",
  "root.package": "루트 패키지",
  "function.receiver.0": "수신자: {0}",
  "function.arguments": "인수:\\u0020",
  "html.0.has.no.corresponding.expected.declaration.1.html": "{0}에 해당하는 예상 선언이 없음{1}",
  "html.0.is.not.abstract.and.does.not.implement.abstract.base.class.member.br.1.html": "{0}은(는) abstract가 아니며 추상 기본 클래스 멤버를 구현하지 않음<br/>{1}",
  "html.0.is.not.abstract.and.does.not.implement.abstract.member.br.1.html": "{0}은(는) abstract가 아니며 추상 멤버를 구현하지 않음<br/>{1}",
  "html.0.method.may.be.missing.none.of.the.following.functions.will.be.called.ul.1.ul.html": "''{0}'' 메서드가 누락되었을 수 있습니다. 다음 함수는 하나도 호출되지 않습니다. <ul>{1}</ul>",
  "html.candidate.resolution.will.be.changed.soon.please.use.fully.qualified.name.to.invoke.the.following.closer.candidate.explicitly.ul.0.ul.html": "후보 해결이 곧 변경될 예정입니다. 정규화된 이름을 사용하여 다음의 더 가까운 후보를 명시적으로 호출하세요: <ul>{0}</ul>",
  "html.expected.0.has.no.actual.declaration.in.module.1.2.html": "{1}{2} 모듈에 예상되는 {0}의 실제 선언이 없습니다.",
  "html.accidental.override.0.html": "우발적 재정의: {0}",
  "html.method.contains.from.concurrenthashmap.may.have.unexpected.semantics.it.calls.containsvalue.instead.of.containskey.br.use.explicit.form.of.the.call.to.containskey.containsvalue.contains.or.cast.the.value.to.kotlin.collections.map.instead.br.see.https.youtrack.jetbrains.com.issue.kt.18053.for.more.details.html": "ConcurrentHashMap의 'contains' 메서드는 예기치 못한 의미 체계를 가질 수 있습니다. 즉 'containsKey' 대신 'containsValue'를 호출합니다.<br/>'containsKey'/'containsValue'/'contains'에 대한 호출의 명시적 형식을 사용하거나 대신 값을 kotlin.collections.Map으로 변환하세요.<br/>자세한 내용은 https://youtrack.jetbrains.com/issue/KT-18053을 참조하세요.",
  "html.javascript.0.html": "JavaScript: {0}",
  "html.platform.declaration.clash.0.html": "플랫폼 선언 충돌: {0}",
  "html.internal.error.occurred.while.analyzing.this.expression.br.0.html": "<strong>이 표현식을 분석하는 중 내부 오류 발생:</strong><br/>{0}",
  "html.property.delegate.must.have.a.0.method.none.of.the.following.functions.are.suitable.ul.1.ul.html": "속성 대리자에는 ''{0}'' 메서드가 있어야 합니다. 다음 중 어떤 함수도 적합하지 않습니다. <ul>{1}</ul>",
  "html.overload.resolution.ambiguity.on.method.0.all.these.functions.match.ul.1.ul.html": "''{0}'' 메서드에서는 오버로드 해결이 모호합니다. 다음 함수가 모두 일치합니다. <ul>{1}</ul>",
  "html.unresolved.reference.br.none.of.the.following.candidates.is.applicable.because.of.receiver.type.mismatch.ul.0.ul.html": "예기치 않은 참조입니다. <br/> 수신자 유형 불일치로 인해 다음 후보 중 어떤 것도 적용할 수 없습니다. <ul>{0}</ul>",
  "html.cannot.choose.among.the.following.candidates.without.completing.type.inference.ul.0.ul.html": "유형 유추를 완료하지 않고 다음 후보 중에 선택할 수 없습니다. <ul>{0}</ul>",
  "html.none.of.the.following.functions.can.be.called.with.the.arguments.supplied.ul.0.ul.html": "제공된 인수를 사용하여 다음 함수 중 어떤 것도 호출할 수 없습니다. <ul>{0}</ul>",
  "html.overload.resolution.ambiguity.all.these.functions.match.ul.0.ul.html": "오버로드 해결이 모호합니다. 다음 함수가 모두 일치합니다. <ul>{0}</ul>",
  "html.function.return.type.mismatch.table.tr.td.expected.td.td.1.td.tr.tr.td.found.td.td.2.td.tr.table.html": "함수 반환 유형 불일치<table><tr><td>예상:</td><td>{1}</td></tr><tr><td>발견:</td><td>{2}</td></tr></table>",
  "html.0.must.override.1.br.because.it.inherits.many.implementations.of.it.html": "많은 구현을 상속하므로<br />{0}은(는) {1}을(를) 재정의해야 합니다.",
  "html.types.of.inherited.var.properties.do.not.match.br.0.br.1.html": "상속된 var 속성의 유형이 일치하지 않습니다:<br/>{0},<br/>{1}",
  "html.types.of.inherited.properties.are.incompatible.br.0.br.1.html": "상속된 속성의 유형이 호환되지 않습니다:<br/>{0},<br/>{1}",
  "html.actual.class.0.has.no.corresponding.members.for.expected.class.members.1.html": "실제 클래스 ''{0}''에 예상되는 클래스 멤버의 해당 멤버가 없음:{1}",
  "html.non.final.expect.class.and.its.actual.class.must.declare.exactly.the.same.non.private.members.html": "{0}: actual 및 해당 non-final expect 클래스는 일치하는 non-private 멤버를 정확히 선언해야 합니다. actual 클래스의 다음 non-private 멤버가 일치하지 않습니다:{1}<br/>이 오류는 expect 클래스 ''{2}''이(가) non-final이므로 발생합니다. 이 경고는 향후 릴리스에서 오류가 될 예정입니다.<br/>자세한 내용은 https://youtrack.jetbrains.com/issue/KT-22841을(를) 참조하세요.",
  "html.val.property.cannot.override.var.property.br.1.html": "Val 속성은 var 속성을 재정의할 수 없습니다.<br />{1}",
  "html.var.property.type.is.0.which.is.not.a.type.of.overridden.br.1.html": "Var 속성 유형이 {0}인데, 이는 재정의된 것의 유형이 아닙니다.<br/>{1}"
}

with open('missing_translations/missing_keys_korean.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

filename = "KotlinBaseFe10HighlightingBundle.properties"
found = False
for file_entry in data.get('new_files', []):
    if file_entry['filename'] == filename:
        file_entry['keys'].update(ko_dict)
        found = True
        break
if not found:
    data.setdefault('new_files', []).append({"filename": filename, "keys": ko_dict})

print(f"Updated {filename} (Keys 1-40)")

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
