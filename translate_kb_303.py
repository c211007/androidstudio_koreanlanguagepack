import json

def update_json():
    file_path = "missing_translations/missing_keys_korean.json"
    target_file = "VcsBundle.properties"
    
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    translations = {
        "settings.filter.configure.link": "구성",
        "remove.changelist.combobox.show.options": "옵션 표시",
        "remove.changelist.combobox.remove.silently": "자동으로 제거",
        "remove.changelist.combobox.do.not.remove": "아무것도 안 함",
        "radio.restore.workspace.on.branch.switching": "브랜치를 전환할 때 작업 공간 복원(&B)",
        "radio.restore.workspace.on.branch.switching.comment": "작업 공간은 열려 있는 파일의 집합, 현재 실행 구성 및 브랜치와 연결된 중단점입니다.",
        "settings.general.confirmation.group.title": "확인",
        "settings.general.changes.group.title": "변경 사항",
        "settings.when.files.are.deleted": "파일이 삭제될 때:",
        "checkbox.including.files.created.outside.ide": "{0} 외부에서 생성된 파일에 적용",
        "settings.border.when.files.are.created": "파일이 생성될 때:",
        "settings.label.when.empty.changelist.becomes.inactive": "빈 변경 목록이 비활성 상태가 될 때:",
        "settings.file.status.color.modified.in.not.active.changelist": "활성화되지 않은 변경 목록에서 수정됨",
        "settings.file.status.color.added.in.not.active.changelist": "활성화되지 않은 변경 목록에 추가됨",
        "settings.file.status.color.changelist.conflict": "변경 목록 충돌",
        "settings.issue.navigation.patterns": "{0}은(는) 체크인 설명에서 지정된 패턴을 검색하고 이슈 트래커의 이슈에 연결합니다",
        "settings.shelf.content.larger": "{0}K보다 큰 파일의 기본 콘텐츠는 저장되지 않습니다",
        "settings.change.shelves.location": "선반 위치 변경\\u2026",
        "change.shelves.location.dialog.title": "선반 위치 변경",
        "change.shelves.location.dialog.action.button": "위치 변경",
        "change.shelves.location.dialog.group.title": "선반 저장 위치:",
        "change.shelves.location.dialog.location.browser.title": "선반을 저장할 디렉터리 선택",
        "change.shelves.location.dialog.default.label": "기본 디렉터리:",
        "change.shelves.location.dialog.custom.label": "사용자 지정 디렉터리(&U):",
        "settings.current.location": "현재 위치: ",
        "settings.default.location": "기본 위치: ",
        "settings.auto.detected": "자동 감지됨: ",
        "settings.auto.detected.progress": "감지 중\\u2026",
        "checkbox.include.issues.not.assigned.to.me": "나에게 할당되지 않은 이슈 포함",
        "checkbox.select.current.file.only": "현재 파일만 선택(&C)",
        "action.Anonymous.text.restore.all.leading.directories": "모든 선행 디렉터리 복원",
        "action.Anonymous.text.remove.all.leading.directories": "모든 선행 디렉터리 제거",
        "action.SearchFieldAction.text.find": "찾기: ",
        "action.DumbAware.ApplyPatchDifferentiatedDialog.text.refresh": "새로고침",
        "action.DumbAware.ApplyPatchDifferentiatedDialog.description.refresh": "새로고침",
        "action.NotificationAction.VcsRootProblemNotifier.text.enable.integration": "통합 활성화",
        "action.NotificationAction.VcsRootProblemNotifier.text.ignore": "무시",
        "action.NotificationAction.VcsRootProblemNotifier.text.configure": "구성\\u2026",
        "action.NotificationAction.AllVcses.text.install": "설치",
        "action.NotificationAction.AllVcses.text.read.more": "자세히 알아보기",
        "action.NotificationAction.AllVcses.text.open.plugin.page": "플러그인 페이지 열기",
        "action.NotificationAction.InactiveRangesDamagedNotification.text.view.changes": "변경 사항 보기\\u2026",
        "action.AnActionButton.text.add.jira.pattern": "JIRA 패턴 추가",
        "action.AnActionButton.text.add.youtrack.pattern": "YouTrack 패턴 추가",
        "action.ToggleAction.text.preview.diff": "차이점 미리보기",
        "action.ToggleAction.text.show.details": "세부 정보 표시",
        "action.ToggleAction.description.show.details": "세부 정보 패널을 표시합니다",
        "action.ToggleAction.text.scope.filter": "범위 필터",
        "action.DumbAwareAction.text.compare.with.local.content": "로컬 콘텐츠와 비교",
        "action.NotificationAction.VFSListener.text.view.files": "파일 보기\\u2026"
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