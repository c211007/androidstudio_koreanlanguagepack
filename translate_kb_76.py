import json
from pathlib import Path

def update_missing_keys():
    file_path = Path("missing_translations/missing_keys_korean.json")
    
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    ko_dict = {
        "compiler.text.experimental.bytecode.instrumentation.for.kotlin.classes.is.enabled": "Kotlin 클래스에 대한 실험적 바이트코드 계측(Instrumentation)이 활성화되었습니다.",   
        "compiler.text.incremental.caches.are.corrupted.all.kotlin.code.will.be.rebuilt": "증분 캐시가 손상되었습니다. 모든 Kotlin 코드가 다시 빌드됩니다.",       
        "compiler.text.0.is.not.yet.supported.in.idea.internal.build.system.please.use.gradle.to.build.1.enable.delegate.ide.build.run.actions.to.gradle.in.settings": "{0}은(는) IDE 내부 빌드 시스템에서 아직 지원되지 않습니다. Gradle을 사용하여 {1}을(를) 빌드하세요(설정에서 'IDE 빌드/실행 작업을 Gradle에 위임' 활성화).",   
        "compiler.text.0.is.not.yet.supported.in.idea.internal.build.system.please.use.gradle.to.build.them.enable.delegate.ide.build.run.actions.to.gradle.in.settings": "{0}은(는) IDE 내부 빌드 시스템에서 아직 지원되지 않습니다.\\nGradle을 사용하여 빌드하세요(설정에서 'IDE 빌드/실행 작업을 Gradle에 위임' 활성화).",
        "error.message.no.output.directory.found.for.0": "{0}에 대한 출력 디렉토리를 찾을 수 없습니다.",
        "progress.text.compiling.0": "[{0}] 컴파일 중",
        "error.text.cyclically.dependent.modules.are.not.supported.in.multiplatform.projects": "순환 종속 모듈은 멀티플랫폼 프로젝트에서 지원되지 않습니다.",
        "info.text.kotlin.jps.plugin.is.disabled": "Kotlin JPS 플러그인이 비활성화되었습니다.",   
        "error.text.cyclically.dependent.modules.0.should.have.same.compiler": "순환 종속 모듈 {0}은(는) 동일한 컴파일러를 가져야 합니다.",
        "error.text.output.directory.not.specified.for.0": "{0}에 대한 출력 디렉토리가 지정되지 않았습니다."
    }
    
    filename = "KotlinJpsBundle.properties"
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
