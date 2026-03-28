import json

ko_dict_jewel = {
  "action.text.more": "더 보기",
  "action.text.open.link.in.browser": "브라우저에서 링크 열기",
  "action.text.copy.link.address": "링크 주소 복사"
}

ko_dict_journeys = {
  "run.configuration.target.picker.popup.title": "테스트 모음 타겟 선택",
  "journeys.test.suite.configuration.error.no.test.suite": "''{0}'' 모듈의 Gradle 빌드 파일에 구성된 테스트 모음이 없습니다.",
  "journeys.test.suite.configuration.error.no.android.model": "''{0}'' 모듈에 대한 Android 모델을 찾을 수 없습니다.",
  "journeys.test.suite.configuration.error.selected.variant.not.enabled": "''{0}'' 테스트 모음이 ''{1}'' 변형을 타겟팅하지 않습니다.",
  "journeys.configuration.type.name": "여정 테스트(지원 중단됨)",
  "journeys.configuration.type.description": "해당 실행 구성은 지원 중단되었습니다. 대신 새로운 테스트 모음 실행 구성을 사용하세요.",
  "journeys.editor.toolbar.run.button.tooltip.enabled": "{0} 실행",
  "journeys.editor.toolbar.run.button.tooltip.disabled.module": "{0} 실행(비활성화됨): Android 모듈을 찾을 수 없음",
  "journeys.editor.toolbar.run.button.tooltip.disabled.build": "{0} 실행(비활성화됨): 호환되는 빌드 시스템을 찾을 수 없음",
  "journeys.editor.toolbar.run.button.tooltip.disabled.indexing": "{0} 실행(비활성화됨): 프로젝트 색인 생성 중에는 여정 실행이 비활성화됨",
  "journeys.editor.toolbar.run.button.tooltip.disabled.empty": "{0} 실행(비활성화됨): 여정을 실행하려면 비어 있지 않은 작업을 하나 이상 추가하세요.",
  "journeys.editor.error.loading.file": "여정 파일을 로드하는 중 오류가 발생했습니다.",
  "journeys.editor.error.parsing.file": "여정 파일을 파싱하는 중 오류가 발생했습니다.",
  "journeys.editor.help.banner.text": "정밀도를 극대화하고 안정성을 높이려면 여정 단계 작성 방법에 대한 가이드라인을 참조하고 현재 지원되거나 지원되지 않는 상호작용을 확인하세요.",
  "journeys.editor.help.banner.action": "가이드라인 보기",
  "journeys.editor.help.banner.dismiss": "닫기",
  "journeys.editor.help.popup.title": "여정 가이드라인",
  "journeys.editor.help.popup.message": "정밀도를 극대화하고 안정성을 높이려면 여정 단계 작성 방법에 대한 가이드라인을 참조하고 현재 지원되거나 지원되지 않는 상호작용을 확인하세요.",
  "journeys.editor.help.popup.action": "가이드라인 보기",
  "journeys.wizard.description": "Gemini 여정을 사용하면 자연어 프롬프트를 사용하여 앱에 대한 엔드투엔드 테스트를 정의하고 실행할 수 있습니다.",
  "journeys.wizard.journey.name.label": "여정 이름",
  "journeys.wizard.journey.file.label": "여정 파일 이름",
  "journeys.wizard.journey.description.label": "여정 설명",
  "journeys.wizard.journey.description.hint": "캡처되는 사용자 여정 설명",
  "journeys.wizard.use.custom.test.suite.checkbox.label": "사용자 지정 테스트 모음 이름 사용:",
  "journeys.wizard.test.suite.warning": "<html>여정에는 테스트 모음으로 구성된 모듈이 필요합니다. Android Gradle 플러그인(AGP)의 테스트 모음 지원은 미리보기로 제공되며 향후 변경될 수 있습니다. 이로 인해 최신 AGP 버전으로 업데이트 기능에 영향을 미칠 수 있습니다.</html>"
}

with open('missing_translations/missing_keys_korean.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for filename, ko_dict in [("JewelIntUIBundle.properties", ko_dict_jewel), ("JourneysBundle.properties", ko_dict_journeys)]:
    found = False
    for file_entry in data.get('new_files', []):
        if file_entry['filename'] == filename:
            file_entry['keys'].update(ko_dict)
            found = True
            break
    if not found:
        data.setdefault('new_files', []).append({"filename": filename, "keys": ko_dict})
    print(f"Updated {filename}")

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
