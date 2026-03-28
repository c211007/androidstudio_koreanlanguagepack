import json

ko_dict = {
  "build.message.builder.0.requested.build.stop": "빌더 {0}이(가) 빌드 중지를 요청했습니다.",
  "build.message.cannot.build.0.because.it.is.included.into.a.circular.dependency.1": "순환 종속성({1})에 포함되어 있으므로 {0}을(를) 빌드할 수 없습니다.",
  "build.message.consider.building.whole.project.or.rebuilding.the.module": "전체 프로젝트를 빌드하거나 모듈을 다시 빌드하는 것을 고려하세요.",
  "build.message.dependency.data.format.has.changed.project.rebuild.required": "종속성 데이터 형식이 변경되었습니다. 프로젝트를 다시 빌드해야 합니다.",
  "build.message.error.cleaning.compiler.storages": "컴파일러 스토리지 정리 중 오류 발생",
  "build.message.error.cleaning.timestamps.storage": "타임스탬프 스토리지 정리 중 오류 발생",
  "build.message.error.cleaning.library.roots.storage": "라이브러리 루트 스토리지 정리 중 오류 발생",
  "build.message.failed.to.delete.output.files.from.obsolete.0.target.1": "더 이상 사용되지 않는 ''{0}'' 대상에서 출력 파일을 삭제하지 못했습니다: {1}",
  "build.message.failed.to.load.project.configuration.0": "프로젝트 구성을 로드하지 못했습니다: {0}",
  "build.message.insufficient.memory": "OutOfMemoryError: 메모리가 부족합니다",
  "build.message.internal.caches.are.corrupted": "내부 캐시가 손상되었거나 형식이 오래되어 프로젝트를 강제로 다시 빌드합니다: {0}",
  "build.message.internal.error.0.1": "내부 오류({0}): {1}",
  "build.message.output.path.0.intersects.with.a.source.root": "출력 경로 {0}이(가) 소스 루트와 교차합니다. 빌드에서 생성된 파일만 정리됩니다.",
  "build.message.perform.full.project.rebuild": "전체 프로젝트를 다시 빌드하세요(빌드 | 프로젝트 다시 빌드)",
  "build.message.problems.clearing.output.files.for.target.0.1": "\"{0}\" 대상의 출력 파일을 지우는 중 문제가 발생했습니다: {1}",
  "build.message.project.rebuild.forced.0": "프로젝트 강제 다시 빌드: {0}",
  "build.message.the.build.has.been.canceled": "빌드가 취소되었습니다.",
  "build.message.too.many.modules.require.recompilation.forcing.full.project.rebuild": "너무 많은 모듈을 다시 컴파일해야 하므로 전체 프로젝트를 강제로 다시 빌드합니다.",
  "build.message.unsupported.message.type.0": "지원되지 않는 메시지 유형: {0}",
  "builder.0.requested.rebuild.of.module.chunk.1": "빌더 \"{0}\"이(가) 모듈 청크 \"{1}\"의 다시 빌드를 요청했습니다.",
  "builder.name.root": "빌드",
  "progress.message.cleaning.old.output.directories": "이전 출력 디렉터리를 지우는 중…",
  "progress.message.cleaning.output.directories": "출력 디렉터리를 지우는 중…",
  "progress.message.dependency.analysis.found.0.affected.files": "종속성 분석에서 영향을 받는 파일 {0}개를 찾았습니다.",
  "progress.message.finished.saving.caches": "완료됨, 캐시 저장 중…",
  "progress.message.running.after.tasks": "'after' 작업 실행 중",
  "progress.message.running.before.tasks": "'before' 작업 실행 중",
  "build.message.conflicting.outputs.error": "출력 파일 \"{0}\"은(는) 이미 \"{1}\"에서 등록되었습니다.",
  "progress.message.updating.library.state": "라이브러리 종속성: {2}에 대해 업데이트된 라이브러리 루트 {0}개, 제거된 라이브러리 루트 {1}개를 찾았습니다.",
  "progress.message.processing.library": "''{0}'' 라이브러리: {1}개의 클래스 파일을 파싱했습니다.",
  "build.message.0.was.used.to.compile.1": "[{1}]을(를) 컴파일하는 데 {0}이(가) 사용되었습니다.",
  "build.message.0.was.used.to.compile.1.modules": "{1}개의 모듈을 컴파일하는 데 {0}이(가) 사용되었습니다.",
  "build.message.0.was.used.to.compile.java.sources": "Java 소스를 컴파일하는 데 {0}이(가) 사용되었습니다.",
  "build.message.cannot.compile.a.module.cycle.with.multiple.module.info.files": "여러 module-info.java 파일이 있는 모듈 주기를 컴파일할 수 없습니다: {0}",
  "build.message.cannot.find.jdk.0.for.module.1": "''{1}'' 모듈에 대한 JDK ''{0}''을(를) 찾을 수 없습니다.",
  "build.message.cannot.find.jdk.for.module.0.1.points.to.2": "''{0}'' 모듈에 대한 JDK를 찾을 수 없습니다: ''{1}''이(가) {2}을(를) 가리킵니다.",
  "build.message.class.dependency.information.may.be.incomplete": "클래스 종속성 정보가 불완전할 수 있습니다. 생성된 클래스 {0}을(를) 파싱하는 중 오류가 발생했습니다.",
  "build.message.compilation.failed.errors.0.warnings.1": "컴파일 실패: 오류: {0}; 경고: {1}",
  "build.message.internal.error.0": "내부 오류: \\n{0}",
  "build.message.jdk.isn.t.specified.for.module.0": "''{0}'' 모듈에 JDK가 지정되지 않았습니다."
}

with open('missing_translations/missing_keys_korean.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

filename = "JpsBuildBundle.properties"
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
