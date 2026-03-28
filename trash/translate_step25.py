import json
with open('missing_translations/missing_keys_korean.json', 'r', encoding='utf-8') as f:
    ko_data = json.load(f)

translations = {
  "generate.module.descriptors.collecting.message": "종속성 수집 중",
  "generate.module.descriptors.command.title": "module-info 디스크립터 생성하기",
  "generate.module.descriptors.no.suitable.modules.message": "module-info를 포함할 수 있는 모듈을 찾지 못했습니다",
  "generate.module.descriptors.io.exceptions.message": "모듈 {0} 파일을 읽는 중 문제가 발생했습니다",
  "generate.module.descriptors.preparing.message": "코드 준비 중",
  "generate.module.descriptors.rebuild.message": "종속성 계산의 정확도를 높이려면 프로젝트를 빌드해야 합니다. \\n\\n  module-info 디스크립터를 생성하기 전에 빌드를 시작하시겠습니까?",
  "generate.module.descriptors.scanning.message": "컴파일러 출력 검사 중",
  "generate.module.descriptors.title": "모듈 디스크립터 생성",
  "getter.and.setter.methods.found.for.the.field.0": "{0} 필드에 대한 getter 및 setter 메서드를 찾았습니다. \\n이것들도 {1}하시겠습니까?",
  "getter.method.found.for.the.field.0": "{0} 필드에 대한 getter 메서드를 찾았습니다. \\n이 getter도 {1}하시겠습니까?",
  "idea.has.not.found.any.code.that.can.be.replaced.with.method.call": "{0}에서 중복을 찾지 못했습니다",
  "ignore.button": "무시",
  "implicit.last.parameter.warning": "암시적 마지막 매개변수는 삭제할 수 없습니다",
  "infer.class.type.args.warning": "클래스 타입 매개변수를 유추할 수 없습니다. 계속 진행하면 원시(raw) {0}이(가) 생성됩니다.",
  "information.title": "정보",
  "initializer.for.variable.cannot.be.a.constant.initializer": "{0} 변수의 초기화자(initializer)는 상수 초기화자가 될 수 없습니다",
  "inline.action.name": "인라인",
  "inline.anonymous.conflict.progress": "\"{0}\" 클래스 상속자 검색 중...",
  "inline.class.elements.header": "인라인 할 클래스",
  "inline.conflicts.progress": "인라인이 가능한지 확인 중...",
  "inline.constant.field.not.supported.for.enum.constants": "{0}은(는) Enum 상수에 대해 지원되지 않습니다",
  "inline.element.unknown.header": "알 수 없는 요소",
  "inline.field.action.name": "필드 인라인...",
  "inline.field.command": "{0} 필드 인라인",
  "inline.field.elements.header": "인라인 할 필드",
  "inline.field.field.name.label": "''{0}'' 필드 인라인:",
  "inline.field.field.occurrences": "''{0}'' 필드 인라인 ({1}개의 {1, choice, 1#사용|2#사용}):",
  "inline.field.title": "필드 인라인",
  "inline.field.used.in.javadoc": "인라인 처리된 필드가 Javadoc에 사용되었습니다",
  "inline.field.used.in.reflection": "인라인 처리된 필드가 리플렉션으로 사용되었습니다",
  "inline.field.initializer.is.not.accessible": "필드 초기화자가 {0}을(를) 참조하지만, {1}에서는 접근할 수 없습니다",
  "inline.local.unable.try.catch.warning.message": "try/catch 문 외부에서는 인라인할 수 없습니다",
  "inline.local.used.as.resource.cannot.refactor.message": "변수가 리소스 참조(resource reference)로 사용되고 있습니다",
  "inline.local.variable.declared.outside.cannot.refactor.message": "변수가 코드 블록 외부에 선언되어 있습니다",
  "inline.method.calls.not.accessible.in": "인라인 메서드가 {1}에서 액세스할 수 없는 {0}을(를) 호출합니다",
  "inline.method.calls.not.accessible.on.qualifier": "인라인 메서드가 한정자(qualifier) {1}에서 접근할 수 없는 {0}을(를) 호출합니다",
  "inline.method.checking.tail.calls.progress": "꼬리 호출(tail call) 사용 검사 중",
  "inline.method.elements.header": "인라인 할 메서드",
  "inline.method.method.label": "''{0}'' 메서드 인라인:",
  "inline.method.method.occurrences": "''{0}'' 메서드 인라인 ({1}개의 {1, choice, 1#사용|2#사용}):"
}

ko_error_bundle = next((x for x in ko_data['new_files'] if x['filename'] == 'JavaRefactoringBundle.properties'), None)
ko_error_bundle['keys'].update(translations)
ko_error_bundle['key_count'] = len(ko_error_bundle['keys'])

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(ko_data, f, ensure_ascii=False, indent=2)

print("Updated JavaRefactoringBundle part 8")