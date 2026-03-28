import json
import os

file_path = 'missing_translations/missing_keys_korean.json'
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

bundle_name = 'JavaBundle.properties'
translations = {
    'introduce.parameter.object.no.accessor.conflict.message': '\'\'{1}\'\' 필드에 대한 {0, choice, 0#Getter|1#Setter}가 필요합니다',
    'push.down.anonymous.conflict': '익명 클래스(anonymous class)로의 implements 밀어내기(push down)를 할 수 없습니다',
    'push.down.static.nonstatic.conflict': '정적(Static) {0}을(를) 비정적(non-static) {1}(으)로 밀어낼(push down) 수 없습니다',
    'push.down.missed.implementation.conflict': '추상(Abstract)이 아닌 {0}에서 {1}의 구현이 누락됩니다',
    'push.down.super.method.call.changed.conflict': '슈퍼 메서드 호출이 다른 메서드로 확인(resolve)됩니다',
    'move.classes.invalid.destination.package.name.message': '\'\'{0}\'\'은(는) 유효하지 않은 대상 패키지 이름입니다',
    'move.classes.destination.class.not.found.message': '대상 클래스를 찾을 수 없습니다',
    'move.class.import.from.default.package.conflict': '기본 패키지에서 {0}에 접근할 수 없게 됩니다',
    'destination.combo.test.root.not.expected.conflict': '소스 루트가 예상되지만 테스트 루트가 선택되었습니다',
    'destination.combo.source.root.not.expected.conflict': '테스트 루트가 예상되지만 소스 루트가 선택되었습니다',
    'leave.in.same.source.root.item': '동일한 소스 루트에 두기',
    'move.inner.select.target.package.title': '대상 패키지 선택',
    'move.member.enum.conflict': '열거형(Enum) 타입은 현재 컨텍스트에서 적용할 수 없습니다',
    'move.member.final.initializer.conflict': 'final {0}의 이니셜라이저가 뒤에 남게 됩니다.',
    'rename.package.invalid.name.error': '유효한 패키지 이름이 아닙니다',
    'rename.package.ignored.name.warning': '무시된 이름으로 패키지를 생성하려고 합니다. 결과가 표시되지 않습니다.',
    'rename.package.class.already.exist.conflict': '정규화된 이름이 \'\'{0}\'\'인 클래스가 이미 존재합니다',
    'rename.package.command.name': '패키지 이름 바꾸기',
    'class.filter.editor.table.model.column.name.pattern': '패턴',
    'class.filter.editor.table.model.column.name.isActive': '활성 상태(Is Active)',
    'create.class.mapping.dialog.title': '{0} 클래스 선택',
    'edit.contract.dialog.hint': '<html>규약 텍스트를 지정하세요<p>예: <code>_, null -> false</code><br><small>자세한 내용은 인텐션 액션 설명을 참조하세요</small></html>',
    'edit.contract.dialog.mutates.hint': '변경 가능한(mutated) 요소를 쉼표로 구분하여 지정하세요<p>예: <code>this,param1</code><p>지정되지 않은 부작용의 경우 비워 두세요.',
    'edit.range.dialog.message': '제한이 없으면 비워 두세요',
    'edit.range.error.invalid.value': '유효하지 않은 값',
    'edit.range.value.should.be.less.than': '{0}보다 작아서는 안 됩니다',
    'edit.range.value.should.be.bigger.than': '{0}보다 커서는 안 됩니다',
    'edit.range.should.not.be.greater.than.to': '\'to\'보다 커서는 안 됩니다',
    'edit.range.should.not.be.less.than.from': '\'from\'보다 작아서는 안 됩니다',
    'generate.constructor.already.exists': '생성자가 이미 존재합니다',
    'generate.equals.no.fields.for.generation': 'equals/hashCode에 포함할 필드를 찾을 수 없습니다',
    'generate.getter.and.setter.error.setters.for.read.only.not.generated': '읽기 전용 필드에 대한 Setter는 생성되지 않았습니다',
    'generate.getter.and.setter.error.no.fields': 'Getter/Setter를 생성할 필드를 찾을 수 없습니다',
    'generate.getter.and.setter.error.no.fields.without.getters.and.setters': 'Getter/Setter가 없는 필드를 찾을 수 없습니다',
    'generate.getter.error.no.fields': 'Getter를 생성할 필드를 찾을 수 없습니다',
    'generate.getter.error.no.fields.without.getters': 'Getter가 없는 필드를 찾을 수 없습니다',
    'generate.getter.setter.header.visibility.hint.': '가시성(Visibility)은 다음 경로에 따라 적용됩니다: 파일 | 설정 | 에디터 | 코드 스타일 | Java | 코드 생성',
    'generate.getter.setter.generate.all.annotations': '모든 어노테이션 복사(&A)',
    'generate.getter.setter.generate.all.annotations.tooltip': '필드에서 적용 가능한 모든 어노테이션을 복사합니다. 그렇지 않으면 null 허용 여부 어노테이션만 복사됩니다.',
    'generate.members.nothing.to.insert': '삽입할 내용을 찾을 수 없습니다'
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

print(f'Updated {bundle_name} (Keys 161-200)')
