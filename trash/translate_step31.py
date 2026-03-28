import json
with open('missing_translations/missing_keys_korean.json', 'r', encoding='utf-8') as f:
    ko_data = json.load(f)

translations = {
  "move.nonstatic.class.from.jsp.not.supported": "JSP 페이지에서 정적(static)이 아닌 클래스를 이동하는 것은 지원되지 않습니다",
  "move.package.or.directory": "패키지 또는 디렉터리 이동...",
  "move.package.refactoring.cannot.be.applied.to.default.package": "패키지 이동 리팩터링은 기본 패키지에 적용할 수 없습니다",
  "move.packages.or.directories": "패키지 또는 디렉터리 이동...",
  "move.single.class.or.package.name.label": "{0} {1} 이동",
  "move.specified.classes": "지정된 클래스 이동",
  "move.specified.packages": "지정된 패키지 이동",
  "move.to.inner.duplicate.inner.class": "클래스 {0}에 이미 {1}이라는 이름의 내부 클래스가 있습니다",
  "move.class.or.package.build.directories": "디렉터리 목록을 구성하는 중입니다",
  "moving.local.classes.is.not.supported": "로컬 클래스 이동은 지원되지 않습니다",
  "no.class.name.specified": "지정된 클래스 이름이 없습니다",
  "no.exact.method.duplicates.were.found": "<html><b>정확히 일치하는 메서드 중복이 {0,choice, 0#없거나|1#1개|2#{0}개} 발견되었습니다</b>. 다만, 아래 표시된 것처럼 변경된 메서드에는 {1}개의 중복이 더 있습니다.</html>",
  "no.initializer.present.for.the.field": "필드에 초기화자가 없습니다",
  "no.parameter.name.specified": "지정된 매개변수 이름이 없습니다",
  "no.usages.can.be.replaced": "{0}의 사용을\\n{1}의 사용으로 바꿀 수 없습니다",
  "occurrences.to.be.migrated": "마이그레이션할 발생 항목 {0}개",
  "ok.button": "확인",
  "only.fields.variables.of.methods.of.valid.type.can.be.considered": "유효한 타입의 필드, 변수, 메서드 매개변수 또는 메서드만 고려될 수 있습니다.",
  "package.description": "패키지 {0}",
  "package.does.not.exist": "{0} 패키지가 존재하지 않습니다.\\n생성하시겠습니까?",
  "package.does.not.exist.preview": "{0} 패키지가 존재하지 않습니다.\\n나중에 리팩터링에서 이 패키지를 만듭니다.",
  "package.name.prompt": "패키지 이름(&G):",
  "parameter.description": "매개변수 {0}",
  "parameter.initializer.contains.0.but.not.all.calls.to.method.are.in.its.class": "매개변수 초기화자에 {0}이(가) 포함되어 있지만, 메서드에 대한 모든 호출이 해당 클래스에 있는 것은 아닙니다",
  "parameter.name.prompt": "매개변수 이름(&M):",
  "parameter.of.type": "타입의 매개변수(&T):",
  "parameter.type.table.column.title": "타입",
  "parameter.used.in.method.body.warning": "{0}이(가) 메서드 본문에서 사용되었습니다",
  "record.component.used.in.method.body.warning": "레코드 구성 요소 ''{0}''이(가) 사용되었습니다",
  "pass.outer.class.instance.as.parameter": "외부 클래스의 인스턴스를 매개변수로 전달(&U)",
  "please.enter.a.valid.target.package.name": "유효한 대상 패키지 이름을 입력하세요",
  "press.the.do.migrate.button": "검색 결과 패널 상단의 \\\"마이그레이션 수행\\\" 버튼을 눌러\\n\"{0}\" 마이그레이션 맵을 사용하여 마이그레이션하세요.\\n",
  "preview.usages.to.be.changed": "변경할 사용 미리보기(&P)",
  "process.duplicates.change.signature.promt": "모든 항목을 교체하려면 메서드 시그니처가 변경됩니다. 계속하시겠습니까?",
  "process.duplicates.title": "중복 처리",
  "process.methods.duplicates.title": "메서드 {2} 중복 처리 ({1}개 중 {0}개)",
  "processing.progress.text": "{0} 처리 중",
  "project.files.have.been.changed": "프로젝트 파일이 변경되었습니다.\\n리팩터링을 다시 실행하시겠습니까?",
  "push.down.delete.warning.text": "{0}멤버를 아래로 푸시(push down)하면 해당 멤버들이 삭제됩니다. 계속 진행하시겠습니까?",
  "push.down.enum.no.constants.warning.text": "Enum {0}에는 인라인할 상수가 없습니다."
}

ko_error_bundle = next((x for x in ko_data['new_files'] if x['filename'] == 'JavaRefactoringBundle.properties'), None)
ko_error_bundle['keys'].update(translations)
ko_error_bundle['key_count'] = len(ko_error_bundle['keys'])

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(ko_data, f, ensure_ascii=False, indent=2)

print("Updated JavaRefactoringBundle part 14")