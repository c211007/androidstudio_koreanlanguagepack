import json
import os

translated_keys = {
  "vcs.log.show.commit.in.log.process": "로그에서 커밋 {0} 검색 중",
  "file.history.commit.not.found.in.branch": "선택한 브랜치의 {1}에 대한 히스토리에 {0}이(가) 없습니다.",
  "file.history.commit.not.found": "{1}에 대한 히스토리에 {0}이(가) 없습니다.",
  "file.history.commit.not.found.view.and.show.all.branches.link": "모든 브랜치 보기 및 표시",
  "file.history.commit.not.found.view.in.log.link": "로그에서 보기",
  "file.history.show.commit.in.history.process": "파일 히스토리에서 커밋 {0} 검색 중",
  "vcs.log.status.bar.indexing.cancel.tooltip": "인덱싱을 취소합니다. {0} 로그 툴바에서 인덱싱을 수동으로 다시 시작할 수 있습니다.",
  "vcs.log.status.bar.indexing.cancel.cancelling": "취소 중",
  "vcs.log.status.bar.indexing": "{0} 로그 인덱싱 중\\u2026",
  "vcs.log.creating.process": "커밋 로드 중\\u2026",
  "vcs.log.loading.selected.details.process": "선택한 세부 정보 로드 중",
  "vcs.log.applying.filters.process": "필터 적용 중\\u2026",
  "vcs.log.tab.name": "로그",
  "vcs.log.diff.preview.editor.empty.tab.name": "저장소 Diff",
  "vcs.log.diff.preview.editor.tab.name": "저장소 Diff: {0}",
  "vcs.log.editor.name": "VCS 로그 편집기",
  "vcs.log.filter.all": "모두",
  "vcs.log.filter.clear": "지우기",
  "vcs.log.filter.recent": "최근",
  "vcs.log.filter.structure.presentation.with.prefix": "{0}에 대한",
  "vcs.log.filter.root.presentation.with.prefix": "{0}에서",
  "vcs.log.filter.branch.presentation.with.prefix": "{0}의",
  "vcs.log.filter.date.presentation.with.prefix.made.between": "{0}과 {1} 사이에 작성됨",
  "vcs.log.filter.date.presentation.with.prefix.made.after": "{0} 이후에 작성됨",
  "vcs.log.filter.date.presentation.with.prefix.made.before": "{0} 이전까지 작성됨",
  "vcs.log.filter.date.display.name.between": "{0}과 {1} 사이",
  "vcs.log.filter.date.display.name.after": "{0} 이후",
  "vcs.log.filter.date.display.name.before": "{0} 이전까지",
  "vcs.log.filter.user.presentation.with.prefix": "작성자 {0}",
  "vcs.log.filter.text.presentation.with.prefix": "{0} 포함",
  "vcs.log.filter.text.hash.tooltip": "커밋 메시지 또는 해시로 필터링",
  "vcs.log.filter.text.hash.empty.text": "텍스트 또는 해시",
  "vcs.log.filter.popup.no.roots": "루트 없음",
  "vcs.log.filter.popup.no.folders": "경로 없음",
  "vcs.log.filter.popup.no.items": "항목 없음",
  "vcs.log.filter.popup.paths": "경로",
  "vcs.log.date.filter.label": "날짜",
  "vcs.log.branch.filter.label": "브랜치",
  "vcs.log.branch.filter.favorites": "즐겨찾기",
  "vcs.log.user.filter.label": "사용자",
  "vcs.log.user.filter.me": "나",
  "vcs.log.date.filter.since": "{0} 이후",
  "vcs.log.date.filter.until": "{0} 이전까지",
  "vcs.log.date.filter.action.last.day": "지난 24시간",
  "vcs.log.date.filter.action.last.week": "지난 7일",
  "vcs.log.date.filter.select.period.dialog.title": "기간 선택",
  "vcs.log.filter.action.select": "선택\\u2026",
  "vcs.log.select.folder.dialog.title": "필터링할 경로 선택",
  "vcs.log.filters.structure.label": "선택됨: {0}",
  "vcs.log.filters.structure.max.selected.error.message": "{0}개의 요소를 추가했습니다. 더 이상 허용되지 않습니다."
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

print("Batch 4 translated successfully.")