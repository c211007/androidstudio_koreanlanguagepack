import json

ko_dict = {
  "inspection.trailing.comma.add.line.break": "줄바꿈 추가",
  "inspection.trailing.comma.missing.line.break": "줄바꿈 누락됨",
  "inspection.trailing.comma.remove.trailing.comma": "후행 쉼표 제거",
  "inspection.trailing.comma.redundant.trailing.comma": "중복되는 후행 쉼표",
  "inspection.trailing.comma.add.trailing.comma": "후행 쉼표 추가",
  "inspection.trailing.comma.missing.trailing.comma": "후행 쉼표 누락됨",
  "inspection.trailing.comma.fix.comma.position": "쉼표 위치 수정",
  "inspection.trailing.comma.comma.loses.the.advantages.in.this.position": "이 위치에서는 쉼표의 장점이 사라집니다.",
  "inspection.redundant.label.text": "중복되는 레이블",
  "inspection.context.parameters.migration.display.text": "지원되지 않는 컨텍스트 수신자(context receivers) 사용됨",
  "inspection.context.parameters.migration.problem.description": "컨텍스트 수신자는 컨텍스트 매개변수로 바꿔야 합니다.",
  "inspection.context.parameters.migration.quick.fix.text": "컨텍스트 수신자를 컨텍스트 매개변수로 바꾸기",
  "inspection.add.annotation.target.problem.description": "주석은 매개변수에만 적용됩니다. 명시적인 주석 사용 지점 대상을 지정하는 것이 권장됩니다.",
  "intention.convert.lambda.line": "{0,choice,0#한|1#여러} 줄 람다로 변환",
  "intention.trailing.comma.custom.text": "포맷터에서 기본적으로 후행 쉼표를 {0,choice,0#활성화|1#비활성화}",
  "intention.trailing.comma.text": "포맷터에서 후행 쉼표 활성화/비활성화",
  "intention.name.specify.supertype": "상위 유형(supertype) 지정",
  "intention.name.specify.supertype.title": "상위 유형 지정",
  "popup.title.choose.supertype": "상위 유형 선택",
  "fix.remove.argument.text": "인수 제거",
  "fix.remove.redundant.star.text": "중복되는 * 제거",
  "refactoring.extract.to.separate.file.text": "별도의 파일로 추출",
  "action.usage.update.command": "사용법 업데이트",
  "progress.title.analyze.extraction.data": "추출 데이터 분석 중\\u2026",
  "fix.move.file.to.package.dir.name.text": "소스 루트",
  "move.refactoring.error.text.cannot.perform.refactoring.since.the.following.files.already.exist": "다음 파일이 이미 존재하므로 리팩터링을 수행할 수 없습니다:\\n\\n",
  "kotlin.script.definitions.title": "스크립트 정의 관리:",
  "kotlin.script.definitions.model.name.autoReloadScriptDependencies.description": "파일 변경 시 스크립트 구성을 자동으로 로드하려면 자동 새로고침을 활성화하세요.",
  "kotlin.script.definitions.model.name.autoReloadScriptDependencies": "자동 새로고침(Auto Reload)",
  "kotlin.script.definitions.model.name.is.enabled": "활성화됨",
  "kotlin.script.definitions.model.name.pattern.extension": "패턴/확장자",
  "kotlin.script.definitions.model.name.name": "이름",
  "kotlin.script.lookup.definitions": "Kotlin 스크립트 정의 찾는 중\\u2026",
  "kotlin.script.in.project.sources": "<html>이 스크립트는 소스 루트 내부에 있으면 안 됩니다. Kotlin 1.9 이후에는 모듈 컴파일 중에 무시됩니다.</html>",
  "kotlin.script.in.project.sources.1.9": "<html>이 스크립트는 소스 루트 내부에 있으면 안 됩니다. Kotlin 1.9부터는 모듈 컴파일 중에 무시됩니다.</html>",
  "kotlin.script.warning.more.info": "추가 정보",
  "kotlin.script.in.project.sources.hide": "숨기기",
  "kotlin.script.in.project.sources.later": "나중에 결정",
  "kotlin.script.in.project.sources.move": "이동\\u2026",
  "kotlin.script.in.project.sources.allow": "허용\\u2026",
  "kotlin.script.in.project.sources.link": "https://youtrack.jetbrains.com/issue/KT-52735",
  "kotlin.script.in.beta.stage": "Kotlin 스크립팅이 이제 베타 단계입니다.",
  "kotlin.script.in.beta.stage.link": "https://kotlinlang.org/docs/components-stability.html#stability-levels-explained",
  "codestyle.name.kotlin": "Kotlin",
  "add.missing.class.keyword": "누락된 'class' 키워드 추가",
  "fix.move.typealias.to.top.level": "typealias를 최상위(top level)로 이동",
  "fix.change.jvm.name": "JVM 이름 변경",
  "expand.boolean.expression.to.if.else": "부울 표현식을 'if else'로 확장",
  "inspection.logger.initialized.with.foreign.class.display.name": "외부(foreign) 클래스로 초기화된 로거",
  "logger.initialized.with.foreign.class": "''{0}'' 외부 클래스로 초기화된 로거"
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

print(f"Updated {filename} (Keys 1941-1990)")

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
