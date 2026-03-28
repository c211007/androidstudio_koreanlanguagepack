import json

ko_dict = {
  "kotlin.references.types.hints": "Kotlin: 유형의 인레이 힌트 표시",
  "kotlin.references.types.hints.hints.type.function.parameter": "Kotlin: 함수 매개변수 유형에 대한 인레이 힌트 표시",
  "kotlin.references.types.hints.hints.type.function.return": "Kotlin: 함수 반환 유형에 대한 인레이 힌트 표시",
  "kotlin.references.types.hints.hints.type.variable": "Kotlin: 지역 변수 유형에 대한 인레이 힌트 표시",
  "kotlin.references.types.hints.hints.type.property": "Kotlin: 속성 유형에 대한 인레이 힌트 표시",
  "kotlin.lambdas.hints": "Kotlin: 람다의 인레이 힌트 표시",
  "kotlin.call.chains.hints": "Kotlin: 호출 체인의 인레이 힌트 표시",
  "kotlin.lambdas.hints.hints.lambda.receivers.parameters": "Kotlin: 암시적 수신자 및 매개변수의 인레이 힌트 표시",
  "kotlin.lambdas.hints.hints.lambda.return": "Kotlin: 반환 표현식의 인레이 힌트 표시",
  "kotlin.values.hints": "값의 인레이 힌트 표시",
  "kotlin.values.hints.kotlin.values.ranges": "Kotlin: 범위의 인레이 힌트 표시",
  "microservices.url.path.inlay.hints": "Kotlin: URL 경로에 대한 인레이 힌트 표시",
  "vcs.code.author": "Kotlin: 코드 작성자와 함께 인레이 힌트 표시",
  "ignore.imports.and.formatting": "가져오기 및 포맷 무시",
  "spring.secured.urls.inlay.hints": "Kotlin: 보안 Spring URL에 대한 인레이 힌트 표시",
  "hints.settings.common.items": "다음에 대한 힌트 표시:",
  "hints.settings.types": "유형",
  "hints.types": "유형 힌트",
  "hints.settings.types.property": "속성 유형",
  "hints.settings.types.variable": "지역 변수 유형",
  "hints.settings.types.return": "함수 반환 유형",
  "hints.settings.types.parameter": "함수 매개변수 유형",
  "hints.settings.values.ranges": "범위",
  "hints.settings.compiler.plugins.supertypes": "Kotlin 컴파일러 플러그인이 추가한 상위 유형",
  "hints.description.compiler.plugins.supertypes": "Kotlin 컴파일러 플러그인에 의해 생성된 상위 유형이 포함된 힌트를 제공합니다.",
  "hints.tooltip.compiler.plugins.supertypes": "Kotlin 컴파일러 플러그인에서 상위 유형 추가됨",
  "hints.settings.compiler.plugins.modality": "Kotlin 컴파일러 플러그인이 변경한 양식",
  "hints.description.compiler.plugins.modality": "Kotlin 컴파일러 플러그인에 의해 변경된 선언 양식이 포함된 힌트를 제공합니다.",
  "hints.tooltip.compiler.plugins.modality": "Kotlin 컴파일러 플러그인에 의해 양식이 ''{0}''에서 ''{1}''(으)로 변경됨",
  "hints.settings.compiler.plugins.declarations": "Kotlin 컴파일러 플러그인에서 생성된 선언",
  "inlay.kotlin.compiler.plugins.declarations.description": "Kotlin 컴파일러 플러그인에서 생성된 선언",
  "hints.settings.compiler.plugins.declarations.show.hidden.name": "숨겨진 선언 표시",
  "hints.settings.compiler.plugins.declarations.show.hidden.description": "호출 위치에서 보이지 않는 선언 표시",
  "hints.description.compiler.plugins.declarations": "Kotlin 컴파일러 플러그인에서 생성된 선언",
  "hints.tooltip.compiler.plugins.declarations": "Kotlin 컴파일러 플러그인에 의해 생성됨",
  "hints.tooltip.compiler.plugins.declarations.expand": "Kotlin 컴파일러 플러그인이 생성한 Kotlin 선언. 보려면 클래스 본문을 확장하세요.",
  "hints.settings.show.types.property": "속성 유형 힌트 표시",
  "hints.settings.dont.show.types.property": "속성 유형 힌트 표시 안 함",
  "hints.settings.show.types.variable": "지역 변수 유형 힌트 표시",
  "hints.settings.dont.show.types.variable": "지역 변수 유형 힌트 표시 안 함",
  "hints.settings.show.types.return": "함수 반환 유형 힌트 표시",
  "hints.title.show.argument.name.enabled": "인수 이름 힌트 표시",
  "hints.title.dont.show.argument.name.enabled": "인수 이름 힌트 표시 안 함",
  "hints.settings.dont.show.types.return": "함수 반환 유형 힌트 표시 안 함",
  "hints.settings.show.types.parameter": "함수 매개변수 유형 힌트 표시",
  "hints.settings.dont.show.types.parameter": "함수 매개변수 유형 힌트 표시 안 함",
  "hints.settings.show.lambda.return": "반환 표현식 힌트 표시",
  "hints.settings.dont.show.lambda.return": "반환 표현식 힌트 표시 안 함",
  "hints.settings.show.lambda.receivers.parameters": "암시적 수신자 및 매개변수 힌트 표시",
  "hints.settings.dont.show.lambda.receivers.parameters": "암시적 수신자 및 매개변수 힌트 표시 안 함"
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

print(f"Updated {filename} (Keys 391-440)")

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
