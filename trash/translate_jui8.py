import json

ko_dict = {
  "project.new.wizard.import.title": "외부 모델에서 {0} 가져오기(&M)",
  "library.name.already.exists.error": "라이브러리 ''{0}''이(가) 이미 존재합니다.",
  "progress.title.searching.source": "소스 검색 중…",
  "error.source.directory.should.be.under.module.content.root.directory": "소스 디렉터리는 모듈 콘텐츠 루트 디렉터리 아래에 있어야 합니다.",
  "project.new.wizard.module.file.description": "모듈 .iml 파일이 선택한 디렉터리에 배치됩니다.",
  "dialog.mesage.0.was.not.loaded": "{0}이(가) 로드되지 않았습니다.",
  "project.roots.replace.library.entry.message": "이전 라이브러리 ''{0}''을(를) 바꾸시겠습니까?",
  "setup.library.dialog.title": "라이브러리 설정",
  "warning.text.0.do.you.want.to.overwrite.these.files": "{0}\n{1,choice,1#이 파일을|2#이러한 파일을} 덮어쓰시겠습니까?",
  "action.continue.searching": "계속 검색",
  "new.project.action.text": "새로운 {0, choice, 0# |1#}{1, choice, 0#Java |1#}프로젝트…",
  "project.import.default.name.dotIdea": "{0}에서 가져옴",
  "chooser.description.select.directory.where.external.annotations.are.located": "외부 어노테이션이 있는 디렉터리를 선택하세요.",
  "label.source.directory": "다음 디렉터리가 소스 디렉터리로 표시됩니다.",
  "chooser.title.directory.for.library.files": "라이브러리 파일 디렉터리",
  "rename.module.title": "모듈 이름 변경",
  "action.text.change.module.names": "모듈 이름 변경…",
  "error.message.module.name.prefix.contains.invalid.chars": "접두사는 파일 이름에 사용할 수 있는 문자로 구성되어야 합니다.",
  "path.0.is.invalid.error.message": "경로 ''{0}''이(가) 잘못되었습니다.",
  "classpath.add.simple.module.library.action": "JAR 또는 디렉터리…",
  "project.new.wizard.from.existent.sources.description": "<html>기존 소스 위에 {0} {1} 구조 만들기</html>",
  "dialog.title.copy.library": "라이브러리 복사",
  "action.text.sort.elements.by.names.and.types": "이름 및 유형별로 요소 정렬",
  "dialog.title.new.library": "새로운 라이브러리…",
  "can.t.find.library.for.0": "{0}에 대한 라이브러리를 찾을 수 없습니다.",
  "empty.module.selection.string": "세부 정보를 보거나 편집하려면 여기에서 모듈을 선택하세요.",
  "library.name.already.exists.title": "라이브러리가 이미 존재합니다",
  "message.text.creating.deployment.descriptor": "배포 설명자 만드는 중",
  "modules.order.export.scope.column": "범위",
  "choose.modules.dialog.title": "모듈 선택",
  "class.file.open.source.action": "소스 파일 열기",
  "class.file.open.source.version.specific.action": "라이브러리 루트에서 소스 파일 열기",
  "library.java.attach.files.description": "라이브러리 클래스, 소스, 설명서 또는 네이티브 라이브러리가 있는 파일 또는 디렉터리를 선택하세요.",
  "project.roots.project.banner.text": "프로젝트 ''{0}'' 일반 설정",
  "library.attach.sources.action": "소스 연결",
  "quarantine.cleaner": "격리 해제 도구",
  "chooser.title.attach.external.annotations": "외부 어노테이션 연결",
  "dialog.title.cannot.change.library.0.copy": "복사할 수 없음",
  "dialog.title.cannot.change.library.0.move": "이동할 수 없음",
  "library.name.not.specified.error": "라이브러리 이름을 입력하세요."
}

with open('missing_translations/missing_keys_korean.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for file_entry in data['new_files']:
    if file_entry['filename'] == 'JavaUiBundle.properties':
        file_entry['keys'].update(ko_dict)
        print("Updated JavaUiBundle.properties (Keys 281-320)")
        break

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
