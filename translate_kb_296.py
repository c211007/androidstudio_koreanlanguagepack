import json

def update_json():
    file_path = "missing_translations/missing_keys_korean.json"
    target_file = "VcsBundle.properties"
    
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    translations = {
        "patch.apply.somehow.diff.name": "패치 임의 적용",
        "patch.apply.changes.in.patch.resolve": "패치 해결 중 {0}",
        "patch.apply.display.local.content.was.modified.error": "패치 적용기를 표시하지 못했습니다 - 로컬 콘텐츠가 수정되었습니다.",
        "patch.content.viewer.name": "패치 뷰어",
        "patch.content.viewer.side.by.side.name": "나란히 보기 패치 뷰어",
        "patch.apply.marker.renderer": "마커: {0}",
        "patch.apply.syntax.line": "\\ (줄: {0})",
        "patch.apply.hunk.warning": "-{0},{1} +{2},{3}에 대한 청크 수정 줄을 감지할 수 없습니다",
        "patch.binary.decoder.content.error": "예상보다 {0,choice,0#적은|1#많은} 바이너리 콘텐츠가 디코딩되었습니다",
        "patch.binary.decoder.line.error": "바이너리 파일 패치를 인코딩할 수 없음: 잘못된 줄 크기",
        "patch.binary.decoder.char.error": "바이너리 파일 패치를 디코딩할 수 없음: 잘못된 문자 크기 기호",
        "patch.binary.decoder.decompress.error": "바이너리 파일 패치를 디코딩할 수 없음: 데이터를 압축 해제할 수 없음",
        "patch.simple.apply.base.line.error": "예기치 않은 기준선: 예상 - {0}, 실제 - {1}",
        "patch.simple.apply.base.line.total.error": "예기치 않은 기준선: 총 줄 수 - {0}, 실제 - {1}",
        "patch.simple.apply.hunk.base.start.error": "예기치 않은 청크 기준선 시작: 예상  - {0}, 실제 - {1}",
        "patch.simple.apply.hunk.patched.start.error": "예기치 않은 청크 패치 시작: 예상  - {0}, 실제 - {1}",
        "patch.simple.apply.hunk.base.end.error": "예기치 않은 청크 기준 종료: 총 줄 수  - {0}, 청크 종료 - {1}",
        "patch.simple.apply.hunk.base.body.error": "예기치 않은 청크 기준 본문: 예상 - {0}, 실제 - {1}",
        "patch.simple.apply.hunk.patched.body.error": "예기치 않은 청크 패치 본문: 예상 - {0}, 실제 - {1}",
        "patch.simple.apply.hunk.content.error": "예기치 않은 청크 본문: 예상 - {0}, 실제 - {1}",
        "patch.copied.to.clipboard": "패치가 클립보드에 복사되었습니다",
        "patch.creation.failed": "패치 생성 실패",
        "patch.creation.save.patch.file.title": "패치 파일 저장",
        "patch.creation.can.not.write.patch.error": "지정된 파일에 패치를 쓸 수 없습니다: {0}",
        "patch.creation.save.to.title": "패치 저장 위치",
        "patch.creation.save.to.file.button": "파일에 패치 저장",
        "patch.creation.base.path.field": "기본 경로(&B):",
        "patch.creation.wrong.base.path.for.changes.error": "기본 경로에 선택한 모든 변경 사항이 포함되어 있지 않습니다({0} 사용)",
        "patch.creation.base.dir.does.not.exist.error": "기본 디렉터리가 존재하지 않습니다",
        "patch.creation.empty.base.path.error": "기본 경로는 비워 둘 수 없습니다!",
        "patch.creation.name.too.long.error": "파일 경로가 너무 길면 안 됩니다.",
        "patch.import.to.shelf.progress.title": "선반으로 패치 가져오기",
        "patch.import.to.shelf.tab": "선반으로 패치 가져오기",
        "patch.import.no.patches.found.warning": "패치를 찾을 수 없음",
        "patch.import.additional.info.error": "추가 패치 정보를 가져올 수 없습니다: {0}",
        "action.import.to.shelf": "선반으로 가져오기",
        "shelve.changes.action": "변경 사항 보류(_S)",
        "shelve.changes.progress.title": "변경 사항 보류 중",
        "shelve.changes.progress.text": "변경 사항 보류 중\\u2026",
        "shelve.file.is.locked.for.editing.message": "보류 중인 동안 파일이 편집을 위해 잠겨 있습니다",
        "shelve.remove.successfully.applied.files.checkbox": "선반에서 성공적으로 적용된 파일 제거",
        "shelve.delete.already.unshelved.label": "이미 보류 해제된 변경 목록 삭제:",
        "shelve.base.content.not.found.or.not.applicable.error": "기본 콘텐츠를 찾을 수 없거나 적용할 수 없습니다. 로컬 버전과의 차이를 표시합니다",
        "shelve.shelved.version": "보류된 버전",
        "shelve.import.one.patch.file.prompt": "패치 파일 1개({0})를 찾았습니다.\\n가져오기를 계속하시겠습니까?",
        "shelve.import.patches.prompt": "패치 파일 {0}개를 찾았습니다.\\n가져오기를 계속하시겠습니까?",
        "shelve.show.already.unshelved.action": "이미 보류 해제됨",
        "shelve.delete.files.successful.message": "{0,choice, 1#파일 1개|2#파일 {0}개}",
        "shelve.delete.changelist.name.message": "''{0}'' 변경 목록",
        "shelve.delete.changelists.count.message": "{0}개의 변경 목록"
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