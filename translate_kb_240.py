import json

translations = {
  "studio.gemini.settings.title": "편집기",
  "studio.gemini.settings.rename.title": "AI 스마트 이름 바꾸기 제안 사용",  
  "studio.gemini.settings.rename.comment": "AI가 기호의 이름이 변경되는 범위의 이름을 제안하도록 허용합니다. 이 기능을 사용하려면 컨텍스트 인식을 사용 설정해야 합니다.",
  "action.sml.studiobot.rethink.text": "변수 이름 다시 생각하기",
  "action.sml.studiobot.rethink.action.text": "{0} \"{1}\"의 변수 이름 다시 생각하기",
  "studio.gemini.code.action.rethink.notification.title": "Gemini 변수 이름 다시 생각하기",
  "studio.gemini.code.action.rethink.notification.text": "Gemini에 제안할 변수 이름이 없습니다. 이는 이름을 바꿀 변수가 없거나 모델이 변경되었거나 예기치 않은 형식이거나 잘못된 제안이 있는 등 다양한 이유로 발생할 수 있습니다.",  
  "studio.gemini.code.action.rethink.notification.error.text": "Gemini 응답에 문제가 있습니다. 인터넷에 연결되어 있지 않거나, 비율 제한을 초과했거나, 통신 문제가 있으면 이 같은 문제가 발생할 수 있습니다.",
  "studio.gemini.code.action.rethink.notification.error.too.large.text": "코드 컨텍스트가 너무 커서 ML 모델이 처리할 수 없습니다.",
  "studio.gemini.code.action.rethink.dialog.title": "로컬 변수 이름 바꾸기",   
  "studio.gemini.code.action.rethink.dialog.text": "다음 변수의 이름 바꾸기",
  "studio.gemini.code.action.rethink.dialog.entity": "변수",
  "studio.gemini.npw.entry.title": "무엇을 빌드하고 싶으신가요?",
  "studio.gemini.npw.entry.subtitle": "앱을 더 빠르게 구현하세요.",
  "studio.gemini.npw.entry.input.placeholder.text": "앱 디자인을 안내하는 데 도움이 되는 이미지 추가",
  "studio.gemini.npw.entry.attach.image.button.text": "이미지 첨부",
  "studio.gemini.npw.entry.model.key.tip.content": "이미지 생성 및 디자인 기능을 갖춘 가장 빠르고 최신 모델을 사용하려면 유료 Gemini API 키를 추가하세요.",
  "studio.gemini.npw.entry.not.signed.in.title": "시작하는 방법",
  "studio.gemini.npw.entry.not.signed.in.content": "이 기능을 사용하려면 Android 스튜디오용 Gemini에 로그인하거나 유료 또는 타사 모델에 액세스할 수 있는 API 키를 추가해야 합니다.\\n\\n이러한 기능에 액세스하는 방법을 알아보고 AI가 생성한 멋진 Android 앱을 만드는 방법에 대한 팁을 얻으려면 블로그를 읽어보세요.",
  "logcat.studio.bot.action.label": "이 {0} 설명",
  "logcat.studio.bot.action.crash": "비정상 종료",
  "logcat.studio.bot.action.entry": "로그 항목",
  "logcat.studio.bot.action.selection": "선택",
  "logcat.studio.bot.action.query": "이 {0} 설명: {1}",
  "logcat.studio.bot.action.query.basic": "수정: {0}",
  "logcat.studio.bot.link.text": "({0})",
  "layout.inspector.studio.bot.action.query": "다음 스택 추적이 주어지면:\\n\\n{2}\\n\\n\n  1. 읽은 상태 변수를 설명합니다.\\n\n  2. {1} 파일을 읽고 \"{0}\"(이)라는 컴포저블이 재구성된 이유를 설명합니다.",
  "layout.inspector.studio.bot.link.text": "({0})",
  "designer.action.generate.preview": "Compose 미리보기",
  "designer.action.generate.preview.generate.prefix": "생성",
  "designer.action.generate.preview.function.name": "\"{0}\"의 Compose 미리보기",
  "designer.action.generate.preview.error.balloon.text": "Compose 미리보기 생성에 실패했습니다. 다시 시도해 주세요.",
  "designer.action.generate.single.preview": "컴포저블의 미리보기 생성", 
  "designer.action.generate.previews.for.file": "이 파일의 Compose 미리보기 생성",
  "designer.action.generate.previews.for.file.dialog.title": "Compose 미리보기 생성",
  "designer.action.generate.previews.for.file.dialog.empty": "이 파일에는 @Preview로 변환할 수 있는 컴포저블이 없습니다.",
  "designer.action.generate.previews.for.file.dialog.composables.label": "미리보기를 생성할 컴포저블 선택",
  "designer.action.generate.previews.for.file.dialog.ok.button": "생성",    
  "designer.action.match.ui.to.image": "대상 이미지에 UI 맞추기",
  "designer.action.gemini.actions.dropdown": "AI 작업",
  "designer.action.gemini.actions.for.selected.preview": "선택한 미리보기",
  "designer.action.gemini.actions.for.focused.preview": "포커스된 미리보기",  
  "designer.action.fix.visual.issues.agent.title": "UI 확인 문제 수정",       
  "designer.action.fix.visual.issues.agent.fixing.text": "새로운 시각적 린트 문제를 수정하세요:\\n{0}",
  "designer.action.fix.visual.issues.agent.finding.text": "수정할 시각적 린트 문제 찾기",
  "designer.action.fix.render.issues.agent.title": "렌더링 오류 수정",   
  "designer.action.fix.render.agent.text": "렌더링 오류 수정...",        
  "designer.action.fix.with.ai.button": "AI로 수정",
  "designer.action.migrate.layout.to.compose": "Compose로 마이그레이션",
  "designer.action.migrate.layout.to.compose.description": "AI를 사용하여 레이아웃 XML을 Jetpack Compose로 마이그레이션합니다."
}

with open("missing_translations/missing_keys_korean.json", "r", encoding="utf-8") as f:
    data = json.load(f)

found = False
for file_info in data.get("new_files", []):
    if file_info.get("filename") == "StudioGeminiBundle.properties":
        keys_dict = file_info.get("keys", file_info.get("properties", {}))
        keys_dict.update(translations)
        file_info["keys"] = keys_dict
        found = True
        break

if not found:
    data.setdefault("new_files", []).append({
        "filename": "StudioGeminiBundle.properties",
        "keys": translations
    })

with open("missing_translations/missing_keys_korean.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)
