import json

ko_dict = {
  "library.sources.node": "소스",
  "prompt.new.project.file.name": "새로운 {0} {1}을(를) 만들기 위한 파일 이름을 입력하세요.",
  "module.paths.output.label": "출력 경로:",
  "action.text.pack.element.into.0": "{0}에 패킹",
  "add.new.global.library.text": "새로운 전역 라이브러리",
  "prompt.please.specify.java.sources.directory": "프로젝트의 소스 파일을 찾을 수 있는 디렉터리를 지정하세요.\n이 경로는 기본(루트, 이름 없음, 최상위 레벨) 패키지에 해당해야 합니다.\n참고: 프로그램은 이 디렉터리 아래에 있는 소스 파일만 인식합니다.",
  "action.text.add.to.modules": "모듈에 추가…",
  "dialog.message.artifact.0.already.exists": "아티팩트 ''{0}''이(가) 이미 존재합니다!",
  "project.settings.display.name": "프로젝트 구조",
  "button.unmark.resource": "리소스 표시 해제",
  "project.new.wizard.module.content.root.chooser.title": "모듈 콘텐츠 루트 선택",
  "project.new.wizard.from.existent.sources.title": "기존 소스에서 {0} 만들기(&E)",
  "configurable.FrameworkDetectionConfigurable.display.name": "감지",
  "settings.remote.repo.service.connection.successful": "서비스 연결 완료",
  "facet.banner.text": "패싯 ''{0}''",
  "dialog.title.search.library.in.maven.repositories": "Maven 리포지토리에서 라이브러리 검색",
  "new.library.file.chooser.title": "새로운 라이브러리 파일",
  "action.mark": "표시",
  "project.import.open.existing": "''{1}''에 {0}이(가) 있습니다.\n기존 프로젝트를 여시겠습니까, 아니면 삭제하고 ''{2}''을(를) 가져오시겠습니까?",
  "module.paths.test.output.title": "테스트 출력 경로 선택",
  "message.text.dependencies.were.successfully.collected.in.0.toolwindow": "\"{0}\" 도구 창에 종속성이 성공적으로 수집되었습니다.",
  "progress.title.0.library.files": "라이브러리 파일 {0}개",
  "project.import.open.existing.openExisting": "기존 프로젝트 열기",
  "title.mark.source.directory": "소스 디렉터리 표시",
  "configurable.artifact.prefix": "아티팩트",
  "library.attach.sources.description": "라이브러리 소스가 있는 JAR/ZIP 파일 또는 디렉터리를 선택하세요.",
  "action.name.facet.navigate": "탐색",
  "action.attach.external.project.description": "{0} 프로젝트를 현재 IDE 프로젝트에 연결",
  "dialog.message.0.do.you.want.to.proceed": "{0}\n\n계속하시겠습니까?",
  "message.text.stop.searching.for.frameworks": "{0}이(가) 현재 프레임워크를 검색하고 있습니다. 검색을 중지하시겠습니까?",
  "libraries.remove.confirmation.text": "라이브러리 ''{0}'' 및 {1}개의 {1, choice, 1#라이브러리가|2#라이브러리가} 프로젝트에서 사용 중입니다.\n \n선택한 모든 라이브러리를 삭제하시겠습니까?",
  "jdk.combo.box.none.item": "<없음>",
  "error.resolve.generic": "해결 오류",
  "action.name.extract.artifact": "아티팩트 추출…",
  "module.circular.dependency.warning.description": "다음 사이에 순환 종속성이 있습니다.",
  "action.text.0.disabled.if.elements.are.sorted": "{0} (요소가 정렬된 경우 사용 안 함)",
  "error.project.undefined": "정의된 외부 프로젝트 구성 파일이 없습니다.",
  "dialog.title.extract.artifact": "아티팩트 추출",
  "find.pointcut.applications.not.found.title": "정보",
  "artifact.source.items.tree.tooltip": "<html>기본 위치에 넣으려면 요소를 두 번 클릭하세요<br>\n원하는 위치에 추가하려면 요소를 끌어서 놓으세요<br>\n더 많은 작업은 팝업 메뉴에서 사용할 수 있습니다</html>"
}

with open('missing_translations/missing_keys_korean.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for file_entry in data['new_files']:
    if file_entry['filename'] == 'JavaUiBundle.properties':
        file_entry['keys'].update(ko_dict)
        print("Updated JavaUiBundle.properties (Keys 41-80)")
        break

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
