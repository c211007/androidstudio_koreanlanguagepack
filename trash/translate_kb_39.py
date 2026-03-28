import json

ko_dict = {
  "implement.interface": "인터페이스 구현",
  "implement.abstract.function": "abstract 함수 구현",
  "implement.abstract.property": "abstract 속성 구현",
  "replace.explicit.lambda.parameter.with.it": "명시적 람다 매개변수를 'it'으로 바꾸기",
  "create.test": "테스트 생성",
  "convert.class.0.to.kotlin": "''{0}'' 클래스를 Kotlin으로 변환",
  "status": "(상태)",
  "action.text.install": "설치",
  "version": "{version}",
  "don.t.show.this.dialog.next.time": "다음에 이 대화상자 표시 안 함(&D)",
  "clipboard.content.copied.from.java.file.do.you.want.to.convert.it.to.kotlin.code": "Java 파일에서 클립보드 내용이 복사되었습니다. Kotlin 코드로 변환하시겠습니까?",
  "name": "이름(&N):",
  "return.type": "반환 유형(&R):",
  "visibility": "가시성(&V):",
  "title.parameters": "매개변수",
  "signature.preview": "서명 미리보기",
  "move.members.from": "다음에서 멤버 이동:",
  "open.moved.members.in.editor": "이동된 멤버를 편집기에서 열기",
  "open.moved.method.in.editor": "이동된 메서드를 편집기에서 열기",
  "to.fully.qualified.name": "대상(정규화된 이름):",
  "incomplete.destructuring.declaration.text": "불완전한 구조 분해(destructuring) 선언",
  "incomplete.destructuring.fix.family.name": "구조 분해 선언에 누락된 변수 추가",
  "no.actual.for.expect.declaration": "다음 모듈에서 expect 선언에 대한 actual이 없습니다: {0}",
  "category.class": "Kotlin/클래스 기반",
  "category.comments": "Kotlin/주석, KDoc 및 메타데이터",
  "category.expressions": "Kotlin/표현식",
  "category.declaration": "Kotlin/선언",
  "category.interesting": "Kotlin/기타 관심 항목",
  "category.operators": "Kotlin/연산자",
  "context.default": "기본",
  "context.property.getter.or.setter": "명시적 Getter/Setter가 있는 속성",
  "error.context.getter.or.setter": "이 컨텍스트는 명시적 getter/setter가 있는 속성에만 사용할 수 있습니다. (파일 유형을 Kotlin으로 설정하세요)",
  "error.expected.an.expression": "표현식이 필요합니다.",
  "error.expected.catch.or.finally": "'catch' 또는 'finally'가 필요합니다.",
  "error.param.can.t.be.null.at.index.0.in.1": "{1}의 인덱스 {0}에서 Param은 null일 수 없습니다.",
  "ssr.modifier.match.val": "val 일치",
  "ssr.modifier.match.var": "var 일치",
  "ssr.modifier.match.companion.object": "companion object 일치",
  "ssr.modifier.match.call.semantically": "의미상 호출 일치",
  "predefined.configuration.all.methods.of.the.class": "클래스의 모든 메서드",
  "predefined.configuration.all.vars.of.the.class": "클래스의 모든 변수(vars)",
  "predefined.configuration.all.vars.of.the.object": "객체의 모든 변수(vars)",
  "predefined.configuration.annotations": "주석(Annotations)",
  "predefined.configuration.anonymous.class": "익명 클래스",
  "predefined.configuration.array.access": "배열 접근",
  "predefined.configuration.assert.not.null": "Not-null 어서션(assertion) 연산자",
  "predefined.configuration.assignments": "할당",
  "predefined.configuration.casts": "캐스트",
  "predefined.configuration.class.annotation": "주석이 포함된 클래스",
  "predefined.configuration.object.companion.object": "객체 및 companion object"
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

print(f"Updated {filename} (Keys 1641-1690)")

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
