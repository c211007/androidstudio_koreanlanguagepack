import json
with open('missing_translations/missing_keys_korean.json', 'r', encoding='utf-8') as f:
    ko_data = json.load(f)

translations = {
  "encapsulate.fields.set.access.checkbox": "설정 접근(&S)",
  "encapsulate.fields.setter.column.name": "Setter",
  "encapsulate.fields.setter.exists": "반환 타입만 setter {1}와(과) 다른 {0} 메서드가 이미 존재합니다",
  "encapsulate.fields.title": "필드 캡슐화",
  "encapsulate.fields.use.accessors.even.when.field.is.accessible.checkbox": "필드에 접근할 수 있는 경우에도 접근자 사용(&U)",
  "entity.name.constructor.parameter": "매개변수",
  "entity.name.inheritor": "상속자",
  "entity.name.test": "테스트",
  "entity.name.variable": "변수",
  "entity.name.accessor": "접근자(Accessor)",
  "enum.constant.description": "열거형 상수 {0}",
  "enum.description": "{1, choice, 0#|1#지역(local) }열거형(enum) {0}",
  "error.cannot.resolve": "{0}을(를) 확인할 수 없습니다",
  "error.incorrect.data": "잘못된 데이터",
  "error.not.supported.for.jsp": "JSP에서는 {0} 리팩토링이 지원되지 않습니다",
  "error.not.supported.for.local": "지역 클래스를 상속하는 클래스는 내부 클래스로 변환할 수 없습니다",
  "error.not.supported.for.package.info": "package-info.java에서는 {0} 리팩토링이 지원되지 않습니다",
  "error.wrong.caret.position.anonymous": "캐럿은 리팩터링할 익명 또는 지역 클래스 내부에 있어야 합니다",
  "error.wrong.caret.position.constructor": "캐럿은 리팩터링할 생성자 내부에 있어야 합니다",
  "error.wrong.caret.position.local.or.expression.name": "캐럿은 리팩터링할 지역 변수나 표현식의 이름에 있어야 합니다",
  "error.wrong.caret.position.method": "캐럿은 리팩터링할 메서드 내부에 있어야 합니다",
  "error.wrong.name.input": "잘못된 이름: {0}",
  "expand.method.reference.warning": "메서드가 하나 이상의 메서드 참조에서 사용되고 있습니다. 계속하면 이러한 메서드 참조가 람다 표현식으로 변환됩니다.",
  "method.reference.will.be.converted.to.lambda.expression.warning": "메서드 참조가 람다 표현식으로 변환됩니다",
  "expression.result": "표현식 결과",
  "extract.chained.constructor.checkbox": "체인 생성자 추출(&C)",
  "extract.delegate.as.enum.checkbox": "열거형(enum)으로 추출",
  "extract.delegate.create.nested.checkbox": "중첩 클래스 생성",
  "extract.delegate.generate.accessors.checkbox": "접근자 생성(&G)",
  "extract.delegate.unable.create.warning.message": "주어진 이름으로 클래스를 생성할 수 없습니다",
  "extract.method.control.flow.analysis.failed": "코드에 구문 오류가 있습니다. 필요한 분석을 수행할 수 없습니다.",
  "extract.method.error.prefix": "메서드를 추출할 수 없습니다.",
  "extract.method.error.class.outside.used": "지역 클래스가 선택한 블록 밖에서 사용됩니다.",
  "extract.method.error.class.outside.defined": "지역 클래스가 선택한 블록 밖에서 정의되어 있습니다.",
  "extract.method.error.many.outputs": "반환할 변수가 여러 개입니다.",
  "extract.method.error.wrap.many.outputs": "선택한 코드 블록에 여러 개의 출력 변수가 있습니다.\\n이 변수들을 {0}(으)로 묶으면 메서드를 추출할 수 있습니다.",
  "extract.method.error.wrap.many.outputs.class": "단일 객체",
  "extract.method.error.wrap.many.outputs.record": "새 레코드",
  "extract.method.error.many.exits": "종료 지점이 여러 개 있습니다.",
  "extract.method.error.exception": "예외가 발생할 때 다르게 동작할 수 있습니다."
}

ko_error_bundle = next((x for x in ko_data['new_files'] if x['filename'] == 'JavaRefactoringBundle.properties'), None)
ko_error_bundle['keys'].update(translations)
ko_error_bundle['key_count'] = len(ko_error_bundle['keys'])

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(ko_data, f, ensure_ascii=False, indent=2)

print("Updated JavaRefactoringBundle part 6")