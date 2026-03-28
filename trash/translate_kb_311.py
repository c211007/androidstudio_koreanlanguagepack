import json
import os

translated_keys = {
  "inlay.vcs.code.author.description": "VCS의 기록에 따른 코드 작성자입니다.<br><br>클래스, 메서드 또는 함수를 마지막으로 편집한 사람이 작성자입니다. 여러 작성자가 커밋한 내용이 있는 경우 가장 많은 줄을 소유한 사람이 작성자로 간주됩니다.",
  "label.new.code": "새로운 코드 *",
  "label.multi.author.modified.code": "{0} +{1} *",
  "label.multi.author.not.modified.code": "{0} +{1}",
  "label.single.author.modified.code": "{0} *",
  "jb.protocol.no.provider": "VCS 제공자를 찾을 수 없습니다: ''{0}''",
  "status.text.vcs.toolwindow": "코드 변경 내용을 추적하려면:",
  "status.text.vcs.toolwindow.emptyPrefix": "\\u2014",
  "status.text.vcs.toolwindow.shareProject": "다음에서 프로젝트 공유:",
  "status.text.vcs.toolwindow.shareProject.orOn": "또는",
  "status.text.vcs.toolwindow.create.repository": "Git 저장소 만들기\\u2026",
  "status.text.vcs.toolwindow.local.history": "로컬 히스토리 사용\\u2026",
  "status.text.vcs.toolwindow.help": "버전 관리 통합",
  "status.text.commit.toolwindow.create.repository.prefix": "변경 내용을 커밋하려면,",
  "status.text.commit.toolwindow.create.repository": "Git 저장소 만들기\\u2026",
  "status.text.commit.toolwindow.local.history.prefix": "최근 변경 내용을 보려면 다음을 확인하세요:",
  "status.text.commit.toolwindow.local.history": "로컬 히스토리\\u2026",
  "notification.group.external.executable": "VCS 외부 실행 파일 유효성 검사 실패",
  "saved.patch.empty.text": "스태시나 선반이 추가되지 않았습니다.",
  "saved.patch.changes.empty": "파일을 보려면 스태시 또는 선반을 선택하세요.",
  "saved.patch.changes.loading": "로드 중\\u2026",
  "saved.patch.editor.diff.preview.empty.title": "스태시 및 선반",
  "saved.patch.created.on.date.at.time.tooltip": "{1} {2}에 생성된 {0}",
  "saved.patch.pop.action": "팝(&P)",
  "saved.patch.apply.action": "적용(&A)",
  "saved.patch.apply.pop.help.tooltip": "<html>적용 \\&mdash; 목록에 스태시를<br/>\n  유지하면서 적용합니다.<br/> 팝 \\&mdash; 스태시를 적용하고<br/> 목록에서 제거합니다. </html>",
  "shelf.pop.action.description": "선택한 선반 팝",
  "shelf.apply.action.description": "선택한 선반 적용",
  "shelf.drop.action": "삭제(&D)",
  "shelf.drop.action.description": "선택한 선반 삭제",
  "shelf.unshelve.changes.action.text": "선반에서 빼기(&U)",
  "shelf.unshelve.changes.action.description": "선택한 변경 내용을 선반에서 뺍니다.",
  "shelf.unshelve.changes.remove.action.text": "선반에서 빼고 제거(&R)",
  "shelf.unshelve.changes.remove.action.description": "선택한 변경 내용을 선반에서 빼고 선반에서 제거합니다.",
  "shelf.root.node.title": "선반",
  "shelf.tooltip.title": "선반",
  "notification.group.vcs.messages": "VCS 메시지",
  "notification.group.vcs.common.messages": "VCS 일반 메시지",
  "notification.group.vcs.important.messages": "VCS 중요 메시지",
  "notification.group.vcs.notifications": "VCS 알림",
  "notification.group.vcs.silent.notifications": "VCS 무음 알림",
  "gutter.name.version.control.ignored.directories": "버전 관리 무시된 디렉토리",
  "activity.name.commit": "변경 내용 커밋",
  "activity.name.commit.message": "변경 내용 커밋: {0}",
  "activity.name.amend.message": "커밋 수정: {0}",
  "activity.name.update": "VCS에서 업데이트",
  "activity.name.get": "VCS에서 가져오기",
  "activity.name.get.from": "{0}에서 가져오기",
  "activity.name.shelve": "변경 내용 선반에 넣기",
  "activity.name.rollback": "롤백"
}

file_path = "c:/Users/klanary/Desktop/vscode 모음/android_korean/androidstudio_koreanlanguagepack/missing_translations/missing_keys_korean.json"
with open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)

for item in data["new_files"]:
    if item["filename"] == "VcsBundle.properties":
        item["keys"].update(translated_keys)
        break

with open(file_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Batch 24 translated successfully.")