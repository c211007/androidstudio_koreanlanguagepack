import json

ko_dict = {
  "highlighter.descriptor.text.annotation.attribute.name": "주석//주석 속성 이름",
  "highlighter.descriptor.text.arrow": "중괄호 및 연산자//화살표",
  "highlighter.descriptor.text.builtin.annotation": "키워드//제어자",
  "highlighter.descriptor.text.builtin.keyword.val": "키워드//'val'",
  "highlighter.descriptor.text.builtin.keyword.var": "키워드//'var'",
  "highlighter.descriptor.text.builtin.keyword": "키워드//키워드",
  "highlighter.descriptor.text.captured.variable": "속성 및 변수//클로저에서 캡처된 변수 및 값",
  "highlighter.descriptor.text.closure.braces": "중괄호 및 연산자//람다 표현식 중괄호 및 화살표",
  "highlighter.descriptor.text.colon": "중괄호 및 연산자//콜론",
  "highlighter.descriptor.text.constructor.call": "함수//생성자 호출",
  "highlighter.descriptor.text.double.colon": "중괄호 및 연산자//이중 콜론",
  "highlighter.descriptor.text.dynamic.fun.call": "함수//동적 함수 호출",
  "highlighter.descriptor.text.dynamic.property": "속성 및 변수//동적 속성",
  "highlighter.descriptor.text.enumEntry": "클래스 및 인터페이스//열거형(Enum) 항목",
  "highlighter.descriptor.text.exclexcl": "중괄호 및 연산자//Null이 아닌 어설션",
  "highlighter.descriptor.text.extension.fun.call": "함수//확장 함수 호출",
  "highlighter.descriptor.text.extension.property": "속성 및 변수//확장 속성",
  "highlighter.descriptor.text.field": "속성 및 변수//백킹 필드 변수",
  "highlighter.descriptor.text.fun.call": "함수//함수 호출",
  "highlighter.descriptor.text.fun": "함수//함수 선언",
  "highlighter.descriptor.text.instance.property.custom.property.declaration": "속성 및 변수//사용자 지정 속성 선언이 있는 인스턴스 속성",
  "highlighter.descriptor.text.instance.property": "속성 및 변수//인스턴스 속성",
  "highlighter.descriptor.text.it": "매개변수//람다 표현식 기본 매개변수",
  "highlighter.descriptor.text.kdoc.comment": "설명//KDoc//KDoc 설명",
  "highlighter.descriptor.text.kdoc.tag": "설명//KDoc//KDoc 태그",
  "highlighter.descriptor.text.kdoc.value": "설명//KDoc//KDoc 태그의 링크",
  "highlighter.descriptor.text.label": "레이블",
  "highlighter.descriptor.text.local.variable": "속성 및 변수//지역 변수 또는 값",
  "highlighter.descriptor.text.named.argument": "명명된 인수",
  "highlighter.descriptor.text.object": "클래스 및 인터페이스//객체",
  "highlighter.descriptor.text.enum": "클래스 및 인터페이스//열거형(Enum)",
  "highlighter.descriptor.text.package.fun.call": "함수//패키지 수준 함수 호출",
  "highlighter.descriptor.text.package.property.custom.property.declaration": "속성 및 변수//사용자 지정 속성 선언이 있는 패키지 수준 속성",
  "highlighter.descriptor.text.package.property": "속성 및 변수//패키지 수준 속성",
  "highlighter.descriptor.text.quest": "중괄호 및 연산자//유형 Null 허용 여부 마커",
  "highlighter.descriptor.text.safe.access": "중괄호 및 연산자//안전한 액세스 점",
  "highlighter.descriptor.text.smart.cast.receiver": "스마트 변환//스마트 변환된 암시적 수신자",
  "highlighter.descriptor.text.smart.cast": "스마트 변환//스마트 변환된 값",
  "highlighter.descriptor.text.smart.constant": "스마트 변환//스마트 상수",
  "highlighter.descriptor.text.string.escape": "문자열//문자열 및 템플릿 중괄호 이스케이프",
  "highlighter.descriptor.text.suspend.fun.call": "함수//일시 중단 함수 호출",
  "highlighter.descriptor.text.synthetic.extension.property": "속성 및 변수//합성 확장 속성",
  "highlighter.descriptor.text.typeAlias": "클래스 및 인터페이스//유형 별칭",
  "highlighter.descriptor.text.data.class": "클래스 및 인터페이스//데이터 클래스",
  "highlighter.descriptor.text.data.object": "클래스 및 인터페이스//데이터 객체",
  "highlighter.descriptor.text.var": "속성 및 변수//Var(변경 가능한 변수, 매개변수 또는 속성)",
  "highlighter.descriptor.text.variable.as.function.call": "속성 및 변수//함수 호출로서의 변수",
  "highlighter.descriptor.text.variable.as.function.like.call": "속성 및 변수//함수와 유사한 호출로서의 변수",
  "highlighter.message.suspend.function.call": "일시 중단 함수 호출",
  "highlighter.message.suspending.iteration": "반복 일시 중단"
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

print(f"Updated {filename} (Keys 491-540)")

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
