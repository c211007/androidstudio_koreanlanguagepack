import json
import os

translated_keys = {
  "action.Vcs.Log.AlignLabels.text": "왼쪽에 참조 표시",
  "action.Vcs.Log.AlignLabels.description": "커밋 메시지의 왼쪽에 참조를 표시합니다.",
  "action.Vcs.Log.ShowChangesFromParents.description": "병합된 각 커밋의 변경 사항을 따로 표시합니다.",
  "action.Vcs.Log.CompactReferencesView.description": "테이블에 커밋에 대한 첫 번째 참조만 표시합니다.",
  "action.Vcs.Log.ShowDetailsAction.description": "세부 정보 패널 표시",
  "action.Vcs.Log.ShowDiffPreview.description": "Diff 미리보기 패널 표시",
  "action.Vcs.Log.ShowLongEdges.description": "현재 보기에서 커밋이 보이지 않더라도 긴 브랜치 가장자리를 표시합니다.",
  "action.Vcs.Log.ShowOnlyAffectedChanges.description": "\"경로\" 메뉴에서 선택한 파일에 영향을 미치는 변경 사항만 표시합니다.",
  "action.Vcs.Log.ShowTagNames.description": "테이블에 태그 이름 표시",
  "vcs.log.action.description.open.new.tab.with.log": "{0} 로그가 있는 새 탭 열기",
  "vcs.log.action.description.open.new.tab.with.log.in.editor": "편집기에서 {0} 로그가 있는 새 탭 열기",
  "action.Vcs.Log.ShowDiffPreview.text": "Diff 미리보기 표시",
  "action.Vcs.Log.MoveDiffPreviewToBottom.text": "하단",
  "action.Vcs.Log.MoveDiffPreviewToBottom.description": "하단에 Diff 미리보기 위치",
  "action.Vcs.Log.MoveDiffPreviewToRight.text": "우측",
  "action.Vcs.Log.MoveDiffPreviewToRight.description": "우측에 Diff 미리보기 위치",
  "action.Vcs.Log.ShowChangesFromParents.text": "상위 변경 사항 표시",
  "action.vcs.log.show.separator": "표시",
  "action.Vcs.Log.CompactReferencesView.text": "참조 축소 보기",
  "action.Vcs.Log.ShowDetailsAction.text": "세부 정보 표시",
  "action.Vcs.Log.ShowLongEdges.text": "긴 가장자리",
  "action.Vcs.Log.ShowOnlyAffectedChanges.text": "영향을 받는 변경 사항만 표시",
  "action.Vcs.Log.ShowRootsColumnAction.text": "루트 이름",
  "action.Vcs.Log.ShowTagNames.text": "태그 이름",
  "action.Vcs.Log.PreferCommitDate.text": "커밋 타임스탬프",
  "prefer.commit.timestamp.action.text.show": "커밋 타임스탬프 표시",
  "action.Vcs.Log.PreferCommitDate.description": "작성된 시간이 아닌 변경 사항이 커밋된 시간을 표시합니다.",
  "vcs.log.action.open.new.tab.with.log": "새 {0} 로그 탭 열기",
  "vcs.log.action.open.new.tab.with.log.in.editor": "새 {0} 로그 편집기 탭 열기",
  "action.process.expanding.linear.branches": "선형 브랜치 확장 중\\u2026",
  "action.process.expanding.merges": "병합 확장 중\\u2026",
  "action.description.expand.merges": "병합 확장",
  "action.title.expand.merges": "병합 확장",
  "action.vcs.log.branches.separator": "브랜치 작업",
  "action.description.expand.linear.branches": "선형 브랜치 확장",
  "action.title.expand.linear.branches": "선형 브랜치 확장",
  "action.process.collapsing.linear.branches": "선형 브랜치 축소 중\\u2026",
  "action.process.collapsing.merges": "병합 축소 중\\u2026",
  "action.description.collapse.merges": "병합 축소",
  "action.title.collapse.merges": "병합 축소",
  "action.description.collapse.linear.branches": "선형 브랜치 축소",
  "action.title.collapse.linear.branches": "선형 브랜치 축소",
  "action.title.match.case": "대소문자 일치",
  "action.title.match.case.only.supported": "대소문자 일치({0}만 해당)",
  "action.go.to.navigate.to": "{0}(으)로 이동",
  "action.go.to.select.child.to.navigate": "이동할 하위 선택",
  "action.go.to.select.parent.to.navigate": "이동할 상위 선택",
  "action.go.to.select.hash.subject.author.date.time": "{0} {1}, 작성자: {2}, 날짜: {3} {4}",
  "action.Vcs.Log.Refresh.text": "새로고침",
  "action.Vcs.Log.Refresh.description": "새 커밋을 확인하고 필요한 경우 로그를 새로고침합니다."
}

file_path = "c:/Users/klanary/Desktop/vscode 모음/android_korean/androidstudio_koreanlanguagepack/missing_translations/missing_keys_korean.json"
with open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)

file_found = False
for item in data["new_files"]:
    if item["filename"] == "VcsLogBundle.properties":
        item["keys"].update(translated_keys)
        file_found = True
        break

if not file_found:
    data["new_files"].append({
        "filename": "VcsLogBundle.properties",
        "keys": translated_keys
    })

with open(file_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Batch 1 translated successfully.")