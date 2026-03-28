import json
with open('missing_translations/missing_keys_korean.json', 'r', encoding='utf-8') as f:
    ko_data = json.load(f)

translations = {
  "this.reference.only.and.keep.super.class": "이 참조만 인라인하고 슈퍼 클래스 유지(&K)",
  "this.reference.only.and.keep.the.class": "이 참조만 인라인하고 클래스 유지(&K)",
  "this.reference.only.and.keep.the.field": "이 참조만 인라인하고 필드 유지(&K)",
  "turn.refs.to.super.command": "{0}의 사용을 {1}(으)로 바꾸는 중",
  "turnRefsToSuper.change.usages.to": "{0}의 사용을 다음으로 변경(&C):",
  "turnRefsToSuper.use.superclass.in.instanceof": "instanceof에서 인터페이스/슈퍼클래스 사용(&U)",
  "type.migration.action.name": "타입 마이그레이션",
  "type.migration.choose.scope.title": "시그니처 변경이 발생할 수 있는 범위 선택",
  "type.migration.conflicts.found": "마이그레이션 충돌 발견",
  "type.migration.exclude.action.text": "제외(&E)",
  "type.migration.include.action.text": "포함(&I)",
  "type.migration.return.type.of.method.label": "{1} 메서드의 {0} 반환 타입을 다음으로 마이그레이션",
  "type.migration.type.of.field.label": "{1} 필드의 {0} 타입을 다음으로 마이그레이션",
  "type.migration.type.of.record.component.label": "{1} 레코드 구성 요소의 {0} 타입을 다음으로 마이그레이션",
  "type.migration.type.of.variable.label": "{1} 변수의 {0} 타입을 다음으로 마이그레이션",
  "type.migration.type.of.pattern.variable.label": "{1} 패턴 변수의 {0} 타입을 다음으로 마이그레이션",
  "type.migration.type.of.parameter.label": "{1} 매개변수의 {0} 타입을 다음으로 마이그레이션",
  "type.migration.class.type.argument.label": "클래스 타입 매개변수 {0}을(를) 다음으로 마이그레이션",
  "type.migration.migrate.button.text": "마이그레이션(&M)",
  "type.migration.no.conflicts.found": "마이그레이션 충돌이 발견되지 않았습니다",
  "type.migration.no.scope.warning.message": "범위가 선택되지 않았습니다",
  "type.migration.reasons.to.migrate": "마이그레이션 이유 발견",
  "type.migration.rerun.button.text": "타입 마이그레이션 다시 실행(&R)",
  "type.migration.select.suggestion": "마이그레이션 할 이유를 찾을 대상 루트 선택",
  "type.of.the.selected.expression.cannot.be.determined": "선택한 표현식의 타입을 결정할 수 없습니다.",
  "unable.to.start.type.migration": "타입 마이그레이션을 시작할 수 없습니다",
  "unknown.expression.type": "알 수 없는 표현식 타입입니다.",
  "unused.overriding.methods.title": "사용되지 않는 재정의(Overriding) 메서드",
  "use.interface.where.possible.title": "가능한 곳에 인터페이스 사용",
  "use.super.references.prompt": "이 단계에서 {0}이(가) {1}의 사용을 분석하고\\n가능한 경우 {2}의 사용으로 바꿀 수 있습니다.\\n진행하시겠습니까?",
  "use.variable.initializer.to.initialize.parameter": "변수 초기화자를 사용하여 매개변수 초기화(&I)",
  "variable.0.is.changed.before.last.access": "''{1}'' 변수에 마지막으로 접근하기 전에 ''{0}'' 변수가 변경됩니다.",
  "variable.does.not.have.an.initializer": "{0} 변수에 초기화자가 없습니다.",
  "variable.is.accessed.for.writing": "''{0}'' 변수에 쓰기 접근을 시도했습니다",
  "variable.is.never.used.before.modification": "{0} 변수는 수정되기 전에 한 번도 사용되지 않았습니다",
  "variable.of.type": "타입의 변수(&T):",
  "would.you.like.to.replace.default.constructor.of.0.with.factory.method": "{0}의 기본 생성자를 팩터리 메서드로 바꾸시겠습니까?",
  "wrap.return.value.create.inner.class": "내부 클래스 생성(&I)",
  "wrap.return.value.create.new.class": "새 클래스 생성(&C)",
  "wrap.return.value.existing.class.name": "이름"
}

ko_error_bundle = next((x for x in ko_data['new_files'] if x['filename'] == 'JavaRefactoringBundle.properties'), None)
ko_error_bundle['keys'].update(translations)
ko_error_bundle['key_count'] = len(ko_error_bundle['keys'])

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(ko_data, f, ensure_ascii=False, indent=2)

print("Updated JavaRefactoringBundle part 18")