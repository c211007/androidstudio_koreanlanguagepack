import json

def update_json():
    file_path = "missing_translations/missing_keys_korean.json"
    target_file = "VcsBundle.properties"
    
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    translations = {
        "action.ImportIntoShelfAction.text": "패치 가져오기\\u2026",
        "action.ImportIntoShelfAction.description": "패치 파일을 선반에 복사합니다",
        "action.presentation.ApplySelectedChangesAction.text": "수락",
        "action.presentation.IgnoreSelectedChangesAction.text": "무시",
        "action.presentation.DiffShelvedChangesWithLocalActionProvider.description": "보류된 버전을 현재 버전과 비교",
        "action.presentation.ShowUpdatedDiffActionProvider.description": "업데이트 전 버전과의 차이점 표시",
        "button.clear": "지우기",
        "import.patches.into.shelf": "패치를 선반으로 가져오기\\u2026",
        "import.patches": "패치 가져오기",
        "looking.for.patch.files": "패치 파일 검색 중\\u2026",
        "title.load.revision.contents": "리비전 콘텐츠 로드",
        "message.read.only.status.title": "{0}: 읽기 전용 상태를 볼 수 없음",
        "message.read.only.status.content": "사용자는 <b>root</b>로 로그인되어 있습니다. 따라서 다음 사항이 해당합니다:<br><br>- {0} 파일의 읽기 전용 상태를 볼 수 없습니다.<br>- 모든 파일은 쓰기 가능한 것으로 취급됩니다.<br>- 수정 시 자동 파일 체크아웃이 불가능합니다.",
        "action.clone.dialog.stub.click.to.continue": "계속하려면 \\\"{0}\\\"을(를) 클릭하세요",
        "vcs.generic.name": "VCS",
        "vcs.generic.name.with.mnemonic": "VCS(_S)",
        "vcs.common.labels.directory": "디렉터리:",
        "vcs.common.labels.vcs": "VCS:",
        "vcs.common.labels.version.control": "버전 관리:",
        "vcs.common.labels.url": "URL:",
        "settings.commit.message.right.margin.label": "오른쪽 여백:",
        "settings.commit.message.show.right.margin.label": "오른쪽 여백 표시",
        "settings.commit.message.show.right.margin.n.columns.label": "{0}열에서 오른쪽 여백 표시",
        "settings.commit.message.body.add.blank.line.fix": "빈 줄 추가",
        "get.from.version.control": "리포지토리 복제",
        "clone.dialog.repository.url.item": "리포지토리 URL",
        "clone.dialog.clone.button": "복제",
        "clone.dialog.unable.create.destination.error": "대상 디렉터리를 만들 수 없습니다",
        "clone.dialog.clone.failed.error": "복제 실패",
        "committed.changes.tab": "리포지토리",
        "incoming.changes.tab": "수신",
        "local.changes.tab": "로컬 변경 사항",
        "error.cant.perform.operation.now": "지금은 {0}을(를) 할 수 없습니다",
        "local.changes.freeze.message": "로컬 변경 사항은 {0}이(가) 완료될 때까지 사용할 수 없습니다",
        "file.history.checking.last.revision.process": "최신 리비전 확인 중",
        "file.history.diff.revisions.process": "리비전 비교 중\\u2026",
        "file.history.exceeded.limit.message": "파일 히스토리: {1}에 대해 {0}개의 리비전만 로드되었습니다.\\n히스토리 제한을 변경하려면 {2}(으)로 이동하세요.",
        "file.history.details.empty.status": "커밋 메시지",
        "file.history.details.hash.author.on.date.at.time": "{2} {3}, {0} {1}",
        "file.history.details.committer.info": "{0}에 의해 커밋됨",
        "file.history.details.committer.tooltip.info": "{0}을(를) 거침",
        "file.history.diff.handler.paths.diff.title": "{2}에 있는 {0} 및 {1}의 차이점",
        "file.history.diff.handler.paths.diff.with.local.title": "{1}의 {0}과(와) 로컬 버전의 차이점",
        "file.history.diff.handler.affected.changes.title": "{1}의 초기 커밋 {0}",
        "file.history.diff.handler.collecting.affected.process": "영향을 받는 변경 사항 수집 중\\u2026",
        "file.history.diff.handler.comparing.process": "리비전 비교 중\\u2026",
        "file.history.diff.handler.process.error": "작업 중 오류 발생: {0}",
        "selection.history.loading.revision.status": "리비전 {0} 로드 중\\u2026",
        "selection.history.commit.message.label": "커밋 메시지:",
        "selection.history.local.revision.text": "로컬 변경 사항"
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