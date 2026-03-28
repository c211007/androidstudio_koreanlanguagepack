import json
from pathlib import Path

def update_missing_keys():
    file_path = Path("missing_translations/missing_keys_korean.json")
    
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    ko_dict = {
        "fetching.available.maven.versions.title": "사용 가능한 Maven 버전 가져오는 중…",
        "automatic.library.version.update.for.maven.and.gradle.projects.is.currently.unsupported.please.update.your.build.scripts.manually": "Maven 및 Gradle 프로젝트에 대한 자동 라이브러리 버전 업데이트는 현재 지원되지 않습니다. 빌드 스크립트를 수동으로 업데이트하세요.",
        "update.kotlin.runtime.library": "Kotlin 런타임 라이브러리 업데이트",
        "configure.kotlin.title": "{0}(으)로 Kotlin 구성",
        "configure.kotlin.cant.load.versions": "Kotlin 버전 목록을 로드할 수 없습니다.",
        "configure.kotlin.root.contains.another.kotlin": "최상위 빌드 스크립트에 Kotlin {0}이(가) 포함되어 있습니다.<br>",
        "configure.kotlin.root.should.contain.same.version": "최상위 및 모듈의 빌드 스크립트에는 동일한 버전이 포함되어야 합니다.<br>",
        "configure.kotlin.currently.there.are.versions": "현재 다음 버전이 있습니다.<br>",
        "configure.kotlin.version.and.modules": "{1}의 {0}<br>",
        "configure.kotlin.version.and.modules.and.more": "및 {0}개 모듈의 추가 항목.<br>",
        "configure.kotlin.choose.another.kotlin.version": "<br>변환 후 다른 Kotlin 버전을 선택하거나 버전을 수동으로 수정할 수 있습니다.<br>",
        "configure.kotlin.choose.the.same.kotlin.version": "<br>{0} Kotlin 버전을 사용하거나 변환 후 버전을 수동으로 수정할 수 있습니다.<br>",
        "kotlin.compiler.and.runtime.version": "Kotlin 컴파일러 및 런타임 버전:",
        "lookup.kotlin.modules.configurations.progress.text": "Kotlin 모듈 구성 확인 중…",
        "choose.module.modules": "{0}, {1} 및 <a href=\"#\">{2,number,#}개의 다른 모듈</a>",
        "choose.module.modules.with.kotlin": "Kotlin 파일이 있는 모듈",
        "single.module": "단일 모듈:",
        "all.modules": "모든 모듈",
        "all.modules.containing.kotlin.files": "Kotlin 파일을 포함하는 모든 모듈:",
        "warning.failed.disable.default.compile.message": "default-compile 또는 default-testCompile 실행을 비활성화하지 못했습니다.",
        "warning.failed.disable.default.compile.action": "이 문제를 해결하는 방법 알아보기",
        "warning.failed.disable.default.compile.link": "https://kotl.in/maven/compile-kotlin-and-java-sources",
        "configurator.kotlin.jvm.targets.unsupported": "{0} 미만의 JVM 타겟이 있으며, Kotlin에서 지원되지 않습니다.<br>",
        "configurator.kotlin.jvm.target.in.modules": "{1}의 {0}<br>",
        "configure.kotlin.jvm.target.in.modules.and.more": "및 {0}개 모듈의 추가 항목.<br>",
        "configurator.kotlin.jvm.target.bump.manually.learn.more": "<br>이러한 모듈에 Kotlin을 추가하는 경우, JVM 타겟을 수동으로 변경해야 합니다.<br>\n  <a href=\"https://kotl.in/jvm-target-compatibility\">Java 및 Kotlin 타겟 호환성</a>에 대해 자세히 알아보세요.",
        "configure.kotlin.changes.title": "Kotlin 구성: 변경 사항",
        "configure.kotlin.original.content": "원본 콘텐츠",
        "configure.kotlin.modified.content": "수정된 콘텐츠",
        "k1.mode.does.not.support.features.0": "K1 모드는 다음 기능을 지원하지 않습니다: {0}",
        "enable.k2.mode": "K2 모드 활성화…",
        "k1.does.not.support.features.ignore": "무시"
    }
    
    filename = "KotlinProjectConfigurationBundle.properties"
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
