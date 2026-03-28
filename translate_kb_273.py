import json

translations = {
  "testng.util.found.test.class": "테스트 클래스 {0}을(를) 찾았습니다.",
  "testng.util.searching.test.progress.title": "테스트 검색 중…",
  "testng.util.unable.to.convert": "변환할 수 없습니다.",
  "testng.util.will.be.added.to.module.classpath": "TestNG가 모듈 클래스 경로에 추가됩니다.",
  "action.excludeFromTestNGSuite.text": "스위트에서 제외",
  "action.AddToTestNGSuite.text": "임시 스위트에 추가",
  "inspection.data.provider.return.type.check": "데이터 제공자는 배열 또는 이터레이터를 반환해야 합니다.",
  "inspection.data.provider.return.type.multi.check": "데이터 제공자는 다차원 배열을 반환하거나, 배열을 타입 인수로 사용하는 이터레이터를 반환해야 합니다.",
  "inspection.testNG.data.provider.display.name": "데이터 제공자 문제",
  "inspection.data.provider.return.type.display.name": "잘못된 데이터 제공자 반환 유형",
  "inspection.duplicated.data.provider.names.display.name": "중복된 데이터 제공자 이름",
  "inspection.expected.exception.never.thrown.testNG.display.name": "테스트 메서드 본문에서 발생할 것으로 예상된 예외가 발생하지 않음",
  "inspection.undeclared.tests.display.name": "선언되지 않은 테스트",
  "inspection.groups.testNG.display.name": "정의되지 않은 그룹 이름",
  "inspection.depends.on.method.testNG.display.name": "'dependsOnMethods'에 잘못된 메서드 이름이 전달됨",
  "inspection.convert.javadoc.display.name": "TestNG Javadoc을 어노테이션으로 변환할 수 있습니다.",
  "inspection.convert.old.annotations.display.name": "이전 TestNG 어노테이션인 @Configuration이 사용되었습니다.",
  "inspection.junit.testNG.display.name": "JUnit 테스트를 TestNG로 변환할 수 있습니다.",
  "package.browser.dialog.title.choose.package": "패키지 선택",
  "test.class.browser.dialog.title.choose.test.class": "테스트 클래스 선택",
  "testng.config.editor.dialog.title.choose.listener.class": "리스너 클래스 선택",
  "testng.test.class.dialog.message.invalid.scope.specified.exception": "지정된 범위가 잘못되었습니다.",
  "testng.dialog.message.unable.to.parse.specified.exception": "지정한 ''{0}''을(를) 파싱할 수 없습니다.",
  "testng.dialog.message.no.pattern.selected.warning": "선택한 패턴이 없습니다.",
  "tetsng.dialog.message.package.not.found.exception": "''{0}'' 패키지를 찾을 수 없습니다.",
  "testng.dialog.message.method.doesn.t.contain.test.exception": "''{0}'' 메서드에 테스트가 포함되어 있지 않습니다.",
  "testng.dialog.message.method.not.found.exception": "''{0}'' 메서드를 찾을 수 없습니다.",
  "testng.dialog.message.class.not.found.exception": "''{0}'' 클래스를 찾을 수 없습니다.",
  "testng.dialog.message.invalid.scope.specified.exception": "지정된 범위가 잘못되었습니다.",
  "dialog.message.no.tests.found.in.package": "\"{0}\" 패키지에서 테스트를 찾을 수 없습니다.",
  "dialog.message.cannot.test.anonymous.or.local.class": "익명 또는 로컬 클래스 \"{0}\"을(를) 테스트할 수 없습니다.",
  "dialog.message.no.tests.found.in.class": "\"{0}\" 클래스에서 테스트를 찾을 수 없습니다.",
  "dialog.message.unable.to.bind.to.port": "{0} 포트에 바인딩할 수 없습니다.",
  "dialog.message.unable.to.parse.suite": "스위트를 파싱할 수 없습니다( {0} ).",
  "checkbox.testng.test": "TestNG 테스트 메서드",
  "dialog.message.no.tests.found.in.for.patterns": "\"{0}\" 패턴에 해당하는 테스트를 찾을 수 없습니다.",
  "dialog.message.cannot.test.anonymous.or.local.class2": "익명 또는 로컬 클래스 \"{0}\"을(를) 테스트할 수 없습니다.",
  "inspection.message.data.provider.with.name.already.exists.in.context": "이름이 ''{0}''인 데이터 제공자가 컨텍스트에 이미 존재합니다.",
  "intention.family.name.convert.testng.javadoc.to.annotations": "TestNG Javadoc을 1.5 어노테이션으로 변환",
  "inspection.message.testng.javadoc.can.be.converted.to.annotations": "TestNG Javadoc을 어노테이션으로 변환할 수 있습니다.",
  "intention.family.name.convert.testcase.to.testng": "TestCase를 TestNG로 변환",
  "intention.family.name.convert.old.configuration.testng.annotations": "이전 @Configuration TestNG 어노테이션 변환",
  "inspection.message.old.testng.annotation.configuration.used": "이전 TestNG 어노테이션인 @Configuration이 사용되었습니다.",
  "label.source.location.test.type": "소스 위치",
  "label.pattern.test.type": "패턴",
  "label.suite.test.type": "스위트",
  "label.group.test.type": "그룹",
  "label.method.test.type": "메서드",
  "label.class.test.type": "클래스",
  "label.all.in.package.test.type": "패키지 내 모두"
}

with open("missing_translations/missing_keys_korean.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for file_info in data.get("new_files", []):
    if file_info.get("filename") == "TestngBundle.properties":
        keys_dict = file_info.get("keys", file_info.get("properties", {}))
        keys_dict.update(translations)
        file_info["keys"] = keys_dict
        break

with open("missing_translations/missing_keys_korean.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)
