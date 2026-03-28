import json

ko_dict = {
  "create.setup.dialog.message": "setUp 메서드가 이미 존재하지만 {0}(으)로 어노테이션이 지정되지 않았습니다. 어노테이션을 지정하시겠습니까?",
  "junit.configuration.display.name": "JUnit",
  "class.isnt.inheritor.of.testcase.error.message": "{0}은(는) TestCase의 상속자가 아닙니다.",
  "cannot.browse.test.inheritors.dialog.title": "TestCase 상속자를 찾아볼 수 없음",
  "junit.configuration.package.label": "패키지(&G):",
  "create.setup.dialog.title": "setUp 메서드 생성",
  "junit.not.found.in.module.error.message": "''{0}'' 모듈에서 JUnit을 찾을 수 없습니다.",
  "junit.configuration.across.module.dependencies.radio": "모듈 종속성 전반(&L)",
  "method.name.not.specified.error.message": "메서드 이름이 지정되지 않았습니다.",
  "junit.configuration.search.for.tests.label": "테스트 검색:",
  "class.not.test.error.message": "''{0}'' 클래스는 테스트가 아닙니다.",
  "configuration.not.specified.message": "구성 테스트 유형이 지정되지 않았습니다: {0}",
  "package.does.not.exist.error.message": "''{0}'' 패키지가 존재하지 않습니다.",
  "test.method.doesnt.exist.error.message": "''{0}'' 테스트 메서드가 존재하지 않습니다.",
  "junit.configuration.in.whole.project.radio": "전체 프로젝트 내(&W)",
  "junit.entry.point.suggest.package.private.visibility.junit5": "JUnit 5 테스트에 대해 package-private 가시성 수준 제안",
  "category.is.not.specified.error.message": "카테고리가 지정되지 않았습니다.",
  "directory.is.not.specified.error.message": "디렉터리가 지정되지 않았습니다.",
  "directory.0.is.not.found.error.message": "''{0}'' 디렉터리를 찾을 수 없습니다.",
  "module.to.choose.classpath.not.specified.error.message": "클래스 경로를 선택할 모듈이 지정되지 않았습니다.",
  "tags.are.not.specified.error.message": "태그가 지정되지 않았습니다.",
  "tag.name.0.must.be.syntactically.valid.warning": "태그 이름 [{0}]은(는) 구문상 유효해야 합니다.",
  "dialog.message.no.unique.id.specified.exception": "고유 ID가 지정되지 않았습니다.",
  "test.kind.hint": "테스트를 검색할 리소스 유형",
  "test.pattern.hint": "테스트를 포함하는 클래스의 이름과 일치하는 정규식",
  "test.class.hint": "테스트를 포함하는 클래스의 정규화된 이름",
  "test.method.hint": "테스트 메서드의 정규화된 이름",
  "test.package.hint": "테스트를 포함하는 패키지의 이름",
  "junit.configuration.kind.all.in.package": "패키지 내 전체",
  "junit.configuration.kind.all.in.directory": "디렉터리 내 전체",
  "junit.configuration.kind.by.pattern": "패턴",
  "junit.configuration.kind.class": "클래스",
  "junit.configuration.kind.method": "메서드",
  "junit.configuration.kind.category": "카테고리",
  "junit.configuration.kind.by.unique.id": "고유 ID",
  "junit.configuration.kind.by.tags": "태그",
  "junit.configuration.repeat.mode.once": "1회",
  "junit.configuration.repeat.mode.n.times": "N번",
  "junit.configuration.repeat.mode.until.failure": "실패할 때까지",
  "junit.configuration.repeat.mode.until.success": "성공할 때까지"
}

with open('missing_translations/missing_keys_korean.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

filename = "JUnitBundle.properties"
found = False
for file_entry in data.get('new_files', []):
    if file_entry['filename'] == filename:
        file_entry['keys'].update(ko_dict)
        found = True
        break
if not found:
    data.setdefault('new_files', []).append({"filename": filename, "keys": ko_dict})

print(f"Updated {filename} (Keys 41-80)")

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
