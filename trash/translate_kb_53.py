import json
from pathlib import Path

def update_missing_keys():
    file_path = Path("missing_translations/missing_keys_korean.json")
    
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    ko_dict = {
        "notification.text.kotlin.js.compiler.body": "새로운 Kotlin/JS IR 컴파일러를 사용하여 애플리케이션의 번들 크기를 줄이고 TypeScript 정의(d.ts)를 자동 생성하세요.",
        "notification.text.kotlin.js.compiler.learn.more": "자세히 알아보기",
        "notification.text.kotlin.js.compiler.link": "https://kotl.in/jsirstable",    
        "find.usages.prepare.dialog.progress": "대화상자 준비",
        "replace.overloaded.operator.with.function.call": "오버로드된 연산자를 함수 호출로 바꾸기",
        "dialog.progress.collect.members.to.generate": "멤버 수집 중\\u2026",      
        "progress.title.collect.members.to.generate": "멤버 수집 중\\u2026",       
        "group.advanced.settings.kotlin": "Kotlin",
        "advanced.setting.kotlin.mpp.experimental": "실험적 멀티플랫폼 IDE 기능 활성화",
        "advanced.setting.kotlin.mpp.experimental.description": "IDE 재시작 필요",
        "dialog.title.resolving.inheritable.status": "상속 가능 상태 확인 중\\u2026",
        "inspection.join.declaration.and.assignment.option.report.with.complex.initialization.of.member.properties": "멤버 프로퍼티의 복잡한 초기화와 함께 보고",
        "goto.related.provider.in.module.0": "(모듈 {0})",
        "progress.title.searching.for.expected.actual": "expect/actual 검색 중\\u2026",
        "button.rename.current": "현재 이름 바꾸기",
        "button.rename.base": "기본 이름 바꾸기",
        "progress.title.calculate.occurrences": "발생 횟수 계산 중\\u2026",       
        "progress.title.check.for.conflicts": "충돌 확인 중\\u2026",
        "checkbox.collapse.to.expression.body": "표현식 본문으로 축소",        
        "inspection.runblocking.analysis.found.runblocking": "--> runBlocking",       
        "inspection.runblocking.analysis.graphbuilding.progress": "{0} 처리 중",   
        "inspection.runblocking.presentation.text": "코루틴에서 호출된 RunBlocking 빌더",
        "inspection.runblocking.presentation.settings.exploration.title": "오버라이드된 함수 탐색",
        "inspection.runblocking.presentation.settings.exploration.option.strict": "아니요",
        "inspection.runblocking.presentation.settings.exploration.option.declaration": "예 (오버라이드 제외)",
        "inspection.runblocking.presentation.settings.exploration.option.all": "예 (오버라이드 포함)",
        "inspection.runblocking.presentation.descriptor": "runBlocking 분석:",   
        "inspection.runblocking.presentation.display.name": "코루틴의 RunBlocking",
        "inspection.redundant.label.display.name": "불필요한 레이블",
        "inspection.redundant.label.problem.description": "레이블은 'break', 'continue' 또는 'return' 표현식에서 참조할 수 없으므로 불필요합니다.", 
        "group.names.coroutine": "코루틴 검사",
        "dialog.title.build.super.types.hierarchy": "{0}에 대한 상위 타입 계층 구조 구축",
        "progress.title.converting.to.if.then.else.expression": "if-then-else 표현식으로 변환 중\\u2026",
        "progress.title.introducing.value.for.condition": "조건에 대한 값 도입 중\\u2026",
        "inspection.kotlin.options.to.compiler.options.display.name": "더 이상 사용되지 않는 'kotlinOptions' DSL 사용",
        "replace.kotlin.options.with.compiler.options": "'kotlinOptions'를 'compilerOptions'로 바꾸기",
        "intention.implement.abstract.method.searching.for.descendants.progress": "하위 요소 검색 중\\u2026",
        "intention.implement.abstract.method.command.name": "메서드 구현",       
        "inspection.java.default.methods.not.overridden.by.delegation.display.name": "Java 기본 메서드가 위임을 통해 오버라이드되지 않음",
        "inspection.java.default.methods.not.overridden.by.delegation.message": "Java 기본 메서드가 위임을 통해 오버라이드되지 않았습니다.",
        "override.java.default.methods.delegate.fix.text": "위임 객체에 대한 위임을 통해 Java 기본 메서드 오버라이드",
        "override.java.default.methods.superclass.fix.text": "상위 클래스에 대한 명시적 위임을 통해 Java 기본 메서드 오버라이드",
        "override.accessor.functions.instead": "대신 접근자 함수 오버라이드", 
        "make.override.accessor.function.0": "접근자 함수 ''{0}'' 오버라이드 만들기",
        "inspection.run.blocking.in.suspend.function.display.name": "일시 중단 함수 내부의 'runBlocking'",
        "inspection.run.blocking.in.suspend.function.description": "일시 중단 함수 내부에서 'runBlocking'을 사용하면 호출 스레드가 차단되고 비동기 프로그래밍의 목적이 무산됩니다.",
        "inspection.suspicious.implicit.coroutine.scope.receiver.display.name": "의심스러운 암시적 'CoroutineScope' 수신자 액세스",
        "inspection.suspicious.implicit.coroutine.scope.receiver.description": "일시 중단 컨텍스트에서 의심스러운 암시적 'CoroutineScope' 수신자 액세스",
        "inspection.suspicious.implicit.coroutine.scope.receiver.detect.subclasses.option": "'CoroutineScope' 하위 타입의 수신자 감지",
        "inspection.suspicious.implicit.coroutine.scope.receiver.add.explicit.receiver.fix.text": "명시적인 레이블이 지정된 수신자 추가 (의미(Semantics)는 변경되지 않음)"
    }
    
    filename = "KotlinBundle.properties"
    found = False
    for file_entry in data.get('new_files', []):
        if file_entry['filename'] == filename:
            file_entry['keys'].update(ko_dict)
            found = True
            break
    if not found:
        data.setdefault('new_files', []).append({"filename": filename, "keys": ko_dict})
    
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        
    print(f"Updated KotlinBundle.properties (Keys 2241-2290)")

if __name__ == "__main__":
    update_missing_keys()
