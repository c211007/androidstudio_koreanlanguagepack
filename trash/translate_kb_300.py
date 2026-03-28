import json

def update_json():
    file_path = "missing_translations/missing_keys_korean.json"
    target_file = "VcsBundle.properties"
    
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    translations = {
        "committed.changes.regex.title": "정규 표현식(&G)",
        "changelist.details.committed.format": "{0} {1}에 의해 커밋됨",
        "incoming.changes.indicator.tooltip": "수신되는 변경 목록 {0}개 사용 가능",
        "incoming.changes.indicator.name": "수신 변경 사항",
        "committed.changes.incorrect.regex.message": "필터에 사용된 정규 표현식이 잘못되었습니다",
        "committed.changes.empty.message": "리포지토리에 커밋된 변경 사항이 없습니다",
        "committed.changes.not.loaded.message": "리포지토리 변경 사항을 로드하려면 새로고침 버튼을 누르십시오",
        "incoming.changes.not.loaded.message": "수신 변경 사항을 로드하려면 새로고침 버튼을 누르십시오",
        "incoming.changes.empty.message": "수신 변경 사항이 없습니다",
        "show.history.action.name.template": "{0}의 히스토리 표시(_F)\\u2026",
        "show.history.dialog.title.template": "{0}의 히스토리",
        "action.name.show.history.for.selection": "선택 영역",
        "action.name.show.history.for.class": "클래스",
        "action.name.show.history.for.field": "필드",
        "action.name.show.history.for.method": "메서드",
        "action.name.show.history.for.function": "함수",
        "action.name.show.history.for.code.block": "코드 블록",
        "action.name.show.history.for.statement": "문",
        "open.repository.version.text": "리포지토리 버전 열기",
        "open.repository.version.description": "파일의 선택된 리비전이 있는 편집기 열기",
        "edit.source.action.text": "소스 편집",
        "local.history.update.from.vcs": "VCS에서 업데이트",
        "unshelve.changes.dialog.title": "변경 사항 보류 해제",
        "unshelve.changes.progress.title": "변경 사항 보류 해제 중\\u2026",
        "shelved.version.name": "보류된 버전",
        "patched.version.name": "패치된 버전",
        "local.version.title": "로컬 버전",
        "change.file.renamed.from.text": "- {0}에서 이름 변경됨",
        "change.file.moved.from.text": "- {0}에서 이동됨",
        "change.file.copied.from.text": "- {0}에서 복사됨",
        "change.file.replaced.text": "- 교체됨",
        "change.file.renamed.to.text": "- {0}(으)로 이름 변경됨",
        "change.file.moved.to.text": "- {0}(으)로 이동됨",
        "cannot.create.directory.for.patch": "파일을 생성할 수 없습니다: {0}. {1}",
        "cannot.find.file.to.patch": "패치할 파일을 찾을 수 없습니다: {0}",
        "cannot.apply.file.already.exists": "{0} 파일에 패치를 적용할 수 없습니다. 파일이 이미 존재합니다.",
        "change.lists.manager.add.unversioned": "버전 관리되지 않는 파일 추가",
        "vcs.shelf.action.restore.text": "복원",
        "vcs.shelf.action.restore.description": "최근에 삭제된 {0, choice, 1#변경 목록을|2#변경 목록을} 복원합니다",
        "vcs.shelf.move.text": "선반을 새 위치로 이동(&M)",
        "vcs.shelf.store.base.content": "분산 버전 제어 시스템에서 파일의 기본 리비전을 보류합니다.",
        "vcs.shelving.changes": "변경 사항 보류 중\\u2026",
        "vcs.unshelving.changes": "변경 사항 보류 해제 중\\u2026",
        "vcs.unshelving.conflict.left": "커밋되지 않은 변경 사항",
        "vcs.unshelving.conflict.right": "원격의 변경 사항",
        "action.enable.version.control.integration.text": "버전 관리 통합 활성화(_E)\\u2026",
        "dialog.enable.version.control.integration.title": "버전 관리 통합 활성화",
        "dialog.enable.version.control.integration.select.vcs.label.text": "{0}과(와) 연결할 버전 제어 시스템을 선택하십시오:",
        "dialog.enable.version.control.integration.hint.text": "버전 관리 설정은 다음에서 구성할 수 있습니다: ",
        "confirmation.title.add.file.to": "{0}에 파일을 추가하시겠습니까?"
    }
    
    file_found = False
    for file_obj in data['new_files']:
        if file_obj['filename'] == target_file:
            file_obj['keys'].update(translations)
            file_found = True
            break
            
    if not file_found:
        data['new_files'].append({
            "filename": target_file,
            "keys": translations
        })
        
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    update_json()