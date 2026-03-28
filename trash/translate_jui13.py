import json

ko_dict = {
  "jar.repository.manager.delegate.repository.usages.dialog.title": "다른 리포지토리에 사용 위임",
  "jar.repository.manager.delegate.repository.usages.dialog.label": "리포지토리에 바인딩된 {0,choice,1#라이브러리가|2#라이브러리가} {0}개 있습니다.<br/>{0,choice,1#라이브러리를|2#라이브러리를} 바인딩할 다른 리포지토리를 선택하세요.",
  "repository.library.bind.repository.not.selected": "<바인딩된 리포지토리 없음>",
  "repository.library.properties.include.transitive.dependencies": "전이적 종속성 포함(&T)",
  "unnamed.title": "<이름 없음>",
  "attach.source.provider.download.sources.action.name": "소스 다운로드",
  "attach.source.provider.download.sources.action.busy.text": "소스 다운로드 중…",
  "progress.details.building.library.dependencies.for.module": "모듈 {0}에 대한 라이브러리 종속성 빌드 중",
  "progress.details.building.module.dependencies.for.module": "모듈 {0}에 대한 모듈 종속성 빌드 중",
  "progress.text.scanning.for.libraries": "라이브러리 검색 중 {0}",
  "progress.text.building.initial.libraries.layout": "라이브러리의 초기 레이아웃 빌드 중…",
  "error.library.with.name.already.exists": "이름이 {0}인 라이브러리가 이미 있습니다.",
  "error.module.with.name.already.exists": "이름이 {0}인 모듈이 이미 있습니다.",
  "libraries.layout.step.description": "감지된 라이브러리를 검토합니다. 이 단계에서 프로젝트에 사용될 라이브러리 이름을 설정하거나,\n프로젝트에서 특정 라이브러리를 제외하거나, 라이브러리 간에 개별 파일을 이동할 수 있습니다.",
  "module.structure.step.description": "프로젝트에 제안된 모듈 구조를 검토합니다. 이 단계에서 모듈 이름을 설정하거나,\n프로젝트에서 특정 모듈을 제외하거나, 개별 모듈을 병합하거나 분할할 수 있습니다.\n모듈 간의 모든 종속성과 라이브러리에 대한 종속성이 자동으로 업데이트됩니다.",
  "label.select.jars.to.extract.to.new.library": "새 라이브러리로 추출할 JAR을 선택하세요(&S):",
  "label.select.content.roots.to.extract.to.new.module": "새 모듈로 추출할 콘텐츠 루트를 선택하세요(&S):",
  "progress.title.searching.for.redundant.dependencies": "''{0}''에서 중복 종속성 검색 중",
  "notification.title.dependencies.were.cleaned.up": "''{0}''의 종속성이 정리되었습니다.",
  "notification.content.transitive.dependencies.were.added": "계속 사용되는 모듈 ''{0}''{1,choice,0#에|1# 및 1개의 다른 모듈에|2# 및 {1}개의 다른 모듈에} 대한 전이적 {1,choice,0#종속성이|1#종속성이} {1,choice,0#직접 종속성으로|1#직접 종속성으로} 추가되었습니다.",
  "notification.content.unused.dependencies.were.removed": "모듈 ''{0}''{1,choice,0#에|1# 및 1개의 다른 모듈에|2# 및 {1}개의 다른 모듈에} 대한 {1,choice,0#종속성이|1#종속성이} 제거되었습니다.<br>{1,choice,0#이 종속성은|1#이 종속성은} 새 모듈을 추출한 후 사용되지 않게 되었습니다. {2}",
  "notification.content.none.module.dependencies.can.be.safely.removed": "모듈 ''{0}'' 종속성 중 안전하게 제거할 수 있는 것은 없습니다.",
  "notification.action.text.show.dependencies": "종속성 표시",
  "tab.title.module.dependencies": "''{0}''의 종속성",
  "title.module.dependencies": "모듈 종속성",
  "title.modules": "모듈",
  "title.library.contents": "라이브러리 콘텐츠",
  "title.libraries": "라이브러리",
  "default.project.structure.root.type.name": "콘텐츠",
  "module.insight.scan.progress.text.scanning": "검색 중 {0}",
  "module.insight.scan.progress.text.building.modules.layout": "모듈 레이아웃 빌드 중…",
  "module.wizard.dialog.title": "{1, choice, 0#|1#{2}에서 }{0, choice, 0#프로젝트|1#모듈} 가져오기",
  "ivi.attach.source.provider.action.name": "Ivy 리포지토리에서 소스 연결",
  "library": "라이브러리",
  "checkbox.for.generated.resources": "생성된 리소스의 경우(&G)",
  "modification.imported.model.warning.label.text": "{0}은(는) {1}에서 가져왔습니다. 구성을 변경하면 다시 가져온 후에 손실될 수 있습니다.",
  "library.0": "라이브러리 ''{0}''",
  "downloadable.library.type.description": "{0} 라이브러리{2, choice, 0#(버전 {1})|1#}",
  "repository.library.type.maven.description": "Maven: {0}",
  "project.configurable.dialog.message": "프로젝트 이름은 필수입니다."
}

with open('missing_translations/missing_keys_korean.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for file_entry in data['new_files']:
    if file_entry['filename'] == 'JavaUiBundle.properties':
        file_entry['keys'].update(ko_dict)
        print("Updated JavaUiBundle.properties (Keys 481-520)")
        break

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
