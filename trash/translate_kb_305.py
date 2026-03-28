import json

def update_json():
    file_path = "missing_translations/missing_keys_korean.json"
    target_file = "VcsBundle.properties"
    
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    translations = {
        "selection.history.can.not.load.message": "리비전 콘텐츠를 로드할 수 없습니다",
        "vcs.update.tab.name": "업데이트 정보",
        "file.history.tab.name": "히스토리",
        "vcs.commit.files.committed": "{0,choice,0#파일 없음|1#{0}개의 파일|2#{0}개의 파일} 커밋됨",
        "vcs.commit.files.committed.and.files.failed.to.commit": "{0,choice,0#파일 없음|1#{0}개의 파일|2#{0}개의 파일}이 커밋되었으며 {1,choice,1#{1}개의 파일|2#{1}개의 파일}을 커밋하지 못했습니다.",
        "vcs.commit.notification.shareProjectOn": "{0}에 프로젝트 공유",
        "vcs.commit.notification.shareProjectOn.orOn": "{0}에",
        "vcs.commit.canceled": "커밋이 취소됨",
        "checking.vcs.status.progress": "VCS 상태 확인 중\\u2026",
        "notification.showDetailsInConsole": "콘솔에 세부 정보 표시",
        "unregistered.roots.label": "등록되지 않은 루트:",
        "copy.revision.number.action": "리비전 번호 복사",
        "annotations.color.mode.author": "작성자",
        "annotations.color.mode.order": "순서",
        "annotations.color.mode.hide": "숨기기",
        "annotations.color.mode.group.colors": "색상",
        "annotations.short.name.type.initials": "이니셜",
        "annotations.short.name.type.first.name": "이름",
        "annotations.short.name.type.last.name": "성",
        "annotations.short.name.type.full.name": "전체 이름",
        "annotations.short.name.type.email": "이메일",
        "annotations.short.name.type.group.names": "이름",
        "commit.description.tooltip.commit": "커밋 {0}",
        "commit.description.tooltip.author": "작성자: {0}",
        "commit.description.tooltip.date": "날짜: {0}",
        "commit.description.tooltip.path": "경로: {0}",
        "settings.version.control.option.group": "버전 관리",
        "settings.commit.message.option.group": "커밋 메시지",
        "settings.changelists.option.group": "변경 목록",
        "settings.confirmation.option.group": "확인",
        "dialog.title.files.created": "파일 생성됨",
        "label.select.files.to.be.added.to.version.control": "버전 관리에 추가할 파일 선택",
        "dialog.title.cannot.convert.module": "모듈을 변환할 수 없음",
        "dialog.title.select.destination.folder": "대상 폴더 선택",
        "dialog.message.enter.directory.name": "생성된 프로젝트의 디렉터리 이름을 입력하세요. \"{0}\"에 직접 체크아웃하려면 비워 두세요.",
        "dialog.title.project.directory.name": "프로젝트 디렉터리 이름",
        "progress.title.hey": "이봐요",
        "progress.title.version.control.processing.changed.files": "버전 관리: 변경된 파일 처리 중",
        "dialog.message.can.t.create.text.editor.for": "{0}의 텍스트 편집기를 만들 수 없습니다.",
        "link.label.display.anyway": "항상 표시",
        "link.label.hide": "숨기기",
        "action.ShowAffectedFilesAction.show.affected.files.text": "영향을 받는 파일 표시",
        "progress.title.loading.current.revision": "현재 리비전 로드 중\\u2026",
        "dialog.title.remove.empty.changelist": "빈 변경 목록 제거",
        "button.remove": "제거",
        "checkbox.remember.my.choice": "내 선택 기억(&R)",
        "action.vcs.log.show.separator": "표시",
        "notification.title.couldn.t.save.uncommitted.changes": "커밋되지 않은 변경 사항을 저장할 수 없습니다.",
        "dialog.title.ignored.files": "무시된 파일",
        "dialog.title.modified.without.checkout.files": "체크아웃 없이 수정된 파일"
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