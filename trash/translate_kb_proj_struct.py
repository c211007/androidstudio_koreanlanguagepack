import json

ko_dict = {
  "platform.module.0.including.1": "<플랫폼 모듈 {0}({1} 포함)>",
  "special.module.for.files.not.under.source.root": "<소스 루트 아래에 없는 파일을 위한 특수 모듈>",
  "sdk.0": "<sdk {0}>",
  "sources.for.library.0": "<라이브러리 {0}의 소스>",
  "library.0": "<라이브러리 {0}>",
  "script.0.1": "<스크립트 {0} {1}>",
  "module.name.0.test": "{0} (테스트)",
  "title.toggle.library.to.source.dependency.support": "라이브러리 소스 종속성 지원 토글",
  "enable.components.for.library.to.source.analysis.in.kotlin": "Kotlin에서 프로젝트 소스 파일에 의존하는 라이브러리 분석을 위한 컴포넌트 활성화",
  "klib.manifest.description": "Klib 매니페스트",
  "module.sources.scope.0": "모듈 소스 범위: {0}"
}

with open('missing_translations/missing_keys_korean.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

filename = "KotlinBaseProjectStructureBundle.properties"
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
