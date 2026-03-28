import json
from pathlib import Path

def update_missing_keys():
    file_path = Path("missing_translations/missing_keys_korean.json")

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    ko_dict = {
        "sml.studiobot.settings.codeSharing.simplified.allowSharing.dontAskAgain.useForThisProject.html": "<html><head><style>%%STYLE%%</style></head><body><p>이 프로젝트의 컨텍스트 사용({0})</p></body>",
        "sml.studiobot.settings.codeSharing.simplified.neverShare.title.html": "<html><head><style>%%STYLE%%</style></head><body><p>프로젝트 컨텍스트 없이 채팅만 사용</p></body></html>",
        "sml.studiobot.settings.codeSharing.simplified.neverShare.comment.html": "<p>프로젝트 컨텍스트 사용을 허용하지 않고 제한된 Gemini 기능을 사용합니다. Gemini는 사용자의 프롬프트 및 이전 대화 기록만 사용하여 응답합니다. 이 모드에서는 AI 코드 완성과 같은 일부 기능을 사용할 수 없습니다.</p>",        
        "sml.studiobot.settings.codeCompletion.group": "완성",
        "sml.studiobot.settings.codeCompletion.title": "AI 기반 인라인 코드 완성 사용 설정",
        "sml.studiobot.settings.codeCompletion.comment": "Gemini는 입력 시 인텔리전트한 코드 완성을 제안하기 위해 삽입 커서 주변의 코드를 분석합니다. 이 기능을 사용하려면 컨텍스트 인식을 사용 설정해야 합니다.",
        "sml.studiobot.settings.chat.bringYourOwnKey.comment": "<a href=\"https://aistudio.google.com/apikey\">Gemini API 키 받기</a>",
        "sml.studiobot.settings.codeSharing.notification.title": "이 프로젝트의 컨텍스트를 사용하시겠습니까?",
        "sml.studiobot.settings.codeSharing.notification.text": "Gemini는 프로젝트의 컨텍스트를 사용하여 더 나은 제안 및 응답을 제공할 수 있습니다.",
        "sml.studiobot.settings.codeSharing.notification.yes": "예",
        "sml.studiobot.settings.codeSharing.notification.no": "아니요",
        "sml.studiobot.settings.codeSharing.notification.configure": "Gemini 설정 열기…",
        "sml.studiobot.settings.prompt.library.title": "프롬프트 라이브러리",
        "sml.studiobot.single.login.enforcer.notification.singular.text": "단 하나의 계정만 Gemini에 로그인할 수 있습니다. Gemini({0})를 사용하는 다른 모든 Google 계정은 현재 로그아웃 되었습니다.",
        "sml.studiobot.timeline.emptyState.sampleQuery1.html": "<html>구성 가능한 함수가 무엇인가요?</html>",
        "sml.studiobot.timeline.emptyState.sampleQuery1.plainText": "구성 가능한 함수가 무엇인가요?",
        "sml.studiobot.timeline.emptyState.sampleQuery2.html": "<html>Compose에서 RecyclerView와 동등한 항목은 무엇인가요?</html>",
        "sml.studiobot.timeline.emptyState.sampleQuery2.plainText": "Compose에서 RecyclerView와 동등한 항목은 무엇인가요?",
        "sml.studiobot.timeline.emptyState.sampleQuery3.html": "<html>내 앱을 디버그하려면 어떻게 하나요?</html>",
        "sml.studiobot.timeline.emptyState.sampleQuery3.plainText": "내 앱을 디버그하려면 어떻게 하나요?",
        "sml.studiobot.timeline.emptyState.sampleQuery4.html": "<html>minSdkVersion은 어떻게 선택하나요?</html>",
        "sml.studiobot.timeline.emptyState.sampleQuery4.plainText": "minSdkVersion은 어떻게 선택하나요?",
        "sml.studiobot.timeline.emptyState.sampleQuery5.html": "<html>Android 앱을 테스트하려면 어떻게 하나요?</html>",
        "sml.studiobot.timeline.emptyState.sampleQuery5.plainText": "Android 앱을 테스트하려면 어떻게 하나요?",
        "sml.studiobot.timeline.emptyState.sampleQuery6.html": "<html>Kotlin 코드를 문서화하기 위한 KDoc은 어떻게 생겼는지 상기시켜 주시겠어요?</html>",
        "sml.studiobot.timeline.emptyState.sampleQuery6.plainText": "Kotlin 코드를 문서화하기 위한 KDoc은 어떻게 생겼는지 상기시켜 주시겠어요?",
        "sml.studiobot.timeline.emptyState.sampleQuery7.html": "<html>WorkManager의 최신 버전은 무엇인가요?</html>",
        "sml.studiobot.timeline.emptyState.sampleQuery7.plainText": "WorkManager의 최신 버전은 무엇인가요?",
        "sml.studiobot.timeline.emptyState.sampleQuery8.html": "<html>Kotlin에서 Person 데이터 클래스 만들기</html>",
        "sml.studiobot.timeline.emptyState.sampleQuery8.plainText": "Kotlin에서 Person 데이터 클래스 만들기",
        "sml.studiobot.timeline.emptyState.sampleQuery9.html": "<html>권한 요청 결과를 어떻게 처리하나요?</html>",
        "sml.studiobot.timeline.emptyState.sampleQuery9.plainText": "권한 요청 결과를 어떻게 처리하나요?",
        "sml.studiobot.timeline.emptyState.sampleQuery10.html": "<html>Android 스튜디오에서 어두운 모드로 변경</html>",
        "sml.studiobot.timeline.emptyState.sampleQuery10.plainText": "Android 스튜디오에서 어두운 모드로 변경",
        "sml.studiobot.timeline.emptyState.sampleQuery11.html": "<html>Kotlin에서 맵 만들기</html>",
        "sml.studiobot.timeline.emptyState.sampleQuery11.plainText": "Kotlin에서 맵 만들기",
        "sml.studiobot.timeline.emptyState.agentMode.sampleQuery1.plainText": "편집기의 경고 및 오류 수정",
        "sml.studiobot.timeline.emptyState.agentMode.sampleQuery2.plainText": "@libs.version.toml의 Kotlin을 최신 버전으로 업데이트",
        "sml.studiobot.timeline.emptyState.agentMode.sampleQuery3.plainText": "내 프로젝트의 빌드 오류 찾기 및 해결",
        "sml.studiobot.timeline.emptyState.agentMode.sampleQuery4.plainText": "내 테마의 색상 구성표를 더 따뜻하게 만들기",
        "sml.studiobot.timeline.emptyState.agentMode.sampleQuery5.plainText": "현재 파일에 문서 추가",
        "sml.studiobot.timeline.emptyState.agentMode.sampleQuery6.plainText": "이 클래스에서 하드코딩된 모든 문자열을 추출하여 strings.xml로 이동",
        "sml.studiobot.banner.error.dismiss.action.title": "닫기",
        "sml.studiobot.timeline.changesDrawer.header": "검토할 파일({0})",       
        "sml.studiobot.timeline.changesDrawer.keepChange": "변경 사항 유지",
        "sml.studiobot.timeline.changesDrawer.keepAll": "모두 유지",
        "sml.studiobot.timeline.changesDrawer.revertChange": "변경 사항 취소",
        "sml.studiobot.timeline.changesDrawer.revertAll": "모두 취소",
        "sml.studiobot.timeline.changesDrawer.inEditor.keep": "유지",
        "sml.studiobot.timeline.changesDrawer.inEditor.keep.description": "이 파일의 모든 변경 사항 유지"
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
