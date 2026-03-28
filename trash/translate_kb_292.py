import json

translations = {
  "change.nodetitle.change.is.outdated": "파일이 서버에서 변경되었습니다.",
  "changes.nodetitle.changecount": "{0,choice, 0#파일 없음|1#파일 1개|2#파일 {0}개}",
  "changes.nodetitle.directory.changecount": "{0,choice, 0#디렉터리 없음|1#디렉터리 1개|2#디렉터리 {0}개}",
  "changes.nodetitle.directory.file.changecount": "{0,choice, 0#디렉터리 없음|1#디렉터리 1개|2#디렉터리 {0}개} 및 {1,choice, 0#파일 없음|1#파일 1개|2#파일 {1}개}",
  "changes.nodetitle.merge.conflicts": "병합 충돌",
  "changes.nodetitle.merge.conflicts.resolve.link.label": "해결",
  "changes.nodetitle.resolved.conflicts": "해결된 충돌",
  "changes.default.changelist.name": "변경 사항",
  "changes.default.changelist.name.old": "기본 변경 목록",
  "action.ChangesView.ShowIgnored.text": "무시된 파일",
  "action.ChangesView.ShowIgnored.description": "무시된 파일을 표시합니다.",
  "changes.dialog.newchangelist.title": "새 변경 목록",
  "changes.dialog.editchangelist.title": "변경 목록 편집",
  "changes.removechangelist.warning.text": "''{0}'' 변경 목록을 삭제하시겠습니까?\\n모든 변경 사항이 활성 변경 목록으로 이동됩니다.",
  "changes.removechangelist.multiple.warning.text": "{0}개의 변경 목록을 삭제하시겠습니까?\\n모든 변경 사항이 활성 변경 목록으로 이동됩니다.",
  "changes.removechangelist.warning.title": "변경 목록 삭제",
  "changes.removechangelist.all.lists.warning.text": "{0}개의 변경 목록을 삭제하시겠습니까?\\n모든 변경 사항이 새 기본 변경 목록으로 이동됩니다.",
  "changes.tree.accessible.name": "변경 사항",
  "scope.name.changelist.all.changed.files": "변경된 모든 파일",
  "commit.dialog.no.changes.detected.text": "변경 사항이 감지되지 않았습니다.",
  "commit.dialog.no.changes.detected.title": "커밋할 내용 없음",
  "commit.dialog.title": "변경 사항 커밋",
  "commit.dialog.default.commit.operation.name": "커밋(&I)",
  "commit.dialog.include.action.name": "커밋에 포함(&I)",
  "commit.dialog.refresh.files": "파일 동기화 중…",
  "commit.dialog.changelist.label": "변경 목록(&T):",
  "commit.dialog.partial.commit.warning.title": "부분 커밋은 지원되지 않습니다",
  "commit.dialog.partial.commit.warning.body": "''{0}''에 대해서는 부분 커밋을 지원하지 않습니다.\\n선택한 파일의 모든 변경 사항이 커밋됩니다.",
  "commit.dialog.configurable": "커밋",
  "change.list.manager.wait.lists.synchronization.modal": "{1,choice,0#대기 중 |1#{0}: }로컬 변경 사항 새로고침 중",
  "change.list.manager.wait.lists.synchronization.background": "{1,choice,0#대기 중 |1#{0}: }로컬 변경 사항을 새로고침하는 중",
  "commit.wait.util.synched.text": "VCS 새로고침 수행 중…",
  "edit.changelist.name": "이름(&N):",
  "edit.changelist.description": "주석(&C):",
  "checkbox.show.dirty.recursively": "프로젝트 트리에서 수정된 파일이 포함된 디렉터리 강조 표시",
  "commit.legend.modified": "수정됨",
  "commit.legend.new": "추가됨",
  "commit.legend.deleted": "삭제됨",
  "commit.editor.diff.preview.title": "커밋: {0}",
  "commit.editor.diff.preview.empty.title": "커밋",
  "changes.editor.diff.preview.title": "변경 사항: {0}",
  "changes.editor.diff.preview.empty.title": "변경 사항",
  "save.committing.files.confirmation.title": "커밋 중 파일 저장",
  "save.committing.files.confirmation.text": "\n  현재 다음 {0,choice,1#파일이|2#파일들이} VCS에 커밋되고 있습니다. 지금 저장하면 일치하지 않는 데이터가 커밋될 수 있습니다.\\n\n  {1}\\n\n  지금 {0,choice,1#파일을|2#파일들을} 저장하시겠습니까?",
  "save.committing.files.confirmation.ok": "지금 저장",
  "save.committing.files.confirmation.cancel": "저장 연기",
  "amend.commit.different.committer.warning": "수정된 커밋의 커미터가 기본값과 다릅니다.",
  "amend.commit.tree.node.loading": "수정된 커밋 로드 중…",
  "amend.commit.load.details.task.title": "커밋 세부정보 로드 중",
  "amend.commit.load.message.task.title": "커밋 메시지 로드 중"
}

with open("missing_translations/missing_keys_korean.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for file_info in data.get("new_files", []):
    if file_info.get("filename") == "VcsBundle.properties":
        keys_dict = file_info.get("keys", file_info.get("properties", {}))
        keys_dict.update(translations)
        file_info["keys"] = keys_dict
        break

with open("missing_translations/missing_keys_korean.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)
