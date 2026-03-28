import json

ko_dict = {
  "jvm.inspections.junit.malformed.param.file.source.descriptor": "파일 소스를 확인할 수 없음: ''{0}''",
  "jvm.inspections.junit.malformed.source.without.params.descriptor": "메서드에 매개변수가 없으므로 ''@{0}''이(가) 메서드에 인수를 제공할 수 없습니다.",
  "jvm.inspections.junit.malformed.source.without.constructor": "선언된 형식 매개변수가 없으므로 ''@{0}''이(가) [''{1}''] 생성자에 인수를 제공할 수 없습니다.",
  "jvm.inspections.junit.malformed.single.constructor.descriptor": "{0} 클래스는 단일 생성자를 선언해야 합니다.",
  "jvm.inspections.junit.malformed.param.empty.source.unsupported.descriptor": "메서드에 지원되지 않는 ''{1}'' 유형의 매개변수가 있으므로 ''@{0}''이(가) 메서드에 인수를 제공할 수 없습니다.",
  "jvm.inspections.junit.malformed.param.multiple.parameters.descriptor": "''@{0}''(으)로 단일 매개변수만 제공될 수 있습니다.",
  "jvm.inspections.junit.malformed.param.no.sources.are.provided.descriptor": "소스가 제공되지 않으면 모음이 비어 있습니다.",
  "jvm.inspections.junit.malformed.fix.class.signature": "클래스 시그니처 수정",
  "jvm.inspections.junit.malformed.fix.class.signature.multi": "클래스 시그니처 수정",
  "jvm.inspections.junit.malformed.fix.class.signature.descriptor": "''{0}'' 클래스 시그니처 수정",
  "jvm.inspections.junit.malformed.fix.method.signature": "메서드 시그니처 수정",
  "jvm.inspections.junit.malformed.fix.method.signature.descriptor": "''{0}'' 메서드 시그니처 수정",
  "jvm.inspections.junit.malformed.fix.field.signature": "필드 시그니처 수정",
  "jvm.inspections.junit.malformed.fix.field.signature.descriptor": "''{0}'' 필드 시그니처 수정",
  "jvm.inspections.junit.assertequals.on.array.display.name": "배열에서 'assertEquals()' 호출됨",
  "jvm.inspections.junit.assertequals.on.array.problem.descriptor": "배열에서 <code>#ref()</code> 호출됨 #loc",
  "jvm.inspections.junit.assertequals.may.be.assertsame.display.name": "'assertEquals()'는 'assertSame()'일 수 있습니다",
  "jvm.inspections.junit.assertequals.may.be.assertsame.problem.descriptor": "<code>#ref()</code>는 'assertSame()'일 수 있습니다 #loc",
  "jvm.inspections.junit.ignored.test.display.name": "'@Ignore'/'@Disabled'(으)로 어노테이션이 지정된 JUnit 테스트",
  "jvm.inspections.junit.ignored.test.ignore.reason.option": "이유가 없는 어노테이션만 보고",
  "jvm.inspections.junit.ignored.test.class.problem.descriptor": "테스트 클래스 ''{0}''이(가) 무시됨/비활성화됨 {1, choice, 1#|2#이유 없이} #loc",
  "jvm.inspections.junit.ignored.test.method.problem.descriptor": "테스트 메서드 ''{0}()''이(가) 무시됨/비활성화됨 {1, choice, 1#|2#이유 없이} #loc",
  "jvm.inspections.migrate.assertion.name": "JUnit 어설션은 'assertThat()' 호출일 수 있습니다",
  "jvm.inspections.migrate.assert.to.matcher.option": "선택기 메서드를 정적으로 가져오기",
  "jvm.inspections.migrate.assert.to.matcher.description": "어설션 표현식 <code>#ref</code>을(를) ''{0}'' 호출로 바꿀 수 있습니다 #loc",
  "inspection.parameterized.parameters.static.collection.display.name": "데이터 공급자 메서드가 없는 매개변수화된 테스트 클래스",
  "fix.data.provider.signature.fix.name": "메서드 시그니처를 ''{0}''(으)로 변경",
  "fix.data.provider.create.method.fix.name": "'@Parameters public static Iterable<Object> parameters()' 데이터 공급자 메서드 생성",
  "fix.data.provider.signature.family.name": "데이터 공급자 메서드 시그니처 수정",
  "fix.data.provider.signature.missing.method.problem": "매개변수화된 테스트 클래스 <code>#ref</code>에 '@Parameters'로 어노테이션이 지정된 데이터 공급자 메서드가 없습니다.",
  "fix.data.provider.signature.incorrect.problem": "데이터 공급자 메서드 <code>#ref()</code>의 시그니처가 잘못되었습니다.",
  "fix.data.provider.multiple.methods.problem": "클래스 <code>#ref</code>에 여러 @Parameters 데이터 공급자 메서드가 있습니다.",
  "expected.exception.never.thrown.display.name": "예상되는 예외가 테스트 메서드 본문에서 발생하지 않음",
  "expected.exception.never.thrown.problem.descriptor": "예상된 <code>#ref</code>이(가) ''{0}()'' 본문에서 발생하지 않음 #loc",
  "junit3.style.test.method.in.junit4.class.display.name": "JUnit 4 클래스의 이전 스타일 JUnit 테스트 메서드",
  "junit3.style.test.method.in.junit4.class.problem.descriptor": "JUnit 4 클래스의 이전 스타일 JUnit 테스트 메서드 <code>#ref()</code> #loc",
  "multiple.exceptions.declared.on.test.method.display.name": "테스트 메서드에 선언된 예외 여러 개",
  "multiple.exceptions.declared.on.test.method.problem.descriptor": "<code>#ref</code>은(는) 'throws Exception'으로 바꿀 수 있습니다 #loc",
  "usage.of.obsolete.assert.display.name": "유효하지 않은 'junit.framework.Assert' 메서드 사용",
  "use.of.obsolete.assert.problem.descriptor": "''{0}''에서의 <code>#ref()</code> 호출은 ''org.junit.Assert''의 메서드 호출로 대체되어야 합니다 #loc",
  "use.of.obsolete.assert.quickfix": "'org.junit.Assert' 메서드 호출로 교체"
}

with open('missing_translations/missing_keys_korean.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

filename = "JUnitBundle.properties"
found = False
for file_entry in data.get('new_files', []):
    if file_entry['filename'] == filename:
        file_entry['keys'].update(ko_dict)
        found = True
        break
if not found:
    data.setdefault('new_files', []).append({"filename": filename, "keys": ko_dict})

print(f"Updated {filename} (Keys 161-201)")

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
