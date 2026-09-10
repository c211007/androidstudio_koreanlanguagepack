package org.jetbrains.plugins.koreanlanguagepack

import com.intellij.openapi.actionSystem.AnAction
import com.intellij.openapi.actionSystem.AnActionEvent
import com.intellij.openapi.actionSystem.AnActionWrapper

/**
 * 원본 액션의 update()를 그대로 실행시킨 뒤, 그 결과 텍스트를 [transform]으로
 * 다시 한국어로 바꿔치기하는 래퍼. update()에서 스스로 텍스트를 재계산해버리는
 * 액션(OpenFile, GenerateSignedApk, action.android.restore 등)을 고치기 위해 쓴다.
 *
 * [description]이 주어지면 설명도 매번 같은 방식으로 강제 덮어쓴다.
 */
internal class DynamicActionTextWrapper(
    delegate: AnAction,
    private val transform: (String) -> String,
    private val description: String? = null,
) : AnActionWrapper(delegate) {
    override fun update(e: AnActionEvent) {
        super.update(e)
        val currentText = e.presentation.text
        if (currentText != null) {
            e.presentation.setText(transform(currentText), false)
        }
        if (description != null) {
            e.presentation.description = description
        }
    }
}
