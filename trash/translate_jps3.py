import json

ko_dict = {
  "progress.message.building.archives": "아카이브 빌드 중…",
  "progress.message.building.artifact.0": "''{0}'' 아티팩트 빌드 중…",
  "progress.message.building.artifact.0.copying.files": "''{0}'' 아티팩트 빌드 중: 파일 복사 중…",
  "progress.message.building.jar.0": "{0} 빌드 중…",
  "progress.message.copying.archives": "아카이브 복사 중…",
  "progress.message.deleting.outdated.files": "오래된 파일 삭제 중…",
  "progress.message.running.0.tasks.for.1.artifact": "''{1}'' 아티팩트에 대한 {0, choice, 0#전처리|1#마무리|2#후처리} 작업 실행 중…",
  "build.message.cannot.instrument.0.1": "{0}을(를) 계측할 수 없습니다: {1}",
  "builder.name.notnull.instrumentation": "NotNull 계측",
  "progress.message.adding.notnull.assertions": "null 허용 여부 어설션 추가 중…",
  "build.message.rmi.stub.generation.failed": "RMI 스텁 생성 실패",
  "builder.name.backward.references.indexer": "역방향 참조 인덱서",
  "progress.message.generating.rmi.stubs": "RMI 스텁 생성 중…",
  "builder.name.maven.dependency.resolver": "Maven 종속성 확인자",
  "builder.name.project.dependencies.resolver": "프로젝트 종속성 확인자",
  "progress.message.resolving.0.library": "''{0}'' 라이브러리 확인 중…",
  "progress.message.resolving.repository.libraries.in.the.project": "프로젝트의 리포지토리 라이브러리 확인 중…",
  "progress.message.removing.invalid.artifact": "''{0}'' 라이브러리: 잘못된(손상되었을 가능성이 있는) 아티팩트 {1} 제거 중",
  "build.message.error.compile.roots.verification.mismatch": "''{0}'' 라이브러리: 확인 메타데이터가 컴파일된 루트와 일치하지 않습니다.",
  "build.message.error.missing.artifacts": "''{0}'' 라이브러리: 필요한 아티팩트 {1}을(를) 찾을 수 없습니다.",
  "build.message.error.invalid.sha256.checksum": "''{0}'' 라이브러리: {1}의 SHA256 체크섬이 잘못되었습니다. {2}이(가) 필요하지만 {3}이(가) 발견되었습니다.",
  "build.message.error.bind.repository.missing": "''{0}'' 라이브러리: 바인딩 리포지토리가 없습니다.",
  "build.message.error.bind.repository.id.not.found": "ID가 ''{0}''인 바인딩 리포지토리를 찾을 수 없습니다.",
  "build.message.error.resolving.dependencies.for": "{0}에 대한 종속성을 확인하는 중 오류가 발생했습니다.",
  "build.message.unknown.host.0": "알 수 없는 호스트: {0}",
  "builder.name.resource.compiler": "리소스 컴파일러",
  "progress.message.copying.resources.0": "리소스 복사 중… [{0}]",
  "intellilang.pattern.validator.presentable.name": "IntelliLang 패턴 유효성 검사기",
  "intellilang.pattern.validator.progress.message": "패턴 어설션 추가 중…",
  "packaging.jlink.build.task.modules.not.found": "JPMS 모듈을 찾을 수 없음",
  "packaging.jlink.build.task.wrong.java.version": "jlink를 사용하여 런타임 이미지를 빌드하려면 Java 버전 9 이상이 필요합니다.",
  "packaging.jlink.build.task.unknown.artifact.path": "알 수 없는 아티팩트 출력 경로",
  "packaging.jlink.build.task.run.time.image.deletion.failure": "기존 런타임 이미지를 삭제할 수 없습니다.",
  "packaging.jlink.build.task.failure": "jlink 작업 실패",
  "progress.text.rolling.back.downloaded.caches": "다운로드한 캐시 롤백 중",
  "progress.text.rolling.back": "롤백 중",
  "progress.text.fetching.cache.for.commit": "커밋에 대한 캐시 가져오는 중: {0}",
  "progress.text.local.build.is.quicker": "로컬에서 프로젝트를 빌드하는 것이 캐시를 다운로드하는 것보다 빠릅니다.",
  "progress.text.removing.old.caches": "다운로드하기 전에 이전 캐시 제거 중",
  "progress.details.applying.downloaded.caches": "다운로드한 캐시 적용 중"
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

print(f"Updated {filename} (Keys 81-120)")

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
