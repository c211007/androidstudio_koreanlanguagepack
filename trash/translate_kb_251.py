import json

translations = {
  "message.text.update.no.directories.found": "업데이트할 버전이 지정된 디렉터리를 찾을 수 없습니다.",
  "messate.text.update.error": "SVN: 업데이트 오류",
  "label.external.copy": "외부 사본",
  "label.switched.copy": "전환된 사본",
  "progress.text2.added": "{0} 추가됨",
  "progress.text2.deleted": "{0} 삭제됨",
  "progress.text2.conflicted": "{0} 충돌함",
  "progress.text2.treeconflicted": "{0} 충돌함(트리 충돌)",
  "progres.text2.merged": "{0} 병합됨",
  "progres.text2.updated": "{0} 업데이트됨",
  "progress.text2.restored.file": "{0} 복원됨",
  "progres.text2.updated.to.revision": "리비전 {0}(으)로 업데이트되었습니다.",
  "status.text.updated.to.revision": "리비전 {0}(으)로 업데이트되었습니다.",
  "progress.text2.skipped.file": "{0} 건너뜀",
  "progress.text.updating.external.location": "''{0}''의 외부 위치 업데이트 중",
  "server.ssl.accept.temporary.action.name": "일시적으로 수락(_T)",
  "integrate.display.name": "통합",
  "error.invalid.svn.revision": "잘못된 svn 리비전: {0}",
  "error.invalid.url": "잘못된 URL: {0}",
  "integrate.configuration.revision1.label": "리비전(&V)",
  "integrate.configuration.source2.label": "소스 2:",
  "integrate.configuration.revision2.label": "리비전(&R)",
  "integrate.configuration.source1.label": "소스 1:",
  "integrate.configuration.description.label": "소스 간의 차이점을 작업 사본에 통합(소스 2를 소스 1과 비교)",
  "source.url.could.not.be.empty.error.message": "소스 URL은 비워 둘 수 없습니다.",
  "no.differences.between.sources.error.message": "소스와 동일한 소스 간에는 차이가 없습니다.",
  "label.update.switch.to.revision": "리비전으로 업데이트/전환:",
  "configure.revision.specified.radio": "지정됨",
  "configure.revision.head.radio": "헤드(HEAD)",
  "update.configuration.specific.url": "특정 URL로 업데이트/전환(&U):",       
  "progress.text.import": "{0} 가져오는 중",
  "message.text.cannot.import": "svn으로 가져올 수 없음: {0}",
  "message.title.import": "Subversion으로 가져오기",
  "revision.title": "리비전",
  "error.revision.from.must.be.a.valid.number": "시작 리비전은 유효한 숫자여야 합니다.",
  "error.revision.to.must.be.a.valid.number": "끝 리비전은 유효한 숫자여야 합니다.",
  "checkout.dialog.title": "Subversion에서 체크아웃",
  "checkout.dialog.button": "체크아웃",
  "checkout.directory.chooser.title": "체크아웃 디렉터리",
  "checkout.directory.chooser.prompt": "Subversion에서 체크아웃할 디렉터리를 선택하세요.",
  "checkout.options.dialog.title": "SVN 체크아웃 옵션",
  "checkout.options.checkout.label": "체크아웃:",
  "checkout.repository": "저장소 체크아웃 중…",
  "checkout.repository.failed": "체크아웃 실패",
  "checkout.repository.canceled": "체크아웃 취소됨",
  "checkout.repository.tooltip": "체크아웃이 완료되면 프로젝트가 열립니다.",
  "checkout.stop.message.description": "{0} 저장소 체아웃을 중지하시겠습니까?",
  "checkout.stop.message.title": "체크아웃 중지",
  "configure.branches.title": "Subversion 분기 구성",
  "configure.branches.error.wrong.url": "트렁크 위치는 저장소 루트 ''{0}'' 아래에 있어야 합니다."
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
