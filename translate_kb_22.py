import json

ko_dict = {
  "0.interface.1": "{0} 인터페이스 ''{1}''",
  "lift.assignment.out.of.try.expression": "'try' 표현식 밖으로 할당 추출",
  "make.class.an.annotation.class": "클래스를 주석 클래스로 만들기",
  "make.0.an.annotation.class": "''{0}''을(를) 주석 클래스로 만들기",
  "make.constructor.parameter.a.property.0": "생성자 매개변수를 속성으로 만들기{0}",
  "in.class.0": "\\ ''{0}'' 클래스에서",
  "add.an.opt.in.requirement.marker.compiler.argument": "옵트인 요구 사항 마커 컴파일러 인수 추가",
  "make.0.in.1.open": "{1}의 ''{0}''을(를) open으로 만들기",
  "add.modifier": "한정자 추가",
  "make.private.and.0.1": "비공개로 만들고 ''{1}''을(를) {0}합니다.",
  "text.overrides": "재정의",
  "text.implements": "구현",
  "make.type.parameter.reified.and.function.inline": "유형 매개변수를 reified로, 함수를 inline으로 만들기",
  "change.all.usages.of.0.in.this.file.to.1": "이 파일에서 ''{0}''의 모든 사용 항목을 ''{1}''(으)로 변경",
  "change.all.usages.of.0.in.this.file.to.a.kotlin.class": "이 파일에서 ''{0}''의 모든 사용 항목을 Kotlin 클래스로 변경",
  "change.to.kotlin.class": "Kotlin 클래스로 변경",
  "choose.an.appropriate.kotlin.class": "적절한 Kotlin 클래스 선택",
  "add.empty.brackets.after.primary.constructor": "기본 생성자 뒤에 빈 대괄호 추가",
  "add.constructor.keyword": "'constructor' 키워드 추가",
  "move.annotation.to.receiver.type": "주석을 수신자 유형으로 이동",
  "move.type.parameter.constraint.to.where.clause": "유형 매개변수 제약 조건을 'where' 절로 이동",
  "move.else.branch.to.the.end": "else 분기를 끝으로 이동",
  "insert.number.conversion": "숫자 변환 삽입",
  "convert.expression.to.0": "표현식을 ''{0}''(으)로 변환",
  "remove.from.annotation.argument": "주석 인수에서 @ 제거",
  "remove.default.parameter.value": "기본 매개변수 값 제거",
  "remove.final.upper.bound": "final 상한 제거",
  "remove.function.body": "함수 본문 제거",
  "make.0.not.1": "{0}을(를) {1}이(가) 아니게 만들기",
  "remove.modifier.fix": "''{0}''을(를) {1}이(가) 아니게 만들기",
  "remove.modifier.fix.family": "{0}이(가) 아니게 만들기",
  "remove.0.modifier": "''{0}'' 한정자 제거",
  "remove.modifier": "한정자 제거",
  "remove.identifier.from.anonymous.function": "익명 함수에서 식별자 제거",
  "remove.parameter.name": "매개변수 이름 제거",
  "remove.constructor.call": "생성자 호출 제거",
  "make.not.nullable": "null 입력 불가능으로 만들기",
  "remove.useless": "유용한 '?' 제거",
  "remove.redundant": "중복 '?' 제거",
  "remove.0.from.property": "속성에서 {0} 제거",
  "remove.parts.from.property": "속성에서 부분 제거",
  "text.initializer": "초기화자",
  "text.setter": "setter",
  "text.getter": "getter",
  "remove.element": "요소 제거",
  "for.0": "''{0}''의 경우",
  "remove.conflicting.import.0": "충돌하는 가져오기 {0} 제거",
  "remove.type.parameters": "유형 매개변수 제거",
  "remove.type.arguments": "유형 인수 제거",
  "remove.star": "'*' 제거"
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

print(f"Updated {filename} (Keys 941-990)")

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
