import json

ko_dict = {
  "predefined.configuration.comments.containing.word": "특정 단어가 포함된 주석",
  "predefined.configuration.do.while": "Do...while 루프",
  "predefined.configuration.elvis": "Elvis 연산자",
  "predefined.configuration.for": "For 루프",
  "predefined.configuration.function.annotation": "주석이 포함된 함수",
  "predefined.configuration.function.signature": "함수 서명",
  "predefined.configuration.function.explicit.inferred.type": "명시적 및 유추된 유형",
  "predefined.configuration.ifs": "If 문",
  "predefined.configuration.instance": "인스턴스",
  "predefined.configuration.kdoc.tag": "KDoc 태그",
  "predefined.configuration.lambda": "람다 표현식",
  "predefined.configuration.method.calls": "메서드 호출",
  "predefined.configuration.companion.object.method.calls": "companion object의 메서드 호출",
  "predefined.configuration.properties.getter": "명시적 getter가 있는 속성",
  "predefined.configuration.safe.call.operator": "안전한 호출(Safe call) 연산자",
  "predefined.configuration.string.literals": "문자열 리터럴",
  "predefined.configuration.strings": "문자열",
  "predefined.configuration.strings.with.long.template": "긴 템플릿이 포함된 문자열",
  "predefined.configuration.trys": "Try 문",
  "predefined.configuration.vars.of.given.type": "지정된 유형의 변수",
  "predefined.configuration.also.match.vals": "var 및 val 모두 일치",
  "predefined.configuration.when": "When 표현식",
  "predefined.configuration.while": "While 루프",
  "action.Kotlin.StopScratch.text": "스크래치 실행 중지",
  "action.Kotlin.StopScratch.description": "스크래치 실행 중지",
  "action.Kotlin.ClearScratch.text": "Kotlin 스크래치 지우기",
  "action.Kotlin.ClearScratch.description": "Kotlin 스크래치 지우기",
  "action.Kotlin.RunScratch.text": "Kotlin 스크래치 실행",
  "action.Kotlin.RunScratch.description": "Kotlin 스크래치 실행",
  "action.KotlinGenerateToString.text": "toString()",
  "action.KtAddToExcludeListAction.text": "현재 메서드에 대한 힌트 표시 안 함",
  "action.KotlinGenerateEqualsAndHashCode.text": "equals() 및 hashCode()",
  "action.KotlinGenerateSecondaryConstructor.text": "보조 생성자",
  "action.KotlinGenerateDataMethod.text": "매개변수 함수",
  "action.KotlinGenerateTearDownMethod.text": "TearDown 함수",
  "action.KotlinGenerateSetUpMethod.text": "SetUp 함수",
  "action.KotlinGenerateTestMethod.text": "테스트 함수",
  "action.KotlinShellExecute.text": "Kotlin 코드 실행",
  "action.KotlinShellExecute.description": "콘솔에서 Kotlin 코드 실행",
  "action.IntroduceTypeAlias.text": "유형 별칭(Type Alias) 도입(_A)\\u2026",
  "action.ShortenSelectionAction.text": "선택 영역 줄이기",
  "action.IntroduceTypeParameter.text": "유형 매개변수 도입(_Y)\\u2026",
  "action.ExtractFunctionToScope.text": "함수를 Scope로 추출(_S)\\u2026",
  "action.KotlinThrowException.text": "Kotlin 플러그인에서 오류 발생(Drop)",
  "action.KotlinFormattingSettingsStatusAction.text": "포맷터 설정 정보",
  "action.CopyAsDiagnosticTest.text": "현재 파일을 진단 테스트로 복사",
  "action.StoredExceptionsThrowToggleAction.text": "캐시된 PCE 예외 던지기",
  "action.PrintOutNotPropertyMatches.text": "Not 속성 후보 검색",
  "action.FindImplicitNothingAction.text": "암시적 Nothing 호출 찾기",
  "action.CheckComponentsUsageSearchAction.text": "구성 요소(Component) 함수 사용법 검색 확인"
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

print(f"Updated {filename} (Keys 1691-1740)")

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
