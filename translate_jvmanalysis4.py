import json

ko_dict = {
  "jvm.inspections.source.unsafe.to.sink.flow.check.warn.if.complex.comment": "복잡성으로 인해 확인할 수 없는 객체 보고",
  "jvm.inspections.source.unsafe.to.sink.flow.check.private.methods": "프라이빗 메서드의 매개변수를 안전한 것으로 간주",
  "jvm.inspections.source.unsafe.to.sink.flow.check.private.methods.comment": "활성화된 경우 프라이빗 메서드의 매개변수는 안전한 것으로 간주되며, 그렇지 않으면 알 수 없는 것으로 간주됩니다.",
  "jvm.inspections.source.unsafe.to.sink.flow.checked.types": "확인된 유형:",
  "jvm.inspections.source.unsafe.to.sink.flow.depth.inside": "메서드 내부의 분석 깊이:",
  "jvm.inspections.testonly.display.name": "프로덕션 코드에서 테스트 전용으로 사용",
  "jvm.inspections.testonly.class.reference": "프로덕션 코드에서 테스트 전용 클래스가 참조되었습니다.",
  "jvm.inspections.testonly.field.reference": "프로덕션 코드에서 테스트 전용 필드가 참조되었습니다.",
  "jvm.inspections.testonly.method.call": "프로덕션 코드에서 테스트 전용 메서드가 호출되었습니다.",
  "jvm.inspections.testonly.visiblefortesting": "@VisibleForTesting은 @TestOnly 코드에서 거의 의미가 없습니다.",
  "jvm.inspections.test.method.without.assertion.display.name": "어설션이 없는 테스트 메서드",
  "jvm.inspections.test.method.without.assertion.problem.descriptor": "테스트 메서드 <code>#ref()</code>에 어설션이 없습니다 #loc",
  "jvm.inspections.test.case.without.test.methods.display.name": "테스트가 없는 테스트 클래스",
  "jvm.inspections.test.case.without.test.methods.option": "테스트 메서드가 포함된 상위 클래스가 있는 테스트 케이스 무시",
  "jvm.inspections.test.case.without.test.methods.problem.descriptor": "테스트 클래스 <code>#ref</code>에 테스트가 없습니다 #loc",
  "jvm.inspections.test.case.with.constructor.display.name": "중요하지 않은 생성자가 있는 TestCase",
  "jvm.inspections.test.case.with.constructor.problem.descriptor": "'setup()' 수명 주기 메서드 대신 <code>#ref()</code> 생성자의 초기화 로직 #loc",
  "jvm.inspections.test.case.with.constructor.problem.descriptor.initializer": "'setup()' 수명 주기 메서드 대신 이니셜라이저의 초기화 로직",
  "jvm.inspections.test.case.in.product.source.display.name": "제품 소스의 테스트",
  "jvm.inspections.test.case.in.product.source.problem.descriptor": "테스트 케이스 <code>#ref</code>는 테스트 소스 트리에 배치해야 할 수 있습니다 #loc",
  "jvm.inspections.test.method.in.product.source.problem.descriptor": "테스트 메서드 <code>#ref()</code>는 테스트 소스 트리에 배치해야 할 수 있습니다 #loc",
  "jvm.inspection.logging.string.template.as.argument.display.name": "로깅 호출의 인수로 제공되는 문자열 템플릿",
  "jvm.inspection.logging.string.template.as.argument.problem.descriptor": "<code>#ref()</code> 로깅 호출의 인수로 제공되는 문자열 템플릿 #loc",
  "jvm.inspection.logging.string.template.as.argument.quickfix.name": "자리 표시자로 교체",
  "jvm.inspection.logging.string.template.as.argument.skip.on.primitives": "원시 유형, 해당 래퍼 또는 String만 있는 표현식이 포함된 경우 경고 안 함",
  "jvm.inspection.logging.string.template.as.argument.skip.on.only.exception": "메시지 인수 뒤에 예외만 인수로 호출하는 경우 경고가 표시되지 않습니다.",
  "jvm.inspection.logging.string.template.as.argument.warn.on.label": "경고 표시 조건:",
  "jvm.inspection.logging.string.template.as.argument.all.levels.option": "모든 로그 수준",
  "jvm.inspection.logging.string.template.as.argument.warn.level.and.lower.option": "경고 수준 이하",
  "jvm.inspection.logging.string.template.as.argument.info.level.and.lower.option": "정보 수준 이하",
  "jvm.inspection.logging.string.template.as.argument.debug.level.and.lower.option": "디버깅 수준 이하",
  "jvm.inspection.logging.string.template.as.argument.trace.level.option": "추적 수준",
  "jvm.inspection.log.statement.not.guarded.display.name": "로그 조건으로 보호되지 않은 로깅 호출",
  "jvm.inspection.log.statement.not.guarded.warn.on.label": "경고 대상:",
  "jvm.inspection.log.statement.not.guarded.all.levels.option": "모든 로그 수준",
  "jvm.inspection.log.statement.not.guarded.warn.level.and.lower.option": "경고 수준 및 그 이하",
  "jvm.inspection.log.statement.not.guarded.info.level.and.lower.option": "정보 수준 및 그 이하",
  "jvm.inspection.log.statement.not.guarded.debug.level.and.lower.option": "디버그 수준 및 그 이하",
  "jvm.inspection.log.statement.not.guarded.trace.level.option": "추적 수준",
  "jvm.inspection.log.statement.not.guarded.unguarded.constant.option": "상수 메시지로 보호되지 않은 로깅 호출 처리"
}

with open('missing_translations/missing_keys_korean.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

filename = "JvmAnalysisBundle.properties"
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
