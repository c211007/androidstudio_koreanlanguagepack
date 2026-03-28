import json

ko_dict = {
  "error.directory.read.only": "''{0}'' 디렉터리는 읽기 전용입니다.",
  "project.roots.javadoc.tab.description": "이 모듈에 연결된 외부 JavaDoc을 관리합니다.<br>외부 JavaDoc은 모듈에 포함될 수 있는 JavaDoc 어노테이션을 재정의합니다.",
  "dialog.title.rename.module.or.library.0": "{0, choice, 0#라이브러리|1#모듈} 이름 변경",
  "module.remove.confirmation": "프로젝트에서 {1, choice, 1#모듈 ''''{0}''''|2#{1}개 모듈}을(를) 제거하시겠습니까?\n디스크의 파일은 삭제되지 않습니다.",
  "title.no.jdk.specified": "지정된 SDK가 없음",
  "project.roots.error.message.invalid.roots": "잘못된 {0} {1, choice, 1#root|2#roots}",
  "label.available.elements": "사용 가능한 요소",
  "new.library.file.chooser.description": "라이브러리 클래스가 있는 JAR 파일을 선택하세요.",
  "dialog.message.obsolete.library.files.remover.delete.files": "다음 선택한 {0,choice,1#파일은|2#파일은} 더 이상 사용되지 않습니다: \n  {1}\n  {0,choice,1#이|2#이} 파일을 삭제하시겠습니까?\n  이 작업을 완전히 실행 취소하지 못할 수 있습니다!",
  "module.paths.searching.source.roots.title": "소스 루트 추가 중",
  "project.roots.library.banner.text": "{1} ''{0}''",
  "settings.remote.repo.no.remote.repositories": "원격 리포지토리 없음",
  "module.libraries.target.jdk.module.radio": "모듈 SDK(&M):",
  "dialog.title.cannot.create.facet": "패싯을 만들 수 없습니다.",
  "classpath.panel.navigate.action.text": "탐색",
  "facet.defaults.display.name": "기본값",
  "quarantine.clean.progress": "격리 상태 지우는 중",
  "quarantine.error.message": "격리 상태를 지우지 못했습니다: {0}",
  "chooser.title.exclude.from.library": "라이브러리에서 제외",
  "radio.do.not.create.source.directory": "소스 디렉터리 만들지 않음(&D)",
  "sdk.missing.item": "<SDK 없음>",
  "jdk.missing.item": "<JDK 없음>",
  "jdk.missing.item.no.internet.comment": "JDK를 다운로드하려면 안정적인 인터넷 연결이 필요합니다. 나중에 파일 | 프로젝트 구조에서 구성하세요.",
  "jdk.missing.item.comment": "나중에 파일 | 프로젝트 구조에서 JDK를 구성하세요.",
  "jdk.project.item": "프로젝트 JDK",
  "jdk.registered.items": "등록된 JDK",
  "jdk.detected.items": "감지된 JDK",
  "jdk.download.predefined.item": "{0} 다운로드",
  "jdk.download.item": "JDK 다운로드…",
  "jdk.location.error": "''{0}''에 JDK를 설치할 수 없습니다.",
  "jdk.download.comment": "프로젝트 생성 시 JDK가 다운로드 및 설치됩니다.",
  "jdk.incompatible.location.error": "호환되지 않는 JDK 위치입니다. 선택한 JDK는 {0}에 있지만 프로젝트는 {1}에 있습니다.",
  "button.set.default": "기본값 설정",
  "prompt.enter.relative.path.to.module.content.root": "모듈 콘텐츠 루트에 대한 상대 경로를 입력하세요(예: java{0}src):",
  "classpath.add.library.action": "라이브러리…",
  "error.cannot.parse.project": "{0} 프로젝트를 구문 분석할 수 없습니다.",
  "project.new.wizard.module.root.title": "콘텐츠 루트(&R):",
  "sdk.configure.save.settings.error": "설정을 저장할 수 없습니다.",
  "action.description.add.the.library.to.the.dependencies.list.of.chosen.modules": "선택한 모듈의 종속성 목록에 라이브러리 추가",
  "settings.remote.repo.service.url": "서비스 URL"
}

with open('missing_translations/missing_keys_korean.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for file_entry in data['new_files']:
    if file_entry['filename'] == 'JavaUiBundle.properties':
        file_entry['keys'].update(ko_dict)
        print("Updated JavaUiBundle.properties (Keys 321-360)")
        break

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
