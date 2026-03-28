import json
with open('missing_translations/missing_keys_korean.json', 'r', encoding='utf-8') as f:
    ko_data = json.load(f)

translations = {
  "record.component.cstyle.declaration": "레코드 구성요소에는 C 스타일 배열 선언이 허용되지 않습니다",
  "record.component.restricted.name": "잘못된 레코드 구성요소 이름 ''{0}''",
  "record.instance.initializer": "레코드에는 인스턴스 이니셜라이저가 허용되지 않습니다",
  "record.instance.field": "레코드에는 인스턴스 필드가 허용되지 않습니다",
  "record.accessor.wrong.return.type": "구성요소 접근자의 반환 유형이 잘못되었습니다. 필요: ''{0}'', 발견: ''{1}''",
  "record.canonical.constructor.wrong.parameter.type": "레코드 구성요소 ''{0}''의 매개변수 유형이 잘못되었습니다. 필요: ''{1}'', 발견: ''{2}''",
  "record.canonical.constructor.wrong.parameter.name": "표준(canonical) 생성자 매개변수 이름은 레코드 구성요소 이름과 일치해야 합니다. 필요: ''{0}'', 발견: ''{1}''",
  "record.constructor.call.in.canonical": "표준(canonical) 생성자는 다른 생성자에게 위임할 수 없습니다",
  "record.no.constructor.call.in.non.canonical": "비표준(non-canonical) 레코드 생성자는 다른 생성자에게 위임해야 합니다",
  "record.special.method.type.parameters": "{0}에는 유형 매개변수를 가질 수 없습니다",
  "record.special.method.non.public": "{0}은(는) ''public''이어야 합니다",
  "record.special.method.stronger.access": "{0} 액세스 수준은 레코드 접근 제한 수준(''{1}'')보다 더 제한적일 수 없습니다",
  "record.special.method.throws": "{0}은(는) 발생하는 예외를 선언할 수 없습니다",
  "record.canonical.constructor": "표준(canonical) 생성자",
  "record.compact.constructor": "압축(compact) 생성자",
  "record.accessor": "레코드 구성요소 접근자",
  "record.component.not.initialized": "레코드 구성요소 ''{0}''이(가) 표준(canonical) 생성자에서 초기화되지 않았을 수 있습니다",
  "compact.constructor.in.regular.class": "매개변수 목록이 필요합니다",
  "record.compact.constructor.return": "압축(compact) 생성자에서는 'return' 구문이 허용되지 않습니다",
  "record.permits": "레코드에는 permits 절이 허용되지 않습니다",
  "insufficient.language.level": "{0}은(는) 언어 수준 ''{1}''에서 지원되지 않습니다",
  "cannot.select.from.a.type.parameter": "유형 매개변수에서 선택할 수 없습니다",
  "method.reference.expression.is.not.expected": "여기는 메서드 참조 표현식이 올 자리가 아닙니다",
  "not.a.functional.interface": "{0}은(는) 함수형 인터페이스가 아닙니다",
  "cannot.find.class": "{0} 클래스를 찾을 수 없습니다",
  "cannot.infer.functional.interface.type": "함수형 인터페이스 유형을 추론할 수 없습니다",
  "lambda.expression.not.expected": "여기는 람다 표현식이 올 자리가 아닙니다",
  "lambda.parameters.consistency.message": "람다 표현식에서 'var'과 명시적으로 입력된 매개변수를 섞어서 쓸 수 없습니다",
  "target.method.is.generic": "대상 메서드가 제네릭입니다",
  "multiple.non.overriding.abstract.methods.found.in.0": "{0}에서 오버라이딩되지 않은 여러 추상 메서드를 발견했습니다"
}

ko_error_bundle = next((x for x in ko_data['new_files'] if x['filename'] == 'JavaErrorBundle.properties'), None)
ko_error_bundle['keys'].update(translations)
ko_error_bundle['key_count'] = len(ko_error_bundle['keys'])

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(ko_data, f, ensure_ascii=False, indent=2)

print("Updated keys.")
