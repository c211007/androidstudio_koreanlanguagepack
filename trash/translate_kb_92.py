import json
from pathlib import Path

def update_missing_keys():
    file_path = Path("missing_translations/missing_keys_korean.json")
    
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    ko_dict = {
        "validation.identifier.additional.symbols": ", 및 기호: {0}",
        "validation.file.should.exist": "{0}에 대한 파일이 존재해야 합니다.",
        "version.error.bad.format": "설정 {0}의 버전 형식이 잘못되었습니다.",
        "parse.error.no.value.for.key": "키 {0}의 값을 찾을 수 없습니다.",
        "module.type.jvm": "Kotlin/JVM",
        "module.type.js": "Kotlin/JS",
        "module.type.common": "공통(Common)",
        "module.type.android": "Android",
        "module.type.native": "Kotlin/Native",
        "module.type.wasm": "Kotlin/Wasm",
        "module.name": "모듈 이름",
        "module.configurator.simple.js.browser": "브라우저용 JS",
        "module.configurator.simple.js.node": "Node.js용 JS",
        "module.configurator.command": "Kotlin 구성",
        "module.configurator.android": "Android",
        "module.configurator.android.setting.android.plugin": "Android 플러그인",
        "module.configurator.android.setting.android.plugin.tooltip": "현재 모듈에 사용될 Android Gradle 플러그인",
        "module.configurator.android.setting.android.plugin.application": "com.android.application",
        "module.configurator.android.setting.android.plugin.library": "com.android.library",
        "module.configurator.common": "공통",
        "module.configurator.jvm": "JVM",
        "module.configurator.jvm.setting.target.jvm.version": "대상 JVM 버전",
        "module.configurator.jvm.setting.target.jvm.version.tooltip": "이 모듈을 컴파일한 결과로 생성될 JVM 바이트코드의 버전",
        "module.configurator.jvm.setting.target.jvm.test.framework.tooltip": "단위 테스트에 사용될 프레임워크",
        "module.configurator.mpp": "멀티플랫폼",
        "module.configurator.ios": "iOS",
        "module.configurator.ios.requires.xcode": "Xcode 필요",
        "module.configurator.js.browser": "브라우저",
        "module.configurator.js.node": "Node.js",
        "module.configurator.wasm.simple": "Wasm",
        "module.configurator.js.target.settings.kind": "대상 종류",
        "module.configurator.js.target.settings.kind.library": "JavaScript 라이브러리",
        "module.configurator.js.target.settings.kind.application": "JavaScript 애플리케이션",
        "module.configurator.js.target.settings.kind.hint": "모듈 컴파일 결과",
        "module.configurator.tests.setting.framework": "테스트 프레임워크",
        "module.configurator.tests.setting.framework.junit4": "JUnit 4",
        "module.configurator.tests.setting.framework.junit5": "JUnit 5",
        "module.configurator.tests.setting.framework.test.ng": "TestNG",
        "module.configurator.tests.setting.framework.none": "없음",
        "module.configurator.tests.setting.framework.kotlin.test": "Kotlin 테스트",
        "module.configurator.tests.setting.kotlin.test.title": "kotlin.test 사용",
        "module.configurator.tests.setting.kotlin.test.desc": "<html>단위 테스트를 위한 <a href=\"https://kotlinlang.org/api/latest/kotlin.test/\">kotlin.test</a> 주석 및 어설션 함수를 추가합니다.</html>",
        "module.configurator.native.for.current.system": "사용자 시스템",
        "project.template.empty.jvm.console.title": "콘솔 애플리케이션",
        "project.template.empty.jvm.console.description": "Kotlin/JVM이 포함된 간단한 'Hello World!' 애플리케이션",
        "project.template.mpp.lib.title": "라이브러리",
        "project.template.mpp.lib.description": "다양한 플랫폼에서 공유할 수 있는 공통 코드가 포함된 멀티플랫폼 라이브러리",
        "project.template.full.stack.title": "풀스택 웹 애플리케이션",
        "project.template.full.stack.description": "Kotlin/JS 웹 프런트엔드, Kotlin/JVM 서버 백엔드 및 플랫폼 간에 공유되는 공통 코드가 포함된 웹 애플리케이션",
        "project.template.native.console.title": "네이티브 애플리케이션"
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
