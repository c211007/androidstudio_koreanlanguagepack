import json

ko_dict = {
  "highlighter.name.expect.actual.line.markers": "Kotlin ''expect''//''actual'' 줄 마커",
  "highlighter.name.dsl.markers": "DSL 마커",
  "highlighter.name.implemented.declaration": "구현된 선언",
  "highlighter.name.implementing.declaration": "구현하는 선언",
  "highlighter.name.kotlin.line.markers": "Kotlin 줄 마커",
  "highlighter.name.multiplatform.actual.declaration": "멀티플랫폼 실제 선언",
  "highlighter.name.multiplatform.expect.declaration": "멀티플랫폼 예상 선언",
  "highlighter.name.overridden.declaration": "재정의된 선언",
  "highlighter.name.overriding.declaration": "재정의하는 선언",
  "highlighter.notification.text.navigation.to.overriding.classes.is.not.possible.during.index.update": "인덱스 업데이트 중에는 재정의하는 클래스로 이동할 수 없습니다.",
  "highlighter.prefix.text.has.actuals.in": "다음 {0} {1, choice, 0#모듈|1#모듈}에 실젯값이 있습니다.",
  "highlighter.text.click.for.navigate": "이동하려면 {0}을(를) 클릭하세요.",
  "highlighter.text.has.functional.implementations": "기능적 구현 포함",
  "highlighter.text.implements": "구현",
  "highlighter.text.in": "''{1}''의 {0}",
  "highlighter.text.or.press": "\\ 또는 {0}을(를) 누르세요",
  "highlighter.text.overrides": "재정의",
  "highlighter.title.overriding.declarations.of": "{0} 선언 재정의",
  "highlighter.title.searching.for.overriding.declarations": "재정의 선언 검색 중",
  "highlighter.title.searching.for.overriding.methods": "재정의 메서드 검색 중",
  "highlighter.tool.tip.has.expect.declaration.in": "다음 {0} {1, choice, 0#모듈|1#모듈}에 예상 선언이 있습니다.",
  "highlighter.tool.tip.marker.annotation.for.dsl": "DSL 마커 주석",
  "highlighter.tool.tip.text.function": "함수",
  "highlighter.tool.tip.text.property": "속성",
  "highlighter.tool.tip.text.recursive.call": "재귀 호출",
  "import.optimizer.notification.text.unused.imports.not.found": "사용되지 않는 가져오기를 찾을 수 없음",
  "import.optimizer.progress.indicator.text.collect.imports.for": "{0} 가져오기 수집 중",
  "import.optimizer.text.import": "{0, choice, 0#가져오기|2#가져오기}",
  "import.optimizer.text.non.zero": "{0}개 {1} 제거됨{2, choice, 0#|1#, {2} {3} 추가됨}",
  "import.optimizer.text.zero": "가져오기 재정렬됨",
  "import.progress.text.resolve.imports": "모든 가져오기 찾기…",
  "test.integration.button.text.cancel": "취소",
  "test.integration.button.text.rewrite": "다시 쓰기",
  "test.integration.message.text.create.test.in.the.same.source.root": "동일한 소스 루트에 테스트를 생성하시겠습니까?",
  "test.integration.message.text.kotlin.class": "Kotlin 클래스 ''{0}''이(가) 이미 존재합니다. 업데이트하시겠습니까?",
  "test.integration.title.no.test.roots.found": "테스트 루트를 찾을 수 없음",
  "slicer.text.in": "내부:",
  "slicer.text.tracking.enclosing.lambda": "\\ (포함하는 람다 추적 중)",
  "slicer.text.tracking.lambda.calls": "\\ (람다 호출 추적 중)",
  "slicer.text.tracking.lambda.argument": "\\ (람다 매개변수 추적 중)",
  "slicer.text.tracking.lambda.receiver": "\\ (람다 수신자 추적 중)",
  "slicer.title.dataflow.from.here": "여기로부터의 데이터플로",
  "slicer.title.dataflow.to.here": "여기로의 데이터플로",
  "slicer.tool.tip.text.variable.dereferenced": "변수 역참조됨",
  "script.action.text.ignore": "무시",
  "script.action.text.open.settings": "설정 열기",
  "script.action.text.show.all": "모두 표시",
  "script.name.kotlin.scripting": "Kotlin 스크립팅",
  "text.first.definition.that.matches.script.pattern.extension.applied.starting.from.top": "위에서부터 시작하여 스크립트 패턴/확장자와 일치하는 첫 번째 정의가 적용됩니다.",
  "status.text.no.definitions": "정의 없음"
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

print(f"Updated {filename} (Keys 541-590)")

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
