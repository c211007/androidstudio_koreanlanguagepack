import json
from pathlib import Path

def update_missing_keys():
    file_path = Path("missing_translations/missing_keys_korean.json")

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    ko_dict = {
        "sml.studiobot.onboarding.aida.simplified.step3.context.allowContext.radiobutton.text": "모든 Gemini 기능 사용(권장)",
        "sml.studiobot.onboarding.aida.simplified.step3.context.allowContext.info.markdown": "Gemini의 모든 기능을 사용하려면 프로젝트 컨텍스트 사용을 허용하세요.\\n\\n프로젝트에서 .aiexclude 파일을 사용하여 특정 파일과 디렉터리를 제외할 수도 있습니다. [자세히 알아보기](https://d.android.com/r/studio-ui/gemini/data-and-privacy/aiexclude)",
        "sml.studiobot.onboarding.aida.simplified.step3.context.allowContext.dontAskAgain.text": "모든 프로젝트에 적용",
        "sml.studiobot.onboarding.aida.simplified.step3.context.noContext.radiobutton.text": "프로젝트 컨텍스트 없이 채팅만 사용",
        "sml.studiobot.onboarding.aida.simplified.step3.context.noContext.info.text": "프로젝트 컨텍스트 사용을 허용하지 않고 제한된 Gemini 기능을 사용합니다. Gemini는 사용자의 프롬프트 및 이전 대화 기록만 사용하여 응답합니다. 이 모드에서는 AI 코드 완성과 같은 일부 기능을 사용할 수 없습니다.",        
        "sml.studiobot.onboarding.step1.auth.cta.authorize": "Gemini 승인",      
        "sml.studiobot.onboarding.step1.auth.authorized": "승인됨!",
        "sml.studiobot.onboarding.step1.disclaimer.markdown": "{0}의 Gemini는 현재 [일부 국가](https://d.android.com/r/studio-ui/gemini/availability)에서 사용할 수 있습니다.",
        "sml.studiobot.onboarding.step3.checkbox.markdown": "{0}에서 Gemini를 사용하려면 만 18세 이상이어야 합니다. 귀하의 Gemini 사용은 [Google 서비스 약관](https://policies.google.com/terms) 및 [생성형 AI 추가 서비스 약관](https://policies.google.com/terms/generative-ai)의 적용을 받습니다.",
        "sml.studiobot.onboarding.aistudio.model": "AI Studio 모델 사용",
        "sml.studiobot.onboarding.local.model": "로컬 모델 사용",
        "sml.studiobot.onboarding.remote.model": "원격 모델 사용",
        "sml.studiobot.timeline.loading.text": "기다려 주세요…",
        "sml.studiobot.timeline.experimentalNotice.html": "<html><head><style>%%STYLE%%</style></head><body><div><center>AI는 실수를 할 수 있으므로 다시 한번 확인하세요.</center></div></body></html>",
        "sml.ai.assistance.timeline.experimentalNotice.ai.assistant.markdown": "AI는 실수를 할 수 있으므로 다시 한번 확인하세요.",
        "sml.studiobot.timeline.emptyState.instructions.html": "<html><div>{0}의 Gemini는 고품질 앱을 더 빠르게 구축하도록 돕는 AI 코딩 컴패니언입니다.</div><p>다음은 사용해 볼 수 있는 몇 가지 예시 프롬프트입니다.</p></html>",
        "sml.studiobot.timeline.emptyState.greeting.noUserName": "안녕하세요.",
        "sml.studiobot.timeline.emptyState.greeting.withUserName": "안녕하세요. {0} 님.",
        "sml.studiobot.timeline.emptyState.greeting.secondLine": "어떤 도움이 필요하신가요?",
        "sml.studiobot.timeline.emptyState.agentMode.greeting.secondLine": "오늘 무엇을 빌드하도록 도와드릴까요?",
        "sml.studiobot.timeline.emptyState.tipsCard.title": "시작하기 위한 팁",
        "sml.studiobot.timeline.emptyState.samplePrompts.title": "사용해 볼 프롬프트",    
        "sml.ai.assistance.timeline.emptyState.instructions.html": "<html><div>고품질 앱을 더 빠르게 빌드시킬 수 있도록 돕는 AI 코딩 컴패니언입니다.</div><p>다음은 사용해 볼 수 있는 몇 가지 예시 프롬프트입니다.</p></html>",
        "sml.ai.assistance.timeline.emptyState.greeting.secondLine": "무엇을 도와드릴까요?",
        "sml.ai.assistance.timeline.emptyState.agentMode.greeting.secondLine": "오늘 무엇을 빌드하도록 도와드릴까요?",
        "sml.studiobot.timeline.emptyState.agentMode.bringYourOwnKey.markdown": "**더 높은 비율 제한을 위해 Gemini API 키 사용**\\n\\n결제를 사용 설정하고 유료 등급의 Gemini API를 사용하면 더 높은 비율 제한의 이점을 얻을 수 있으며, 프롬프트와 응답은 Google 제품을 개선하는 데 사용되지 않습니다.\\n\\n[키 추가]({0})   [키 생성](https://aistudio.google.com/app/apikey)",
        "sml.studiobot.timeline.attachAction.title": "이미지 파일 첨부. 최대 허용 크기: {0}MB",
        "sml.studiobot.timeline.attachmentSizeLimit.dialog.title": "최대 파일 크기 초과",
        "sml.studiobot.timeline.attachmentSizeLimit.dialog.description": "첨부 파일은 최대 파일 크기({0}MB)를 초과할 수 없습니다.",
        "sml.studiobot.timeline.imageAttachFailed.dialog.description": "하나 이상의 이미지를 첨부하지 못했습니다.",
        "sml.studiobot.timeline.imageAttachFailed.dialog.title": "이미지 첨부 실패",
        "sml.studiobot.timeline.removeButton.contentDescription": "파일 제거",      
        "sml.studiobot.timeline.enterpriseBanner": "비즈니스용 Gemini",
        "sml.studiobot.tab.chat": "채팅",
        "sml.studiobot.tab.agent": "에이전트",
        "sml.studiobot.timeline.agentModePreviewBanner.learnMore": "[자세히 알아보기](https://developer.android.com/studio/preview/gemini/agent-mode)",
        "sml.studiobot.timeline.agent.tool.expand": "펼치기",
        "sml.studiobot.timeline.agent.tool.collapse": "접기",
        "sml.studiobot.timeline.agent.tool.dependencyUpdate.result.noneToUpgrade": "업그레이드할 종속성이 없습니다.",
        "sml.studiobot.timeline.agent.tool.dependencyUpdate.result.chosenDependencies": "업그레이드할 종속성",
        "sml.studiobot.timeline.agent.tool.dependencyUpdate.selectAll.text": "모두 선택",
        "sml.studiobot.timeline.agent.tool.singleFileEdit.initializing": "초기화 중…",
        "sml.studiobot.timeline.agent.tool.singleFileEdit.restored.edited": "편집됨", 
        "sml.studiobot.timeline.agent.tool.singleFileEdit.restored.noEdit": "편집되지 않음",
        "sml.studiobot.timeline.agent.tool.singleFileEdit.error": "다음 위치에서 파일을 편집하려고 했습니다:\\n{0}\\n하지만 다음과 같은 오류가 발생했습니다: {1}",
        "sml.studiobot.timeline.agent.tool.singleFileEdit.diffComputed.create": "생성",
        "sml.studiobot.timeline.agent.tool.singleFileEdit.diffComputed.edit": "편집", 
        "sml.studiobot.timeline.agent.tool.singleFileEdit.diffComputed.created": "생성됨",
        "sml.studiobot.timeline.agent.tool.singleFileEdit.diffComputed.edited": "편집됨",
        "sml.studiobot.timeline.agent.tool.singleFileEdit.diffComputed.proposeCreate": "생성 제안:"
    }

    filename = "SmlBundle.properties"
    for file_entry in data.get('new_files', []):
        if file_entry['filename'] == filename:
            file_entry['keys'].update(ko_dict)
            break
            
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    update_missing_keys()
