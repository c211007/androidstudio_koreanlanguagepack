// [배포판 미포함 - 개발용 진단 도구] 이 파일은 src/main/kotlin 에 있지 않고
// version_updates/ 에만 보관된다. 마켓플레이스에 올라가는 빌드에는 포함되지 않는다.
// 재사용 방법은 version_updates/README.md의 "UntranslatedActionScanner.kt" 항목 참고.
package org.jetbrains.plugins.koreanlanguagepack

import com.intellij.openapi.actionSystem.ActionManager
import com.intellij.openapi.diagnostic.logger
import java.io.File

/**
 * IDE에 등록된 모든 액션/그룹을 훑어서, 텍스트에 한글이 하나도 없는 것들을 찾아
 * 사용자 홈 디렉터리에 목록 파일로 남긴다.
 *
 * plugin.xml의 인라인 text=, Kotlin/Java 코드에 하드코딩된 문자열, 리소스 번들 키 등
 * 텍스트가 어디서 오는지와 무관하게, "지금 화면에 실제로 표시될 텍스트"를 직접 읽어서
 * 검사하기 때문에 정적 분석으로는 찾을 수 없던 케이스(코드에 박힌 문자열 등)까지 잡아낸다.
 *
 * InlineActionTextOverrideApplier가 먼저 알려진 오버라이드를 적용한 뒤에 호출되므로,
 * 여기 남는 것들은 "아직 우리가 모르는, 여전히 번역이 안 된" 액션들이다.
 */
internal object UntranslatedActionScanner {
    private val LOG = logger<InlineActionTextOverrideApplier>()
    private val HANGUL_REGEX = Regex("[\\uAC00-\\uD7A3]")
    private val LATIN_LETTER_REGEX = Regex("[A-Za-z]")

    fun scanAndWriteReport() {
        val actionManager = ActionManager.getInstance()
        val ids = actionManager.getActionIdList("")

        val untranslated = mutableListOf<Triple<String, String?, String?>>()
        for (id in ids) {
            // 이미 우리가 강제 래핑해서 update() 때마다 한국어로 다시 씌우는 액션들은
            // templatePresentation만 봐서는 여전히 영어로 보이므로(래퍼가 손대는 건
            // 실제 렌더링 시점의 이벤트 Presentation뿐) 스캔 대상에서 제외한다.
            if (id in INLINE_ACTION_TEXT_OVERRIDES || id in DYNAMIC_ACTION_TEXT_TRANSFORMS) continue

            val action = actionManager.getAction(id) ?: continue
            val presentation = action.templatePresentation
            val text = presentation.text
            val description = presentation.description

            val textNeedsTranslation = !text.isNullOrBlank() &&
                LATIN_LETTER_REGEX.containsMatchIn(text) &&
                !HANGUL_REGEX.containsMatchIn(text)
            val descriptionNeedsTranslation = !description.isNullOrBlank() &&
                LATIN_LETTER_REGEX.containsMatchIn(description) &&
                !HANGUL_REGEX.containsMatchIn(description)

            if (textNeedsTranslation || descriptionNeedsTranslation) {
                untranslated.add(Triple(id, text, description))
            }
        }

        untranslated.sortBy { it.first }

        val outFile = File(System.getProperty("user.home"), "AndroidStudioKoreanPack_untranslated_actions.txt")
        outFile.bufferedWriter(Charsets.UTF_8).use { w ->
            w.write("# 총 ${untranslated.size}개 액션/그룹이 아직 한글 번역이 없는 것으로 보입니다.\n")
            w.write("# 형식: id | text | description\n\n")
            for ((id, text, description) in untranslated) {
                w.write("$id | ${text ?: ""} | ${description ?: ""}\n")
            }
        }

        LOG.info("한국어 언어팩: 미번역 의심 액션 ${untranslated.size}건을 ${outFile.absolutePath} 에 기록함")
    }
}
