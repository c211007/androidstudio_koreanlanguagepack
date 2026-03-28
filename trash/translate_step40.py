import json
with open('missing_translations/missing_keys_korean.json', 'r', encoding='utf-8') as f:
    ko_data = json.load(f)

translations = {
  "title.project.java.version.label": "Java:",
  "title.project.config.file.format.label": "구성(Configuration):",
  "title.project.version.label": "버전:",
  "title.project.dependencies.label": "종속성:",
  "title.project.dependencies.selected.label": "추가된 종속성:",
  "title.server.url.dialog": "서버 URL",
  "hint.library.search": "검색",
  "hint.no.library.selected": "선택되지 않음",
  "hint.dependencies.not.selected": "추가된 종속성 없음",
  "message.specified.path.is.illegal": "지정된 경로가 잘못되었습니다",
  "message.directory.not.writable.error": "디렉터리에 쓸 수 없습니다",
  "message.file.not.directory.error": "지정된 경로가 디렉터리가 아닙니다",
  "message.directory.not.empty.warning": "디렉터리가 비어 있지 않습니다",
  "message.directory.0.not.empty.warning": "''{0}'' 디렉터리가 비어 있지 않습니다",
  "project.settings.warnings.group": "경고:",
  "project.settings.warnings.ignore": "무시하고 계속하시겠습니까?",
  "onboarding.search.everywhere.tip.comment.1": "{0} 키를 두 번 눌러 전체 검색(Search Everywhere) 대화상자를 열고 `show whitespaces`를 입력하세요.",
  "onboarding.search.everywhere.tip.comment.2": "그런 다음 Enter 키를 누르세요. 이제 코드에서 공백 문자를 볼 수 있습니다.",
  "onboarding.show.intention.tip.comment.1": "강조 표시된 텍스트에 캐럿을 놓고 {0} 키를 눌러 확인하세요.",
  "onboarding.show.intention.tip.comment.2": "{0}이(가) 어떻게 수정할지 제안합니다.",
  "onboarding.run.comment": "코드를 실행하려면 {0} 키를 누르거나 거터(gutter)의 녹색 화살표 버튼을 클릭하세요.",
  "onboarding.debug.comment.1": "코드 디버깅을 시작하려면 {0} 키를 누르세요. 하나의 중단점(breakpoint)이 설정되어 있습니다.",
  "onboarding.debug.comment.2": "언제든지 {0} 키를 눌러 더 추가할 수 있습니다.",
  "onboarding.run.comment.render.1": "코드를 <b>실행</b>하려면 {0} 키를 누르거나,",
  "onboarding.run.comment.render.2": "거터에서 {0} 아이콘을 클릭하세요.",
  "onboarding.show.intention.tip.comment.render.1": "강조 표시된 텍스트에 캐럿을 놓고 {0} 키를 누르세요.",
  "onboarding.show.intention.tip.comment.render.2": "{0}이(가) 이 부분을 어떻게 수정할지 제안합니다.",
  "onboarding.debug.comment.render.1": "코드 디버깅을 시작하려면 {0} 키를 누르세요. 하나의 {1} 중단점이 설정되어 있습니다.",
  "onboarding.debug.comment.render.2": "언제든지 {0} 키를 눌러 더 추가할 수 있습니다."
}

ko_error_bundle = next((x for x in ko_data['new_files'] if x['filename'] == 'JavaStartersBundle.properties'), None)
ko_error_bundle['keys'].update(translations)
ko_error_bundle['key_count'] = len(ko_error_bundle['keys'])

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(ko_data, f, ensure_ascii=False, indent=2)

print("Updated JavaStartersBundle part 2 (Final)")