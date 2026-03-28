import json
with open('missing_translations/missing_keys_korean.json', 'r', encoding='utf-8') as f:
    ko_data = json.load(f)

translations = {
  "java.inheritance.hierarchy.goto.implementation": "{1}의 구현(implementation)을 찾으려면 {0}을(를) 누르세요.",
  "java.inheritance.hierarchy.choose.any.implementation": "임의의 구현을 선택하고 {0}을(를) 누르거나 클릭하세요.",
  "java.inheritance.hierarchy.navigate.to.base": "파생된 메서드에서 슈퍼 메서드로 이동할 수 있습니다. {0}을(를) 누르거나 편집기 여백(거터)에서 {1} 아이콘을 클릭하세요.",
  "java.inheritance.hierarchy.invoke.implementations.again": "기본(base) 메서드의 선언에는 고유한 여백 아이콘({0})이 있습니다.\n  이를 클릭하거나 {1}을(를) 다시 누르세요.",
  "java.inheritance.hierarchy.open.in.find.tool.window": "거대한 계층 구조인 경우, {0} 도구 창에서 구현을 검색해야 할 수도 있습니다.\n  {1}을(를) 클릭하세요.",
  "java.inheritance.hierarchy.hide.find.tool.window": "{1} 도구 창을 숨기려면 {0}을(를) 누르세요.",
  "java.inheritance.hierarchy.open.method.hierarchy": "이 메서드의 전체 계층 구조를 탐색할 수 있습니다. {0}을(를) 누르세요.",
  "java.inheritance.hierarchy.hide.method.hierarchy": "{0} 또한 숨겨보겠습니다. 다시 {1}을(를) 누르세요.",
  "java.inheritance.hierarchy.open.class.hierarchy": "클래스 계층 구조를 보려면 {0}을(를) 누르세요.",
  "java.inheritance.hierarchy.last.note": "<strong>참고:</strong> {0} 및 {1} 액션은 클래스에도 적용할 수 있습니다.\n  {2} 및 {3} 액션은 거의 사용되지 않지만, {5} 필터를 써서 {4}을(를) 통해 항상 찾을 수 있습니다.",
  "java.inheritance.hierarchy.help.link": "소스 코드 계층 구조",
  "java.debug.workflow.hotswap.disabled.warning": "IDE 설정에서 <strong>Hot Swap(핫 스왑)</strong> 기능이 비활성화되어 있습니다.\n  {0} | {1} | {2} <strong>\\u2192</strong> {3}에서 활성화하거나 <callback id=\"{4}\">클릭하여 활성화</callback>하세요.",
  "java.debug.workflow.rebuild": "버그 수정 후에 작은 프로그램을 재실행할 수 있지만, 큰 프로그램의 경우 재실행에 오랜 시간이 걸릴 수 있습니다.\n  수정 사항이 이 경우처럼 순수 메서드에만 영향을 주는 경우, 재실행하는 대신 프로젝트를 빌드하고 <strong>Hot Swap(핫 스왑)</strong>을 적용할 수 있습니다.\n  프로젝트를 빌드하려면 {0}을(를) 누르세요.",
  "java.debug.workflow.confirm.hot.swap": "<strong>Hot Swap(핫 스왑)</strong> 다시 로드를 확인하세요.",
  "java.debug.workflow.no.confirmation": "<strong>Hot Swap(핫 스왑)</strong>은 백그라운드에서 자동으로 수행됩니다. 좌측 하단 모서리에 관련 메시지가 표시될 수 있습니다.",
  "java.debug.workflow.drop.frame": "메서드를 패치했지만, 우리는 여전히 구식이 된(예외가 다시 발생할) {0}을(를) 실행 중입니다.\n  프레임을 삭제(drop)하고 {1}이(가) 호출되기 전 상태로 돌아가 보겠습니다. 스택 프레임 상단 호출 근처에 있는 {2}을(를) 클릭하거나 {3}을(를) 누르세요.",
  "java.debug.workflow.invalid.drop": "레슨에서 계획하지 않은 작업을 수행한 것 같습니다. 레슨을 다시 시작해 주세요."
}

ko_error_bundle = next((x for x in ko_data['new_files'] if x['filename'] == 'JavaLessonsBundle.properties'), None)
ko_error_bundle['keys'].update(translations)
ko_error_bundle['key_count'] = len(ko_error_bundle['keys'])

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(ko_data, f, ensure_ascii=False, indent=2)

print("Updated JavaLessonsBundle.properties part 3")
