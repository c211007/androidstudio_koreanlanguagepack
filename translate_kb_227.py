import json

translations = {
  "aiplugin.release.notes.notification.text": "출시 노트 보기",
  "aiplugin.release.notes.notification.chat.message": "**{0}이(가) 버전 {1}(으)로 업데이트되었습니다.**\\n\\n새로운 기능 및 제공되는 기능에 대해 자세히 알아보려면 [출시 노트]({2})를 참조하세요.",
  "aiplugin.announcement.gemini3.title": "Gemini 3가 출시되었습니다.",
  "aiplugin.announcement.gemini3.markdown": "Code Assist에서 Gemini 3 사용을 시작하는 방법에 대해 자세히 알아보려면 문서를 확인하세요.\\n\\n[문서 보기](https://developers.google.com/gemini-code-assist/docs/gemini-3)",
  "aiplugin.actions.createNewFile.text": "파일 만들기",
  "aiplugin.actions.undo.createNewFile.text": "파일 만들기: {0}",
  "aiplugin.actions.acceptAllChanges.text": "모든 변경사항 수락",
  "aiplugin.actions.rollbackAllChanges.text": "모든 변경사항 롤백",
  "aiplugin.actions.addToContext.text": "{0}채팅 컨텍스트에 {1} 추가",
  "aiplugin.actions.addToContext.file": "채팅 컨텍스트에 현재 파일 추가",     
  "aiplugin.actions.addToContext.file.selection": "채팅 컨텍스트에 선택한 텍스트 추가",
  "aiplugin.gemini.statusbar.group.text.gemini": "Gemini",
  "aiplugin.outlines.action.text": "현재 파일 개요 표시",
  "aiplugin.outlines.refresh.action.text": "현재 파일의 개요 새로고침",  
  "aiplugin.outlines.notification.title": "Gemini Code Assist",
  "aiplugin.outlines.notification.message": "{0}의 개요가 제공됩니다.",     
  "aiplugin.outlines.notification.action.show": "개요 보기",
  "aiplugin.outlines.notification.action.dont.show.again": "다시 표시 안함",
  "aiplugin.outlines.progress.message": "개요 생성 중\\u2026",
  "aiplugin.outlines.status.bar.progress.message": "{0}의 개요 생성 중",
  "aiplugin.outlines.status.bar.ready.message": "개요 준비 완료",
  "aiplugin.outlines.not.available.message": "제공되는 개요가 없습니다.",
  "aiplugin.outlines.error.message": "오류가 발생하여 개요를 사용할 수 없습니다. 개요를 다시 생성해 보세요.",
  "aiplugin.outlines.error.retry.message": "다시 시도",
  "aiplugin.outlines.stopped.message": "개요 생성이 중지되었습니다.",  
  "aiplugin.outlines.tab": "개요",
  "aiplugin.outlines.gotItTour.header": "개요를 통해 이 코드베이스 알아보기",     
  "aiplugin.outlines.gotItTour.message": "개요를 통해 자연어를 사용하여 더 높은 추상화 수준에서 코드에 대해 생각해 볼 수 있습니다.",
  "aiplugin.outlines.gotItTour.tryIt.button": "사용해 보기",
  "aiplugin.outlines.tip.card.message": "개요는 파일의 요약 및 구조를 제공하여 자연어를 사용하여 더 높은 추상화 수준에서 코드에 대해 생각할 수 있도록 도와줍니다.",
  "aiplugin.outlines.tip.card.file.excluded.message": "Gemini Code Assist의 제외 파일에 의해 차단되었으므로 이 파일의 개요를 사용할 수 없습니다.",
  "aiplugin.outlines.tip.card.file.not.supported.message": "지원되지 않는 파일 형식이므로 개요를 생성할 수 없습니다.",
  "aiplugin.outlines.empty.state.title": "이 파일의 개요 생성",      
  "aiplugin.outlines.empty.state.no.file.title": "파일을 선택하여 개요 가져오기",
  "aiplugin.outlines.empty.state.message": "개요는 파일의 요약 및 구조를 제공하여 자연어를 사용하여 더 높은 추상화 수준에서 코드에 대해 생각할 수 있도록 도와줍니다.",
  "aiplugin.outlines.empty.state.link": "개요 생성",
  "aiplugin.outlines.outdated.title": "이 개요를 새로고침해 주세요.",
  "aiplugin.outlines.outdated.message": "{0} 파일이 수정되어 이 개요는 더 이상 유효하지 않습니다. 최신 개요를 가져오려면 다시 생성하세요.",
  "aiplugin.outlines.outdated.refresh.button": "개요 새로고침",
  "aiplugin.outlines.icon.refresh.tooltip": "새로고침",
  "aiplugin.outlines.icon.cancel.tooltip": "취소",
  "aiplugin.outlines.icon.feedback.downvote": "이 개요에 싫어요 표시",
  "aiplugin.outlines.icon.feedback.upvote": "이 개요에 좋아요 표시",
  "aiplugin.outlines.icon.hide.tooltip": "모든 파일의 개요 숨기기 ({0})",    
  "aiplugin.outlines.icon.show.tooltip": "모든 파일의 개요 표시 ({0})",    
  "aiplugin.outlines.file.icon.hide.tooltip": "이 파일의 개요 숨기기",     
  "aiplugin.outlines.file.icon.show.tooltip": "이 파일의 개요 표시",     
  "aiplugin.outlines.feedback.moreFeedback.description": "기능 개선에 도움이 되도록 이 개요가 도움이 되지 않은 이유를 알려주세요.",
  "aiplugin.outlines.feedback.moreFeedback": "의견 제공",
  "aiplugin.outlines.banner.message": "Gemini Code Assist에서 이 파일의 개요를 자연어로 생성할 수 있습니다."
}

with open("missing_translations/missing_keys_korean.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for file_info in data.get("new_files", []):
    if file_info.get("filename") == "SmlIjBundle.properties":
        keys_dict = file_info.get("keys", file_info.get("properties", {}))
        keys_dict.update(translations)
        file_info["keys"] = keys_dict
        break

with open("missing_translations/missing_keys_korean.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)
