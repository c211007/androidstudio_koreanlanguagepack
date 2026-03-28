import json

def update_json():
    file_path = "missing_translations/missing_keys_korean.json"
    target_file = "VcsBundle.properties"
    
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    translations = {
        "ignored.file.manage.this.project": "이 프로젝트에서",
        "ignored.file.manage.all.project": "모든 프로젝트에서",
        "ignored.file.manage.notmanage": "추가 안 함",
        "ignored.file.manage.view.dialog.title": "무시할 파일 추가",
        "ignored.file.manage.view.dialog.ignore.action": "무시(&I)",
        "ignoring.files.progress.title": "파일 무시 중\\u2026",
        "browse.changes.content.title": "{0}의 변경 사항",
        "browse.changes.no.filter.prompt": "필터링 기준을 지정하지 않았습니다. 프로젝트의 전체 히스토리를 보시겠습니까?",
        "browse.changes.title": "변경 사항 찾아보기",
        "browse.changes.show.all.button": "모든 변경 사항 표시",
        "browse.changes.show.recent.button": "최근 변경 사항 표시",
        "new.changelist.make.active.checkbox": "활성으로 설정(&A)",
        "new.changelist.new.label": "새로 만들기",
        "move.to.another.changelist.nothing.selected.notification": "이동할 수 있는 항목이 선택되지 않았습니다",
        "composite.change.provider.include.vcs.checkbox": "{0}의 변경 사항 포함",
        "shelf.tab": "선반",
        "directory.mapping.remove.title": "VCS 디렉터리 매핑 편집",
        "directory.mapping.add.title": "VCS 디렉터리 매핑 추가",
        "directory.mapping.checkbox.detect.vcs.mappings.automatically": "자동 매핑 감지 활성화",
        "directory.mapping.checkbox.detect.vcs.mappings.automatically.hint": "프로젝트 구조 변경 시 매핑을 추가 및 제거합니다. 새로 생성된 VCS 루트를 감지합니다.",
        "settings.vcs.mapping.browser.select.directory.title": "디렉터리 선택",
        "settings.vcs.mapping.browser.select.directory.description": "VCS에 매핑할 디렉터리를 선택하세요",
        "settings.vcs.mapping.status.looking.for.vcs.administrative.area": "VCS 관리 영역 찾는 중",
        "settings.vcs.mapping.invalid.vcs.options.error": "잘못된 VCS 옵션: {0}",
        "settings.vcs.mapping.project.description": "모든 모듈의 콘텐츠 루트 및 프로젝트 기본 디렉터리의 모든 직접적인 하위 디렉터리",
        "settings.vcs.mapping.project.description.with.idea.directory": "모든 모듈의 콘텐츠 루트, 프로젝트 기본 디렉터리의 모든 직접적인 하위 디렉터리 및 {0} 디렉터리 콘텐츠",
        "unshelve.changelist.chooser.title": "변경 목록으로 변경 사항 보류 해제",
        "revert.changes.changelist.chooser.title": "대상 변경 목록 선택",
        "retrieving.annotations": "어노테이션 로드 중",
        "multiple.file.merge.title": "충돌",
        "multiple.file.merge.accept.yours": "내 것 수락(&Y)",
        "multiple.file.merge.accept.theirs": "상대 것 수락(&T)",
        "multiple.file.merge.merge": "병합(&M)\\u2026",
        "multiple.file.merge.column.name": "이름",
        "multiple.file.merge.request.title": "{0}에 대한 수정 사항 병합",
        "multiple.file.merge.loading.progress.title": "병합 수정 사항 로드 중\\u2026",
        "multiple.file.merge.group.by.directory.checkbox": "디렉터리별로 파일 그룹화",
        "unknown.vcs.presentation": "<알 수 없는 VCS> ({0})",
        "project.detected.n.roots.presentation": "{0}개 감지됨",
        "show.diff.progress.title": "콘텐츠 로드 중",
        "show.diff.progress.title.detailed": "{0}의 콘텐츠 로드 중",
        "new.changelist.duplicate.name.error": "해당 이름의 변경 목록이 이미 존재합니다",
        "new.changelist.empty.name.error": "비어 있는 이름으로 새 변경 목록을 생성할 수 없습니다",
        "browse.changes.action": "변경 사항 찾아보기",
        "browse.changes.scope": "{0}에 영향을 미치는 변경 사항",
        "rollback.modified.without.checkout.error.tab": "체크아웃 없이 {0} 수정됨",
        "annotate.action.name": "어노테이션",
        "annotate.action.description": "파일 어노테이션",
        "operation.name.annotate": "어노테이션",
        "changes.remove.active.prompt": "변경 사항을 이동할 변경 목록을 선택하세요:"
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