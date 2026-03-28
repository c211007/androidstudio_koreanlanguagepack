import json
import os

translated_keys = {
  "action.title.enable.indexing": "{0} 로그 인덱싱 활성화",
  "action.description.was.disabled": "{0} 인덱싱이 비활성화되었습니다. 활성화합니다.",
  "action.title.resume.indexing": "{0} 로그 인덱싱 재개",
  "action.description.was.paused": "{0} 인덱싱이 일시 중지되었습니다. 재개합니다.",
  "action.description.is.scheduled": "{0} 인덱싱이 예약되었습니다. 일시 중지합니다.",
  "action.title.pause.indexing": "{0} 로그 인덱싱 일시 중지",
  "action.help.tooltip.resume.indexing": "프로젝트 저장소 인덱싱은 IDE 전반의 변경 사항 히스토리 작업 환경을 개선합니다:<br/>\n  - 빠른 로그 필터링 및 정확한 히스토리 계산<br/>\n  - 개정을 위한 파일 히스토리의 브랜치 필터<br/>\n  - 통합 검색에서 히스토리 전반을 검색",
  "group.Vcs.Log.ToggleColumns.description": "테이블에 표시할 열 선택",
  "group.Vcs.Log.ToggleColumns.text": "열",
  "action.Vcs.Log.FocusTextFilter.text": "텍스트 필터에 포커스",
  "action.Vcs.Log.FocusTextFilter.description": "텍스트 필터에 포커스를 주거나 커밋 목록으로 다시 포커스 이동",
  "action.vcs.log.sort.type.separator": "정렬",
  "group.Vcs.Log.GraphOptionsGroup.text": "그래프 옵션",
  "group.Vcs.Log.GraphOptionsGroup.description": "VCS 로그 그래프 옵션 및 작업",
  "action.vcs.log.graph.options.separator": "옵션",
  "action.ShowCommitTooltipAction.text": "커밋 툴팁 표시",
  "action.ShowCommitTooltipAction.description": "로그에서 현재 선택한 커밋의 툴팁 표시",
  "action.presentation.CompareRevisionsFromFileHistoryActionProvider.text.compare": "비교",
  "action.presentation.CompareRevisionsFromFileHistoryActionProvider.text.show.diff": "Diff 표시",
  "action.presentation.CompareRevisionsFromFileHistoryActionProvider.description.compare": "선택한 버전 비교",
  "action.presentation.CompareRevisionsFromFileHistoryActionProvider.description.show.diff": "이전 버전과의 Diff 표시",
  "action.Vcs.Log.GoToRef.text": "해시/브랜치/태그로 이동(&G)",
  "action.Vcs.Log.GoToRef.description": "이동할 커밋을 가리키는 태그나 브랜치의 해시 또는 이름을 지정합니다.",
  "action.Vcs.Log.GoToParent.text": "상위 커밋으로 이동",
  "action.Vcs.Log.GoToParent.description": "커밋 그래프의 상위 행으로 이동합니다.",
  "action.Vcs.Log.GoToChild.text": "하위 커밋으로 이동",
  "action.Vcs.Log.GoToChild.description": "커밋 그래프의 하위 행으로 이동합니다.",
  "action.Vcs.Show.Log.text": "VCS 로그 표시",
  "action.Vcs.Show.Log.text.template": "{0} 로그 표시",
  "action.Vcs.Log.ShowTooltip.text": "커밋 툴팁 표시",
  "action.Vcs.Log.ShowTooltip.description": "로그에서 현재 선택한 커밋의 툴팁 표시",
  "action.Vcs.Log.EnableFilterByRegexAction.text": "정규식(Regex)",
  "action.Vcs.Log.MatchCaseAction.text": "대소문자 일치",
  "action.Vcs.Log.OpenRepositoryVersion.text": "개정에서 파일 표시",
  "action.Vcs.Log.OpenRepositoryVersion.description": "파일의 선택한 개정으로 편집기 열기",
  "action.Vcs.Log.AnnotateRevisionAction.text": "어노테이션 추가",
  "action.Vcs.Log.AnnotateRevisionAction.description": "선택한 개정에 어노테이션 추가",
  "action.Vcs.Log.ShowAllAffected.text": "영향을 받는 모든 파일 표시",
  "action.Vcs.Log.ShowAllAffected.description": "선택한 개정에서 수행된 모든 변경 사항 표시",
  "action.Vcs.Log.CompareRevisions.text": "버전 비교",
  "action.Vcs.Log.CompareRevisions.description": "선택한 버전 비교",
  "action.Vcs.Log.ResumeIndexing.text": "인덱싱 재개",
  "action.Vcs.Log.ResumeIndexing.description": "예상보다 오래 걸려 인덱싱이 일시 중지되었습니다. 재개합니다.",
  "action.Vcs.Log.SelectInLog.text": "VCS 로그에서 표시",
  "action.Vcs.Log.SelectInLog.text.template": "{0} 로그에서 표시",
  "vcs.log.action.show.in.file.history.text": "파일 히스토리에 표시",
  "action.Vcs.Log.ShowSettingsAction.text": "설정",
  "action.Vcs.Log.ShowSettingsAction.GoToAction.text": "VCS 로그 설정",
  "group.Vcs.Log.PresentationSettings.text": "보기 옵션",
  "group.Vcs.Log.PresentationSettings.description": "로그의 표시 방법 구성"
}

file_path = "c:/Users/klanary/Desktop/vscode 모음/android_korean/androidstudio_koreanlanguagepack/missing_translations/missing_keys_korean.json"
with open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)

for item in data["new_files"]:
    if item["filename"] == "VcsLogBundle.properties":
        item["keys"].update(translated_keys)
        break

with open(file_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Batch 2 translated successfully.")