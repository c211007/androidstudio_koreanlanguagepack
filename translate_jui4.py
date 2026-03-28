import json

ko_dict = {
  "button.mark.all": "모두 표시(&M)",
  "module.group.banner.text": "모듈 그룹 ''{0}''",
  "artifacts.add.copy.action": "다음의 사본 추가",
  "sdk.configure.editor.title": "SDK 편집기",
  "configurable.ErrorPaneConfigurable.display.name": "문제",
  "project.inherit.compile.output.path": "프로젝트 컴파일 출력 경로 상속",
  "library.unnamed.text": "{0} 및 {1, choice, 1#1개의 파일 더|2#{1}개의 파일 더}",
  "error.message.module.name.prefix.contains.empty.string": "접두사는 점으로 구분된 단어의 시퀀스여야 합니다.",
  "project.roots.classpath.format.label": "종속성 스토리지 형식:",
  "project.import.select.title": "가져올 {0} 프로젝트 선택",
  "rename.message.prefix.module": "모듈",
  "module.javadoc.add.path.prompt": "모듈 javadoc 문서가 있는 JAR/zip 파일 또는 디렉터리를 선택하세요.",
  "project.import.open.existing.reimport": "기존 프로젝트를 삭제하고 가져오기",
  "tab.title.output.layout": "출력 레이아웃",
  "output.tab.title": "출력",
  "project.new.wizard.module.file.chooser.title": "모듈 파일 상위 디렉터리 선택",
  "action.text.put.source.item.into.0": "{0}에 넣기",
  "action.text.library.0.to.1.copy": "{0}(으)로 복사…",
  "action.text.library.0.to.1.move": "{0}(으)로 이동…",
  "settings.remote.repo.no.services": "서비스 없음",
  "directory.module.file": "모듈 파일 디렉터리\n",
  "label.please.enter.project.name": "새로운 {0} {1}을(를) 만들기 위한 이름을 입력하세요.",
  "error.message.required.library.is.not.configured": "{1, choice, 1#해당 라이브러리가|2#해당 라이브러리가} 구성되지 않았기 때문에 프로젝트에 {0}을(를) 활성화할 수 없습니다.",
  "project.roots.module.jdk.problem.message": "모듈 SDK가 정의되지 않았습니다.",
  "banner.slogan.artifact.0": "아티팩트 ''{0}''",
  "action.description.change.module.names": "모듈 이름의 공통 접두사를 변경하여 모듈의 자동 그룹화를 조정합니다.",
  "module.paths.exclude.output.checkbox": "출력 경로 제외",
  "project.roots.project.jdk.problem.message": "프로젝트 SDK가 정의되지 않았습니다.",
  "project.import.default.name": "ImportedFrom{0}",
  "label.text.specify.artifact.name": "아티팩트 이름 지정(&N):",
  "message.no.module.dependency.candidates": "종속될 모듈을 찾을 수 없습니다.",
  "dialog.title.download.library.from.maven.repository": "Maven 리포지토리에서 라이브러리 다운로드",
  "module.module.language.level": "언어 레벨(&L):",
  "project.import.show.settings.after": "가져온 후 프로젝트 구조 열기(&O)",
  "prompt.stop.searching.for.sources": "{0}이(가) 현재 소스를 검색하고 있습니다. 검색을 중지하시겠습니까?",
  "label.component.file.location": "{0} 파일 위치(&L):",
  "dialog.title.remove.elements": "요소 제거",
  "project.settings.title": "프로젝트 설정",
  "dialog.title.obsolete.library.files.remover.delete.files": "사용하지 않는 파일 삭제",
  "error.message.module.name.cannot.be.empty": "모듈 이름은 비워둘 수 없습니다."
}

with open('missing_translations/missing_keys_korean.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for file_entry in data['new_files']:
    if file_entry['filename'] == 'JavaUiBundle.properties':
        file_entry['keys'].update(ko_dict)
        print("Updated JavaUiBundle.properties (Keys 121-160)")
        break

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
