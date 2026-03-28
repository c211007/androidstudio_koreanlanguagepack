import json

ko_dict = {
  "jvm.inspection.log.statement.not.guarded.unguarded.constant.option.comment": "상수가 아닌 인수가 있는 로깅 호출뿐만 아니라 보호되지 않는 모든 로깅 호출을 처리합니다.",
  "jvm.inspection.log.statement.not.guarded.log.fix.family.name": "로깅 조건으로 감싸기",
  "jvm.inspection.log.statement.not.guarded.log.problem.descriptor": "로깅 조건으로 보호되지 않은 로깅 호출 #loc",
  "jvm.inspection.log.guarded.display.name": "로그 조건으로 보호된 로깅 호출",
  "jvm.inspection.log.guarded.warn.if.fix.possible": "수정이 가능한 경우에만 경고",
  "jvm.inspection.log.guarded.problem.descriptor": "대수 조건으로 보호된 로깅 호출 #loc",
  "jvm.inspection.log.guarded.fix.family.name": "로그 가드 조건 래핑 해제",
  "jvm.inspection.logging.placeholder.count.matches.argument.count.display.name": "로깅 호출에서 자리 표시자의 개수가 인수의 개수와 일치하지 않음",
  "jvm.inspection.logging.placeholder.count.matches.argument.count.more.problem.descriptor": "지정된 자리 표시자({1})보다 많은 인수({0})가 제공되었습니다 #loc",
  "jvm.inspection.logging.placeholder.count.matches.argument.count.fewer.problem.partial.descriptor": "지정된 자리 표시자(최소 {1})보다 적은 인수({0})가 제공되었습니다 #loc",
  "jvm.inspection.logging.placeholder.count.matches.argument.count.fewer.problem.descriptor": "지정된 자리 표시자({1})보다 적은 인수({0})가 제공되었습니다 #loc",
  "jvm.inspection.logging.placeholder.count.matches.argument.count.incorrect.problem.descriptor": "잘못된 형식 문자열 지정자입니다 #loc",
  "jvm.inspection.logging.placeholder.count.matches.argument.count.slf4j.throwable.option": "SLF4J에서 Log4j 2를 구현으로 사용",
  "jvm.inspection.logging.placeholder.count.matches.argument.count.slf4j.throwable.option.auto": "자동으로 확인",
  "jvm.inspection.logging.placeholder.count.matches.argument.count.slf4j.throwable.option.yes": "예",
  "jvm.inspection.logging.placeholder.count.matches.argument.count.slf4j.throwable.option.no": "아니요",
  "jvm.inspection.logging.similar.message.display.name": "구별할 수 없는 로깅 호출",
  "jvm.inspection.logging.similar.message.problem.descriptor": "유사한 로그 메시지",
  "jvm.inspection.logging.similar.message.problem.min.similar.length": "유사한 시퀀스의 최소 길이",
  "jvm.inspection.logging.similar.message.problem.skip.on.error": "`error` 로그 수준으로 호출 보고 안 함",
  "jvm.inspection.logging.condition.disagrees.with.log.statement.display.name": "로그 조건이 로깅 호출과 일치하지 않음",
  "jvm.inspection.logging.condition.disagrees.with.log.statement.problem.descriptor": "''{0}'' 조건의 수준이 ''{1}'' 로깅 호출의 수준과 일치하지 않습니다.",
  "jvm.inspection.logging.condition.disagrees.with.log.statement.fix.name": "{0, choice, 0#조건|1#호출}의 수준 변경",
  "jvm.inspection.logging.condition.disagrees.with.log.statement.fix.family.name": "로그 수준 변경",
  "action.find.similar.stack.call.methods.not.found": "유사한 클래스를 찾을 수 없습니다.",
  "jvm.inspection.test.failed.line.display.name": "테스트에서 실패한 줄",
  "jvm.inspections.thread.run.display.name": "'Thread.run()' 호출",
  "jvm.inspections.serializable.class.without.serialversionuid.display.name": "'serialVersionUID'가 없는 역직렬화 가능한 클래스",
  "jvm.inspections.serializable.class.without.serialversionuid.problem.descriptor": "<code>#ref</code>에서 'serialVersionUID' 필드를 정의하지 않습니다. #loc",
  "jvm.inspections.string.touppercase.tolowercase.without.locale.description": "국제화된 문자열을 사용하여 로케일을 지정하지 않고 <code>String.{0}()</code> 호출됨 #loc",
  "jvm.inspections.api.display.name": "구성된 언어 수준에서 사용할 수 없는 API의 사용",
  "assertequals.between.inconvertible.types.display.name": "변환할 수 없는 유형의 객체 간 'assertEquals()'",
  "jvm.inspections.1.5.problem.descriptor": "@since {0}+로 문서화된 API 사용",
  "jvm.inspections.1.5.problem.descriptor.preview": "@since {0}+로 문서화된 미리보기 API 사용",
  "jvm.inspections.1.7.problem.descriptor": "JDK {0}와(과)의 컴파일 문제를 일으키는 1.6 API 이후 일반화된 사용",
  "jvm.inspections.1.8.problem.descriptor": "기본 {0, choice, 0#|1#메서드가|2# 메서드가} 재정의되지 않았습니다. JDK {1}에서 컴파일 문제가 발생할 수 있습니다.",
  "jvm.inspections.1.8.problem.single.descriptor": "기본 메서드 ''{0}''이(가) 재정의되지 않았습니다. JDK {1}에서 컴파일 문제가 발생할 수 있습니다.",
  "jvm.inspections.assertequals.between.inconvertible.types.problem.descriptor": "변환할 수 없는 유형의 객체 ''{0}'' 및 ''{1}'' 간의 <code>#ref()</code> #loc",
  "jvm.inspections.assertnotsame.between.inconvertible.types.problem.descriptor": "중복 어설션: 호환되지 않는 유형 ''{0}'' 및 ''{1}''이(가) 비교되었습니다.",
  "jvm.inspections.assertnotequals.between.inconvertible.types.problem.descriptor": "중복 어설션일 수 있는 항목: 호환되지 않는 유형 ''{0}'' 및 ''{1}''이(가) 비교되었습니다."
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

print(f"Updated {filename} (Keys 161-200)")

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
