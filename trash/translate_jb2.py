import json
import os

file_path = 'missing_translations/missing_keys_korean.json'
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

bundle_name = 'JavaBundle.properties'
translations = {
    'generate.tostring.method.already.exists.dialog.me\\': 'ssage=기존 {0} 메서드 바꾸기',
    'intention.error.make.sealed.class.inheritors.not.in.java.file': '일부 상속자가 Java 파일에 없습니다',
    'intention.error.make.sealed.class.different.modules': '일부 상속자가 다른 모듈에 있습니다',
    'intention.error.make.sealed.class.interface.has.no.inheritors': '인터페이스에 상속자가 없습니다',
    'inspection.fill.permits.list.no.missing.inheritors': '봉인된(Sealed) 클래스에 누락된 상속자가 없습니다',
    'inspection.fill.permits.list.display.name': '동일한 파일의 서브클래스가 봉인된(sealed) 클래스의 permits 절에서 누락되었습니다',
    'inspection.fill.permits.list.fix.name': '누락된 서브클래스를 permits 절에 추가',
    'update.external.annotations': '외부 어노테이션 업데이트',
    'intention.create.switch.statement': 'switch 문 생성',
    'inspection.message.pattern.variables.can.be.replaced.with.cast.preserve.option': '빠른 수정(quickfix) 중에 패턴의 사용되지 않는 변수를 보존하려고 시도합니다',
    'inspection.message.pattern.variables.can.be.replaced.with.cast': '패턴과 함께 \'instanceof\' 사용',
    'inspection.message.pattern.variables.can.be.replaced.with.cast.family.name': '패턴 없이 바꾸기',
    'inspection.message.pattern.variables.can.be.replaced.with.cast.fix.name': '\'\'{0}\'\'을(를) 캐스트로 바꾸기',
    'inspection.message.record.can.be.converted.to.class': '레코드를 클래스로 변환할 수 있습니다',
    'intention.family.name.convert.record.to.class': '레코드를 클래스로 변환',
    'class.can.be.record.display.name': '클래스가 레코드 클래스일 수 있습니다',
    'class.can.be.record.quick.fix': '레코드 클래스로 변환',
    'class.can.be.record.suggest.renaming.accessors': '접근자(accessor) 메서드 이름 바꾸기 제안',
    'class.can.be.record.record.highlight.when.semantics.change': '멤버의 접근성이 높아져도 보고하지 않음',
    'class.can.be.record.record.highlight.when.semantics.change.description': '빠른 수정(Quick-fix)은 계속 사용할 수 있습니다',
    'class.can.be.record.suppress.conversion.if.annotated': '클래스에 다음 어노테이션이 있는 경우 변환 억제:',
    'class.can.be.record.suppress.conversion.if.annotated.fix.name': '\'\'{0}\'\' 어노테이션이 있는 경우 레코드 변환 억제',
    'extracted.class.should.have.unique.name': '추출된 클래스는 고유한 이름을 가져야 합니다. \'\'{0}\'\' 이름은 내부 클래스 중 하나에서 이미 사용 중입니다',
    'invalid.extracted.class.name': '\'\'{0}\'\'은(는) 유효하지 않은 추출 클래스 이름입니다',
    'caller.chooser.referenced.code.title': '참조된 코드',
    'dialog.title.choose.annotation': '{0} 어노테이션 선택',
    'unchecked.warning.inspection.settings.ignore.unchecked.assignment': '확인되지 않은(unchecked) 할당 무시',
    'unchecked.warning.inspection.settings.ignore.unchecked.generics.array.creation.for.vararg.parameter': 'vararg 매개변수에 대해 확인되지 않은(unchecked) 제네릭 배열 생성 무시',
    'unchecked.warning.inspection.settings.ignore.unchecked.call.as.member.of.raw.type': '원시(raw) 타입의 멤버로서 확인되지 않은(unchecked) 호출 무시',
    'unchecked.warning.inspection.settings.ignore.unchecked.cast': '확인되지 않은(unchecked) 캐스트 무시',
    'unchecked.warning.inspection.settings.ignore.unchecked.overriding': '확인되지 않은(unchecked) 재정의(overriding) 무시',
    'unchecked.warning.inspection.reason.expr.has.raw.type.so.result.erased': '. 이유: \'\'{0}\'\'이(가) 원시(raw) 타입이므로 {1}의 결과가 지워졌습니다',
    'unchecked.warning.inspection.message.unchecked.generics.array.creation.for.varargs.parameter': 'varargs 매개변수에 대한 확인되지 않은(unchecked) 제네릭 배열 생성',
    'type.migration.dialog.message.invalid.type': '\'\'{0}\'\'은(는) 유효한 타입이 아닙니다',
    'type.migration.dialog.message.void.not.applicable': '메서드 반환 타입만 \'void\'로 마이그레이션할 수 있습니다',
    'type.migration.dialog.message.vararg.type.not.applicable': '메서드의 마지막 매개변수만 vararg 타입으로 마이그레이션할 수 있습니다',
    'type.migration.dialog.message.disjunction.type.not.applicable': 'catch 블록 매개변수만 공용체(union) 타입으로 마이그레이션할 수 있습니다',
    'stream.to.loop.inspection.message.replace.stream.api.chain.with.loop': 'Stream API 체인을 루프로 바꾸기',
    'stream.to.loop.inspection.message.replace.foreach.call.with.loop': '\'forEach()\' 호출을 루프로 바꾸기',
    'todo.index.not.available': '해당 없음(N/A)'
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

print(f'Updated {bundle_name} (Keys 41-80)')
