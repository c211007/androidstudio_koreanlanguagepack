import json
from pathlib import Path

def update_missing_keys():
    file_path = Path("missing_translations/missing_keys_korean.json")
    
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    ko_dict = {
        "inspection.map.await.on.collection.of.deferred.display.name": "단일 'awaitAll()' 대신 'Collection<Deferred>'에 대한 'map { it.await() }' 호출",
        "inspection.map.await.on.collection.of.deferred.description": "단일 'awaitAll()' 대신 'Collection<Deferred>'에 'map { it.await() }'를 사용했습니다.",       
        "inspection.map.await.on.collection.of.deferred.replace.with.awaitAll": "'awaitAll()'로 바꾸기",
        "inspection.foreach.join.on.collection.of.job.display.name": "단일 'joinAll()' 대신 'Collection<Job>'에 대한 'forEach { it.join() }' 호출",
        "inspection.foreach.join.on.collection.of.job.description": "단일 'joinAll()' 대신 'Collection<Job>'에 'forEach { it.join() }'를 사용했습니다.",
        "inspection.foreach.join.on.collection.of.job.replace.with.joinAll": "'joinAll()'로 바꾸기",
        "inspection.prefer.current.coroutine.context.to.coroutine.context.inspection.display.name": "모호할 수 있는 'kotlin.coroutine.coroutineContext' 사용",
        "inspection.prefer.current.coroutine.context.to.coroutine.context.inspection.description": "'kotlin.coroutine.coroutineContext'의 사용이 모호할 수 있습니다.",   
        "inspection.prefer.current.coroutine.context.to.coroutine.context.inspection.fix": "'currentCoroutineContext()'로 바꾸기",
        "inspection.coroutine.context.with.job.display.name": "'CoroutineContext'에 'Job' 요소가 포함될 수 있습니다.",
        "inspection.coroutine.context.with.job.description.cancellable": "''Job''이 있는 ''CoroutineContext''를 ''{0}'' 빌더에 전달하면 구조화된 동시성 위반을 초래할 수 있습니다.",
        "inspection.coroutine.context.with.job.description.non.cancellable": "''NonCancellable'' 객체는 ''{0}'' 빌더와 함께 사용해서는 안 되며, 구조화된 동시성을 위반합니다.",
        "inspection.suspend.coroutine.lacks.cancellation.guarantees.display.name": "'suspendCoroutine'에 취소 보장이 부족합니다.",
        "inspection.suspend.coroutine.lacks.cancellation.guarantees.description": "'suspendCoroutine'은 취소 보장이 부족합니다. 적절한 취소 지원을 위해 'kotlinx.coroutines.suspendCancellableCoroutine'을 사용하는 것이 좋습니다.",
        "inspection.suspend.coroutine.lacks.cancellation.guarantees.fix": "취소에 더 적합한 'suspendCancellableCoroutine'으로 바꾸기",
        "fix.replace.run.blocking.with.inline": "'runBlocking'을 인라인 코드로 바꾸기",
        "fix.replace.run.blocking.with.run": "'runBlocking'을 'run'으로 바꾸기",      
        "fix.replace.run.blocking.with.withContext": "'runBlocking'을 'withContext'로 바꾸기",
        "fix.replace.run.family": "'runBlocking'을 인라인 실행, 'withContext' 또는 'run'으로 바꾸기",
        "big.decimal.equals": "'BigDecimal'에서 'equals()'가 호출되었습니다.",
        "big.decimal.equals.problem.descriptor": "BigDecimal 값 간의 <code>#ref()</code>는 아마도 'compareTo()'여야 합니다 #loc",
        "kotlin.unreachable.code.display.name": "도달할 수 없는 코드",
        "inspection.unreachable.code": "도달할 수 없는 코드",
        "inspection.unreachable.code.remove.unreachable.code": "도달할 수 없는 코드 제거",
        "inspection.variable.is.never.read.display.name": "변수가 한 번도 읽히지 않음",   
        "variable.is.never.read": "변수 ''{0}''을(를) 한 번도 읽지 않았습니다.",
        "inspection.assigned.value.is.never.read.display.name": "할당된 값이 한 번도 읽히지 않음",
        "assigned.value.is.never.read": "할당된 값을 한 번도 읽지 않았습니다.",
        "inspection.variable.initializer.is.redundant.display.name": "변수 초기화자가 불필요함",
        "initializer.is.redundant": "초기화자가 불필요합니다.",
        "explicit.type.arguments.can.be.inferred": "명시적 타입 인수를 추론할 수 있습니다.",
        "add.qualifier": "링크 한정자 추가",
        "add.qualifier.command": "링크 한정자 추가",
        "kotlin.script.sources.not.yet.indexed": "프로젝트 시작 시간을 줄이기 위해 소스 파일이 인덱싱되지 않았습니다.",
        "kotlin.script.sources.index": "인덱스",
        "java.collection.is.parameterized.with.nullable.type": "Java 컬렉션 ''{0}''이(가) {1,choice,1#Null 허용 타입|2#Null 허용 타입}으로 매개변수화되었습니다.",
        "inspection.nullable.type.argument.in.java.collection.display.name": "Null을 지원하지 않는 Java 컬렉션의 Null 허용 타입 인수",
        "replace.nullable.type.with.non.nullable.family.name": "Null 허용 타입을 Null을 허용하지 않는 타입으로 바꾸기",
        "java.collections.to.process": "처리할 Java 컬렉션:",
        "inspection.ambiguous.actuals.display.name": "모호한 실제(Actual) 선언",
        "ambiguous.actuals.for.0": "{0}에 모듈 {1}에 호환되는 실제(Actual) 선언이 여러 개 있습니다.",
        "inspection.redundant.upper.bound.fix.text": "불필요한 상한 'Any?' 제거",
        "inspection.redundant.upper.bound.problem": "불필요한 상한 'Any?'",   
        "make.script.executable": "스크립트를 실행 가능하게 만들기",
        "script.not.executable.missing.execute.permission": "스크립트를 실행할 수 없습니다. 실행 권한이 없습니다."
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
        
    print(f"Updated KotlinBundle.properties (Keys 2291-2335)")

if __name__ == "__main__":
    update_missing_keys()
