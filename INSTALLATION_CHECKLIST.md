# 한국어 언어팩 적용 체크리스트

## ✅ 완료된 사항
1. ✅ 241개의 중복 .properties 파일 삭제 완료
2. ✅ 345개의 _ko.properties 파일만 남음
3. ✅ JAR 파일에 449개의 _ko.properties 포함 확인
4. ✅ plugin.xml에 `<languageBundle locale="ko"/>` 선언 있음
5. ✅ 번역률 99.3% (ActionsBundle 기준)

## 🔧 적용 단계

### 1단계: 클린 빌드 (필수!)
```bash
# 기존 빌드 삭제
.\gradlew clean

# 새로 빌드
.\gradlew buildPlugin -x test
```

### 2단계: 플러그인 설치
1. Android Studio 열기
2. **File > Settings** (Windows/Linux) 또는 **Android Studio > Preferences** (Mac)
3. **Plugins** 메뉴로 이동
4. 톱니바퀴 아이콘 ⚙️ 클릭 → **Install Plugin from Disk...**
5. `build/distributions/androidstudio_koreanlanguagepack-1.0.0.zip` 선택
6. **Restart IDE** 버튼 클릭 (반드시 재시작!)

### 3단계: 언어 설정 변경
1. Android Studio 재시작 후
2. **File > Settings** → **Appearance & Behavior** → **System Settings** → **Language and Region**
3. **Language** 드롭다운에서 **한국어 (Korean)** 선택
4. **OK** 클릭
5. **다시 재시작 (Restart IDE)** - 이 단계가 매우 중요!

### 4단계: 확인
재시작 후 다음을 확인:
- 메뉴 (File, Edit, View 등)가 한국어로 표시되는지
- Settings 창의 텍스트가 한국어인지
- 에러 메시지, 툴팁 등이 한국어인지

## 🚨 문제 해결

### "Korean"이 언어 목록에 없는 경우
1. 플러그인이 제대로 설치되었는지 확인:
   - **File > Settings > Plugins** → "Korean Language Pack" 검색
   - 활성화(Enabled) 상태인지 확인

2. IDE 로그 확인:
   - **Help > Show Log in Explorer/Finder**
   - `idea.log` 파일에서 에러 검색

### 설치했는데도 영어로 표시되는 경우
1. System Locale 확인:
   - **Settings > Appearance & Behavior > System Settings > Language and Region**
   - **Display language:** 가 "Korean"인지 확인
   
2. 완전히 재시작:
   - Android Studio 완전히 종료
   - 다시 실행
   
3. 캐시 초기화:
   - **File > Invalidate Caches...** 
   - **Invalidate and Restart** 선택

### 일부만 한국어로 표시되는 경우
- 정상입니다. 모든 번역이 100%는 아닙니다
- 주요 UI 요소가 한국어로 되어 있으면 성공

## 🔍 디버깅 명령어

### JAR 내부 확인:
```bash
# Windows
jar tf build\libs\androidstudio_koreanlanguagepack-1.0.0.jar | findstr "messages"

# 또는 PowerShell
Add-Type -AssemblyName System.IO.Compression.FileSystem
[System.IO.Compression.ZipFile]::OpenRead("build\libs\androidstudio_koreanlanguagepack-1.0.0.jar").Entries | Where-Object {$_.FullName -like "*messages/*"} | Select-Object FullName
```

### 로그에서 언어팩 로딩 확인:
```
Help > Show Log in Explorer
```
로그에서 "LanguageBundle" 또는 "Korean" 검색

## 📋 예상되는 결과

✅ 메뉴가 한국어로 표시:
- 파일(File) → 파일
- 편집(Edit) → 편집  
- 보기(View) → 보기
- 코드(Code) → 코드
- 실행(Run) → 실행

✅ Settings 창이 한국어로 표시:
- Appearance & Behavior → 모양 및 동작
- Editor → 에디터
- Plugins → 플러그인

날짜: 2026-03-28
