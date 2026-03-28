import json

def update_json():
    file_path = "missing_translations/missing_keys_korean.json"
    target_file = "VcsBundle.properties"
    
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    translations = {
        "ignore.to.exclude.notification.action.mute": "다시 표시 안 함",
        "ignore.to.exclude.notification.action.details": "자세히 알아보기",
        "ignore.to.exclude.view.dialog.title": "디렉터리 제외",
        "ignore.to.exclude.view.dialog.exclude.action": "제외(&E)",
        "ignore.to.exclude.no.directories.found": "제외할 디렉터리를 찾을 수 없음",
        "ignoreTokenType./": "<슬래시>",
        "ignoreTokenType.BRACKET_LEFT": "<왼쪽 대괄호>",
        "ignoreTokenType.BRACKET_RIGHT": "<오른쪽 대괄호>",
        "ignoreTokenType.COMMENT": "<주석>",
        "ignoreTokenType.CRLF": "<빈 줄>",
        "ignoreTokenType.HEADER": "<헤더>",
        "ignoreTokenType.SECTION": "<섹션>",
        "ignoreTokenType.VALUE": "<값>",
        "ignoreTokenType.syntax\\": "=<구문>",
        "ignore.codeInspection.group": "버전 관리",
        "ignore.codeInspection.duplicateEntry": "무시 파일 중복",
        "ignore.codeInspection.duplicateEntry.message": "<code>#ref</code> 패턴이 두 번 이상 정의되었습니다 #loc",
        "ignore.quick.fix.remove.entry": "패턴 제거",
        "vcs.add.to.ignore.file.action.group.text": "{0}에 추가",
        "vcs.add.to.ignore.file.action.group.description": "선택한 파일을 {0}에 추가",
        "vcs.add.to.ignore.file.create.ignore.file.confirmation.title": "{0} 생성",
        "vcs.add.to.ignore.file.create.ignore.file.confirmation.message": "{1}에 {0} 파일을 생성하시겠습니까?",
        "annotate.action.view.group.text": "보기",
        "configurable.ChangelistConflictConfigurable.display.name": "변경 목록",
        "configurable.VcsDirectoryConfigurationPanel.display.name": "디렉터리 매핑",
        "configurable.VcsGeneralConfigurationConfigurable.display.name": "확인",
        "configurable.IssueNavigationConfigurationPanel.display.name": "이슈 탐색",
        "configurable.VcsContentAnnotationConfigurable.display.name": "최근 변경 사항 표시",
        "vcs.operations.popup": "VCS 작업 팝업",
        "vcs.local.changes.toolbar": "VCS 로컬 변경 사항 도구 모음",
        "settings.checkbox.limit.history.to": "히스토리 제한:",
        "settings.checkbox.rows": "행",
        "settings.limit.history.to.n.rows.label": "히스토리를 {0}행으로 제한",
        "settings.checkbox.show.changed.in.last": "다음 기간 동안 변경된 파일 강조 표시:",
        "settings.checkbox.show.changed.in.last.comment": "수정된 파일은 외부 스택 추적 및 디버깅 중에 강조 표시됩니다.",
        "settings.checkbox.measure.days": "일",
        "settings.show.changed.in.last.n.days.label": "최근 {0}일 동안 변경된 내용 표시",
        "settings.check.every.minutes": "분",
        "settings.commit.message.inspections": "커밋 메시지 검사:",
        "inspection.SubjectBodySeparationInspection.display.name": "제목과 본문 사이의 빈 줄",
        "inspection.BodyLimitInspection.display.name": "본문 줄 제한",
        "inspection.CommitMessageSpellCheckingInspection.display.name": "맞춤법",
        "inspection.SubjectLimitInspection.display.name": "제목 줄 제한",
        "settings.commit.postpone.slow.checks": "커밋이 완료된 후 고급 검사를 실행합니다",
        "settings.commit.postpone.slow.checks.description": "검사에 실패하더라도 커밋을 막지는 않습니다",
        "settings.commit.postpone.slow.checks.description.short": "검사에 실패하더라도 커밋을 막지는 않습니다",
        "settings.confirmation.option.text.ask": "묻기",
        "settings.confirmation.option.text.no": "아니요",
        "settings.confirmation.option.text.yes": "예",
        "settings.commit.without.dialog.applies.to.git.mercurial": "Git 및 Mercurial 기반의 프로젝트에 적용됩니다"
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