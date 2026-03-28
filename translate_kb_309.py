import json

def update_json():
    file_path = "missing_translations/missing_keys_korean.json"
    target_file = "VcsBundle.properties"
    
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    translations = {
        "tab.title.commit": "커밋",
        "tab.title.commit.to.branch": "{0}에 커밋",
        "history.file.not.found": "{0} 파일을 찾을 수 없음",
        "history.dialog.title.difference.between.versions.in": "{2}에 있는 {0} 버전 및 {1} 버전의 차이점",
        "history.failed.to.load.content.for.revision.0": "{0} 리비전에 대한 콘텐츠를 로드하지 못했습니다",
        "history.tab.title.can.not.load.changelist.contents": "변경 목록 콘텐츠를 로드할 수 없습니다",
        "error.annotated.line.out.of.bounds": "어노테이션된 줄이 범위를 벗어남: {0}, 총 줄 수: {1}",
        "error.cant.load.affected.files": "''{1}'' 리비전의 ''{0}'' 경로에 영향을 받는 파일을 로드할 수 없습니다",
        "error.cant.get.local.file.for.non.local": "''{0}'' 파일의 로컬 위치를 가져올 수 없습니다",
        "update.label.before.update": "업데이트 전",
        "update.notification.title.project.partially.updated": "프로젝트 일부 업데이트됨",
        "update.notification.title.count.files.updated": "{0,choice,1#1개의 파일|2#{0}개의 파일} 업데이트됨",
        "update.notification.content.files.updated": "{0,choice,1#1개의 파일|2#{0}개의 파일} 업데이트됨",
        "update.file.name.wasn.t.modified": "{0}이(가) 수정되지 않았습니다",
        "update.filtered.files.count.in.filter.name": "{1}의 {0}",
        "update.label.after.update": "업데이트 후",
        "update.notification.content.view": "보기",
        "update.checkbox.don.t.show.again": "다시 표시 안 함",
        "update.can.t.load.content": "콘텐츠를 로드할 수 없습니다",
        "update.error.label": "오류: ",
        "roots.notification.content.added.vcs.name.roots": "{0} {1,choice,1#루트|2#루트} 추가됨: {2}",
        "roots.notification.content.directory.registered.as.root.but.no.repositories.were.found.there": "{0} 디렉터리가 {1} 루트로 등록되어 있지만 그곳에서 {1} 리포지토리를 찾을 수 없습니다.",
        "roots.notification.title.invalid.vcs.root.choice.mapping.mappings": "잘못된 VCS 루트 {0, choice, 1#매핑|2#매핑}",
        "roots.notification.title.vcs.root.configuration.problems": "VCS 루트 구성 문제",
        "roots.notification.title.vcs.name.integration.enabled": "{0} 통합 활성화됨",
        "notification.title.vcs.name.repository.repositories.found": "{0} {1, choice, 1#리포지토리|2#리포지토리}가 발견됨",
        "roots.the.following.directories.are.registered.as.vcs.roots.but.they.are.not": "다음 디렉터리가 VCS 루트로 등록되어 있지만 실제로는 아닙니다:",
        "configurable.issue.link.remove": "제거",
        "configurable.issue.link.edit": "편집",
        "configurable.shelf.storage.destination.shelf.directory.should.have.write.access": "대상 선반 디렉터리에 쓰기 권한이 있어야 합니다",
        "configurable.shelf.storage.destination.shelf.directory.should.have.read.access": "대상 선반 디렉터리에 읽기 권한이 있어야 합니다",
        "configurable.shelf.storage.cant.find.or.create.new.shelf.directory": "새 선반 디렉터리를 찾거나 생성할 수 없습니다",
        "configurable.vcs.manage.scopes": "범위 관리",
        "ex.new.changelist": "새 변경 목록\\u2026",
        "ex.move.lines.to.another.changelist.0": "다른 변경 목록({0})으로 줄 이동",
        "ex.changelists": "변경 목록",
        "checkin.commit.checks.failed": "커밋 확인 실패",
        "checkin.commit.checks.failed.cancel.button": "취소(&N)",
        "checkin.wait": "대기(&W)",
        "checkin.can.not.load.current.revision": "현재 리비전을 로드할 수 없음",
        "checkin.can.not.load.previous.revision": "이전 리비전을 로드할 수 없음",
        "checkin.invalid.file.s": "잘못된 파일",
        "checkin.dialog.title.todo": "TODO",
        "checkin.filter.filter.name": "필터: {0}",
        "checkin.title.for.commit.0": "커밋용({0})",
        "checkin.unresolved.merge.unresolved.conflicts": "해결되지 않은 충돌",
        "checkin.unresolved.merge.are.you.sure.you.want.to.commit.changes.with.unresolved.conflicts": "해결되지 않은 충돌이 있는 변경 사항을 커밋하시겠습니까?",
        "before.checkin.error.unresolved.merge.conflicts": "파일에 해결되지 않은 충돌이 있습니다",
        "before.checkin.error.multiple.changelists.selected": "커밋을 위해 여러 변경 목록이 선택되었습니다",
        "patch.unknown.line.prefix": "알 수 없는 줄 접두사"
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