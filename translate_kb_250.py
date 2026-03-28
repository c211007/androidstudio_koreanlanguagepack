import json

translations = {
  "checkin.different.formats.involved": "{0,choice,0#저장소|1#저장소} {1}에 대해 선택된 변경 사항이\\n\n  다른 형식의 Subversion 작업 사본에 속합니다.\\n\n  커밋은 여러 커밋으로 분할됩니다.\\n\\n\n  변경 사항 | Subversion 작업 사본 정보에서 모든 작업 사본을 동일한 형식으로 변환할 수 있습니다.\\n\n  커밋을 계속하시겠습니까?",
  "dialog.title.commit.will.split": "Subversion: 커밋 분할됨",
  "error.wrong.committed.revision.number": "잘못된 커밋 리비전 번호: {0}",
  "error.missing.committed.revision.number": "누락된 커밋 리비전 번호: {0}",
  "progress.text2.fetching.external.location": "외부 위치를 ''{0}''(으)로 가져오는 중",
  "progress.text2.checked.out": "파일 {1}개를 체크아웃했으며 {0}을(를) 체크아웃하는 중",      
  "progress.text2.exported": "파일 {1}개를 내보냈으며 {0}을(를) 내보내는 중",
  "progress.text2.checked.out.revision": "리비전 {0}을(를) 체크아웃했습니다.",
  "progress.text2.exported.revision": "리비전 {0}을(를) 내보냈습니다.",
  "status.text.checked.out.revision": "리비전 {0}을(를) 체크아웃했습니다.",
  "message.text.cannot.load.supported.formats": "지원되는 형식을 로드할 수 없음: {0}",
  "message.text.cannot.checkout": "svn에서 체크아웃할 수 없음: {0}",
  "message.text.cannot.export": "svn에서 내보낼 수 없음: {0}",
  "dialog.title.check.out": "Subversion에서 체크아웃",
  "progress.title.check.out": "Subversion에서 체크아웃",
  "progress.title.check.out.cancel": "Subversion에서 체크아웃 중지",       
  "message.title.export": "Subversion에서 내보내기",
  "progress.text.checking.out": "파일을 ''{0}''(으)로 체크아웃하는 중",
  "progress.text.export": "파일을 ''{0}''(으)로 내보내는 중",
  "button.text.select.all": "모두 선택(&A)",
  "button.text.deselect.all": "모두 선택 취소(&D)",
  "dialog.title.select.repository.location": "저장소 위치 선택",      
  "dialog.message.can.not.detect.repository.root.for.url": "URL의 저장소 루트를 감지할 수 없음: {0}",
  "progress.title.detecting.repository.root": "저장소 루트 감지 중",      
  "button.text.ssl.accept": "수락(_A)",
  "button.text.ssl.reject": "거부(_R)",
  "button.text.ssh.accept": "예(_Y)",
  "button.text.ssh.reject": "아니요(_N)",
  "dialog.title.ssl.examine.server.crertificate": "서버 인증서 검사", 
  "dialog.title.ssh.examine.server.fingerprints": "서버 키 지문 확인",
  "label.ssl.server.provided.certificate": "서버에서 다음 인증서를 제공했습니다.",
  "label.ssh.server.provided.fingerprints": "호스트 {0}의 신뢰성을 확인할 수 없습니다.",
  "label.ssh.server.provided.fingerprints2": "{0} 키 지문은 다음과 같습니다.",
  "label.ssh.server.provided.fingerprints3": "연결을 계속하시겠습니까?",
  "checkbox.svn.ssh.cache.fingerprint": "Subversion 캐시에 키 추가(&A)",
  "dialog.title.set.property": "속성 설정",
  "label.set.property.property.name": "속성 이름(&N):",
  "radio.set.property.set.property.value": "속성 값 설정(&S):",
  "radio.set.property.delete.property": "속성 삭제(&D)",
  "checkbox.set.property.update.properties.recursively": "재귀적으로 속성 업데이트(&R)",
  "update.switch.configurable.name": "업데이트/전환",
  "label.update.url": "URL:",
  "checkbox.update.switch.configurable.to.specific.revision": "특정 리비전으로 업데이트/전환(&R):",
  "checkbox.force.update": "강제 업데이트(&F)",
  "checkbox.ignore.externals": "외부 무시(&E)",
  "checkbox.update.switch.configurable.try.merge.without.changes": "병합을 시도하되 변경하지 않음(&T)",
  "progress.text.merging.dry.run.changes": "변경 사항을 ''{0}''에 병합(예행 연습)하는 중",
  "progress.text.merging.changes": "변경 사항을 ''{0}''에 병합하는 중",
  "progress.text.updating": "''{0}'' 업데이트 중",
  "exception.text.root.was.not.properly.updated": "svn: {0}이(가) 제대로 업데이트되지 않았습니다. 상위 항목과 함께 저장소에서 이미 제거되었을 수 있습니다."  
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
