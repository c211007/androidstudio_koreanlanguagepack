package com.github.c211007.androidstudiokoreanlanguagepack

import com.intellij.ide.util.PropertiesComponent
import com.intellij.notification.NotificationGroupManager
import com.intellij.notification.NotificationType
import com.intellij.openapi.actionSystem.AnAction
import com.intellij.openapi.actionSystem.AnActionEvent
import com.intellij.openapi.application.ApplicationManager
import com.intellij.openapi.options.ShowSettingsUtil
import com.intellij.openapi.project.DumbAware
import com.intellij.openapi.project.Project
import com.intellij.openapi.startup.ProjectActivity
import java.util.Locale

/**
 * Korean Language Pack Notifier
 *
 * Shows a notification when the plugin is first loaded, prompting the user
 * to change the IDE language to Korean.
 */
class KoreanLanguagePackNotifier : ProjectActivity, DumbAware {

    companion object {
        private const val NOTIFICATION_SHOWN_KEY = "koreanLanguagePack.notificationShown"
        private const val NOTIFICATION_GROUP_ID = "Korean Language Pack"
    }

    override suspend fun execute(project: Project) {
        // Check if user's language is already Korean
        val currentLocale = Locale.getDefault()
        if (currentLocale.language == "ko") {
            return // Already using Korean, no need to show notification
        }

        // Check if we've already shown the notification
        val properties = PropertiesComponent.getInstance()
        if (properties.getBoolean(NOTIFICATION_SHOWN_KEY, false)) {
            return // Already shown notification before
        }

        // Show notification on the main thread
        ApplicationManager.getApplication().invokeLater {
            showLanguageChangeNotification(project)
            // Mark notification as shown
            properties.setValue(NOTIFICATION_SHOWN_KEY, true)
        }
    }

    private fun showLanguageChangeNotification(project: Project) {
        val notificationGroup = NotificationGroupManager.getInstance()
            .getNotificationGroup(NOTIFICATION_GROUP_ID)

        val notification = notificationGroup.createNotification(
            "한국어 번역 플러그인 감지됨",
            "한국어 언어팩이 설치되었습니다. IDE 언어를 한국어로 변경하시겠습니까?\n" +
                    "Korean Language Pack detected. Would you like to change the IDE language to Korean?",
            NotificationType.INFORMATION
        )

        // Add action to open Language and Region settings
        notification.addAction(object : AnAction("예, 한국어로 변경 (Yes, change to Korean)") {
            override fun actionPerformed(e: AnActionEvent) {
                openLanguageSettings(project)
                notification.expire()
            }
        })

        // Add action to dismiss
        notification.addAction(object : AnAction("나중에 (Later)") {
            override fun actionPerformed(e: AnActionEvent) {
                notification.expire()
            }
        })

        // Add action to never show again
        notification.addAction(object : AnAction("다시 표시 안 함 (Don't show again)") {
            override fun actionPerformed(e: AnActionEvent) {
                notification.expire()
            }
        })

        notification.notify(project)
    }

    private fun openLanguageSettings(project: Project) {
        // Open the Language and Region settings page
        ShowSettingsUtil.getInstance().showSettingsDialog(
            project,
            "preferences.language.and.region"
        )
    }
}
