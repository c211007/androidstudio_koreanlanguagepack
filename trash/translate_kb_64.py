import json
from pathlib import Path

def update_missing_keys():
    file_path = Path("missing_translations/missing_keys_korean.json")
    
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    ko_dict = {
        "action.LoadKtGradleConfiguration.text": "스크립트 구성 로드",        
        "action.LoadKtGradleConfiguration.description": "Gradle Kotlin DSL 스크립트 구성이 변경되었습니다. 외부 Gradle 프로젝트를 가져오지 않고 코드 인사이트를 얻으려면 변경 사항을 로드하세요.",
        "notification.outsideAnything.linkAction": "Gradle 프로젝트 연결",
        "gradle.script.configurations.importing.feature": "Gradle 프로젝트 가져오기 중 Gradle Kotlin DSL 스크립트 구성 로드",
        "gradle.scripts.settings.title": "독립 실행형 Gradle Kotlin DSL 스크립트 관리:",
        "notification.text.script.configuration.has.been.changed": "변경 사항을 로드하려면 Gradle 프로젝트를 가져와야 합니다.",
        "error.text.missing.jars.in.gradle.directory": "gradle 디렉토리에 jar 파일 누락됨",
        "error.text.invalid.gradle.libraries.directory": "잘못된 Gradle 라이브러리 디렉토리 {0}",
        "error.text.unable.to.get.gradle.home.directory": "Gradle 홈 디렉토리를 가져올 수 없습니다.",
        "kotlin.build.script.errors": "Kotlin 빌드 스크립트 오류",
        "text.default.kotlin.gradle.script": "Kotlin Gradle 오류",
        "notification.action.text.load.script.configuration": "구성 로드",   
        "notification.gradle.legacy.firstLoad": "Gradle 빌드 구성을 피하기 위해 코드 인사이팅이 비활성화되었습니다.",
        "notification.gradle.legacy.firstLoad.info": "<div width=400><p>스크립트 구성을 가져오려면 Gradle 구성(Configuration) 단계를 실행해야 합니다. \n큰 Gradle 프로젝트의 경우 리소스를 많이 사용할 수 있으므로 스크립트 구성을 불러오는 기능이 비활성화되어 있습니다.</p>\n<p>Gradle Kotlin DSL 스크립트를 평가하려면 \"구성 로드\"를 클릭하십시오.</p>\n<p>또는, 스크립트가 처음 열릴 때 구성을 자동으로 불러오고 구성 블록이 변경될 때마다 다시 로드하도록 설정할 수 있습니다. 스크립트의 \"자동 다시 로드\" 옵션을 켜십시오. \n이러한 설정은 프로젝트의 구성 시간이 긴 대규모 Gradle 프로젝트에는 권장하지 않습니다.</p>\n</div>",
        "notification.gradle.legacy.outsideProject": "코드 인사이틍을 사용할 수 없습니다 (관련 Gradle 프로젝트가 연결되지 않음).",
        "notification.gradle.legacy.outsideProject.addToStandaloneHelp": "<div width=400>\n  <p>이 스크립트를 평가하는 Gradle 프로젝트를 IDE로 가져와야 분석될 수 있습니다. \n  연결된 Gradle 프로젝트를 다시 가져오거나 이 스크립트를 평가하는 새 Gradle 프로젝트를 연결해 보세요.</p>\n  <p>또는, 독립 실행형 스크립트(Standalone scripts)에 추가하면 해당 구성이 자동으로 로드됩니다.</p>\n  <p><b>참고:</b> 독립 실행형 스크립트는 업데이트 시마다 별도의 Gradle 구성 단계를 실행해야 합니다. \n  규모가 큰 Gradle 프로젝트의 경우 리소스를 많이 소모할 수 있습니다.</p>\n  </div>",
        "notification.gradle.legacy.standalone.info": "<div width=400>\n  <p>이 스크립트를 평가하는 Gradle 프로젝트를 IDE로 가져오지 않았습니다. \n  <br/>\n  <p><b>참고:</b> 독립 실행형 스크립트는 업데이트 시마다 별도의 Gradle 구성 단계를 실행해야 합니다. \n  규모가 큰 Gradle 프로젝트의 경우 리소스를 많이 소모할 수 있습니다.</p>\n  </div>",
        "notification.outsideAnything.text": "코드 인사이틍을 사용할 수 없습니다 (관련 Gradle 프로젝트가 연결되지 않음).",
        "notification.wasNotImportedAfterCreation.text": "코드 인사이틍을 사용할 수 없습니다 (스크립트 구성이 로드되지 않음).",
        "notification.wasNotImportedAfterCreation.help": "<div width=400>\n  <p>Gradle Kotlin DSL 스크립트 구성이 누락되었습니다. \n  외부 Gradle 프로젝트를 가져오거나 구성을 로드하여 \n  스크립트 코드 인사이트를 얻으세요.</p>\n  </div>",
        "notification.notEvaluatedInLastImport.text": "코드 인사이팅을 사용할 수 없습니다 (스크립트 구성을 받지 못함).",
        "notification.notEvaluatedInLastImport.addAsStandaloneAction": "독립 실행형 스크립트에 추가",
        "notification.notEvaluatedInLastImport.info": "<div width=400>\n  <p>이 스크립트를 평가하는 Gradle 프로젝트를 IDE로 가져와야 분석될 수 있습니다. \n  연결된 Gradle 프로젝트를 다시 가져오거나 이 스크립트를 평가하는 새 Gradle 프로젝트를 연결해 보세요.</p>\n  <p>또는, 독립 실행형 스크립트에 추가하면 해당 구성이 별도로 로드됩니다.</p>\n  <p><b>참고:</b> 독립 실행형 스크립트는 업데이트 시마다 별도의 Gradle 구성 단계를 실행해야 합니다. \n  규모가 큰 Gradle 프로젝트의 경우 리소스를 많이 소모할 수 있습니다.</p>\n  </div>",
        "notification.standalone.text": "독립 실행형 스크립트",
        "notification.standalone.disableScriptAction": "독립 실행형 스크립트에서 제거",
        "notification.standalone.info": "<div width=400>\n  <p>이 스크립트의 구성은 Gradle 프로젝트 동기화와 별도로 로드됩니다.\n  <br/>\n  <p><b>참고:</b> 독립 실행형 스크립트는 업데이트 시마다 별도의 Gradle 구성 단계를 실행해야 합니다. \n  규모가 큰 Gradle 프로젝트의 경우 리소스를 많이 소모할 수 있습니다.</p>\n  </div>",
        "standalone.scripts.settings.column.name": "경로",
        "action.text.show.kotlin.gradle.dsl.logs.in": "{0}에서 Kotlin Gradle DSL 로그 표시",
        "action.Kotlin.Gradle.ShowDslLogs.text": "Kotlin Gradle DSL 로그 표시",       
        "text.gradle.dsl.logs.cannot.be.found.automatically.see.how.to.find.logs": "Gradle DSL 로그를 자동으로 찾을 수 없습니다.<br/>로그를 찾는 방법은 <a href=\"{0}\">여기</a>를 참조하세요.",
        "open.advanced.settings": "'고급 설정' 열기",
        "link.label.opening.advanced.settings": "'고급 설정' 여는 중",        
        "label.sources.were.not.indexed": "프로젝트의 빠른 시작을 위해 스크립트 종속성 소스 분석이 비활성화되었습니다. '고급 설정'에서 이 설정을 변경할 수 있습니다."
    }
    
    filename = "KotlinGradleScriptingBundle.properties"
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
