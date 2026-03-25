# 플러그인별 변경사항

이 폴더는 Android Studio에 추가 설치된 플러그인들의 한국어 번역을 관리합니다.

## 폴더 구조

```
plugins/
├── kotlin-plugin/          # Kotlin 플러그인
│   ├── README.md          # 플러그인 정보 및 설치 방법
│   ├── plugin-info.json   # 플러그인 메타데이터
│   └── bundles/           # properties 파일들
│       ├── KotlinBundle.properties
│       └── ...
├── flutter-plugin/         # Flutter 플러그인
│   └── ...
└── PLUGINS.md             # 전체 플러그인 목록 및 상태
```

## 플러그인 추가 방법

### 1. 플러그인 폴더 생성
```bash
mkdir version_updates/plugins/plugin-name
cd version_updates/plugins/plugin-name
```

### 2. 플러그인 정보 파일 작성 (plugin-info.json)
```json
{
  "id": "org.jetbrains.kotlin",
  "name": "Kotlin Plugin",
  "version": "1.9.0",
  "description": "Kotlin language support for Android Studio",
  "vendor": "JetBrains",
  "installationPath": "plugins/Kotlin",
  "propertiesFiles": [
    "KotlinBundle.properties",
    "KotlinJvmBundle.properties"
  ],
  "status": "in_progress",
  "translationProgress": 45
}
```

### 3. 플러그인에서 properties 파일 추출

#### 방법 1: 플러그인 jar에서 추출
```bash
# 플러그인 설치 경로 찾기
PLUGIN_PATH="~/.AndroidStudio/config/plugins/Kotlin"

# jar 파일에서 properties 추출
find "$PLUGIN_PATH" -name "*.jar" -exec jar tf {} \; | grep .properties

# 추출
mkdir bundles
for jar in $(find "$PLUGIN_PATH" -name "*.jar"); do
  jar xf "$jar" messages/ 2>/dev/null
done
mv messages/* bundles/
```

#### 방법 2: 자동 추출 스크립트 (향후 개발)
```bash
python scripts/extract_plugin_properties.py --plugin-id="org.jetbrains.kotlin"
```

### 4. README.md 작성
```markdown
# Kotlin Plugin 한국어 번역

## 플러그인 정보
- **ID**: org.jetbrains.kotlin
- **버전**: 1.9.0
- **벤더**: JetBrains
- **설명**: Kotlin language support for Android Studio

## Properties 파일 목록
- `KotlinBundle.properties` - Kotlin 기본 메시지 (350 keys)
- `KotlinJvmBundle.properties` - JVM 관련 메시지 (120 keys)

## 번역 상태
- [x] KotlinBundle.properties (100%)
- [ ] KotlinJvmBundle.properties (45%)

## 설치 및 테스트
1. 플러그인 jar 파일 경로: `~/.AndroidStudio/config/plugins/Kotlin`
2. 번역 적용 방법: 메인 plugin.xml에 resource-bundle 추가
3. 테스트 체크리스트:
   - [ ] Kotlin 파일 생성 메뉴
   - [ ] 코드 완성 메시지
   - [ ] 오류 메시지

## 주의사항
- Kotlin 플러그인은 Android Studio와 별도로 업데이트됨
- 플러그인 버전에 따라 키가 변경될 수 있음
```

### 5. 메인 plugin.xml에 추가
```xml
<!-- Kotlin Plugin Bundles -->
<resource-bundle>messages.KotlinBundle</resource-bundle>
<resource-bundle>messages.KotlinJvmBundle</resource-bundle>
```

### 6. 번역 작업
```bash
# properties 파일을 src/main/resources/messages로 복사
cp bundles/*.properties ../../src/main/resources/messages/

# 번역 작업
python scripts/generate_translations.py --files="KotlinBundle.properties"
```

## 지원하는 주요 플러그인

### 공식 플러그인
- **Kotlin** - Kotlin 언어 지원
- **Gradle** - Gradle 빌드 시스템
- **Git** - Git 버전 관리
- **Terminal** - 내장 터미널

### Android 관련 플러그인
- **Flutter** - Flutter 개발 지원
- **React Native** - React Native 개발 지원
- **Firebase** - Firebase 통합

### 기타 인기 플러그인
- **Database Navigator** - 데이터베이스 관리
- **Rainbow Brackets** - 괄호 색상 구분
- **GitToolBox** - Git 향상 도구

## 플러그인 우선순위

### 1순위: Android Studio 기본 제공 플러그인
- Android 개발에 필수적인 플러그인
- 대부분의 사용자가 사용

### 2순위: 공식 JetBrains 플러그인
- Kotlin, Gradle 등
- 널리 사용되는 플러그인

### 3순위: 커뮤니티 인기 플러그인
- 다운로드 수가 많은 플러그인
- 사용자 요청이 있는 플러그인

## 플러그인 상태 추적

`PLUGINS.md` 파일에서 모든 플러그인의 번역 상태를 추적:

```markdown
| 플러그인 | 버전 | 파일 수 | 키 개수 | 번역 진행률 | 상태 |
|---------|------|---------|---------|-------------|------|
| Kotlin  | 1.9.0 | 2      | 470     | 100%        | ✅ 완료 |
| Flutter | 3.0.0 | 5      | 1200    | 45%         | 🔄 진행중 |
| Gradle  | 8.0.0 | 3      | 320     | 0%          | 📝 계획 |
```

## 자동화 스크립트 (향후 개발 예정)

- `detect_plugins.py` - 설치된 플러그인 자동 감지
- `extract_plugin_properties.py` - 플러그인에서 properties 자동 추출
- `check_plugin_updates.py` - 플러그인 업데이트 확인
- `merge_plugin_translations.py` - 플러그인 번역 병합

## 주의사항

1. **의존성**: 플러그인이 Android Studio 버전에 의존할 수 있음
2. **업데이트**: 플러그인은 별도로 업데이트되므로 주기적인 확인 필요
3. **호환성**: 번역이 Android Studio 버전과 호환되는지 테스트
4. **라이선스**: 각 플러그인의 라이선스 확인 필요

## 기여 가이드

새로운 플러그인 번역을 추가하려면:
1. 해당 플러그인 폴더 생성
2. `plugin-info.json` 작성
3. Properties 파일 추출
4. README.md 작성
5. 번역 작업
6. Pull Request 생성

## 리소스

- [JetBrains 플러그인 마켓플레이스](https://plugins.jetbrains.com/)
- [Android Studio 플러그인 개발 가이드](https://developer.android.com/studio/plugins)
- [IntelliJ Platform SDK](https://plugins.jetbrains.com/docs/intellij/welcome.html)
