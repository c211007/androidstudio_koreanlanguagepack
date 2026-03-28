import json

ko_dict = {
  "script.dependencies": "<스크립트 종속성>",
  "source.for.script.dependencies": "<스크립트 종속성의 소스>",
  "script.name.gradle.script.dependencies": "Gradle 스크립트 종속성",
  "script.name.kotlin.script.dependencies": "Kotlin 스크립트 종속성",
  "script.name.gradle.script.sdk.dependencies": "Gradle 스크립트 SDK 종속성",
  "script.name.kotlin.script.sdk.dependencies": "Kotlin 스크립트 SDK 종속성",
  "script.name.gradle.script.sdk.dependencies.0": "Gradle 스크립트 SDK < {0} >",
  "script.name.kotlin.script.sdk.dependencies.0": "Kotlin 스크립트 SDK < {0} >",
  "text.kotlin.loading.script.configuration": "Kotlin: 스크립트 구성 로드 중…",
  "text.loading.kotlin.script.configuration": "스크립트 구성 로드 중",
  "notification.text.there.is.a.new.script.context.available": "새 스크립트 컨텍스트를 사용할 수 있습니다.",
  "notification.action.text.apply.context": "컨텍스트 적용",
  "notification.action.text.enable.auto.reload": "자동 다시 로드 활성화",
  "action.ReloadScriptConfiguration.text": "스크립트 구성 다시 로드",
  "reload.script.configuration.text": "''{0}'' 구성 다시 로드",
  "action.ReloadScriptConfiguration.description": "스크립트를 다시 로드하고 구문 강조 표시를 다시 시작합니다.",
  "looking.for.script.definitions.in.classpath": "클래스 경로에서 스크립트 정의를 찾는 중",
  "notification.main.kts.unable.execute": "권한 부족으로 현재 스크립트를 실행할 수 없습니다.",
  "notification.main.kts.make.executable": "스크립트에 실행 권한 부여",
  "button.scan.classpath": "클래스 경로 검사",
  "label.kotlin.script.definitions.found": "클래스경로에서 {0}개의 새로운 정의를 찾았습니다.",
  "label.kotlin.script.no.definitions.found": "클래스 경로에서 새 정의를 찾을 수 없습니다.",
  "tooltip.this.definition.used.for.current.kotlin.script.configuration": "이 정의는 현재 Kotlin 스크립트 구성에 사용됩니다.",
  "progress.title.dependency.resolution": "종속성 확인: {0}",
  "progress.text.resolving": "확인 중: {0}",
  "progress.title.processing.scripts": "Kotlin: 스크립트 처리 중…"
}

with open('missing_translations/missing_keys_korean.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

filename = "KotlinBaseScriptingBundle.properties"
found = False
for file_entry in data.get('new_files', []):
    if file_entry['filename'] == filename:
        file_entry['keys'].update(ko_dict)
        found = True
        break
if not found:
    data.setdefault('new_files', []).append({"filename": filename, "keys": ko_dict})

print(f"Updated {filename}")

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
