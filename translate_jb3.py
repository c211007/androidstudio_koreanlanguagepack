import json
import os

file_path = 'missing_translations/missing_keys_korean.json'
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

bundle_name = 'JavaBundle.properties'
translations = {
    'simplify.stream.inspection.message.can.be.replaced': '\'\'{0}\'\'을(를) \'\'{1}\'\'(으)로 바꿀 수 있습니다',
    'simplify.stream.inspection.message.can.be.replaced.may.change.semantics': '\'\'{0}\'\'을(를) \'\'{1}\'\'(으)로 바꿀 수 있습니다(시맨틱이 변경될 수 있음)',
    'inspection.message.filter.is.present.chain.can.be.replaced.with.anymatch': '\'\'filter().{0}().isPresent()\'\' 체인을 \'\'anyMatch()\'\'로 바꿀 수 있습니다',
    'simplify.stream.match.negation.fix.name': '{0}을(를) {1}(...)(으)로 바꾸기',
    'simplify.stream.collection.creation.fix.name': '\'\'{0}\'\' 생성자로 바꾸기',
    'simplify.stream.simple.stream.of.fix.name.use.stream.element.explicitly': 'Stream 요소를 명시적으로 사용',
    'simplify.stream.simple.stream.of.message': '불필요한 단일 요소 Stream',
    'simplify.stream.replace.with.element.iteration.fix.message': '요소 반복으로 바꿀 수 있습니다',
    'simplify.stream.remove.boolean.identity.fix.name': '이전 \'map()\' 호출과 병합',
    'simplify.stream.remove.boolean.identity.fix.message': '이전 \'map()\' 호출과 병합할 수 있습니다',
    'simplify.stream.replace.support.with.collection.fix.name': '\'\'{0}.{1}()\'\' 호출로 바꾸기',
    'simplify.stream.replace.support.with.collection.fix.message': '\'\'{0}.{1}()\'\' 호출로 바꿀 수 있습니다',
    'simplify.stream.swap.filter.and.map.fix.name': '\'filter()\'와 \'map()\' 바꾸기',
    'simplify.stream.swap.filter.and.map.fix.message': '\'filter()\'와 \'map()\'을 바꿀 수 있습니다',
    'simplify.stream.inspection.iterate.take.while.fix.name': '인자가 3개인 \'iterate()\'로 바꾸기',
    'simplify.stream.inspection.iterate.take.while.fix.message': '인자가 3개인 \'iterate()\'로 바꿀 수 있습니다',
    'side.effects.pattern.message': '<html>\\n<body>\\n{0}에서 부작용(side effect)이 발견될 수 있습니다<br>\\n다음을 수행할 수 있습니다:\\n<br>\\n-\\\\&nbsp;관련된 모든 표현식과 함께 변수 사용을 <b>제거</b>하거나,<br>\\n-\\\\&nbsp;변수에 할당된 표현식을 자체 구문으로 <b>변환</b>합니다.<br>\\n<div style=\"padding-left: 0.6cm;\">\\n  즉,<br>\\n  <table border=\"0\">\\n    <tr>\\n      <td><code>{1};</code></td>\\n    </tr>\\n  </table>\\n  는 다음이 됩니다: <br>\\n  <table border=\"0\">\\n    <tr>\\n      <td><code>{2};</code></td>\\n    </tr>\\n  </table>\\n</div>\\n</body>\\n</html>',
    'side.effects.expression.presentation': '표현식 \'\'{0}\'\'',
    'change.signature.from.usage.short.name': '<html> {0}({1})의 시그니처 변경</html>',
    'default.param.value.warning': '{0}이(가) 이미 존재합니다',
    'qualify.static.constant.access': '정적(Static) 상수 접근의 정규화(Qualify)',
    'qualify.static.access.command.name': '정적(Static) 접근의 정규화(Qualify)',
    'qualify.static.call.fix.text': '정적(Static) 호출의 정규화(Qualify)',
    'pull.members.up.fix.name': '멤버 올리기(Pull Members Up)',
    'extract.superclass.command.name': '슈퍼클래스 추출',
    'extract.interface.command.name': '인터페이스 추출',
    'choose.super.class.popup.title': '슈퍼클래스 선택',
    'intention.name.pull.method.up.and.make.it.abstract.conditionally': '\'\'{0}\'\' 메서드를 \'\'{1}\'\'(으)로 올리기{2, choice, 0# 및 추상(abstract)으로 만들기|1#}',
    'intention.name.extract.method.to.new.interface': '\'\'{0}\'\' 메서드를 새 인터페이스로 추출',
    'intention.name.pull.method.up.make.it.abstract': '\'\'{0}\'\' 메서드를 올리고(Pull up) 추상(abstract)으로 만들기',
    'intention.name.pull.method.up': '\'\'{0}\'\' 메서드 올리기(Pull up)',
    'intention.name.copy.to.final.temp.variable': '\'\'{0}\'\'을(를) {1, choice, 0#|1#effectively(실질적) }final 임시 변수에 복사',
    'intention.name.make.variable.final': '{1, choice, 0#\'\'{0}\'\'|1#변수}을(를) final로 만들기',
    'intention.name.transform.variables.into.final.one.element.array': '{1, choice, 0#\'\'{0}\'\'|1#변수}을(를) 단일 요소 final 배열로 변환',
    'type.information.value': '값',
    'type.information.not.equal.to': '같지 않음',
    'type.information.range': '범위',
    'type.information.nullability': 'Null 허용 여부(Nullability)',
    'type.information.constraints': '제약 조건',
    'type.information.mutability': '가변성(Mutability)'
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

print(f'Updated {bundle_name} (Keys 81-120)')
