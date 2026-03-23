# Android Studio 한국어 언어팩 번역 가이드

## 📚 개요

이 프로젝트는 Android Studio의 UI를 한국어로 번역하기 위한 IntelliJ Platform 언어팩입니다.

## 🔧 파일 구조

```
src/main/resources/messages/
├── ActionsBundle_ko.properties      # 메뉴, 액션 (2,885 keys) ⭐ 최우선
├── IdeBundle_ko.properties          # IDE 핵심 메시지 (2,891 keys) ⭐ 최우선
├── AndroidBundle_ko.properties      # Android 관련 (728 keys) ⭐ 최우선
├── ExecutionBundle_ko.properties    # 실행/디버그 (720 keys)
├── CodeInsightBundle_ko.properties  # 코드 완성/분석 (553 keys)
└── ... (기타 70+ 번들 파일들)
```

## 🎯 번역 우선순위

### 1단계: 핵심 UI (필수)
- **ActionsBundle_ko.properties** - 메뉴, 툴바, 액션
- **IdeBundle_ko.properties** - 대화상자, 알림, 기본 UI

### 2단계: Android 특화
- **AndroidBundle_ko.properties** - Android 관련 모든 기능
- **AndroidLintBundle_ko.properties** - Lint 검사 메시지
- **LogcatBundle_ko.properties** - Logcat 도구

### 3단계: 개발 도구
- **ExecutionBundle_ko.properties** - 실행/디버그
- **CodeInsightBundle_ko.properties** - 코드 지능형 기능
- **RefactoringBundle_ko.properties** - 리팩토링
- **FindBundle_ko.properties** - 찾기/바꾸기

### 4단계: 부가 기능
- 나머지 번들 파일들

## 📝 번역 규칙

### 1. 키 명명 규칙

#### Action (액션)
```properties
# 형식: action.<ActionId>.text = 표시 텍스트
action.NewProject.text=새 프로젝트...
action.NewProject.description=새 Android 프로젝트를 만듭니다

# 도구 창 활성화
action.ActivateLogcatToolWindow.text=Logcat
```

#### Group (그룹/메뉴)
```properties
# 형식: group.<GroupId>.text = 메뉴 이름
group.FileMenu.text=파일(&F)
group.EditMenu.text=편집(&E)
```

#### 오류/경고
```properties
# 형식: <문제>.error / <문제>.warning
package.not.found.error=패키지가 매니페스트 파일에 지정되지 않았습니다
cannot.resolve.color.literal.error=색상 ''{0}''을(를) 확인할 수 없습니다
```

#### 다이얼로그/명령
```properties
# 형식: <기능>.dialog.title / <기능>.command.name
new.resource.dialog.title=새 리소스 파일
new.resource.command.name=새 리소스 파일
```

### 2. 번역 스타일 가이드

#### 단축키 표시 (Mnemonics)
```properties
# 영문
File(&F) → 파일(&F)
Edit(&E) → 편집(&E)
View(&V) → 보기(&V)

# 한국어 첫 자음에 맞게 조정
Build(&B) → 빌드(&B)
Run(&R) → 실행(&R)
```

#### 말줄임표 (Ellipsis)
```properties
# 추가 입력이 필요한 경우 ... 유지
Open... → 열기...
New Project... → 새 프로젝트...
Settings... → 설정...

# 즉시 실행되는 경우 ... 제거
Save → 저장
Close → 닫기
```

#### 플레이스홀더
```properties
# {0}, {1}, {2} 등은 그대로 유지
Cannot find {0} class → {0} 클래스를 찾을 수 없습니다
Override Resource in {0} → {0}에서 리소스 오버라이드
```

#### 전문 용어
```properties
# 혼용 가능한 용어
Refactor → 리팩토링 (한글)
Debug → 디버그 (한글)
Commit → 커밋 (한글)
Build → 빌드 (한글)

# 그대로 유지하는 용어
Git, Gradle, APK, SDK, AVD, Logcat, Layout Inspector

# 맥락에 따라
Breakpoint → 중단점
Watch → 조사식
Variable → 변수
```

### 3. 번역 시 주의사항

#### DO ✅
- 키 값은 **절대** 변경하지 마세요
- 자연스러운 한국어 사용
- 일관된 용어 사용 (용어집 참고)
- 맥락에 맞는 번역

#### DON'T ❌
- 직역하지 마세요
- 너무 길게 번역하지 마세요 (UI 공간 제한)
- 문체를 혼용하지 마세요 (존댓말/반말)
- 기술 용어를 과도하게 한글화하지 마세요

## 🔨 작업 흐름

### 1. 원본 keys 확인
```bash
# 특정 번들의 모든 키 확인
cat extracted_keys/ActionsBundle_keys.txt
```

### 2. 번역 작업
```properties
# src/main/resources/messages/ActionsBundle_ko.properties

# 파일 메뉴
action.NewProject.text=새 프로젝트...
action.OpenFile.text=열기...
action.SaveAll.text=모두 저장
```

### 3. 플러그인 빌드
```bash
./gradlew buildPlugin
```

### 4. 테스트
1. Android Studio 실행
2. Settings → Appearance & Behavior → Language and Region
3. Korean 선택
4. IDE 재시작

## 📊 진행 상황 추적

### 통계 확인
```bash
python extract_keys.py
```

생성 파일:
- `extracted_keys/all_keys.txt` - 전체 키 목록 (16,358개)
- `extracted_keys/bundle_stats.txt` - 번들별 키 개수
- `extracted_keys/key_analysis.txt` - 패턴 분석

### 키 패턴 통계
- `action.*`: 3,210개 - 액션/메뉴 항목
- `group.*`: 477개 - 그룹/메뉴
- `*.text`: 2,759개 - 표시 텍스트
- `*.description`: 1,178개 - 도구 설명
- `*.title`: 908개 - 제목
- `*.error`: 198개 - 오류 메시지
- `*.dialog.*`: 489개 - 다이얼로그
- `*.warning`: 34개 - 경고
- `*.intention.*`: 46개 - 인텐션 액션

## 🌐 참고 자료

### JetBrains 공식 번역 가이드
- [IntelliJ Platform Localization Guide](https://plugins.jetbrains.com/docs/intellij/localization-guide.html)

### 기존 한국어 언어팩
- [IntelliJ IDEA Korean Language Pack](https://plugins.jetbrains.com/plugin/13710-korean-language-pack--)
- JetBrains 공식 한국어 리소스

### 용어 일관성
- 기존 JetBrains 번역 용어 참고
- Android 공식 문서 한국어 용어 사용

## 🚀 빠른 시작

```bash
# 1. 키 추출
python extract_keys.py

# 2. 주요 번들부터 번역 시작
# ActionsBundle_ko.properties 편집

# 3. 빌드 및 테스트
./gradlew buildPlugin
```

## 📞 도움이 필요하신가요?

- Issues: 프로젝트 GitHub Issues
- 참고: `extracted_keys/` 디렉토리의 분석 파일들

---
**Happy Translating! 🎉**
