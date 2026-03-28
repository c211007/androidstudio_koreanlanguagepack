import json

ko_dict = {
  "label.enter.library.name": "라이브러리 이름 입력:",
  "module.paths.validation.duplicate.content.error": "콘텐츠 루트 ''{0}''이(가) 모듈 ''{1}'' 및 ''{2}''에 대해 정의되었습니다.\n프로젝트의 두 모듈이 동일한 콘텐츠 루트를 공유할 수 없습니다.",
  "quarantine.dialog.message": "운영 체제에서 다음 폴더를 인터넷에서 다운로드되었을 수 있으므로 ''격리됨''으로 표시했습니다.\n이러한 폴더에서 파일을 열면 예상대로 작동하지 않을 수 있습니다. 격리된 상태를 지우시겠습니까?\n{0}",
  "label.project.jdk": "프로젝트 SDK:",
  "label.java.source.files.have.been.found": "모듈의 소스 파일을 찾았습니다. 소스 경로로 표시될 디렉터리를 선택하세요.\n이 경로는 기본(루트, 이름 없음, 최상위 레벨) 패키지에 해당합니다.\n참고: 프로그램은 이 디렉터리 아래에 있는 소스 파일만 인식합니다.",
  "project.new.wizard.module.content.root.chooser.description": "선택한 디렉터리가 모듈 콘텐츠 루트로 표시됩니다.",
  "library.configure.title": "라이브러리 구성",
  "modules.order.export.export.column": "내보내기",
  "action.text.analyze.this.dependency": "이 종속성 분석",
  "project.import.wizard.title": "{0}에서 가져오기",
  "action.attach.external.project.warning.message.file": "선택한 파일 ''{0}''은(는) {1} 빌드 파일이 아닙니다.",
  "action.attach.external.project.warning.message.directory": "선택한 디렉터리 ''{0}''에 {1} 빌드 파일이 없습니다.",
  "action.attach.external.project.warning.title": "인식할 수 없는 {0} 프로젝트",
  "action.attach.external.project.text": "{0} 프로젝트 연결",
  "configurable.GlobalLibrariesConfigurable.display.name": "전역 라이브러리",
  "project.directory.is.not.writable": "''{0}'' 디렉터리에 쓸 수 없는 것 같습니다. 다른 위치를 선택하세요.",
  "module.remove.last.confirmation": "이 프로젝트에서 {0, choice, 1#유일한 모듈|2#모든 모듈}을(를) 제거하시겠습니까?\n디스크의 파일은 삭제되지 않습니다.",
  "title.select.project.file.directory": "{0} 파일 디렉터리 선택",
  "dialog.title.cannot.create.0.facet": "{0} 패싯을 만들 수 없습니다.",
  "settings.remote.repo.maven.repository.url": "Maven 리포지토리 URL",
  "progress.searching.for.sources": "{0}에서 소스를 검색하는 중입니다. 잠시 기다려 주세요.",
  "project.roots.plain.mode.action.text.enabled": "모듈 그룹 표시",
  "configurable.JdkListConfigurable.display.name": "SDK",
  "enter.module.copy.name.error.message": "모듈 복사본 이름 입력",
  "module.javadoc.add.path.title": "JavaDoc에 경로 추가",
  "project.roots.external.annotations.tab.title": "외부 어노테이션:",
  "error.message.no.files.were.downloaded.for.0": "{0}에 대해 다운로드된 파일이 없습니다.",
  "sdk.configure.title": "SDK 구성",
  "dialog.title.0.library.copy": "라이브러리 복사",
  "dialog.title.0.library.move": "라이브러리 이동",
  "dialog.text.enter.common.prefix": "선택한 모듈 {0}개의 이름에 대한 접두사를 지정하세요.",
  "class.file.decompiled.text": "디컴파일된 .class 파일",
  "class.file.multi.release.decompiled.text": "JDK-{0} 관련 루트에서 디컴파일된 .class 파일",
  "class.file.decompiled.bytecode.version.text": "바이트코드 버전: {0}.{1}",
  "class.file.decompiled.sdk.version.text": "(Java {0})",
  "settings.remote.repo.Maven.Repository.URL": "Maven 리포지토리 URL",
  "project.roots.tooltip.library.has.broken.paths": "라이브러리 ''{0}''에 손상된 {1, choice, 1#경로|2#경로}가 있습니다.",
  "project.sdk.not.defined": "프로젝트 SDK가 정의되지 않았습니다.",
  "module.sdk.not.defined": "모듈 SDK가 정의되지 않았습니다.",
  "label.enter.artifact.name": "아티팩트 이름 입력:"
}

with open('missing_translations/missing_keys_korean.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for file_entry in data['new_files']:
    if file_entry['filename'] == 'JavaUiBundle.properties':
        file_entry['keys'].update(ko_dict)
        print("Updated JavaUiBundle.properties (Keys 241-280)")
        break

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
