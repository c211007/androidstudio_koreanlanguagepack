import json

ko_dict = {
  "text.expected.moved.to.platform.modules.target": "예상되는(expected) 선언 ''{0}''이(가) 플랫폼 모듈로 이동됩니다.",
  "text.actual.moved.to.common.modules.target": "실제(actual) 선언 ''{0}''이(가) 공통 모듈로 이동됩니다.",
  "text.select.target.code.block.file": "대상 코드 블록 / 파일 선택",
  "text.select.target.code.block": "대상 코드 블록 선택",
  "text.select.target.file": "대상 파일 선택",
  "text.there.is.already.a.parameter": "{1}에 ''{0}'' 매개변수가 이미 있습니다. 새 매개변수와 충돌합니다.",
  "text.there.is.already.a.variable.0.in.1.it.will.conflict.with.the.new.parameter": "{1}에 ''{0}'' 변수가 이미 있습니다. 새 매개변수와 충돌합니다.",
  "text.type.alias.cannot.refer.to.types.which.aren.t.accessible.in.the.scope.where.it.s.defined": "유형 별칭은 정의된 범위에서 접근할 수 없는 유형을 참조할 수 없습니다.",
  "text.type.alias.name.must.be.a.valid.identifier.0": "유형 별칭 이름은 유효한 식별자여야 합니다: {0}",
  "text.type.alias": "유형 별칭",
  "text.type.alias.0": "유형 {0,choice,1#별칭|2#별칭}",
  "text.type.already.exists.in.the.target.scope": "대상 범위에 {0} 유형이 이미 존재합니다.",
  "text.type.parameter.names.must.be.distinct": "유형 매개변수 이름은 고유해야 합니다.",
  "text.type.parameters": "유형 매개변수(&P)",
  "text.type": "유형",
  "text.unexpected.element.type.0": "예상치 못한 요소 유형: {0}",
  "text.update.usages.to.reflect.declaration.0.move": "{0, choice, 0#선언|1#선언} 이동을 반영하도록 사용 항목 업데이트",
  "text.updating.usages.progress": "사용 항목 업데이트 중\\u2026",
  "text.cannot.inline.reference.from.0.to.1": "{0}에서 {1}(으)로 참조를 인라인할 수 없습니다.",
  "title.inline.function": "인라인 함수",
  "title.inline.property": "인라인 속성",
  "title.inline.type.alias": "인라인 유형 별칭",
  "refactoring.cannot.be.applied.no.sources.attached": "소스가 첨부되지 않아 {0} 리팩터링을 적용할 수 없습니다.",
  "refactoring.cannot.be.applied.to.abstract.declaration": "추상 선언에는 {0} 리팩터링을 적용할 수 없습니다.",
  "refactoring.cannot.be.applied.to.expect.declaration": "expect 선언에는 {0} 리팩터링을 적용할 수 없습니다.",
  "refactoring.cannot.be.applied.to.anonymous.function.without.invocation": "호출이 없는 익명 함수에는 {0} 리팩터링을 적용할 수 없습니다.",
  "refactoring.the.function.not.found": "함수를 찾을 수 없습니다.",
  "refactoring.the.function.cannot.be.converted.to.anonymous.function": "함수를 익명 함수로 변환할 수 없습니다.",
  "refactoring.the.invocation.cannot.be.resolved": "호출을 확인할 수 없습니다.",
  "refactoring.cannot.be.applied.to.lambda.expression.without.invocation": "호출이 없는 람다 표현식에는 {0} 리팩터링을 적용할 수 없습니다.",
  "text.reference.cannot.be.converted.to.a.lambda": "참조를 람다로 변환할 수 없습니다.",
  "title.introduce.parameter.to.declaration": "선언에 매개변수 도입",
  "title.move.nested.classes.to.upper.level": "상위 수준으로 중첩 클래스 이동",
  "title.move.method": "메서드 이동",
  "title.choose.destination.object": "대상 객체 선택",
  "title.select.target.code.block": "대상 코드 블록 선택",
  "unsupported.usage.0": "지원되지 않는 사용 항목: {0}",
  "parameter.used.in.declaration.body.warning": "''{0}''이(가) 선언 본문에서 사용됩니다.",
  "do.you.want.to.delete.this.parameter.in.expected.declaration.and.all.related.actual.ones": "예상되는(expected) 선언 및 모든 관련 실제(actual) 선언에서 이 매개변수를 삭제하시겠습니까?",
  "do.you.want.to.delete.expected.declaration.together.with.all.related.actual.ones": "예상되는(expected) 선언과 모든 관련 실제(actual) 선언을 함께 삭제하시겠습니까?",
  "delete.with.usage.search": "삭제(사용 항목 검색 포함)",
  "destination.not.found.for.package.0": "''{0}'' 패키지의 대상을 찾을 수 없습니다.",
  "premature.end.of.template": "템플릿이 너무 일찍 끝남",
  "choose.target.class.or.interface": "대상 클래스 또는 인터페이스 선택",
  "text.abstract": "추상",
  "text.secondary.constructor": "보조 생성자",
  "text.create": "만들기",
  "text.member": "멤버",
  "text.extension": "확장",
  "text.extension.function": "확장 함수"
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

print(f"Updated {filename} (Keys 791-840)")

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
