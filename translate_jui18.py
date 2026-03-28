import json

ko_dict = {
  "action.DownloadJdkAction.text": "JDK 다운로드…",
  "action.AddJdkAction.text": "디스크에서 JDK 추가…",
  "library.depends.on.ide.title": "IDE 설치의 JAR에 대한 종속성",
  "library.depends.on.ide.message": "{0} 라이브러리는 IDE 설치의 JAR을 사용합니다. 향후 IDE 버전에서 JAR이 제거되면 손상될 수 있습니다. {1}",
  "library.depends.on.ide.message.can.be.replaced": "Maven 아티팩트 {0}(으)로 대체될 수 있습니다.",
  "library.depends.on.ide.message.replacement.not.found": "그러나 직접적인 Maven 대체를 찾지 못했습니다. 구조 조정을 고려하세요.",
  "library.depends.on.ide.message.jar.mixture": "자동 대체를 불가능하게 만드는 다른 JAR도 포함되어 있습니다. 구조 조정을 고려하세요.",
  "library.depends.on.ide.fix.convert.to.repo": "{0}을(를) Maven 라이브러리로 변환",
  "library1": "라이브러리 '",
  "is.used.in": "'은(는) 다음에서 사용됩니다: ",
  "and.in": " 및 ",
  "in": ", ",
  "action.PromoSpring.text": "활성 Spring 프로필 변경…",
  "action.PromoOpenAPI.text": "OpenAPI 소스 구성…",
  "action.PromoBeans.text": "빈",
  "action.PromoEndpoints.text": "엔드포인트",
  "action.PromoDatabase.text": "데이터베이스",
  "action.PromoKubernetes.text": "Kubernetes",
  "action.PromoPersistence.text": "지속성",
  "action.PromoProfiler.text": "IntelliJ 프로파일러",
  "feature.spring.wizard.description": "IntelliJ IDEA에서 Spring Boot 통합을 사용할 수 있습니다.",
  "feature.spring.description.html": "Spring MVC, Spring Data, Spring Security, Spring Cloud를 포함한 Java 및 Kotlin 코드 모두에서 방대한 기본 개발자 도구를 사용하고 지원합니다. 여기에는 다음이 포함됩니다:",
  "feature.spring.run.config": "전용 실행 구성",
  "feature.spring.config.files": "구성 파일에 대한 광범위한 지원",
  "feature.spring.data": "지능형 JPA 및 SQL 코드 지원",
  "feature.spring.navigation": "고급 코드 탐색 및 시각화 기능",
  "promo.configurable.profiler": "Java 프로파일러",
  "feature.profiler.description.html": "애플리케이션 성능에 대한 <a href=\"{0}\">통계</a>를 확보하고 다음과 같은 강력한 JVM 프로파일링 기능으로 성능을 향상하세요:",
  "feature.profiler.cpu": "CPU 및 메모리 할당 프로파일링",
  "feature.profiler.memory": "메모리 스냅샷",
  "feature.profiler.hints": "에디터 내 성능 힌트",
  "progress.title.downloading": "{0} 다운로드 중…",
  "group.Java.MarkRootGroup.text": "디렉터리를 Java 루트로 표시",
  "group.MarkSourceRootGroup.text": "디렉터리를 JVM 소스 루트로 표시",
  "group.MarkGeneratedSourceRootGroup.text": "생성된 소스로 표시"
}

with open('missing_translations/missing_keys_korean.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for file_entry in data['new_files']:
    if file_entry['filename'] == 'JavaUiBundle.properties':
        file_entry['keys'].update(ko_dict)
        print("Updated JavaUiBundle.properties (Keys 641-671)")
        break

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
