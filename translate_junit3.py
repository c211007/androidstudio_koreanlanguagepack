import json

ko_dict = {
  "junit.configuration.repeat.mode.until.stopped": "중지될 때까지",
  "junit.configuration.fork.mode.none": "없음",
  "junit.configuration.fork.mode.method": "메서드",
  "junit.configuration.fork.mode.class": "클래스",
  "junit.configuration.fork.mode.repeat": "반복",
  "combobox.changelists.all": "모두",
  "no.module.selected.error.message": "선택된 모듈 없음",
  "category.interface.dialog.title": "카테고리 인터페이스",
  "running.tests.disabled.during.index.update.error.message": "색인 업데이트 중에는 테스트 실행이 비활성화됩니다.",
  "dialog.message.failed.to.resolve.maven.id": "{0} 해결 실패",
  "junit5.migration.description": "JUnit 4 테스트 어노테이션을 새로운 jupiter 어노테이션으로 전송하면 빨간색 코드가 나타날 수 있습니다! 어설션은 마이그레이션되지 않습니다. \n  완전히 자동으로 변환될 수 있는 테스트만 마이그레이션하려면 'JUnit | JUnit 4 테스트를 JUnit 5로 변환 가능' 검사를 참조하세요.",
  "progress.title.download.additional.dependencies": "추가 종속성 다운로드 중…",
  "junit.config.with.parameter.0": "\\ 매개변수 \"{0}\" 사용",
  "dialog.title.preparing.test": "테스트 준비 중",
  "junit.inspections.group.name": "JUnit",
  "jvm.inspections.junit3.super.teardown.display.name": "JUnit 3 'super.tearDown()'이 'finally' 블록에서 호출되지 않음",
  "jvm.inspections.junit3.super.teardown.problem.descriptor": "'finally' 블록에서 <code>#ref()</code>이(가) 호출되지 않음 #loc",
  "jvm.inspections.junit.mixed.annotations.name": "단일 TestCase의 여러 버전에 대한 JUnit API 사용량",
  "jvm.inspections.junit.mixed.annotations.junit.descriptor": "JUnit {1} TestCase를 확장하는 클래스 내부의 ''@{0}''(으)로 어노테이션이 지정된 <code>#ref()</code> 메서드 #loc",
  "jvm.inspections.junit4.converter.display.name": "JUnit 3 테스트를 JUnit 4로 변환 가능",
  "jvm.inspections.junit4.converter.problem.descriptor": "<code>#ref</code>을(를) JUnit4 테스트 케이스로 변환할 수 있습니다.",
  "jvm.inspections.junit4.converter.quickfix.name": "JUnit 4 테스트 케이스로 변환",
  "jvm.inspections.junit4.converter.quickfix.conflict.semantics": "{1}이(가) JUnit 4로 변환되면 메서드 호출 {0}에서 의미 체계가 변경될 수 있습니다.",
  "jvm.inspections.junit4.converter.quickfix.conflict.suite": "{0}에 대한 모음 메서드 마이그레이션에는 삭제될 부작용이 있습니다.",
  "jvm.inspections.junit4.converter.quickfix.conflict.name": "{0} 메서드는 해당 슈퍼 메서드와 이름이 충돌합니다.",
  "jvm.inspections.junit4.converter.quickfix.conflict.call.compile": "{1}이(가) JUnit 4로 변환되면 메서드 호출 {0}이(가) 컴파일되지 않습니다.",
  "jvm.inspections.junit4.inherited.runwith.display.name": "'@RunWith' 어노테이션이 이미 상위 클래스에 존재함",
  "jvm.inspections.junit4.inherited.runwith.problem.descriptor": "{0} 클래스에 '@RunWith' 어노테이션이 이미 존재함",
  "jvm.inspections.junit5.converter.display.name": "JUnit 4 테스트를 JUnit 5로 변환 가능",
  "jvm.inspections.junit5.converter.problem.descriptor": "#ref은(는) JUnit 5 테스트일 수 있습니다.",
  "jvm.inspections.junit5.converter.quickfix": "JUnit 5로 마이그레이션",
  "jvm.inspections.junit5.converter.quickfix.presentation.text": "어설션 변환",
  "jvm.inspections.junit5.converter.quickfix.conflict.inheritor": "호환되지 않는 상속자가 있어 {0} 클래스를 JUnit 5로 변환할 수 없습니다: {1}",
  "jvm.inspections.junit5.assertions.converter.display.name": "JUnit 5 사용되지 않는 어설션",
  "jvm.inspections.junit5.assertions.converter.problem.descriptor": "''{0}''에서 <code>#ref()</code>에 대한 호출은 ''{1}''의 메서드에 대한 호출로 대체되어야 합니다. #loc",
  "jvm.inspections.junit5.assertions.converter.quickfix": "''{0}'' 메서드 호출로 대체",
  "jvm.inspections.junit5.assertions.converter.familyName": "JUnit 5 호환 호출로 교체",
  "jvm.inspections.unconstructable.test.case.not.public.descriptor": "테스트 클래스 <code>#ref</code>은(는) 'public'이 아니므로 구성할 수 없습니다. #loc",
  "jvm.inspections.unconstructable.test.case.junit3.descriptor": "테스트 클래스 <code>#ref</code>에는 'public' 인수 없는 생성자 또는 단일 'String' 매개변수 생성자가 없으므로 구성할 수 없습니다. #loc",
  "jvm.inspections.unconstructable.test.case.junit4.descriptor": "테스트 클래스 <code>#ref</code>에 정확히 하나의 'public' 인수 없는 생성자가 있어야 하므로 구성할 수 없습니다. #loc"
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

print(f"Updated {filename} (Keys 81-120)")

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
