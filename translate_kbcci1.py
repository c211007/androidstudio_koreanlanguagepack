import json

ko_dict = {
  "facet.name.general": "일반",
  "facet.column.name.options": "옵션",
  "facet.column.name.plugin": "플러그인",
  "facet.name.compiler.plugins": "컴파일러 플러그인",
  "facet.text.following.options.are.not.correct": "다음 옵션이 올바르지 않습니다.",
  "facet.label.text.target.platform": "대상 플랫폼:",
  "facet.label.text.selected.target.platforms": "선택한 대상 플랫폼:",
  "facet.label.text.the.project.is.imported.from.external.build.system.and.could.not.be.edited": "프로젝트가 외부 빌드 시스템에서 가져온 것이므로 편집할 수 없습니다.",
  "facet.checkbox.text.use.project.settings": "프로젝트 설정 사용",
  "facet.label.text.project.settings.that.are.used.for.this.facet": "이 패싯에 사용되는 프로젝트 설정:",
  "facet.text.multiplatform": "멀티플랫폼",
  "facet.link.text.edit.project.settings": "프로젝트 설정 편집",
  "facet.error.text.at.least.one.target.platform.should.be.selected": "적어도 하나의 대상 플랫폼을 선택해야 합니다.",
  "facet.text.following.arguments.are.redundant": "다음 인수는 중복됩니다: {0}",
  "facet.text.following.arguments.override.facet.settings": "다음 인수는 패싯 설정을 재정의합니다: {0}",
  "facets.editor.general.tab.label.depends.on.0": "다음에 종속됨: {0}.",
  "configuration.description.plain.put.to.global.scope": "일반(전역 범위에 배치)",
  "configuration.description.amd": "AMD",
  "configuration.description.commonjs": "CommonJS",
  "configuration.description.umd.detect.amd.or.commonjs.if.available.fallback.to.plain": "UMD(사용 가능한 경우 AMD 또는 CommonJS를 감지하고 실패 시 일반으로 대체)",
  "configuration.description.always": "항상",
  "configuration.description.never": "안 함",
  "configuration.description.when.inlining.a.function.from.other.module.with.embedded.sources": "소스가 포함된 다른 모듈의 함수를 인라인할 때",
  "configuration.title.choose.output.directory": "출력 디렉터리 선택",
  "configuration.warning.text.modules.override.project.settings": "{0} 모듈이 프로젝트 설정을 재정의합니다.",
  "configuration.warning.text.following.modules.override.project.settings": "다음 모듈이 프로젝트 설정을 재정의합니다.",
  "configuration.text.and": "및",
  "configuration.text.other.s": "기타",
  "loading.available.versions.from.maven": "Maven에서 사용 가능한 버전 로드 중…",
  "failed.fetching.all.available.versions.from.maven": "Maven에서 사용 가능한 모든 버전을 가져오지 못했습니다.",
  "configuration.name.kotlin.compiler": "Kotlin 컴파일러",
  "configuration.text.bundled.0.jps.version": "번들됨({0})",
  "configuration.text.0.unsupported.jps.version": "{0}(지원되지 않음)",
  "deprecated.jvm.version": "(지원 중단됨)",
  "configuration.warning.text.language.version.unsupported": "{0} 언어 버전은 더 이상 지원되지 않습니다.",
  "configuration.warning.text.api.version.unsupported": "{0} API 버전은 더 이상 지원되지 않습니다.",
  "kotlin.compiler.option.generate.no.warnings": "컴파일러 경고 보고(&W)",
  "kotlin.compiler.option.additional.command.line.parameters": "추가 명령줄 매개변수(&A):",
  "additional.command.line.parameters": "추가 명령줄 매개변수",
  "kotlin.compiler.jvm.option.panel.title": "Kotlin을 JVM으로"
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

print(f"Updated {filename} (Keys 1-40)")

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
