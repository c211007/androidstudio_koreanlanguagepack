import json
with open('missing_translations/missing_keys_korean.json', 'r', encoding='utf-8') as f:
    ko_data = json.load(f)

translations = {
  "push.down.no.inheritors.class.warning.text": "클래스 {0}에는 상속자가 없습니다.",
  "push.down.no.inheritors.final.class.warning.text": "final 클래스 {0}에는 상속자가 없습니다.",
  "re.run.refactoring": "리팩터링 다시 실행",
  "record.description": "{1, choice, 0#|1#로컬 }레코드 {0}",
  "refactoring.cannot.be.applied.no.sources.attached": "{0} 리팩터링을 적용할 수 없습니다: 첨부된 소스가 없습니다",
  "refactoring.cannot.be.applied.to.abstract.methods": "{0} 리팩터링은 추상 메서드를 인라인할 수 없습니다",
  "refactoring.cannot.be.applied.to.inline.non.chaining.constructors": "{0} 리팩터링은 체이닝되지 않는 생성자를 인라인할 수 없습니다",
  "refactoring.cannot.be.applied.to.native.methods": "{0} 리팩터링은 native 메서드를 인라인할 수 없습니다",
  "refactoring.extract.method.dialog.duplicates.count": "{0,choice, 1#1개의|2#{0,number}개의} 중복 코드 조각을 추출된 메서드 호출로 바꿀 수 있습니다",
  "refactoring.extract.method.dialog.duplicates.pending": "중복을 찾는 중...",
  "refactoring.extract.method.dialog.duplicates.progress": "중복을 찾는 중",
  "refactoring.extract.method.inner.class.defined": "내부 클래스 {0}이(가) {1} 클래스에 이미 정의되어 있습니다.",
  "refactoring.extract.method.preview.button.refactor": "리팩터링(&R)",
  "refactoring.extract.method.preview.button.rerun": "리팩터링 다시 실행(&E)",
  "refactoring.extract.method.preview.failed": "메서드를 추출하지 못했습니다",
  "refactoring.extract.method.preview.group.duplicates": "중복된 코드 조각",
  "refactoring.extract.method.preview.group.method": "추출할 메서드",
  "refactoring.extract.method.preview.group.original": "원본 코드 조각",
  "refactoring.extract.method.preview.preparing": "Diff 준비 중",
  "refactoring.extract.method.preview.updating": "Diff 업데이트 중",
  "refactoring.extract.method.reference.to.change": "변경할 참조",
  "refactoring.introduce.variable.enum.in.label.message": "switch 레이블의 Enum 상수는 추출할 수 없습니다",
  "refactoring.is.not.supported.for.jsp.classes": "JSP 클래스에 대해서는 리팩터링이 지원되지 않습니다",
  "refactoring.is.not.supported.in.the.current.context": "현재 컨텍스트에서는 {0} 리팩터링이 지원되지 않습니다",
  "references.in.code.to.elements.from.migration.map": "\"{0}\" 마이그레이션 맵의 요소에 대한 코드 내 참조 {1}",
  "references.to.0.to.be.replaced.with.references.to.1": "''{0}''에 대한 참조가 ''{1}''에 대한 참조로 바뀝니다: {2}",
  "remove.parameter.0.no.longer.used": "더 이상 사용되지 않는 ''{0}'' 매개변수 제거",
  "rename.constructor.parameters.title": "생성자 매개변수 이름 변경",
  "rename.constructor.parameters.with.the.following.names.to": "다음 이름을 가진 매개변수 이름 변경:",
  "rename.inheritors.with.the.following.names.to.title": "다음 이름의 상속자 이름 변경:",
  "rename.module.already.exists": "''{0}'' 모듈이 프로젝트에 이미 존재합니다",
  "rename.module.directory.command": "모듈 및 디렉터리 이름을 ''{0}''(으)로 변경",
  "rename.module.directory.title": "모듈과 디렉터리 이름 변경(&A)",
  "rename.overloads": "오버로드 이름 변경(&O)",
  "rename.overloads.dialog.title": "오버로드 이름 변경",
  "rename.overloads.to.dialog.description": "오버코드 이름 변경:",
  "rename.parameter.in.hierarchy.to.dialog.description": "계층 구조에서 파라미터 이름 변경:",
  "rename.parameters.dialog.title": "매개변수 이름 변경",
  "rename.tests": "테스트 이름 변경(&E)",
  "rename.tests.title": "테스트 이름 변경"
}

ko_error_bundle = next((x for x in ko_data['new_files'] if x['filename'] == 'JavaRefactoringBundle.properties'), None)
ko_error_bundle['keys'].update(translations)
ko_error_bundle['key_count'] = len(ko_error_bundle['keys'])

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(ko_data, f, ensure_ascii=False, indent=2)

print("Updated JavaRefactoringBundle part 15")