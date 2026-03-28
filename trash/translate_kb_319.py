import json
import os

translated_keys = {
  "vcs.log.filter.roots": "루트",
  "vcs.log.filter.tooltip.click.to.see.only": "{1}만 보려면 {0}+클릭하세요",
  "vcs.log.filter.tooltip.no.roots.selected": "선택된 루트 없음",
  "vcs.log.filter.tooltip.roots": "루트:",
  "vcs.log.filter.tooltip.folders": "경로:",
  "vcs.log.filter.popup.advertisement.text": "{0}(으)로 구분된 하나 이상의 값을 선택하세요",
  "vcs.log.filter.popup.advertisement.text.new.lines": "새 줄",
  "vcs.log.filter.popup.advertisement.text.or.suffix": "또는 {0}",
  "vcs.log.filter.popup.advertisement.with.key.text": "{0}(으)로 구분된 하나 이상의 값을 선택하세요. 마치려면 {1}을(를) 사용하세요.",
  "vcs.log.filter.select.folders": "트리에서 선택\\u2026",
  "vcs.log.filter.edit.folders": "선택\\u2026",
  "vcs.log.filter.no.merges": "병합 없음",
  "vcs.log.text.filter.action.text": "텍스트 또는 해시로 필터링",
  "vcs.log.branch.filter.action.text": "브랜치로 필터링",
  "vcs.log.user.filter.action.text": "사용자로 필터링",
  "vcs.log.date.filter.action.text": "날짜로 필터링",
  "vcs.log.path.filter.action.text": "경로로 필터링",
  "vcs.log.details.in.branches.loading": "브랜치: 로드 중\\u2026",
  "vcs.log.details.in.branches.empty": "어떤 브랜치에도 없음",
  "vcs.log.details.in.branches.hide": "숨기기",
  "vcs.log.details.in.branches.show.all": "모두 표시",
  "vcs.log.details.in.branches": "{0,choice,1#{0}개 브랜치|2# {0}개 브랜치}에 있음:",
  "vcs.log.details.committer.info.user.date.time": "{0}이(가) {1} {2}에 커밋함",
  "vcs.log.details.committer.info.date.time": "{0} {1}에 커밋됨",
  "vcs.log.details.author.on.date.at.time": "{0}, 날짜: {1} {2}",
  "vcs.log.details.committer.info.user": "{0}이(가) 커밋함",
  "vcs.log.details.showing.selected.commits": "(선택한 {1}개 커밋 중 {0}개 표시)",
  "vcs.log.details.references.more.label": "... 기타 {0}개",
  "loading.commit.changes": "커밋 변경 사항 로드 중",
  "vcs.log.commit.details.status": "커밋 세부 정보",
  "vcs.log.changes.select.commits.to.view.changes.status": "변경 사항을 볼 커밋을 선택하세요.",
  "vcs.log.changes.no.merge.conflicts.status": "병합된 충돌이 없습니다.",
  "vcs.log.changes.show.changes.to.parents.status.action": "상위 변경 사항 표시",
  "vcs.log.changes.no.changes.that.affect.selected.paths.status": "선택한 경로에 영향을 미치는 변경 사항이 없습니다.",
  "vcs.log.changes.show.all.paths.status.action": "모든 경로의 변경 사항 표시",
  "vcs.log.changes.details.no.commits.selected.status": "선택한 커밋 없음",
  "vcs.log.changes.too.many.status": "{0,choice,1#이 커밋|2#선택한 커밋 중 하나}에 변경 사항이 {1}개 있습니다.",
  "vcs.log.changes.too.many.show.anyway.status.action": "계속 표시",
  "vcs.log.changes.no.merge.conflicts.node": "병합된 충돌 없음",
  "vcs.log.changes.changes.to.parent.node": "{0}에 대한 변경 사항",
  "vcs.log.action.highlight.current.branch": "현재 브랜치",
  "vcs.log.action.highlight.indexed.commits": "인덱스된 커밋",
  "vcs.log.action.highlight.merge.commits": "병합 커밋",
  "vcs.log.action.highlight.my.commits": "내 커밋",
  "action.vcs.log.highlight.separator": "강조 표시",
  "vcs.log.fatal.error.message": "{0}에서 캐시를 무효화할 수 없습니다.\\n캐시 디렉토리를 수동으로 삭제하고 {1}을(를) 다시 시작하세요.",
  "vcs.log.is.not.available": "VCS 로그를 사용할 수 없습니다",
  "vcs.log.clear.caches.checkbox.description": "VCS 로그 캐시 및 인덱스 지우기",
  "vcs.log.invalidate.caches.text": "{0} 로그 캐시 및 인덱스 무효화",
  "vcs.log.invalidate.caches.progress": "{0} 로그 캐시 및 인덱스 무효화 중"
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

print("Batch 5 translated successfully.")