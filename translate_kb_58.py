import json
from pathlib import Path

def update_missing_keys():
    file_path = Path("missing_translations/missing_keys_korean.json")
    
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    ko_dict = {
        "coroutine.dump.panel.title": "코루틴 덤프",
        "coroutine.dump.filter.field": "필터:",
        "coroutine.dump.filter.action": "필터",
        "coroutine.dump.filter.description": "특정 문자열이 포함된 코루틴만 표시",
        "coroutine.dump.merge.action": "동일한 스택 추적 병합",
        "coroutine.dump.merge.description": "동일한 스택 추적을 가진 코루틴 그룹화",
        "coroutine.dump.copy.action": "클립보드에 복사",
        "coroutine.dump.copy.description": "전체 코루틴 덤프를 클립보드에 복사",  
        "coroutine.dump.failed": "코루틴 덤프에 실패했습니다. 로그를 확인하세요.",
        "coroutine.dump.full.title": "전체 코루틴 덤프",
        "coroutine.dump.full.copied": "전체 코루틴 덤프가 클립보드에 성공적으로 복사되었습니다.",
        "coroutine.dump.creation.trace": "코루틴 생성 스택 추적",
        "coroutine.dump.threads.loading": "로드 중\\u2026",
        "coroutine.view.node.root": "코루틴",
        "coroutine.view.node.dispatchers": "디스패처(Dispatchers)",
        "coroutine.view.node.jobs": "코루틴 계층 구조",
        "coroutine.view.title": "코루틴",
        "coroutine.view.dispatcher.empty": "빈 디스패처",
        "coroutine.view.fetching.error": "정보를 가져오는 중 오류가 발생했습니다.", 
        "coroutine.view.fetching.not_found": "코루틴 정보를 찾을 수 없습니다.",        
        "optimised.variable.message": "{0}이(가) 최적화되어 제거되었습니다.",
        "to.enable.information.breakpoint.suspend.policy.should.be.set.to.all.threads": "정보 중단점을 활성화하려면 일시 중단 정책을 '모두(All)' 스레드로 설정해야 합니다.",
        "dump.item.coroutine.tooltip": "코루틴"
    }
    
    filename = "KotlinDebuggerCoroutinesBundle.properties"
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
