import json

def update_json():
    file_path = "missing_translations/missing_keys_korean.json"
    target_file = "VcsBundle.properties"
    
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    translations = {
        "changes.button.newer": "최신 >",
        "changes.button.older": "< 이전",
        "changes.directory.does.not.belong.to.the.active.changelist": "{0, choice, 1#이 디렉터리는|2#다음 디렉터리들은} 활성 변경 목록에 속하지 않습니다:",
        "changes.file.does.not.belong.to.the.active.changelist": "{0, choice, 1#이 파일은|2#다음 파일들은} 활성 변경 목록에 속하지 않습니다:",
        "changes.configure": "\\\\&구성\\u2026",
        "changes.hide.this.notification": "이 알림 숨기기",
        "changes.set.active.changelist.to.change.list.name": "''{0}''(을)를 활성 변경 목록으로 설정",
        "changes.move.changes.to.active.change.list.name": "활성 변경 목록({0})으로 변경 사항 이동",
        "changes.file.from.non.active.changelist.is.modified": "비활성 변경 목록의 파일이 수정되었습니다",
        "changes.another.change.list": "다른",
        "changes.default.change.list": "기본",
        "changes.IncludeChangedLinesIntoCommit.chunks.action.text": "선택한 청크를 커밋에 포함",
        "changes.ExcludeChangedLinesFromCommit.chunks.action.text": "선택한 청크를 커밋에서 제외",
        "changes.include.lines.into.commit": "커밋에 줄 포함",
        "changes.exclude.lines.from.commit": "커밋에서 줄 제외",
        "changes.move.to.changelist": "''{0}'' 변경 목록으로 이동",
        "changes.notification.content.repository.location.not.found.for": "{0}에 대한 리포지토리 위치를 찾을 수 없습니다",
        "changes.days.of.history.to.cache.initially": "초기에 캐시할 히스토리 일수:",
        "changes.changelists.to.cache.initially": "초기에 캐시할 변경 목록 수:",
        "changes.minutes": "분",
        "changes.refresh.changes.every": "변경 사항 새로고침 주기:",
        "changes.please.enter.a.valid.regex": "유효한 정규 표현식을 입력하세요",
        "changes.no.incoming.changelists.available": "사용 가능한 수신 변경 목록이 없습니다",
        "changes.error.refreshing.vcs.history": "VCS 히스토리 새로고침 중 오류 발생",
        "changes.committed.changes": "커밋된 변경 사항",
        "changes.error.refreshing.view": "뷰 새로고침 오류: {0}",
        "changes.title.loading.changes": "변경 사항 로드 중",
        "changes.no.tracking.branch": "추적 브랜치 없음",
        "changes.no.tracking.branch.suffix": "\\ (추적 브랜치 없음)",
        "changes.ignore.file": "무시 파일",
        "impl.notification.content.vcs.plugin.not.found.for.mapping.to": "매핑할 VCS 플러그인을 찾을 수 없음: ''{0}''",
        "impl.progress.title.installing.plugin": "플러그인 설치 중\\u2026",
        "impl.notification.title.failed.to.install.plugin": "플러그인 설치 실패",
        "impl.notification.content.could.not.find.plugin": "{0} 플러그인을 찾을 수 없습니다",
        "impl.notification.content.plugin.was.unbundled.needs.to.be.installed.manually": "{0} 플러그인이 번들에서 해제되었으므로 수동으로 설치해야 합니다",
        "impl.show.all.affected.files.for.path.at.revision.failed": "{1}의 {0}에 대해 영향을 받는 모든 파일을 표시하지 못했습니다",
        "merge.loading.merge.details": "병합 세부 정보 로드 중\\u2026",
        "RepositoryBrowser.toolwindow.name": "리포지토리",
        "ChangesBrowserToolWindow.toolwindow.name": "변경 사항",
        "commit.message": "커밋 메시지",
        "commit.message.intention.family.name.reformat.commit.message": "커밋 메시지 서식 다시 지정",
        "commit.message.inspection.message.body.lines.should.not.exceed.characters": "본문 줄은 {0}자를 초과할 수 없습니다",
        "commit.message.intention.family.name.wrap.line": "자동 줄 바꿈",
        "commit.message.missing.blank.line.between.subject.and.body": "제목과 본문 사이에 빈 줄 누락",
        "commit.message.inspection.message.subject.should.not.exceed.characters": "제목은 {0}자를 초과할 수 없습니다",
        "commit.amend.commit": "커밋 수정",
        "commit.tooltip.merge.this.commit.with.the.previous.one": "이 커밋을 이전 커밋과 병합",
        "ranges.to.commit.of.ranges.size.changes": "{1}개의 변경 사항 중 {0}개",
        "commit.changes": "변경 사항 커밋",
        "commit.progress.title": "커밋"
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