import json
with open('missing_translations/missing_keys_korean.json', 'r', encoding='utf-8') as f:
    ko_data = json.load(f)

translations = {
  "inline.super.type.params.differ": "{0}에서 타입 매개변수가 일치하지 않습니다. {1}이(가) 예상되었지만 {2}을(를) 찾았습니다.",
  "inline.super.unknown.type": "알 수 없는 타입입니다",
  "inline.to.anonymous.border.title": "인라인",
  "inline.to.anonymous.command.name": "{0} 클래스 인라인",
  "inline.to.anonymous.name.label": "클래스 {0}",
  "inline.to.anonymous.no.abstract": "추상 클래스는 인라인할 수 없습니다",
  "inline.to.anonymous.no.ctor.calls": "클래스가 자체 생성자를 호출하므로 인라인할 수 없습니다",
  "inline.to.anonymous.no.get.class.calls": "getClass() 호출 결과가 변경됩니다",
  "inline.to.anonymous.no.method.calls": "클래스가 다른 인스턴스에서 자체 멤버에 접근하므로 인라인할 수 없습니다",
  "inline.to.anonymous.no.multiple.interfaces": "여러 인터페이스를 구현하는 클래스는 인라인할 수 없습니다",
  "inline.to.anonymous.no.superclass.and.interface": "슈퍼 클래스가 있고 인터페이스를 구현하는 클래스는 인라인할 수 없습니다",
  "inline.to.anonymous.refactoring": "익명 클래스로 인라인",
  "inline.vars.elements.header": "인라인 할 변수",
  "inlined.method.implements.method.from.0": "인라인 메서드가 {0}의 메서드를 구현합니다",
  "inlined.method.overrides.method.from.0": "인라인 메서드가 {0}의 메서드를 재정의(override)합니다",
  "inlined.method.will.be.transformed.to.single.return.form": "인라인 메서드가 단일 반환(single-return) 형식으로 변환됩니다",
  "inner.class.0.is.already.defined.in.class.1": "내부 클래스 {0}이(가) {1} 클래스에 이미 정의되어 있습니다.\\n그래도 계속하시겠습니까?",
  "inner.class.0.is.not.static": "내부 클래스 {0}은(는) static이 아닙니다.\\n{1} 리팩터링은 정적(static) 멤버에만 지원됩니다.",
  "inner.class.exists": "''{0}''이라는 이름의 내부 클래스가\\n''{1}'' 클래스에 이미 정의되어 있습니다",
  "inner.class.name": "내부 클래스 이름(&I):",
  "instance.initializer.description": "{0}의 인스턴스 초기화자",
  "instances.casted.to.java.lang.object": "java.lang.Object로 캐스팅된 인스턴스",
  "instances.of.0.upcasted.to.1.were.found": "{1}(으)로 업캐스팅된 {0}의 인스턴스를 찾았습니다. 계속하면 별도의 찾기 탭에 표시됩니다.",
  "instances.upcasted.to.java.lang.object.found": "java.lang.Object로 업캐스팅된 인스턴스를 찾았습니다",
  "instances.upcasted.to.object": "Object로 업캐스팅된 인스턴스",
  "interface.0.does.not.have.inheritors": "{0} 인터페이스에 상속자가 없습니다",
  "interface.description": "{1, choice, 0#|1#로컬 }인터페이스 {0}",
  "interface.does.not.have.base.interfaces": "{0} 인터페이스에 기본 인터페이스가 없습니다",
  "interface.has.been.successfully.created": "{0} 인터페이스가 성공적으로 생성되었습니다",
  "introduce.constant.enum.cb": "Enum 상수로 추출(&E)",
  "introduce.constant.field.of.type": "타입의 상수(static final 필드)(&T):",
  "introduce.constant.introduce.to.class": "클래스로 추출 (정규화된 이름)(&C):",
  "introduce.constant.move.to.another.class.checkbox": "다른 클래스로 이동(&M)",
  "introduce.field.field.of.type": "타입의 필드(&T):",
  "introduce.field.static.field.of.type": "타입의 정적 필드(&T):",
  "introduce.functional.variable.pass.fields.checkbox": "필드를 매개변수로 전달(&F)",
  "introduce.local.variable.to.reassign.title": "재할당할 변수 선택",
  "introduce.parameter.command": "매개변수를 {0}(으)로 추출하는 중",
  "introduce.parameter.convert.lambda": "함수형 표현식으로 변환(&C)",
  "introduce.parameter.duplicates.progress": "메서드 중복 검색 중..."
}

ko_error_bundle = next((x for x in ko_data['new_files'] if x['filename'] == 'JavaRefactoringBundle.properties'), None)
ko_error_bundle['keys'].update(translations)
ko_error_bundle['key_count'] = len(ko_error_bundle['keys'])

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(ko_data, f, ensure_ascii=False, indent=2)

print("Updated JavaRefactoringBundle part 10")