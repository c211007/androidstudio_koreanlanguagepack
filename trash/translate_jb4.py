import json
import os

file_path = 'missing_translations/missing_keys_korean.json'
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

bundle_name = 'JavaBundle.properties'
translations = {
    'type.information.locality': '지역성(Locality)',
    'type.information.local.object': '로컬 객체',
    'type.information.type': '타입(Type)',
    'simplify.optional.chain.inspection.remove.redundant.steps.from.optional.chain': 'Optional 체인에서 중복되는 단계 제거',
    'simplify.optional.chain.inspection.to.x': 'Optional 체인을 \'\'{0}\'\'(으)로 단순화',
    'simplify.optional.chain.inspection.map.or.else.description': 'Optional 체인을 단순화할 수 있습니다',
    'simplify.optional.chain.inspection.optional.rewrapping.name': '래핑 해제(Unwrap)',
    'simplify.optional.chain.inspection.optional.rewrapping.description': '불필요한 Optional 재래핑',
    'simplify.optional.chain.inspection.or.else.return.fix.name': 'null 검사를 {0}({1})(으)로 바꾸기',
    'simplify.optional.chain.inspection.or.else.return.fix.description': 'null 검사를 제거할 수 있습니다',
    'simplify.optional.chain.inspection.or.else.non.null.fix.name': 'null 검사를 ifPresent()로 바꾸기',
    'simplify.optional.chain.inspection.or.else.non.null.fix.description': '\'ifPresent\'를 사용하여 null 검사를 제거할 수 있습니다',
    'simplify.optional.chain.inspection.fix.name.remove.redundant.optional.chain': '중복 Optional 체인 제거',
    'simplify.optional.chain.inspection.fix.description.optional.chain.can.be.eliminated': 'Optional 체인을 제거할 수 있습니다',
    'simplify.optional.chain.inspection.fix.description.replace.with.value.of.name': '\'String.valueOf()\'로 바꾸기',
    'simplify.optional.chain.inspection.fix.description.replace.with.value.of.description': 'Optional 체인을 \'String.valueOf()\'로 바꿀 수 있습니다',
    'generate.test.support.method.error.no.template.found.for.framework': '{0}:{1}에 대한 템플릿을 찾을 수 없습니다',
    'generate.test.support.method.error.method.already.exists': '{0} 메서드가 이미 존재합니다',
    'generate.test.support.method.error.cannot.generate.method': '메서드를 생성할 수 없습니다: {0}',
    'base.package.project.wizard.error.x.not.valid.package': '{0}은(는) 유효한 패키지 이름이 아닙니다',
    'class.patterns.separator.mark.code.as.entry.point.if.qualified.name.matches': '정규화된 이름이 일치하는 경우 코드를 진입점으로 표시',
    'class.patterns.error.method.pattern.0.must.be.a.valid.java.identifier': '메서드 패턴 \'\'{0}\'\'은(는) 유효한 Java 식별자여야 하며, 자리 표시자로 \'\'*\'\'만 허용됩니다.',
    'class.patterns.error.class.pattern.0.must.be.a.valid.java.qualifier': '패턴은 유효한 Java 정규화된 이름이어야 하며, 자리 표시자로 \'*\'만 허용됩니다.',
    'code.style.generation.settings.error.not.valid.identifier.part.in.prefix': '접두사 \'\'{0}\'\'에 유효하지 않은 Java 식별자 부분이 있습니다',
    'code.style.generation.settings.error.not.valid.identifier.part.in.suffix': '접미사 \'\'{0}\'\'에 유효하지 않은 Java 식별자 부분이 있습니다',
    'hide.out.of.cyclic.packages.action.text': '순환 종속성이 없는 패키지 숨기기',
    'hide.out.of.cyclic.packages.action.description': '순환 종속성이 없는 패키지를 숨깁니다',
    'generate.missed.tests.action.error.no.tests.found': '테스트를 찾을 수 없습니다.',
    'generate.missed.tests.action.failed.to.detect.framework': '{0}의 테스트 프레임워크를 감지하지 못했습니다',
    'pull.up.accessible.conflict': '{0}에 접근할 수 없게 됩니다',
    'pull.up.accessible.conflict.1': '{1}에서 {0}에 접근할 수 없게 됩니다',
    'pull.up.concrete.inherit.abstract.method.conflict': '구체(Concrete) {0}이(가) 새로운 추상 메서드를 상속합니다',
    'pull.up.members.usage.view.description.code.references.node': '"{0}"(으)로 멤버를 올릴(pull up) 클래스',
    'pull.up.members.usage.view.description.processed.elements.node': '{0} 클래스에서 멤버 올리기(Pull up)',
    'refactoring.method.reference.to.lambda.conflict': '메서드 참조가 람다로 변환됩니다',
    'introduce.variable.change.type.adv': '타입을 변경하려면 {0}을(를) 누르세요',
    'introduce.variable.reassign.adv': '기존 변수를 재할당하려면 {0}을(를) 누르세요',
    'introduce.functional.variable.accessibility.conflict': '{0} 변수는 실질적으로 final(effectively final)이 아니므로 함수형 표현식 내에서 접근할 수 없습니다',
    'introduce.functional.variable.interface.chooser.title': '적용 가능한 함수형 인터페이스 선택: {0} -> {1}',
    'introduce.functional.variable.nothing.found.message': '적용 가능한 함수형 인터페이스를 찾을 수 없습니다'
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

print(f'Updated {bundle_name} (Keys 121-160)')
