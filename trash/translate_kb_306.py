import json

def update_json():
    file_path = "missing_translations/missing_keys_korean.json"
    target_file = "VcsBundle.properties"
    
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    translations = {
        "dialog.title.unversioned.files": "버전 관리되지 않는 파일",
        "button.skip": "건너뛰기",
        "progress.text.performing": "{0}: {1} 수행 중\\u2026",
        "action.message.use.selected.changes.description": "선택한 변경 사항 {0}개",
        "progress.text.performing.rollback": "{0}: 롤백 수행 중\\u2026",
        "progress.title.adding.files.to.vcs": "VCS에 파일 추가 중\\u2026",
        "notification.content.didn.t.update.repository.changes": "오류로 인해 새 메시지로 리포지토리 변경 사항을 업데이트하지 못했습니다: {0}",
        "progress.title.discovering.location": "{0}의 위치 검색 중",
        "dialog.title.resolve.changelist.conflict": "변경 목록 충돌 해결",
        "changes.view.conflicts.banner.title": "병합 충돌로 인해 계속할 수 없습니다",
        "changes.view.conflicts.banner.default.resolve.action": "해결\\u2026",
        "link.label.move.changes": "변경 사항 이동",
        "link.label.switch.changelist": "변경 목록 전환",
        "dialog.message.no.changes.for.this.file": "이 파일에 대한 변경 사항이 없습니다",
        "dialog.title.message": "메시지",
        "link.label.ignore": "무시",
        "tooltip.show.options.dialog": "옵션 대화상자 표시",
        "dialog.message.conflict.seems.to.be.resolved": "충돌이 해결된 것 같습니다",
        "dialog.title.no.conflict.found": "충돌이 발견되지 않음",
        "dialog.title.move.changes.to.active.changelist": "활성 변경 목록으로 변경 사항 이동",
        "checkbox.include": "포함(&I)",
        "action.filter.filter.by.text": "필터 기준",
        "action.filter.separator.text": "파일 숨기기",
        "action.filter.moved.files.text": "변경 없이 이동됨",
        "action.filter.non.important.files.text": "중요하지 않은 변경 사항 포함",
        "group.mainmenu.vcs.current.file.text": "현재 파일",
        "multiple.file.merge.dialog.progress.title.resolving.conflicts": "충돌 해결 중\\u2026",
        "multiple.file.merge.dialog.message.error.saving.merged.data": "병합된 데이터를 저장하는 중 오류 발생: {0}",
        "multiple.file.merge.dialog.command.name.accept.yours": "내 것 수락",
        "multiple.file.merge.dialog.command.name.accept.theirs": "상대 것 수락",
        "multiple.file.merge.dialog.progress.title.loading.revisions": "리비전 로드 중\\u2026",
        "multiple.file.merge.dialog.error.loading.revisions.to.merge": "병합할 리비전을 로드하는 중 오류 발생: {0}",
        "multiple.file.merge.dialog.message.file.too.big.to.be.loaded": "파일이 너무 커서 로드할 수 없습니다",
        "multiple.file.merge.dialog.title.can.t.show.merge.dialog": "병합 대화상자를 표시할 수 없음",
        "text.commit.message.truncated.by.ide.name": "{0}\\n\\n... 커밋 메시지가 너무 길어 {1}에서 잘렸습니다\\u2026",
        "label.project.vcs.root.mapping": "<프로젝트>",
        "label.relative.project.path.presentation": "<프로젝트>/{0}",
        "file.content.too.big.to.load.increase.property.suggestion": "''{0}''의 콘텐츠를 표시할 수 없습니다.\\n파일이 {1}보다 큽니다.\\n\\n''idea.properties'' 파일에서 {2} 속성을 늘려 이 제한을 무시할 수 있습니다.",
        "error.date.before.must.be.a.valid.date": "이전 날짜는 유효한 날짜여야 합니다",
        "error.date.after.must.be.a.valid.date": "이후 날짜는 유효한 날짜여야 합니다",
        "error.change.from.must.be.a.valid.number": "변경 시작은 유효한 숫자여야 합니다",
        "error.change.to.must.be.a.valid.number": "변경 끝은 유효한 숫자여야 합니다",
        "action.annotate.revision.text": "리비전 어노테이션",
        "action.annotate.selected.revision.in.new.tab.description": "새 탭에서 선택한 리비전 어노테이션",
        "action.annotate.previous.revision.text": "이전 리비전 어노테이션",
        "action.annotate.successor.selected.revision.in.new.tab.description": "새 탭에서 선택한 리비전의 후속 리비전 어노테이션",
        "action.annotate.show.diff.preview.on.hover.text": "호버 시 차이점 미리보기 표시",
        "notification.title.cant.load.annotations": "어노테이션을 로드할 수 없습니다",
        "hide.this.notification": "이 알림 숨기기",
        "vcs.error.failed.to.load.file.content.from.vcs": "콘텐츠를 로드할 수 없습니다"
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