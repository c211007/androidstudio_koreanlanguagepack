import json
with open('missing_translations/missing_keys_korean.json', 'r', encoding='utf-8') as f:
    ko_data = json.load(f)

translations = {
  "method.0.will.override.a.method.of.the.base.class": "메서드가 슈퍼 {1}의 {0}을(를) 재정의(override)합니다",
  "method.call.would.be.linked.to.0.after.rename": "이름을 바꾼 후에는 다른 {0}이(가) 호출됩니다",
  "method.column": "메서드",
  "method.description": "메서드 {0}",
  "method.does.not.have.a.body": "{0} 메서드에 본문이 없습니다",
  "method.duplicates.found.message": "{0, choice, 1#1개의 코드 조각|2#{0,number}개의 코드 조각}을 찾았습니다",
  "method.has.an.empty.body": "{0} 메서드 본문이 비어있습니다.",
  "method.is.not.a.constructor": "메서드가 생성자가 아닙니다",
  "migration.class": "클래스",
  "migration.dialog.ok.button.text": "실행",
  "migration.dialog.title": "패키지 및 클래스 마이그레이션",
  "migration.dialog.alert.name": "마이그레이션 맵 삭제",
  "migration.dialog.alert.text": "''{0}'' 마이그레이션을 삭제하시겠습니까?",
  "migration.dialog.alert.delete": "삭제",
  "migration.dialog.link.delete": "삭제",
  "migration.dialog.link.duplicate": "복제 및 편집...",
  "migration.dialog.link.edit": "편집...",
  "migration.dialog.scope.label": "범위:",
  "migration.dialog.scope.whole.project": "전체 프로젝트",
  "migration.entry.class": "클래스",
  "migration.entry.new.name": "새 이름:",
  "migration.entry.old.name": "이전 이름:",
  "migration.entry.package": "패키지",
  "migration.map.description.label": "맵 설명:",
  "migration.map.name.prompt": "맵 이름:",
  "migration.new.name.column.header": "새 이름",
  "migration.no.usages.found.in.the.project": "프로젝트에서 사용을 찾지 못했습니다",
  "migration.old.name.column.header": "이전 이름",
  "migration.package": "패키지",
  "migration.package.with.subpackages": "하위 패키지가 있는 패키지",
  "migration.title": "마이그레이션",
  "migration.type.column.header": "타입",
  "migration.edit.duplicated.migration.name": "{0} 복사본",
  "migration.edit.existing.name": "이름이 같은 마이그레이션이 이미 존재합니다.",
  "migration.edit.empty.name": "마이그레이션 이름은 비워둘 수 없습니다.",
  "migration.edit.empty.table": "마이그레이션 테이블은 비워둘 수 없습니다.",
  "migration.edit.copy.existing": "기존 항목 복사",
  "move.class": "클래스 이동...",
  "move.class.refactoring.cannot.be.applied.to.anonymous.classes": "클래스 이동 리팩터링은 익명 클래스에 적용할 수 없습니다",
  "move.class.to.inner.command.name": "{0, choice, 1#클래스|2#클래스들} {1}을(를) {2}(으)로 이동"
}

ko_error_bundle = next((x for x in ko_data['new_files'] if x['filename'] == 'JavaRefactoringBundle.properties'), None)
ko_error_bundle['keys'].update(translations)
ko_error_bundle['key_count'] = len(ko_error_bundle['keys'])

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(ko_data, f, ensure_ascii=False, indent=2)

print("Updated JavaRefactoringBundle part 12")