import json
from pathlib import Path

def update_missing_keys():
    file_path = Path("missing_translations/missing_keys_korean.json")

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    ko_dict = {
        "action.sml.studiobot.updateDependencies.text": "종속성 업데이트",        
        "action.sml.studiobot.document.text": "코드 문서화",
        "action.sml.studiobot.generate.tests.text": "단위 테스트 생성",
        "action.sml.studiobot.generate.tests.description": "Studio Bot Agent를 사용하여 단위 테스트 생성",
        "action.sml.studiobot.testGeneration.text": "단위 테스트 시나리오",
        "action.sml.studiobot.generate.agents.md.text": "AGENTS.md 생성",
        "action.sml.studiobot.add.code.snippet.text": "채팅에 추가",
        "action.sml.studiobot.add.code.snippet.description": "명령 코드를 Studio Bot Agent의 스니펫으로 추가",
        "sml.studiobot.testGeneration.config.dialog.title": "단위 테스트 시나리오 생성",
        "sml.studiobot.testGeneration.notification.title": "단위 테스트 시나리오 생성",
        "sml.studiobot.testGeneration.dialog.className": "클래스 이름:",
        "sml.studiobot.testGeneration.dialog.destinationPackage": "대상 패키지:",
        "sml.studiobot.testGeneration.dialog.generate": "다음의 테스트 시나리오 생성:",
        "sml.studiobot.testGeneration.dialog.showInherited": "상속된 메서드 표시",
        "sml.studiobot.testGeneration.dialog.selectAll": "모두 선택",
        "sml.studiobot.testGeneration.dialog.helpId": "studiobot.testGeneration.dialog",
        "sml.studiobot.testGeneration.dialog.updateExistingClass": "{0}. 기존 클래스를 업데이트하시겠습니까?",
        "sml.studiobot.testGeneration.dialog.failedToCreateTestFolder": "테스트 소스 폴더를 생성하지 못했습니다. 수동으로 생성하는 것을 고려해 보세요.",
        "sml.studiobot.testGeneration.dialog.missingTestSourceDirectory": "현재 모듈에서 테스트 소스 디렉터리를 찾을 수 없습니다. 현재 모듈에 단위 테스트 디렉터리를 생성하시겠습니까?",
        "sml.studiobot.testGeneration.dialog.unsupportedSourceDirectory": "단위 테스트 소스 디렉터리를 선택하거나 생성하세요. 현재 \"단위 테스트 시나리오\" 생성은 Android 계측 테스트를 지원하지 않습니다.",
        "sml.studiobot.testGeneration.dialog.createTestSourceDirectoryButton": "생성",
        "sml.studiobot.testGeneration.dialog.emptyDestinationPackage": "비어 있지 않은 대상 패키지를 입력하세요.",
        "sml.studiobot.testGeneration.dialog.invalidDestinationPackage": "유효한 대상 패키지를 입력하세요. \"{0}\"의 형식이 잘못되었습니다.",
        "sml.studiobot.testGeneration.dialog.noTargetMethod": "대상 메서드를 선택하지 않았습니다. 테스트가 생성되지 않습니다. 대화 상자에서 대상 메서드를 선택하세요.",
        "sml.studiobot.testGeneration.query.progress": "단위 테스트 시나리오 생성 중…",
        "sml.studiobot.onboarding.back.text": "뒤로",
        "sml.studiobot.onboarding.next.text": "다음",
        "sml.studiobot.onboarding.cancel.text": "취소",
        "sml.studiobot.onboarding.finish.text": "마침",
        "sml.studiobot.onboarding.step1.introBlurb.markdown": "{0}의 Gemini는 고품질 앱을 더 빠르게 구축하도록 돕는 AI 코딩 컴패니언입니다. [자세히 알아보기](https://d.android.com/studio/gemini/overview)",
        "sml.studiobot.onboarding.product.variant.selection.secondLine": "제품 계층 확인",
        "sml.studiobot.onboarding.product.variant.selection.heading": "거의 다 왔습니다!",
        "sml.studiobot.onboarding.product.variant.selection.intro.text": "{0}에서 Gemini 사용을 시작하려면 사용할 제품을 선택하세요.",
        "sml.studiobot.onboarding.product.variant.selection.individuals.heading": "개인용 Gemini",
        "sml.studiobot.onboarding.product.variant.selection.individuals.markdown": "코드를 인지하는 채팅 인터페이스, 입력 시 자동 코드 완성, 온디맨드 방식의 전체 함수 또는 파일 생성 및 변환 등 Gemini의 기능을 무료로 사용해 보세요. [자세히 알아보기](https://d.android.com/studio/gemini/overview)",
        "sml.studiobot.onboarding.product.variant.selection.businesses.heading": "비즈니스용 Gemini",
        "sml.studiobot.onboarding.product.variant.selection.businesses.markdown": "개인용 Gemini의 기능이 포함되어 있으며, 감사 로깅, 코드 학습 방지 등 조직의 개인 정보 보호, 보안, 관리 요구사항을 충족하도록 설계되었습니다. [자세히 알아보기](https://d.android.com/r/studio-ui/gemini-for-business)\\n\\n참고: 아직 비즈니스를 위한 Android 스튜디오의 Gemini를 설정하지 않았다면 [여기](https://d.android.com/r/studio-ui/gemini-for-business-setup)에서 자세히 알아보세요.",
        "sml.studiobot.onboarding.aida.simplified.step1.welcome.text": "Gemini 시작하기",
        "sml.studiobot.onboarding.aida.simplified.step1.bullet1.text": "Gemini 채팅을 사용하여 앱 개발 지원받기",
        "sml.studiobot.onboarding.aida.simplified.step1.bullet2.text": "편집기에서 선택한 코드 변환하기",
        "sml.studiobot.onboarding.aida.simplified.step1.bullet3.text": "코드 개선 제안받기",
        "sml.studiobot.onboarding.aida.simplified.step1.bullet4.text": "커밋 메시지 생성",
        "sml.studiobot.onboarding.aida.simplified.step1.signIn.text": "Google에 로그인",
        "sml.studiobot.onboarding.aida.simplified.step2.greeting.secondLine": "개인 정보 보호 관련 안내",
        "sml.studiobot.onboarding.aida.simplified.step2.privacy.title": "Gemini 및 개인 정보 보호",
        "sml.studiobot.onboarding.aida.simplified.step2.privacy.blurb1.markdown": "아래에 표시된 개인 정보 처리방침 및 Google [개인정보처리방침](https://policies.google.com/privacy)은 Gemini가 데이터를 처리하는 방법을 설명합니다.",
        "sml.studiobot.onboarding.aida.simplified.step2.privacy.blurb2.markdown": "{0}에서 Gemini를 사용할 때 Google은 채팅 텍스트, 프롬프트, 관련 코드, 생성된 결과, 관련 기능 사용 정보 및 의견을 수집합니다. Google은 이 데이터를 사용하여 Google Cloud와 같은 Google 엔터프라이즈 제품을 비롯한 Google 제품과 서비스, 기계 학습 기술을 제공, 개선, 개발합니다.\\n\\n품질 관리와 제품 개선을 돕기 위해, 검토 담당자가 귀하의 프롬프트, 관련 코드, 생성된 결과, 관련 기능 사용 정보 및 의견을 읽고 확인, 처리할 수 있습니다. 귀하의 데이터는 Google에서 출처를 식별할 수 없는 상태로 최대 18개월 동안 보관됩니다. Google은 이 기간 동안 삭제 요청을 이행할 수 없습니다.\\n\\n**귀하 또는 타인을 식별할 수 있는 민감한 정보(예: 기밀 정보) 또는 개인 정보를 프롬프트 또는 답변에 포함하지 마십시오.**",
        "sml.studiobot.onboarding.aida.simplified.step3.greeting.secondLine": "나에게 맞는 응답 받기",
        "sml.studiobot.onboarding.aida.simplified.step3.context.title": "프로젝트 컨텍스트 사용",
        "sml.studiobot.onboarding.aida.simplified.step3.context.blurb.markdown": "프로젝트 컨텍스트를 사용하면 코드베이스와 프로젝트에 더 구체적인 코드를 생성하는 데 도움이 됩니다. 시작할 설정을 확인하세요. **설정 > 도구 > {0}**에서 언제든지 변경할 수 있습니다."
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
