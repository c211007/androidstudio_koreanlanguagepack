import json

ko_dict = {
  "formatter.title.after.colon.before.declaration.type": "콜론 뒤, 선언 유형 앞",
  "formatter.title.after.colon.in.new.type.definition": "새 유형 정의의 콜론 뒤",
  "formatter.title.align.when.branches.in.columns": "열에 'when' 분기 정렬",
  "formatter.title.line.break.after.multiline.when.entry": "여러 줄 항목 다음 새 줄",
  "formatter.title.indent.before.arrow.on.new.line": "새 줄의 '->' 앞에 들여쓰기",
  "formatter.title.around.arrow.in.function.types": "함수 유형의 화살표 부근",
  "formatter.title.around.arrow.in": "\"when\" 절의 화살표 부근",
  "formatter.title.around.when.branches.with": "{}가 있는 'when' 분기 부근",
  "formatter.title.before.declaration.with.comment.or.annotation": "주석 또는 설명이 있는 선언 앞",
  "formatter.title.before.colon.after.declaration.name": "콜론 앞, 선언 이름 뒤",
  "formatter.title.before.colon.in.new.type.definition": "새 유형 정의의 콜론 앞",
  "formatter.title.before.lambda.arrow": "람다 화살표 앞",
  "formatter.title.chained.function.calls": "연결된 함수 호출",
  "formatter.title.elvis.expressions": "엘비스(Elvis) 표현식",
  "formatter.title.expression.body.functions": "표현식 본문 함수",
  "formatter.title.function.annotations": "함수 주석",
  "formatter.title.function.call.arguments": "함수 호출 인수",
  "formatter.title.function.context.parameters": "함수 컨텍스트 매개변수",
  "formatter.title.property.context.parameters": "속성 컨텍스트 매개변수",
  "formatter.title.function.declaration.parameters": "함수 선언 매개변수",
  "formatter.title.function.parentheses": "함수 괄호",
  "formatter.title.in.simple.one.line.methods": "간단한 한 줄 메서드 내부",
  "formatter.title.java.statics.and.enum.members": "Java 정적 및 열거형(Enum) 멤버",
  "formatter.title.load.save": "로드/저장",
  "formatter.title.other": "기타",
  "formatter.title.trailing.comma": "후행 쉼표",
  "formatter.title.property.annotations": "속성 주석",
  "formatter.title.put.left.brace.on.new.line": "새 줄에 왼쪽 중괄호 넣기",
  "formatter.title.range.operator": "범위 연산자(.., ..<)",
  "formatter.title.elvis.operator": "엘비스(Elvis) 연산자(?:)",
  "formatter.title.top.level.symbols": "최상위 기호",
  "formatter.title.use.continuation.indent.in.conditions": "조건에 연속 들여쓰기 사용",
  "formatter.title.use.continuation.indent": "연속 들여쓰기 사용",
  "formatter.title.when.parentheses": "'when' 괄호",
  "formatter.title.when.statements": "'when' 문",
  "ambiguous.non.local.break.or.continue.display.name": "모호한 로컬이 아닌 'break' 또는 'continue'",
  "ambiguous.non.local.break.or.continue.use.label": "모호한 로컬이 아닌 ''{0}''(''{1}'' 대 ''{2}'')입니다. 명확한 레이블을 사용하세요.",
  "ambiguous.non.local.break.or.continue.use.label.or.contract": "모호한 로컬이 아닌 ''{0}''(''{1}'' 대 ''{2}'')입니다. 명확한 레이블을 사용하거나 ''{3}''에 ''callsInPlace'' 계약을 추가하세요.",
  "hierarchy.text.anonymous": "[익명]",
  "hierarchy.text.in": "\\ {0} 내부",
  "highlighter.action.text.go.to.actual.declarations": "실제 선언으로 이동",
  "highlighter.action.text.go.to.expected.declaration": "예상 선언으로 이동",
  "highlighter.action.text.go.to.implementations": "구현으로 이동",
  "highlighter.action.text.go.to.overridden.methods": "재정의된 메서드로 이동",
  "highlighter.action.text.go.to.overridden.properties": "재정의된 속성으로 이동",
  "highlighter.action.text.go.to.subclasses": "하위 클래스로 이동",
  "highlighter.action.text.go.to.super.method": "상위 메서드로 이동",
  "highlighter.action.text.go.to.super.property": "상위 속성으로 이동",
  "highlighter.descriptor.text.android.extensions.property": "속성 및 변수//Android 확장 기능 합성 속성",
  "highlighter.descriptor.text.annotation": "주석//주석 이름"
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
