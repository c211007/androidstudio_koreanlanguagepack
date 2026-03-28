import json

ko_dict = {
  "file.chooser.directory.for.downloaded.libraries.description": "다운로드한 라이브러리가 선택한 디렉터리로 복사됩니다.",
  "project.structure.platform.title": "플랫폼 설정",
  "description.select.project.file.directory": "{0} 파일이 이 디렉터리에 저장됩니다.",
  "checkbox.text.build.on.make": "프로젝트 빌드에 포함(&B)",
  "project.facets.display.name": "패싯",
  "module.paths.searching.source.roots.progress": "{0}에서 소스 루트 검색 중",
  "label.library.level": "수준(&L):",
  "sdk.configure.javadoc.tab": "문서 경로",
  "add.external.annotations.path.title": "외부 어노테이션에 경로 추가",
  "library.source.show.diff": "차이점 표시",
  "prompt.relative.path.to.sources.empty": "소스에 대한 상대 경로가 비어 있습니다.\n모듈 콘텐츠 루트\n''{0}''\n을(를) 소스 디렉터리로 표시하시겠습니까?",
  "project.new.wizard.progress.title": "초기화 중…",
  "sdk.paths.specify.url.button": "URL 지정…",
  "dialog.text.enter.common.prefix.comment": "<html>IDE에서 모듈은 이름에 따라 그룹화됩니다.<br>여러 모듈의 이름에 공통 접두사가 있는 경우\n 함께 표시됩니다.</html>",
  "copy.module.dialog.title": "모듈 복사",
  "project.directory.is.already.taken": "''{0}'' 디렉터리는 이미 ''{1}'' 프로젝트에서 사용 중입니다. 다른 위치를 선택하세요.",
  "create.default.library.type.action.name": "Java",
  "project.new.wizard.import.description": "<html>외부 모델에서 {0} {1} 만들기({2})</html>",
  "label.project.roots.have.been.found": "프로젝트의 소스 파일을 찾았습니다. 프로젝트 루트에 추가될 디렉터리를 선택하세요.\n이 경로는 기본(루트, 이름 없음, 최상위 레벨) 패키지에 해당합니다.\n참고: 프로그램은 이 디렉터리 아래에 있는 소스 파일만 인식합니다.",
  "error.title.required.library.is.not.configured": "라이브러리가 구성되지 않음",
  "combobox.item.module.library": "모듈 라이브러리",
  "add.new.project.library.text": "새로운 프로젝트 라이브러리",
  "action.AnActionButton.text.remove": "제거",
  "display.name.artifacts": "아티팩트",
  "error.message.library.0.already.exists": "라이브러리 ''{0}''이(가) 이미 존재합니다.",
  "notification.title.io.error": "IO 오류",
  "import.module.action.text": "기존 소스에서 {0, choice, 0#가져오기 |1#}{1, choice, 0#Java |1#}모듈 가져오기…",
  "library.name.not.specified.title": "라이브러리 이름이 지정되지 않았습니다",
  "classpath.message.library.already.added": "라이브러리 ''{0}''이(가) 이 모듈에 이미 추가되었습니다.",
  "library.javadocs.node": "JavaDocs",
  "notification.title.repository.libraries.cleanup": "리포지토리 라이브러리 정리",
  "label.relative.output.path": "상대 출력 경로(&P):",
  "settings.remote.repo.no.repositories.found": "리포지토리를 찾을 수 없음",
  "settings.remote.repo.repositories.found": "{0}개의 {0, choice, 1#리포지토리를|2#리포지토리를} 찾았습니다.",
  "error.message.library.name.is.not.specified": "라이브러리 이름이 지정되지 않았습니다.",
  "settings.remote.repo.maven.jar.repositories": "Maven Jar 리포지토리:",
  "file.location.should.be.absolute": "{0} 위치 경로는 절대 경로여야 합니다.",
  "sdk.configure.classpath.tab": "클래스 경로",
  "label.module.name": "모듈 이름(&M):",
  "module.paths.test.output.label": "테스트 출력 경로:"
}

with open('missing_translations/missing_keys_korean.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for file_entry in data['new_files']:
    if file_entry['filename'] == 'JavaUiBundle.properties':
        file_entry['keys'].update(ko_dict)
        print("Updated JavaUiBundle.properties (Keys 161-200)")
        break

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
