import json
with open('missing_translations/missing_keys_korean.json', 'r', encoding='utf-8') as f:
    ko_data = json.load(f)

translations = {
  "java.onboarding.invoke.intention.for.code.balloon": "사용 가능한 인텐션을 표시하려면 {0}을(를) 누르세요",
  "java.onboarding.apply.intention": "{0}을(를) 선택하고 {1}을(를) 누르세요.",
  "java.onboarding.invoke.search.everywhere.1": "<ide/>에서 작업하는 동안 프로젝트의 파일, 기호, 클래스 또는 IDE 액션을 검색하고 싶을 수 있습니다. 이번 레슨에서는 {0} 액션을 검색하여 {1} 문자열을 소문자로 만들어 보겠습니다.",
  "java.onboarding.invoke.search.everywhere.2": "{0}을(를) 두 번 눌러 {1} 대화상자를 엽니다.",
  "java.onboarding.search.everywhere.description": "보시다시피 선택한 텍스트인 {0}이(가) 입력 문자열에 자동으로 복사되었습니다. {0} 대신 {1}을(를) 입력해 보겠습니다.",
  "java.onboarding.apply.action": "{0} 액션을 선택하고 {1}을(를) 누르세요.",
  "java.onboarding.case.changed": "대소문자가 변경되었습니다.",
  "java.onboarding.epilog": "축하합니다! 온보딩 투어를 완료했습니다. 이제 다음을 수행할 수 있습니다:\n  \\n  - 학습 프로젝트 <callback id=\"{0}\">닫기</callback>{1}\n  \\n  - 더 많은 레슨 <callback id=\"{2}\">표시</callback>",
  "java.onboarding.feedback.system.found.jdks": "발견된 JDK:",
  "java.onboarding.feedback.system.jdk.at.start": "시작 시 JDK:",
  "java.onboarding.feedback.system.current.jdk": "현재 JDK:",
  "java.onboarding.feedback.system.lang.level": "언어 수준(Language level):",
  "java.basic.completion.choose.first": "{0}을(를) 눌러 조회 메뉴에서 첫 번째 항목을 선택할 수 있습니다.",
  "java.basic.completion.activate": "기본 완성(Basic Completion)을 활성화하려면 {0}을(를) 누르고 다시 조회 메뉴를 확인하세요.",
  "java.basic.completion.choose.item": "조회 메뉴에서 {0}을(를) 선택하고 {1}을(를) 누르세요.",
  "java.basic.completion.complete": "{0}을(를) 눌러 이 문장을 마칩니다.",
  "java.basic.completion.deeper.level": "가끔 정적 상수나 메서드 제안을 봐야 할 때가 있습니다.\n  {0}을(를) 두 번 눌러 조회 항목에 표시합니다.",
  "java.basic.completion.module.promotion": "{0} 모듈에서 리팩토링에 대한 자세한 내용을 찾을 수 있습니다.",
  "java.run.configuration.lets.run": "코드를 실행하는 방법은 여러 가지가 있습니다.\n  {0}을(를) 클릭하고 {1} 항목을 선택하여 여백에서 실행해 보겠습니다.\n  또는 {2}을(를) 누를 수도 있습니다.",
  "java.postfix.completion.type": "괄호 뒤에 {0}을(를) 입력하면 연산자 후위(postfix) 완성 제안 목록이 표시됩니다.",
  "java.postfix.completion.complete": "목록에서 {0}을(를) 선택하거나 편집기에 동일한 값을 입력합니다. {1}을(를) 눌러 문장을 완성하세요.",
  "java.smart.type.completion.apply": "스마트 타입 완성을 사용하면 현재 컨텍스트 내에서 적용할 수 있는 타입만 포함하도록 제안 목록을 필터링합니다. {0}을(를) 눌러 일치하는 제안 목록을 확인하세요. {1}을(를) 눌러 첫 번째 항목을 선택합니다.",
  "java.smart.type.completion.return": "스마트 타입 완성은 return 문에 대한 코드도 제안할 수 있습니다.\n  {0}을(를) 눌러 return에 대한 조회 메뉴를 표시하세요. {1}을(를) 눌러 첫 번째 메뉴를 선택하세요.",
  "java.statement.completion.lesson.name": "구문 완성",
  "java.statement.completion.complete.for": "{0}을(를) 눌러 {1} 문장을 완성하세요.",
  "java.statement.completion.complete.if": "{0}을(를) 입력하고 {1}을(를) 눌러 문장을 생성하세요.",
  "java.statement.completion.complete.condition": "괄호 {0} 안에 조건을 추가하고 {1}을(를) 눌러 {2} 구문 안으로 이동합니다.",
  "java.statement.completion.complete.finish.body": "코드 한 줄({0})을 입력한 다음 {1}을(를) 눌러 구문을 완성하고 서식을 적용하세요.",
  "java.statement.completion.help.link": "구문 완성",
  "java.rename.press.rename": "{0}을(를) 눌러 필드 {1}의 이름을 변경하세요.",
  "java.rename.type.new.name": "이 필드의 새 이름(예: {0})을 입력하고 {1}을(를) 누르세요.",
  "java.rename.confirm.accessors.rename": "<ide/>는 해당 getter/setter를 감지하고 그에 맞게 이름을 바꾸도록 제안합니다.\n  이제 {0}을(를) 누르거나 {1}을(를) 클릭하세요.",
  "java.refactoring.menu.inline.variable.eng": "이제 단일로 사용된 {0} 변수를 이를 정의하는 표현식으로 대체해 보겠습니다.\n  {1}을(를) 누르고 <strong>iv</strong>(<strong>i</strong>nline <strong>v</strong>ariable)를 입력해 리팩토링 메뉴를 필터링할 수 있습니다.\n  이 항목을 선택하거나 {2}을(를) 누르세요.",
  "java.refactoring.menu.inline.variable": "이제 단일로 사용된 {0} 변수를 이를 정의하는 표현식으로 대체해 보겠습니다.\n  {1}을(를) 누르고 목록에서 {2}을(를) 선택하거나 {3}을(를) 눌러 이 액션을 직접 호출할 수 있습니다.",
  "java.refactoring.menu.introduce.constant.eng": "마지막으로, 파일 이름에서 확장자를 추출해 보겠습니다.\n  다시 {0}을(를) 누르고 <strong>ic</strong> (<strong>i</strong>ntroduce <strong>c</strong>onstant)로 필터링하거나 {1}을(를) 누를 수 있습니다.",
  "java.refactoring.menu.introduce.constant": "마지막으로, 파일 이름에서 확장자를 추출해 보겠습니다.\n  다시 {0}을(를) 누르고 {1}을(를) 선택하거나 {2}을(를) 누를 수 있습니다.",
  "java.refactoring.menu.confirm.constant": "이 대화상자에서 새 상수의 타입, 이름, 상위 클래스 및 가시성을 선택할 수 있습니다.\n  기본값을 그대로 두고 {0}을(를) 누르거나 {1}을(를) 클릭할 수 있습니다.",
  "java.editor.coding.assistance.press.to.fix": "{0}을(를) 눌러 인수를 빈 배열로 바꿉니다.",
  "java.extract.method.edit.method.name": "새 메서드의 이름을 편집하거나 IDE가 제안한 이름을 그대로 두세요. 그런 다음 {0}을(를) 누르세요.",
  "java.inheritance.hierarchy.lesson.name": "상속 계층 구조"
}

ko_error_bundle = next((x for x in ko_data['new_files'] if x['filename'] == 'JavaLessonsBundle.properties'), None)
ko_error_bundle['keys'].update(translations)
ko_error_bundle['key_count'] = len(ko_error_bundle['keys'])

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(ko_data, f, ensure_ascii=False, indent=2)

print("Updated JavaLessonsBundle.properties part 2")
