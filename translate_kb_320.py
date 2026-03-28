import json
import os

translated_keys = {
  "vcs.log.index.diagnostic.action.title": "이전 커밋에 대한 VCS 로그 인덱스 데이터 확인",
  "vcs.log.index.diagnostic.selected.action.title": "선택한 커밋에 대한 VCS 로그 인덱스 데이터 확인",
  "vcs.log.index.diagnostic.selected.non.indexed.warning.message": "선택한 커밋이 인덱싱되지 않았습니다.",
  "vcs.log.index.diagnostic.progress.title": "VCS 로그 인덱스 진단 실행 중",
  "vcs.log.index.diagnostic.success.message": "확인된 {0}개의 {0,choice,1#커밋|2#커밋}에 대한 VCS 로그 인덱스 데이터가 올바릅니다.",
  "vcs.log.index.diagnostic.report.title": "VCS 로그 인덱스 진단 보고서 {0}",
  "vcs.log.index.diagnostic.error.for.commit": "커밋 {0}에 대한 Diff\\n{1}",
  "vcs.log.index.diagnostic.error.message": "예상된 {0}: {1}, 실제 {0}: {2}",
  "vcs.log.index.diagnostic.error.attribute.name.author.time": "작성자 날짜",
  "vcs.log.index.diagnostic.error.attribute.name.author": "작성자",
  "vcs.log.index.diagnostic.error.attribute.name.committer.time": "커밋 날짜",
  "vcs.log.index.diagnostic.error.attribute.name.committer": "커미터",
  "vcs.log.index.diagnostic.error.attribute.name.message": "메시지",
  "vcs.log.index.diagnostic.error.attribute.name.parents": "상위",
  "vcs.log.index.diagnostic.error.filter": "{0}(으)로 필터링해도 {1}이(가) 반환되지 않습니다.",
  "action.Vcs.Log.ShowBigRepositories.text": "인덱싱이 비활성화된 저장소 분",
  "vcs.log.big.repositories.dialog.title": "인덱싱이 비활성화된 저장소",
  "vcs.log.column.subject": "제목",
  "vcs.log.column.author": "작성자",
  "vcs.log.column.date": "날짜",
  "vcs.log.column.hash": "해시",
  "graph.options.linear": "병합 선형화",
  "graph.options.linear.description": "병합의 경우 마치 리베이스된 것처럼 메인 브랜치 커밋 위에 들어오는 커밋을 표시합니다.",
  "graph.options.linear.presentation": "선형화됨",
  "graph.options.first.parent": "첫 번째 상위",
  "graph.options.first.parent.description": "병합 커밋을 볼 때 첫 번째 상위 커밋만 따릅니다.",
  "graph.sort.standard": "토폴로지 방식",
  "graph.sort.standard.description": "병합의 경우 수신 커밋을 병합 커밋 바로 아래에 먼저 표시합니다.",
  "graph.sort.off": "커밋 날짜 기준",
  "graph.sort.off.description": "커밋을 토폴로지 및 커밋 날짜를 기준으로 정렬합니다.",
  "vcs.log.table.accessible.name": "{0} 로그",
  "vcs.log.changes.accessible.name": "커밋 변경 사항 브라우저",
  "vcs.log.text.filter.accessible.name": "{0} 로그 텍스트 또는 해시 필터",
  "vcs.log.filter.accessible.name": "{0}: {1}",
  "vcs.log.failed.loading.details": "{1}에서 커밋 {0}에 대한 세부 정보를 로드할 수 없습니다.",
  "vcs.log.settings.group.title": "로그",
  "vcs.log.settings.group.indexing.title": "인덱싱",
  "vcs.log.settings.enable.index.checkbox": "프로젝트에 대해 인덱싱 활성화{0,choice,0#|1# ({1}만 해당)}",
  "vcs.log.settings.enable.index.checkbox.comment": "IDE 전반에서 변경 사항 히스토리 작업 환경을 개선하려면",
  "vcs.log.settings.visible.columns": "표시되는 열",
  "vcs.log.settings.diff.preview.location": "위치:",
  "vcs.log.settings.group.file.history.title": "파일 히스토리",
  "vcs.log.settings.show.file.names": "파일 이름 표시",
  "vcs.log.bookmark.description.empty.subject": "(메시지 없음)",
  "vcs.log.bookmark.label": "북마크",
  "vcs.log.bookmark.label.mnemonic": "북마크 ''{0}''",
  "vcs.log.wip.label": "새 커밋\\u2026"
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

print("Batch 6 translated successfully.")