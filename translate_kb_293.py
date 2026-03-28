import json

def update_json():
    file_path = "missing_translations/missing_keys_korean.json"
    target_file = "intellij/vcs-release/VcsBundle.properties"
    
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    translations = {
        "amend.commit.load.message.error.title": "커밋 메시지 로드 안 됨",
        "amend.commit.load.message.error.text": "수정할 커밋의 커밋 메시지를 로드할 수 없습니다.",
        "checkbox.amend": "수정(_M)",
        "label.by.author": "작성자:",
        "label.at.date.leading": "{0}에",
        "label.at.date.middle": "{0}에",
        "button.tooltip.remove.commit.author.date": "제거",
        "error.executing.commit": "''{0}'' 실행 중 오류 발생: {1}",
        "changes.action.rollback.title": "{0} 변경 사항",
        "changes.action.rollback.custom.title": "{0} 변경 사항",
        "changes.dialog.editchangelist.error.already.exists": "이름이 ''{0}''인 변경 목록이 이미 있습니다",
        "error.adding.files.prompt": "파일을 추가하는 중 다음 문제가 발생했습니다:",
        "error.adding.files.title": "파일 추가 실패",
        "error.adding.files.notification.title": "파일 추가 실패",
        "column.name.revision.list.committer": "사용자",
        "column.name.revision.list.number": "번호",
        "column.name.revision.list.description": "설명",
        "browse.changes.nothing.found": "조건과 일치하는 변경 사항을 찾을 수 없습니다",
        "browse.changes.nothing.found.title": "변경 사항 없음",
        "browse.changes.progress.title": "변경 사항 검색 중",
        "browse.changes.error.title": "변경 사항을 표시할 수 없음",
        "browse.changes.error.message": "VCS 액세스 문제: {0}",
        "button.search.again": "다시 검색",
        "browse.changes.filter.title": "검색 조건 지정",
        "changes.checkbox.delete.locally.added.files": "추가된 파일의 로컬 사본 삭제(&D)",
        "changes.action.rollback.text": "롤백",
        "patch.apply.file.name.field": "패치 파일 이름(&P):",
        "create.patch.commit.action.title": "패치 생성",
        "create.patch.commit.action.progress": "패치 생성 중\\u2026",
        "create.patch.error.title": "패치 생성 오류: {0}",
        "create.patch.settings.dialog.title": "패치 파일 설정",
        "button.apply.patch": "패치 적용",
        "patch.apply.dialog.title": "패치 적용",
        "patch.apply.notification.title": "패치 적용",
        "filetype.patch.description": "패치",
        "filetype.patch.display.name": "패치",
        "patch.apply.conflict.for.title": "{0}의 패치 충돌",
        "patch.apply.conflict.title": "패치 충돌",
        "patch.apply.conflict.local.version": "로컬 버전",
        "patch.apply.conflict.merged.version": "병합 결과",
        "patch.apply.conflict.patched.version": "패치된 버전",
        "patch.apply.conflict.patched.somehow.version": "결과",
        "patch.apply.conflict.patch": "패치",
        "patch.apply.select.title": "패치 파일 선택",
        "patch.apply.before.patch.label.text": "패치 이전",
        "patch.apply.after.patch.label.text": "패치 이후",
        "patch.apply.aborted.title": "패치 적용 중단됨",
        "patch.apply.aborted.message": "'패치 적용' 작업 중 변경된 모든 파일이 롤백되었습니다",
        "patch.apply.rollback.failed.title": "롤백 실패",
        "patch.apply.rollback.failed.message": "'로컬 히스토리' 대화상자를 사용하여 수동으로 복원을 시도하십시오."
    }
    
    file_found = False
    for file_obj in data['new_files']:
        if file_obj['file'] == target_file:
            file_obj['translations'].update(translations)
            file_found = True
            break
            
    if not file_found:
        data['new_files'].append({
            "file": target_file,
            "translations": translations
        })
        
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    update_json()