import json

ko_dict = {
  "kotlin.compiler.js.option.panel.title": "Kotlin을 JavaScript로",
  "kotlin.script.option.panel.title": "Kotlin 스크립트(베타)",
  "kotlin.compiler.js.option.generate.sourcemaps": "소스 맵 생성(&S)",
  "embed.source.code.into.source.map": "소스 코드를 소스 맵에 포함:",
  "kotlin.compiler.js.option.output.copy.files": "라이브러리 런타임 파일 복사(&C)",
  "enable.incremental.compilation": "증분 컴파일 활성화",
  "keep.compiler.process.alive.between.invocations": "호출 간 컴파일러 프로세스를 활성 상태로 유지",
  "module.kind": "모듈 종류(&K):",
  "destination.directory": "대상 디렉터리(&D)",
  "kotlin.compiler.lib": "lib",
  "kotlin.compiler.version": "Kotlin 컴파일러 버전(&K)",
  "target.jvm.version": "대상 JVM 버전(&J)",
  "language.version": "언어 버전(&L)",
  "api.version": "API 버전(&I)",
  "script.definition.template.classes.to.load.explicitly": "명시적으로 로드할 스크립트 정의 템플릿 클래스(&T)",
  "classpath.required.for.loading.script.definition.template.classes": "스크립트 정의 템플릿 클래스를 로드하는 데 필요한 클래스 경로(&F)"
}

with open('missing_translations/missing_keys_korean.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

filename = "KotlinBaseCompilerConfigurationUiBundle.properties"
found = False
for file_entry in data.get('new_files', []):
    if file_entry['filename'] == filename:
        file_entry['keys'].update(ko_dict)
        found = True
        break
if not found:
    data.setdefault('new_files', []).append({"filename": filename, "keys": ko_dict})

print(f"Updated {filename} (Keys 41-56)")

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
