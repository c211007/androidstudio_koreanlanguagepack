# 번역이 적용되는 원리와, 여기까지 오게 된 과정

이 문서는 "번역 파일은 다 채웠는데 왜 Android Studio 화면에는 영어가 남아있는가"라는
질문에 답하기 위해 실제로 조사했던 과정과, 그 결과로 만들어진 3단 구조를 정리한다.
나중에 비슷한 문제(새 버전에서 또 안 되는 문자열이 생겼을 때)를 만났을 때 다시 이
과정을 반복하지 않도록 원리 위주로 적는다.

## 1. 증상

`src/main/resources/messages/*.properties` 345개 파일의 키 커버리지는 99% 이상이고
내용도 대부분 한국어로 채워져 있는데, 실제 Android Studio를 켜보면 어떤 메뉴는 한글로
잘 나오고 어떤 메뉴는 영어로 남아있었다. 심지어 같은 File 메뉴 안에서도 "새로 만들기"는
한글, "Open..."은 영어처럼 항목별로 들쭉날쭉했다.

## 2. IntelliJ 플랫폼이 텍스트를 찾는 3가지 경로

Android Studio(IntelliJ 플랫폼)에서 메뉴/버튼 텍스트가 화면에 나타나는 경로는 사실
하나가 아니라 최소 3가지다. 이 프로젝트가 겪은 모든 "왜 안 되지"는 결국 어떤 경로를
타는 문자열인지 착각한 데서 비롯됐다.

### 경로 A — 리소스 번들 키 (정상적인 경우)

```xml
<action id="Foo" class="..."/>   <!-- text=가 없다 -->
```

이렇게 plugin.xml에 `text=`를 아예 안 쓰면, 플랫폼이 자동으로
`action.Foo.text` (그룹은 `group.Foo.text`) 라는 키를 관례에 따라 만들어서
그 플러그인에 등록된 리소스 번들(`messages.ActionsBundle` 등)에서 찾는다.

이 프로젝트는 `messages/*.properties` 파일들을 `plugin.xml`의
`<languageBundle locale="ko">` 확장포인트와 함께 제공해서, IntelliJ가 로케일을
`ko`로 인식했을 때 우리 플러그인의 번들이 우선 적용되게 한다. **File/Edit/View 같은
코어 메뉴가 잘 되는 이유가 이것**이다 — JetBrains가 자기 코드를 짤 때 원래
이 방식(관례적인 키, 인라인 텍스트 없음)을 따랐기 때문이다.

### 경로 B — plugin.xml에 박힌 인라인 텍스트 (번들이 안 통하는 경우)

```xml
<action id="ImportApkAction" class="..." text="Profile or Debug APK...">
```

Android/Compose/NDK 같은 서드파티(Google) 플러그인들은 위처럼 텍스트를
**그냥 XML에 직접 적어버린** 경우가 매우 많다. 공식 문서에 "액션을 지역화하려면
`text`/`description`을 plugin.xml에 쓰지 말고 리소스 번들에 선언하라"고 나와
있는데, 뒤집어 말하면 **인라인으로 써버리면 애초에 번들 키 조회 자체가 발생하지
않는다**는 뜻이다. 그래서 `action.ImportApkAction.text` 키를 아무리 번들 파일에
넣어도 무시된다 — 조회를 안 하니까.

이 카테고리는 `.properties` 파일이 아니라 **코드로** 고쳐야 한다.
[`tools/translation/extract_inline_action_texts.py`](../tools/translation/extract_inline_action_texts.py)가 실제
설치된 Android Studio의 모든 플러그인 jar를 열어서 이런 인라인 `text=`/`description=`
액션·그룹을 전부 찾아내고, [`InlineActionTextOverrides.kt`](../src/main/kotlin/org/jetbrains/plugins/koreanlanguagepack/InlineActionTextOverrides.kt)에
번역을 담아 [`InlineActionTextOverrideApplier`](../src/main/kotlin/org/jetbrains/plugins/koreanlanguagepack/InlineActionTextOverrideApplier.kt)가
IDE 시작 시 `ActionManager.getAction(id).templatePresentation.setText(...)`로
직접 텍스트를 갈아 끼운다.

### 경로 C — update()가 매번 텍스트를 다시 계산하는 경우 (가장 까다로움)

경로 A/B로도 안 잡히는 게 있었다. 예를 들어 `OpenFile`, `Android.GenerateSignedApk`,
`action.android.restore`는 전부 **제대로 번들 키를 쓰는** 정상적인 액션이고,
번들 파일의 값도 정확히 한국어였다. 그런데도 화면에는 영어가 나왔다.

실제 Android Studio 설치 파일(`android.jar` 등)의 바이트코드를 직접 까본 결과,
원인은 이 액션들의 `update(e: AnActionEvent)` 메서드가 **메뉴가 열릴 때마다**
자기 번들 키를 다시 조회해서 `e.presentation.text`에 새로 써넣기 때문이었다.
우리가 시작 시점에 한 번 `templatePresentation`을 바꿔놔도, 실제 화면에 쓰이는
건 `update()`가 매번 새로 만드는 `e.presentation`이라서 우리가 해둔 건
매번 덮어써진다.

`Assemble '{module}' Run Configuration`, `Compile '{module}'`,
`... (disabled: devices not connected)` 같이 **실행 구성/모듈 이름이나 상태가
동적으로 끼워지는 텍스트**도 같은 카테고리다 (경로 A/B라면 애초에 고정된 문자열이라
이런 게 불가능하다).

이건 `.properties`도, 1회성 `setText()`도 못 고친다. 대신
[`DynamicActionTextWrapper`](../src/main/kotlin/org/jetbrains/plugins/koreanlanguagepack/DynamicActionTextWrapper.kt)
(그룹인 경우
[`DynamicActionGroupTextWrapper`](../src/main/kotlin/org/jetbrains/plugins/koreanlanguagepack/DynamicActionGroupTextWrapper.kt))로
원본 액션을 감싸서, `ActionManager.replaceAction(id, wrapper)`로 등록을 바꿔치기한다.
래퍼는 원본의 `update()`를 그대로 실행시켜서(동적으로 끼워지는 이름이나 활성/비활성
상태 등은 원본 로직이 그대로 계산하게 둠) 그 결과 텍스트만 우리 함수
([`DYNAMIC_ACTION_TEXT_TRANSFORMS`](../src/main/kotlin/org/jetbrains/plugins/koreanlanguagepack/DynamicActionTextOverrides.kt))로
후처리해서 한국어로 바꾼다. 이름처럼 매번 달라지는 부분은 정규식으로 캡처해서
그대로 살리고, 나머지 고정된 영어 부분만 치환한다.

**중요한 안전장치**: 경로 B로 번역해둔 397개 액션도 전부 이 방식(래퍼)으로
한 번 더 감싸져 있다. 이유는 경로 B로 등록해도 나중에 알고 보니 경로 C였던
사례(`action.android.restore` 등)가 실제로 여러 개 나왔기 때문이다. 즉 지금은
"1회성 setText"는 최소한의 기본값이고, 실제 방어선은 "매번 강제로 다시 씌우는
래퍼"다.

그리고 `ActionManager.replaceAction()`은 **액션↔그룹을 서로 바꿔치기하는 걸
허용하지 않는다** (`IllegalStateException: cannot replace a group with an
action and vice versa`). 그래서 원본이 `ActionGroup`인지 아닌지 반드시 먼저
확인하고 맞는 래퍼를 골라야 하고, 어느 한 id에서 실패해도 전체가 멈추지 않도록
항목마다 try/catch로 감싸뒀다.

**⚠️ 절대 감싸면 안 되는 액션이 있다 — `ActivateXxxToolWindow`류**: 도구 창을
활성화하는 액션(`com.intellij.ide.actions.ActivateToolWindowAction` 계열)은
`ActionRemoteBehaviorSpecification.Frontend`라는 마커 인터페이스를 구현하고
있다. 우리 범용 `AnActionWrapper`로 감싸면 이 인터페이스가 사라지는데, "보기 >
도구 창" 메뉴를 만드는 플랫폼 코드가 이 인터페이스(또는 유사한 타입 체크)에
의존하는 것으로 보인다. 실제로 `ActivateBuildVariantsToolWindow`를 감쌌더니
메뉴 생성이 깨지면서 전혀 상관없는 `Build` 도구 창까지 메뉴에서 통째로
사라지는 사고가 있었다. 그래서 이 카테고리는
[`DynamicActionTextOverrides.kt`](../src/main/kotlin/org/jetbrains/plugins/koreanlanguagepack/DynamicActionTextOverrides.kt)의
`NEVER_WRAP_ACTION_IDS`에 넣어서 절대 래핑하지 않고, 1회성 `setText()`만
적용한다 (그래서 `update()`가 텍스트를 재계산하는 경우엔 여전히 영어로 보일 수
있지만, 최소한 도구 창 자체가 사라지는 것보다는 낫다). **새로운
`ActivateXxxToolWindow` id를 번역하려 할 때는 절대로
`DYNAMIC_ACTION_TEXT_TRANSFORMS`에 넣지 말고, `NEVER_WRAP_ACTION_IDS`에
먼저 추가해야 한다.**

**⚠️ 재시도 루프는 반드시 `execute()` 밖에서 돌려야 한다**: 프로젝트가 열리고
Gradle 동기화가 끝난 뒤에야 등록되는 액션(Build Variants 등)을 잡으려고 재시도
루프를 넣었는데, 이걸 `ApplicationInitializedListener.execute()` 안에서 그대로
돌렸더니 IDE 시작 시퀀스 자체가 느려지는 사고가 있었다 (`execute()`가 끝날 때까지
IDE가 기다리는 것으로 보임). 그래서 `execute()`는 즉시 반환하는 1회성 작업만 하고,
재시도 루프는 [`KoreanLanguagePackCoroutineScope`](../src/main/kotlin/org/jetbrains/plugins/koreanlanguagepack/KoreanLanguagePackCoroutineScope.kt)
(`@Service(Service.Level.APP)`, 앱 생명주기에 묶인 코루틴 스코프)로 분리해서
백그라운드에서 돌게 했다.

## 3. 파일 구조

| 파일 | 역할 |
|---|---|
| `src/main/resources/messages/*.properties` (345개) | 경로 A. 원본 IntelliJ/Android Studio 리소스 번들의 번역본 |
| `src/main/resources/META-INF/plugin.xml` | `<resource-bundle>` 목록 + `<languageBundle locale="ko">` + `<applicationInitializedListener>` 등록 |
| `tools/translation/extract_inline_action_texts.py` | 설치된 Android Studio의 모든 plugin jar를 스캔해서 경로 B(인라인 text=) 대상을 찾아내는 도구 |
| `tools/translation/apply_action_translations.py`, `tools/translation/action_translations_round2.py` | 경로 B/C 대상 액션 id → 한국어 번역 데이터 (사람이 직접 채워넣는 부분) |
| `tools/translation/generate_action_override_kotlin.py` | 위 두 파이썬 딕셔너리를 병합해서 `InlineActionTextOverrides.kt`를 자동 생성 |
| `InlineActionTextOverrides.kt` | (자동 생성) id → 번역 텍스트/설명 맵 |
| `DynamicActionTextOverrides.kt` | 경로 C 전용: id → "원본 텍스트를 받아 한국어로 변환하는 함수" 맵 + `NEVER_WRAP_ACTION_IDS` (사람이 직접 작성) |
| `InlineActionTextOverrideApplier.kt` | IDE 시작 시 실제로 위 데이터들을 적용하는 진입점 (`ApplicationInitializedListener`) |
| `KoreanLanguagePackCoroutineScope.kt` | 재시도 루프를 앱 시작 시퀀스와 분리해서 돌리기 위한 앱 레벨 코루틴 스코프 서비스 |
| `DynamicActionTextWrapper.kt` / `DynamicActionGroupTextWrapper.kt` | 경로 C를 구현하는 래퍼 (액션용 / 그룹용) — `ActivateXxxToolWindow`류에는 절대 쓰면 안 됨 |
| `UntranslatedActionScanner.kt` | IDE에 등록된 모든 액션·그룹을 실제로 훑어서 "아직 한글이 없는" 것을 찾아 사용자 홈 디렉터리에 리포트를 남기는 진단 도구 |

## 4. 액션 ID를 직접 확인하는 방법 (내부 모드 + UI Inspector)

경로 C를 고치려면 정확한 액션 id가 필요한데, `Activate<도구창ID>ToolWindow`처럼
"관례"만 믿고 추측하면 틀리기 쉽다 (예: 표시 텍스트는 "Build Variants"인데 실제
id는 공백 없는 `ActivateBuildVariantsToolWindow`). 추측 대신 Android Studio에서
직접 확인하는 게 훨씬 빠르고 정확하다.

1. `Help` → `Edit Custom Properties...` 로 `idea.properties`를 열어
   `idea.is.internal=true` 한 줄을 추가하고 재시작한다 (내부 모드 활성화)
2. `Find Action`(`Ctrl+Shift+A` 또는 Shift 두 번)에서 `UI Inspector`를 찾아 실행한다
3. 확인하고 싶은 메뉴 항목을 클릭하면 컴포넌트 정보 창이 뜨는데, 액션으로 만들어진
   항목이면 `Action ID`와 `Action Class` 필드가 그대로 나온다

이렇게 확인한 id를 `DYNAMIC_ACTION_TEXT_TRANSFORMS`/번역 딕셔너리에 그대로 쓰면 된다.
그럴듯한 후보를 여러 개 등록해두는 것도 안전한 방법이다 — 틀린 id는 `ActionManager.getAction()`이
`null`을 반환해서 조용히 무시되기 때문에 부작용이 없다.

## 5. 새로운 미번역 항목을 찾는 방법

정적으로 plugin.xml/코드를 미리 읽는 방식(`extract_inline_action_texts.py`)은
**경로 B만** 잡아낸다. 경로 C(코드에 하드코딩되거나 update()에서 재계산되는
텍스트)는 정적 분석으로는 원천적으로 못 찾는다. 그래서 가장 신뢰할 수 있는
방법은 실제로 IDE를 켜서 확인하는 것이다.

1. `.\gradlew buildPlugin -x test`로 빌드 → 실제(또는 샌드박스) Android Studio에 설치
2. 재시작 후 프로젝트를 열고 20~30초 정도 기다린다
   (`InlineActionTextOverrideApplier`가 시작 시 오버라이드를 적용하고,
   15초 뒤 `UntranslatedActionScanner`가 전체 스캔을 돌린다)
3. `%USERPROFILE%\AndroidStudioKoreanPack_untranslated_actions.txt` 확인
   — 텍스트에 한글이 하나도 없는 액션/그룹 목록이 `id | text | description`
   형식으로 저장된다
4. 목록에서 실제로 고쳐야 할 것과, 의도적으로 영어로 둬야 하는 것을 구분한다
   (아래 7번 참고)

## 6. 새 번역을 추가하는 방법

1. 위 스캐너 결과에서 대상 id/원문 텍스트를 확인한다 (id가 확실하지 않으면
   4번의 UI Inspector로 정확히 확인한다)
2. id가 `Activate`로 시작하고 `ToolWindow`로 끝나면(도구 창 활성화 액션) —
   **절대 래핑하면 안 된다.** `tools/translation/action_translations_round2.py`에
   번역을 추가하는 것까지는 해도 되지만, 곧바로
   [`DynamicActionTextOverrides.kt`](../src/main/kotlin/org/jetbrains/plugins/koreanlanguagepack/DynamicActionTextOverrides.kt)의
   `NEVER_WRAP_ACTION_IDS`에도 그 id를 추가해야 한다 (2번 항목 참고)
3. 나머지 일반적인 경우 `tools/translation/action_translations_round2.py`
   (또는 새 `action_translations_round3.py`를 만들어서)
   `{id: (번역된_text_또는_None, 번역된_description_또는_None)}` 형식으로 추가한다.
   `None`은 "이 필드는 건드리지 않는다"는 뜻이다
   - 실행 구성/모듈 이름처럼 **매번 달라지는 값이 포함된 텍스트**라면
     `action_translations_round2.py`가 아니라 위 `DynamicActionTextOverrides.kt`의
     `DYNAMIC_ACTION_TEXT_TRANSFORMS`에 정규식 기반 변환 함수로 직접 추가한다
   - `tools/translation/generate_action_override_kotlin.py`를 새로 만든 파일
     목록에 맞게 `_load_dict(...)` 호출을 추가해야 한다면 그렇게 한다
4. `python tools/translation/generate_action_override_kotlin.py` 실행 →
   `InlineActionTextOverrides.kt` 재생성
5. 다시 빌드하고, 스캐너 리포트에서 항목이 사라졌는지 + 실제 화면에서 근처
   메뉴/도구 창이 사라지지 않았는지 눈으로 확인한다

## 7. 번역하면 안 되는 것들 (일부러 영어로 남긴 것)

스캐너 결과에는 실제 버그가 아닌 것도 많이 섞여 나온다. 아래는 의도적으로
그대로 둔 카테고리다.

- **코드/기호 리터럴**: `toString()`, `createUI(…)`, `provider()`,
  `methodMissing()`, `CMakeLists.txt`, `module-info.java`, `if`,
  `try / catch` — 다른 언어로 바꾸면 오히려 혼란을 준다
- **고유명사/브랜드명**: `Git`, `GitHub`, `GitLab`, `Kotlin`, `Firebase`,
  `Logcat`, `Markdown`, `TODO`, `Android` 그룹 라벨 등
- **관용적으로 영어를 유지하는 개발 용어**: `Getter`/`Setter` (단독으로 쓰일 때),
  `Worktree`, `Fixup`, `Typedef`, `Watch`/`Watches` — 이 프로젝트의 다른
  번역들도 이미 이 단어들은 영어 그대로 쓰고 있어서 일관성을 맞췄다

## 8. 알려진 한계

- **고정 id 없이 동적으로 생성되는 자식 액션**: 예를 들어 우클릭 메뉴에서
  나오는 `Assemble Module 'app'` 같은 항목은 부모 그룹의 `getChildren()`이
  호출될 때마다 새로 만들어지는 임시 액션 인스턴스라, `ActionManager.getAction(id)`로
  붙잡을 수 있는 고정된 id 자체가 없다. 고치려면 부모 그룹까지 감싸서
  `getChildren()`이 반환하는 액션들을 순회하며 다시 라벨링해야 하는데,
  아직 구현하지 않았다
- **`ActivateXxxToolWindow`류(보기 > 도구 창 메뉴)는 사실상 번역 불가**: 2번의
  안전장치 때문에 이 카테고리는 1회성 `setText()`만 적용되는데, 실제로는
  `update()`가 텍스트를 재계산하는 경우가 많아서(예: `ActivateDebugToolWindow`)
  결국 영어로 남는다. 안전하게 고치려면 마커 인터페이스까지 보존하는 전용
  래퍼를 새로 만들어야 하는데, 아직 시도하지 않았다
- **원인 미확인 항목**: `Select Device...` 등 일부는 아직 어느 경로(B/C)에
  해당하는지, 정확한 id가 무엇인지 특정하지 못했다
- `UntranslatedActionScanner`는 `templatePresentation`을 직접 읽기 때문에,
  경로 C로 래핑된 액션(래퍼가 실제 렌더링 시점의 `update()`에서만 텍스트를
  바꿔치기함)은 스캐너 상으로는 여전히 "영어"로 보일 수 있어 스캔 대상에서
  제외해뒀다. 즉 이 리포트는 "경로 A/B로 이미 처리된 것"과 "전혀 손 안 댄 것"만
  구분해줄 뿐, 실제 화면에 제대로 나오는지는 눈으로 확인해야 한다
