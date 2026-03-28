import json

translations = {
  "inspection.depends.on.groups.add.as.defined.test.group.fix": "''{0}''을(를) 정의된 테스트 그룹으로 추가합니다.",
  "inspection.depends.on.groups.defined.groups.panel.title": "정의된 그룹(&D):",
  "inspection.depends.on.groups.family.name": "TestNG",
  "inspection.depends.on.groups.undefined.group.problem": "''{0}'' 그룹이 정의되지 않았습니다.",
  "inspection.depends.on.method.duplicated.name.problem": "중복된 메서드 이름: {0}",
  "inspection.depends.on.method.unknown.method.problem": "알 수 없는 메서드 ''{0}''입니다.",
  "inspection.depends.on.method.check": "메서드 ''{0}''에 () 문자가 포함되어서는 안 됩니다.",
  "inspection.depends.on.method.is.not.test": "메서드 ''{0}''은(는) 테스트 또는 구성 메서드가 아닙니다.",
  "inspection.depends.on.method.is.not.annotated": "메서드 ''{0}''에 @{1} 어노테이션이 지정되지 않았습니다.",
  "inspection.testng.data.provider.does.not.exist.problem": "데이터 제공자가 존재하지 않습니다.",
  "inspection.testng.data.provider.need.to.be.static": "외부 클래스의 데이터 제공자는 static이어야 합니다.",
  "inspection.testng.expected.exception.never.thrown.problem": "예상되는 <code>#ref</code> 예외가 ''{0}()'' #loc의 본문에서 발생하지 않았습니다.",
  "inspection.undeclared.test.create.suite.fix": "스위트 만들기",
  "inspection.undeclared.test.problem.descriptor": "선언되지 않은 테스트 ''{0}''입니다.",
  "inspection.undeclared.test.register": "''{0}'' 등록",
  "inspection.undeclared.test.register.test": "테스트 등록",
  "junit.configuration.test.runner.parameters.label": "테스트 러너 매개변수(&R):",
  "test.case.can.be.converted.to.testng": "TestCase를 TestNG로 변환할 수 있습니다.",
  "testng.annotate.dialog.title": "어노테이션",
  "testng.browse.button.title": "TestNG",
  "testng.choose.test.group": "테스트 그룹 선택",
  "testng.configuration.across.module.dependencies.radio": "모듈 종속성 전체(&D)",
  "testng.configuration.class.label": "클래스(&C)",
  "testng.configuration.group.label": "그룹(&G)",
  "testng.configuration.in.single.module.radio": "단일 모듈에서(&S)",
  "testng.configuration.in.whole.project.radio": "전체 프로젝트에서(&W)",
  "testng.configuration.jdk.settings.pane": "JDK 설정",
  "testng.configuration.listeners.pane": "리스너",
  "testng.configuration.method.label": "메서드(&E)",
  "testng.configuration.output.directory": "출력 디렉터리(&O)",
  "testng.configuration.package.label": "패키지(&G)",
  "testng.configuration.parameters.pane": "매개변수",
  "testng.configuration.pattern.label": "패턴",
  "testng.configuration.properties.file": "속성 파일(&P)",
  "testng.configuration.suite.label": "스위트(&S)",
  "testng.configuration.test.kind.label": "테스트 종류:",
  "testng.configuration.use.default.reporters.option": "기본 리포터 사용",
  "testng.create.new.method.dialog.title": "새 메서드 만들기",
  "testng.create.setup.dialog.message": "''{0}'' 메서드가 이미 존재하지만 @BeforeMethod 어노테이션이 지정되지 않았습니다.",
  "testng.create.setup.dialog.title": "SetUp 만들기",
  "testng.entry.point.test.cases": "TestNG 테스트 케이스",
  "testng.group.browser.cannot.browse.groups": "그룹을 찾아볼 수 없음",
  "testng.group.browser.no.tests.found.in.project": "프로젝트에서 테스트를 찾을 수 없음",
  "testng.output.directory.button.title": "TestNG",
  "testng.parameters.table.model.name": "이름",
  "testng.parameters.table.model.value": "값",
  "testng.select.output.directory": "테스트 출력 디렉터리 선택",
  "testng.select.properties.file": "테스트 속성을 지정할 .properties 파일 선택",
  "testng.suite.browser.select.suite": "스위트 선택",
  "testng.suite.browser.select.xml.or.yaml.suite.file": "스위트(.xml 또는 .yaml) 파일을 선택하세요."
}

with open("missing_translations/missing_keys_korean.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for file_info in data.get("new_files", []):
    if file_info.get("filename") == "TestngBundle.properties":
        keys_dict = file_info.get("keys", file_info.get("properties", {}))
        keys_dict.update(translations)
        file_info["keys"] = keys_dict
        break
else:
    data.setdefault("new_files", []).append({
        "filename": "TestngBundle.properties",
        "keys": translations
    })

with open("missing_translations/missing_keys_korean.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)
