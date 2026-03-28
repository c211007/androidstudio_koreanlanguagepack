import json

ko_dict = {
  "script.text.multiple.script.definitions.are.applicable.for.this.script": "이 스크립트에 여러 스크립트 정의를 적용할 수 있습니다. {0}이(가) 사용됩니다.",
  "roots.description.text.update.source.roots.for.non.jvm.modules.in.kotlin.project": "Kotlin 프로젝트의 비 JVM 모듈 소스 루트 업데이트",
  "configuration.maven.group.name": "Kotlin Maven 프로젝트 가져오기",
  "configuration.message.enter.fully.qualified.method.name": "정규화된 메서드 이름 입력:",
  "configuration.migration.group.name": "Kotlin: 최신 버전으로 마이그레이션할 수 있음",
  "kotlin.jps.plugin.group.name": "Kotlin JPS 플러그인",
  "configuration.name.method": "메서드",
  "configuration.status.text.installing": "설치 중…",
  "configuration.title.add.exclusion": "제외 추가",
  "configuration.title.edit.exclusion": "제외 편집",
  "configuration.kotlin.code.style.group.name": "Kotlin 공식 코드 스타일 사용 가능",
  "kotlin.dist.downloading.failed.group.name": "Kotlin 배포본 다운로드 실패",
  "0.1.is.never.used": "{0} ''{1}''이(가) 한 번도 사용되지 않음",
  "0.has.detected.1.code.fragments.in.2.that.can.be.replaced.with.3": "{0}이(가) {3}(으)로 대체될 수 있는 {2}에 포함된 {1}개의 코드 조각을 발견했습니다. 이를 검토하고 대체하시겠습니까?",
  "0.will.become.invisible.after.extraction": "{0}은(는) 추출 후 표시되지 않습니다.",
  "0.will.no.longer.be.accessible.after.extraction": "추출 후 {0}에 더 이상 액세스할 수 없습니다.",
  "action.text.append": "추가",
  "action.text.cancel": "취소",
  "action.text.continue": "계속",
  "action.text.overwrite": "덮어쓰기",
  "button.text.move.nested.class.0.to.upper.level": "중첩 클래스 {0} 상위 수준으로 이동(&N)",
  "button.text.move.nested.class.0.to.another.class": "중첩 클래스 {0} 다른 클래스로 이동(&M)",
  "cannot.extract.super.call": "super-call을 추출할 수 없습니다.",
  "cannot.inline.property.with.accessor.s.and.backing.field": "접근자 및 백킹 필드가 포함된 속성을 인라인할 수 없습니다.",
  "cannot.introduce.parameter.of.0.type": "''{0}'' 유형의 매개변수를 도입할 수 없습니다.",
  "cannot.refactor.expression.has.unit.type": "unit 유형의 표현식을 도입할 수 없습니다.",
  "cannot.refactor.no.container": "이 위치에서 리팩터링할 수 없습니다.",
  "cannot.refactor.no.expression": "표현식 없이 리팩터링을 수행할 수 없습니다.",
  "cannot.refactor.no.type": "유형 없이 리팩터링을 수행할 수 없습니다.",
  "cannot.refactor.not.expression": "도입할 표현식을 찾을 수 없습니다.",
  "cannot.refactor.package.expression": "패키지 참조를 도입할 수 없습니다.",
  "cannot.refactor.syntax.errors": "오류 코드 때문에 리팩터링할 수 없습니다.",
  "cannot.refactor.synthesized.function": "합성 함수를 리팩터링할 수 없습니다.",
  "checkbox.text.declare.with.var": "var로 선언(&V)",
  "checkbox.text.delete.empty.source.files": "비어 있는 소스 파일 삭제(&D)",
  "checkbox.text.extension.property": "확장 속성(&X):",
  "checkbox.text.introduce.default.value": "기본값 도입(&D)",
  "checkbox.text.open.moved.files.in.editor": "편집기에서 이동된 멤버 열기",
  "checkbox.text.replace.all.occurrences.0": "모든 항목 대체({0})(&R)",
  "checkbox.text.search.references": "참조 검색(&R)",
  "checkbox.text.specify.type.explicitly": "명시적으로 유형 지정(&T)",
  "checkbox.text.update.package.directive": "패키지 지시문 업데이트(Kotlin 파일)",
  "column.name.receiver": "수신자:",
  "column.name.context.parameter": "컨텍스트 매개변수:",
  "column.name.default.parameter": "기본 매개변수:",
  "column.name.val.var": "Val/Var",
  "declarations.are.used.outside.of.selected.code.fragment": "다음 선언이 선택한 코드 조각 밖에서 사용됩니다:",
  "declarations.will.move.out.of.scope": "다음 선언은 추출된 함수 본문 밖에서는 사용할 수 없습니다:",
  "description.a.reference.to.extracted.type.parameter": "추출된 유형 매개변수에 대한 참조",
  "error.cant.refactor.vararg.functions": "가변 인수가 있는 함수는 리팩터링할 수 없습니다."
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

print(f"Updated {filename} (Keys 591-640)")

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
