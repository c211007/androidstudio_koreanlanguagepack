import json

def update_json():
    file_path = "missing_translations/missing_keys_korean.json"
    target_file = "VcsBundle.properties"
    
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    translations = {
        "diff.producer.error.cant.get.revision.content": "리비전 콘텐츠를 가져올 수 없습니다",
        "show.diff.from.annotation.action.error.can.not.load.data.to.show.diff": "차이점을 표시하기 위한 데이터를 로드할 수 없습니다",
        "vcs.preview.panel.added.ignored.line": "추가된 무시 줄",
        "vcs.preview.panel.modified.ignored.line": "수정된 무시 줄",
        "vcs.preview.panel.deleted.ignored.line.below": "아래 삭제된 무시 줄",
        "vcs.preview.panel.line.with.modified.whitespaces.and.deletion.after": "공백이 수정되고 뒤에 삭제가 있는 줄",
        "vcs.preview.panel.added.line": "추가된 줄",
        "vcs.preview.panel.line.with.modified.whitespaces": "공백이 수정된 줄",
        "vcs.preview.panel.modified.line": "수정된 줄",
        "vcs.preview.panel.deleted.line.below": "아래 삭제된 줄",
        "vcs.preview.panel.last.commit.modified.line": "마지막 커밋에서 수정된 줄",
        "annotation.background": "어노테이션 배경",
        "changes.error.shelving.changes.failed": "변경 사항 보류 실패: {0}",
        "changes.error.can.t.get.revision.content": "리비전 콘텐츠를 가져올 수 없습니다",
        "changes.error.failed.to.create.content.for.current.revision": "현재 리비전의 콘텐츠를 생성하지 못했습니다",
        "changes.error.failed.to.fetch.current.revision": "현재 리비전을 가져오지 못했습니다",
        "changes.finishing.changed.on.server.update": "\"서버에서 변경됨\" 업데이트 완료 중",
        "changes.tried.to.save.uncommitted.changes.in.shelve.before.s.but.failed.with.an.error": "{0} 이전에 커밋되지 않은 변경 사항을 보류하려고 시도했지만 오류와 함께 실패했습니다.<br/>{1}",
        "changes.refresh.changelists.after.update": "업데이트 후 변경 목록 새로고침",
        "changes.deleting.added.files.locally": "로컬에서 추가된 파일 삭제 중\\u2026",
        "changes.progress.text.vcs.name.performing.operation.name": "{0}: {1} 수행 중\\u2026",
        "changes.project.exclude.paths": "프로젝트 제외 경로",
        "changes.error.default.project.not.supported": "기본 프로젝트는 지원되지 않습니다",
        "changes.removing.configuration.0.from.ignore": "무시에서 구성 {0}을(를) 제거하는 중\\u2026",
        "changes.checking.configuration.0.for.ignore": "무시에 대해 구성 {0}을(를) 확인하는 중\\u2026",
        "changes.cant.load.changes": "변경 사항을 로드할 수 없습니다",
        "changes.switched.to.branch.name": "{0}(으)로 전환됨",
        "changes.do.cleanup": "정리 수행\\u2026",
        "changes.locked.by": "잠금 주체: {0}",
        "changes.browse": "찾아보기",
        "changes.diff.separator": "차이점",
        "changes.combined.diff": "결합된 변경 사항 차이점",
        "changes.warning.not.all.local.changes.may.be.shown.due.to.an.error": "경고: 오류로 인해 일부 로컬 변경 사항이 표시되지 않을 수 있습니다: {0}",
        "changes.new.changelist": "새 변경 목록",
        "changes.action.include.in.operation.name": "{0}에 포함(&I)",
        "changes.error.content.for.0.was.removed": "''{0}''의 콘텐츠가 제거되었습니다",
        "changes.error.can.t.show.diff.for": "''{0}''의 차이점을 표시할 수 없습니다",
        "changes.can.not.find.patch.for.path.in.patch.file": "패치 파일에서 {0}의 패치를 찾을 수 없습니다.",
        "changes.error.cannot.find.base.for.path": "''{0}''의 기본을 찾을 수 없습니다",
        "changes.error.can.t.show.diff.for.binary.file": "바이너리 파일 ''{0}''의 차이점을 표시할 수 없습니다",
        "changes.impossible.until.indices.are.up.to.date": "인덱스가 최신 상태가 될 때까지 불가능합니다",
        "changes.empty.changelists.no.longer.active": "{0,choice,1#빈 변경 목록 ''{1}''이(가)|2#빈 변경 목록<br/>'{1}이(가)} 더 이상 활성화되어 있지 않습니다.<br/>제거하시겠습니까?",
        "changes.text.default.ignored.files": "기본 무시된 파일",
        "changes.tab.title.vcs.errors": "VCS 오류",
        "changes.progress.title.choice.revert.apply.changes": "변경 사항 {0, choice, 0#복원|1#적용}",
        "changes.dialog.message.failed.to.revert.apply.changes": "변경 사항 {0, choice, 0#복원|1#적용} 실패: ",
        "changes.revert.apply.change.list.name": "{0, choice, 0#복원: |1#적용: }{1}",
        "change.dialog.title.change.list.name": "{0} [{1}]",
        "change.dialog.title.in.change.list.name": "{1}의 {0}",
        "changes.none": "<없음>"
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