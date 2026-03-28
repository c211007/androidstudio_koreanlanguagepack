import json

translations = {
  "sml.studiobot.settings.prompt.templates.scheme.name": "범위",
  "sml.studiobot.settings.prompt.templates.duplicate.template": "복제",    
  "sml.studiobot.settings.prompt.templates.revert.template": "기본 프롬프트 텍스트 복원",
  "sml.studiobot.settings.prompt.templates.saved.prompts": "저장된 프롬프트",     
  "sml.studiobot.settings.prompt.templates.group.rules": "규칙",
  "sml.studiobot.settings.prompt.templates.group.rules.ide": "규칙",
  "sml.studiobot.settings.prompt.templates.group.rules.project": "규칙",       
  "sml.studiobot.settings.prompt.templates.open.setting": "프롬프트 라이브러리 열기",
  "sml.studiobot.settings.prompt.templates.group.rules.zero": "없음",
  "sml.studiobot.settings.prompt.templates.group.rules.sg": "{0}개의 규칙",
  "sml.studiobot.settings.prompt.templates.group.rules.pl": "{0}개의 규칙",        
  "sml.studiobot.prompt.templates.add.action.name": "프롬프트 라이브러리에 추가",    
  "sml.studiobot.prompt.library.context.drawer.tooltip": "설정에 지정된 규칙 포함",
  "sml.studiobot.fix.error.editor.action.text": "AI로 수정",
  "sml.aiplugin.fix.error.editor.action.text": "Gemini로 수정",
  "sml.studiobot.context.provider.current.file": "현재 파일",
  "sml.studiobot.context.provider.recent.files": "최근 파일",
  "sml.studiobot.context.provider.agents.md.files": "AGENTS.md 파일",
  "sml.studiobot.context.provider.agents.md.tooltip": "적용 가능한 AGENTS.md 또는 GEMINI.md 파일 포함",
  "sml.studiobot.settings.previewAttachment.title": "처리할 수 있도록 미리보기 이미지를 Gemini 서비스로 보내기 허용",
  "sml.studiobot.advertiser.description.generateCode": "Gemini에 로그인하여 코드 제안을 얻고, 코드 diff를 비교하고, 코드 편집기에서 직접 변경사항을 수락하세요.",
  "sml.studiobot.advertiser.description.documentFunction": "Gemini에 로그인하여 코드 문서화 제안을 받고, 제안된 변경사항을 검토하고, 코드 편집기에서 직접 변경사항을 수락하세요.",
  "sml.studiobot.advertiser.description.explainCode": "Gemini에 로그인하여 코드가 수행하는 작업에 대한 자세한 설명을 얻고 해당 코드가 앱의 모양이나 동작에 어떻게 기여하는지 알아보세요.",
  "sml.studiobot.advertiser.description.suggestImprovements": "Gemini에 로그인하여 최신 Android 기능을 사용하여 앱을 최적화하는 방법과 코드를 더 잘 정리하는 방법에 대한 제안을 받아보세요.",
  "sml.studiobot.advertiser.description.rethinkVariables": "Gemini에 로그인하여 파일의 변수 또는 메서드 이름에 대한 제안을 받고 마음에 드는 이름을 수락하세요.",
  "sml.studiobot.advertiser.description.generateUnitTestScenarios": "Gemini에 로그인하여 자세한 테스트 이름 및 설명을 포함하여 단위 테스트할 항목에 대한 제안을 받아보세요.",
  "sml.studiobot.advertiser.description.suggestCommitMessage": "버전 제어 시스템을 Android 스튜디오 IDE에 연결한 후 Gemini에 로그인하여 최근 코드 변경사항 및 과거 커밋을 기반으로 한 커밋 메시지 제안을 받아보세요.",
  "sml.studiobot.advertiser.description.buildErrors": "Gemini에 로그인하여 예기치 않은 빌드 오류를 해결하고 빌드 구성을 최적화하는 데 도움을 받으세요.",
  "sml.studiobot.advertiser.description.transformCode": "Gemini에 로그인하여 컨텍스트를 공유하고 변환 기능을 사용하여 코드 제안을 받거나, 코드를 최적화하거나 앱에 코드를 추가하세요.",
  "sml.studiobot.advertiser.description.promptLibrary": "Gemini에 로그인하여 즐겨찾는 프롬프트를 IDE 또는 프로젝트 수준에서 저장하고 관리하세요.",      
  "sml.studiobot.advertiser.description.journeys": "Gemini에 로그인하여 자연어 프롬프트를 사용하여 엔드 투 엔드 테스트를 실행하고 기록하세요.",
  "sml.studiobot.advertiser.agent.mode": "에이전트 모드",
  "sml.studiobot.advertiser.agent.mode.description": "에이전트 모드를 사용하여 수천 줄의 코드를 더 빠르게 수정하고 디버그하여 생산성을 한 단계 높이세요.",  
  "sml.studiobot.advertiser.agent.mode.open": "열기",
  "sml.studiobot.advertiser.agent.learn.more": "자세히 알아보기",
  "sml.studiobot.advertiser.agent.mode.title": "이제 에이전트 모드 사용 가능",      
  "sml.studiobot.advertiser.description.uiTools": "Gemini에 로그인하여 UI를 만들고 변경하고, UI 문제를 해결하고, 미리보기를 생성하세요.",
  "sml.studiobot.agentmode.requires.context.title": "컨텍스트 공유 사용 중지됨", 
  "sml.studiobot.agentmode.requires.context": "에이전트 모드를 사용하려면 컨텍스트 공유를 사용해야 합니다. `설정 > 도구 > {0}`에서 켤 수 있습니다.",
  "sml.studiobot.prompt.library.suggestCommitMessage.groupName": "기본 제공 작업",
  "sml.studiobot.prompt.library.suggestCommitMessage.promptName": "커밋 메시지 생성",
  "sml.studiobot.prompt.library.suggestCommitMessage.description": "프롬프트 템플릿은 프롬프트 실행 중에 동적 값으로 자동 교체되는 변수 사용을 지원합니다. 다음과 같은 변수를 사용할 수 있습니다.",       
  "sml.studiobot.timeline.scrollToBottom.text": "맨 아래로 스크롤",
  "sml.studiobot.timeline.queryBox.dragAndDropHint": "드롭하여 첨부",
  "sml.studiobot.settings.permissions.title": "에이전트 권한",
  "sml.studiobot.settings.sandbox.title": "에이전트 셸 샌드박스",
  "sml.studiobot.settings.sandbox.useSandbox": "셸 명령어에 샌드박스 사용",
  "sml.studiobot.settings.sandbox.rootDirectory": "샌드박스 루트 디렉터리",     
  "sml.studiobot.settings.sandbox.rootDirectory.placeholder": "비워 두면 프로젝트 디렉터리가 사용됩니다.",
  "sml.studiobot.settings.sandbox.rootDirectory.comment": "다른 명령어에서 이 디렉터리를 $SANDBOX_ROOT로 참조할 수 있습니다."
}

with open("missing_translations/missing_keys_korean.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for file_info in data.get("new_files", []):
    if file_info.get("filename") == "SmlBundle.properties":
        file_info["keys"].update(translations)
        break

with open("missing_translations/missing_keys_korean.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)
