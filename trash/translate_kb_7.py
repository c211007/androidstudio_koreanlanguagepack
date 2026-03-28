import json

ko_dict = {
  "kdoc.section.title.returns": "반환",
  "kdoc.section.title.throws": "예외",
  "kdoc.section.title.author": "작성자",
  "kdoc.section.title.properties": "속성",
  "kdoc.section.title.constructor": "생성자",
  "kdoc.section.title.since": "Since",
  "kdoc.section.title.suppress": "표시 안 함",
  "kdoc.section.title.samples": "샘플",
  "kdoc.section.title.see.also": "참고",
  "kdoc.comment.unresolved": "해결되지 않음",
  "livetemplate.description.main": "main() 함수",
  "livetemplate.description.maina": "main(args) 함수",
  "livetemplate.description.soutp": "함수 매개변수 이름과 값을 System.out에 출력",
  "livetemplate.description.sout": "문자열을 System.out에 출력",
  "livetemplate.description.serr": "문자열을 System.err에 출력",
  "livetemplate.description.soutv": "값을 System.out에 출력",
  "livetemplate.description.iter": "반복 가능한 요소에 대해 반복(for-in 루프)",
  "livetemplate.description.ifn": "'if null' 표현식 삽입",
  "livetemplate.description.inn": "'if not null' 표현식 삽입",
  "livetemplate.description.void": "아무것도 반환하지 않는 함수",
  "livetemplate.description.fun0": "매개변수가 없는 함수",
  "livetemplate.description.fun1": "매개변수가 한 개인 함수",
  "livetemplate.description.fun2": "매개변수가 두 개인 함수",
  "livetemplate.description.interface": "인터페이스",
  "livetemplate.description.singleton": "싱글톤",
  "livetemplate.description.closure": "클로저(이름 없는 함수)",
  "livetemplate.description.anonymous": "익명 클래스",
  "livetemplate.description.exfun": "확장 함수",
  "livetemplate.description.exval": "읽기 전용 확장 속성",
  "livetemplate.description.exvar": "읽기/쓰기 확장 속성",
  "inlay.kotlin.references.types.hints": "유형의 인레이 힌트 표시",
  "inlay.kotlin.references.types.hints.hints.type.function.parameter": "함수 매개변수 유형에 대한 인레이 힌트 표시",
  "inlay.kotlin.references.types.hints.hints.type.function.return": "함수 반환 유형에 대한 인레이 힌트 표시",
  "inlay.kotlin.references.types.hints.hints.type.variable": "지역 변수 유형에 대한 인레이 힌트 표시",
  "inlay.kotlin.references.types.hints.hints.type.property": "속성 유형에 대한 인레이 힌트 표시",
  "inlay.kotlin.lambdas.hints": "람다의 인레이 힌트 표시",
  "inlay.kotlin.call.chains.hints": "호출 체인의 인레이 힌트 표시",
  "inlay.kotlin.lambdas.hints.hints.lambda.receivers.parameters": "암시적 수신자 및 매개변수의 인레이 힌트 표시",
  "inlay.kotlin.lambdas.hints.hints.lambda.return": "반환 표현식의 인레이 힌트 표시",
  "inlay.kotlin.values.hints": "값의 인레이 힌트 표시",
  "inlay.kotlin.values.hints.kotlin.values.ranges": "범위의 인레이 힌트 표시",
  "inlay.kotlin.value.ranges": "범위의 인레이 힌트 표시",
  "inlay.kotlin.value.kotlin.time": "kotlin.time 패키지 경고 인레이 힌트 표시",
  "hints.settings.parameters": "매개변수",
  "inlay.kotlin.parameters.hints": "함수 호출 위치에 매개변수 이름을 표시합니다.",
  "hints.settings.excluded.parameters": "제외된 매개변수 이름",
  "inlay.kotlin.parameters.hints.excluded": "제외된 매개변수 이름 표시",
  "hints.settings.compiled.parameters": "컴파일된 매개변수 이름",
  "inlay.kotlin.parameters.hints.compiled": "컴파일된 매개변수 이름 표시",
  "parameter.hints.old": "Kotlin: 매개변수의 인레이 힌트 표시"
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

print(f"Updated {filename} (Keys 341-390)")

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
