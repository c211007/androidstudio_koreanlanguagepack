package org.jetbrains.plugins.koreanlanguagepack

/**
 * 일부 액션은 자신의 update()에서 매번 (번들 키를 통해서든, 하드코딩이든) 텍스트를
 * 새로 계산해서 Presentation에 다시 써버린다. 그래서 시작 시점에 한 번 텍스트를
 * 덮어써도 메뉴가 열릴 때마다 원래 영어로 되돌아간다 (예: OpenFile, Android.GenerateSignedApk,
 * AssembleRunConfiguration, CompileGradleModule).
 *
 * 이런 액션은 InlineActionTextOverrideApplier가 DynamicActionTextWrapper로 감싸서,
 * 원본 update()를 그대로 실행시킨 뒤 결과 텍스트를 여기 정의된 함수로 다시 한국어로
 * 바꿔치기한다. 함수는 원본이 만든 텍스트(동적으로 끼워넣은 이름 등 포함)를 받아서
 * 한국어 텍스트를 돌려주며, 패턴이 안 맞으면 원본 텍스트를 그대로 반환해야 한다.
 */
// BaseAction("%s (disabled: %s)")로 만들어지는 배포 액션들의 비활성 사유 번역.
// 알려지지 않은 사유는 원문 그대로 괄호 안에 남겨둔다.
private val DISABLE_REASON_KO: Map<String, String> = mapOf(
    "devices not connected" to "기기가 연결되지 않음",
)

private val DISABLED_SUFFIX_REGEX = Regex("^.+ \\(disabled: (.+)\\)$")

private fun withDisabledSuffix(koreanBaseText: String): (String) -> String = { text ->
    DISABLED_SUFFIX_REGEX.find(text)?.let { m ->
        val reason = m.groupValues[1]
        val reasonKo = DISABLE_REASON_KO[reason] ?: reason
        "$koreanBaseText (비활성화됨: $reasonKo)"
    } ?: koreanBaseText
}

internal val DYNAMIC_ACTION_TEXT_TRANSFORMS: Map<String, (String) -> String> = mapOf(
    "OpenFile" to { _: String -> "열기…" },
    "Android.GenerateSignedApk" to { _: String -> "서명된 앱 번들 또는 APK 생성…" },
    "AssembleRunConfiguration" to { text: String ->
        Regex("^Assemble '(.+)' Run Configuration$").find(text)
            ?.let { "'${it.groupValues[1]}' 실행 구성 빌드(Assemble)" }
            ?: text
    },
    "CompileGradleModule" to { text: String ->
        Regex("^Compile '(.+)'$").find(text)
            ?.let { "'${it.groupValues[1]}' 컴파일" }
            ?: text
    },
    "android.deploy.ApplyChanges" to withDisabledSuffix("변경사항 적용 및 액티비티 재시작"),
    "android.deploy.CodeSwap" to withDisabledSuffix("코드 변경사항 적용"),
    "android.deploy.RunWithoutBuild" to withDisabledSuffix("빌드 없이 실행"),
    "android.deploy.DebugWithoutBuild" to withDisabledSuffix("빌드 없이 디버그"),

    // 주의: ActivateXxxToolWindow류(도구 창 활성화 액션)는 절대 여기 넣지 말 것.
    // 이 액션들은 com.intellij.ide.actions.ActivateToolWindowAction 계열인데
    // ActionRemoteBehaviorSpecification.Frontend라는 마커 인터페이스를 구현하고 있고,
    // 우리 범용 AnActionWrapper로 감싸면 그 인터페이스가 사라져서 "보기 > 도구 창" 메뉴를
    // 만드는 플랫폼 코드가 깨진다 (실제로 겪음: Build Variants를 감쌌더니 Build 도구창
    // 자체가 메뉴에서 사라짐). 이 카테고리는 1회성 setText만으로 만족해야 한다.
)

/**
 * ActivateXxxToolWindow류처럼, 감싸면(wrap) 위험한 것으로 확인된 액션 id 목록.
 * INLINE_ACTION_TEXT_OVERRIDES/DYNAMIC_ACTION_TEXT_TRANSFORMS에 들어있어도
 * InlineActionTextOverrideApplier는 이 목록에 있는 id는 절대 wrap하지 않고
 * 1회성 setText만 적용한다.
 */
internal val NEVER_WRAP_ACTION_IDS: Set<String> = setOf(
    "ActivateDebugToolWindow",
)
