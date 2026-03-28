import json

ko_dict = {
  "text.function.0": "{0,choice,1#함수|2#함수}",
  "text.anonymous.function": "익명 함수",
  "text.implicit.companion.object.will.be.inaccessible.0": "암시적 동반 객체에 접근할 수 없게 됩니다: {0}",
  "text.incorrect.target.path.directory.0.does.not.belong.to.current.project": "잘못된 대상 경로입니다. {0} 디렉터리가 현재 프로젝트에 속하지 않습니다.",
  "text.indirect.outer.instances.will.not.be.extracted.0": "간접 외부 인스턴스는 추출되지 않습니다: {0}",
  "text.inline.0": "{0} 인라인화",
  "text.inline.all.references.and.verb.0.the.kind.1.occurrences.2": "모든 참조를 인라인화하고 {1} {2}을(를) {0}합니다.",
  "text.inline.recursive.function.is.supported.only.on.references": "재귀 함수 인라인화는 참조에서만 지원됩니다.",
  "text.inline.function.not.supported": "인라인 함수는 아직 지원되지 않습니다.",
  "text.inline.this.reference.and.keep.the.0": "이 참조를 인라인화하고 {0} 유지",
  "text.inlining.0.1": "{0} {1} 인라인화 중",
  "text.inlined.0.overrides.0.1": "인라인화된 {0}이(가) {0} {1}을(를) 재정의합니다.",
  "text.inner.class.0.cannot.be.moved.to.interface": "{0}은(는) 내부 클래스입니다. 인터페이스로 이동할 수 없습니다.",
  "text.introduce.default.value": "기본값 도입(&D)",
  "text.invalid.target.path.0": "잘못된 대상 경로 {0}",
  "text.invalid.target.specified": "잘못된 대상이 지정되었습니다.",
  "text.keep": "유지",
  "text.lambda.parameter": "람다 매개변수",
  "text.lambda.parameters": "람다 매개변수(&P):\\u0020",
  "text.lambda.return.type": "람다 반환 유형(&T)",
  "text.lazy.property": "지연 속성",
  "text.local.property": "속성",
  "text.local.variable": "지역 변수",
  "text.looking.for.usages": "사용 항목 검색 중",
  "text.member.0.in.super.class.will.clash.with.existing.member.of.1": "상위 클래스의 {0}이(가) {1}의 기존 멤버와 충돌합니다.",
  "text.property.would.conflict.with.superclass.primary.constructor.parameter.0": "''{0}'' 속성이 상위 클래스의 기본 생성자 매개변수 ''{1}''과(와) 충돌합니다.",
  "text.member.extension.call.will.not.be.processed.0": "멤버 확장 호출은 처리되지 않습니다: {0}",
  "text.move.declaration.no.support.for.companion.objects": "동반 객체에 대한 선언 이동은 지원되지 않습니다.",
  "text.move.declaration.no.support.for.enums": "enum 항목에 대한 선언 이동은 지원되지 않습니다.",
  "text.move.file.no.support.for.file.target": "디렉터리가 아닌 대상으로는 파일 이동이 지원되지 않습니다.",
  "text.move.declaration.only.support.for.some.nested.declarations": "중첩된 클래스, 함수, 속성을 제외한 중첩된 선언에 대해서는 선언 이동이 지원되지 않습니다.",
  "text.move.declaration.only.support.for.single.elements": "여러 중첩 선언에 대한 선언 이동은 지원되지 않습니다.",
  "text.move.declaration.no.support.for.multi.file": "다른 파일의 선언 이동은 지원되지 않습니다.",
  "text.move.declaration.no.support.incorrect.modality": "'abstract', 'open', 'override' 멤버는 이동이 지원되지 않습니다.",
  "text.move.declaration.supports.only.top.levels.and.nested.classes": "선언 이동은 최상위 선언 및 중첩 클래스에만 지원됩니다.",
  "text.move.declaration.proceed.move.without.mpp.counterparts.text": "이 리팩터링은 컴파일 오류로 이어질 수 있는 expect/actual 상대 요소 없이 선택한 선언을 이동합니다.\\n계속하시겠습니까?",
  "text.move.declaration.proceed.move.without.mpp.counterparts.title": "리팩터링할 수 없습니다. 이 리팩터링에서는 MPP 선언이 지원되지 않습니다.",
  "text.move.declarations": "선언 이동",
  "command.move.declarations": "선언 이동",
  "preparing.move.descriptor": "이동 설명자 준비 중",
  "retargeting.usages.progress": "사용 항목 대상 변경 중",
  "shortening.usages.progress": "사용 항목 축소 중",
  "text.no.destination.object.specified": "대상 객체가 지정되지 않았습니다.",
  "title.select.a.name.for.this.parameter": "''this@{0}'' 매개변수의 이름 선택",
  "text.move.method.is.not.supported.for.non.project.methods": "프로젝트 외 메서드에는 메서드 이동이 지원되지 않습니다.",
  "text.move.method.is.not.supported.for.generic.classes": "제네릭 클래스에는 메서드 이동이 지원되지 않습니다.",
  "text.move.method.is.not.supported.when.method.is.a.part.of.inheritance.hierarchy": "메서드가 상속 계층의 일부인 경우에는 메서드 이동이 지원되지 않습니다.",
  "text.references.to.outer.classes.have.to.be.added.manually": "이동 후에 외부 클래스에 대한 참조를 수동으로 추가해야 합니다.",
  "action.move.method": "메서드 이동\\u2026",
  "text.move.file.0": "{0} 이동"
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

print(f"Updated {filename} (Keys 691-740)")

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
