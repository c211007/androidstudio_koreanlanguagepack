package org.jetbrains.plugins.koreanlanguagepack

import com.intellij.ide.ApplicationInitializedListener
import com.intellij.openapi.actionSystem.ActionGroup
import com.intellij.openapi.actionSystem.ActionManager
import com.intellij.openapi.actionSystem.AnAction
import com.intellij.openapi.components.service
import com.intellij.openapi.diagnostic.logger
import kotlinx.coroutines.delay
import kotlinx.coroutines.launch

/**
 * Android/Compose/NDK 등 다른 플러그인이 plugin.xml에 text=/description= 을 인라인으로
 * 선언한 액션·그룹은 리소스 번들 키(action.<id>.text) 조회 경로를 아예 타지 않기 때문에
 * ActionsBundle.properties에 키를 넣어도 무시된다. 대신 여기서 ActionManager를 통해
 * 등록된 액션의 Presentation 텍스트를 직접 덮어쓴다.
 *
 * Build Variants 같은 일부 도구창 액션은 프로젝트가 열리고 Gradle 동기화가 끝난
 * 뒤에야 등록되기 때문에, 앱 시작 직후 한 번만 시도하면 놓친다. 그래서 못 찾은
 * 액션들은 한동안 주기적으로 재시도하는데, 이 재시도는 execute() 자신을 오래
 * 붙잡아두면 IDE 시작 시퀀스가 느려지므로 별도 백그라운드 코루틴으로 분리한다.
 */
internal class InlineActionTextOverrideApplier : ApplicationInitializedListener {
    override suspend fun execute() {
        val actionManager = ActionManager.getInstance()

        var applied = 0
        var missing = 0
        for ((id, text) in INLINE_ACTION_TEXT_OVERRIDES) {
            val action = actionManager.getAction(id)
            if (action == null) {
                missing++
                continue
            }
            action.templatePresentation.setText(text, true)
            applied++
        }
        for ((id, description) in INLINE_ACTION_DESCRIPTION_OVERRIDES) {
            actionManager.getAction(id)?.templatePresentation?.description = description
        }
        LOG.info("한국어 언어팩: 인라인 액션 텍스트 $applied 건 적용, $missing 건은 아직 액션을 찾지 못함(백그라운드에서 재시도)")

        // execute()는 여기서 바로 반환하고, 오래 걸릴 수 있는 재시도는
        // 앱 생명주기에 묶인 별도 코루틴에서 돌린다.
        //
        // (미번역 액션을 스캔해서 사용자 홈 디렉터리에 리포트를 남기던
        //  UntranslatedActionScanner 호출은 배포판에서 제거했다 - 실사용자에게
        //  불필요한 파일을 만드는 개발용 진단 도구라서. 향후 번역 점검이 필요하면
        //  version_updates/UntranslatedActionScanner.kt 를 다시 src/main/kotlin/
        //  org/jetbrains/plugins/koreanlanguagepack/ 로 옮기고 아래 줄을 복원할 것:
        //  UntranslatedActionScanner.scanAndWriteReport())
        service<KoreanLanguagePackCoroutineScope>().coroutineScope.launch {
            wrapWithRetry(actionManager)
        }
    }

    private suspend fun wrapWithRetry(actionManager: ActionManager) {
        // 일부 액션은 update()가 매번 텍스트를 새로 계산해서 위의 1회성 setText를 덮어써버린다.
        // (예: OpenFile, action.android.restore) 그래서 정적으로 번역해둔 액션 전부를,
        // 이름이 동적으로 끼워지는 것만 빼고 "매번 강제로 다시 씌우는" 래퍼로 감싼다.
        val allTransforms = LinkedHashMap<String, (String) -> String>(DYNAMIC_ACTION_TEXT_TRANSFORMS)
        for ((id, text) in INLINE_ACTION_TEXT_OVERRIDES) {
            allTransforms.putIfAbsent(id) { _ -> text }
        }
        for (id in NEVER_WRAP_ACTION_IDS) {
            allTransforms.remove(id)
        }

        val pendingIds = allTransforms.keys.toMutableSet()
        var wrapped = 0
        var wrapFailed = 0

        fun tryWrap(id: String): Boolean {
            val original = actionManager.getAction(id) ?: return false
            if (original is DynamicActionTextWrapper || original is DynamicActionGroupTextWrapper) return true
            val transform = allTransforms.getValue(id)
            try {
                val description = INLINE_ACTION_DESCRIPTION_OVERRIDES[id]
                val replacement: AnAction = if (original is ActionGroup) {
                    DynamicActionGroupTextWrapper(original, transform, description)
                } else {
                    DynamicActionTextWrapper(original, transform, description)
                }
                actionManager.replaceAction(id, replacement)
                wrapped++
            } catch (e: Exception) {
                wrapFailed++
                LOG.warn("한국어 언어팩: '$id' 액션 래핑 실패", e)
            }
            return true
        }

        var attempt = 0
        while (pendingIds.isNotEmpty() && attempt < MAX_RETRY_ATTEMPTS) {
            val iterator = pendingIds.iterator()
            while (iterator.hasNext()) {
                if (tryWrap(iterator.next())) iterator.remove()
            }
            if (pendingIds.isEmpty()) break
            attempt++
            delay(RETRY_INTERVAL_MS)
        }

        LOG.info(
            "한국어 언어팩: 강제 래핑 $wrapped 건, 래핑 실패 $wrapFailed 건, " +
                "${attempt}번 재시도 후에도 못 찾은 액션 ${pendingIds.size}건: $pendingIds"
        )
    }

    companion object {
        private val LOG = logger<InlineActionTextOverrideApplier>()
        private const val MAX_RETRY_ATTEMPTS = 20
        private const val RETRY_INTERVAL_MS = 15_000L
    }
}
