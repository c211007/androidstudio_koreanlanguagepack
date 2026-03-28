import json
with open('missing_translations/missing_keys_korean.json', 'r', encoding='utf-8') as f:
    ko_data = json.load(f)

translations = {
  "toggle.case.part": "case",
  "java.missed.sdk.click.setup": "<ide/>에서 컴퓨터의 JDK를 찾을 수 없습니다. Java 프로그램을 실행하고 코드 지원을 제공하려면 IDE에 JDK가 필요합니다.\n  JDK를 구성하려면 강조 표시된 {0} 링크를 클릭하세요.",
  "java.missed.sdk.show.options": "클릭하여 사용 가능한 옵션 확인",
  "java.missed.sdk.read.more.tip": "<strong>팁</strong>: JDK에 대한 자세한 내용은 <a href=''{0}''>문서</a>를 참조하세요.",
  "java.missed.sdk.configure": "제안된 옵션 중 하나를 사용하여 JDK를 구성하세요. 다운로드하거나 컴퓨터의 기존 JDK 홈 디렉터리 경로를 지정할 수 있습니다.",
  "java.missed.sdk.wait.installation": "IDE가 JDK를 설치하는 동안 잠시 기다려주세요",
  "java.onboarding.module.name": "온보딩 투어",
  "java.onboarding.module.description": "{0}의 주요 기능에 대한 간략한 개요입니다.",
  "java.onboarding.lesson.name": "IDEA와 친해지기",
  "java.onboarding.change.ui.settings": "이 레슨을 위해 IDEA는 일부 UI 설정을 기본 상태로 변경합니다.\n  레슨을 완료하거나 종료하면 사용자의 기본 설정이 복원됩니다.",
  "java.onboarding.project.view.description": "<strong>프로젝트 도구 창</strong>은 주요 도구 창 중 하나입니다. 이것은 프로젝트 디렉터리, SDK 특화 외부 라이브러리 및 스크래치 파일이 포함되어 있습니다. 스트라이프 버튼을 클릭하여 데모 프로젝트의 내용을 미리 봅니다. {0}을(를) 눌러 열 수도 있습니다.",
  "java.onboarding.balloon.project.view": "클릭하여 <strong>프로젝트 도구 창</strong> 열기",
  "java.onboarding.balloon.source.directory": "{0} 디렉터리를 확장하여 프로젝트 소스 파일 보기",
  "java.onboarding.balloon.open.file": "두 번 클릭하여 {0} 열기",
  "java.onboarding.balloon.open.learn.toolbar": "이 레슨을 계속하려면 {0} 도구 창으로 전환하세요",
  "java.onboarding.indexing.description": "프로젝트를 처음 열면, <ide/>가 코드 지원을 활성화하기 위해 JDK 및 프로젝트를 분석합니다.\n  프로젝트 분석이 완료될 때까지 기다려 주세요.",
  "java.onboarding.wait.indexing": "IDE가 JDK 파일을 분석하는 동안 잠시 기다려주세요",
  "java.onboarding.temporary.configuration.description": "데모 샘플을 열었습니다. 이제 실행해 보겠습니다! 강조 표시된 {0}에서\n  선택한 구성에 대해 널리 쓰이는 실행 액션을 볼 수 있습니다. 예를 들어 코드를 실행({1}) 하거나 디버그({2})할 수 있습니다.",
  "java.onboarding.run.options.community": "커버리지로 실행 {0}과 같은 기타 작업은 {1}을(를) 클릭하여 표시할 수 있습니다.",
  "java.onboarding.run.options.ultimate": "프로파일 {0} 및 커버리지로 실행 {1}과 같은 기타 작업은 {2}을(를) 클릭하여 표시할 수 있습니다.",
  "java.onboarding.run.sample": "일단 현재 파일을 실행해 보겠습니다. {0}을(를) 클릭하거나 {1}을(를) 누르세요.",
  "java.onboarding.run.sample.balloon": "현재 파일을 실행해 보겠습니다. {0}을(를) 클릭하거나 {1}을(를) 누르세요.",
  "java.onboarding.balloon.click.here": "여기를 클릭하여 중단점을 설정하세요.",
  "java.onboarding.toggle.breakpoint.1": "예상 값인 {0} 대신, {1} 메서드가 {2}을(를) 반환하는 것을 눈치채셨을 수 있습니다.\n  문제가 있는 코드를 디버그하기 위해 return 구문에서 정지해 보겠습니다.",
  "java.onboarding.toggle.breakpoint.2": "중단점을 설정하려면 강조 표시된 영역 안의 거터(여백)를 클릭하세요.",
  "java.onboarding.balloon.start.debugging": "아이콘을 클릭하여 디버깅을 시작하세요",
  "java.onboarding.start.debugging": "{0} 아이콘을 클릭하여 디버깅 프로세스를 시작하세요.",
  "java.onboarding.balloon.about.debug.panel": "{0} 도구 창은 다양한 디버깅 작업이 지원되는 툴바를 제공합니다.\n  나중에 {1} 레슨을 통해 시도해 볼 수 있습니다.",
  "java.onboarding.balloon.stop.debugging": "아이콘을 클릭하여 디버깅을 중지하세요",
  "java.onboarding.stop.debugging": "디버깅을 중지해 보겠습니다. {0} 아이콘을 클릭하세요.",
  "java.onboarding.type.division": "코드에서 문제를 발견했으니 수정해 보겠습니다. 결과 합계를 값의 길이로 나누세요.\n  레슨 스크립트가 {0}을(를) 이미 삽입했습니다.",
  "java.onboarding.invoke.completion": "이제 마침표 {0}을(를) 입력하여 사용 가능한 모든 자동 완성 옵션을 표시해 보겠습니다.",
  "java.onboarding.invoke.completion.balloon": "마침표 {0}을(를) 입력하여 사용 가능한 모든 자동 완성 옵션을 표시하세요",
  "java.onboarding.choose.values.item": "이제 {0}을(를) 입력하여 자동 완성 목록을 줄이거나 이 항목을 선택하고 {1}을(를) 누를 수 있습니다.",
  "java.onboarding.invoke.completion.tip": "<strong>팁</strong>: <ide/>는 입력하는 동안 사용 가능한 자동 완성 옵션을 자동으로 표시합니다.\n  또한, {0}을(를) 눌러 코드의 어느 위치에서든 자동 완성 항목을 표시할 수 있습니다.",
  "java.onboarding.invoke.intention.for.warning.1": "방금 버그를 수정했지만 이 코드를 훨씬 더 깔끔하게 만들 수 있습니다.\n  IDEA는 개선할 수 있는 코드 줄을 강조 표시하고 노란색 전구를 추가합니다.",
  "java.onboarding.invoke.intention.for.warning.2": "{0}을(를) 눌러 경고를 미리 보고 퀵픽스를 적용합니다.",
  "java.onboarding.invoke.intention.for.warning.balloon": "{0}을(를) 눌러 사용 가능한 퀵픽스를 표시하세요",
  "java.onboarding.select.fix": "첫 번째 항목인 {0}을(를) 적용합니다. 이 경우 <strong>for-each</strong> 루프를 사용하면 코드를 더 쉽게 이해할 수 있습니다.",
  "java.onboarding.invoke.intention.for.code": "인텐션(의도 작업)은 시간을 절약하고 코딩을 더 쉽게 해줍니다. 문자열 연결(concatenation)을 다시 포맷하는 인텐션을 사용해 보겠습니다.\n  {0}을(를) 눌러 가능한 옵션을 표시하세요."
}

ko_error_bundle = next((x for x in ko_data['new_files'] if x['filename'] == 'JavaLessonsBundle.properties'), None)
if not ko_error_bundle:
    ko_error_bundle = {'filename': 'JavaLessonsBundle.properties', 'keys': {}, 'key_count': 0}
    ko_data['new_files'].append(ko_error_bundle)
ko_error_bundle['keys'].update(translations)
ko_error_bundle['key_count'] = len(ko_error_bundle['keys'])

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(ko_data, f, ensure_ascii=False, indent=2)

print("Updated JavaLessonsBundle.properties part 1")
