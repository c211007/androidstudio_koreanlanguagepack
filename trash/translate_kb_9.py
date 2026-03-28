import json

ko_dict = {
  "hints.settings.show.suspending": "일시 중단 호출 힌트 표시",
  "hints.settings.dont.show.suspending": "일시 중단 호출 힌트 표시 안 함",
  "hints.settings.show.ranges": "범위 힌트 표시",
  "hints.settings.dont.show.ranges": "범위 힌트 표시 안 함",
  "hints.settings.lambdas": "람다",
  "hints.settings.lambda.return": "반환 표현식",
  "hints.settings.lambda.receivers.parameters": "암시적 수신자 및 매개변수",
  "hints.settings.value.ranges": "범위",
  "hints.settings.ranges": "범위",
  "hints.ranges.lessOrEqual": "≤",
  "hints.ranges.less": "<",
  "hints.ranges.greaterOrEqual": "≥",
  "hints.settings.value.kotlin.time": "kotlin.time 경고",
  "hints.settings.default.parameters": "기본 매개변수 값",
  "inlay.kotlin.default.parameters.hints": "재정의된 메서드에 기본 매개변수 값 표시",
  "hints.settings.suspending": "일시 중단 호출",
  "hints.title.argument.name.enabled": "인수 이름",
  "presentation.text.paren": "({0})",
  "presentation.text.paren.no.brackets": "{0}",
  "presentation.text.in.container.paren": "({0} 내부)",
  "presentation.text.in.container.paren.no.brackets": "{0} 내부",
  "presentation.text.in.container": "{1} 내부의 {0}",
  "presentation.text.for.receiver.in.container.paren": "({1} 내부의 {0}용)",
  "presentation.text.for.receiver.in.container.paren.no.brackets": "{1} 내부의 {0}용",
  "presentation.text.object.in.container": "{0} 내부의 객체",
  "project.view.class.initializer": "클래스 이니셜라이저",
  "project.view.expression": "표현식",
  "project.view.class.error.name": "제공된 이름 없음",
  "editor.checkbox.title.auto.add.val.keyword.to.data.value.class.constructor.parameters": "데이터/값 클래스 생성자 매개변수에 'val' 키워드 자동 추가",
  "editor.checkbox.title.convert.pasted.java.code.to.kotlin": "붙여넣은 Java 코드를 Kotlin으로 변환",
  "editor.checkbox.title.don.t.show.java.to.kotlin.conversion.dialog.on.paste": "붙여넣을 때 Java를 Kotlin으로 변환 대화상자 표시 안 함",
  "editor.title.kotlin": "Kotlin",
  "find.usages.progress.text.declaration.superMethods": "상위 메서드 확인 중…",
  "formatter.button.text.use.import.with.when.at.least": "최소 조건인 경우 '*'를 포함하여 가져오기 사용",
  "formatter.button.text.use.import.with": "'*'를 포함하여 가져오기 사용",
  "formatter.button.text.use.single.name.import": "단일 이름 가져오기 사용",
  "formatter.checkbox.text.insert.imports.for.nested.classes": "중첩 클래스용 가져오기 삽입",
  "formatter.checkbox.text.use.trailing.comma": "후행 쉼표 사용",
  "formatter.checkbox.text.type.parameter.list": "유형 매개변수 목록",
  "formatter.checkbox.text.destructuring.declaration": "구조 분해 선언",
  "formatter.checkbox.text.when.entry": "when 항목",
  "formatter.checkbox.text.function.literal": "함수 리터럴",
  "formatter.checkbox.text.value.parameter.list": "값 매개변수 목록",
  "formatter.checkbox.text.context.receiver.list": "컨텍스트 수신자 목록",
  "formatter.checkbox.text.collection.literal.expression": "컬렉션 리터럴 표현식",
  "formatter.checkbox.text.type.argument.list": "유형 인수 목록",
  "formatter.checkbox.text.indices": "인덱스",
  "formatter.checkbox.text.value.argument.list": "값 인수 목록",
  "formatter.text.names.used": "\\ 이름 사용됨",
  "formatter.text.use.defaults.from": "다음에서 기본값 사용:"
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

print(f"Updated {filename} (Keys 441-490)")

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
