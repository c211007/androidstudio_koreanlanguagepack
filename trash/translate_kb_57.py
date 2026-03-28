import json
from pathlib import Path

def update_missing_keys():
    file_path = Path("missing_translations/missing_keys_korean.json")
    
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    ko_dict = {
        "find.inline.calls.task.compute.names": "{0} 선언에 대한 클래스 이름 계산",
        "find.inline.calls.task.cancelled": "클래스 이름 계산이 중단되어 디버거가 {0}의 일부 실행을 건너뛸 수 있습니다.",
        "alternative.sources.notification.title": "{0} 파일에 대한 대체 소스 사용 가능",
        "alternative.sources.notification.hide": "숨기기",
        "function.breakpoint.tab.title": "Kotlin 함수 중단점",
        "function.breakpoint.description": "함수 중단점",
        "function.breakpoint.initialize": "함수 중단점 초기화",
        "line.breakpoint.tab.title": "Kotlin 줄 중단점",
        "filter.ignore.internal.classes": "Kotlin 런타임 라이브러리 구현 클래스로 한 단계씩 코드 실행(Step into) 안 함",
        "always.do.smart.step.into": "항상 스마트 한 단계씩 코드 실행 수행",
        "variables.disable.coroutine.agent.values": "코루틴 에이전트 연결",
        "variables.disable.coroutine.agent.tooltip": "Gradle 및 Java 실행 구성에 대해 코루틴 에이전트 연결",
        "stepping.over.inline": "인라인 건너뛰기",
        "message.class.has.no.properties": "클래스에 속성이 없습니다.",
        "message.variables.property.get": "... get()",
        "filters.text.inline.function.body": "인라인 함수 본문",
        "filters.text.inline.function.call.site": "인라인 함수 호출 위치",        
        "filters.title.navigate.to": "탐색 경로:",
        "configurable.name.kotlin": "Kotlin",
        "property.watchpoint.tab.title": "Kotlin 프로퍼티 감시점",
        "property.watchpoint.description": "프로퍼티 감시점",
        "property.watchpoint.property.name.initialization": "초기화 감시:",  
        "property.watchpoint.property.name.access": "접근 감시:",
        "property.watchpoint.property.name.modification": "수정 감시:",      
        "property.watchpoint.access": "프로퍼티 접근(&A)",
        "property.watchpoint.modification": "프로퍼티 수정(&M)",
        "property.watchpoint.initialization": "프로퍼티 초기화(&I)",
        "property.watchpoint.error.couldnt.find.0.class": "''{0}'' 클래스를 찾을 수 없습니다.",
        "property.watchpoint.properties.panel.option.pass.count": "통과 횟수(&P):",     
        "property.watchpoint.properties.panel.option.class.filters": "클래스 필터(&L):",
        "property.watchpoint.properties.panel.option.instance.filters": "인스턴스 필터(&I):",
        "property.watchpoint.properties.panel.panel.group.conditions": "필터",     
        "property.watchpoint.add.dialog.title": "프로퍼티 감시점 추가",
        "property.watchpoint.add.dialog.choose.owner.class.title": "프로퍼티 소유자 클래스 선택",
        "property.watchpoint.add.dialog.choose.owner.class.label": "클래스의 정규화된 이름(Fully qualified name):",
        "property.watchpoint.add.dialog.choose.property.label": "프로퍼티 이름:",     
        "property.watchpoint.add.dialog.chooser.title": "{0,choice, 0#클래스에 프로퍼티 없음|1#프로퍼티 선택}",
        "progress.title.kt.file.search": "디버거: Kotlin 파일 검색 중",       
        "progress.text.waiting.for.smart.mode": "프로젝트 분석이 완료될 때까지 대기 중",
        "stepping.filter.coroutine.name": "코루틴 {0}",
        "stepping.filter.several.coroutines.name": "코루틴 {0}개"
    }
    
    filename = "KotlinDebuggerCoreBundle.properties"
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
        
    print(f"Updated {filename}")

if __name__ == "__main__":
    update_missing_keys()
