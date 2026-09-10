package org.jetbrains.plugins.koreanlanguagepack

import com.intellij.openapi.actionSystem.ActionGroup
import com.intellij.openapi.actionSystem.ActionGroupWrapper
import com.intellij.openapi.actionSystem.AnActionEvent

/**
 * DynamicActionTextWrapper와 같은 역할이지만, 대상이 <group>으로 등록된 경우를 위한 버전.
 * ActionManager.replaceAction()은 액션을 그룹으로(혹은 그 반대로) 바꿔치기하는 걸 허용하지
 * 않기 때문에(IllegalStateException), 원본이 ActionGroup이면 이 래퍼를 대신 써야 한다.
 */
internal class DynamicActionGroupTextWrapper(
    delegate: ActionGroup,
    private val transform: (String) -> String,
    private val description: String? = null,
) : ActionGroupWrapper(delegate) {
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
