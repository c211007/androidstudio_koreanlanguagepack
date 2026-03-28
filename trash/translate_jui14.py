import json

ko_dict = {
  "project.jdks.configurable.empty.selection.string": "세부 정보를 보거나 편집하려면 여기에서 SDK를 선택하세요.",
  "project.structure.configurable.reset.text": "프로젝트 구조를 다시 설정하는 중",
  "facet.project.structure.display.text": "모듈 ''{1}''의 패싯 ''{0}''",
  "library.project.structure.invalid.roots.description": "라이브러리 {0}에 손상된 {1} {2, choice, 0#root|1#roots}이(가) 있습니다.",
  "library.0.is.not.used": "라이브러리 {0}이(가) 사용되지 않습니다.",
  "label.remove.invalid.roots": "잘못된 {0, choice, 0#루트|1#루트} 제거",
  "label.add.to.dependencies": "종속성에 추가…",
  "label.remove.library": "라이브러리 제거",
  "label.remove.all.unused.libraries": "사용하지 않는 모든 라이브러리 제거",
  "circular.dependencies.message": "순환 종속성",
  "layout.tree.check.can.remove.dialog.message": "선택한 노드는 {1, choice, \n    1#''''{0}'''' 요소에 속합니다.|\n    2#{1}개의 요소에 속합니다.}\n  아티팩트에서 {1, choice, \n    1#전체 ''''{0}'''' 요소를 제거 | \n    2#이 모든 요소를 제거 }하시겠습니까?",
  "action.hide.content.text": "콘텐츠 숨기기{1, choice, 1#(''''{0}'''')|2#}",
  "popup.title.surround.with": "다음으로 둘러싸기…",
  "library.source.item.label.invalid.library": "잘못된 라이브러리",
  "library.source.item.label.empty.library": "빈 라이브러리",
  "analyze.module.dependency.action.dialog.message.no.dependency.found": "코드 종속성을 찾을 수 없습니다.{0} 종속성을 제거하시겠습니까?",
  "analyze.module.dependency.however.exported.by": "그러나 ''{2}''에서 내보낸 ''{0}''{3, choice, \n      0#|\n      1# 및 ''''{1}''''|\n      2# 및 {3}개의 추가 종속성}이 코드에서 사용됩니다.",
  "analyze.module.dependency.replace.dialog.confirm.replace": "''{0}''에 대한 종속성을 {1, choice, \n      1#''''{2}''''에 대한 직접 종속성|\n      2#직접 종속성}으로 바꾸시겠습니까?",
  "analyze.module.dependency.replace.dialog.message": "직접적인 코드 종속성을 찾을 수 없습니다.{0}\n{1}\n{2}",
  "downloadable.library.properties.change.version.title": "버전 변경(&V)…",
  "notification.content.no.files.were.downloaded": "{0}에 대해 다운로드된 파일이 없습니다.",
  "notification.content.no.files.were.downloaded.multiple": "{0} 및 {1}개에 대해 다운로드된 파일이 없습니다.",
  "library.jars.diff.dialog.0.jars.differ.from.1.library.jars": "{0} JAR이 ''{1}'' 라이브러리 JAR과 다릅니다.",
  "library.jars.change.coordinates.action.title": "좌표 변경…",
  "project.structure.dialog.title.choose.libraries": "라이브러리 선택",
  "add.idea.module.label": "Intellij IDEA 모듈 추가",
  "existing.sources": "기존 소스",
  "label.ipr.file.based": ".ipr(파일 기반)",
  "label.directory.based": "{0}(디렉터리 기반)",
  "select.imported.projects.dialog.message.nothing.found": "가져올 항목이 없습니다.",
  "select.imported.projects.dialog.title.unable.to.proceed": "계속할 수 없음",
  "fix.link.text": "수정",
  "facet.title": "패싯",
  "choose.module": "모듈 선택",
  "facet.will.be.added.to.selected.module": "{0} 패싯이 선택한 모듈에 추가됩니다.",
  "select.parent.facet": "상위 패싯 선택",
  "library.name.is.not.specified": "라이브러리 이름이 지정되지 않았습니다.",
  "no.facets.are.configured": "구성된 패싯이 없습니다.",
  "text.press.button.to.add.new.facet": "새 패싯을 추가하려면 '+' 버튼을 누르세요."
}

with open('missing_translations/missing_keys_korean.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for file_entry in data['new_files']:
    if file_entry['filename'] == 'JavaUiBundle.properties':
        file_entry['keys'].update(ko_dict)
        print("Updated JavaUiBundle.properties (Keys 521-560)")
        break

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
