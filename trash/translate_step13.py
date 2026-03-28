import json
with open('missing_translations/missing_keys_korean.json', 'r', encoding='utf-8') as f:
    ko_data = json.load(f)

translations = {
  "element.variable": "변수",
  "element.throws.list": "throws 목록",
  "element.extends.list": "extends 목록",
  "element.type.arguments": "타입 인수",
  "element.type.semicolon": "세미콜론",
  "element.receiver.parameter": "수신자(receiver) 매개변수",
  "element.method.call": "메서드 호출",
  "feature.assertions": "어설션(Assertions)",
  "feature.enums": "열거형(Enums)",
  "feature.generics": "제네릭(Generics)",
  "feature.annotations": "애너테이션",
  "feature.override.interface": "인터페이스의 @Override",
  "feature.static.imports": "정적 가져오기",
  "feature.for.each": "For-each 루프",
  "feature.varargs": "가변 인수 메서드(Variable arity methods)",
  "feature.hex.fp.literals": "16진수 부동 소수점 리터럴",
  "feature.diamond.types": "다이아몬드 타입",
  "feature.multi.catch": "다중 catch",
  "feature.try.with.resources": "Try-with-resources",
  "feature.binary.literals": "2진수 리터럴",
  "feature.underscores.in.literals": "리터럴의 밑줄",
  "feature.string.switch": "'switch' 구문의 문자열",
  "feature.stream.and.optional.api": "Stream 및 Optional API",
  "feature.advanced.collection.api": "컬렉션의 람다 메서드",
  "feature.with.initial": "ThreadLocal.withInitial()",
  "feature.extension.methods": "확장(Extension) 메서드",
  "feature.method.references": "메서드 참조",
  "feature.lambda.expressions": "람다 표현식",
  "feature.type.annotations": "타입 애너테이션",
  "feature.type.receivers": "수신자(Receiver) 매개변수",
  "feature.intersections.in.casts": "형 변환에서의 교차(Intersection) 타입",
  "feature.static.interface.calls": "정적 인터페이스 메서드 호출",
  "feature.effectively.final": "사실상 final인 변수(Effectively final variables)",
  "feature.try.with.resources.refs": "리소스 참조",
  "feature.modules": "모듈",
  "feature.private.interface.methods": "프라이빗 인터페이스 메서드",
  "feature.collection.factories": "컬렉션 팩토리 메서드",
  "feature.lvti": "지역 변수 타입 추론",
  "feature.var.lambda.parameter": "람다 매개변수의 'var'",
  "feature.nestmates": "네스트(Nest) 기반 접근 제어"
}

ko_error_bundle = next((x for x in ko_data['new_files'] if x['filename'] == 'JavaPsiBundle.properties'), None)
ko_error_bundle['keys'].update(translations)
ko_error_bundle['key_count'] = len(ko_error_bundle['keys'])

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(ko_data, f, ensure_ascii=False, indent=2)

print("Updated JavaPsiBundle.properties part 2")