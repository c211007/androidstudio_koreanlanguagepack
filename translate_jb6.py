import json
import os

file_path = 'missing_translations/missing_keys_korean.json'
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

bundle_name = 'JavaBundle.properties'
translations = {
    'generate.setters.no.fields': 'Setter를 생성할 필드를 찾을 수 없습니다',
    'generate.setters.no.fields.without.setters': 'Setter가 없는 필드를 찾을 수 없습니다',
    'implement.abstract.method.potential.implementations.with.weaker.access': '더 약한 접근 권한(weaker access privileges)을 가진 잠재적인 구현이 발견되었습니다: {0}',
    'implement.method.no.methods.to.implement': '구현할 메서드를 찾을 수 없습니다',
    'action.sort.by.percent.classes.which.overrides.method.text': '메서드를 재정의하는 서브클래스 비율순 정렬',
    'action.sort.by.percent.classes.which.overrides.method.description': '메서드를 재정의하는 서브클래스 비율에 따라 정렬합니다',
    'override.methods.error.no.methods': '재정의(override)할 메서드를 찾을 수 없습니다',
    'base.package.parameter.wizard.label': '기본 패키지(&P):',
    'type.migration.multi.root.toolwindow.title': '{0}의 타입 마이그레이션',
    'type.migration.single.root.toolwindow.title': '{0}의 타입을 \'\'{1}\'\'에서 \'\'{2}\'\'(으)로 마이그레이션',
    'type.migration.processed.elements.header': '타입 마이그레이션 루트',
    'type.migration.cannot.convert.message': '표현식 <b>{0}</b>의 타입을{3, choice, 0#|1# \'<b>\'{1}\'</b>\'에서} <b>{2}</b>(으)로 변환할 수 없습니다',
    'type.migration.cannot.convert.vararg.message': '호출 <b>{0}</b>을(를) vararg에서 non-vararg로 변환할 수 없습니다',
    'type.migration.replaced.notification': '{0}(으)로 교체됨',
    'type.migration.cannot.convert.tooltip': '표현식의 타입을 {0}에서 {1}(으)로 변환할 수 없습니다',
    'type.migration.cannot.convert.vararg.tooltip': '호출을 vararg에서 non-vararg로 변환할 수 없습니다',
    'type.migration.getter.rename.suggestion.text': '반환 타입이 \'\'{2}\'\'(으)로 마이그레이션되었으므로 getter 이름을 \'\'{0}\'\'에서 \'\'{1}\'\'(으)로 바꾸시겠습니까?',
    'type.migration.getter.rename.suggestion.never.migrate.method.names': '메서드 이름 마이그레이션 안 함',
    'type.migration.getter.rename.suggestion.always.migrate.method.names': '항상 메서드 이름 마이그레이션',
    'hint.text.press.to.go.through.inlined.occurrences': '인라인으로 처리된(inlined) 항목 {1}개를 순회하려면 {0}을(를) 누르세요',
    'hint.text.occurrences.were.inlined': '항목 {0}개가 인라인으로 처리되었습니다',
    'action.expand.static.import.text': '정적(Static) 임포트(Import) 확장',
    'class.cannot.be.inlined.because.a.call.to.its.constructor.is.unresolved': '생성자 호출이 확인되지(unresolved) 않아서 클래스를 인라인시킬 수 없습니다',
    'class.cannot.be.inlined.because.it.is.used.as.a.this.qualifier': '\'this\' 한정자(qualifier)로 사용되기 때문에 클래스를 인라인시킬 수 없습니다',
    'class.cannot.be.inlined.because.it.is.used.in.a.throws.clause': '\'throws\' 절에 사용되기 때문에 클래스를 인라인시킬 수 없습니다',
    'class.cannot.be.inlined.because.it.is.used.in.a.catch.clause': '\'catch\' 절에 사용되기 때문에 클래스를 인라인시킬 수 없습니다',
    'class.cannot.be.inlined.because.it.has.usages.of.its.class.literal': '클래스 리터럴의 사용이 있으므로 클래스를 인라인시킬 수 없습니다',
    'class.cannot.be.inlined.because.it.has.static.initializers': '클래스에 정적(static) 이니셜라이저가 있으므로 인라인시킬 수 없습니다',
    'class.cannot.be.inlined.because.it.has.usages.of.fields.not.inherited.from.its.superclass': '클래스가 슈퍼클래스로부터 상속되지 않은 필드를 사용하므로 인라인시킬 수 없습니다',
    'class.cannot.be.inlined.because.it.has.static.fields.with.non.constant.initializers': '클래스에 상수가 아닌 이니셜라이저를 가진 정적(static) 필드가 있으므로 인라인시킬 수 없습니다',
    'class.cannot.be.inlined.because.it.has.static.non.final.fields': '클래스에 final이 아닌 정적(static) 필드가 있으므로 인라인시킬 수 없습니다',
    'class.cannot.be.inlined.because.it.has.usages.of.its.inner.classes': '클래스가 자체 내부 클래스를 사용하므로 인라인시킬 수 없습니다',
    'class.cannot.be.inlined.because.it.has.static.inner.classes': '클래스에 정적(static) 내부 클래스가 있으므로 인라인시킬 수 없습니다',
    'class.cannot.be.inlined.because.it.has.static.methods': '클래스에 정적(static) 메서드가 있으므로 인라인시킬 수 없습니다',
    'class.cannot.be.inlined.because.there.are.usages.of.its.methods.not.inherited.from.its.superclass.or.interface': '슈퍼클래스나 인터페이스에서 상속되지 않은 메서드의 사용이 있으므로 클래스를 인라인시킬 수 없습니다',
    'class.cannot.be.inlined.because.its.constructor.contains.return.statements': '생성자에 \'return\' 문이 있으므로 클래스를 인라인시킬 수 없습니다',
    'class.cannot.be.inlined.because.an.interface.implemented.by.it.cannot.be.resolved': '구현한 인터페이스를 확인할 수(resolved) 없어 클래스를 인라인시킬 수 없습니다',
    'class.cannot.be.inlined.because.its.superclass.cannot.be.resolved': '슈퍼클래스를 확인할 수(resolved) 없어 클래스를 인라인시킬 수 없습니다',
    'library.classes.cannot.be.inlined': '라이브러리 클래스는 인라인시킬 수 없습니다',
    'enums.cannot.be.inlined': '열거형(Enum)은 인라인시킬 수 없습니다'
}

found = False
for file_entry in data['new_files']:
    if file_entry['filename'] == bundle_name:
        file_entry.setdefault('keys', {}).update(translations)
        found = True
        break
if not found:
    data['new_files'].append({'filename': bundle_name, 'keys': translations})

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

print(f'Updated {bundle_name} (Keys 201-240)')
