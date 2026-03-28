import json
with open('missing_translations/missing_keys_korean.json', 'r', encoding='utf-8') as f:
    ko_data = json.load(f)

translations = {
  "node.annotation.tooltip": "애너테이션",
  "node.anonymous.class.tooltip": "익명 클래스",
  "node.class.tooltip": "클래스",
  "node.enum.tooltip": "열거형(Enum)",
  "node.exception.tooltip": "예외(Exception)",
  "node.field.tooltip": "필드",
  "node.final.flag.tooltip": "Final",
  "node.interface.tooltip": "인터페이스",
  "node.junit.test.tooltip": "JUnit 테스트",
  "node.method.tooltip": "메서드",
  "node.record.tooltip": "레코드(Record)",
  "node.runnable.class.tooltip": "실행 가능한(Runnable) 클래스",
  "node.static.flag.tooltip": "정적(Static)",
  "psi.error.attempt.to.edit.class.file": "''{0}'' 파일의 컴파일된 요소를 수정할 수 없습니다",
  "task.background.title.maven": "Maven",
  "unexpected.identifier": "예기치 않은 식별자",
  "unexpected.token": "예기치 않은 토큰",
  "unexpected.tokens": "예기치 않은 토큰",
  "error.message.wildcard.not.expected": "예기치 않은 와일드카드",
  "bad.return.type.in.method.reference": "메서드 참조 내 잘못된 반환 타입: {0}을(를) {1}(으)로 변환할 수 없습니다",
  "bad.return.type.in.lambda.expression": "람다 표현식 내 잘못된 반환 타입: {0}을(를) {1}(으)로 변환할 수 없습니다",
  "bad.return.type.in.lambda.expression1": "람다 표현식 내 잘못된 반환 타입: {0}을(를) void로 변환할 수 없습니다",
  "missing.return.value.lambda": "반환 값 누락",
  "unexpected.return.value": "예기치 않은 반환 값",
  "lambda.body.must.be.a.statement.expression": "람다 본문은 구문 표현식(statement expression)이어야 합니다",
  "diamond.error.explicit.type.parameters.for.constructor": "생성자의 명시적 타입 매개변수와 다이아몬드를 함께 사용할 수 없습니다",
  "diamond.error.cannot.infer.arguments": "인수를 추론할 수 없습니다",
  "diamond.error.cannot.infer.arguments.unable.to.resolve.constructor": "인수를 추론할 수 없습니다(생성자를 확인할 수 없음)",
  "diamond.error.anonymous.inner.classes": "익명 내부 클래스와 '<>'를 함께 사용할 수 없습니다",
  "diamond.error.anonymous.inner.classes.non.private": "상위 타입의 메서드를 재정의(override)하거나 구현하지 않는 비공개(non-private) 메서드로 인해 '<>'를 사용할 수 없습니다",
  "diamond.error.cannot.infer.type.arguments": "{0}에 대한 타입 인수를 추론할 수 없습니다",
  "error.incompatible.type.no.type.variable": "타입 매개변수의 인스턴스가 존재하지 않아 {0}",
  "error.incompatible.type.no.type.variable.0": "타입 매개변수의 인스턴스 {0}이(가) 존재하지 않아 {1}",
  "type.conforms.to.constraint": "{0}이(가) {1}을(를) 준수합니다",
  "type.can.be.converted": "{0}은(는) {1}(으)로 변환할 수 있습니다",
  "conflicting.conjuncts": "{0} 및 {1}",
  "error.type.parameter.has.incompatible.upper.bounds": "타입 매개변수 {0}에 호환되지 않는 상한(upper bounds)이 있습니다: {1}",
  "error.incompatible.upper.bounds": "호환되지 않는 상한(upper bounds): {0}",
  "error.inference.variable.has.incompatible.bounds": "추론 변수 {0}에 호환되지 않는 경계가 있습니다:\\n {1}: {2}\\n{3}: {4}",
  "error.incompatible.type": "{0}이(가) {1}와(과) 호환되지 않습니다",
  "error.incompatible.type.not.a.functional.interface": "{0}은(는) 함수형 인터페이스가 아닙니다",
  "error.incompatible.type.no.valid.function.type.found": "{0}에 대해 유효한 함수 타입을 찾을 수 없습니다",
  "error.incompatible.type.parameter.type.is.not.yet.inferred": "매개변수 타입이 아직 추론되지 않았습니다: {0}",
  "error.incompatible.type.return.type.is.not.yet.inferred": "반환 타입이 아직 추론되지 않았습니다: {0}",
  "error.incompatible.type.unhandled.exception": "처리되지 않은 예외: {0}",
  "error.incompatible.type.failed.to.resolve.argument": "인수를 확인하지 못했습니다",
  "error.incompatible.type.incompatible.parameter.types.in.lambda": "람다 매개변수 개수가 잘못되었습니다: {0}개가 필요하지만 {1}개가 발견되었습니다",
  "error.incompatible.type.incompatible.types.expected.void.lambda": "호환되지 않는 타입: void가 필요하지만 람다 본문이 구문 표현식(statement expression)이나 void 호환 블록이 아닙니다",
  "error.incompatible.type.expected.value.lambda": "호환되지 않는 타입: void가 아닌 값이 필요하지만 람다 본문이 값 호환 블록이 아닙니다",
  "error.incompatible.type.bad.lambda.return.type": "람다 표현식 내 잘못된 반환 타입: {0}을(를) {1}(으)로 변환할 수 없습니다",
  "error.incompatible.type.incompatible.parameter.types.in.method.reference": "메서드 참조 표현식의 매개변수 타입이 호환되지 않습니다",
  "error.incompatible.type.incompatible.types.expected.not.void.got.void.method.reference": "호환되지 않는 타입: void가 아닌 값이 필요하지만 메서드 참조에 대한 컴파일 타임 선언의 반환 타입이 void입니다",
  "error.incompatible.type.declaration.for.the.method.reference.not.found": "메서드 참조에 대한 컴파일 타임 선언을 찾을 수 없습니다",
  "error.incompatible.type.expected.non.void.got.void.method.reference": "호환되지 않는 타입: void가 아닌 값이 필요하지만 메서드 참조에 대한 컴파일 타임 선언의 반환 타입이 void입니다",
  "error.incompatible.type.not.convertible": "호환되지 않는 타입: {0}을(를) {1}(으)로 변환할 수 없습니다",
  "error.incompatible.type.incompatible.equality.constraint": "호환되지 않는 동등성(equality) 제약조건: {0} 및 {1}",
  "list.item.no.module": "<모듈 없음>",
  "element.kind.and.name": "{0} {1}",
  "command.name.insert.block.statement": "블록 구문 삽입"
}

ko_error_bundle = next((x for x in ko_data['new_files'] if x['filename'] == 'JavaPsiBundle.properties'), None)
ko_error_bundle['keys'].update(translations)
ko_error_bundle['key_count'] = len(ko_error_bundle['keys'])

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(ko_data, f, ensure_ascii=False, indent=2)

print("Updated JavaPsiBundle.properties part 6")