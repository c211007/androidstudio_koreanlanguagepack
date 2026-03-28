import json
import os

translated_keys = {
  "patch.unknown.after.hunk.start.syntax": "알 수 없는 청크 시작 후 구문",
  "patch.missing.after.hunk": "청크 후 누락됨",
  "patch.parse.no.document.error": "패치 파일을 구문 분석할 수 없습니다",
  "patch.parse.error": "잘못된 패치 파일: {0}",
  "patch.parse.error.empty.file": "패치 파일이 비어 있습니다",
  "patch.is.binary.text": "바이너리 패치 파일",
  "patch.unknown.before.hunk.start.syntax": "알 수 없는 청크 시작 전 구문",
  "patch.unknown.hunk.start.syntax": "알 수 없는 청크 시작 구문",
  "patch.second.file.name.expected": "두 번째 파일 이름이 필요합니다",
  "patch.empty.0.data.section": "비어 있는 ''{0}'' 데이터 섹션",
  "patch.empty.additional.info.header": "비어 있는 추가 정보 헤더",
  "patch.contains.additional.information.without.patch.itself": "패치 자체 없이 추가 정보 포함",
  "patch.can.t.detect.file.names.from.git.format.header.line": "git 형식 헤더 줄에서 파일 이름을 감지할 수 없습니다",
  "patch.unexpected.end.of.binary.patch": "바이너리 패치의 예기치 않은 끝",
  "patch.failed.to.fetch.old.content.for.file.name.in.revision": "개정 {1}에서 파일 {0}의 이전 콘텐츠를 가져오지 못했습니다",
  "patch.apply.error.file.not.found": "파일 {0}을(를) 찾을 수 없습니다",
  "patch.apply.error.document.not.found": "문서 {0}을(를) 찾을 수 없습니다",
  "patch.apply.error.conflict": "패치 적용 충돌",
  "vfs.revision.author.unknown": "알 수 없음",
  "change.list.scope.provider.local.changes": "로컬 변경 내용",
  "change.list.scope.provider.only.changes": "모든 파일에서 VCS에 커밋되지 않은 변경 내용만",
  "change.list.scope.provider.only.changes.in.file": "파일 {0}에서 VCS에 커밋되지 않은 변경 내용만",
  "changes.change.list.conflict.dialog.radio.button.ignore": "무시(&I)",
  "changes.change.list.conflict.dialog.radio.button.shelve.changes": "변경 내용 선반에 넣기(&S)",
  "todo.tab.title.all.changes": "로컬 변경 내용",
  "todo.tab.title.changelist.suffix": "변경 목록",
  "get.from.vcs.extension.list.accessible.name": "저장소 위치",
  "vcs.dnd.image.text.n.files": "{0} {0, choice, 1#파일|2#파일}",
  "checking.recent.changes": "최근 변경 내용 확인 중\\u2026",
  "show.diff.in.editor.tab.got.it.tooltip": "편집기 탭에서 diff를 다시 표시하려면 이 메뉴를 사용하세요.",
  "advanced.settings.vcs": "버전 관리",
  "advanced.setting.vcs.annotations.preload": "편집기에서 파일이 열릴 때 VCS에서 파일 어노테이션 로드",
  "advanced.setting.vcs.annotations.preload.description": "이를 통해 요청 시 더 빠르게 표시할 수 있습니다.",
  "advanced.setting.vcs.process.ignored": "무시된 파일 강조 표시",
  "advanced.setting.vcs.process.ignored.description": "VCS에서 무시된 파일 목록을 요청하여 IDE에 해당 상태를 표시합니다.",
  "advanced.setting.vcs.commit.tool.window": "커밋 도구 창 활성화",
  "advanced.setting.vcs.commit.tool.window.description": "별도의 커밋 도구 창에 로컬 변경 내용 및 선반 탭을 표시합니다.",
  "advanced.setting.vcs.non.modal.commit.toggle.ui": "커밋 컨트롤 전환",
  "advanced.setting.vcs.non.modal.commit.close.in.windowed.mode": "커밋 후 창/플로팅 모드에서 자동으로 커밋 도구 창 닫기",
  "advanced.setting.vcs.non.modal.commit.toggle.ui.description": "커밋 수행 후 커밋 패널 및 체크박스를 숨기고 로컬 변경 내용에서 커밋 UI 전환을 허용합니다.",
  "advanced.setting.vcs.push.all.with.commits": "푸시할 새 커밋이 있는 모든 저장소 선택",
  "advanced.setting.vcs.push.all.with.commits.description": "푸시할 커밋이 있는 모든 저장소를 기본적으로 미리 선택합니다.",
  "advanced.setting.vcs.allow.force.push.without.confirmation": "강제 푸시 시 경고 표시 안 함",
  "advanced.setting.vcs.allow.force.push.without.confirmation.description": "보호되지 않은 브랜치에 강제 푸시할 때 확인 메시지를 묻지 않습니다.",
  "sequence.concatenation.a.and.b": "{0} 및 {1}",
  "sequence.concatenation.separator": ",\\u0020",
  "sequence.concatenation.tail": "\\ 및 {0}",
  "sequence.concatenation.tail.n.others": "\\ 및 기타 {0}개",
  "title.code.author.inlay.hints": "코드 작성자",
  "label.code.author.inlay.hints": "코드 작성자"
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

print("Batch 23 translated successfully.")