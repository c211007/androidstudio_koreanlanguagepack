import json

ko_dict = {
  "inspection.different.kotlin.gradle.version.display.name": "Kotlin Gradle과 IDE 플러그인 버전이 다릅니다.",
  "inspection.maven.coroutines.deprecation.display.name": "Maven에서 호환되지 않는 kotlinx.coroutines 종속성이 Kotlin 1.3+와 함께 사용됩니다.",
  "inspection.deprecated.maven.dependency.display.name": "Maven에서 더 이상 사용되지 않는 라이브러리가 사용되었습니다.",
  "inspection.different.kotlin.maven.version.display.name": "Maven과 IDE 플러그인 버전이 다릅니다.",
  "inspection.different.maven.stdlib.version.display.name": "라이브러리와 Maven 플러그인 버전이 다릅니다.",
  "inspection.kotlin.test.j.unit.display.name": "kotlin-test-junit을 사용할 수 있습니다.",
  "inspection.kotlin.maven.plugin.phase.display.name": "Kotlin Maven 플러그인이 잘못 구성되었습니다.",
  "action.KotlinGenerateMavenPluginAction.text": "Kotlin 플러그인",
  "action.KotlinGenerateMavenTestCompileExecutionAction.text": "Kotlin 테스트 컴파일 실행",
  "action.KotlinGenerateMavenCompileExecutionAction.text": "Kotlin 컴파일 실행",
  "dialog.message.incorrect.target.path.directory.not.specified": "잘못된 대상 경로입니다. 디렉터리가 지정되지 않았습니다.",
  "dialog.message.none.elements.were.selected": "선택된 요소가 없습니다.",
  "a.field.without.an.initializer.is.not.yet.supported": "초기화자가 없는 필드는 아직 지원되지 않습니다.",
  "a.constructor.call.is.not.yet.supported": "생성자 호출은 아직 지원되지 않습니다.",
  "failed.to.create.a.wrapper.for.inlining.to.kotlin": "Kotlin으로 인라이닝(inlining)하기 위한 래퍼(wrapper)를 만들지 못했습니다.",
  "inspection.unused.result.of.data.class.copy": "데이터 클래스 복사의 사용되지 않는 결과",
  "unclear.precedence.of.binary.expression.inspection.display.name": "서로 다른 우선순위를 가진 여러 연산자",
  "unclear.precedence.of.binary.expression.inspection": "표현식에 명확성을 위한 괄호를 사용해야 합니다.",
  "unclear.precedence.of.binary.expression.quickfix": "명확성을 위해 괄호 추가",
  "unclear.precedence.of.binary.expression.report.even.obvious.cases.checkbox": "명백한 경우에도 보고",
  "replace.function.call.with.if": "함수 호출을 'if'로 바꾸기",
  "lift.function.call.out.of.if": "'if' 밖으로 함수 호출 리프트(Lift)",
  "replace.function.call.with.when": "함수 호출을 'when'으로 바꾸기",
  "lift.function.call.out.of.when": "'when' 밖으로 함수 호출 리프트(Lift)",
  "replace.function.call.with.the.opposite": "반대되는 함수 호출로 바꾸기",
  "replace.0.with.1.and.vice.versa": "''{0}''을(를) ''{1}''(으)로 바꾸기 및 그 반대",
  "inspection.kotlin.constant.conditions.display.name": "상수 조건",
  "inspection.message.value.always.true": "''{0}''의 값은 항상 true입니다.",
  "inspection.message.value.always.false": "''{0}''의 값은 항상 false입니다.",
  "inspection.message.condition.always.true": "''{0}'' 조건은 항상 true입니다.",
  "inspection.message.condition.always.false": "''{0}'' 조건은 항상 false입니다.",
  "inspection.message.condition.always.true.when.reached": "도달했을 때 ''{0}'' 조건은 항상 true입니다.",
  "inspection.message.condition.always.false.when.reached": "도달했을 때 ''{0}'' 조건은 항상 false입니다.",
  "inspection.message.value.always.zero": "''{0}''의 값은 항상 0입니다.",
  "inspection.message.value.always.null": "''{0}''의 값은 항상 null입니다.",
  "inspection.kotlin.result.of.filterIsInstance.call.always.empty.collection": "'filterIsInstance' 호출의 결과는 항상 빈 컬렉션입니다.",
  "inspection.message.result.of.0.always.empty.collection": "''{0}''의 결과는 항상 빈 컬렉션입니다.",
  "inspection.message.when.condition.always.false": "'when' 분기에 결코 도달할 수 없습니다.",
  "inspection.message.cast.will.always.fail": "캐스트는 항상 실패합니다.",
  "inspection.message.nonnull.cast.will.always.fail": "피연산자가 항상 null이므로 작업은 항상 실패합니다.",
  "inspection.message.index.out.of.bounds": "인덱스가 항상 범위를 벗어납니다.",
  "inspection.message.for.never.visited": "'for' 범위가 항상 비어 있습니다.",
  "floating.point.literal.precision.inspection.display.name": "부동 소수점 리터럴이 사용 가능한 정밀도를 초과합니다.",
  "floating.point.literal.precision.inspection": "부동 소수점 리터럴을 필요한 정밀도로 나타낼 수 없습니다.",
  "inspection.replace.mapIndexed.with.list.generator.display.name": "'mapIndexed'를 List 생성기로 바꾸기",
  "should.be.replaced.with.list.generator": "List 생성기로 바꿔야 합니다.",
  "replace.with.list.generator.fix.text": "List 생성기로 바꾸기",
  "inspection.java.io.serializable.object.must.have.read.resolve.display.name": "직렬화 가능한 객체는 'readResolve'를 구현해야 합니다.",
  "inspection.java.io.serializable.object.must.have.read.resolve.warning": "직렬화 가능한 객체는 'readResolve'를 구현해야 합니다.",
  "inspection.java.io.serializable.object.must.have.read.resolve.quick.fix.name": "'readResolve' 구현"
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

print(f"Updated {filename} (Keys 2091-2140)")

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
