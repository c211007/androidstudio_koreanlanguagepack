import json

def update_json():
    file_path = "missing_translations/missing_keys_korean.json"
    target_file = "VcsBundle.properties"
    
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    translations = {
        "patch.apply.rollback.progress.title": "적용된 변경 사항 롤백 중\\u2026",
        "patch.apply.rollback.progress": "적용된 변경 사항 롤백 중\\u2026",
        "patch.apply.outside.content.root.message": "루트 콘텐츠 외부에 패치할 파일이 있습니다: {0}",
        "patch.apply.overwrite.existing.title": "기존 파일 덮어쓰기",
        "patch.apply.overwrite.existing.files.prompt": "패치에 의해 다음 파일이 생성되어야 하지만 이미 존재합니다.\\n덮어쓰시겠습니까?",
        "patch.apply.overwrite.existing.file.prompt": "패치에 의해 다음 파일이 생성되어야 하지만 이미 존재합니다.\\n덮어쓰시겠습니까?\\n{0}",
        "patch.apply.file.type.directory.error": "{0} 파일은 디렉터리이므로 패치에서 콘텐츠를 적용할 수 없습니다.",
        "patch.apply.file.type.undefined.error": "{0} 파일은 유형이 정의되지 않아 패치에서 콘텐츠를 적용할 수 없습니다.",
        "patch.apply.file.type.binary.error": "{0} 파일은 바이너리이므로 패치에서 적용할 수 없습니다.",
        "patch.apply.incorrectly.processed.warning": "다음 {0, choice, 1#파일이|2#파일들이} VCS에서 잘못 처리될 수 있습니다.\\n수동으로 확인하십시오: {1}",
        "patch.apply.rollback.prompt": "다음 항목에 대한 패치를 적용하지 못했습니다: {0, choice, 0#패치.|1#파일:|2#파일들:}",
        "patch.apply.rollback.prompt.bottom": "패치의 다른 변경 사항이 성공적으로 적용되었습니다. 롤백하시겠습니까?",
        "patch.apply.rollback.will.not.affect.binaries.info": "롤백은 바이너리에 영향을 미치지 않습니다",
        "patch.apply.partly.failed.title": "패치 적용 일부 실패",
        "patch.apply.rollback.action": "롤백",
        "patch.apply.new.files.warning": "새 파일 적용 오류",
        "patch.apply.cannot.apply.now": "지금은 패치를 적용할 수 없음",
        "patch.apply.abort.action": "중단\\u2026",
        "patch.apply.abort.and.rollback.prompt": "패치 적용을 중단하고 롤백하시겠습니까, 아니면 이 파일을 건너뛰시겠습니까?",
        "patch.apply.abort.title": "패치 중단",
        "patch.apply.abort.and.rollback.action": "중단 및 롤백(_A)",
        "patch.apply.skip.action": "건너뛰기(_S)",
        "patch.apply.continue.resolve.action": "해결 계속",
        "patch.apply.can.t.find.patch.file.warning": "{0} 패치 파일을 찾을 수 없습니다",
        "patch.apply.not.patch.type.file.error": "선택한 파일 {0}은(는) 패치 유형 파일이 아닙니다",
        "patch.apply.not.patch": "콘텐츠가 패치가 아닙니다",
        "patch.apply.not.patch.clipboard": "클립보드 콘텐츠가 패치가 아닙니다",
        "patch.apply.can.not.apply.additional.info.error": "추가 패치 정보를 적용할 수 없습니다: {0}",
        "patch.apply.missing.base.file.label": "기본 누락됨",
        "patch.apply.change.directory.paths.group": "디렉터리 경로 변경",
        "patch.apply.cannot.read.patch": "{0} 패치를 읽을 수 없음: {1}",
        "patch.apply.map.base.directory.action": "기본 디렉터리 매핑\\u2026",
        "patch.apply.select.base.for.a.path.message": "경로의 기본 선택",
        "path.apply.select.base.directory.for.a.path.popup": "경로의 기본 디렉터리 선택",
        "patch.apply.new.base.detected.node.description": "새 기본이 감지됨",
        "patch.apply.select.missing.base.link": "누락된 기본 선택",
        "patch.apply.modified.status": "수정됨",
        "patch.apply.deleted.status": "삭제됨",
        "patch.apply.added.status": "추가됨",
        "patch.apply.stripped.description": "\\ 벗겨낸 {0}",
        "patch.apply.old.new.base.info": "이전: {0} (기본 디렉터리: {1})<br/>현재: {2} (기본 디렉터리: {3})",
        "patch.apply.select.base.title": "{0, choice, 0#디렉터리|1#파일} 기본 선택",
        "patch.apply.analyze.from.clipboard.on.the.fly.checkbox": "클립보드의 패치를 실시간으로 분석하고 적용",
        "patch.apply.wrong.base.and.can.t.be.applied.warning": "{0}에 대한 패치의 기본이 잘못되어 제대로 적용할 수 없습니다",
        "patch.apply.already.exists.overwrite.prompt": "{0} ({1}) 파일이 이미 존재합니다.\\n덮어쓰시겠습니까?",
        "patch.apply.bad.diff.to.title": "{0} 패치 적용 결과",
        "patch.apply.bad.diff.title": "패치 적용 결과",
        "patch.apply.already.applied.status": "이미 적용됨",
        "patch.apply.automatically.applied.status": "자동으로 적용됨",
        "patch.apply.not.applied.status": "적용되지 않음"
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