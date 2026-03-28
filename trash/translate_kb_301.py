import json

def update_json():
    file_path = "missing_translations/missing_keys_korean.json"
    target_file = "VcsBundle.properties"
    
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    translations = {
        "confirmation.title.add.files.to": "{0}에 파일을 추가하시겠습니까?",
        "confirmation.title.add.ignored.single.file": "파일이 .gitignore에 있음",
        "confirmation.title.add.ignored.single.directory": "디렉터리가 .gitignore에 있음",
        "confirmation.message.add.ignored.single.file": "선택한 파일을 Git에 추가하시겠습니까?",
        "confirmation.message.add.ignored.single.directory": "선택한 디렉터리를 Git에 추가하시겠습니까?",
        "confirmation.title.add.ignored.files.or.dirs": "항목이 .gitignore에 있음",
        "confirmation.message.add.ignored.files.or.dirs": "Git에 추가할 파일을 선택하십시오",
        "waiting.changelists.update.for.show.commit.dialog.message": "커밋",
        "rolling.back.file": "{0} 롤백 중",
        "annotation.original.revision.text": "리비전: {0}",
        "annotation.switch.to.original.text": "병합 소스 숨기기",
        "annotation.switch.to.merged.text": "병합 소스 표시",
        "switch.to.changelist": "변경 목록으로 전환(&T) (''{0}'')",
        "move.to.changelist": "활성 변경 목록으로 변경 사항 이동(&M) (''{0}'')",
        "vcs.config.track.changed.on.server": "다음 주기마다 서버와 충돌 확인:",
        "vcs.quicklist.popup.title": "VCS 작업",
        "action.Vcs.Toolbar.QuickListPopupAction.text": "VCS 작업",
        "line.annotation.aspect.author": "작성자",
        "line.annotation.aspect.date": "날짜",
        "line.annotation.aspect.revision": "리비전",
        "annotation.commit.number": "커밋 번호",
        "annotation.wrong.line.number.notification.text": "<html>{0}에 의해 어노테이션된 줄 수가 파일의 줄 수와 같지 않습니다. 파일 인코딩 및 줄 구분 기호를 확인하십시오.</html>",
        "lst.inactive.ranges.damaged.notification": "변경 사항의 일부가 활성 변경 목록으로 이동되었습니다",
        "todo.handler.only.skipped": "<html><body>TODO 검사에서 {0,choice, 0#|1#1개의 파일|2#{0}개의 파일}을(를) 건너뛰었습니다.<br/>\\n 새로 추가되거나 편집된 TODO 항목이 없거나 변경된 텍스트 조각에 위치한 항목이 없습니다.</body></html>",
        "todo.handler.only.added": "<html><body>{0,choice, 0#|1#1|2#{0}}개의 추가/편집된 TODO {0,choice, 0#|1#항목이|2#항목이} 발견되었습니다.<br/>\n 검토하시겠습니까?<br/>\n {1,choice, 0#|1#1개의 파일을 건너뛰었습니다.|2#{1}개의 파일을 건너뛰었습니다.}</body></html>",
        "todo.handler.only.in.changed": "<html><body>변경된 조각에서 {0,choice, 1#1|2#{0}}개의 TODO {0,choice, 1#항목이|2#항목이} 발견되었습니다.<br/>\n 검토하시겠습니까?<br/>\n {1,choice, 0#|1#1개의 파일을 건너뛰었습니다.|2#{1}개의 파일을 건너뛰었습니다.}</body></html>",
        "todo.handler.only.both": "<html><body>{0, choice, 1#1|2#{0}}개의 추가/편집된 TODO {0,choice, 1#항목|2#항목} 및 <br/>\n 변경된 조각에 위치한 {1, choice, 1#1개의 항목이|2#{1}개의 항목이} 발견되었습니다.<br/>\n 검토하시겠습니까?<br/>\n {2,choice, 0#|1#1개의 파일을 건너뛰었습니다.|2#{2}개의 파일을 건너뛰었습니다.}</body></html>",
        "label.todo.items.found": "TODO {0}개",
        "paths.affected.in.revision": "{0}의 변경 사항",
        "executable.select.label": "{0} 실행 경로(&P):",
        "executable.select.title": "실행 파일 선택",
        "executable.test": "테스트",
        "executable.project.override": "현재 프로젝트에 대해서만 이 경로 설정",
        "executable.project.override.reset.title": "프로젝트 실행 파일",
        "executable.project.override.reset.message": "이 프로젝트에 대해 구성된 실행 파일 경로를 모든 프로젝트에 대한 전역 경로로 설정하거나 현재 전역 실행 파일로 복원할 수 있습니다.",
        "executable.project.override.reset.globalize": "전역으로 설정",
        "executable.project.override.reset.revert": "복원",
        "project.configuration.files.add.notification.message": "IDE 프로젝트 설정을 {0}에 추가할 수 있습니다",
        "project.configuration.files.add.notification.action.view": "파일 보기",
        "project.configuration.files.add.notification.action.add": "항상 추가",
        "project.configuration.files.add.notification.action.mute": "다시 묻지 않음",
        "project.configuration.files.view.dialog.title": "{0}에 파일 추가",
        "external.files.add.notification.message": "외부에서 추가된 파일을 {0}에 추가할 수 있습니다",
        "external.files.add.notification.action.view": "파일 보기",
        "external.files.add.notification.action.add": "항상 추가",
        "external.files.add.notification.action.mute": "다시 묻지 않음",
        "external.files.add.view.dialog.title": "{0}에 파일 추가",
        "ignore.to.exclude.notification.message": "무시된 디렉터리 중 일부가 분석 및 검색에서 제외되지 않았습니다",
        "ignore.to.exclude.notification.notice": "<html><b>참고:</b> 제외하기 전에 디렉터리 콘텐츠를 다시 확인하는 것이 좋습니다. 일부 디렉터리에는 제외해서는 안 되는 항목이 포함되어 있을 수 있습니다.</html>",
        "ignore.to.exclude.notification.action.view": "디렉터리 보기"
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