import json
import os

file_path = 'missing_translations/missing_keys_korean.json'
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

bundle_name = 'JavaBundle.properties'
translations = {
    'interfaces.cannot.be.inlined': '인터페이스는 인라인시킬 수 없습니다',
    'records.cannot.be.inlined': '레코드(Record) 클래스는 인라인시킬 수 없습니다',
    'annotation.types.cannot.be.inlined': '어노테이션 타입은 인라인시킬 수 없습니다',
    'type.parameters.cannot.be.inlined': '타입 매개변수는 인라인시킬 수 없습니다',
    'postfix.template.editor.choose.class.title': '클래스 선택',
    'null.check.surrounder.description': 'if (expr != null) {...}',
    'push.method.down.command.name': '메서드 밀어내기(Push down)…',
    'show.siblings.choose.super.class.title': '슈퍼클래스 또는 인터페이스 선택',
    'show.siblings.find.usages.method.title': '슈퍼 메서드',
    'show.siblings.find.usages.class.title': '슈퍼클래스/인터페이스',
    'switch.stmt.template.description': 'switch (expr) {...}',
    'wrap.return.value.created.class.not.accessible.conflict': '호출 위치에서 생성된 클래스에 접근할 수 없습니다',
    'wrap.return.value.existing.class.does.not.have.getter.conflict': '기존 클래스에 선택한 필드에 대한 getter가 없습니다',
    'wrap.return.value.existing.class.does.not.have.appropriate.constructor.conflict': '기존 클래스에 적절한 생성자가 없습니다',
    'wrap.return.value.anonymous.class.presentation': '익명(Anonymous) {0}',
    'empty.title': '비어 있음',
    'separator.annotations.to.copy': '복사할 어노테이션',
    'action.go.to.functional.implementation.text': '함수형 인터페이스 구현 찾기',
    'action.go.to.implementation.text': '구현으로 이동',
    'action.go.to.subclass.text': '서브클래스로 이동',
    'action.go.to.overriding.methods.text': '재정의하는(Overriding) 메서드로 이동',
    'action.go.to.super.method.text': '슈퍼 메서드로 이동',
    'tooltip.recursive.call': '재귀(Recursive) 호출',
    'label.compact.constructor': '컴팩트(Compact) 생성자',
    'label.canonical.constructor': '표준(Canonical) 생성자',
    'edit.contract.dialog.checkbox.impure.method': '메서드가 부작용(side effect)을 생성할 수 있음(&S)',
    'separator.mark.as.entry.point.if.annotated.by': '다음 어노테이션이 있는 경우 진입점(entry point)으로 표시:',
    'separator.mark.field.as.implicitly.written.if.annotated.by': '다음 어노테이션이 있는 경우 필드를 암시적으로 작성된(implicitly written) 것으로 표시:',
    'rename.super.methods.chooser.popup.title': '{0}에 슈퍼 메서드가 있습니다',
    'rename.super.base.chooser.popup.title': '{0}이(가) {2}의 메서드를{1, choice, 0# 구현합니다|1# 재정의합니다}',
    'add.methods.dialog.or': '\\ 또는',
    'command.name.delegate.detected.change': '위임(Delegate)',
    'encapsulate.fields.dialog.javadoc.title': 'Javadoc',
    'dependant.sdk.unsatisfied.dependency.message': '먼저 Java SDK를 구성해야 합니다',
    'javadoc.gen.error.modules.without.module.info': '{0} 모듈에 module-info.java 파일이 없으므로 IDEA에서 Javadoc을 생성할 수 없습니다',
    'javadoc.gen.error.module.source.path.is.not.evaluated': 'module-source-path를 평가할 수 없으므로 IDEA에서 Javadoc을 생성할 수 없습니다',
    'generate.members.implement.command': '구현',
    'non.code.annotations.explanation.external.and.inferred.available': '외부 및 <i>추론된(inferred)</i> 어노테이션을 사용할 수 있습니다.',
    'non.code.annotations.explanation.external.available': '외부 어노테이션을 사용할 수 있습니다.',
    'non.code.annotations.explanation.inferred.available': '<i>추론된(Inferred)</i> 어노테이션을 사용할 수 있습니다.'
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
