import json

ko_dict = {
  "dialog.title.move.directory": "디렉터리 이동",
  "progress.title.checking.if.class.exists": "대상 클래스 ''{0}''이(가) 존재하는지 확인 중…",
  "quickfix.find.cause.description": "이 경고를 초래한 코드 요소를 강조 표시하고 정확히 어떻게 기여하는지 설명하려고 시도합니다.",
  "completion.generate.via.wizard": "(마법사를 통해 생성)",
  "notification.group.jdk.resolve.problems": "JDK를 해결하지 못했습니다.",
  "notification.group.repository": "리포지토리와 동기화된 JAR 파일",
  "notification.group.source.searcher": "JAR 파일의 소스를 찾지 못했습니다.",
  "notification.group.language.level": "프리뷰 Java 언어 레벨을 사용하려면 라이선스 동의가 필요합니다.",
  "notification.group.preview.features": "프리뷰 Java 언어 레벨이 중단될 수 있습니다.",
  "notification.group.redundant.exports": "중복된 exports/opens를 제거할 수 있습니다.",
  "notification.group.setup.jdk": "JDK가 구성되었습니다.",
  "notification.group.setup.external.annotations": "외부 어노테이션을 로드하지 못했습니다.",
  "notification.group.testintegration": "@TestDataPath에 대한 테스트를 생성하지 못했습니다.",
  "notification.group.legacy.library": "레거시 라이브러리는 IDE 설치에 의존합니다.",
  "notification.group.arch.checker": "JDK와 시스템 아키텍처가 다릅니다.",
  "arch.checker.notification.title": "선택한 JDK로 인해 빌드가 느려질 수 있습니다.",
  "arch.checker.notification.content": "JDK ''{0}''({1})이(가) 시스템 아키텍처({2})와 일치하지 않습니다.",
  "arch.checker.notification.project.structure": "JDK 구성",
  "notification.group.unsupported.jdk": "지원되지 않는 JDK",
  "unsupported.jdk.notification.title": "지원되지 않는 JDK",
  "unsupported.jdk.notification.content": "Java 7에 대한 Oracle 확장 지원은 2022년에 종료되었습니다. ''{0}''을(를) 사용하면 보안 문제가 발생할 수 있습니다.",
  "inspection.io.stream.constructor.description": "'Files' 메서드를 사용하여 'InputStream' 및 'OutputStream'을 생성할 수 있습니다.",
  "inspection.input.stream.constructor.message": "'Files.newInputStream()'을 사용하여 'InputStream'을 생성할 수 있습니다.",
  "inspection.output.stream.constructor.message": "'Files.newOutputStream()'을 사용하여 'OutputStream'을 생성할 수 있습니다.",
  "inspection.bulk.file.attributes.read.description": "대량 'Files.readAttributes()' 호출을 사용할 수 있습니다.",
  "inspection.replace.with.bulk.file.attributes.read.fix.family.name": "대량 'Files.readAttributes()' 호출로 바꾸기",
  "inspection.bulk.file.attributes.read.message": "여러 파일 속성 호출을 단일 'Files.readAttributes()' 호출로 바꿀 수 있습니다.",
  "external.annotations.problem.title": "외부 어노테이션을 읽을 수 없습니다.",
  "external.annotations.problem.parse.error": "파일: {0}<br>문제: {1}",
  "external.annotations.open.file": "어노테이션 파일 열기",
  "intention.family.name.set.explicit.variable.type": "명시적 변수 유형 설정",
  "intention.name.set.variable.type": "변수 유형을 ''{0}''(으)로 설정",
  "introduce.parameter.inlay.title.delegate": "위임",
  "introduce.parameter.inlay.tooltip.delegate": "오버로딩 메서드를 통해 위임",
  "introduce.parameter.advertisement.text": "{0}을(를) 눌러 오버로딩 메서드를 통해 위임하거나 {1}을(를) 눌러 더 많은 옵션을 표시합니다.",
  "progress.title.collect.method.overriders": "메서드 재정의 수집 중…",
  "remove.var.keyword.text": "'var' 제거",
  "error.message.ide.does.not.support.starting.processes.using.old.java": "IDE는 Java {0}을(를) 사용하여 Java 프로세스를 시작하는 것을 지원하지 않습니다.\n 지원되는 최소 버전은 Java 8입니다.\n 이 문제를 해결하려면 최신 Java 버전을 사용하도록 실행 구성을 변경하십시오.",
  "error.message.ide.does.not.support.starting.processes.using.old.java.app": "IDE는 Java {0}을(를) 사용하여 Java 프로세스를 시작하는 것을 지원하지 않습니다.\n 지원되는 최소 버전은 Java 8입니다. 이 문제를 해결하려면 다음 중 하나를 수행하십시오.\n * 최신 Java 버전을 사용하도록 실행 구성을 변경합니다.\n * `idea.no.launcher` 사용자 지정 속성을 `true`로 설정하여 IntelliJ 런처를 비활성화합니다(`소프트 종료`와 같은 추가 기능이 작동하지 않음).",
  "intention.family.name.upgrade.jdk": "JDK 업그레이드"
}

with open('missing_translations/missing_keys_korean.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for file_entry in data['new_files']:
    if file_entry['filename'] == 'JavaBundle.properties':
        file_entry['keys'].update(ko_dict)
        print("Updated JavaBundle.properties (Keys 361-400)")
        break

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
