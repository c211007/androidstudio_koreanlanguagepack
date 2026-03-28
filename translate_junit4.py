import json

ko_dict = {
  "jvm.inspections.junit.malformed.declaration.name": "형식이 잘못된 JUnit 선언",
  "jvm.inspections.junit.malformed.option.ignore.test.parameter.if.annotated.by": "다음으로 어노테이션이 지정된 경우 테스트 매개변수 무시:",
  "jvm.inspections.junit.malformed.no.arg.descriptor": "<code>#ref</code> 메서드는 {0}, {1}{2, choice, 0#이어야 하며 매개변수가 없어야 함|1#이어야 하며, 매개변수가 없고 void 유형이어야 함}",
  "jvm.inspections.junit.malformed.annotated.single.descriptor": "''@{1}''(으)로 어노테이션이 지정된 <code>#ref</code> {0, choice, 0#필드|1#메서드}는 {2}이어야 합니다.",
  "jvm.inspections.junit.malformed.annotated.double.descriptor": "''@{1}''(으)로 어노테이션이 지정된 <code>#ref</code> {0, choice, 0#필드|1#메서드}는 {2}이고 {3}이어야 합니다.",
  "jvm.inspections.junit.malformed.annotated.typed.descriptor": "''@{1}''(으)로 어노테이션이 지정된 <code>#ref</code> {0, choice, 0#필드|1#메서드}는 ''{2}'' 유형이어야 합니다.",
  "jvm.inspections.junit.malformed.annotated.single.typed.descriptor": "''@{1}''(으)로 어노테이션이 지정된 <code>#ref</code> {0, choice, 0#필드|1#메서드}는 {2}이고 ''{3}'' 유형이어야 합니다.",
  "jvm.inspections.junit.malformed.annotated.double.typed.descriptor": "''@{1}''(으)로 어노테이션이 지정된 <code>#ref</code> {0, choice, 0#필드|1#메서드}는 {2}, {3}이고 ''{4}'' 유형이어야 합니다.",
  "jvm.inspections.junit.malformed.annotated.method.param.single.descriptor": "''@{0}''(으)로 어노테이션이 지정된 <code>#ref</code> 메서드는 ''{1}'' 매개변수를 선언하지 않아야 합니다.",
  "jvm.inspections.junit.malformed.annotated.method.typed.param.single.descriptor": "''@{0}''(으)로 어노테이션이 지정된 <code>#ref</code> 메서드는 ''{1}'' 유형이어야 하며 ''{2}'' 매개변수를 선언하지 않아야 합니다.",
  "jvm.inspections.junit.malformed.annotated.method.single.param.single.descriptor": "''@{0}''(으)로 어노테이션이 지정된 <code>#ref</code> 메서드는 {1}이어야 하며 ''{2}'' 매개변수를 선언하지 않아야 합니다.",
  "jvm.inspections.junit.malformed.annotated.method.double.param.single.descriptor": "''@{0}''(으)로 어노테이션이 지정된 <code>#ref</code> 메서드는 {1}, {2}이어야 하며 ''{3}'' 매개변수를 선언하지 않아야 합니다.",
  "jvm.inspections.junit.malformed.annotated.method.single.typed.param.single.descriptor": "''@{0}''(으)로 어노테이션이 지정된 <code>#ref</code> 메서드는 {1}, ''{2}'' 유형이어야 하며 ''{3}'' 매개변수를 선언하지 않아야 합니다.",
  "jvm.inspections.junit.malformed.annotated.method.double.typed.param.single.descriptor": "''@{0}''(으)로 어노테이션이 지정된 <code>#ref</code> 메서드는 {1}, {2}, ''{3}'' 유형이어야 하며 ''{4}'' 매개변수를 선언하지 않아야 합니다.",
  "jvm.inspections.junit.malformed.annotated.method.param.double.descriptor": "''@{0}''(으)로 어노테이션이 지정된 <code>#ref</code> 메서드는 {1} 및 ''{2}'' 매개변수를 선언하지 않아야 합니다.",
  "jvm.inspections.junit.malformed.annotated.method.typed.param.double.descriptor": "''@{0}''(으)로 어노테이션이 지정된 <code>#ref</code> 메서드는 ''{1}'' 유형이어야 하며 {2} 및 ''{3}'' 매개변수를 선언하지 않아야 합니다.",
  "jvm.inspections.junit.malformed.annotated.method.single.param.double.descriptor": "''@{0}''(으)로 어노테이션이 지정된 <code>#ref</code> 메서드는 {1}이어야 하며 ''{2}'' 및 ''{3}'' 매개변수를 선언하지 않아야 합니다.",
  "jvm.inspections.junit.malformed.annotated.method.double.param.double.descriptor": "''@{0}''(으)로 어노테이션이 지정된 <code>#ref</code> 메서드는 {1}, {2}이어야 하며 ''{3}'' 및 ''{4}'' 매개변수를 선언하지 않아야 합니다.",
  "jvm.inspections.junit.malformed.annotated.method.single.typed.param.double.descriptor": "''@{0}''(으)로 어노테이션이 지정된 <code>#ref</code> 메서드는 {1}, ''{2}'' 유형이어야 하며 {3} 및 ''{4}'' 매개변수를 선언하지 않아야 합니다.",
  "jvm.inspections.junit.malformed.annotated.method.double.typed.param.double.descriptor": "''@{0}''(으)로 어노테이션이 지정된 <code>#ref</code> 메서드는 {1}, {2}, ''{3}'' 유형이어야 하며 {4} 및 ''{5}'' 매개변수를 선언하지 않아야 합니다.",
  "jvm.inspections.junit.malformed.annotated.suspend.function.descriptor": "''@{0}''(으)로 어노테이션이 지정된 <code>#ref</code> 메서드는 일시 중단 함수가 될 수 없습니다.",
  "jvm.inspections.junit.malformed.suspend.function.descriptor": "<code>#ref</code> 메서드는 일시 중단 함수가 될 수 없습니다.",
  "jvm.inspections.junit.malformed.test.combination.descriptor": "{0} 및 ''@{1}''의 의심스러운 조합",
  "jvm.inspections.junit.malformed.repetition.number.descriptor": "반복 횟수는 0보다 커야 합니다.",
  "jvm.inspections.junit.malformed.missing.nested.annotation.descriptor": "중첩 클래스의 테스트는 실행되지 않습니다.",
  "jvm.inspections.junit.malformed.extension.class.level.descriptor": "{0}은(는) 클래스 수준에서 등록되어야 합니다.",
  "jvm.inspections.junit.malformed.param.method.source.unresolved.descriptor": "대상 메서드 소스를 확인할 수 없음: ''{0}''",
  "jvm.inspections.junit.malformed.param.field.source.unresolved.descriptor": "대상 필드 소스를 확인할 수 없음: ''{0}''",
  "jvm.inspections.junit.malformed.param.wrapped.in.arguments.descriptor": "여러 매개변수는 'Arguments'로 래핑되어야 합니다.",
  "jvm.inspections.junit.malformed.param.method.source.return.type.descriptor": "메서드 소스 ''{0}''의 반환 유형은 다음 중 하나여야 합니다: ''Stream<?>'', ''Iterator<?>'', ''Iterable<?>'' 또는 ''Object[]''",
  "jvm.inspections.junit.malformed.param.method.source.no.params.descriptor": "메서드 소스 ''{0}''에는 매개변수가 없어야 합니다.",
  "jvm.inspections.junit.malformed.param.method.source.static.descriptor": "메서드 소스 ''{0}''은(는) static이어야 합니다.",
  "jvm.inspections.junit.malformed.param.field.source.static.descriptor": "필드 소스 ''{0}''은(는) static이어야 합니다.",
  "jvm.inspections.junit.malformed.param.field.source.return.type.descriptor": "필드 소스 ''{0}'' 유형은 Stream으로 변환할 수 있어야 합니다.",
  "jvm.inspections.junit.malformed.param.method.source.assignable.descriptor": "''{0}''을(를) ''{1}''(으)로 변환하기 위해 찾은 암시적 변환이 없습니다.",
  "jvm.inspections.junit.malformed.param.method.source.missing.name.descriptor": "@ParameterizedClass와 함께 @MethodSource를 사용할 때 메서드 이름을 지정해야 합니다.",
  "jvm.inspections.junit.malformed.param.duplicated.enum.descriptor": "중복된 'enum' 상수 이름",
  "jvm.inspections.junit.malformed.param.unresolved.enum.descriptor": "'enum' 상수 참조를 확인할 수 없습니다.",
  "jvm.inspections.junit.malformed.param.no.value.source.is.defined.descriptor": "정의된 값 소스가 없습니다.",
  "jvm.inspections.junit.malformed.param.exactly.one.type.of.input.must.be.provided.descriptor": "정확히 한 가지 유형의 입력이 제공되어야 합니다."
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

print(f"Updated {filename} (Keys 121-160)")

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
