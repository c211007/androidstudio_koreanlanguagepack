import json
import os

translated_keys = {
  "group.Vcs.Log.ChangesBrowser.PresentationSettings.text": "보기 옵션",
  "group.Vcs.Log.TextFilterSettings.text": "텍스트 필터 설정",
  "group.Vcs.Log.TextFilterSettings.description": "텍스트 필터 옵션 선택",
  "group.Vcs.Log.LayoutConfiguration.text": "레이아웃 구성",
  "group.Vcs.Log.LayoutConfiguration.separator.text": "레이아웃",
  "group.Vcs.Log.LayoutConfiguration.description": "창 레이아웃 구성",
  "group.Vcs.FileHistory.PresentationSettings.text": "보기 옵션",
  "group.Vcs.FileHistory.PresentationSettings.description": "파일 히스토리 보기 구성",
  "group.Log.KeymapGroup.text": "로그",
  "group.Vcs.Log.Diff.Preview.Location.text": "Diff 미리보기 위치",
  "group.Vcs.Log.Internal.text": "VCS 로그",
  "vcs.log.right.corner.toolbar": "VCS 로그 툴바",
  "vcs.log.changes.browser.toolbar": "VCS 로그 변경 사항 브라우저 툴바",
  "file.history.toolbar": "파일 히스토리 툴바",
  "dialog.title.paths.affected.by.commit": "커밋 {0}에 영향을 받는 경로",
  "vcs.log.click.to.collapse.paths.column.tooltip": "축소하려면 클릭하세요",
  "vcs.log.click.to.expand.paths.column.tooltip": "확장하려면 클릭하세요",
  "vcs.log.graph.arrow.tooltip.jump.to.subject.author.date.time": "{0} 작성자: {1} 날짜: {2} {3}(으)로 이동",
  "vcs.log.graph.arrow.tooltip.jump.to.hash": "커밋 {0}(으)로 이동",
  "vcs.log.graph.arrow.tooltip.jump.to.hash.in.root": "{1}의 커밋 {0}(으)로 이동",
  "vcs.log.references.more.tooltip": "... 세부 정보 창의 기타 {0}개",
  "filetype.vcs.log.description": "VCS 로그",
  "vcs": "VCS",
  "activity.tracker.vcs.log": "VCS 로그 인덱싱",
  "vcs.log.is.loading": "VCS 로그 로드 중\\u2026",
  "vcs.log.loading.status": "커밋 로드 중\\u2026",
  "vcs.log.error.loading.commits.status": "커밋을 로드하는 중 오류 발생",
  "vcs.log.error.loading.details.status": "커밋 세부 정보를 로드하는 중 오류 발생",
  "vcs.log.error.loading.changes.status": "변경 사항을 로드하는 중 오류 발생",
  "vcs.log.no.commits.status": "커밋된 변경 사항이 없습니다.",
  "vcs.log.commit.status.action": "로컬 변경 내용 커밋",
  "vcs.log.error.filtering.status": "커밋 필터링 중 오류 발생",
  "vcs.log.no.commits.matching.status": "필터와 일치하는 커밋이 없습니다.",
  "vcs.log.reset.filters.status.action": "필터 초기화",
  "vcs.log.refresh.status.action": "새로고침",
  "vcs.log.default.status": "변경 사항 로그",
  "vcs.log.duplicated.tab.id.error": "VCS 로그 탭은 두 번 열 수 없습니다.",
  "file.history.error.status": "파일 히스토리를 계산하는 중 오류 발생",
  "file.history.empty.status": "파일 히스토리",
  "file.history.reset.filters.status.action": "필터 초기화",
  "file.history.action.could.not.load.selected.commits.message": "선택한 커밋을 로드할 수 없습니다: {0}",
  "file.history.diff.preview.editor.tab.name": "히스토리: {0}",
  "vcs.log.go.to.hash.popup.label": "해시 또는 브랜치/태그 이름 입력:",
  "vcs.log.string.is.not.a.hash": "''{0}''은(는) 커밋 해시처럼 보이지 않습니다.",
  "vcs.log.commit.not.found": "{0}을(를) 찾을 수 없습니다",
  "vcs.log.commit.does.not.match": "{0}이(가) 필터와 일치하지 않습니다.",
  "vcs.log.commit.prefix": "커밋 ''{0}''",
  "vcs.log.commit.or.reference.prefix": "커밋 또는 참조 ''{0}''",
  "vcs.log.commit.does.not.match.view.and.reset.link": "필터 보기 및 초기화",
  "vcs.log.commit.does.not.match.view.in.tab.link": "새 탭에서 보기"
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

print("Batch 3 translated successfully.")