import json
with open('missing_translations/missing_keys_korean.json', 'r', encoding='utf-8') as f:
    ko_data = json.load(f)

translations = {
  "extract.method.error.many.finals": "final 필드에 대한 할당이 있습니다.",
  "extract.method.error.variable.in.expression": "선택한 표현식 내부에 반환할 변수가 있습니다.",
  "extract.method.error.class.not.found": "선택한 블록은 Java 클래스의 일부여야 합니다.",
  "template.error.invalid.identifier.name": "잘못된 식별자 이름",
  "template.error.variable.already.defined": "해당 이름의 변수가 이미 정의되어 있습니다",
  "template.error.class.already.defined": "이름이 ''{0}''인 클래스가 해당 범위(scope)에 이미 정의되어 있습니다",
  "extract.method.error.method.conflict": "동일한 시그니처를 가진 메서드가 이미 존재합니다",
  "extract.method.object.anonymous.make.varargs.option": "가변 인수(varargs)로 만들기(&V)",
  "extract.method.object.class.name": "클래스 이름(&C):",
  "extract.method.object.create.anonymous.class": "익명 클래스 생성(&A)",
  "extract.method.object.create.inner.class": "내부 클래스 생성(&I)",
  "extract.method.object.inner.class.visibility": "가시성:",
  "extract.method.object.inner.make.static.option": "정적(static)으로 만들기(&S)",
  "extract.method.object.inner.make.varargs.option": "가변 인수(varargs)로 만들기(&V)",
  "extract.method.object.inner.visibility.package.local": "패키지 전용(package local)(&K)",
  "extract.method.object.inner.visibility.private": "pri&vate",
  "extract.method.object.inner.visibility.protected": "pr&otected",
  "extract.method.object.inner.visibility.public": "pu&blic",
  "extract.method.object.method.name": "메서드 이름(&M):",
  "extract.method.object.parameters": "매개변수",
  "extract.method.object.signature.preview": "시그니처 미리보기",
  "extract.method.object.suggestion": "메서드 객체를 추출하시겠습니까?",
  "extract.parameters.to.replace.duplicates": "중복을 바꾸기 위해 매개변수 추출",
  "extract.subclass.command": "하위 클래스(Subclass) 추출",
  "extractSuper.rename.original.class.to": "다음으로 원본 클래스 이름 변경(&R):",
  "extractSuperInterface.javadoc": "JavaDoc",
  "factory.method.name.label": "팩터리 메서드 이름:",
  "failed.to.re.run.refactoring": "리팩터링을 다시 실행하지 못했습니다",
  "field.0.is.already.defined.in.the.1": "{0} 필드가 {1}에 이미 정의되어 있습니다",
  "field.0.is.never.used": "{0} 필드가 사용되지 않습니다",
  "field.0.is.not.accessible": "{1}에서 {0} 필드에 액세스할 수 없습니다",
  "field.0.will.hide.field.1.of.the.base.class": "{0} 필드가 기본 {2}의\\n{1} 필드를 숨깁니다",
  "field.declaration.radio": "필드 선언(&D)",
  "field.description": "{0} 필드",
  "field.name": "필드 이름(&F):",
  "fields.to.be.refactored.should.belong.to.the.same.class": "리팩터링할 필드는 동일한 클래스에 속해야 합니다",
  "functional.interface.broken": "함수형 표현식은 함수형 인터페이스에 정확히 하나의 메서드가 있어야 합니다",
  "generate.getter.for.delegated.component": "위임된 컴포넌트에 대한 getter 생성(&G)",
  "generate.module.descriptors.analysing.message": "종속성 분석 중",
  "generate.module.descriptors.build.required.message": "프로젝트가 아직 빌드되지 않아 모듈 디스크립터를 생성할 수 없습니다"
}

ko_error_bundle = next((x for x in ko_data['new_files'] if x['filename'] == 'JavaRefactoringBundle.properties'), None)
ko_error_bundle['keys'].update(translations)
ko_error_bundle['key_count'] = len(ko_error_bundle['keys'])

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(ko_data, f, ensure_ascii=False, indent=2)

print("Updated JavaRefactoringBundle part 7")