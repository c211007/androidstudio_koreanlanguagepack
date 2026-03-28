import json
from pathlib import Path

def update_missing_keys():
    file_path = Path("missing_translations/missing_keys_korean.json")
    
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    ko_dict = {
        "activity.empty.text.loading": "로드 중…",
        "activity.list.empty.text.recent": "최근 활동이 감지되지 않았습니다.",
        "activity.list.empty.text.recent.matching": "일치하는 최근 활동이 감지되지 않았습니다.",
        "activity.list.empty.text.in.scope": "{0}에서 활동이 감지되지 않았습니다.",
        "activity.list.empty.text.in.scope.matching": "{0}에서 일치하는 활동이 감지되지 않았습니다.",
        "activity.list.accessible.name": "활동 히스토리",
        "activity.item.presentation": "변경",
        "activity.item.presentation.from.path": "{0} 변경",
        "activity.item.presentation.from.paths": "{0} 외 {1}개 변경",
        "activity.item.presentation.create.path": "{0} 생성",
        "activity.item.presentation.delete.path": "{0} 삭제",
        "activity.item.presentation.rename.path": "{0}을(를) {1}(으)로 이름 바꾸기",
        "activity.item.presentation.move.path": "{0}을(를) {1}(으)로 이동",
        "activity.item.presentation.modify.path": "{0} 수정",
        "activity.filter.empty.text.content": "내용으로 검색",
        "activity.filter.empty.text.fileName": "파일 이름으로 검색",
        "activity.browser.empty.text": "변경 사항이 감지되지 않았습니다.",
        "activity.browser.empty.text.no.selection": "변경 사항을 보려면 활동을 선택하세요.",
        "activity.browser.diff.mode.presentation.local": "로컬 디렉터리",
        "activity.browser.diff.mode.presentation.next": "다음 리비전",
        "activity.browser.diff.mode.text": "{0}와(과) 차이를 비교합니다.",
        "activity.browser.diff.mode.link": "{0}와(과) 차이 비교로 전환",
        "activity.diff.tab.title": "로컬 히스토리 차이",
        "activity.diff.tab.title.recent": "최근 로컬 히스토리 차이",
        "activity.diff.tab.title.file": "로컬 히스토리: {0}",
        "activity.diff.content.title": "{0} 이전",
        "activity.action.patch.collecting.diff": "차이점 수집 중",
        "action.ActivityView.Revert.text": "선택사항 및 이후 변경 사항 되돌리기",
        "action.ActivityView.RevertDifferences.text": "선택 사항 되돌리기",
        "action.ActivityView.CreatePatch.text": "패치 생성…",
        "group.ActivityView.Options.text": "보기 옵션",
        "action.ActivityView.ShowSystemLabelsAction.text": "시스템 이벤트 표시",
        "notification.group.general": "로컬 히스토리 메시지",
        "notification.title.local.history.broken": "로컬 히스토리가 손상되었습니다",
        "notification.content.local.history.broken": "로컬 히스토리 저장소 파일이 손상되어 다시 빌드됩니다.",
        "notification.content.label.name.created": "레이블 {0} 생성됨",
        "notification.action.view.local.history": "로컬 히스토리 보기",
        "notification.content.label.creation.failed": "레이블 {0}을(를) 생성할 수 없습니다",
        "dialog.title.revert": "되돌리기",
        "message.do.you.want.to.proceed": "{0}\\n\\n계속하시겠습니까?"
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
