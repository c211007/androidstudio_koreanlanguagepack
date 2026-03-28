import json
from pathlib import Path

def update_missing_keys():
    file_path = Path("missing_translations/missing_keys_korean.json")
    
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    ko_dict = {
        "revisions.table.period.recent": "지난 {0}시간",
        "revisions.table.period.older": "이전",
        "revisions.table.period.old": "오래된 변경 사항",
        "revisions.table.filesCount": "파일 {0}개",
        "current.revision": "현재",
        "file.does.not.exist": "파일이 없습니다.",
        "content.not.available": "파일 내용을 사용할 수 없습니다.",
        "action.show.difference": "차이점 표시",
        "action.revert": "되돌리기",
        "action.create.patch": "패치 생성…",
        "action.revert.selection": "선택 항목 되돌리기",
        "message.patch.copied.to.clipboard": "패치가 클립보드에 복사되었습니다.",
        "message.patch.created": "패치 파일이 생성되었습니다.",
        "message.processing.revisions": "리비전 처리 중…",
        "message.processing.left.revision": "왼쪽 리비전 처리 중…",
        "message.processing.right.revision": "오른쪽 리비전 처리 중…",
        "message.cannot.revert.because": "{0}(으)로 인해 되돌릴 수 없습니다.",
        "message.cannot.create.patch.because.of.unavailable.content": "선택한 일부 파일의 내용이 너무 커서 저장되지 않았기 때문에 패치를 생성할 수 없습니다.",
        "message.error.during.revert": "되돌리기 중 오류 발생: {0}",
        "message.error.during.create.patch": "패치 생성 중 오류 발생: {0}",
        "create.patch.dialog.title": "패치 생성",
        "put.label.dialog.title": "레이블 지정",
        "put.label.name": "레이블 이름(&N):",
        "recent.changes.loading": "최근 변경 사항 로드 중",
        "recent.changes.popup.title": "최근 변경 사항",
        "recent.changes.to.changes": "변경 사항이 없습니다",
        "activity.name.external.change": "외부 변경",
        "activity.name.revert.to.date": "{0}(으)로 되돌리기",
        "activity.name.revert.to.change.date": "{1}의 ''{0}''(으)로 되돌리기",
        "activity.name.revert": "되돌리기",
        "activity.name.revert.date": "{0} 되돌리기",
        "activity.name.revert.change.date": "{1}의 ''{0}'' 되돌리기",
        "revert.error.files.are.read.only": "일부 파일이 읽기 전용입니다",
        "group.LocalHistory.text": "로컬 히스토리(&H)",
        "action.LocalHistory.ShowHistory.text": "히스토리 표시(&H)…",
        "action.LocalHistory.ShowHistory.GoToAction.text": "로컬 히스토리 표시…",
        "action.LocalHistory.ShowHistory.ActionPlace.VcsQuickListPopupAction.text": "로컬 히스토리 표시…",
        "action.LocalHistory.ShowSelectionHistory.text": "선택 항목에 대한 로컬 히스토리 표시…",
        "action.LocalHistory.ShowSelectionHistory.GoToAction.text": "선택 항목의 로컬 히스토리 표시…",
        "action.synonym.LocalHistory.ShowSelectionHistory.method.text": "메서드의 로컬 히스토리 표시…",
        "action.synonym.LocalHistory.ShowSelectionHistory.class.text": "클래스의 로컬 히스토리 표시…",
        "action.LocalHistory.ShowProjectHistory.text": "프로젝트 로컬 히스토리 표시…",
        "action.LocalHistory.ShowProjectHistory.GoToAction.text": "프로젝트의 로컬 히스토리 표시…",
        "action.LocalHistory.ShowProjectHistory.Vcs.Toolbar.Widget.text": "로컬 히스토리…",
        "action.LocalHistory.PutLabel.text": "레이블 입력(&L)…",
        "action.RecentChanges.text": "최근 변경 사항(&E)",
        "action.ValidateLocalHistory.text": "로컬 히스토리 저장소 검증",
        "activity.toolwindow.title": "로컬 히스토리",
        "activity.dialog.title": "로컬 히스토리: {0}",
        "activity.recent.tab.title": "최근"
    }
    
    filename = "LocalHistoryBundle.properties"
    found = False
    for file_entry in data.get('new_files', []):
        if file_entry['filename'] == filename:
            file_entry['keys'].update(ko_dict)
            found = True
            break
    if not found:
        data.setdefault('new_files', []).append({"filename": filename, "keys": ko_dict})
    
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        
    print(f"Updated {filename}")

if __name__ == "__main__":
    update_missing_keys()
