import json

ko_dict = {
  "project.language.level.combo.item": "프로젝트 기본값",
  "dialog.title.include.transitive.dependencies": "전이적 종속성 포함",
  "tooltip.text.dependency.was.rejected": "충돌 해결 중 종속성이 거부되었습니다.",
  "action.do.not.mark": "표시하지 않음",
  "dialog.title.split.module.or.library.0": "{0, choice, 0#라이브러리|1#모듈} 분할",
  "intention.family.maven.libraries": "Maven 라이브러리",
  "facet.type.banner.text": "''{0}'' 패싯",
  "module.add.error.message": "프로젝트에 모듈을 추가하는 중 오류 발생: {0}",
  "label.project.format": "프로젝트 형식:",
  "module.0.already.exists.error.message": "모듈 ''{0}''이(가) 이미 존재합니다.",
  "info.text.found.0.br.showing.1": "<html>찾음: {0}<br>표시 중: {1}</html>",
  "file.chooser.directory.for.downloaded.libraries.title": "다운로드한 라이브러리 디렉터리",
  "artifacts.create.action": "{0} 만들기",
  "action.text.extract.source.item.into.0": "{0}에 추출",
  "library.remove.action": "제거",
  "button.unmark.all": "모두 표시 해제(&U)",
  "error.message.please.enter.valid.coordinate.discover.it.or.select.one.from.the.list": "유효한 좌표를 입력하거나, 검색하거나, 목록에서 선택하세요.",
  "warning.message.some.required.libraries.wasn.t.downloaded": "일부 필수 라이브러리가 다운로드되지 않았습니다. 해당 라이브러리 없이 계속 진행하시겠습니까?",
  "library.source.open.class": ".class 파일 열기",
  "chooser.description.select.directories.which.should.be.excluded.from.the.library.content": "라이브러리 콘텐츠에서 제외할 디렉터리를 선택하세요. 제외된 디렉터리의 콘텐츠는 IDE에서 처리되지 않습니다.",
  "configurable.ProjectLibrariesConfigurable.display.name": "라이브러리",
  "dialog.title.failed.to.download.library": "라이브러리 다운로드에 실패했습니다",
  "intention.text.add.0.library.to.module.dependencies": "모듈 종속성에 {0} 라이브러리 추가",
  "prompt.select.source.directory": "소스 디렉터리 선택",
  "label.text.please.select.desired.technologies": "<html>원하는 기술을 선택하세요.<br>그러면 필요한 모든 라이브러리가 다운로드되고 프로젝트 구성에 패싯이 생성됩니다.</html>",
  "module.paths.output.title": "출력 경로 선택",
  "module.paths.validation.duplicate.source.root.error": "모듈 ''{0}''에는\n소스 루트 ''{1}''이(가) 포함되어서는 안 됩니다.\n해당 루트는 이미 모듈 ''{2}''에 속해 있습니다.",
  "chooser.title.select.directory.containing.module.files": "모듈 파일이 있는 디렉터리를 선택하세요.",
  "module.javadoc.title": "JavaDoc:",
  "title.directory.does.not.exist": "디렉터리가 없습니다",
  "add.external.annotations.path.description": "모듈 소스의 외부 어노테이션이 있는 경로를 선택하세요.",
  "sdk.configure.sourcepath.tab": "소스 경로",
  "error.message.please.enter.valid.library.files.path": "유효한 라이브러리 파일 경로를 입력하세요.",
  "add.new.module.text.full": "모듈",
  "project.roots.classpath.format.default.descr": "IntelliJ IDEA(.iml)",
  "module.classpath.button.edit": "편집(&I)…",
  "choose.modules.dialog.description": "선택한 모듈에 라이브러리 ''{0}''이(가) 추가됩니다.",
  "dialog.message.no.suitable.modules.for.0.facet.found": "{0} 패싯에 적합한 모듈을 찾을 수 없습니다.",
  "project.roots.output.compiler.title": "컴파일러 출력",
  "tab.name.all.facets": "모든 패싯"
}

with open('missing_translations/missing_keys_korean.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for file_entry in data['new_files']:
    if file_entry['filename'] == 'JavaUiBundle.properties':
        file_entry['keys'].update(ko_dict)
        print("Updated JavaUiBundle.properties (Keys 361-400)")
        break

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
