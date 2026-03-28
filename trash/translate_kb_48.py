import json

ko_dict = {
  "inspection.logger.placeholder.count.matches.argument.count.display.name": "로깅 호출에서 자리 표시자 수가 인수 수와 일치하지 않습니다.",
  "placeholder.count.matches.argument.count.more.problem.descriptor": "지정된 자리 표시자({1})보다 많은 인수({0})가 제공되었습니다. #loc",
  "placeholder.count.matches.argument.count.fewer.problem.descriptor": "지정된 자리 표시자({1})보다 적은 인수({0})가 제공되었습니다. #loc",
  "title.logger.factory.method.name": "로거 팩토리 메서드 이름",
  "title.logger.factory.class.name": "로거 팩토리 클래스 이름",
  "title.choose.logger.factory.class": "로거 팩토리 클래스 선택",
  "inspection.redundant.assequence.call": "중복되는 'asSequence' 호출",
  "remove.assequence.call.fix.text": "'asSequence' 호출 제거",
  "codestyle.layout.import.aliases.separately": "가져오기(import) 별칭 개별 배치",
  "button.add.package": "패키지 추가",
  "listbox.import.package": "패키지",
  "listbox.import.with.subpackages": "하위 패키지 포함",
  "title.import.layout": "가져오기(Import) 레이아웃",
  "title.packages.to.use.import.with": "'*'와 함께 Import를 사용할 패키지",
  "redundant.qualifier.unnecessary.non.direct.parent.class.qualifier": "불필요한 비직접적인(non-direct) 부모 클래스 한정자",
  "fix.add.exception.to.throws": "''{0}'' 추가",
  "fix.add.eq.eq.true": "'== true' 추가",
  "inspection.replace.isempty.with.ifempty.display.name": "'if' 조건을 람다 호출로 바꿀 수 있습니다.",
  "inspection.replace.with.ignore.case.equals.display.name": "'equals(..., ignoreCase = true)'로 바꿔야 합니다.",
  "inspection.redundant.nullable.return.type.display.name": "중복되는 null 허용 반환 유형",
  "0.always.returns.non.null.type": "''{0}''은(는) 항상 null이 아닌 유형을 반환합니다.",
  "0.is.always.non.null.type": "''{0}''은(는) 항상 null이 아닌 유형입니다.",
  "inspection.simplifiable.scope.function.display.name": "중첩된 forEach가 있는 범위(Scope) 함수를 간소화할 수 있습니다.",
  "nested.1.call.in.0.could.be.simplified.to.2": "''{0}''의 중첩된 ''{1}'' 호출을 {2}(으)로 간소화할 수 있습니다.",
  "evaluate.compile.time.expression": "컴파일 시간(compile-time) 표현식 평가",
  "reorder.parameters": "매개변수 순서 변경",
  "reorder.parameters.command": "매개변수 순서 변경",
  "analyzing.functions": "함수 분석 중\\u2026",
  "hints.title.codevision": "Code Vision",
  "hints.codevision.usages.format": "{0, choice, 1#1개 사용법|2#{0,number}개 사용법}",
  "hints.codevision.usages.too_many.format": "{0,number}+ 사용법",
  "hints.codevision.implementations.format": "{0, choice, 1#1개 구현|2#{0,number}개 구현}",
  "hints.codevision.implementations.too_many.format": "{0,number}+ 구현",
  "hints.codevision.inheritors.format": "{0, choice, 1#1개 상속자|2#{0,number}개 상속자}",
  "hints.codevision.inheritors.to_many.format": "{0,number}+ 상속자",
  "hints.codevision.overrides.format": "{0, choice, 1#1개 재정의|2#{0,number}개 재정의}",
  "hints.codevision.overrides.to_many.format": "{0,number}+ 재정의",
  "hints.codevision.settings": "설정\\u2026",
  "convert.string.template.to.build.string": "'buildString' 호출로 변환",
  "convert.concatenation.to.build.string": "연결을 'buildString' 호출로 변환",
  "convert.to.indexed.function.call": "색인된(indexed) 함수 호출로 변환",
  "convert.context.parameter.to.regular.parameter": "컨텍스트 매개변수를 값(value) 매개변수로 변환",
  "convert.context.parameter.to.regular.parameter.progress": "변환 중\\u2026",
  "convert.context.parameter.to.receiver.parameter": "컨텍스트 매개변수를 수신자로 변환",
  "convert.value.parameter.to.context.parameter": "값 매개변수를 컨텍스트 매개변수로 변환",
  "convert.receiver.parameter.to.context.parameter": "수신자를 컨텍스트 매개변수로 변환",
  "inspection.kotlin.invalid.bundle.or.property.display.name": "잘못된 속성 키",
  "inspection.gradle.kotlinx.coroutines.deprecation.display.name": "Gradle에서 호환되지 않는 kotlinx.coroutines 종속성이 Kotlin 1.3+와 함께 사용됩니다.",
  "inspection.deprecated.gradle.dependency.display.name": "Gradle에서 더 이상 사용되지 않는 라이브러리가 사용되었습니다.",
  "inspection.different.stdlib.gradle.version.display.name": "Kotlin 라이브러리와 Gradle 플러그인 버전이 다릅니다."
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

print(f"Updated {filename} (Keys 2041-2090)")

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
