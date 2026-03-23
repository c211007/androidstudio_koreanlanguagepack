package com.github.c211007.androidstudiokoreanlanguagepack

import com.intellij.openapi.actionSystem.AnAction
import com.intellij.openapi.actionSystem.AnActionEvent
import com.intellij.openapi.ui.Messages
import java.util.Locale

class TestLanguagePackAction : AnAction("Test Korean Language Pack") {
    override fun actionPerformed(e: AnActionEvent) {
        val currentLocale = Locale.getDefault()
        val message = """
            Korean Language Pack Status

            Current Locale: ${currentLocale.displayName}
            Language: ${currentLocale.language}
            Country: ${currentLocale.country}

            Plugin is loaded and working!
            플러그인이 로드되었습니다!
        """.trimIndent()

        Messages.showInfoMessage(
            e.project,
            message,
            "Language Pack Test"
        )
    }
}
