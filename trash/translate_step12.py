import json
with open('missing_translations/missing_keys_korean.json', 'r', encoding='utf-8') as f:
    ko_data = json.load(f)

translations = {
  "0.is.not.an.identifier": "''{0}''은(는) 식별자가 아닙니다.",
  "annotation.name.is.missing": "애너테이션 속성은 'name=value' 형식이어야 합니다",
  "implicit.class.context.display": "암시적 클래스",
  "anonymous.class.context.display": "{0}의 익명 클래스",
  "anonymous.class.derived.display": "{0}에서 파생된 익명 클래스",
  "aux.context.display": "{0}의 보조",
  "class.file.version": "버전 {0}",
  "bound.not.expected": "예기치 않은 경계(bound)",
  "catch.without.try": "'try' 없는 'catch'",
  "class.context.display": "{1}의 {0}",
  "class.literal.expected": ".class가 필요합니다",
  "context.type.java.comment": "주석",
  "context.type.string": "문자열",
  "default.language.level.description": "SDK 기본값",
  "element.abstract_method": "추상 메서드",
  "element.annotation": "애너테이션",
  "element.anonymous_class": "익명 클래스",
  "element.class": "클래스",
  "element.type.parameter": "타입 매개변수",
  "element.constant": "상수 필드",
  "element.constructor": "생성자",
  "element.enum": "열거형(enum)",
  "element.enum_constant": "열거형 상수(enum constant)",
  "element.expression": "표현식",
  "element.field": "필드",
  "element.initializer": "초기화자(initializer)",
  "element.interface": "인터페이스",
  "element.label": "레이블",
  "element.local_variable": "지역 변수",
  "element.method": "메서드",
  "element.module": "모듈",
  "element.package": "패키지",
  "element.package.statement": "패키지 문장",
  "element.parameter": "매개변수",
  "element.pattern_variable": "패턴 변수",
  "element.record": "레코드(record)",
  "element.record_component": "레코드 컴포넌트",
  "element.snippet_body": "스니펫 본문",
  "element.statement": "구문(statement)",
  "element.unknown": "요소"
}

ko_error_bundle = next((x for x in ko_data['new_files'] if x['filename'] == 'JavaPsiBundle.properties'), None)
if not ko_error_bundle:
    ko_error_bundle = {'filename': 'JavaPsiBundle.properties', 'keys': {}, 'key_count': 0}
    ko_data['new_files'].append(ko_error_bundle)
ko_error_bundle['keys'].update(translations)
ko_error_bundle['key_count'] = len(ko_error_bundle['keys'])

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(ko_data, f, ensure_ascii=False, indent=2)

print("Updated JavaPsiBundle.properties part 1")