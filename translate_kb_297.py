import json

def update_json():
    file_path = "missing_translations/missing_keys_korean.json"
    target_file = "VcsBundle.properties"
    
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    translations = {
        "shelve.delete.successful.message": "{0}{1,choice, 0#|1# 및 }{2}을(를) 선반에서 성공적으로 삭제했습니다",
        "shelve.undo.deletion": "선반 삭제 실행 취소",
        "shelve.recently.deleted.node": "최근 삭제됨",
        "shelve.changelist.not.found": "보류된 변경 목록 {0}을(를) 찾을 수 없습니다",
        "shelve.default.path.rendering": "<프로젝트 루트>",
        "shelve.copying.shelves.to.progress": "새 디렉터리로 선반 복사 중\\u2026",
        "shelve.moving.failed.prompt": "선반 이동에 실패했습니다.<br/>새 선반 디렉터리 경로를 사용하시겠습니까, 아니면 이전 경로로 복원하시겠습니까?",
        "shelve.error.title": "선반 오류",
        "shelve.use.new.directory.button": "새 경로 사용(&U)",
        "shelve.revert.moving.button": "복원(&R)",
        "shelve.import.to.progress": "처리 중 ",
        "shelve.delete.files.from.changelist.error": "{0}에서 파일을 삭제할 수 없습니다",
        "shelve.failed.title": "보류 실패",
        "shelve.failed.message": "{0,choice,1#변경 목록|2#변경 목록} [{1}]의 변경 사항을 보류하지 못했습니다",
        "shelve.successful.message": "변경 사항이 성공적으로 보류되었습니다",
        "shelve.loading.patch.error": "패치 파일을 로드할 수 없습니다: {0}",
        "unshelve.loading.patch.error": "패치를 로드할 수 없습니다: {0}",
        "unshelve.changes.action": "변경 사항 보류 해제",
        "patch.apply.already.applied": "지정된 패치의 모든 변경 사항이 이미 코드에 포함되어 있습니다",
        "patch.apply.partially.applied": "지정된 패치의 일부 변경 사항은 이미 코드에 포함되어 있으므로 건너뛰었습니다",
        "patch.apply.success.applied.text": "패치가 성공적으로 적용되었습니다",
        "patch.apply.command": "패치 적용",
        "patch.apply.progress.title": "패치 적용 중\\u2026",
        "shelve.changes.restore.error": "일부 파일이 영구적으로 삭제되어 {0, choice, 1#보류된 변경 목록을|2#{0}개의 보류된 변경 목록을} 완전히 복원할 수 없습니다",
        "create.patch.success.confirmation": "패치 {0}을(를) 성공적으로 생성했습니다",
        "shelve.changes.only.directories": "선택한 변경 사항은 파일이 아닌 디렉터리에만 영향을 미치므로 보류할 수 없습니다",
        "shelve.editor.diff.preview.title": "보류됨: {0}",
        "shelve.tree.accessible.name": "선반",
        "stash.tree.accessible.name": "스태시",
        "stash.changes.message": "{0} 이전의 커밋되지 않은 변경 사항",
        "stash.changes.message.with.date": "{1}의 {0} 이전의 커밋되지 않은 변경 사항",
        "edit.errors": "오류 편집",
        "rollback.modified.without.editing.confirm.single": "{1}의 변경 사항을 {0}하시겠습니까?",
        "rollback.modified.without.editing.confirm.multiple": "선택한 파일 {1}개의 변경 사항을 {0}하시겠습니까?",
        "error.updating.changes": "변경 사항 업데이트 오류: {0}",
        "no.ignored.files": "무시된 파일 없음",
        "ignored.file.tab.title": "무시된 파일",
        "ignored.file.general.settings.title": "일반 설정",
        "ignored.file.manage.policy.label": "무시된 파일 관리 정책:",
        "ignored.file.manage.always.ask.option": "항상 묻기",
        "ignored.file.manage.all.projects.option": "모든 프로젝트에 대해 관리",
        "ignored.file.manage.this.project.option": "이 프로젝트에 대해서만 관리",
        "ignored.file.not.manage.this.project.option": "이 프로젝트에 대해서만 관리 안 함",
        "ignored.file.not.manage.option": "앱 전체 사용 안 함",
        "ignored.file.excluded.settings.title": "제외된 디렉터리 관리 정책",
        "ignored.file.excluded.to.ignored.label": "제외된 디렉터리를 무시 파일에 추가",
        "ignored.file.ignored.to.excluded.label": "분석에서 무시된 디렉터리 자동 제외",
        "ignored.file.manage.view": "보기",
        "ignored.file.manage.with.files.message": "{0}은(는) 일반적으로 무시되는 파일을 {1}에 자동으로 추가할 수 있습니다.",
        "ignored.file.manage.message": "{0}은(는) 일반적으로 무시되는 파일을 {1}에 자동으로 추가할 수 있습니다."
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