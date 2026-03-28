import json

translations = {
  "designer.action.generate.screenshot.test": "스크린샷 테스트 생성",       
  "designer.action.generate.screenshot.test.description": "AI를 사용하여 레이아웃에 대한 스크린샷 테스트를 생성합니다.",
  "designer.ml.agent.generating.screenshot.test": "{0}에 대한 테스트 생성 중...", 
  "designer.ml.agent.screenshot.test.generation.title": "스크린샷 테스트 생성",
  "designer.ml.migration.agent.migrating.layout": "{0}을(를) Compose로 마이그레이션 중...",
  "designer.ml.migration.agent.migration.title": "XML을 Compose로 마이그레이션",    
  "designer.ml.actions.progress.indicator.generating.preview.title": "미리보기 생성 중",
  "designer.ml.actions.progress.indicator.generating.previews.title": "미리보기 생성 중",
  "designer.ml.preview.generation.agent.generate.preview.for": "{0}의 미리보기 생성",
  "designer.ml.preview.generation.agent.generate.previews.for": "{0}의 미리보기 생성",
  "screenshot.to.code.action.title": "이미지에서 코드 생성",
  "screenshot.to.code.action.description": "첨부된 이미지에서 Jetpack Compose 코드를 생성합니다.",
  "designer.circle.to.fix.balloon.title": "해결할 원",
  "designer.circle.to.fix.balloon.placeholder": "이 UI를 어떻게 변경할까요?",       
  "designer.circle.to.fix.balloon.error.body": "요청을 처리하는 동안 오류가 발생했습니다.",
  "designer.circle.to.fix.balloon.no.change.body": "모델이 아무런 변경사항도 반환하지 않았습니다. 다른 프롬프트로 다시 시도해 보세요.",
  "designer.attach.preview.to.ai.legal.note.title": "미리보기 이미지에 대한 Gemini AI 데이터 처리",
  "designer.attach.preview.to.ai.legal.note.body": "이 작업을 실행하면 선택한 미리보기 이미지가 Google의 Gemini AI 서비스로 전송되어 처리됩니다. \n  Gemini는 Android 스튜디오에 맞게 이미지를 분석하여 최적화합니다.\n  <br/><br/>Gemini 처리 및 데이터 개인정보 보호에 대해 <a href=\"https://developer.android.com/studio/preview/gemini/data-and-privacy/\">자세히 알아보세요</a>.",
  "designer.attach.preview.to.ai.accept.legal.note": "계속",
  "designer.attach.preview.to.ai.cancel.legal.note": "취소",
  "designer.action.transform.ui.with.gemini": "UI 변경",
  "designer.action.transform.ui.with.gemini.agent.title": "UI 변경 중: {0}",   
  "designer.notification.error.title": "오류",
  "designer.action.transform.ui.with.gemini.agent.error": "요청을 준비하는 동안 문제가 발생했습니다. 다시 시도해 주세요.",
  "designer.notification.retry.action.text": "다시 시도",
  "settings.go.to.gemini.inline.completion": "인라인 완성 설정을 조정하려면 <a>Gemini 설정</a>으로 이동",
  "aqi.fix.suggester.title": "수정 제안",
  "aqi.fix.suggester.in.progress.title": "수정 제안 중...",
  "image.to.code.balloon.image.delete.content.description": "이미지 삭제",     
  "image.to.code.balloon.image.selected.content.description": "선택한 이미지", 
  "image.to.code.balloon.image.attach.content.description": "이미지 첨부",     
  "image.to.code.balloon.match.ui.with.design": "디자인 모의 광고와 UI를 일치시킵니다.",
  "image.to.code.balloon.screenshot.to.code": "스크린샷에서 코드를 생성합니다.",
  "image.to.code.balloon.cancel": "취소",
  "image.to.code.balloon.submit": "제출",
  "image.to.code.balloon.image.select.or.drop.markdown": "여기에 이미지를 드래그하거나 붙여넣거나 [파일 선택\\u2026](select_file)",
  "image.to.code.balloon.match.ui.title": "대상 이미지에 UI 맞추기",
  "image.to.code.balloon.match.ui.description": "이미지를 업로드합니다. AI가 시각적 불일치를 분석하고 일치하도록 컴포저블을 다시 작성합니다. 기존 Material Theme 및 프로젝트 리소스에 우선순위를 둡니다.",
  "image.to.code.balloon.screenshot.to.code.title": "이미지에서 코드 생성", 
  "image.to.code.balloon.screenshot.to.code.description": "이미지를 업로드합니다. AI가 기존 프로젝트 구성요소의 재사용을 우선순위로 하여 샘플 데이터로 새 컴포저블을 만들고 가장 적합한 파일 위치를 자동으로 결정합니다.",    
  "studio.bot.agent.tool.deploy.running": "앱 배포 중\\u2026",
  "studio.bot.agent.tool.deploy.completed": "앱 배포됨",
  "studio.bot.agent.tool.liveEdit.running": "실시간 편집 실행 중\\u2026",
  "studio.bot.agent.tool.liveEdit.completed": "실시간 편집 실행됨",
  "studio.bot.agent.tool.listDevices.running": "사용 가능한 장치 나열 중\\u2026",
  "studio.bot.agent.tool.listDevices.completed": "사용 가능한 기기 나열됨",    
  "studio.bot.agent.tool.wait.running": "{0}초 기다리는 중\\u2026",
  "studio.bot.agent.tool.wait.completed": "{0}초 기다림",
  "studio.bot.agent.tool.logcat.running": "Logcat 확인 중\\u2026",
  "studio.bot.agent.tool.logcat.completed": "Logcat 확인됨"
}

with open("missing_translations/missing_keys_korean.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for file_info in data.get("new_files", []):
    if file_info.get("filename") == "StudioGeminiBundle.properties":
        keys_dict = file_info.get("keys", file_info.get("properties", {}))
        keys_dict.update(translations)
        file_info["keys"] = keys_dict
        break

with open("missing_translations/missing_keys_korean.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)
