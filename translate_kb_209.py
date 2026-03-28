import json
from pathlib import Path

def update_missing_keys():
    file_path = Path("missing_translations/missing_keys_korean.json")

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    ko_dict = {
        "sml.aiplugin.product.name.default": "Gemini",
        "sml.aiplugin.product.name.ai.assistance": "AI 지원",
        "sml.aiplugin.toolwindow.name.default": "채팅",
        "sml.aiplugin.toolwindow.name.gemini": "Gemini",
        "sml.studiobot.aiexclude.blockingFiles.open": "차단 중인 .aiexclude 파일 열기",
        "sml.studiobot.aiexclude.blockingFiles.title": "{0}을(를) 차단 중인 .aiexclude 파일",
        "sml.studiobot.aiexclude.blockingFiles.sibling": "형제",
        "sml.studiobot.aiexclude.blockingFiles.parentDirectory": "상위 디렉터리",  
        "sml.studiobot.aiexclude.blockingFiles.directoriesAbove": "{0} 디렉터리 위",
        "sml.studiobot.ask.errorMessageQuery": "오류 메시지 \"{0}\"의 의미는 무엇인가요?",
        "sml.studiobot.ask.confirmation.title": "코드 전송 확인",
        "sml.studiobot.ask.confirmation.message": "선택한 텍스트를 분석을 위해 Gemini 서버로 전송하시겠습니까?",
        "sml.studiobot.ask.confirmation.dontAskAgain": "새 채팅을 시작할 때 항상 변경 사항 유지",
        "sml.studiobot.ask.gemini.text": "Gemini에 질문",
        "sml.studiobot.ask.gemini.description": "이에 대해 Gemini에 질문",
        "sml.studiobot.ask.generic.text": "AI로 설명",
        "sml.studiobot.ask.build.output.text": "AI로 수정",
        "sml.studiobot.ask.generic.description": "AI로 설명",
        "sml.studiobot.ask.logcat.output.text": "AI로 수정",
        "sml.studiobot.ask.transform.dialog.title": "변환",
        "sml.studiobot.quickedit.emptyText": "AI를 사용하여 선택한 코드와 관련된 제한된 범위의 작업을 수행하세요.",
        "sml.studiobot.quickedit.dialog.title": "빠른 편집",
        "sml.studiobot.quickedit.permissions.rejected": "요청에 추가 권한이 필요합니다.",
        "sml.studiobot.quickedit.transferToChat": "채팅으로 전송",
        "sml.studiobot.quickedit.changesInDifferentFile": "변경 사항이 다른 파일에 적용되었습니다!",
        "sml.studiobot.ask.transform.dialog.message": "선택한 코드를 어떻게 변환할지 Gemini에게 알려주세요.",
        "sml.studiobot.ask.generate.dialog.title": "생성",
        "sml.studiobot.ask.generate.dialog.message": "Gemini가 생성하기를 원하는 코드를 설명하세요.",
        "sml.studiobot.ask.transform.refine.dialog.message": "이 제안을 어떻게 다듬을지 Gemini에게 알려주세요.",
        "sml.studiobot.ask.transform.dialog.disclaimer": "Gemini는 부정확한 코드를 생성할 수 있습니다. 코드를 신중하게 사용하세요. <a href=\"https://g.co/legal/generative-code\">자세히 알아보기</a>",
        "sml.studiobot.ask.transform.progress.message": "쿼리 전송 중…",       
        "sml.studiobot.ask.transform.diff.tab.title": "Gemini 비교: {0}",
        "sml.studiobot.document.parameterized_text": "{0} \"{1}\" 문서화",
        "sml.studiobot.transform.citations.blocked.user.visible": "Gemini가 사용 가능한 결과를 반환하지 않았습니다.",
        "sml.studiobot.transform.error": "Gemini가 유용한 결과를 제공하지 못했습니다.",
        "sml.studiobot.transform.empty": "Gemini가 변경 사항을 제안하지 않았습니다.",       
        "sml.studiobot.transform.difftree.header": "{0,choice,1#Gemini 변경 사항(파일 1개)|1<Gemini 변경 사항(파일 {0}개)}",
        "sml.studiobot.transform.diff.file.position": "{1}개 파일 중 {0}번째",
        "sml.studiobot.transform.diff.hide.filetree": "파일 트리 보기 숨기기",
        "sml.studiobot.transform.diff.show.filetree": "파일 트리 보기 표시",
        "sml.studiobot.more.details": "자세한 내용…",
        "sml.studiobot.stack.trace": "스택 트레이스",
        "group.aiplugin.gemini.editor.group.text.gemini": "Gemini",
        "group.aiplugin.gemini.editor.group.text": "AI",
        "action.sml.studiobot.custom.transform.intention.text": "Gemini로 변환…",
        "action.sml.studiobot.custom.transform.text": "선택한 코드 변환…",
        "action.sml.studiobot.unsupported.text": "지원되지 않는 버전: 지금 업데이트",   
        "action.sml.studiobot.generate.code.text": "코드 생성…",
        "action.sml.studiobot.explain.text": "코드 설명",
        "action.sml.studiobot.improve.text": "개선 사항 제안"
    }

    filename = "SmlBundle.properties"
    found = False
    for file_entry in data.get('new_files', []):
        if file_entry['filename'] == filename:
            file_entry['keys'].update(ko_dict)
            found = True
            break
            
    if not found:
        data.setdefault('new_files', []).append({"filename": filename, "keys": ko_dict})

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    update_missing_keys()
