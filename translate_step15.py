import json
with open('missing_translations/missing_keys_korean.json', 'r', encoding='utf-8') as f:
    ko_data = json.load(f)

translations = {
  "expected.comma.or.semicolon": "',' 또는 ';'가 필요합니다",
  "expected.dot": "'.'가 필요합니다",
  "expected.eq": "'='가 필요합니다",
  "expected.expression": "표현식이 필요합니다",
  "expected.case.label.element": "표현식, 패턴, 'default' 또는 'null'이 필요합니다",
  "expected.template.fragment": "템플릿 프래그먼트(fragment)가 필요합니다",
  "expected.gt": "'>'가 필요합니다.",
  "expected.gt.or.comma": "'>' 또는 ','가 필요합니다",
  "expected.identifier": "식별자가 필요합니다",
  "expected.identifier.or.type": "식별자 또는 타입이 필요합니다",
  "expected.lbrace": "'{'가 필요합니다",
  "expected.lbrace.or.semicolon": "'{' 또는 ';'가 필요합니다",
  "expected.lbracket": "'['가 필요합니다",
  "expected.lparen": "'('가 필요합니다",
  "expected.lparen.or.lbracket": "'(' 또는 '['가 필요합니다",
  "expected.lt.or.lparen": "'<' 또는 '('가 필요합니다",
  "expected.module.declaration": "모듈 선언이 필요합니다",
  "expected.module.statement": "모듈 지시문(directive)이 필요합니다",
  "expected.package.reference": "패키지 참조가 필요합니다",
  "expected.parameter": "매개변수가 필요합니다",
  "expected.rbrace": "'}'가 필요합니다",
  "expected.rbracket": "']'가 필요합니다",
  "expected.resource": "리소스 정의가 필요합니다",
  "expected.rparen": "')'가 필요합니다",
  "expected.semicolon": "';'가 필요합니다",
  "expected.statement": "구문(Statement)이 필요합니다",
  "expected.string": "문자열 리터럴이 필요합니다",
  "expected.switch.label": "'case', 'default' 또는 '}'가 필요합니다",
  "expected.switch.rule": "표현식, 블록, 또는 throw 구문이 필요합니다",
  "expected.type": "타입이 필요합니다",
  "expected.type.parameter": "타입 매개변수가 필요합니다",
  "expected.value": "값이 필요합니다",
  "expected.while": "'while'이 필요합니다",
  "expected.with": "'with'가 필요합니다",
  "expected.pattern": "패턴이 필요합니다",
  "filetype.class.description": "Java 클래스",
  "filetype.class.display.name": "Java 클래스",
  "filetype.java.description": "Java",
  "filetype.jshell.description": "JShell 스니펫",
  "finally.without.try": "'try' 없는 'finally'"
}

ko_error_bundle = next((x for x in ko_data['new_files'] if x['filename'] == 'JavaPsiBundle.properties'), None)
ko_error_bundle['keys'].update(translations)
ko_error_bundle['key_count'] = len(ko_error_bundle['keys'])

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(ko_data, f, ensure_ascii=False, indent=2)

print("Updated JavaPsiBundle.properties part 4")