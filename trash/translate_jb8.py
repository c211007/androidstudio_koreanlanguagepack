import json
import os

file_path = 'missing_translations/missing_keys_korean.json'
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

bundle_name = 'JavaBundle.properties'
translations = {
    'non.code.annotations.explanation.full.signature': '전체 시그니처:',
    'type.migration.command.name': '타입 마이그레이션(TypeMigration)',
    'dfa.constraint.not.null': 'null이 아님(non-null)',
    'dfa.constraint.0.not.null': '{0} (null이 아님)',
    'dfa.constraint.null.or.0': 'null 또는 {0}',
    'label.class.pattern.syntax.explanation': '생성자를 나타내려면 메서드를 비워 두세요.\\n모든 *는 정규화된 이름(점 포함)의 하나 이상의 문자와 일치합니다.',
    'dialog.message.modules.dont.refer.to.existing.annotations.library': '{0, choice, 0#모듈|2#모듈} {1}이(가) IntelliJ IDEA null 허용 여부 어노테이션이 있는 기존 \'\'{2}\'\' 라이브러리를 참조하지 않습니다. 지금 {0, choice, 0#종속성|2#종속성}을 추가하시겠습니까?',
    'tab.title.slices.grouped.by.nullness': '\\ (Null 허용 여부로 그룹화됨)',
    'exclude.0.from.auto.import': '자동 임포트(auto-import)에서 \'\'{0}\'\' 제외',
    'column.name.method.entry.point': '메서드',
    'column.name.class.entry.point': '클래스',
    'column.name.with.subclasses.entry.point': '서브클래스 포함',
    'code.vision.implementations.hint': '{0, choice, 1#구현 1개|2#구현 {0,number}개}',
    'code.vision.inheritors.hint': '{0, choice, 1#상속자 1개|2#상속자 {0,number}개}',
    'code.vision.overrides.hint': '{0, choice, 1#재정의(override) 1개|2#재정의 {0,number}개}',
    'hint.text.tostring.method.could.not.be.created.from.template': '\'\'toString()\'\' 메서드를 \'\'{0}\'\' 템플릿에서 생성할 수 없습니다',
    'hint.text.tostring.template.invalid': 'toString() 템플릿 \'\'{0}\'\'이(가) 유효하지 않습니다',
    'command.name.generate.tostring': 'toString() 생성',
    'hint.text.removed.imports': '{1, choice, 0#import|1#import} {0}개 제거됨',
    'hint.text.added.imports': ', {1, choice, 0#import|1#import} {0}개 추가됨',
    'hint.text.rearranged.imports': '임포트 재정렬됨',
    'enum.constant.ordinal': '열거형 상수 서수(ordinal): ',
    'tab.title.infer.nullity.preview': 'Null 허용 여부 추론(Infer Nullity) 미리보기',
    'inspection.message.full.description': '전체 설명',
    'popup.title.debug.recent.tests': '최근 테스트 디버그',
    'list.item.suite': '[스위트] {0}',
    'list.item.configuration': '[구성] {0}',
    'no.jre.description': '<JRE 없음>',
    'popup.content.tests.were.not.found.in.module': '\'\'{0}\'\' 모듈에서 테스트를 찾을 수 없습니다.\\n',
    'popup.content.tests.were.not.found.in.module.use.instead': '대신 {0, choice, 0#모듈 {1} |1#다음 중 하나\\n{2}\\n}을(를) 사용하세요',
    'popup.content.tests.were.not.found.in.module.search.in.dependencies': '대신 모듈 종속성에서 검색하세요',
    'postfix.template.provider.name': 'Java',
    'postfix.template.condition.void.name': 'void',
    'postfix.template.condition.non.void.name': 'non void',
    'postfix.template.condition.boolean.name': 'boolean',
    'postfix.template.condition.number.name': 'number',
    'postfix.template.condition.not.primitive.type.name': 'not primitive type(원시 타입 아님)',
    'postfix.template.condition.array.name': 'array(배열)',
    'postfix.template.condition.array.reference.name': '원시가 아닌(non-primitive) 타입의 배열',
    'inspection.redundant.unmodifiable.call.display.name': '\'\'{0}\'\' 래퍼의 중복 사용'
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

print(f'Updated {bundle_name} (Keys 241-280)')
