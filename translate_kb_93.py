import json
from pathlib import Path

def update_missing_keys():
    file_path = Path("missing_translations/missing_keys_korean.json")
    
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    ko_dict = {
        "project.template.native.console.description": "Kotlin/Native를 사용하는 특정 플랫폼 또는 여러 플랫폼용 네이티브 애플리케이션",
        "project.template.wasm.browser.title": "Kotlin/Wasm가 있는 브라우저 애플리케이션",
        "project.template.wasm.browser.description": "Kotlin/Wasm가 있는 간단한 브라우저 애플리케이션",
        "project.template.browser.title": "브라우저 애플리케이션",
        "project.template.browser.description": "Kotlin/JS가 있는 웹 프런트엔드 애플리케이션",
        "project.template.react.title": "React 애플리케이션",
        "project.template.react.description": "React UI 프레임워크와 함께 Kotlin/JS를 사용하는 웹 프런트엔드 애플리케이션",
        "project.template.nodejs.title": "Node.JS 애플리케이션",
        "project.template.nodejs.description": "Kotlin/JS가 있는 Node.js 런타임용 애플리케이션",
        "project.template.mpp.mobile.title": "모바일 애플리케이션",
        "project.template.mpp.mobile.description": "플랫폼 간에 공유되는 공통 코드가 있는 iOS 및 Android용 모바일 애플리케이션",
        "module.template.console.jvm.title": "콘솔 애플리케이션",
        "module.template.console.jvm.description": "콘솔에서 작동하는 간단한 \"Hello World!\" Kotlin/JVM 애플리케이션",
        "module.template.mpp.mobile.title": "모바일 애플리케이션",
        "module.template.mpp.mobile.description": "플랫폼 간 공통 코드 공유를 지원하는 Kotlin 멀티플랫폼 모바일이 있는 iOS 및 Android용 모바일 애플리케이션입니다.",
        "module.template.ktor.server.title": "웹 서버",
        "module.template.ktor.server.description": "백엔드 웹 서버",
        "module.template.native.console.title": "네이티브 애플리케이션",
        "module.template.native.console.description": "현재 운영 체제용 간단한 Kotlin/Native 애플리케이션",
        "module.template.js.simple.title": "브라우저 애플리케이션",
        "module.template.js.simple.description": "브라우저를 대상으로 하는 빈 애플리케이션",
        "module.template.js.simple.run.configuration.dev": "연속 모드의 BrowserDevelopmentRun",
        "module.template.js.simple.run.configuration.prod": "연속 모드의 BrowserProductionRun",
        "module.template.simple.use.kotlinx.html": "kotlinx.html 사용",
        "module.template.simple.use.kotlinx.html.description": "HTML 요소를 생성하고 DOM 트리를 구축하기 위한 타입 세이프(Type-safe) Kotlin DSL",
        "module.template.js.react.title": "React 애플리케이션",
        "module.template.js.react.description": "브라우저를 대상으로 하는 React 애플리케이션",
        "module.template.react.use.react.router.dom": "react-router-dom 사용",
        "module.template.react.use.react.router.dom.description": "URL과 UI를 동기화된 상태로 유지하기 위한 탐색 컴포넌트 추가",
        "module.template.react.use.react.redux": "react-redux 사용",
        "module.template.react.use.react.redux.description": "Redux로 구동되는 상태 컨테이너 추가",
        "module.template.simple.nodejs.title": "Node.JS 애플리케이션",
        "module.template.simple.nodejs.description": "Node.js를 대상으로 하는 빈 애플리케이션",
        "module.template.simple.nodejs.use.kotlinx.nodejs": "실험적 Node.js API(kotlinx-nodejs) 사용",
        "module.template.simple.nodejs.use.kotlinx.nodejs.description": "Node.js 관련 기능에 대한 액세스 허용",
        "module.template.wasm.browser.title": "Kotlin/Wasm가 있는 브라우저 애플리케이션",
        "module.template.wasm.browser.description": "Kotlin/Wasm가 있는 간단한 브라우저 애플리케이션",
        "error.text.project.importing.error.kotlin.version.0.reason.1": "프로젝트 가져오기 오류\\nKotlin 버전: {0}\\n원인: {1}",
        "error.text.module.0.should.contain.at.least.one.ios.target": "{0} 모듈에는 하나 이상의 iOS 타겟이 포함되어야 합니다.",
        "error.text.project.templates.is.not.supported.in.yaml.for.now": "지금은 yaml에서 프로젝트 템플릿이 지원되지 않습니다.",
        "configuration.name.run": "실행",
        "error.text.for.setting.0.one.of.1.was.expected.but.2.was.found": "`{0}` 설정의 경우 [{1}] 중 하나가 예상되었으나 `{2}`이(가) 발견되었습니다.",
        "error.text.expected.0.for.1.but.2.was.found": "`{1}`에 대해 {0}이(가) 예상되었으나 {2}이(가) 발견되었습니다.",
        "gradle.settings.wizard.unsupported.multi.module.message": "다중 모듈 프로젝트는 Gradle {0}에서 지원되지 않습니다.",
        "gradle.project.settings.distribution.version.kotlin.unsupported": "Kotlin {0}은(는) Gradle {1}에서 지원되지 않습니다.",
        "gradle.settings.wizard.unsupported.kotlin.message": "\n  Kotlin {0}은(는) Gradle {1}을(를) 지원하지 않습니다.\\n\\n\n  Kotlin {0} 및 Gradle {1}(으)로 계속 진행하시겠습니까?",
        "multiplatform.web.wizard.comment": "Kotlin 멀티플랫폼 프로젝트를 생성하려면 <a href=\"{0}\">여기를 클릭하세요</a>.",
        "multiplatform.web.wizard.link": "https://kmp.jetbrains.com/",
        "onboarding.show.intention.tip.comment.1": "강조 표시된 텍스트에 캐럿을 놓고 {0}을(를) 눌러 방법을 확인하세요.",
        "onboarding.show.intention.tip.comment.2": "{0}이(가) 이 문제를 수정하도록 제안합니다."
    }
    
    filename = "KotlinNewProjectWizardBundle.properties"
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
        
    print(f"Updated {filename}")

if __name__ == "__main__":
    update_missing_keys()
