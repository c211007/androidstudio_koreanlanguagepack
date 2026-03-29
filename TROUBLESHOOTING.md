# 🔍 한국어 언어팩 작동하지 않을 때 진단 방법

## 1단계: 빌드 및 설치 확인

### 빌드
```bash
.\gradlew clean
.\gradlew buildPlugin -x test
```

### ZIP 파일 확인
```bash
# 빌드 결과 확인
dir build\distributions
# androidstudio_koreanlanguagepack-1.0.0.zip이 생성되어야 함
```

## 2단계: 플러그인 설치

1. Android Studio 실행
2. **File > Settings > Plugins**
3. ⚙️ 클릭 → **Install Plugin from Disk...**
4. `build\distributions\androidstudio_koreanlanguagepack-1.0.0.zip` 선택
5. **OK** → **Restart IDE**

## 3단계: 진단 도구 실행

플러그인이 설치되면 **Tools** 메뉴에 두 개의 테스트 액션이 나타납니다:

### A. Test Korean Language Pack
- 플러그인이 로드되었는지 확인
- "Korean Language Pack is loaded!" 메시지가 표시되어야 함

### B. Korean Language Pack Diagnostics ⭐
- **중요**: 이 도구를 반드시 실행하세요!
- 다음 정보를 표시합니다:
  - 현재 Locale 정보
  - 플러그인 로딩 상태
  - Resource Bundle 로딩 테스트
  - 사용 가능한 번들 목록

**이 진단 결과를 스크린샷으로 캡처해주세요!**

## 4단계: 언어 변경

### 옵션 A: 설정에서 변경 (권장)
1. **File > Settings**
2. **Appearance & Behavior** → **System Settings** → **Language and Region**
3. **Language** 드롭다운에서 **한국어 (Korean)** 선택
4. **OK** → **Restart IDE**

### 옵션 B: VM 옵션으로 강제 설정
만약 Settings에 "Korean"이 나타나지 않으면:

1. **Help > Edit Custom VM Options...**
2. 다음 줄 추가:
   ```
   -Duser.language=ko
   -Duser.country=KR
   ```
3. 저장 후 Android Studio 재시작

## 5단계: 확인

재시작 후 다음을 확인:
- [ ] 메뉴 바 (File, Edit, View)가 한국어인가?
- [ ] Settings 창이 한국어인가?
- [ ] 툴팁이 한국어인가?
- [ ] 에러 메시지가 한국어인가?

## 🚨 여전히 작동하지 않는 경우

### 1. idea.log 확인
**Help > Show Log in Explorer/Finder**
- `idea.log` 파일 열기
- "LanguageBundle", "Korean", "resource bundle" 키워드 검색
- 에러 메시지를 찾아서 공유

### 2. 플러그인 충돌 확인
다른 언어팩 플러그인이 설치되어 있는지 확인:
- **File > Settings > Plugins**
- "Language Pack" 검색
- 다른 언어팩이 있으면 비활성화

### 3. Android Studio 버전 확인
```
Help > About
```
- Build number가 242 이상인지 확인
- 현재 플러그인은 build 242+를 요구합니다

### 4. 캐시 초기화
```
File > Invalidate Caches...
→ Invalidate and Restart
```

## 📊 진단 결과 예시

### 정상 작동하는 경우:
```
=== LOCALE INFORMATION ===
Default Locale: ko_KR
Language: ko
Country: KR

=== PLUGIN INFORMATION ===
Plugin loaded: true
Plugin enabled: true
Plugin version: 1.0.0

=== RESOURCE BUNDLE TEST ===
ActionsBundle loaded: YES
Bundle locale: ko
  action.ContextHelp.text = 컨텍스트 도움말(_x)
  action.RunConfiguration.text = 실행/디버그 구성 선택
  action.ShowIntentionActions.text = 컨텍스트 액션 표시

=== AVAILABLE BUNDLES (Korean) ===
  messages.ActionsBundle: FOUND
  messages.IdeBundle: FOUND
  messages.CommonBundle: FOUND
  messages.AndroidBundle: FOUND
```

### 문제가 있는 경우:
- "ActionsBundle loaded: NO" → 번들 파일이 누락됨
- "Bundle locale: en" → 한국어 버전이 로드되지 않음
- "NOT FOUND" → 해당 번들이 JAR에 없음

## 🔧 고급 디버깅

### JAR 내용 확인
```powershell
# PowerShell에서 실행
Expand-Archive -Path "build\distributions\androidstudio_koreanlanguagepack-1.0.0.zip" -DestinationPath "temp_check"
Expand-Archive -Path "temp_check\androidstudio_koreanlanguagepack\lib\androidstudio_koreanlanguagepack-1.0.0.jar" -DestinationPath "jar_contents"
dir jar_contents\messages\*_ko.properties
```

**449개의 _ko.properties 파일이 있어야 합니다.**

### Resource Bundle 수동 테스트
Android Studio의 **Groovy Console**에서:
```groovy
import java.util.*

// 한국어 리소스 번들 로드 테스트
def bundle = ResourceBundle.getBundle("messages.ActionsBundle", Locale.KOREAN)
println "Locale: ${bundle.locale}"
println "Sample: ${bundle.getString('action.ContextHelp.text')}"
```

실행: **Tools > Groovy Console** → 위 코드 붙여넣기 → Ctrl+Enter

## 📝 보고할 정보

문제가 해결되지 않으면 다음 정보를 제공해주세요:
1. **진단 도구 출력 (전체 텍스트)**
2. **Android Studio 버전** (Help > About)
3. **idea.log에서 "LanguageBundle" 관련 로그**
4. **Settings > Language and Region 스크린샷**

날짜: 2026-03-28
