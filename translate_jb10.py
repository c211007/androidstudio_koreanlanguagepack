import json

ko_dict = {
  "notification.content.change.jdk": "JDK 변경",
  "code.vision.java.external.configuration.name": "Java 구성",
  "code.vision.java.external.configuration.description": "외부 구성 파일(.sdkmanrc, .tool-versions)에 구성된 JDK의 상태입니다.",
  "external.java.configuration.inlay.provider.name": "외부 JDK 구성",
  "external.java.configuration.inlay.unknown": "동기화 중…",
  "external.java.configuration.inlay.already.configured": "프로젝트 JDK({0})",
  "external.java.configuration.inlay.found": "프로젝트 JDK로 설정",
  "external.java.configuration.inlay.missing.actions": "JDK를 찾을 수 없습니다. 더 보기…",
  "external.java.configuration.inlay.missing": "JDK를 찾을 수 없습니다.",
  "external.java.configuration.copy.command": "다운로드 명령 복사",
  "external.java.configuration.refresh": "새로 고침",
  "button.to.another.directory": "디렉터리(&D)",
  "button.to.another.source.root": "소스 루트(&S)",
  "where.do.you.want.to.move.directory.prompt": "{0}\n\n디렉터리를 다른 소스 루트 또는 다른 디렉터리로 이동하시겠습니까?",
  "loading.additional.annotations": "추가 어노테이션 로드 중…",
  "tooltip.anonymous": "익명",
  "tooltip.has.several.functional.implementations": "여러 기능적 구현이 있음",
  "tooltip.implements.method": "메서드를 구현함",
  "tooltip.implements.method.in": "다음에서 메서드를 구현함",
  "tooltip.is.functionally.implemented.in": "다음에서 기능적으로 구현됨",
  "tooltip.is.implemented.by": "다음에 의해 구현됨",
  "tooltip.is.implemented.by.several.subclasses": "여러 하위 클래스에 의해 구현됨",
  "tooltip.is.implemented.in": "다음에서 구현됨",
  "tooltip.is.implemented.in.several.subclasses": "여러 하위 클래스에서 구현됨",
  "tooltip.is.overridden.by.several.subclasses": "여러 하위 클래스에 의해 재정의됨",
  "tooltip.is.overridden.in": "다음에서 재정의됨",
  "tooltip.is.overridden.in.several.subclasses": "여러 하위 클래스에서 재정의됨",
  "tooltip.is.subclassed.by": "다음에 의해 하위 분류됨",
  "tooltip.overrides.method": "메서드를 재정의함",
  "tooltip.overrides.method.in": "다음에서 메서드를 재정의함",
  "tooltip.via.subclass": "하위 클래스를 통해",
  "progress.title.calculate.applicable.types": "적용 가능한 유형 계산 중…",
  "completion.inner.scope.tail.text": " ({0} 블록에서)",
  "completion.inner.scope": "내부",
  "javadoc.documentation.url.checked": "다음 문서 {0, choice, 1#URL이|2#URL이} 확인되었습니다:",
  "javadoc.edit.api.docs.paths": "API 문서 경로 편집",
  "intention.family.name.move.class.to.test.root": "클래스를 테스트 루트로 이동",
  "intention.name.move.class.to.test.root": "''{0}''을(를) 테스트 루트로 이동",
  "megabytes.unit": "MB",
  "java.platform.module.system.name": "Java 플랫폼 모듈 시스템"
}

with open('missing_translations/missing_keys_korean.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for file_entry in data['new_files']:
    if file_entry['filename'] == 'JavaBundle.properties':
        file_entry['keys'].update(ko_dict)
        print("Updated JavaBundle.properties (Keys 321-360)")
        break

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
