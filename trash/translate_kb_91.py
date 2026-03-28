import json
from pathlib import Path

def update_missing_keys():
    file_path = Path("missing_translations/missing_keys_korean.json")
    
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    ko_dict = {
        "buildsystem.type.gradle.groovy": "Gradle Groovy",
        "buildsystem.type.gradle.kotlin": "Gradle Kotlin",
        "buildsystem.type.intellij": "IntelliJ",
        "buildsystem.type.intellij.full": "IntelliJ 빌드 시스템",
        "buildsystem.type.maven": "Maven",
        "error.template.not.found": "ID가 {0}인 템플릿을 찾을 수 없습니다.",
        "error.required.settings.are.not.present.0": "다음 필수 설정이 구성되지 않았습니다:\\n{0}",
        "error.configurator.not.found": "{0} 모듈 유형을 찾을 수 없습니다.",
        "error.invalid.module.dependency": "모듈 {0}에서 {1}${2}(으)로의 모듈 종속성이 잘못되었습니다.",
        "module.configuration.group.android.native": "Android Native",
        "module.configuration.group.ios": "iOS",
        "module.configuration.group.linux": "Linux",
        "module.configuration.group.macos": "macOS",
        "module.configuration.group.windows.mingw": "Windows (MinGW)",
        "module.type": "모듈 유형",
        "module.kind.android.module": "Android 모듈",
        "module.kind.ios.module": "iOS 모듈",
        "module.kind.js.browser.module": "JS 브라우저 모듈",
        "module.kind.js.node.module": "JS Node 모듈",
        "module.kind.module": "모듈",
        "module.kind.mpp.module": "MPP 모듈",
        "module.kind.target": "타겟",
        "plugin.buildsystem.setting.type": "빌드 시스템",
        "plugin.buildsystem.setting.type.error.wrong.project.kind": "{0} 프로젝트는 {1}을(를) 사용하여 생성할 수 없습니다.",
        "plugin.kotlin.downloading.kotlin.versions": "Kotlin 버전 목록 다운로드 중",
        "plugin.kotlin.setting.modules": "모듈",
        "plugin.kotlin.setting.modules.error.duplicated.modules": "이름이 {1}인 모듈이 {0}개 있습니다.",
        "plugin.kotlin.setting.modules.error.duplicated.targets": "이름이 {1}인 타겟이 {0}개 있습니다.",
        "plugin.kotlin.setting.project.kind": "프로젝트 종류",
        "project.kind.android": "Android",
        "project.kind.kotlin.js": "Kotlin/JS",
        "project.kind.multiplatform": "멀티플랫폼",
        "project.kind.singleplatform": "JVM",
        "project.kind.kmm": "Kotlin Multiplatform Mobile",
        "project": "프로젝트",
        "plugin.structure.setting.location": "위치",
        "plugin.structure.setting.location.error.is.not.empty": "디렉터리가 비어 있지 않습니다.",
        "plugin.structure.setting.name": "이름",
        "plugin.structure.setting.group.id": "그룹 ID",
        "plugin.structure.setting.group.id.tooltip": "조직의 고유 식별자입니다. IntelliJ 빌드 시스템에는 적용되지 않습니다.",
        "plugin.structure.setting.artifact.id": "아티팩트 ID",
        "plugin.structure.setting.artifact.id.tooltip": "이 프로젝트의 기본 아티팩트의 고유 이름입니다. IntelliJ 빌드 시스템에는 적용되지 않습니다.",
        "plugin.structure.setting.version": "버전",
        "plugin.structure.setting.version.tooltip": "프로젝트에서 생성된 기본 아티팩트의 버전입니다. IntelliJ 빌드 시스템에는 적용되지 않습니다.",
        "plugin.templates.setting.template": "프로젝트 템플릿",
        "plugin.templates.setting.template.tooltip": "초기 프로젝트 구조를 정의합니다. 목적에 따라 다음 템플릿 중 하나를 선택하세요:",
        "plugin.android.setting.sdk": "Android SDK",
        "plugin.android.setting.sdk.tooltip": "현재 애플리케이션에 사용될 Android SDK",
        "validation.should.not.be.blank": "{0}을(를) 지정하세요.",
        "validation.identifier": "{0}은(는) 문자, 숫자{1}(으)로만 구성되어야 합니다."
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
