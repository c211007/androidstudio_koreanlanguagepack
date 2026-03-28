import json

ko_dict = {
  "project.wizard.sdk.preindexing.progress.title": "SDK 사전 색인을 생성하는 중…",
  "dialog.message.cannot.file.copy": "{0} 파일을 복사할 수 없습니다: {1}",
  "dialog.message.cannot.file.move": "{0} 파일을 이동할 수 없습니다: {1}",
  "module.name.location.dialog.message.module.already.exist.in.project": "모듈 ''{0}''이(가) 프로젝트에 이미 있습니다. 다른 이름을 지정하세요.",
  "module.name.location.dialog.message.enter.module.file.location": "모듈 파일 위치 입력",
  "module.name.location.dialog.message.enter.module.name": "모듈 이름 입력",
  "module.name.location.dialog.message.error.module.file.location": "''{0}'' 디렉터리를 모듈 파일 위치로 설정하지 못했습니다.",
  "module.name.location.dialog.message.error.content.root": "''{0}'' 디렉터리를 콘텐츠 루트로 설정하지 못했습니다.",
  "project.settings.wizard.label.project.format": "프로젝트 형식(&F):",
  "projects.settings.wizard.expert.decorator.separator.title": "추가 설정(&E)",
  "library.options.panel.existing.library.combobox.label.no.library.selected": "[선택한 라이브러리 없음]",
  "library.options.panel.update.state.library.from.0.will.be.used": "{0}의 라이브러리가 사용됩니다.",
  "library.options.panel.update.state.error.library.is.not.specified": "<b>오류:</b> 라이브러리가 지정되지 않았습니다.",
  "library.options.panel.update.state.download.files.message": "{0}개의 {0, choice, 1#JAR가|2#JAR가} <b>{1}</b> 디렉터리로 다운로드됩니다.<br>{2} 라이브러리 <b>{3}</b>이(가) 생성됩니다.",
  "add.support.for.single.framework.remove.duplicates.dialog.message": "이미 {0, choice, 1#{1} 라이브러리 ''''{2}''''이(가)|2#{1} 라이브러리 {0}개가} 있습니다.\n  바꾸시겠습니까?",
  "framework.support.options.label.versions": "버전:",
  "add.framework.support.label.version": "{0} 버전:",
  "create.module.from.sources.dialog.message.file.not.exist": "파일 ''{0}''이(가) 없습니다.",
  "create.module.from.sources.dialog.message.not.directory": "''{0}''은(는) 디렉터리가 아닙니다.",
  "library.detection.dialog.message.stop.library.analysis": "라이브러리 분석을 중지하시겠습니까?",
  "module.detection.dialog.message.stop.module.analysis": "모듈 분석을 중지하시겠습니까?",
  "sdk.setting.step.label": "{0, choice, 0#프로젝트|1#모듈} SDK(&S):",
  "internet.attach.source.provider.name": "다운로드한 소스 연결",
  "internet.attach.source.provider.action.name": "다운로드…",
  "internet.attach.source.provider.action.busy.text": "검색 중…",
  "internet.attach.source.provider.action.notification.title.downloading.failed": "다운로드 실패",
  "internet.attach.source.provider.action.notification.title.sources.not.found": "소스를 찾을 수 없습니다.",
  "internet.attach.source.provider.action.notification.content.sources.for.jar.not.found": "''{0}.jar''의 소스를 찾을 수 없습니다.",
  "internet.attach.source.provider.action.notification.content.failed.to.create.directory": "소스를 저장할 디렉터리를 만들지 못했습니다: {0}",
  "internet.attach.source.provider.action.notification.content.connection.problem": "연결 문제가 있습니다. 자세한 내용은 로그를 참조하세요.",
  "repository.library.type.action.name.label": "Maven에서…",
  "repository.library.root.action.attach.annotations.text": "어노테이션 연결…",
  "repository.attach.dialog.caption.label": "검색할 키워드, 클래스 이름 또는 정확한 Maven 좌표(예: 'spring', 'Logger' 또는 'ant:ant-junit:1.6.5')",
  "jar.repository.manager.dialog.resolving.dependencies.title": "Maven 종속성 확인 중{0, choice, 0#|1#…}",
  "jar.repository.manager.notification.title.downloaded": "다음 파일이 다운로드되었습니다.",
  "jar.repository.manager.progress.text.loading.dependencies": "{0}의 종속성 로드 중",
  "jar.repository.manager.library.resolve.progress.text": "{0} 로드 중",
  "jar.repository.manager.version.resolve.progress.text": "{0} 버전 로드 중",
  "jar.repository.manager.confirm.reset.default.repositories.dialog.title": "기본 리포지토리 재설정 확인",
  "jar.repository.manager.confirm.reset.default.repositories.dialog.text": "{0,choice,1#리포지토리에|2#리포지토리에} 바인딩된 {0,choice,1#라이브러리가|2#라이브러리가} {0}개 있습니다. {0,choice,1#바인딩을|2#모두 바인딩을} 해제하시겠습니까?"
}

with open('missing_translations/missing_keys_korean.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for file_entry in data['new_files']:
    if file_entry['filename'] == 'JavaUiBundle.properties':
        file_entry['keys'].update(ko_dict)
        print("Updated JavaUiBundle.properties (Keys 441-480)")
        break

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
