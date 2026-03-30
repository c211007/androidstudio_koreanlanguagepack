package com.github.c211007.androidstudiokoreanlanguagepack

import com.intellij.DynamicBundle
import com.intellij.ide.plugins.PluginManagerCore
import com.intellij.openapi.actionSystem.AnAction
import com.intellij.openapi.actionSystem.AnActionEvent
import com.intellij.openapi.extensions.PluginId
import com.intellij.openapi.ui.Messages
import java.util.*

/**
 * Diagnostic action to check language pack loading status
 */
class DiagnosticAction : AnAction("Korean Language Pack Diagnostics") {

    override fun actionPerformed(e: AnActionEvent) {
        val sb = StringBuilder()
        
        // 1. Check system locale
        sb.appendLine("=== LOCALE INFORMATION ===")
        sb.appendLine("Default Locale: ${Locale.getDefault()}")
        sb.appendLine("Language: ${Locale.getDefault().language}")
        sb.appendLine("Country: ${Locale.getDefault().country}")
        sb.appendLine()
        
        // 2. Check plugin status
        sb.appendLine("=== PLUGIN INFORMATION ===")
        val pluginId = PluginId.getId("com.github.c211007.androidstudiokoreanlanguagepack")
        val plugin = PluginManagerCore.getPlugin(pluginId)
        sb.appendLine("Plugin loaded: ${plugin != null}")
        if (plugin != null) {
            sb.appendLine("Plugin enabled: ${plugin.isEnabled}")
            sb.appendLine("Plugin version: ${plugin.version}")
        }
        sb.appendLine()
        
        // 3. Test resource bundle loading
        sb.appendLine("=== RESOURCE BUNDLE TEST ===")
        try {
            val bundle = ResourceBundle.getBundle("messages.ActionsBundle", Locale.KOREAN)
            sb.appendLine("ActionsBundle loaded: YES")
            sb.appendLine("Bundle locale: ${bundle.locale}")
            
            // Try to get a sample key
            val testKeys = listOf(
                "action.ContextHelp.text",
                "action.RunConfiguration.text",
                "action.ShowIntentionActions.text"
            )
            
            for (key in testKeys) {
                try {
                    val value = bundle.getString(key)
                    sb.appendLine("  $key = $value")
                } catch (ex: MissingResourceException) {
                    sb.appendLine("  $key = [MISSING]")
                }
            }
        } catch (ex: Exception) {
            sb.appendLine("ActionsBundle loading FAILED: ${ex.message}")
        }
        sb.appendLine()
        
        // 4. Check available resource bundles
        sb.appendLine("=== AVAILABLE BUNDLES (Korean) ===")
        val bundleNames = listOf(
            "messages.ActionsBundle",
            "messages.IdeBundle",
            "messages.CommonBundle",
            "messages.AndroidBundle"
        )
        
        for (bundleName in bundleNames) {
            try {
                ResourceBundle.getBundle(bundleName, Locale.KOREAN)
                sb.appendLine("  $bundleName: FOUND")
            } catch (ex: Exception) {
                sb.appendLine("  $bundleName: NOT FOUND")
            }
        }
        
        // Show results
        Messages.showMessageDialog(
            e.project,
            sb.toString(),
            "Korean Language Pack Diagnostics",
            Messages.getInformationIcon()
        )
    }
}
