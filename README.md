# Android Studio 한국어 언어팩

[![Build](https://github.com/c211007/androidstudio_koreanlanguagepack/workflows/Build/badge.svg)][gh:build]

[gh:build]: https://github.com/c211007/androidstudio_koreanlanguagepack/actions/workflows/build.yml

<!-- Plugin description -->
**Android Studio 한국어 언어팩** (Android Studio Korean Language Pack)은 Android Studio / IntelliJ 기반 IDE의 UI를 한국어로 번역하여 제공하는 플러그인입니다.

이 플러그인을 설치하면 IDE의 메뉴, 대화 상자, 도구 창 등 주요 UI 요소가 한국어로 표시됩니다.

## 설치 방법

1. Android Studio를 실행합니다.
2. **File > Settings > Plugins** 메뉴를 엽니다.
3. Marketplace 탭에서 `Android Studio 한국어 언어팩`을 검색합니다.
4. **Install** 버튼을 클릭하여 플러그인을 설치합니다.
5. IDE를 재시작합니다.

## 기여하기

번역 개선 및 오류 신고는 [GitHub 이슈](https://github.com/c211007/androidstudio_koreanlanguagepack/issues)를 통해 제출해 주세요.
<!-- Plugin description end -->

## 개발 환경 설정

이 플러그인은 [IntelliJ Platform Gradle Plugin][gh:intellij-platform-gradle-plugin]을 사용하여 빌드됩니다.

### 빌드 요구 사항

- JDK 21 이상
- Gradle (Gradle Wrapper 포함)

### 빌드 방법

```bash
./gradlew build
```

### IDE 실행

```bash
./gradlew runIde
```

### 테스트 실행

```bash
./gradlew test
```

## 번역 기여 방법

1. 이 저장소를 포크합니다.
2. `src/main/resources/messages/MyBundle_ko.properties` 파일에서 번역을 수정합니다.
3. Pull Request를 통해 변경 사항을 제출합니다.

## 라이선스

이 프로젝트는 [Apache 2.0 License](LICENSE)에 따라 배포됩니다.

[gh:intellij-platform-gradle-plugin]: https://github.com/JetBrains/intellij-platform-gradle-plugin
