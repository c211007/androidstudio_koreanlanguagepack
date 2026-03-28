import json

ko_dict = {
  "can.t.replace.foreign.reference.with.call.expression.0": "외부(foreign) 참조를 호출 표현식으로 바꿀 수 없습니다: {0}",
  "unrecognized.reference.will.be.skipped.0": "인식할 수 없는 참조는 건너뜁니다: {0}",
  "property.overloaded.in.child.class.constructor": "하위 클래스 생성자에서 속성이 오버로드되었습니다.",
  "property.has.an.actual.declaration.in.the.class.constructor": "클래스 생성자에 속성의 'actual' 선언이 있습니다.",
  "convert.to.comparisons": "비교로 변환",
  "convert.receiver.to.parameter": "수신자를 매개변수로 변환",
  "highlight.usages.of.receiver": "수신자 사용 강조",
  "convert.reference.to.lambda.before.text": "참조를 람다로 변환할 수 있습니다.",
  "convert.reference.to.lambda": "참조를 람다로 변환",
  "following.problems.are.found": "다음 문제가 발견되었습니다:\\n",
  "all.expected.and.actual.classes.must.be.sealed.classes": "모든 'expected' 및 'actual' 클래스는 sealed 클래스여야 합니다.\\n",
  "all.inheritors.must.be.nested.objects.of.the.class.itself.and.may.not.inherit.from.other.classes.or.interfaces": "모든 상속자는 클래스 자체의 중첩된(nested) 객체여야 하며, 다른 클래스나 인터페이스에서 상속할 수 없습니다.\\n",
  "searching.inheritors": "상속자를 검색하는 중\\u2026",
  "convert.to.enum.class": "enum 클래스로 변환",
  "convert.to.primary.constructor": "기본 생성자로 변환",
  "convert.to.primary.constructor.before.text": "보조 생성자를 기본 생성자로 변환해야 합니다.",
  "rename.to.01": "{0}(으)로 이름 바꾸기",
  "replace.0.name.with.spaces": "{0} 이름을 공백으로 바꾸기",
  "convert.to.block.body": "블록 본문으로 변환",
  "convert.body.to.expression": "본문을 표현식으로 변환",
  "convert.template.to.concatenated.string": "템플릿을 연결 문자열로 변환",
  "replace.with.a.foreach.function.call": "''{0}'' 함수 호출로 바꾸기",
  "convert.concatenation.to.raw.string": "연결을 원시(raw) 문자열로 변환",
  "convert.concatenation.to.template.before.text": "'String' 연결을 템플릿으로 변환할 수 있습니다.",
  "convert.concatenation.to.template": "연결을 템플릿으로 변환",
  "convert.try.finally.to.use.before.text": "'try-finally'를 'use()'로 바꿀 수 있습니다.",
  "convert.try.finally.to.use": "'try-finally'를 'use()'로 바꾸기",
  "convert.to.unsafe.cast": "안전하지 않은(unsafe) 캐스트로 변환",
  "convert.to.0.as.1": "''{0} as {1}''(으)로 변환",
  "convert.to.0.unsafecast.1": "''{0}.unsafeCast<{1}>()''(으)로 변환",
  "convert.to.unsafecast.call": "unsafeCast() 호출로 변환",
  "convert.to.array.parameter": "배열 매개변수로 변환",
  "convert.to.assignment.expression": "할당 문을 표현식으로 변환",
  "convert.to.trim.indent": "'trimIndent()' 호출로 변환",
  "convert.to.trim.margin": "'trimMargin()' 호출로 변환",
  "create.kotlin.subclass": "Kotlin 하위 클래스 만들기",
  "use.destructuring.declaration": "구조 분해(destructuring) 선언 사용",
  "implement.as.constructor.parameter": "생성자 매개변수로 구현",
  "implement.abstract.member": "추상(abstract) 멤버 구현",
  "import.members.from.0": "''{0}''에서 멤버 가져오기",
  "import.members.with": "'*'로 멤버 가져오기",
  "add.import.for.0": "''{0}''에 대한 가져오기(import) 추가",
  "add.import.for.member": "멤버에 대한 가져오기(import) 추가",
  "indent.raw.string": "원시(raw) 문자열 들여쓰기",
  "replace.infix.call.with.ordinary.call": "중위(infix) 호출을 일반 호출로 바꾸기",
  "infix.call.may.be.dot.call": "중위 호출이 점(dot) 호출일 수 있습니다.",
  "insert.curly.braces.around.variable": "변수 주위에 중괄호 삽입",
  "add.explicit.type.arguments": "명시적 유형 인수 추가",
  "introduce.backing.property": "배킹(backing) 속성 도입",
  "introduce.import.alias": "가져오기(import) 별칭 도입"
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

print(f"Updated {filename} (Keys 1441-1490)")

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
