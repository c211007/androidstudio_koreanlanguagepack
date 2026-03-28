import json

ko_dict = {
  "text.extension.function.0": "확장 {0,choice,1#함수|2#함수}",
  "text.infix.function": "중위 함수",
  "text.infix.function.0": "중위 {0,choice,1#함수|2#함수}",
  "text.infix.extension.function": "중위 확장 함수",
  "text.infix.extension.function.0": "중위 확장 {0,choice,1#함수|2#함수}",
  "text.extension.property": "확장 속성",
  "text.extension.property.0": "확장 {0,choice,1#속성|2#속성}",
  "text.operator.0": "{0,choice,1#연산자|2#연산자}",
  "text.object": "객체",
  "text.object.0": "{0,choice,1#객체|2#객체}",
  "text.interface": "인터페이스",
  "text.enum.constant": "enum 상수",
  "text.enum": "enum",
  "text.annotation": "주석",
  "create.0.1": "{0} ''{1}'' 만들기",
  "choose.class.container": "클래스 컨테이너 선택",
  "create.0": "{0} 만들기",
  "create.package.0": "패키지 ''{0}'' 만들기",
  "text.type.parameter": "유형 {0, choice, 0#매개변수|2#매개변수}",
  "create.0.in.1": "{1}에서 {0} 만들기",
  "searching.0": "{0} 검색 중\\u2026",
  "create.property.0.as.constructor.parameter": "생성자 매개변수로 속성 ''{0}'' 만들기",
  "create.parameter.0": "매개변수 ''{0}'' 만들기",
  "quickfix.add.property.familyName": "속성 추가",
  "quickFix.add.property.text": "''{3}''에 ''{0}{1}'' 속성 ''{2}'' 추가",
  "add.method": "메서드 추가",
  "add.0.constructor.to.1": "''{1}''에 {0} 생성자 추가",
  "text.secondary": "보조",
  "text.primary": "주",
  "add.method.0.to.1": "''{1}''에 메서드 ''{0}'' 추가",
  "create.actual": "actual 만들기",
  "create.actual.in.0": "''{0}''에서 actual 만들기",
  "create.actuals": "누락된 actual 만들기\\u2026",
  "choose.actual.module": "actual 모듈 선택",
  "create.actual.0.for.module.1.2": "{1} 모듈({2})을 위한 actual {0} 만들기",
  "create.expected.0.in.common.module.1": "공통 모듈 {1}에서 expected {0} 만들기",
  "repair.actual.members": "actual 멤버 복구",
  "these.declarations.cannot.be.transformed": "다음 선언은 변환할 수 없습니다:",
  "unknown.types.title": "알 수 없는 유형",
  "choose.actual.members.title": "actual 멤버 선택",
  "text.annotation.class": "주석 클래스",
  "text.enum.class": "enum 클래스",
  "text.class": "클래스",
  "text.class.0": "{0,choice,1#클래스|2#클래스}",
  "text.enum.entry.0": "{0,choice,1#enum 항목|2#enum 항목}",
  "type.0.1.is.not.accessible.from.target.module": "대상 모듈에서 {0, choice, 0#유형|2#유형} {1}에 접근할 수 없습니다.",
  "the.function.declaration.shouldn.t.have.a.default.implementation": "함수 선언에는 기본 구현이 없어야 합니다.",
  "some.types.are.not.accessible.from.0.1": "{0}에서 일부 유형에 접근할 수 없습니다:\\n{1}",
  "the.declaration.has.0.modifier": "선언에 ''{0}'' 한정자가 있습니다.",
  "inaccessible.declaration": "접근할 수 없는 선언"
}

with open('missing_translations/missing_keys_korean.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

filename = "KotlinBundle.properties"
found = False
for file_entry in data.get('new_files', []):
    if file_entry['filename'] == filename:
        file_entry['keys'].update(ko_dict)
        found = True
        break
if not found:
    data.setdefault('new_files', []).append({"filename": filename, "keys": ko_dict})

print(f"Updated {filename} (Keys 841-890)")

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
