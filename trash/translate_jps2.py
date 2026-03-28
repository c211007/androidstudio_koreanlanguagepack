import json

ko_dict = {
  "build.message.missing.content.for.file.0": "{0} 파일에 대한 콘텐츠가 누락되었습니다.",
  "build.message.multiple.encodings.set.for.module.chunk": "모듈 청크 {0}에 여러 인코딩이 설정되었습니다.{2, choice, 0#\\n\"{1}\"이(가) 컴파일러에 의해 사용됩니다.|1#}",
  "build.message.some.modules.with.cyclic.dependencies.0.have.additional.command.line.parameters": "순환 종속성이 있는 일부 모듈 [{0}]의 프로젝트 설정에서 ''추가 명령줄 매개변수''가 재정의되었습니다.\\n이러한 컴파일 옵션은 주기의 모든 모듈에 적용되었습니다.",
  "build.message.unsupported.compact.compilation.profile.was.requested": "압축 컴파일 프로필이 요청되었지만 \"{0}\" 모듈의 대상 플랫폼이 javac의 플랫폼({1})과 다릅니다.\\n이러한 구성에는 컴파일 프로필이 지원되지 않습니다.",
  "build.message.user.specified.option.0.for.1.may.conflict.with.calculated.option": "\"{1}\"에 대해 사용자가 지정한 옵션 \"{0}\"이(가) 프로젝트 설정에 따라 자동으로 계산된 해당 옵션과 충돌할 수 있습니다.",
  "build.message.user.specified.option.0.is.ignored.for.1": "사용자가 지정한 옵션 \"{0}\"은(는) \"{1}\"에서 무시됩니다. 이 컴파일 매개변수는 프로젝트 설정에 따라 자동으로 설정됩니다.",
  "build.message.incremental.annotation.processing.disabled.0": "JPS 증분 어노테이션 처리가 비활성화되었습니다. 부분 다시 컴파일 시의 컴파일 결과가 정확하지 않을 수 있습니다. 증분 어노테이션 처리 환경을 활성화/비활성화하려면 빌드 프로세스 \"{0}\" VM 플래그를 사용하세요.",
  "progress.message.checking.dependencies.0": "종속성 확인 중… [{0}]",
  "progress.message.checking.sources": "소스 확인 중",
  "progress.message.marking.0.and.direct.dependants.for.recompilation": "다시 컴파일을 위해 {0} 및 직접적인 종속 요소 표시 중",
  "progress.message.parsing.java.0": "Java 파싱 중… [{0}]",
  "progress.message.updating.dependency.information.0": "종속성 정보 업데이트 중… [{0}]",
  "progress.message.writing.classes.0": "클래스 작성 중… {0}",
  "build.message.modules.0.and.1.must.have.the.same.language.level": "{0} 모듈과 {1} 모듈은 주기적 종속성 때문에 언어 수준이 동일해야 합니다.",
  "build.message.modules.0.and.1.must.have.the.same.additional.command.line.parameters": "{0} 모듈과 {1} 모듈은 주기적 종속성 때문에 동일한 ''추가 명령줄 매개변수''가 지정되어야 합니다.",
  "build.message.annotation.processing.is.not.supported.for.module.cycles": "모듈 주기에 대해서는 어노테이션 처리가 지원되지 않습니다. [{0}] 주기의 모든 모듈이 어노테이션 처리에서 제외되었는지 확인하세요.",
  "target.description.tests.of.0": "{0}의 테스트",
  "target.description.0.and.1.more": "{0} 및 {1}개 더",
  "build.messages.modules.were.fully.rebuilt": "프로젝트 구성{3, choice, 0#|1#/종속성} 변경으로 인해 {1, choice, 1#{0} 모듈이|2#{0} 모듈이|7#{0} 모듈 및 다른 {2}개가} 완전히 다시 빌드되었습니다.",
  "build.message.errors.occurred.while.compiling.module.0": "''{0}'' 모듈을 컴파일하는 동안 오류가 발생했습니다.",
  "build.message.compilation.failed.internal.java.compiler.error": "컴파일 실패: 내부 Java 컴파일러 오류",
  "build.message.cannot.start.javac.process.for.0.unknown.jdk.home": "{0}에 대한 javac 프로세스를 시작할 수 없습니다: 알 수 없는 JDK 홈 경로 또는 버전입니다.\\n프로젝트 구성을 확인하세요.",
  "build.message.unsupported.javac.version": "{0}에 대한 javac 프로세스를 시작할 수 없습니다: JDK {1}을(를) 사용하도록 구성되어 있지만,\\nIDE는 JDK {2} 이상을を使用した 컴파일만 지원합니다.\\n모듈을 지원되는 JDK 버전과 연결하는 것을 고려하세요. 생성된 *.class 파일을 최신 컴파일러 버전으로 컴파일하더라도\\nJava {3}와 호환되게 유지하도록 현재 Java 언어 수준을 유지할 수 있습니다.",
  "build.message.fallback.javac.used": "''{0}'' 모듈이 JVM 대상 {1}에 대해 구성되었습니다. 구성된 대체 SDK에서 java 컴파일러 {2}을(를) 사용하여 모듈을 컴파일합니다.",
  "build.message.cannot.compile.fallback.jdk.not.supported": "JVM 대상 {1}에 대해 구성된 ''{0}'' 모듈을 컴파일할 수 없습니다: 지정된 대체 SDK 버전 {2}은(는) IDE에서 지원되지 않습니다.",
  "build.message.cannot.compile.fallback.jdk.unsupported.jvm.target": "JVM 대상 {1}에 대해 구성된 ''{0}'' 모듈을 컴파일할 수 없습니다: 지정된 대체 SDK 버전 {2}은(는) 필수 jvm 대상 {1}을(를) 지원하지 않습니다.",
  "build.message.cannot.compile.associated.jdk.not.supported": "JVM 대상 {1}에 대해 구성된 ''{0}'' 모듈을 컴파일할 수 없습니다: 현재 모듈과 연결된 JDK {2}은(는) IDE에서 지원되지 않습니다.",
  "build.message.cannot.compile.associated.jdk.unsupported.jvm.target": "JVM 대상 {1}에 대해 구성된 ''{0}'' 모듈을 컴파일할 수 없습니다: 현재 모듈과 연결된 JDK {2}은(는) 필수 jvm 대상 {1}을(를) 지원하지 않습니다.",
  "build.message.fallback.jdk.hint": "프로젝트 구조 | 플랫폼 설정 | SDK에 JDK {0} 이상을 추가하세요.\\n추가된 JDK는 JVM 대상 {1}에 대한 교차 컴파일을 지원해야 합니다.\\n이 JDK는 이전 JVM 대상을 위해 IDE에 의해 자동으로 선택됩니다.",
  "builder.name.artifacts.builder": "아티팩트 빌더",
  "build.message.archive.0.doesn.t.contain.files.so.it.won.t.be.created": "''{0}'' 아카이브에 파일이 포함되어 있지 않아 생성되지 않습니다.",
  "build.message.cannot.build.0.artifact.it.includes.itself": "''{0}'' 아티팩트를 빌드할 수 없습니다: {2, choice, 0#자체|1#''''{1}'''' 아티팩트}(이)가 출력 레이아웃에 포함되어 있습니다.",
  "build.message.cannot.build.0.artifact.output.path.is.not.specified": "''{0}'' 아티팩트를 빌드할 수 없습니다: 출력 경로가 지정되지 않았습니다.",
  "build.message.cannot.build.circular.dependency.found.between.0.and.1": "빌드할 수 없음: ''{0}''과(와) ''{1}'' 사이에 주기적 종속성이 발견되었습니다.",
  "build.message.cannot.create.0.1": "''{0}''을(를) 생성할 수 없습니다: {1}",
  "build.message.cannot.create.manifest.mf.from.0.1": "{0}에서 MANIFEST.MF를 생성할 수 없습니다: {1}",
  "build.message.cannot.delete.file.0": "''{0}'' 파일을 삭제할 수 없습니다.",
  "build.message.cannot.extract.0.from.1.while.building.2.artifact.3": "''{2}'' 아티팩트를 빌드하는 동안 ''{1}''에서 ''{0}''을(를) 추출할 수 없습니다: {3}",
  "build.message.deletion.of.outdated.files.stopped": "삭제할 수 없는 파일이 너무 많아 오래된 파일 삭제가 중지되었습니다.",
  "build.message.manifest.file.0.included.into.archive.does.not.contain.required.attribute": "''{1}'' 아카이브에 포함된 ''{0}'' 매니페스트 파일에 ''{2}'' 속성이 포함되어 있지 않습니다. 이러한 매니페스트 파일은 유효하지 않으며 해당 콘텐츠는 JAR 파일에 포함되지 않습니다."
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

print(f"Updated {filename} (Keys 41-80)")

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
