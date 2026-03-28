import json
with open('missing_translations/missing_keys_korean.json', 'r', encoding='utf-8') as f:
    ko_data = json.load(f)

translations = {
  "feature.text.blocks": "텍스트 블록 리터럴",
  "feature.text.block.escape.sequences": "'\\\\s' 이스케이프 시퀀스",
  "feature.enhanced.switch": "향상된 'switch' 블록",
  "feature.switch.expressions": "'switch' 표현식",
  "feature.serial.annotation": "@Serial 애너테이션",
  "feature.records": "레코드(Records)",
  "feature.patterns.instanceof": "'instanceof' 패턴",
  "feature.sealed.classes": "Sealed(봉인된) 클래스",
  "feature.strictfp": "항상 엄격한(Always-strict) 부동 소수점 시맨틱",
  "feature.no.this.capture": "내부 클래스가 'this'를 캡처하지 않음",
  "feature.local.interfaces": "지역 인터페이스",
  "feature.local.enums": "지역 열거형(enums)",
  "feature.inner.statics": "내부 클래스의 정적 선언",
  "feature.patterns.in.switch": "switch 내 패턴",
  "feature.javadoc.snippets": "Javadoc의 @snippet",
  "feature.pattern.guard.and.record.patterns": "패턴 가드 및 레코드 패턴",
  "feature.record.patterns.in.for.each": "for-each 루프 내 레코드 패턴",
  "feature.enum.qualified.name.in.switch": "switch 상수 내 정규화된 열거형",
  "feature.string.templates": "문자열 템플릿",
  "feature.unnamed.vars": "이름 없는 패턴 및 변수",
  "feature.implicit.classes": "암시적으로 선언된 클래스",
  "feature.scoped.values": "범위가 지정된 값(Scoped Values)",
  "feature.structured.concurrency": "구조화된 동시성(Structured Concurrency)",
  "feature.sequenced.collections": "순서가 지정된 컬렉션(Sequenced Collections)",
  "feature.classfile.api": "클래스 파일(ClassFile) API",
  "feature.stream.gatherers": "스트림 게더러(Stream Gatherers)",
  "feature.foreign.functions": "외부 함수 및 메모리 API(Foreign Function & Memory API)",
  "feature.virtual.threads": "가상 스레드(Virtual Threads)",
  "feature.statements.before.super": "super() 이전의 구문",
  "else.without.if": "'if' 없는 'else'",
  "enum.constant.context": "''{1}'' 내의 열거형 상수 ''{0}''",
  "expected.array.initializer": "배열 초기화자가 필요합니다",
  "expected.boolean.expression": "Boolean(부울) 표현식이 필요합니다",
  "expected.catch.or.finally": "'catch' 또는 'finally'가 필요합니다",
  "expected.class.or.interface": "'class' 또는 'interface'가 필요합니다",
  "expected.class.reference": "클래스 참조가 필요합니다",
  "expected.colon": "':'가 필요합니다",
  "expected.colon.or.arrow": "':' 또는 '->'가 필요합니다",
  "expected.comma": "','가 필요합니다",
  "expected.comma.or.rparen": "',' 또는 ')'가 필요합니다"
}

ko_error_bundle = next((x for x in ko_data['new_files'] if x['filename'] == 'JavaPsiBundle.properties'), None)
ko_error_bundle['keys'].update(translations)
ko_error_bundle['key_count'] = len(ko_error_bundle['keys'])

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(ko_data, f, ensure_ascii=False, indent=2)

print("Updated JavaPsiBundle.properties part 3")