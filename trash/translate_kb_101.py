import json
from pathlib import Path

def update_missing_keys():
    file_path = Path("missing_translations/missing_keys_korean.json")
    
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    ko_dict = {
        "configure.kotlin": "Kotlin 구성",
        "auto.configure.kotlin": "Kotlin 자동 구성됨",
        "auto.configure.kotlin.notification": "{0}에 Kotlin 플러그인, 라이브러리 및 JVM 타겟을 구성했습니다.",
        "auto.configure.kotlin.notification.no-module": "Kotlin 플러그인, 라이브러리 및 JVM 타겟을 구성했습니다.",
        "auto.configure.kotlin.undo.not-possible.title": "실행 취소할 수 없음",
        "auto.configure.kotlin.undo.not-possible.content": "자동 구성기에 의해 변경된 파일의 수정으로 인해 구성을 자동으로 취소할 수 없습니다.",
        "auto.configure.kotlin.undone": "Kotlin 자동 구성이 취소되었습니다",
        "auto.configure.kotlin.check": "Kotlin 자동 구성 확인 중",
        "auto.configure.kotlin.documentation.open": "문서 열기",
        "auto.configure.kotlin.wait.build.system.sync.finished.title": "{0} 동기화 진행 중",
        "auto.configure.kotlin.wait.build.system.sync.finished": "이 작업을 수행하기 전에 {0} 동기화가 완료될 때까지 기다리세요.",
        "command.name.configure.kotlin.automatically": "Kotlin 자동 구성",
        "command.name.configure.kotlin": "Kotlin 구성",
        "configure.kotlin.manually": "Kotlin 수동 구성",
        "step.configure.kotlin.preparing": "빌드 파일 준비 중",
        "step.configure.kotlin.writing": "빌드 파일 작성 중",
        "view.code.differences.action": "변경 사항 보기",
        "undo.configuration.action": "실행 취소",
        "create.kotlin.java.runtime.library": "Kotlin Java 런타임 라이브러리 생성",
        "java.runtime.library.creation": "Java 런타임 라이브러리 생성",
        "create.kotlin.javascript.library": "Kotlin JavaScript 라이브러리 생성",
        "javascript.library.creation": "JavaScript 라이브러리 생성",
        "configure.kotlin.language.settings": "Kotlin 언어 설정 구성",
        "configure.kotlin.language.settings.title": "Kotlin 언어 설정 구성",
        "configure.kotlin.language.settings.0.module": "{0} 모듈에서 언어 설정 구성",
        "configure.0.in.1.project.br.2": "''{1}'' 프로젝트에서 {0} 구성<br/> {2}",
        "configure.0.module": "''{0}'' 모듈",
        "configure.modules": "모듈",
        "as.kotlin.1.module": "Kotlin({0}) {1,choice,0#모듈|2#모듈}로",
        "lookup.module.0.configuration.progress.text": "모듈 {0}",
        "language.name.java": "Java",
        "language.name.javascript": "JavaScript",
        "updated.javascript.libraries.in.module.0": "{0} 모듈에서 JavaScript 라이브러리 업데이트됨",
        "added.0.requirement.to.module.info.in.1": "{1}의 module-info에 {0} 요구 사항 추가됨",
        "kotlin.not.configured": "Kotlin이 구성되지 않았습니다.",
        "action.text.configure": "구성",
        "title.choose.configurator": "구성 도구 선택",
        "action.text.ignore": "무시",
        "version.message.is.deprecated.since.1.2.0.and.should.be.replaced.with": "{0}은(는) 1.2.0부터 사용 중단(deprecated)되었으며 {1}(으)로 대체되어야 합니다.",
        "added.0.to.library.configuration": "라이브러리 구성에 {0}을(를) 추가했습니다.",
        "0.library.was.added.to.module.1": "{1} 모듈에 {0} 라이브러리가 추가되었습니다.",
        "0.library.was.created": "{0} 라이브러리가 생성되었습니다.",
        "lookup.modules.configurations.progress.text": "모듈 구성 확인 중…",
        "0.library.scope.has.changed.from.1.to.2.for.module.3": "{3} 모듈의 {0} 라이브러리 범위가 {1}에서 {2}(으)로 변경되었습니다.",
        "configure.kotlin.in.modules.progress.text": "모듈에 Kotlin 구성 중…",
        "configure.kotlin.in.module.0.progress.text": "모듈 {0}",
        "this.language.feature.requires.version.0.or.later.of.the.kotlin.runtime.library.would.you.like.to.update.the.runtime.library.in.your.project": "이 언어 기능에는 Kotlin 런타임 라이브러리의 버전 {0} 이상이 필요합니다. 프로젝트의 런타임 라이브러리를 업데이트하시겠습니까?",
        "update.runtime.library": "런타임 라이브러리 업데이트",
        "cant.fetch.available.maven.versions": "사용 가능한 Maven 버전을 가져올 수 없습니다.",
        "cant.fetch.available.maven.versions.title": "사용 가능한 Maven 버전을 가져오는 중 오류 발생"
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
