import json
with open('missing_translations/missing_keys_korean.json', 'r', encoding='utf-8') as f:
    ko_data = json.load(f)

translations = {
  "introduce.parameter.elements.header": "메서드에 매개변수 추가",
  "introduce.parameter.object.create.inner.class": "내부 클래스 생성(&I)",
  "introduce.parameter.object.create.new.class": "새 클래스 생성(&C)",
  "introduce.parameter.object.escalate.visibility.option": "가시성 에스컬레이션(&E)",
  "introduce.parameter.object.existing.class.name": "이름(&N)",
  "introduce.parameter.object.generate.accessors.option": "접근자(accessors) 생성(&G)",
  "introduce.parameter.object.inner.class.name": "이름(&N)",
  "introduce.parameter.object.new.class.name": "이름(&N)",
  "introduce.parameter.object.new.class.package.name": "패키지 이름(&P)",
  "introduce.parameter.object.use.existing.class": "기존 클래스 사용(&U)",
  "introduce.parameter.super.method.checkbox": "Super 메서드 리팩터링(&U)",
  "introduced.variable.will.conflict.with.0": "도입된 변수가 {0}와(과) 충돌합니다",
  "introducing.variable.may.break.code.logic": "변수를 도입하면 코드 로직이 중단될 수 있습니다",
  "invalid.expression.context": "잘못된 표현식 컨텍스트입니다.",
  "invalid.package.name": "잘못된 패키지 이름: {0}",
  "invalid.target.package.name.specified": "잘못된 대상 패키지 이름이 지정되었습니다",
  "invert.boolean.foreach": "Foreach 매개변수 초기화자는 반전(invert)할 수 없습니다",
  "invert.boolean.wrong.type": "리팩터링할 메서드의 반환 타입이나 변수의 타입은 boolean이어야 합니다",
  "invocations.to.be.inlined": "인라인 처리할 호출 {0}",
  "is.modified.in.loop.body": "{0}은(는) 반복문 본문에서 수정됩니다",
  "javadoc.for.abstracts": "추상 맴버를 위한 JavaDoc",
  "keep.original.signature": "원본 시그니처 유지",
  "local.variable.description": "로컬 변수 {0}",
  "pattern.variable.description": "패턴 변수 {0}",
  "local.will.be.hidden.renamed.description": "이름이 바뀐 필드가 {0}을(를) 숨깁니다",
  "locate.caret.inside.a.method": "캐럿을 멤버 안에 위치시키세요",
  "locate.duplicates.action.name": "중복 찾기",
  "make.0.static": "{0} 정적(static)으로 만들기",
  "make.method.static.title": "메서드를 정적(static)으로 만들기",
  "make.static.command": "{0}을(를) 정적(static)으로 만드는 중",
  "make.static.description.label": "{0} {1}을(를) 정적(static)으로 만들기",
  "make.static.elements.header": "정적(static)으로 만들 {0}",
  "make.static.method.references.progress": "메서드 참조 검색 중",
  "make.static.methods.to.propagate.dialog.title": "정적(static) 파급할 메서드 선택",
  "members.to.form.interface.title": "인터페이스를 구성할 멤버",
  "members.to.form.superclass.title": "슈퍼 클래스를 구성할 멤버",
  "method.0.is.overridden.by.1": "{0} 메서드는 {1}에 의해 재정의(override)됩니다",
  "method.with.the.same.erasure": "지우개(erasure)가 동일한 메서드",
  "method.0.will.hide.method.of.the.base.class": "메서드가 슈퍼 {1}의 {0}을(를) 숨깁니다",
  "method.0.will.implement.method.of.the.base.class": "메서드가 슈퍼 {1}의 {0}을(를) 구현합니다"
}

ko_error_bundle = next((x for x in ko_data['new_files'] if x['filename'] == 'JavaRefactoringBundle.properties'), None)
ko_error_bundle['keys'].update(translations)
ko_error_bundle['key_count'] = len(ko_error_bundle['keys'])

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(ko_data, f, ensure_ascii=False, indent=2)

print("Updated JavaRefactoringBundle part 11")