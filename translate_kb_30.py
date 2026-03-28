import json

ko_dict = {
  "remove.require.not.null.call.fix.text": "''{0}'' 호출 제거",
  "remove.return.label.fix.text": "중복 ''@{0}'' 제거",
  "remove.return.label.fix.family": "중복 레이블 제거",
  "remove.redundant.return": "중복 반환 제거",
  "redundant.0": "중복 ''@{0}''",
  "remove.redundant.sam.constructors": "중복 SAM 생성자 제거",
  "remove.redundant.sam.constructor": "중복 SAM 생성자 제거",
  "redundant.sam.constructors": "중복 SAM 생성자",
  "redundant.sam.constructor": "중복 SAM 생성자",
  "redundant.semicolon.text": "중복 세미콜론 제거",
  "redundant.semicolon": "중복 세미콜론",
  "remove.redundant.setter.fix.text": "중복 setter 제거",
  "remove.redundant.setter.body.fix.text": "중복 setter 본문 제거",
  "redundant.setter": "중복 setter",
  "redundant.setter.body": "중복 setter 본문",
  "redundant.suspend.modifier": "중복 'suspend' 한정자",
  "redundant.unit.return.type": "중복 'Unit' 반환 유형",
  "redundant.visibility.modifier": "중복 가시성 한정자",
  "remove.redundant.unit.fix.text": "중복 'Unit' 제거",
  "redundant.unit": "중복 'Unit'",
  "remove.redundant.with.fix.text": "중복 'with' 호출 제거",
  "remove.jvmoverloads.annotation": "@JvmOverloads 주석 제거",
  "remove.jvmfield.annotation": "@JvmField 주석 제거",
  "remove.extension.function.type.annotation": "적용할 수 없는 @ExtensionFunctionType 주석 제거",
  "remove.annotation.doesnt.have.any.effect": "효과가 없으므로 주석을 제거합니다. 참조: https://youtrack.jetbrains.com/issue/KT-48141",
  "remove.use.site.get.target": "주석을 효과적으로 만들려면 'get:'을 제거합니다. (의미가 변경됩니다. 참조: https://youtrack.jetbrains.com/issue/KT-48141)",
  "report.also.for.a.variables.without.a.whitespace.around": "주위에 공백이 없는 변수에 대해서도 보고",
  "remove.curly.braces": "중괄호 제거",
  "redundant.curly.braces.in.string.template": "문자열 템플릿의 중복 중괄호",
  "remove.empty.parentheses.from.annotation.entry.fix.text": "불필요한 괄호 제거",
  "parentheses.should.be.removed": "괄호를 제거해야 합니다.",
  "remove.redundant.qualifier.name.quick.fix.text": "중복 한정자 이름 제거",
  "redundant.qualifier.name": "중복 한정자 이름",
  "remove.redundant.backticks.quick.fix.text": "중복 백틱(`) 제거",
  "remove.redundant.spread.operator.quickfix.text": "중복 스프레드 연산자 제거",
  "remove.to.string.fix.text": "'toString()' 호출 제거",
  "redundant.tostring.call.in.string.template": "문자열 템플릿의 중복 'toString()' 호출",
  "redundant.setter.parameter.type": "중복 setter 매개변수 유형",
  "replace.not.equal.with.content.equals": "'!='를 'contentEquals'로 바꾸기",
  "replace.equal.with.content.equals": "'=='를 'contentEquals'로 바꾸기",
  "replace.with.content.equals": "'contentEquals'로 바꾸기",
  "dangerous.array.comparison": "위험한 배열 비교",
  "replace.with.array.literal.fix.family.name": "[...]로 바꾸기",
  "0.call.should.be.replaced.with.array.literal": "''{0}'' 호출을 배열 리터럴 [...]로 바꿔야 합니다.",
  "replace.assert.boolean.with.assert.equality": "부울 어설션을 동등성 어설션으로 바꾸기",
  "replace.0.with.1": "''{0}''을(를) ''{1}''(으)로 바꾸기",
  "replace.collection.count.with.size.quick.fix.text": "'count'를 'size'로 바꾸기",
  "could.be.replaced.with.size": "'size'로 바꿀 수 있습니다.",
  "replace.with.kotlin.s.function.call": "Kotlin 함수 호출로 바꾸기",
  "replace.guard.clause.with.kotlin.s.function.call": "가드(guard) 절을 Kotlin 함수 호출로 바꾸기"
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

print(f"Updated {filename} (Keys 1191-1240)")

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
