import json

ko_dict = {
  "action.CacheResetOnProcessCanceledToggleAction.text": "ProcessCanceledException 발생 시 캐시 재설정",
  "action.HighlightingBenchmarkAction.text": "강조 표시(Highlighting) 벤치마크",
  "action.LocalCompletionBenchmarkAction.text": "로컬 시나리오",
  "action.TopLevelCompletionBenchmarkAction.text": "최상위(Top-Level) 시나리오",
  "group.KotlinCompletionBenchmarkGroup.text": "완성(Completion) 벤치마크",
  "group.KotlinInternalGroup.text": "Kotlin",
  "action.TestMoveRefactiringAction.text": "열린 프로젝트에서 이동 리팩터링 테스트",
  "group.KotlinRefactoringTesting.text": "Kotlin 리팩터링 테스트",
  "action.DumbModeTremble.text": "Dumb Mode 진동(Tremble)",
  "group.InternalKotlin.text": "Kotlin 내부 작업(Internal Actions)",
  "action.IntroduceProperty.text": "속성 도입(_R)\\u2026",
  "action.ExtractFunction.text": "함수 추출(_F)\\u2026",
  "action.ExtractFunction.command.completion.description": "선택한 코드 조각을 함수로 변환합니다.",
  "action.KotlinCodeMigrationToggle.text": "마이그레이션 감지 활성화",
  "action.KotlinCodeMigration.text": "코드 마이그레이션 실행",
  "action.CopyKotlinProjectInformation.text": "Kotlin 프로젝트 개요를 클립보드에 복사",
  "action.DecompileKotlinToJava.text": "Kotlin을 Java로 디컴파일",
  "action.KotlinConfigurePlugin.text": "Kotlin 플러그인 구성",
  "group.KotlinToolsGroup.text": "Kotlin",
  "action.ConvertJavaToKotlin.text": "Java 파일을 Kotlin 파일로 변환",
  "action.Kotlin.XDebugger.ToggleKotlinVariableView.text": "Kotlin 변수만 표시",
  "action.InspectBreakpointApplicability.text": "중단점 적용 가능성 검사",
  "action.ShowKotlinBytecode.text": "Kotlin 바이트코드 표시",
  "action.ConfigureKotlinInProject.text": "프로젝트에서 Kotlin 구성",
  "action.KotlinConsoleREPL.text": "Kotlin REPL(실험적)",
  "action.LibraryToSourceDependencySupportToggleAction.text": "라이브러리에서 소스로의 종속성 지원 전환",
  "inspection.unused.unary.operator.display.name": "사용되지 않는 단항 연산자",
  "inspection.incomplete.destructuring.declaration.display.name": "불완전한 구조 분해(destructuring) 선언",
  "inspection.inconsistent.comment.for.java.parameter.display.name": "Java 매개변수에 대한 일관성 없는 주석",
  "inspection.replace.guard.clause.with.function.call.display.name": "가드 절(Guard clause)을 Kotlin의 함수 호출로 바꿀 수 있습니다.",
  "inspection.lateinit.var.overrides.lateinit.var.display.name": "'lateinit var' 속성이 'lateinit var' 속성을 재정의합니다.",
  "inspection.kotlin.equals.between.inconvertible.types.display.name": "변환할 수 없는 유형의 객체 간 'equals()'",
  "inspection.redundant.empty.initializer.block.display.name": "중복되는 빈 초기화 블록",
  "inspection.add.operator.modifier.display.name": "함수에 'operator' 제어자가 있어야 합니다.",
  "inspection.control.flow.with.empty.body.display.name": "본문이 비어 있는 제어 흐름(Control flow)",
  "inspection.replace.java.static.method.with.kotlin.analog.display.name": "Java 메서드를 Kotlin 아날로그로 바꿔야 합니다.",
  "inspection.self.reference.constructor.parameter.display.name": "생성자를 완료할 수 없습니다.",
  "inspection.replace.not.null.assertion.with.elvis.return.display.name": "Not-null 어서션(assertion)을 'return'으로 바꿀 수 있습니다.",
  "inspection.kotlin.covariant.equals.display.name": "공변(Covariant) 'equals()'",
  "inspection.replace.associate.function.display.name": "'associate'를 'associateBy' 또는 'associateWith'로 바꿀 수 있습니다.",
  "inspection.java.map.for.each.display.name": "Java Map.forEach 메서드 호출을 Kotlin의 forEach로 바꿔야 합니다.",
  "inspection.kotlin.throwable.not.thrown.display.name": "Throwable이 발생하지 않음(not thrown)",
  "inspection.redundant.require.not.null.call.display.name": "중복되는 'requireNotNull' 또는 'checkNotNull' 호출",
  "inspection.replace.range.start.end.inclusive.with.first.last.display.name": "박스형(Boxed) 속성을 언박싱된(unboxed) 속성으로 바꿔야 합니다.",
  "inspection.redundant.enum.constructor.invocation.display.name": "중복되는 enum 생성자 호출",
  "inspection.redundant.labeled.return.on.last.expression.in.lambda.display.name": "람다의 마지막 표현식에 중복되는 레이블 지정 반환(return)",
  "inspection.replace.negated.is.empty.with.is.not.empty.display.name": "부정된(Negated) 호출을 간소화할 수 있습니다.",
  "inspection.function.with.lambda.expression.body.display.name": "'= { ... }' 및 유추된 반환 유형이 있는 함수",
  "inspection.suspend.function.on.coroutine.scope.display.name": "suspend 함수의 CoroutineScope 수신자로 인한 모호한 coroutineContext",
  "inspection.boolean.literal.argument.display.name": "매개변수 이름이 없는 부울 리터럴 인수"
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

print(f"Updated {filename} (Keys 1741-1790)")

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
