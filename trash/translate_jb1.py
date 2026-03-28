import json
import os

file_path = 'missing_translations/missing_keys_korean.json'
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

bundle_name = 'JavaBundle.properties'
translations = {
    'generate.equals.hashcode.comparison.table': '<html><table>\n  <tr><th><th>instanceof<th>getClass()\n  <tr><td>서브클래스의 인스턴스가 슈퍼클래스 인스턴스와 일치하도록 허용<td align=center>예<td align=center>아니요\n  <tr><td>다른 서브클래스의 인스턴스가 서로 동일하도록 허용<td align=center>예<td align=center>아니요\n  <tr><td>생성된 equals() 메서드를 재정의해도 규약이 손상되지 않음<td align=center>아니요<td align=center>예\n  <tr><td>추가 null 검사를 피함<td align=center>예<td align=center>아니요\n  <tr><td>리스코프\\\\&nbsp;치환\\\\&nbsp;원칙\\\\&nbsp;준수<td align=center>예<td align=center>아니요\n  </table></html>',
    'generate.equals.hashcode.accept.sublcasses.explanation': '<html><body>일반적으로 Object.equals()의 규약을 준수하지 않지만, Hibernate와 같이<br>\n 프록시 서브클래스를 생성하는 프레임워크에서 생성된 메서드가 올바르게 작동하려면<br>서브클래스를 허용하는 것이 필요할 수 있습니다.</body></html>',
    'generate.tostring.method.already.exists.dialog.message': '기존 {0} 메서드 바꾸기',
    'java.preview.features.legal.notice': '"{0}"에 대한 지원을 활성화하려면 베타 Java 사양의 법적 고지 약관에 동의해야 합니다.<br/><br/>\n  <b>Java Community Process(JCP)에 따라 개발된 초기 초안 사양의 구현은 테스트 및 평가 목적으로만 사용할 수 있으며 JCP의 어떠한 사양과도 호환되지 않습니다.</b>{1}',
    'java.preview.features.warning': '최신 IDE 버전에서는 Java Preview 기능에 대한 지원이 중단될 수 있습니다. Java {0}이(가) 릴리스되면 {1} (Preview) 언어 수준에 대한 지원이 중단될 수 있습니다.',
    'java.preview.features.unsupported': '이 프로젝트에서 사용된 Java 언어 수준 <b>{0} (Preview)</b>는 더 이상 지원되지 않습니다. \n  Preview 기능에 대한 코드 인사이트가 올바르게 작동하지 않을 수 있습니다.<br>\n  더 새로운 Java 버전으로 마이그레이션하거나 Preview 기능 사용을 중지할 것을 강력히 권장합니다.',
    'inlay.parameters.java.method.name.contains.parameter.name': '접근자 메서드처럼 메서드 이름에서 예상되는 인자가 명확할 때 단일 인자를 취하는 메서드.',
    'inlay.parameters.java.multiple.params.same.type': '동일한 타입의 리터럴이 아닌 인자가 두 개 이상인 메서드 호출.',
    'inlay.parameters.java.build.like.method': '작동 대상인 클래스의 인스턴스를 반환하는 메서드 (예: StringBuilder 체인 호출 또는 Java 8 Stream API의 중간 연산).',
    'inlay.parameters.java.simple.sequentially.numbered': '하나의 문자와 그 뒤에 이어지는 숫자로 구성된 이름의 여러 매개변수를 사용하는 메서드.',
    'inlay.parameters.java.enums': '매개변수가 있는 생성자를 사용하는 열거형 상수 선언.',
    'inlay.parameters.java.new.expr': '매개변수가 있는 생성자 호출.',
    'inlay.parameters.java.clear.expression.type': '복잡한 표현식을 인자로 사용하는 메서드 호출 (예: 삼항 연산자 또는 Java 13의 switch 문).',
    'inlay.MethodChainsInlayProvider.description': '호출 체인에서의 메서드 반환 타입.',
    'inlay.annotation.hints.inferred.annotations': 'IntelliJ IDEA가 라이브러리 및 프로젝트 코드를 검사하여 생성하는 어노테이션입니다. 이 어노테이션은 코드 규약을 이해하고 정적 분석 기능을 향상시키는 데 도움이 됩니다. 다음을 포함합니다: <br> @Contract <br> @Nullable <br> @NotNull <br> @Unmodifiable <br>@UnmodifiableView <br><br><a href="https://www.jetbrains.com/help/idea/inferring-nullity.html#inferred-annotations">문서</a>',
    'inlay.annotation.hints.external.annotations': '소스 코드 외부에 저장된 어노테이션입니다.<br>이 어노테이션은 어노테이션이 필요하지만 소스 코드에 추가할 수 없는 경우(예를 들어, 라이브러리 코드로 작업하는 경우)에 유용합니다.<br><br><a href="https://www.jetbrains.com/help/idea/external-annotations.html">문서</a>',
    'generate.type.use.before.type.description': '<html>TYPE_USE 대상이 있는 어노테이션은 제어자 뒤, 그리고 타입<br>바로 앞에 배치됩니다. 비활성화하면 제어자 앞에 배치됩니다.</html>',
    'slice.filter.parse.error.null.filter.not.applicable.for.primitive.type': "''null'' 필터는 원시 타입 {0}에 적용할 수 없습니다",
    'slice.filter.parse.error.not.null.filter.not.applicable.for.primitive.type': "''!null'' 필터는 원시 타입 {0}에 적용할 수 없습니다",
    'slice.filter.parse.error.enum.constant.not.found': '열거형 상수를 찾을 수 없습니다: {0}',
    'slice.filter.parse.error.incorrect.expression': '올바르지 않은 표현식: {0}',
    'slice.filter.parse.error.incorrect.constant.type': '올바르지 않은 상수 타입 (필요: {0})',
    'slice.filter.parse.error.expression.must.evaluate.to.constant': '표현식은 상수로 평가되어야 합니다: {0}',
    'slice.filter.parse.error.incorrect.constant.expected.number': '올바르지 않은 상수 (예상되는 숫자): {0}',
    'action.find.similar.stack.call.diverged': "줄 번호가 일치하지 않을 가능성이 있습니다. ''{0}.{1}()'' 내에서 현재 위치를 찾아보세요",
    'action.find.similar.stack.call.methods': "''{0}.{1}()''와(과) 유사한 메서드",
    'action.find.similar.stack.call.similar.calls': "''{0}.{1}()'' 내의 가능한 위치",
    'action.find.similar.stack.call.methods.not.found': "''{0}.{1}()''와(과) 유사한 메서드가 없음",
    'action.find.similar.stack.call.location.not.found': "''{0}.{1}()'' 내에 유사한 위치가 없음",
    'action.dfa.from.stacktrace.text': "''{0}''이(가) {1}일 수 있는 이유 찾기",
    'slice.usage.message.assertion.violated': '(단언(assertion) 위반됨!)',
    'slice.usage.message.in.file.stopped.here': '({0} 파일에서 - 여기서 중지됨)',
    'slice.usage.message.tracking.container.contents': "(컨테이너 ''{0}{1}'' 내용 추적 중)",
    'slice.usage.message.location': '{0}에서',
    'intention.name.move.into.if.branches': "'if' 문 분기로 위로 이동",
    'intention.name.collapse.into.loop': '루프로 접기',
    'intention.family.name.make.sealed': '클래스 봉인(Seal)',
    'intention.error.make.sealed.class.is.used.in.functional.expression': '클래스가 함수형 표현식에 사용됩니다',
    'intention.error.make.sealed.class.has.anonymous.or.local.inheritors': '일부 상속자가 익명이거나 로컬입니다',
    'intention.error.make.sealed.class.different.packages': '모듈에 이름이 없으며 일부 상속자가 다른 패키지에 있습니다'
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

print(f'Updated {bundle_name} (Keys 1-40)')