import json

ko_dict = {
  "build.script.found.notification": "{0} 빌드 {1,choice,1#스크립트를|1<스크립트를} 찾았습니다.",
  "build.script.found.notification.import": "{0,choice,1#로드|2#모두 로드}",
  "build.scripts.from.multiple.providers.found.notification": "빌드 스크립트를 찾았습니다.",
  "project.structure.automatically.detected.notification": "프로젝트 소스를 기반으로 프로젝트가 자동으로 구성되었습니다.",
  "project.structure.automatically.detected.notification.gotit.action": "확인",
  "project.structure.automatically.detected.notification.configure.action": "수동으로 구성…",
  "task.searching.for.project.sources": "프로젝트 구조 감지 중…",
  "notification.text.duplicated.urls.were.removed": "{0}에서 중복된 URL이 제거되었습니다. 이러한 중복 URL은 이전 {1} 버전의 버그로 인해 생성되었으며 성능 문제를 일으킬 수 있습니다.",
  "dialog.title.cannot.import": "가져올 수 없음",
  "message.cannot.import.anything.from.0": "{0}에서 아무것도 가져올 수 없습니다.",
  "chooser.title.select.file.or.directory.to.import": "가져올 파일 또는 디렉터리 선택",
  "dialog.title.create.library": "라이브러리 만들기",
  "dialog.title.edit.library": "라이브러리 편집",
  "notification.title.repository.library.synchronization": "리포지토리 라이브러리 동기화",
  "action.description.add.0.support": "{0} 지원 추가",
  "dialog.title.library.already.exists": "라이브러리가 이미 존재합니다",
  "dialog.title.libraries.are.required": "라이브러리가 필요합니다",
  "label.project.layout.panel.name": "이름(&N):",
  "label.downloading.options.dialog.version": "버전(&V):",
  "dialog.title.downloading.options": "다운로드 옵션",
  "label.add.to.module": "모듈에 추가(&A):",
  "radio.button.use.library.from.0": "{0}의 라이브러리 사용",
  "warning.message.the.module.file.0.already.exist.and.will.be.overwritten": "모듈 파일 ''{0}''이(가) 이미 존재합니다.",
  "error.resolve.with.log_link": "<html>{0}<br><br>자세한 내용은 IDE 로그를 참조하세요(도움말 | <a href=\"{1}\">로그 표시</a>)<html>",
  "select.in.project.settings": "프로젝트 구조",
  "label.artifact.configurable.type": "유형:",
  "configurable.RemoteRepositoriesConfigurable.display.name": "원격 Jar 리포지토리",
  "project.new.wizard.module.name.title": "모듈 이름(&M):",
  "action.name.inline.artifact": "인라인 아티팩트",
  "action.text.add.packaging.element": "추가…",
  "configurable.library.prefix": "라이브러리",
  "project.roots.no.jdk.on.project.title": "SDK 만들기",
  "find.usage.view.no.usages.text": "사용 위치를 찾을 수 없습니다.",
  "libraries.remove.confirmation.title": "{0, choice, 1#라이브러리|2#라이브러리} 제거",
  "add.group.framework.separator": "프레임워크",
  "label.library.will.be.created.description.text": "{2}개의 {2, choice, 1#파일이|2#파일이} 있는 {0} 수준 라이브러리 <b>{1}</b>이(가) 만들어집니다.",
  "drag.n.drop.text.0.packaging.elements": "요소 {0}개",
  "dialog.title.change.module.names": "모듈 이름 변경",
  "project.module.compile.output.path": "모듈 컴파일 출력 경로 사용",
  "add.new.jdk.text": "새 SDK 추가"
}

with open('missing_translations/missing_keys_korean.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

filename = 'JavaUiBundle.properties'
found = False
for file_entry in data['new_files']:
    if file_entry['filename'] == filename:
        file_entry['keys'].update(ko_dict)
        found = True
        break

if not found:
    data['new_files'].append({"filename": filename, "keys": ko_dict})

print("Updated JavaUiBundle.properties (Keys 1-40)")

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
