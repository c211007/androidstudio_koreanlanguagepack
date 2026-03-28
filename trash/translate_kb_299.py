import json

def update_json():
    file_path = "missing_translations/missing_keys_korean.json"
    target_file = "VcsBundle.properties"
    
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    translations = {
        "changes.remove.active.empty.prompt": "활성 상태로 만들 변경 목록을 선택하세요:",
        "changes.remove.active.title": "활성 변경 목록 삭제",
        "create.patch.loading.content.progress": "콘텐츠 수정 사항 로드 중",
        "create.patch.reverse.checkbox": "패치 뒤집기(&R)",
        "create.patch.file.path": "파일로(&F):",
        "create.patch.to.clipboard": "클립보드로(&C)",
        "create.patch.encoding": "인코딩(&E):",
        "committed.changes.refresh.progress": "VCS 히스토리 새로고침 중",
        "cache.settings.dialog.title": "VCS 히스토리 캐시 설정",
        "changes.browser.details.marker": "더 보기\\u2026",
        "changelist.details.title": "변경 목록 세부 정보",
        "date.group.title": "날짜",
        "date.group.today": "오늘",
        "date.group.last.week": "지난주",
        "user.group.title": "사용자",
        "filter.structure.name": "구조",
        "filter.none.name": "없음",
        "issue.link.issue.column": "이슈",
        "issue.link.link.column": "링크",
        "issue.link.add.title": "이슈 탐색 링크 추가",
        "issue.link.edit.title": "이슈 탐색 링크 편집",
        "issue.link.delete.prompt": "선택한 탐색 링크를 삭제하시겠습니까?",
        "issue.link.delete.title": "이슈 탐색 링크 삭제",
        "issue.link.no.patterns": "구성된 패턴 없음",
        "issue.action.add.jira.issue.navigation.pattern.title": "JIRA 이슈 탐색 패턴 추가",
        "issue.action.enter.jira.installation.url.label": "JIRA 설치 URL 입력:",
        "issue.action.add.youtrack.issue.navigation.pattern.title": "YouTrack 이슈 탐색 패턴 추가",
        "issue.action.enter.youtrack.installation.url.label": "YouTrack 설치 URL 입력:",
        "add.issue.dialog.invalid.regular.expression": "잘못된 정규 표현식: {0}",
        "add.issue.dialog.issue.link.label": "이슈 링크:",
        "add.issue.dialog.issue.id.label": "이슈 ID:",
        "add.issue.dialog.issue.example.border.title": "예시",
        "add.issue.dialog.issue.link.replacement.expression": "이슈 링크 (교체 표현식):",
        "add.issue.dialog.issue.id.regular.expression": "이슈 ID (정규 표현식):",
        "add.issue.dialog.issue.no.match": "<일치 없음>",
        "committed.changes.empty.comment": "<설명 없음>",
        "committed.changes.filter.all": "모두",
        "committed.changes.filter.none": "<없음>",
        "committed.changes.partial.list": "[일부]",
        "update.info.loading.changelists": "변경 목록 로드 중\\u2026",
        "update.info.group.by.changelist": "변경 목록별 그룹화",
        "update.info.click.status.text.prefix": "클릭",
        "update.info.to.initialize.status.text.suffix": "하여 리포지토리 변경 캐시 초기화",
        "update.info.refresh.link.status.text": "새로고침",
        "outdated.version.show.diff.action": "차이점 표시",
        "outdated.version.update.project.action": "프로젝트 업데이트",
        "outdated.version.text": "구버전입니다. {0} {1}에 의해 {3,choice,0#수정|1#삭제}됨: {2}",
        "current.version.text": "{4}<br/><br/>현재 버전은 {3}입니다.<br/>{0}에 의해 수정됨<br/>{1}<br/>{2}",
        "committed.changes.filter.title": "필터 기준",
        "committed.changes.group.title": "그룹 기준"
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