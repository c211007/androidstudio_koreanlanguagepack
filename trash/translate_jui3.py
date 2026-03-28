import json

ko_dict = {
  "library.attach.sources.action.busy.text": "연결 중…",
  "action.text.new.module": "새로운 모듈",
  "dialog.title.edit.repository.0": "{0} 편집",
  "button.unmark.test.resource": "테스트 리소스 표시 해제",
  "project.roots.module.duplicate.name.message": "중복된 모듈 이름",
  "title.question": "질문",
  "prompt.please.select.project.jdk": "프로젝트 SDK를 선택하세요.\n이 SDK는 모든 프로젝트 모듈에서 기본적으로 사용됩니다.",
  "project.roots.module.groups.text": "모듈 그룹은 프로젝트 모듈을 논리적으로 구성하는 데 사용됩니다.",
  "project.roots.external.annotations.description": "이 모듈에 연결된 외부 어노테이션을 관리합니다.",
  "settings.remote.repo.artifactory.or.nexus": "Artifactory 또는 Nexus 서비스 URL",
  "module.new.action": "새로운 모듈…",
  "project.roots.native.library.node.text": "기본 라이브러리 위치",
  "button.add.selected": "선택 항목 추가",
  "label.project.roots.not.found": "프로젝트의 소스 파일을 찾을 수 없습니다.",
  "progress.text.processing.0.project.roots": "{0}개 프로젝트 루트 처리 중…",
  "label.missed.libraries.text": "모듈 종속성 목록에서 ''{0}'' 라이브러리를 찾을 수 없습니다.",
  "message.text.error.creating.deployment.descriptor": "배포 항목 생성 오류: {0}",
  "error.message.the.selected.node.consist.of.several.elements.so.it.cannot.be.edited": "선택한 노드는 여러 요소로 구성되어 있어 편집할 수 없습니다.\n출력 레이아웃을 편집하려면 '요소 콘텐츠 표시' 확인란을 선택 해제하세요.",
  "project.structure.empty.text": "<html><body><center>세부 정보를 보거나 편집하려면 여기에서 설정을 선택하세요.</center></body></html>",
  "checkbox.0.library.files.to.copy": "다음으로 라이브러리 파일 복사(&C):",
  "checkbox.0.library.files.to.move": "다음으로 라이브러리 파일 이동(&M):",
  "library.source.mismatch": "라이브러리 소스가 {0} 클래스의 바이트코드와 일치하지 않습니다.",
  "dialog.title.add.frameworks.support": "프레임워크 지원 추가",
  "classpath.add.module.dependency.action": "모듈 종속성…",
  "label.new.name.for.0.1": "{0, choice, 0#라이브러리|1#모듈} ''{1}''의 새 이름:",
  "module.libraries.choose.sources.button": "소스 선택(&S)…",
  "combobox.item.global.library": "전역 라이브러리",
  "popup.title.select.library.type": "라이브러리 유형 선택",
  "label.text.the.following.frameworks.are.detected": "<html>프로젝트에서 몇 가지 프레임워크가 감지되었습니다. 다음 항목을 검토하고 잘못 감지된 프레임워크를 제외하세요.</html>",
  "project.roots.library.problem.message": "종속성 목록에 잘못된 항목 ''{0}''이(가) 있습니다.",
  "sdk.configure.annotations.tab": "어노테이션",
  "project.roots.jdk.banner.text": "SDK ''{0}''",
  "progress.text.searching.frameworks": "프레임워크를 검색하는 중입니다. 잠시 기다려 주세요.",
  "module.new.action.description": "프로젝트에 새 모듈 추가",
  "module.paths.validation.duplicate.source.root.in.same.module.error": "소스 루트 ''{0}''이(가) 모듈 ''{1}''에 중복되었습니다.",
  "progress.title.downloading.sources": "소스 다운로드 중",
  "label.text.output.directory": "출력 디렉터리:",
  "prompt.project.wizard.directory.does.not.exist": "{0}''{1}''\n이(가) 없습니다. {2}에서 만듭니다.",
  "project.roots.path.tab.title": "경로",
  "dialog.title.copy.artifact": "아티팩트 복사"
}

with open('missing_translations/missing_keys_korean.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for file_entry in data['new_files']:
    if file_entry['filename'] == 'JavaUiBundle.properties':
        file_entry['keys'].update(ko_dict)
        print("Updated JavaUiBundle.properties (Keys 81-120)")
        break

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
