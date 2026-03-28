import json

ko_dict = {
  "inspection.replace.with.import.alias.display.name": "정규화된 이름(Fully qualified name)을 기존 가져오기(import) 별칭으로 바꿀 수 있습니다.",
  "replace.with.import.alias": "가져오기 별칭으로 바꾸기",
  "inspection.suspicious.call.on.collection.to.add.or.remove.path.display.name": "Java NIO Path를 추가하거나 제거하기 위한 Collection에 대한 의심스러운 호출",
  "plus.call.appends.path.elements": "'plus' 호출은 Path 요소를 추가합니다.",
  "minus.call.removes.path.elements": "'minus' 호출은 Path 요소를 제거합니다.",
  "convert.to.plus.element.call": "'plusElement' 호출로 변환 (의미 체계 변경됨)",
  "convert.to.minus.element.call": "'minusElement' 호출로 변환 (의미 체계 변경됨)",
  "convert.path.to.explicit.collection": "Path를 명시적 Collection으로 변환",
  "inspection.convert.argument.to.set.display.name": "성능을 향상시키기 위해 인수를 'Set'으로 변환할 수 있습니다.",
  "can.convert.argument.to.set": "성능을 향상시키기 위해 인수를 'Set'으로 변환할 수 있습니다.",
  "convert.argument.to.set.fix.text": "인수를 'Set'으로 변환",
  "convert.to.unicode.escape": "유니코드 이스케이프로 변환",
  "popup.title.expressions": "표현식",
  "popup.title.types": "유형",
  "popup.title.elements": "요소",
  "action.hints.settings.text": "힌트 설정\\u2026",
  "start.import.button.text.add": "추다",
  "start.import.button.text.remove": "제거",
  "import.order.button.text.add.package": "패키지 추가",
  "import.order.button.text.remove": "제거",
  "import.order.button.text.up": "위로",
  "import.order.button.text.down": "아래로",
  "import.text.all.other.imports": "기타 모든 가져오기",
  "import.text.import": "가져오기(import)",
  "import.text.all.alias.imports": "모든 별칭 가져오기",
  "extract.new.parameter.name.receiver": "<receiver>",
  "kotlin.compiler.configurable": "Kotlin 컴파일러",
  "kotlin.scripting.configurable": "Kotlin 스크립팅",
  "hint.text.no.expression.found": "표현식을 찾을 수 없음",
  "progress.title.calculating.type": "유형 계산 중\\u2026",
  "intention.name.use.correct.parameter.name": "올바른 매개변수 이름 사용",
  "intention.add.import.alias.group.name": "가져오기 별칭 추가",
  "inspection.message.inconsistent.parameter.name.for.0": "''{0}''에 대한 일관성 없는 매개변수 이름",
  "inspection.kotlin.catch.may.ignore.exception.display.name": "'catch' 블록이 예외를 무시할 수 있습니다.",
  "inspection.message.empty.catch.block": "빈 catch 블록",
  "replace.and.with.when.guard": "'\\\\&\\\\&'를 'if'로 바꾸기",
  "inspection.kotlin.jvm.annotation.in.java.display.name": "Java의 Kotlin JVM 주석",
  "inspection.kotlin.jvm.annotation.in.java.description": "Kotlin JVM 주석 ''{0}''은(는) Java에서 아무런 효과가 없습니다.",
  "add.empty.argument.list": "빈 인수 목록 추가",
  "find.declaration.implementing.methods.checkbox": "구현 함수(&I)",
  "find.declaration.overriding.methods.checkbox": "재정의 함수(&R)",
  "find.declaration.implementing.properties.checkbox": "구현 속성(&I)",
  "find.declaration.overriding.properties.checkbox": "재정의 속성(&R)",
  "find.declaration.property.readers.checkbox": "독자(Readers)",
  "find.declaration.property.writers.checkbox": "작성자(Writers)",
  "find.declaration.include.overloaded.methods.checkbox": "오버로드된 함수 및 확장 포함(&V)",
  "find.declaration.functions.usages.checkbox": "함수 사용법(&F)",
  "find.declaration.properties.usages.checkbox": "속성 사용법(&P)",
  "find.declaration.constructor.usages.checkbox": "생성자 사용법(&C)",
  "find.declaration.derived.classes.checkbox": "파생 클래스(&D)"
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

print(f"Updated {filename} (Keys 2091-2140)")

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
