import json

translations = {
  "confirmation.title.add.multiple.files": "Subversion에 추가할 파일 선택", 
  "action.name.ignore.files": "무시 파일 마스크 추가 중",
  "action.name.undo.ignore.files": "무시 목록에서 파일 이름(또는 마스크) 제거 중",
  "confirmation.text.delete.file": "다음 파일을 Subversion에서 삭제하도록 예약하시겠습니까?\\n{0}",
  "confirmation.text.delete.dir": "다음 디렉터리를 Subversion에서 삭제하도록 예약하시겠습니까?\\n{0}\\n참고: 변경 사항이 커밋되면 디스크에서 디렉터리가 삭제됩니다.",
  "confirmation.text.delete.dir.17": "다음 디렉터리를 Subversion에서 삭제하도록 예약하시겠습니까?\\n{0}",
  "confirmation.title.delete.file": "삭제 예약",
  "confirmation.title.delete.multiple.files": "Subversion에서 삭제할 파일 선택",
  "progress.text.locking.files": "저장소의 파일 잠그는 중…",
  "progress.text2.processing.file": "{0} 파일 처리 중",
  "progress.title.lock.files": "파일 잠금",
  "exception.text.locking.file.failed": "파일 잠금 실패: {0}",
  "message.text.files.lock.failed": "{0,choice, 0#파일 잠금에 실패했습니다.|1#파일 잠금에 실패했습니다.}",
  "message.text.files.locked": "{0,choice, 0#파일 잠금에 실패했습니다.|1#파일 1개 잠김|2#{0,number}개 파일 잠김}",
  "progress.text.unlocking.files": "저장소의 파일 잠금 해제 중…",      
  "progress.title.unlock.files": "파일 잠금 해제",
  "exception.text.failed.to.unlock.file": "파일 잠금 해제 실패: {0}",
  "message.title.unlock.failures": "잠금 해제 실패",
  "message.text.files.unlocked": "{0,choice, 0#파일 잠금 해제에 실패했습니다.|1#파일 1개 잠금 해제됨|2#{0,number}개 파일 잠금 해제됨}",
  "exception.text.cleanupaction.batchperform.not.implemented": "CleanupAction.batchPerform이 구현되지 않았음",
  "progress.text2.adding": "''{0}'' 추가 중",
  "progress.text2.deleting": "''{0}'' 삭제 중",
  "progress.text2.sending": "''{0}'' 보내는 중",
  "progress.text2.replacing": "''{0}'' 바꾸는 중",
  "progress.text2.transmitting.delta": "''{0}''에 대한 델타 전송 중",       
  "progress.title.copy": "Subversion 복사",
  "progress.text.copy.to": "''{0}''(으)로 복사",
  "message.text.no.conflicts.found": "충돌이 발견되지 않음",
  "message.title.no.conflicts.found": "충돌 없음",
  "label.select.files.and.directories.to.mark.resolved": "해결됨으로 표시할 파일과 디렉터리 선택:",
  "dialog.title.mark.resolved": "해결됨으로 표시",
  "action.name.mark.resolved": "해결됨으로 표시",
  "action.name.resolve.conflict": "충돌 해결",
  "action.name.revert": "되돌리기(&R)",
  "error.revert.failed": "되돌리기 실패",
  "action.name.set.property": "속성 설정",
  "exception.text.cannot.annotate.directory": "어노테이션 작업은 파일에만 적용됩니다.",
  "progress.text.computing.annotation": "''{0}''에 대한 어노테이션 계산 중",     
  "action.text.annotate": "어노테이션",
  "label.revision": "리비전",
  "label.merge.source.revision": "소스 리비전 병합",
  "tooltip.revision.number.message": "리비전 {0}: {1}",
  "error.can.not.find.relative.path.for.path.at.revision": "{0}@{1}의 상대 경로를 찾을 수 없음",
  "error.can.not.get.current.revision.for.path": "{0} 파일의 현재 리비전을 가져올 수 없음",
  "error.can.not.get.last.changed.revision.for.path.please.file.an.issue": "다음 파일의 마지막으로 변경된 리비전을 가져올 수 없습니다. {0}\\n\n 이 파일에 대해 svn info를 실행하고 이슈를 제출하세요.",
  "checkbox.checkin.keep.files.locked": "파일 잠금 유지(&K)",
  "checkbox.checkin.auto.update.after.commit": "커밋 후 자동 업데이트",      
  "progress.title.commit": "커밋",
  "status.text.committed.revision": "리비전 {0}을(를) 커밋했습니다.",
  "checkin.operation.name": "커밋(_I)"
}

with open("missing_translations/missing_keys_korean.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for file_info in data.get("new_files", []):
    if file_info.get("filename") == "SvnBundle.properties":
        keys_dict = file_info.get("keys", file_info.get("properties", {}))
        keys_dict.update(translations)
        file_info["keys"] = keys_dict
        break

with open("missing_translations/missing_keys_korean.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)
