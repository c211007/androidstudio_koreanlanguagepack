import json
with open('missing_translations/missing_keys_korean.json', 'r', encoding='utf-8') as f:
    ko_data = json.load(f)

translations = {
  "all.references.and.remove.the.field": "모든 사용 위치 인라인화 및 필드 제거(&A)",
  "all.invocations.and.remove.the.method": "모든 사용 위치 인라인화 및 메서드 제거(&A)",
  "all.invocations.in.project": "프로젝트 내 모든 사용 위치 인라인화(&A)",
  "this.invocation.only.and.keep.the.method": "이 사용 위치만 인라인화 및 메서드 유지(&K)",
  "all.references.keep.field": "모든 사용 위치 인라인화 및 필드 유지(&E)",
  "all.these.directories.will.be.moved.and.all.references.to.0.will.be.changed": "이 모든 디렉터리가 이동되며 {0}에 대한 모든 참조가\\n변경됩니다.",
  "analyze.and.replace.usages": "사용 위치 분석 및 바꾸기",
  "analyze.module.conflicts": "모듈 충돌 분석\\u2026",
  "annotate.field.as.nonnls.checkbox": "필드에 @NonNls 애너테이션 추가(&F)",
  "anonymous.class.description": "{0}에서 파생된 익명 클래스",
  "anonymous.class.text": "익명 클래스",
  "anonymous.to.inner.enum.constant.cannot.refactor.message": "열거형 상수(Enum constant)는 내부 클래스로 변환할 수 없습니다",
  "anonymousToInner.class.name.label.text": "클래스 이름:",
  "anonymousToInner.make.class.static.checkbox.text": "정적(static) 클래스로 만들기(&S)",
  "anonymousToInner.no.inner.class.name": "클래스 이름을 지정해야 합니다",
  "anonymousToInner.parameters.panel.border.title": "생성자 매개변수",
  "anonymousToInner.refactoring.name": "익명을 내부로 변환(Convert Anonymous to Inner)",
  "localToInner.refactoring.name": "지역 클래스를 내부로 변환(Convert Local Class to Inner)",
  "auto.rename.module.dialog.description": "다음 이름의 Java 모듈 이름 변경:",
  "auto.rename.module.dialog.title": "Java 모듈 이름 변경",
  "auto.rename.module.entity": "Java 모듈",
  "boolean.method.result": "부울(boolean) 메서드 결과",
  "can.t.restore.context.for.method.extraction": "메서드 추출을 위한 컨텍스트를 복원할 수 없습니다",
  "cannot.find.or.create.destination.directory": "대상 디렉터리를 찾거나 생성할 수 없습니다",
  "cannot.introduce.field.in.interface": "상수가 아닌 필드는 인터페이스에 허용되지 않습니다.",
  "variable.type.unknown": "변수 타입이 알 수 없는 타입입니다",
  "0.is.not.visible.to.members.of.1": "{0}은(는) {1}의 멤버에게 표시되지 않습니다",
  "cannot.move": "이동할 수 없음",
  "cannot.move.inner.class.0.into.itself": "내부 클래스 {0}을(를) 자기 자신 안으로 이동할 수 없습니다",
  "cannot.move.package.into.itself": "패키지를 자기 자신 안으로 이동할 수 없습니다",
  "caret.position.warning.message": "캐럿은 리팩터링할 필드, 변수, 메서드 또는 메서드 매개변수 타입에 있어야 합니다",
  "change.method.signature.action.name": "메서드 시그니처 변경",
  "change.signature.default.value.missing.warning.message": "기본값이 누락되었습니다. 메서드 호출에 새 매개변수 값 대신 공백이 포함됩니다.",
  "change.signature.use.any.checkbox": "아무 변수나 사용(&U)",
  "changeClassSignature.bad.value": "잘못된 {0} 값: 매개변수 ''{2}''에 대한 ''{1}''",
  "changeClassSignature.class.label.text": "<code>{0}</code>의 시그니처 변경.",
  "changeClassSignature.no.type.parameters": "클래스에는 타입 매개변수가 있을 수 없습니다",
  "changeClassSignature.parameters.panel.border.title": "매개변수:",
  "changeClassSignature.refactoring.name": "클래스 시그니처 변경",
  "changeClassSignature.already.contains.type.parameter": "''{0}''에 이미 ''{1}'' 타입 매개변수가 포함되어 있습니다"
}

ko_error_bundle = next((x for x in ko_data['new_files'] if x['filename'] == 'JavaRefactoringBundle.properties'), None)
ko_error_bundle['keys'].update(translations)
ko_error_bundle['key_count'] = len(ko_error_bundle['keys'])

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(ko_data, f, ensure_ascii=False, indent=2)

print("Updated JavaRefactoringBundle part 2")