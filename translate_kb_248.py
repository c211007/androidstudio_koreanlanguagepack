import json

translations = {
  "progress.title.test.connection": "연결 테스트",
  "progress.message.connecting.to.url": "{0}에 연결 중",
  "confirmation.text.delete.stored.authentication.information": "저장된 모든 Subversion 인증 정보를 삭제하려고 합니다.\\n삭제하시겠습니까?",
  "confirmation.title.clear.authentication.cache": "인증 캐시 지우기",
  "dialog.title.select.path.to.subversion.executable": "Subversion",
  "label.select.path.to.subversion.executable": "Subversion 실행 파일(1.7+)의 경로 선택",
  "label.path.to.svn.executable": "Subversion 실행 파일 경로:",
  "command.line.interactive.mode.title": "대화형 모드 사용",
  "command.line.interactive.mode.description": "Subversion 명령이 터미널에서 (대화형 모드로) 직접 실행될 때의 동작을 에뮬레이션합니다.<br>\n  svn+ssh 저장소의 비밀번호/암호 구문 프롬프트를 처리하고 https 저장소의 잘못된 서버 인증서를 신뢰하는 데 필요합니다.",       
  "non.english.locale.detected.warning": "영어가 아닌 언어가 사용되었습니다.",       
  "ssh.settings.executable.label": "SSH 실행 파일\\:",
  "dialog.title.ssh.settings.browse.executable": "SSH 실행 파일",
  "ssh.settings.user.name.label": "사용자 이름\\:",
  "ssh.settings.port.label": "포트\\:",
  "ssh.settings.password.choice.title": "비밀번호",
  "ssh.settings.private.key.choice.title": "비공개 키",
  "ssh.settings.private.key.path.label": "경로\\:",
  "dialog.title.ssh.settings.browse.private.key": "비공개 키",
  "ssh.settings.subversion.config.choice.title": "Subversion 구성",
  "ssh.settings.tunnel.label": "SSH 터널\\:",
  "ssh.settings.update.tunnel.title": "업데이트",
  "label.working.copy.format.unknown": "알 수 없음",
  "error.format.is.not.supported": "{0} 형식은 지원되지 않습니다. 지원되는 형식은 다음과 같습니다: {1}.",
  "label.configure.upgrade.label": "작업 사본 업그레이드 전략:",
  "radio.configure.upgrade.auto.16format": "자동으로 업그레이드(Subversion 1.6 사용)(&6)",
  "radio.configure.upgrade.auto.17format": "자동으로 업그레이드(Subversion 1.7 사용)(&7)",
  "radio.configure.upgrade.auto.18format": "자동으로 업그레이드(Subversion 1.8 사용)(&8)",
  "label.configure.create.label": "{0}에서 새 Subversion 작업 사본을 만들려고 합니다.\\n\n  원하는 작업 사본 형식을 선택하세요.",
  "radio.configure.create.auto.16format": "1.6 형식(&6)",
  "radio.configure.create.auto.17format": "1.7 형식(&7)",
  "radio.configure.create.auto.18format": "1.8 형식(&8)",
  "label.configure.change.label": "''{0}'' 작업 사본 형식을 다음으로 변경:",     
  "radio.configure.change.auto.16format": "1.6 형식(&6)",
  "radio.configure.change.auto.17format": "1.7 형식(&7)",
  "radio.configure.change.auto.18format": "1.8 형식(&8)",
  "dialog.upgrade.wcopy.format.title": "Subversion 작업 사본 형식",        
  "label.working.copy.root.outside.text": "작업 사본 루트가 프로젝트 설정에 지정된 디렉터리 외부에 있습니다.\\n전체 작업 사본이 변환됩니다.",
  "progress.text.loading.contents": "''{0}'' 콘텐츠 로드 중",
  "progress.text2.revision.information": "리비전 {0}",
  "progress.title.loading.file.content": "원격 파일 콘텐츠 로드 중",
  "progress.title.loading.file.properties": "원격 파일 속성 로드 중",   
  "exception.text.file.miss.svn": "''{0}'' 파일은 읽기 전용이지만 svn:needs-lock 속성이 없습니다.",
  "confirmation.text.edit.file": "편집하려는 파일은 편집하기 전에 잠가야 합니다.",
  "file.status.external": "외부(svn)",
  "file.status.obstructed": "차단됨(svn)",
  "file.status.replaced": "바뀜(svn)",
  "status.group.name.replaced": "바뀜",
  "confirmation.text.add.file": "다음 파일을 Subversion에 추가하도록 예약하시겠습니까?\\n{0}",
  "confirmation.text.add.dir": "다음 디렉터리를 Subversion에 추가하도록 예약하시겠습니까?\\n{0}",
  "confirmation.title.add.file": "추가 예약"
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
