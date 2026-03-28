import json

ko_dict = {
  "module.add.error.title": "모듈 추가",
  "module.paths.validation.source.root.belongs.to.another.module.error": "소스 루트 ''{0}''은(는)\n중첩된 모듈 ''{2}''의 콘텐츠에 속하므로 모듈 ''{1}''에서 정의할 수 없습니다.",
  "button.stop.searching": "검색 중지(&S)",
  "label.enter.new.name.for.merge.result": "병합 결과의 새 이름 입력:",
  "dialog.title.merge.module.or.library": "병합",
  "library.choose.one.to.attach": "소스를 연결할 라이브러리 선택",
  "radio.create.source.directory": "소스 디렉터리 만들기(&C)",
  "dialog.title.add.framework.0.support": "{0} 지원 추가",
  "action.text.put.into.0.and.link.via.manifest": "''{0}''에 넣고 매니페스트를 통해 연결",
  "project.roots.no.jdk.on.project.message": "생성된 SDK를 프로젝트에 설정하시겠습니까?",
  "prompt.please.select.module.jdk": "이 모듈에 설정할 {0}을(를) 선택하세요.",
  "project.new.wizard.module.file.title": "모듈 파일 위치(&U):",
  "module.javadoc.add.url.button": "JavaDoc URL 추가…",
  "action.stop.searching": "검색 중지",
  "dialog.title.project.initialization.failed": "프로젝트 초기화 실패",
  "project.roots.display.name": "모듈",
  "settings.remote.repo.artifactory.or.nexus.service.urls": "Artifactory 또는 Nexus 서비스 URL:",
  "dialog.title.add.repository.0": "{0} 추가",
  "action.text.cancel.exclusion": "제외 취소",
  "title.test.resources": "테스트 리소스",
  "multiple.facets.banner.0.1.facets": "{1} 패싯 {0}개",
  "title.resources": "리소스",
  "combobox.item.project.library": "프로젝트 라이브러리",
  "action.text.import.module": "모듈 가져오기",
  "modal.text.importing.module": "가져오는 중…",
  "prompt.overwrite.project.folder": "{1}에 {0} 폴더가 이미 있습니다.\n콘텐츠를 덮어쓸 수 있습니다.\n계속하시겠습니까?",
  "label.library.name": "이름(&N):",
  "project.roots.module.banner.text": "모듈 ''{0}''",
  "label.text.no.frameworks.detected": "프레임워크가 감지되지 않았습니다.",
  "directory.module.content.root": "모듈 콘텐츠 루트\n",
  "label.missed.libraries.prefix": "다음 라이브러리가 누락되었습니다.",
  "library.classes.node": "클래스",
  "notification.title.downloading.failed": "다운로드 실패",
  "classpath.chooser.title.add.module.dependency": "모듈 선택",
  "action.name.rename.packaging.element": "이름 변경",
  "module.remove.confirmation.title": "{0, choice, 1#모듈|2#모듈} 제거",
  "settings.label.project.format": "프로젝트 형식:",
  "prompt.enter.project.file.location": "{0} 파일 위치 입력",
  "dependencies.used.in.popup.title": "사용되는 위치",
  "module.libraries.attach.sources.button": "소스 연결(&S)…"
}

with open('missing_translations/missing_keys_korean.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for file_entry in data['new_files']:
    if file_entry['filename'] == 'JavaUiBundle.properties':
        file_entry['keys'].update(ko_dict)
        print("Updated JavaUiBundle.properties (Keys 201-240)")
        break

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
