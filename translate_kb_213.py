import json
from pathlib import Path

def update_missing_keys():
    file_path = Path("missing_translations/missing_keys_korean.json")

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    ko_dict = {
        "sml.studiobot.timeline.agent.tool.debuggerState.running": "디버거 상태 읽는 중…",
        "sml.studiobot.timeline.agent.tool.debuggerState.completed": "디버거 상태 읽음",
        "sml.studiobot.timeline.agent.tool.frameVars.running": "프레임 변수 가져오는 중…",
        "sml.studiobot.timeline.agent.tool.frameVars.completed": "프레임 변수 가져옴",
        "sml.studiobot.timeline.agent.tool.stackFrames.running": "스택 프레임 쿼리 중…",
        "sml.studiobot.timeline.agent.tool.stackFrames.completed": "스택 프레임 쿼리됨",
        "sml.studiobot.timeline.agent.tool.getThreads.running": "디버거 스레드 쿼리 중…",
        "sml.studiobot.timeline.agent.tool.getThreads.completed": "디버거 스레드 쿼리됨",
        "sml.studiobot.timeline.agent.tool.pauseDebugger.running": "디버거 일시 중지 중…",
        "sml.studiobot.timeline.agent.tool.pauseDebugger.completed": "디버거 일시 중지됨",
        "sml.studiobot.timeline.agent.tool.removeLineBreakpoint.running": "{0}:{1}의 중단점 제거 중…",
        "sml.studiobot.timeline.agent.tool.removeLineBreakpoint.completed": "{0}:{1}의 중단점 제거됨",
        "sml.studiobot.timeline.agent.tool.resumeDebugger.running": "디버거 다시 시작 중…",
        "sml.studiobot.timeline.agent.tool.resumeDebugger.completed": "디버거 다시 시작됨",
        "sml.studiobot.timeline.agent.tool.generateVector.running": "설명에서 벡터 드로어블 생성 중…",
        "sml.studiobot.timeline.agent.tool.generateVector.completed": "설명에서 벡터 드로어블을 생성했습니다",
        "sml.studiobot.timeline.agent.tool.renderPreview.running": "{0}에 대한 작성 미리보기 렌더링 중…",
        "sml.studiobot.timeline.agent.tool.renderPreview.completed": "{0}에 대한 작성 미리보기를 렌더링했습니다",
        "sml.studiobot.timeline.agent.tool.visualLint.running": "미리보기에서 UI 문제 확인 중…",
        "sml.studiobot.timeline.agent.tool.visualLint.completed": "미리보기에서 UI 문제를 확인했습니다",
        "sml.studiobot.timeline.agent.tool.connectDevice.running": "기기에 연결 중: {0}…",
        "sml.studiobot.timeline.agent.tool.connectDevice.completed": "기기에 연결되었습니다: {0}",
        "sml.studiobot.timeline.agent.tool.generateImage.running": "이미지 생성 중: {0}…",
        "sml.studiobot.timeline.agent.tool.generateImage.completed": "이미지를 생성했습니다: {0}",
        "sml.studiobot.timeline.agent.tool.unregistered.running": "도구 호출 중: {0}…",
        "sml.studiobot.timeline.agent.tool.unregistered.completed": "도구 호출됨: {0}",
        "sml.studiobot.timeline.agent.tool.verb.accept": "수락",
        "sml.studiobot.timeline.agent.tool.verb.auto-accept": "자동 수락",
        "sml.studiobot.timeline.agent.tool.verb.auto-accept.description1": "에이전트가 만든 모든 변경 사항을 자동으로 수락합니다.",
        "sml.studiobot.timeline.agent.tool.verb.auto-accept.description2": "에이전트 옵션에서 이 설정을 전환할 수 있습니다.",
        "sml.studiobot.timeline.agent.tool.verb.auto-accept.new": "파일 편집 시 묻지 않음",
        "sml.studiobot.timeline.agent.tool.verb.auto-accept.new.description1": "에이전트가 만든 변경 사항을 자동으로 적용하고 검토를 위해 스테이징합니다.",
        "sml.studiobot.timeline.agent.tool.verb.auto-accept.new.description2": "에이전트 옵션에서 이 설정을 전환할 수 있습니다.",
        "sml.studiobot.timeline.agent.tool.verb.reject": "거부",
        "sml.studiobot.timeline.agent.tool.readFile.verb": "읽기",
        "sml.studiobot.timeline.agent.tool.readFile.verb.failed": "읽기 실패",   
        "sml.studiobot.timeline.agent.tool.status.deferred": "실행되지 않음",
        "sml.studiobot.timeline.model.name.hint": "{0}에 의해 생성됨",
        "sml.studiobot.settings.title": "AI",
        "sml.studiobot.settings.title.gemini": "Gemini",
        "sml.studiobot.settings.userAccount.label.loggedOut": "Gemini에는 Google 계정 로그인이 필요합니다.",
        "sml.studiobot.settings.userAccount.label.loggedIn": "{0} 님으로 로그인되었으나 권한이 없습니다.",
        "sml.studiobot.settings.userAccount.label.authorized": "{0} 님으로 승인되었습니다.",  
        "sml.studiobot.settings.userAccount.label.cta.logIn": "로그인",
        "sml.studiobot.settings.userAccount.label.cta.authorize": "Gemini 승인", 
        "sml.studiobot.settings.notOnboarded.info.html": "&<icon src=\"AllIcons.General.Information\">\\&nbsp;이 설정에 액세스하기 전에 Gemini 도구 창에서 온보딩을 완료해 주세요.",
        "sml.studiobot.settings.codeSharing.title": "컨텍스트 인식",
        "sml.studiobot.settings.codeSharing.simplified.allowSharing.title.html": "<html><head><style>%%STYLE%%</style></head><body><p>모든 Gemini 기능 사용(권장)</p></body></html>",
        "sml.studiobot.settings.codeSharing.simplified.allowSharing.comment.html": "<p>Gemini의 모든 기능을 사용하려면 프로젝트 컨텍스트 사용을 허용하세요.</p><p></p><p>프로젝트에서 .aiexclude 파일을 사용하여 특정 파일과 디렉터리를 제외할 수 있습니다.<br><a href=\"https://d.android.com/r/studio-ui/gemini/data-and-privacy/aiexclude\">자세히 알아보기</a></p>",
        "sml.studiobot.settings.codeSharing.simplified.allowSharing.dontAskAgain.html": "<html><head><style>%%STYLE%%</style></head><body><p>모든 프로젝트에 적용</p></body></html>"
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
