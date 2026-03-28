import json

ko_dict = {
  "add.documentation.fix.text": "문서 추가",
  "missing.documentation": "누락된 문서",
  "0.is.missing.documentation": "{0}에 문서가 누락되었습니다.",
  "it.s.prohibited.to.call.0.with.min.value.step.since.1.3": "1.3부터는 MIN_VALUE step으로 {0}을(를) 호출하는 것이 금지되어 있습니다.",
  "obsolete.coroutine.usage.in.whole.fix.family.name": "프로젝트에서 실험적인 코루틴 사용 항목 수정",
  "obsolete.kotlin.js.packages.usage.in.whole.fix.family.name": "프로젝트에서 'kotlin.dom' 및 'kotlin.browser' 패키지 사용 항목 수정",
  "apply.in.the.project.0": "프로젝트에 적용: {0}",
  "obsolete.coroutine.usage.fix.family.name": "실험적인 코루틴 사용 항목 수정",
  "obsolete.package.usage.fix.family.name": "''{0}'' 패키지 사용 항목 수정",
  "0.is.expected.to.be.used.since.kotlin.1.3": "Kotlin 1.3부터는 ''{0}''이(가) 사용될 것으로 예상됩니다.",
  "methods.are.absent.in.coroutines.class.since.1.3": "1.3부터 coroutines 클래스에 메서드가 없습니다.",
  "experimental.coroutines.usages.are.obsolete.since.1.3": "실험적인 코루틴 사용은 1.3부터 사용되지 않습니다.",
  "package.usages.are.obsolete.since.1.4": "''{0}'' 패키지 사용은 1.4부터 사용되지 않습니다.",
  "replace.substring.call.with.droplast.call": "'substring' 호출을 'dropLast' 호출로 바꾸기",
  "replace.substring.call.with.indexing.operation.call": "'substring' 호출을 인덱싱 작업 호출로 바꾸기",
  "replace.substring.call.with.substringbefore.call": "'substring' 호출을 'substringBefore' 호출로 바꾸기",
  "replace.substring.call.with.substringafter.call": "'substring' 호출을 'substringAfter' 호출로 바꾸기",
  "replace.substring.call.with.take.call": "'substring' 호출을 'take' 호출로 바꾸기",
  "add.operator.modifier": "'operator' 한정자 추가",
  "function.should.have.operator.modifier": "함수에는 'operator' 한정자가 있어야 합니다.",
  "type.parameter.can.have.0.variance": "유형 매개변수는 ''{0}'' 변성을 가질 수 있습니다.",
  "add.variance.fix.text": "''{0}'' 변성 추가",
  "add.variance.fix.family.name": "변성 추가",
  "interface.member.dependency.required.by.interfaces": "{0,choice,1#인터페이스|2#인터페이스}에 필요함",
  "generate.equals.and.hashcode.fix.text": "equals() 및 hashCode() 생성",
  "array.property.in.data.class.it.s.recommended.to.override.equals.hashcode": "'data' 클래스의 'Array' 유형 속성: 'equals()' 및 'hashCode()'를 재정의하는 것이 좋습니다.",
  "report.also.on.call.with.single.boolean.literal.argument": "단일 부울 리터럴 인수가 있는 호출에 대해서도 보고",
  "boolean.literal.argument.without.parameter.name": "매개변수 이름이 없는 부울 리터럴 인수",
  "constructor.parameter.is.never.used.as.a.property": "생성자 매개변수가 속성으로 사용되지 않습니다.",
  "property.is.explicitly.assigned.to.parameter.0.can": "속성이 매개변수 {0}에 명시적으로 할당되므로 생성자에서 직접 선언할 수 있습니다.",
  "variable.is.never.modified.and.can.be.declared.immutable.using.val": "변수가 수정되지 않으므로 'val'을 사용하여 선언할 수 있습니다.",
  "sealed.sub.class.has.no.state.and.no.overridden.equals": "'sealed' 하위 클래스에 상태가 없고 재정의된 'equals()'가 없습니다.",
  "cascade.if.should.be.replaced.with.when": "계단식 'if'는 'when'으로 바꿔야 합니다.",
  "mark.as.deprecated.level.deprecationlevel.hidden": "'@Deprecated(..., level = DeprecationLevel.HIDDEN)'으로 표시",
  "searching.for.imports.to.delete.title": "삭제할 가져오기 검색 중",
  "delete.redundant.extension.property": "중복 확장 속성 삭제",
  "this.property.conflicts.with.synthetic.extension.and.should.be.removed.or.renamed.to.avoid.breaking.code.by.future.changes.in.the.compiler": "속성이 합성 확장과 충돌하며, 향후 Kotlin 컴파일러의 변경으로 인해 코드가 손상되지 않도록 제거하거나 이름을 바꿔야 합니다.",
  "condition.is.always.0": "조건은 항상 ''{0}''입니다.",
  "remove.fix.text": "표현식 삭제",
  "simplify.fix.text": "표현식 간소화",
  "0.has.empty.body": "''{0}''에 본문이 비어 있습니다.",
  "convert.na.n.equality.quick.fix.text": "'isNaN()'으로 대체",
  "equality.check.with.nan.should.be.replaced.with.isnan": "NaN과의 동등성 검사는 'isNaN()'으로 대체해야 합니다.",
  "convert.pair.constructor.to.to.fix.text": "중위 'to'로 바꾸기",
  "can.be.converted.to.to": "명시적인 'Pair' 시작을 중위 'to()' 호출로 바꿀 수 있습니다.",
  "convert.to.a.range.check": "범위 검사로 변환",
  "convert.comparisons.to.range.check": "비교를 ''{0}''(으)로 변환",
  "two.comparisons.should.be.converted.to.a.range.check": "두 가지 비교를 범위 검사로 변환해야 합니다.",
  "copy.method.of.data.class.is.called.without.named.arguments": "'copy()' 메서드 호출에 대한 매개변수 이름을 명시적으로 지정해야 합니다.",
  "private.data.class.constructor.is.exposed.via.the.generated.copy.method": "비공개 기본 생성자가 'data' 클래스의 생성된 'copy()' 메서드를 통해 노출됩니다."
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

print(f"Updated {filename} (Keys 1091-1140)")

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
