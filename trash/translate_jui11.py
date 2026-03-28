import json

ko_dict = {
  "section.title.test.resource.folders": "테스트 리소스 폴더",
  "module.circular.dependency.warning.short": "{0} 사이에 순환 종속성이 있습니다.",
  "import.project.action.text": "기존 소스에서 {0, choice, 0#가져오기 |1#}{1, choice, 0#Java |1#}프로젝트 가져오기…",
  "action.description.remove.packaging.elements": "선택한 요소 제거",
  "section.title.resource.folders": "리소스 폴더",
  "classpath.chooser.description.add.module.dependency": "현재 모듈이 종속되어야 하는 모듈 선택:",
  "error.message.the.selected.node.belongs.to.0.element.so.it.cannot.be.edited": "선택한 노드는 ''{0}'' 요소에 속해 있으므로 편집할 수 없습니다.\n출력 레이아웃을 편집하려면 ''요소 콘텐츠 표시'' 확인란을 선택 해제하세요.",
  "action.description.inline.module.dependency": "소스 루트가 없는 모듈에 대한 종속성을 해당 종속성 목록으로 바꿉니다.",
  "project.roots.plain.mode.action.text.disabled": "모듈 그룹 숨기기",
  "dialog.title.configure.library.0": "{0} 구성",
  "directory.project.file.directory": "{0} 디렉터리\n",
  "project.roots.replace.library.entry.title": "라이브러리가 이미 추가됨",
  "add.new.header.text": "추가",
  "classpath.title.adding.dependency": "종속성 추가",
  "library.root.node": "루트",
  "action.text.inline.module.dependency": "인라인 모듈 종속성",
  "action.name.remove.packaging.element": "제거",
  "prompt.confirm.project.no.jdk": "할당된 SDK 없이 프로젝트를 만드시겠습니까?\n응용 프로그램을 컴파일, 디버깅 및 실행하고 표준 SDK 클래스를 확인하려면 SDK가 필요합니다.",
  "settings.remote.repo.service.connection.failed": "서비스 연결 실패",
  "dialog.message.no.suitable.parent.0.facets.found": "적절한 상위 {0} 패싯을 찾을 수 없습니다.",
  "action.text.hide.content": "콘텐츠 숨기기",
  "error.message.failed.to.download.sources.0": "소스를 다운로드하지 못했습니다: {0}",
  "error.message.failed.to.save.0": "{0}에 저장하지 못했습니다.",
  "notification.content.libraries.reloaded": "{0, choice, 0#라이브러리가|1#1개의 라이브러리가|2#{0}개의 라이브러리가} 성공적으로 다시 로드되었습니다.",
  "action.description.convert.to.repository.library": "IDE에서 라이브러리 JAR가 누락된 경우 자동으로 다운로드할 수 있도록 Maven 좌표를 추가로 저장하는 리포지토리 라이브러리로 일반 라이브러리를 변환합니다.",
  "action.text.convert.to.repository.library": "리포지토리 라이브러리로 변환…",
  "button.text.replace": "바꾸기",
  "dialog.message.no.files.were.downloaded": "다운로드된 파일이 없습니다. 다른 좌표를 시도하시겠습니까?",
  "dialog.title.no.files.were.downloaded": "라이브러리 다운로드 실패",
  "dialog.message.cannot.detect.maven.coordinates": "라이브러리 JAR에서 Maven 좌표를 감지할 수 없습니다.",
  "dialog.message.multiple.maven.coordinates": "라이브러리 JAR에 여러 Maven 좌표가 있습니다.",
  "dialog.message.do.you.want": "Maven 리포지토리를 수동으로 검색하시겠습니까?",
  "dialog.title.cannot.detect.maven.coordinates": "Maven 좌표를 감지할 수 없음",
  "task.title.comparing.jar.files": "JAR 파일 비교 중…",
  "action.text.class.path.move.up": "위로 이동(항목이 정렬된 순서로 표시된 경우 사용 안 함)",
  "action.text.class.path.move.down": "아래로 이동(항목이 정렬된 순서로 표시된 경우 사용 안 함)",
  "configurable.empty.text.select.library": "세부 정보를 보거나 편집하려면 여기에서 라이브러리를 선택하세요.",
  "action.name.text": "텍스트",
  "label.project.wizard.new.project.build.system": "빌드 시스템:",
  "label.project.wizard.new.project.jdk": "JDK:"
}

with open('missing_translations/missing_keys_korean.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for file_entry in data['new_files']:
    if file_entry['filename'] == 'JavaUiBundle.properties':
        file_entry['keys'].update(ko_dict)
        print("Updated JavaUiBundle.properties (Keys 401-440)")
        break

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
