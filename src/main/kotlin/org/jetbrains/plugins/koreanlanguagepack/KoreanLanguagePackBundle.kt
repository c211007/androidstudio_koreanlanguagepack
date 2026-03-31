package org.jetbrains.plugins.koreanlanguagepack

import com.intellij.DynamicBundle
import org.jetbrains.annotations.Nls
import org.jetbrains.annotations.NonNls
import org.jetbrains.annotations.PropertyKey
import java.util.function.Supplier

/**
 * Android Studio 한국어 언어팩 번들 클래스 모음
 * 
 * JetBrains 공식 가이드에 따른 구현:
 * https://plugins.jetbrains.com/docs/intellij/internationalization.html
 * 
 * 자동 생성됨 - 총 345개 번들
 */

// ============================================================================
// ActionsBundle
// ============================================================================
@NonNls
private const val ACTIONS_BUNDLE = "messages.ActionsBundle"

internal object ActionsBundle {
    private val INSTANCE = DynamicBundle(ActionsBundle::class.java, ACTIONS_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = ACTIONS_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = ACTIONS_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// ActionsDeprecatedMessagesBundle
// ============================================================================
@NonNls
private const val ACTIONS_DEPRECATED_MESSAGES_BUNDLE = "messages.ActionsDeprecatedMessagesBundle"

internal object ActionsDeprecatedMessagesBundle {
    private val INSTANCE = DynamicBundle(ActionsDeprecatedMessagesBundle::class.java, ACTIONS_DEPRECATED_MESSAGES_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = ACTIONS_DEPRECATED_MESSAGES_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = ACTIONS_DEPRECATED_MESSAGES_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// AgentsCoreBundle
// ============================================================================
@NonNls
private const val AGENTS_CORE_BUNDLE = "messages.AgentsCoreBundle"

internal object AgentsCoreBundle {
    private val INSTANCE = DynamicBundle(AgentsCoreBundle::class.java, AGENTS_CORE_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = AGENTS_CORE_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = AGENTS_CORE_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// AgpUpgradeBundle
// ============================================================================
@NonNls
private const val AGP_UPGRADE_BUNDLE = "messages.AgpUpgradeBundle"

internal object AgpUpgradeBundle {
    private val INSTANCE = DynamicBundle(AgpUpgradeBundle::class.java, AGP_UPGRADE_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = AGP_UPGRADE_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = AGP_UPGRADE_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// AgreementsBundle
// ============================================================================
@NonNls
private const val AGREEMENTS_BUNDLE = "messages.AgreementsBundle"

internal object AgreementsBundle {
    private val INSTANCE = DynamicBundle(AgreementsBundle::class.java, AGREEMENTS_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = AGREEMENTS_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = AGREEMENTS_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// AnalysisBundle
// ============================================================================
@NonNls
private const val ANALYSIS_BUNDLE = "messages.AnalysisBundle"

internal object AnalysisBundle {
    private val INSTANCE = DynamicBundle(AnalysisBundle::class.java, ANALYSIS_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = ANALYSIS_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = ANALYSIS_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// AndroidAdbUiBundle
// ============================================================================
@NonNls
private const val ANDROID_ADB_UI_BUNDLE = "messages.AndroidAdbUiBundle"

internal object AndroidAdbUiBundle {
    private val INSTANCE = DynamicBundle(AndroidAdbUiBundle::class.java, ANDROID_ADB_UI_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = ANDROID_ADB_UI_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = ANDROID_ADB_UI_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// AndroidBundle
// ============================================================================
@NonNls
private const val ANDROID_BUNDLE = "messages.AndroidBundle"

internal object AndroidBundle {
    private val INSTANCE = DynamicBundle(AndroidBundle::class.java, ANDROID_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = ANDROID_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = ANDROID_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// AndroidDesignerActionsBundle
// ============================================================================
@NonNls
private const val ANDROID_DESIGNER_ACTIONS_BUNDLE = "messages.AndroidDesignerActionsBundle"

internal object AndroidDesignerActionsBundle {
    private val INSTANCE = DynamicBundle(AndroidDesignerActionsBundle::class.java, ANDROID_DESIGNER_ACTIONS_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = ANDROID_DESIGNER_ACTIONS_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = ANDROID_DESIGNER_ACTIONS_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// AndroidExecutionBundle
// ============================================================================
@NonNls
private const val ANDROID_EXECUTION_BUNDLE = "messages.AndroidExecutionBundle"

internal object AndroidExecutionBundle {
    private val INSTANCE = DynamicBundle(AndroidExecutionBundle::class.java, ANDROID_EXECUTION_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = ANDROID_EXECUTION_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = ANDROID_EXECUTION_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// AndroidLintBundle
// ============================================================================
@NonNls
private const val ANDROID_LINT_BUNDLE = "messages.AndroidLintBundle"

internal object AndroidLintBundle {
    private val INSTANCE = DynamicBundle(AndroidLintBundle::class.java, ANDROID_LINT_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = ANDROID_LINT_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = ANDROID_LINT_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// AndroidNdkBundle
// ============================================================================
@NonNls
private const val ANDROID_NDK_BUNDLE = "messages.AndroidNdkBundle"

internal object AndroidNdkBundle {
    private val INSTANCE = DynamicBundle(AndroidNdkBundle::class.java, ANDROID_NDK_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = ANDROID_NDK_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = ANDROID_NDK_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// AndroidRunBundle
// ============================================================================
@NonNls
private const val ANDROID_RUN_BUNDLE = "messages.AndroidRunBundle"

internal object AndroidRunBundle {
    private val INSTANCE = DynamicBundle(AndroidRunBundle::class.java, ANDROID_RUN_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = ANDROID_RUN_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = ANDROID_RUN_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// AndroidTestBundle
// ============================================================================
@NonNls
private const val ANDROID_TEST_BUNDLE = "messages.AndroidTestBundle"

internal object AndroidTestBundle {
    private val INSTANCE = DynamicBundle(AndroidTestBundle::class.java, ANDROID_TEST_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = ANDROID_TEST_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = ANDROID_TEST_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// AndroidWearPairingBundle
// ============================================================================
@NonNls
private const val ANDROID_WEAR_PAIRING_BUNDLE = "messages.AndroidWearPairingBundle"

internal object AndroidWearPairingBundle {
    private val INSTANCE = DynamicBundle(AndroidWearPairingBundle::class.java, ANDROID_WEAR_PAIRING_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = ANDROID_WEAR_PAIRING_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = ANDROID_WEAR_PAIRING_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// ApkAnalyzerBundle
// ============================================================================
@NonNls
private const val APK_ANALYZER_BUNDLE = "messages.ApkAnalyzerBundle"

internal object ApkAnalyzerBundle {
    private val INSTANCE = DynamicBundle(ApkAnalyzerBundle::class.java, APK_ANALYZER_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = APK_ANALYZER_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = APK_ANALYZER_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// AppInspectionBundle
// ============================================================================
@NonNls
private const val APP_INSPECTION_BUNDLE = "messages.AppInspectionBundle"

internal object AppInspectionBundle {
    private val INSTANCE = DynamicBundle(AppInspectionBundle::class.java, APP_INSPECTION_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = APP_INSPECTION_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = APP_INSPECTION_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// AppInspectorBundle
// ============================================================================
@NonNls
private const val APP_INSPECTOR_BUNDLE = "messages.AppInspectorBundle"

internal object AppInspectorBundle {
    private val INSTANCE = DynamicBundle(AppInspectorBundle::class.java, APP_INSPECTOR_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = APP_INSPECTOR_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = APP_INSPECTOR_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// ApplicationBundle
// ============================================================================
@NonNls
private const val APPLICATION_BUNDLE = "messages.ApplicationBundle"

internal object ApplicationBundle {
    private val INSTANCE = DynamicBundle(ApplicationBundle::class.java, APPLICATION_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = APPLICATION_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = APPLICATION_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// BackgroundTaskInspectorBundle
// ============================================================================
@NonNls
private const val BACKGROUND_TASK_INSPECTOR_BUNDLE = "messages.BackgroundTaskInspectorBundle"

internal object BackgroundTaskInspectorBundle {
    private val INSTANCE = DynamicBundle(BackgroundTaskInspectorBundle::class.java, BACKGROUND_TASK_INSPECTOR_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = BACKGROUND_TASK_INSPECTOR_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = BACKGROUND_TASK_INSPECTOR_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// BackupBundle
// ============================================================================
@NonNls
private const val BACKUP_BUNDLE = "messages.BackupBundle"

internal object BackupBundle {
    private val INSTANCE = DynamicBundle(BackupBundle::class.java, BACKUP_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = BACKUP_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = BACKUP_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// BookmarkBundle
// ============================================================================
@NonNls
private const val BOOKMARK_BUNDLE = "messages.BookmarkBundle"

internal object BookmarkBundle {
    private val INSTANCE = DynamicBundle(BookmarkBundle::class.java, BOOKMARK_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = BOOKMARK_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = BOOKMARK_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// BootstrapBundle
// ============================================================================
@NonNls
private const val BOOTSTRAP_BUNDLE = "messages.BootstrapBundle"

internal object BootstrapBundle {
    private val INSTANCE = DynamicBundle(BootstrapBundle::class.java, BOOTSTRAP_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = BOOTSTRAP_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = BOOTSTRAP_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// build
// ============================================================================
@NonNls
private const val BUILD = "messages.build"

internal object build {
    private val INSTANCE = DynamicBundle(build::class.java, BUILD)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = BUILD) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = BUILD) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// BuildBundle
// ============================================================================
@NonNls
private const val BUILD_BUNDLE = "messages.BuildBundle"

internal object BuildBundle {
    private val INSTANCE = DynamicBundle(BuildBundle::class.java, BUILD_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = BUILD_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = BUILD_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// BuiltInServerBundle
// ============================================================================
@NonNls
private const val BUILT_IN_SERVER_BUNDLE = "messages.BuiltInServerBundle"

internal object BuiltInServerBundle {
    private val INSTANCE = DynamicBundle(BuiltInServerBundle::class.java, BUILT_IN_SERVER_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = BUILT_IN_SERVER_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = BUILT_IN_SERVER_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// CidrAsmBundle
// ============================================================================
@NonNls
private const val CIDR_ASM_BUNDLE = "messages.CidrAsmBundle"

internal object CidrAsmBundle {
    private val INSTANCE = DynamicBundle(CidrAsmBundle::class.java, CIDR_ASM_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = CIDR_ASM_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = CIDR_ASM_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// CidrDapBundle
// ============================================================================
@NonNls
private const val CIDR_DAP_BUNDLE = "messages.CidrDapBundle"

internal object CidrDapBundle {
    private val INSTANCE = DynamicBundle(CidrDapBundle::class.java, CIDR_DAP_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = CIDR_DAP_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = CIDR_DAP_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// CidrDebuggerBackendBundle
// ============================================================================
@NonNls
private const val CIDR_DEBUGGER_BACKEND_BUNDLE = "messages.CidrDebuggerBackendBundle"

internal object CidrDebuggerBackendBundle {
    private val INSTANCE = DynamicBundle(CidrDebuggerBackendBundle::class.java, CIDR_DEBUGGER_BACKEND_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = CIDR_DEBUGGER_BACKEND_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = CIDR_DEBUGGER_BACKEND_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// CidrDebuggerBundle
// ============================================================================
@NonNls
private const val CIDR_DEBUGGER_BUNDLE = "messages.CidrDebuggerBundle"

internal object CidrDebuggerBundle {
    private val INSTANCE = DynamicBundle(CidrDebuggerBundle::class.java, CIDR_DEBUGGER_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = CIDR_DEBUGGER_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = CIDR_DEBUGGER_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// CidrExecutionBundle
// ============================================================================
@NonNls
private const val CIDR_EXECUTION_BUNDLE = "messages.CidrExecutionBundle"

internal object CidrExecutionBundle {
    private val INSTANCE = DynamicBundle(CidrExecutionBundle::class.java, CIDR_EXECUTION_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = CIDR_EXECUTION_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = CIDR_EXECUTION_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// CidrLangBundle
// ============================================================================
@NonNls
private const val CIDR_LANG_BUNDLE = "messages.CidrLangBundle"

internal object CidrLangBundle {
    private val INSTANCE = DynamicBundle(CidrLangBundle::class.java, CIDR_LANG_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = CIDR_LANG_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = CIDR_LANG_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// CidrProjectModelBundle
// ============================================================================
@NonNls
private const val CIDR_PROJECT_MODEL_BUNDLE = "messages.CidrProjectModelBundle"

internal object CidrProjectModelBundle {
    private val INSTANCE = DynamicBundle(CidrProjectModelBundle::class.java, CIDR_PROJECT_MODEL_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = CIDR_PROJECT_MODEL_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = CIDR_PROJECT_MODEL_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// CidrRunnerBundle
// ============================================================================
@NonNls
private const val CIDR_RUNNER_BUNDLE = "messages.CidrRunnerBundle"

internal object CidrRunnerBundle {
    private val INSTANCE = DynamicBundle(CidrRunnerBundle::class.java, CIDR_RUNNER_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = CIDR_RUNNER_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = CIDR_RUNNER_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// CidrTestBundle
// ============================================================================
@NonNls
private const val CIDR_TEST_BUNDLE = "messages.CidrTestBundle"

internal object CidrTestBundle {
    private val INSTANCE = DynamicBundle(CidrTestBundle::class.java, CIDR_TEST_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = CIDR_TEST_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = CIDR_TEST_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// CidrUtilsBundle
// ============================================================================
@NonNls
private const val CIDR_UTILS_BUNDLE = "messages.CidrUtilsBundle"

internal object CidrUtilsBundle {
    private val INSTANCE = DynamicBundle(CidrUtilsBundle::class.java, CIDR_UTILS_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = CIDR_UTILS_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = CIDR_UTILS_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// CidrUtilsExecutionBundle
// ============================================================================
@NonNls
private const val CIDR_UTILS_EXECUTION_BUNDLE = "messages.CidrUtilsExecutionBundle"

internal object CidrUtilsExecutionBundle {
    private val INSTANCE = DynamicBundle(CidrUtilsExecutionBundle::class.java, CIDR_UTILS_EXECUTION_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = CIDR_UTILS_EXECUTION_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = CIDR_UTILS_EXECUTION_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// CidrUtilUiBundle
// ============================================================================
@NonNls
private const val CIDR_UTIL_UI_BUNDLE = "messages.CidrUtilUiBundle"

internal object CidrUtilUiBundle {
    private val INSTANCE = DynamicBundle(CidrUtilUiBundle::class.java, CIDR_UTIL_UI_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = CIDR_UTIL_UI_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = CIDR_UTIL_UI_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// CidrWorkspaceBundle
// ============================================================================
@NonNls
private const val CIDR_WORKSPACE_BUNDLE = "messages.CidrWorkspaceBundle"

internal object CidrWorkspaceBundle {
    private val INSTANCE = DynamicBundle(CidrWorkspaceBundle::class.java, CIDR_WORKSPACE_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = CIDR_WORKSPACE_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = CIDR_WORKSPACE_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// ClangdBundle
// ============================================================================
@NonNls
private const val CLANGD_BUNDLE = "messages.ClangdBundle"

internal object ClangdBundle {
    private val INSTANCE = DynamicBundle(ClangdBundle::class.java, CLANGD_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = CLANGD_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = CLANGD_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// ClangFormatBundle
// ============================================================================
@NonNls
private const val CLANG_FORMAT_BUNDLE = "messages.ClangFormatBundle"

internal object ClangFormatBundle {
    private val INSTANCE = DynamicBundle(ClangFormatBundle::class.java, CLANG_FORMAT_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = CLANG_FORMAT_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = CLANG_FORMAT_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// CloudBundle
// ============================================================================
@NonNls
private const val CLOUD_BUNDLE = "messages.CloudBundle"

internal object CloudBundle {
    private val INSTANCE = DynamicBundle(CloudBundle::class.java, CLOUD_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = CLOUD_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = CLOUD_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// CloudsBundle
// ============================================================================
@NonNls
private const val CLOUDS_BUNDLE = "messages.CloudsBundle"

internal object CloudsBundle {
    private val INSTANCE = DynamicBundle(CloudsBundle::class.java, CLOUDS_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = CLOUDS_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = CLOUDS_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// CodeInsightBundle
// ============================================================================
@NonNls
private const val CODE_INSIGHT_BUNDLE = "messages.CodeInsightBundle"

internal object CodeInsightBundle {
    private val INSTANCE = DynamicBundle(CodeInsightBundle::class.java, CODE_INSIGHT_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = CODE_INSIGHT_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = CODE_INSIGHT_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// CodeStyleBundle
// ============================================================================
@NonNls
private const val CODE_STYLE_BUNDLE = "messages.CodeStyleBundle"

internal object CodeStyleBundle {
    private val INSTANCE = DynamicBundle(CodeStyleBundle::class.java, CODE_STYLE_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = CODE_STYLE_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = CODE_STYLE_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// CodeVisionBundle
// ============================================================================
@NonNls
private const val CODE_VISION_BUNDLE = "messages.CodeVisionBundle"

internal object CodeVisionBundle {
    private val INSTANCE = DynamicBundle(CodeVisionBundle::class.java, CODE_VISION_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = CODE_VISION_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = CODE_VISION_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// CollaborationToolsBundle
// ============================================================================
@NonNls
private const val COLLABORATION_TOOLS_BUNDLE = "messages.CollaborationToolsBundle"

internal object CollaborationToolsBundle {
    private val INSTANCE = DynamicBundle(CollaborationToolsBundle::class.java, COLLABORATION_TOOLS_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = COLLABORATION_TOOLS_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = COLLABORATION_TOOLS_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// CommonBundle
// ============================================================================
@NonNls
private const val COMMON_BUNDLE = "messages.CommonBundle"

internal object CommonBundle {
    private val INSTANCE = DynamicBundle(CommonBundle::class.java, COMMON_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = COMMON_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = COMMON_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// CommonFeedbackMessagesBundle
// ============================================================================
@NonNls
private const val COMMON_FEEDBACK_MESSAGES_BUNDLE = "messages.CommonFeedbackMessagesBundle"

internal object CommonFeedbackMessagesBundle {
    private val INSTANCE = DynamicBundle(CommonFeedbackMessagesBundle::class.java, COMMON_FEEDBACK_MESSAGES_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = COMMON_FEEDBACK_MESSAGES_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = COMMON_FEEDBACK_MESSAGES_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// CommonQuickFixBundle
// ============================================================================
@NonNls
private const val COMMON_QUICK_FIX_BUNDLE = "messages.CommonQuickFixBundle"

internal object CommonQuickFixBundle {
    private val INSTANCE = DynamicBundle(CommonQuickFixBundle::class.java, COMMON_QUICK_FIX_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = COMMON_QUICK_FIX_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = COMMON_QUICK_FIX_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// ComposeBundle
// ============================================================================
@NonNls
private const val COMPOSE_BUNDLE = "messages.ComposeBundle"

internal object ComposeBundle {
    private val INSTANCE = DynamicBundle(ComposeBundle::class.java, COMPOSE_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = COMPOSE_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = COMPOSE_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// ComposeIdeBundle
// ============================================================================
@NonNls
private const val COMPOSE_IDE_BUNDLE = "messages.ComposeIdeBundle"

internal object ComposeIdeBundle {
    private val INSTANCE = DynamicBundle(ComposeIdeBundle::class.java, COMPOSE_IDE_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = COMPOSE_IDE_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = COMPOSE_IDE_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// ComposeProjectWizardBundle
// ============================================================================
@NonNls
private const val COMPOSE_PROJECT_WIZARD_BUNDLE = "messages.ComposeProjectWizardBundle"

internal object ComposeProjectWizardBundle {
    private val INSTANCE = DynamicBundle(ComposeProjectWizardBundle::class.java, COMPOSE_PROJECT_WIZARD_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = COMPOSE_PROJECT_WIZARD_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = COMPOSE_PROJECT_WIZARD_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// ConfigurationScriptBundle
// ============================================================================
@NonNls
private const val CONFIGURATION_SCRIPT_BUNDLE = "messages.ConfigurationScriptBundle"

internal object ConfigurationScriptBundle {
    private val INSTANCE = DynamicBundle(ConfigurationScriptBundle::class.java, CONFIGURATION_SCRIPT_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = CONFIGURATION_SCRIPT_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = CONFIGURATION_SCRIPT_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// ConfigurationStoreBundle
// ============================================================================
@NonNls
private const val CONFIGURATION_STORE_BUNDLE = "messages.ConfigurationStoreBundle"

internal object ConfigurationStoreBundle {
    private val INSTANCE = DynamicBundle(ConfigurationStoreBundle::class.java, CONFIGURATION_STORE_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = CONFIGURATION_STORE_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = CONFIGURATION_STORE_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// CopyrightBundle
// ============================================================================
@NonNls
private const val COPYRIGHT_BUNDLE = "messages.CopyrightBundle"

internal object CopyrightBundle {
    private val INSTANCE = DynamicBundle(CopyrightBundle::class.java, COPYRIGHT_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = COPYRIGHT_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = COPYRIGHT_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// CoreBundle
// ============================================================================
@NonNls
private const val CORE_BUNDLE = "messages.CoreBundle"

internal object CoreBundle {
    private val INSTANCE = DynamicBundle(CoreBundle::class.java, CORE_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = CORE_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = CORE_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// CoreDeprecatedMessagesBundle
// ============================================================================
@NonNls
private const val CORE_DEPRECATED_MESSAGES_BUNDLE = "messages.CoreDeprecatedMessagesBundle"

internal object CoreDeprecatedMessagesBundle {
    private val INSTANCE = DynamicBundle(CoreDeprecatedMessagesBundle::class.java, CORE_DEPRECATED_MESSAGES_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = CORE_DEPRECATED_MESSAGES_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = CORE_DEPRECATED_MESSAGES_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// CoverageBundle
// ============================================================================
@NonNls
private const val COVERAGE_BUNDLE = "messages.CoverageBundle"

internal object CoverageBundle {
    private val INSTANCE = DynamicBundle(CoverageBundle::class.java, COVERAGE_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = COVERAGE_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = COVERAGE_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// CredentialStoreBundle
// ============================================================================
@NonNls
private const val CREDENTIAL_STORE_BUNDLE = "messages.CredentialStoreBundle"

internal object CredentialStoreBundle {
    private val INSTANCE = DynamicBundle(CredentialStoreBundle::class.java, CREDENTIAL_STORE_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = CREDENTIAL_STORE_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = CREDENTIAL_STORE_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// CsatFeedbackMessagesBundle
// ============================================================================
@NonNls
private const val CSAT_FEEDBACK_MESSAGES_BUNDLE = "messages.CsatFeedbackMessagesBundle"

internal object CsatFeedbackMessagesBundle {
    private val INSTANCE = DynamicBundle(CsatFeedbackMessagesBundle::class.java, CSAT_FEEDBACK_MESSAGES_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = CSAT_FEEDBACK_MESSAGES_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = CSAT_FEEDBACK_MESSAGES_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// CTestingBundle
// ============================================================================
@NonNls
private const val CTESTING_BUNDLE = "messages.CTestingBundle"

internal object CTestingBundle {
    private val INSTANCE = DynamicBundle(CTestingBundle::class.java, CTESTING_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = CTESTING_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = CTESTING_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// DaemonBundle
// ============================================================================
@NonNls
private const val DAEMON_BUNDLE = "messages.DaemonBundle"

internal object DaemonBundle {
    private val INSTANCE = DynamicBundle(DaemonBundle::class.java, DAEMON_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = DAEMON_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = DAEMON_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// DaggerBundle
// ============================================================================
@NonNls
private const val DAGGER_BUNDLE = "messages.DaggerBundle"

internal object DaggerBundle {
    private val INSTANCE = DynamicBundle(DaggerBundle::class.java, DAGGER_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = DAGGER_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = DAGGER_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// DatabaseInspectorBundle
// ============================================================================
@NonNls
private const val DATABASE_INSPECTOR_BUNDLE = "messages.DatabaseInspectorBundle"

internal object DatabaseInspectorBundle {
    private val INSTANCE = DynamicBundle(DatabaseInspectorBundle::class.java, DATABASE_INSPECTOR_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = DATABASE_INSPECTOR_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = DATABASE_INSPECTOR_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// DataGridBundle
// ============================================================================
@NonNls
private const val DATA_GRID_BUNDLE = "messages.DataGridBundle"

internal object DataGridBundle {
    private val INSTANCE = DynamicBundle(DataGridBundle::class.java, DATA_GRID_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = DATA_GRID_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = DATA_GRID_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// DeclarativeBundle
// ============================================================================
@NonNls
private const val DECLARATIVE_BUNDLE = "messages.DeclarativeBundle"

internal object DeclarativeBundle {
    private val INSTANCE = DynamicBundle(DeclarativeBundle::class.java, DECLARATIVE_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = DECLARATIVE_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = DECLARATIVE_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// DemoFeedbackMessagesBundle
// ============================================================================
@NonNls
private const val DEMO_FEEDBACK_MESSAGES_BUNDLE = "messages.DemoFeedbackMessagesBundle"

internal object DemoFeedbackMessagesBundle {
    private val INSTANCE = DynamicBundle(DemoFeedbackMessagesBundle::class.java, DEMO_FEEDBACK_MESSAGES_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = DEMO_FEEDBACK_MESSAGES_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = DEMO_FEEDBACK_MESSAGES_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// dependencySearchBundle
// ============================================================================
@NonNls
private const val DEPENDENCY_SEARCH_BUNDLE = "messages.dependencySearchBundle"

internal object dependencySearchBundle {
    private val INSTANCE = DynamicBundle(dependencySearchBundle::class.java, DEPENDENCY_SEARCH_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = DEPENDENCY_SEARCH_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = DEPENDENCY_SEARCH_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// DependencyUpdaterBundle
// ============================================================================
@NonNls
private const val DEPENDENCY_UPDATER_BUNDLE = "messages.DependencyUpdaterBundle"

internal object DependencyUpdaterBundle {
    private val INSTANCE = DynamicBundle(DependencyUpdaterBundle::class.java, DEPENDENCY_UPDATER_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = DEPENDENCY_UPDATER_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = DEPENDENCY_UPDATER_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// DesignerBundle
// ============================================================================
@NonNls
private const val DESIGNER_BUNDLE = "messages.DesignerBundle"

internal object DesignerBundle {
    private val INSTANCE = DynamicBundle(DesignerBundle::class.java, DESIGNER_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = DESIGNER_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = DESIGNER_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// DevCodeInsightBundle
// ============================================================================
@NonNls
private const val DEV_CODE_INSIGHT_BUNDLE = "messages.DevCodeInsightBundle"

internal object DevCodeInsightBundle {
    private val INSTANCE = DynamicBundle(DevCodeInsightBundle::class.java, DEV_CODE_INSIGHT_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = DEV_CODE_INSIGHT_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = DEV_CODE_INSIGHT_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// DeviceFileExplorerBundle
// ============================================================================
@NonNls
private const val DEVICE_FILE_EXPLORER_BUNDLE = "messages.DeviceFileExplorerBundle"

internal object DeviceFileExplorerBundle {
    private val INSTANCE = DynamicBundle(DeviceFileExplorerBundle::class.java, DEVICE_FILE_EXPLORER_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = DEVICE_FILE_EXPLORER_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = DEVICE_FILE_EXPLORER_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// DeviceManagerBundle
// ============================================================================
@NonNls
private const val DEVICE_MANAGER_BUNDLE = "messages.DeviceManagerBundle"

internal object DeviceManagerBundle {
    private val INSTANCE = DynamicBundle(DeviceManagerBundle::class.java, DEVICE_MANAGER_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = DEVICE_MANAGER_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = DEVICE_MANAGER_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// DevPsiViewerBundle
// ============================================================================
@NonNls
private const val DEV_PSI_VIEWER_BUNDLE = "messages.DevPsiViewerBundle"

internal object DevPsiViewerBundle {
    private val INSTANCE = DynamicBundle(DevPsiViewerBundle::class.java, DEV_PSI_VIEWER_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = DEV_PSI_VIEWER_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = DEV_PSI_VIEWER_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// DfaBundle
// ============================================================================
@NonNls
private const val DFA_BUNDLE = "messages.DfaBundle"

internal object DfaBundle {
    private val INSTANCE = DynamicBundle(DfaBundle::class.java, DFA_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = DFA_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = DFA_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// DiagnosticBundle
// ============================================================================
@NonNls
private const val DIAGNOSTIC_BUNDLE = "messages.DiagnosticBundle"

internal object DiagnosticBundle {
    private val INSTANCE = DynamicBundle(DiagnosticBundle::class.java, DIAGNOSTIC_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = DIAGNOSTIC_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = DIAGNOSTIC_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// DiffBundle
// ============================================================================
@NonNls
private const val DIFF_BUNDLE = "messages.DiffBundle"

internal object DiffBundle {
    private val INSTANCE = DynamicBundle(DiffBundle::class.java, DIFF_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = DIFF_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = DIFF_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// DupLocatorBundle
// ============================================================================
@NonNls
private const val DUP_LOCATOR_BUNDLE = "messages.DupLocatorBundle"

internal object DupLocatorBundle {
    private val INSTANCE = DynamicBundle(DupLocatorBundle::class.java, DUP_LOCATOR_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = DUP_LOCATOR_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = DUP_LOCATOR_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// DvcsBundle
// ============================================================================
@NonNls
private const val DVCS_BUNDLE = "messages.DvcsBundle"

internal object DvcsBundle {
    private val INSTANCE = DynamicBundle(DvcsBundle::class.java, DVCS_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = DVCS_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = DVCS_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// DxBundle
// ============================================================================
@NonNls
private const val DX_BUNDLE = "messages.DxBundle"

internal object DxBundle {
    private val INSTANCE = DynamicBundle(DxBundle::class.java, DX_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = DX_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = DX_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// EAPFeedbackMessagesBundle
// ============================================================================
@NonNls
private const val EAPFEEDBACK_MESSAGES_BUNDLE = "messages.EAPFeedbackMessagesBundle"

internal object EAPFeedbackMessagesBundle {
    private val INSTANCE = DynamicBundle(EAPFeedbackMessagesBundle::class.java, EAPFEEDBACK_MESSAGES_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = EAPFEEDBACK_MESSAGES_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = EAPFEEDBACK_MESSAGES_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// EditorBundle
// ============================================================================
@NonNls
private const val EDITOR_BUNDLE = "messages.EditorBundle"

internal object EditorBundle {
    private val INSTANCE = DynamicBundle(EditorBundle::class.java, EDITOR_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = EDITOR_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = EDITOR_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// EditorConfigBundle
// ============================================================================
@NonNls
private const val EDITOR_CONFIG_BUNDLE = "messages.EditorConfigBundle"

internal object EditorConfigBundle {
    private val INSTANCE = DynamicBundle(EditorConfigBundle::class.java, EDITOR_CONFIG_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = EDITOR_CONFIG_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = EDITOR_CONFIG_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// EmojiCategoriesBundle
// ============================================================================
@NonNls
private const val EMOJI_CATEGORIES_BUNDLE = "messages.EmojiCategoriesBundle"

internal object EmojiCategoriesBundle {
    private val INSTANCE = DynamicBundle(EmojiCategoriesBundle::class.java, EMOJI_CATEGORIES_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = EMOJI_CATEGORIES_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = EMOJI_CATEGORIES_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// EmojipickerBundle
// ============================================================================
@NonNls
private const val EMOJIPICKER_BUNDLE = "messages.EmojipickerBundle"

internal object EmojipickerBundle {
    private val INSTANCE = DynamicBundle(EmojipickerBundle::class.java, EMOJIPICKER_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = EMOJIPICKER_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = EMOJIPICKER_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// EvaluationFeedbackMessagesBundle
// ============================================================================
@NonNls
private const val EVALUATION_FEEDBACK_MESSAGES_BUNDLE = "messages.EvaluationFeedbackMessagesBundle"

internal object EvaluationFeedbackMessagesBundle {
    private val INSTANCE = DynamicBundle(EvaluationFeedbackMessagesBundle::class.java, EVALUATION_FEEDBACK_MESSAGES_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = EVALUATION_FEEDBACK_MESSAGES_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = EVALUATION_FEEDBACK_MESSAGES_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// ExecutionBundle
// ============================================================================
@NonNls
private const val EXECUTION_BUNDLE = "messages.ExecutionBundle"

internal object ExecutionBundle {
    private val INSTANCE = DynamicBundle(ExecutionBundle::class.java, EXECUTION_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = EXECUTION_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = EXECUTION_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// ExternalProcessAuthHelperBundle
// ============================================================================
@NonNls
private const val EXTERNAL_PROCESS_AUTH_HELPER_BUNDLE = "messages.ExternalProcessAuthHelperBundle"

internal object ExternalProcessAuthHelperBundle {
    private val INSTANCE = DynamicBundle(ExternalProcessAuthHelperBundle::class.java, EXTERNAL_PROCESS_AUTH_HELPER_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = EXTERNAL_PROCESS_AUTH_HELPER_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = EXTERNAL_PROCESS_AUTH_HELPER_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// ExternalSystemBundle
// ============================================================================
@NonNls
private const val EXTERNAL_SYSTEM_BUNDLE = "messages.ExternalSystemBundle"

internal object ExternalSystemBundle {
    private val INSTANCE = DynamicBundle(ExternalSystemBundle::class.java, EXTERNAL_SYSTEM_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = EXTERNAL_SYSTEM_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = EXTERNAL_SYSTEM_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// FeaturePromoBundle
// ============================================================================
@NonNls
private const val FEATURE_PROMO_BUNDLE = "messages.FeaturePromoBundle"

internal object FeaturePromoBundle {
    private val INSTANCE = DynamicBundle(FeaturePromoBundle::class.java, FEATURE_PROMO_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = FEATURE_PROMO_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = FEATURE_PROMO_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// FeatureStatisticsBundle
// ============================================================================
@NonNls
private const val FEATURE_STATISTICS_BUNDLE = "messages.FeatureStatisticsBundle"

internal object FeatureStatisticsBundle {
    private val INSTANCE = DynamicBundle(FeatureStatisticsBundle::class.java, FEATURE_STATISTICS_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = FEATURE_STATISTICS_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = FEATURE_STATISTICS_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// FeedbackBundle
// ============================================================================
@NonNls
private const val FEEDBACK_BUNDLE = "messages.FeedbackBundle"

internal object FeedbackBundle {
    private val INSTANCE = DynamicBundle(FeedbackBundle::class.java, FEEDBACK_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = FEEDBACK_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = FEEDBACK_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// FileTypesBundle
// ============================================================================
@NonNls
private const val FILE_TYPES_BUNDLE = "messages.FileTypesBundle"

internal object FileTypesBundle {
    private val INSTANCE = DynamicBundle(FileTypesBundle::class.java, FILE_TYPES_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = FILE_TYPES_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = FILE_TYPES_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// FindBundle
// ============================================================================
@NonNls
private const val FIND_BUNDLE = "messages.FindBundle"

internal object FindBundle {
    private val INSTANCE = DynamicBundle(FindBundle::class.java, FIND_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = FIND_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = FIND_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// FirebaseBundle
// ============================================================================
@NonNls
private const val FIREBASE_BUNDLE = "messages.FirebaseBundle"

internal object FirebaseBundle {
    private val INSTANCE = DynamicBundle(FirebaseBundle::class.java, FIREBASE_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = FIREBASE_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = FIREBASE_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// FrontendDebuggerImplBundle
// ============================================================================
@NonNls
private const val FRONTEND_DEBUGGER_IMPL_BUNDLE = "messages.FrontendDebuggerImplBundle"

internal object FrontendDebuggerImplBundle {
    private val INSTANCE = DynamicBundle(FrontendDebuggerImplBundle::class.java, FRONTEND_DEBUGGER_IMPL_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = FRONTEND_DEBUGGER_IMPL_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = FRONTEND_DEBUGGER_IMPL_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// FrontMatterBundle
// ============================================================================
@NonNls
private const val FRONT_MATTER_BUNDLE = "messages.FrontMatterBundle"

internal object FrontMatterBundle {
    private val INSTANCE = DynamicBundle(FrontMatterBundle::class.java, FRONT_MATTER_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = FRONT_MATTER_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = FRONT_MATTER_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// GDBBundle
// ============================================================================
@NonNls
private const val GDBBUNDLE = "messages.GDBBundle"

internal object GDBBundle {
    private val INSTANCE = DynamicBundle(GDBBundle::class.java, GDBBUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = GDBBUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = GDBBUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// GeneralFeedbackMessagesBundle
// ============================================================================
@NonNls
private const val GENERAL_FEEDBACK_MESSAGES_BUNDLE = "messages.GeneralFeedbackMessagesBundle"

internal object GeneralFeedbackMessagesBundle {
    private val INSTANCE = DynamicBundle(GeneralFeedbackMessagesBundle::class.java, GENERAL_FEEDBACK_MESSAGES_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = GENERAL_FEEDBACK_MESSAGES_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = GENERAL_FEEDBACK_MESSAGES_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// GiasEnterpriseBundle
// ============================================================================
@NonNls
private const val GIAS_ENTERPRISE_BUNDLE = "messages.GiasEnterpriseBundle"

internal object GiasEnterpriseBundle {
    private val INSTANCE = DynamicBundle(GiasEnterpriseBundle::class.java, GIAS_ENTERPRISE_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = GIAS_ENTERPRISE_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = GIAS_ENTERPRISE_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// GitBundle
// ============================================================================
@NonNls
private const val GIT_BUNDLE = "messages.GitBundle"

internal object GitBundle {
    private val INSTANCE = DynamicBundle(GitBundle::class.java, GIT_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = GIT_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = GIT_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// GitFrontendBundle
// ============================================================================
@NonNls
private const val GIT_FRONTEND_BUNDLE = "messages.GitFrontendBundle"

internal object GitFrontendBundle {
    private val INSTANCE = DynamicBundle(GitFrontendBundle::class.java, GIT_FRONTEND_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = GIT_FRONTEND_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = GIT_FRONTEND_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// GithubBundle
// ============================================================================
@NonNls
private const val GITHUB_BUNDLE = "messages.GithubBundle"

internal object GithubBundle {
    private val INSTANCE = DynamicBundle(GithubBundle::class.java, GITHUB_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = GITHUB_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = GITHUB_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// GitLabBundle
// ============================================================================
@NonNls
private const val GIT_LAB_BUNDLE = "messages.GitLabBundle"

internal object GitLabBundle {
    private val INSTANCE = DynamicBundle(GitLabBundle::class.java, GIT_LAB_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = GIT_LAB_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = GIT_LAB_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// GitLabDeprecatedMessagesBundle
// ============================================================================
@NonNls
private const val GIT_LAB_DEPRECATED_MESSAGES_BUNDLE = "messages.GitLabDeprecatedMessagesBundle"

internal object GitLabDeprecatedMessagesBundle {
    private val INSTANCE = DynamicBundle(GitLabDeprecatedMessagesBundle::class.java, GIT_LAB_DEPRECATED_MESSAGES_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = GIT_LAB_DEPRECATED_MESSAGES_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = GIT_LAB_DEPRECATED_MESSAGES_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// GitTerminalBundle
// ============================================================================
@NonNls
private const val GIT_TERMINAL_BUNDLE = "messages.GitTerminalBundle"

internal object GitTerminalBundle {
    private val INSTANCE = DynamicBundle(GitTerminalBundle::class.java, GIT_TERMINAL_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = GIT_TERMINAL_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = GIT_TERMINAL_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// GradleBundle
// ============================================================================
@NonNls
private const val GRADLE_BUNDLE = "messages.GradleBundle"

internal object GradleBundle {
    private val INSTANCE = DynamicBundle(GradleBundle::class.java, GRADLE_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = GRADLE_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = GRADLE_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// GradleDeprecatedMessagesBundle
// ============================================================================
@NonNls
private const val GRADLE_DEPRECATED_MESSAGES_BUNDLE = "messages.GradleDeprecatedMessagesBundle"

internal object GradleDeprecatedMessagesBundle {
    private val INSTANCE = DynamicBundle(GradleDeprecatedMessagesBundle::class.java, GRADLE_DEPRECATED_MESSAGES_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = GRADLE_DEPRECATED_MESSAGES_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = GRADLE_DEPRECATED_MESSAGES_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// GradleDocumentationBundle
// ============================================================================
@NonNls
private const val GRADLE_DOCUMENTATION_BUNDLE = "messages.GradleDocumentationBundle"

internal object GradleDocumentationBundle {
    private val INSTANCE = DynamicBundle(GradleDocumentationBundle::class.java, GRADLE_DOCUMENTATION_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = GRADLE_DOCUMENTATION_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = GRADLE_DOCUMENTATION_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// GradleFeedbackBundle
// ============================================================================
@NonNls
private const val GRADLE_FEEDBACK_BUNDLE = "messages.GradleFeedbackBundle"

internal object GradleFeedbackBundle {
    private val INSTANCE = DynamicBundle(GradleFeedbackBundle::class.java, GRADLE_FEEDBACK_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = GRADLE_FEEDBACK_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = GRADLE_FEEDBACK_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// GradleInspectionBundle
// ============================================================================
@NonNls
private const val GRADLE_INSPECTION_BUNDLE = "messages.GradleInspectionBundle"

internal object GradleInspectionBundle {
    private val INSTANCE = DynamicBundle(GradleInspectionBundle::class.java, GRADLE_INSPECTION_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = GRADLE_INSPECTION_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = GRADLE_INSPECTION_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// GradleJpsBundle
// ============================================================================
@NonNls
private const val GRADLE_JPS_BUNDLE = "messages.GradleJpsBundle"

internal object GradleJpsBundle {
    private val INSTANCE = DynamicBundle(GradleJpsBundle::class.java, GRADLE_JPS_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = GRADLE_JPS_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = GRADLE_JPS_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// GrazieBundle
// ============================================================================
@NonNls
private const val GRAZIE_BUNDLE = "messages.GrazieBundle"

internal object GrazieBundle {
    private val INSTANCE = DynamicBundle(GrazieBundle::class.java, GRAZIE_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = GRAZIE_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = GRAZIE_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// GraziePluginBundle
// ============================================================================
@NonNls
private const val GRAZIE_PLUGIN_BUNDLE = "messages.GraziePluginBundle"

internal object GraziePluginBundle {
    private val INSTANCE = DynamicBundle(GraziePluginBundle::class.java, GRAZIE_PLUGIN_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = GRAZIE_PLUGIN_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = GRAZIE_PLUGIN_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// GridCsvBundle
// ============================================================================
@NonNls
private const val GRID_CSV_BUNDLE = "messages.GridCsvBundle"

internal object GridCsvBundle {
    private val INSTANCE = DynamicBundle(GridCsvBundle::class.java, GRID_CSV_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = GRID_CSV_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = GRID_CSV_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// GroovyBundle
// ============================================================================
@NonNls
private const val GROOVY_BUNDLE = "messages.GroovyBundle"

internal object GroovyBundle {
    private val INSTANCE = DynamicBundle(GroovyBundle::class.java, GROOVY_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = GROOVY_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = GROOVY_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// GroovyDeprecatedMessagesBundle
// ============================================================================
@NonNls
private const val GROOVY_DEPRECATED_MESSAGES_BUNDLE = "messages.GroovyDeprecatedMessagesBundle"

internal object GroovyDeprecatedMessagesBundle {
    private val INSTANCE = DynamicBundle(GroovyDeprecatedMessagesBundle::class.java, GROOVY_DEPRECATED_MESSAGES_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = GROOVY_DEPRECATED_MESSAGES_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = GROOVY_DEPRECATED_MESSAGES_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// GroovyIntentionsBundle
// ============================================================================
@NonNls
private const val GROOVY_INTENTIONS_BUNDLE = "messages.GroovyIntentionsBundle"

internal object GroovyIntentionsBundle {
    private val INSTANCE = DynamicBundle(GroovyIntentionsBundle::class.java, GROOVY_INTENTIONS_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = GROOVY_INTENTIONS_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = GROOVY_INTENTIONS_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// GroovyJpsBundle
// ============================================================================
@NonNls
private const val GROOVY_JPS_BUNDLE = "messages.GroovyJpsBundle"

internal object GroovyJpsBundle {
    private val INSTANCE = DynamicBundle(GroovyJpsBundle::class.java, GROOVY_JPS_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = GROOVY_JPS_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = GROOVY_JPS_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// GroovyRefactoringBundle
// ============================================================================
@NonNls
private const val GROOVY_REFACTORING_BUNDLE = "messages.GroovyRefactoringBundle"

internal object GroovyRefactoringBundle {
    private val INSTANCE = DynamicBundle(GroovyRefactoringBundle::class.java, GROOVY_REFACTORING_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = GROOVY_REFACTORING_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = GROOVY_REFACTORING_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// HgBundle
// ============================================================================
@NonNls
private const val HG_BUNDLE = "messages.HgBundle"

internal object HgBundle {
    private val INSTANCE = DynamicBundle(HgBundle::class.java, HG_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = HG_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = HG_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// HtmlToolsBundle
// ============================================================================
@NonNls
private const val HTML_TOOLS_BUNDLE = "messages.HtmlToolsBundle"

internal object HtmlToolsBundle {
    private val INSTANCE = DynamicBundle(HtmlToolsBundle::class.java, HTML_TOOLS_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = HTML_TOOLS_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = HTML_TOOLS_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// IdeaDecompilerBundle
// ============================================================================
@NonNls
private const val IDEA_DECOMPILER_BUNDLE = "messages.IdeaDecompilerBundle"

internal object IdeaDecompilerBundle {
    private val INSTANCE = DynamicBundle(IdeaDecompilerBundle::class.java, IDEA_DECOMPILER_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = IDEA_DECOMPILER_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = IDEA_DECOMPILER_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// IdeBundle
// ============================================================================
@NonNls
private const val IDE_BUNDLE = "messages.IdeBundle"

internal object IdeBundle {
    private val INSTANCE = DynamicBundle(IdeBundle::class.java, IDE_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = IDE_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = IDE_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// IdeCoreBundle
// ============================================================================
@NonNls
private const val IDE_CORE_BUNDLE = "messages.IdeCoreBundle"

internal object IdeCoreBundle {
    private val INSTANCE = DynamicBundle(IdeCoreBundle::class.java, IDE_CORE_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = IDE_CORE_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = IDE_CORE_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// IdeDeprecatedMessagesBundle
// ============================================================================
@NonNls
private const val IDE_DEPRECATED_MESSAGES_BUNDLE = "messages.IdeDeprecatedMessagesBundle"

internal object IdeDeprecatedMessagesBundle {
    private val INSTANCE = DynamicBundle(IdeDeprecatedMessagesBundle::class.java, IDE_DEPRECATED_MESSAGES_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = IDE_DEPRECATED_MESSAGES_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = IDE_DEPRECATED_MESSAGES_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// IdeUtilIoBundle
// ============================================================================
@NonNls
private const val IDE_UTIL_IO_BUNDLE = "messages.IdeUtilIoBundle"

internal object IdeUtilIoBundle {
    private val INSTANCE = DynamicBundle(IdeUtilIoBundle::class.java, IDE_UTIL_IO_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = IDE_UTIL_IO_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = IDE_UTIL_IO_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// IjentBundle
// ============================================================================
@NonNls
private const val IJENT_BUNDLE = "messages.IjentBundle"

internal object IjentBundle {
    private val INSTANCE = DynamicBundle(IjentBundle::class.java, IJENT_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = IJENT_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = IJENT_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// ImagesBundle
// ============================================================================
@NonNls
private const val IMAGES_BUNDLE = "messages.ImagesBundle"

internal object ImagesBundle {
    private val INSTANCE = DynamicBundle(ImagesBundle::class.java, IMAGES_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = IMAGES_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = IMAGES_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// IndexingBundle
// ============================================================================
@NonNls
private const val INDEXING_BUNDLE = "messages.IndexingBundle"

internal object IndexingBundle {
    private val INSTANCE = DynamicBundle(IndexingBundle::class.java, INDEXING_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = INDEXING_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = INDEXING_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// InlineCompletionBundle
// ============================================================================
@NonNls
private const val INLINE_COMPLETION_BUNDLE = "messages.InlineCompletionBundle"

internal object InlineCompletionBundle {
    private val INSTANCE = DynamicBundle(InlineCompletionBundle::class.java, INLINE_COMPLETION_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = INLINE_COMPLETION_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = INLINE_COMPLETION_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// InspectionGadgetsBundle
// ============================================================================
@NonNls
private const val INSPECTION_GADGETS_BUNDLE = "messages.InspectionGadgetsBundle"

internal object InspectionGadgetsBundle {
    private val INSTANCE = DynamicBundle(InspectionGadgetsBundle::class.java, INSPECTION_GADGETS_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = INSPECTION_GADGETS_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = INSPECTION_GADGETS_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// InspectionsBundle
// ============================================================================
@NonNls
private const val INSPECTIONS_BUNDLE = "messages.InspectionsBundle"

internal object InspectionsBundle {
    private val INSTANCE = DynamicBundle(InspectionsBundle::class.java, INSPECTIONS_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = INSPECTIONS_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = INSPECTIONS_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// InspectionsDeprecatedMessagesBundle
// ============================================================================
@NonNls
private const val INSPECTIONS_DEPRECATED_MESSAGES_BUNDLE = "messages.InspectionsDeprecatedMessagesBundle"

internal object InspectionsDeprecatedMessagesBundle {
    private val INSTANCE = DynamicBundle(InspectionsDeprecatedMessagesBundle::class.java, INSPECTIONS_DEPRECATED_MESSAGES_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = INSPECTIONS_DEPRECATED_MESSAGES_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = INSPECTIONS_DEPRECATED_MESSAGES_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// IntellijPluginCoreMessageBundle
// ============================================================================
@NonNls
private const val INTELLIJ_PLUGIN_CORE_MESSAGE_BUNDLE = "messages.IntellijPluginCoreMessageBundle"

internal object IntellijPluginCoreMessageBundle {
    private val INSTANCE = DynamicBundle(IntellijPluginCoreMessageBundle::class.java, INTELLIJ_PLUGIN_CORE_MESSAGE_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = INTELLIJ_PLUGIN_CORE_MESSAGE_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = INTELLIJ_PLUGIN_CORE_MESSAGE_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// IntelliLangBundle
// ============================================================================
@NonNls
private const val INTELLI_LANG_BUNDLE = "messages.IntelliLangBundle"

internal object IntelliLangBundle {
    private val INSTANCE = DynamicBundle(IntelliLangBundle::class.java, INTELLI_LANG_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = INTELLI_LANG_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = INTELLI_LANG_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// IntentionPowerPackBundle
// ============================================================================
@NonNls
private const val INTENTION_POWER_PACK_BUNDLE = "messages.IntentionPowerPackBundle"

internal object IntentionPowerPackBundle {
    private val INSTANCE = DynamicBundle(IntentionPowerPackBundle::class.java, INTENTION_POWER_PACK_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = INTENTION_POWER_PACK_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = INTENTION_POWER_PACK_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// InternalActionsBundle
// ============================================================================
@NonNls
private const val INTERNAL_ACTIONS_BUNDLE = "messages.InternalActionsBundle"

internal object InternalActionsBundle {
    private val INSTANCE = DynamicBundle(InternalActionsBundle::class.java, INTERNAL_ACTIONS_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = INTERNAL_ACTIONS_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = INTERNAL_ACTIONS_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// JavaAnalysisBundle
// ============================================================================
@NonNls
private const val JAVA_ANALYSIS_BUNDLE = "messages.JavaAnalysisBundle"

internal object JavaAnalysisBundle {
    private val INSTANCE = DynamicBundle(JavaAnalysisBundle::class.java, JAVA_ANALYSIS_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = JAVA_ANALYSIS_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = JAVA_ANALYSIS_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// JavaBundle
// ============================================================================
@NonNls
private const val JAVA_BUNDLE = "messages.JavaBundle"

internal object JavaBundle {
    private val INSTANCE = DynamicBundle(JavaBundle::class.java, JAVA_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = JAVA_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = JAVA_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// JavaCompilationErrorBundle
// ============================================================================
@NonNls
private const val JAVA_COMPILATION_ERROR_BUNDLE = "messages.JavaCompilationErrorBundle"

internal object JavaCompilationErrorBundle {
    private val INSTANCE = DynamicBundle(JavaCompilationErrorBundle::class.java, JAVA_COMPILATION_ERROR_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = JAVA_COMPILATION_ERROR_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = JAVA_COMPILATION_ERROR_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// JavaCompilerBundle
// ============================================================================
@NonNls
private const val JAVA_COMPILER_BUNDLE = "messages.JavaCompilerBundle"

internal object JavaCompilerBundle {
    private val INSTANCE = DynamicBundle(JavaCompilerBundle::class.java, JAVA_COMPILER_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = JAVA_COMPILER_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = JAVA_COMPILER_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// JavaCoverageBundle
// ============================================================================
@NonNls
private const val JAVA_COVERAGE_BUNDLE = "messages.JavaCoverageBundle"

internal object JavaCoverageBundle {
    private val INSTANCE = DynamicBundle(JavaCoverageBundle::class.java, JAVA_COVERAGE_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = JAVA_COVERAGE_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = JAVA_COVERAGE_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// JavaDebuggerBundle
// ============================================================================
@NonNls
private const val JAVA_DEBUGGER_BUNDLE = "messages.JavaDebuggerBundle"

internal object JavaDebuggerBundle {
    private val INSTANCE = DynamicBundle(JavaDebuggerBundle::class.java, JAVA_DEBUGGER_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = JAVA_DEBUGGER_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = JAVA_DEBUGGER_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// JavaDebuggerSharedBundle
// ============================================================================
@NonNls
private const val JAVA_DEBUGGER_SHARED_BUNDLE = "messages.JavaDebuggerSharedBundle"

internal object JavaDebuggerSharedBundle {
    private val INSTANCE = DynamicBundle(JavaDebuggerSharedBundle::class.java, JAVA_DEBUGGER_SHARED_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = JAVA_DEBUGGER_SHARED_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = JAVA_DEBUGGER_SHARED_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// JavaDevBundle
// ============================================================================
@NonNls
private const val JAVA_DEV_BUNDLE = "messages.JavaDevBundle"

internal object JavaDevBundle {
    private val INSTANCE = DynamicBundle(JavaDevBundle::class.java, JAVA_DEV_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = JAVA_DEV_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = JAVA_DEV_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// JavaErrorBundle
// ============================================================================
@NonNls
private const val JAVA_ERROR_BUNDLE = "messages.JavaErrorBundle"

internal object JavaErrorBundle {
    private val INSTANCE = DynamicBundle(JavaErrorBundle::class.java, JAVA_ERROR_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = JAVA_ERROR_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = JAVA_ERROR_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// JavaFrontbackBundle
// ============================================================================
@NonNls
private const val JAVA_FRONTBACK_BUNDLE = "messages.JavaFrontbackBundle"

internal object JavaFrontbackBundle {
    private val INSTANCE = DynamicBundle(JavaFrontbackBundle::class.java, JAVA_FRONTBACK_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = JAVA_FRONTBACK_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = JAVA_FRONTBACK_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// JavaI18nBundle
// ============================================================================
@NonNls
private const val JAVA_I18N_BUNDLE = "messages.JavaI18nBundle"

internal object JavaI18nBundle {
    private val INSTANCE = DynamicBundle(JavaI18nBundle::class.java, JAVA_I18N_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = JAVA_I18N_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = JAVA_I18N_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// JavaIndexingBundle
// ============================================================================
@NonNls
private const val JAVA_INDEXING_BUNDLE = "messages.JavaIndexingBundle"

internal object JavaIndexingBundle {
    private val INSTANCE = DynamicBundle(JavaIndexingBundle::class.java, JAVA_INDEXING_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = JAVA_INDEXING_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = JAVA_INDEXING_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// JavaLessonsBundle
// ============================================================================
@NonNls
private const val JAVA_LESSONS_BUNDLE = "messages.JavaLessonsBundle"

internal object JavaLessonsBundle {
    private val INSTANCE = DynamicBundle(JavaLessonsBundle::class.java, JAVA_LESSONS_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = JAVA_LESSONS_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = JAVA_LESSONS_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// JavaOptionBundle
// ============================================================================
@NonNls
private const val JAVA_OPTION_BUNDLE = "messages.JavaOptionBundle"

internal object JavaOptionBundle {
    private val INSTANCE = DynamicBundle(JavaOptionBundle::class.java, JAVA_OPTION_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = JAVA_OPTION_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = JAVA_OPTION_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// JavaPsiBundle
// ============================================================================
@NonNls
private const val JAVA_PSI_BUNDLE = "messages.JavaPsiBundle"

internal object JavaPsiBundle {
    private val INSTANCE = DynamicBundle(JavaPsiBundle::class.java, JAVA_PSI_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = JAVA_PSI_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = JAVA_PSI_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// JavaRefactoringBundle
// ============================================================================
@NonNls
private const val JAVA_REFACTORING_BUNDLE = "messages.JavaRefactoringBundle"

internal object JavaRefactoringBundle {
    private val INSTANCE = DynamicBundle(JavaRefactoringBundle::class.java, JAVA_REFACTORING_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = JAVA_REFACTORING_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = JAVA_REFACTORING_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// JavaStartersBundle
// ============================================================================
@NonNls
private const val JAVA_STARTERS_BUNDLE = "messages.JavaStartersBundle"

internal object JavaStartersBundle {
    private val INSTANCE = DynamicBundle(JavaStartersBundle::class.java, JAVA_STARTERS_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = JAVA_STARTERS_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = JAVA_STARTERS_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// JavaStructureViewBundle
// ============================================================================
@NonNls
private const val JAVA_STRUCTURE_VIEW_BUNDLE = "messages.JavaStructureViewBundle"

internal object JavaStructureViewBundle {
    private val INSTANCE = DynamicBundle(JavaStructureViewBundle::class.java, JAVA_STRUCTURE_VIEW_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = JAVA_STRUCTURE_VIEW_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = JAVA_STRUCTURE_VIEW_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// JavaSyntaxBundle
// ============================================================================
@NonNls
private const val JAVA_SYNTAX_BUNDLE = "messages.JavaSyntaxBundle"

internal object JavaSyntaxBundle {
    private val INSTANCE = DynamicBundle(JavaSyntaxBundle::class.java, JAVA_SYNTAX_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = JAVA_SYNTAX_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = JAVA_SYNTAX_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// JavaTerminalBundle
// ============================================================================
@NonNls
private const val JAVA_TERMINAL_BUNDLE = "messages.JavaTerminalBundle"

internal object JavaTerminalBundle {
    private val INSTANCE = DynamicBundle(JavaTerminalBundle::class.java, JAVA_TERMINAL_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = JAVA_TERMINAL_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = JAVA_TERMINAL_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// JavaUiBundle
// ============================================================================
@NonNls
private const val JAVA_UI_BUNDLE = "messages.JavaUiBundle"

internal object JavaUiBundle {
    private val INSTANCE = DynamicBundle(JavaUiBundle::class.java, JAVA_UI_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = JAVA_UI_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = JAVA_UI_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// JcefBundle
// ============================================================================
@NonNls
private const val JCEF_BUNDLE = "messages.JcefBundle"

internal object JcefBundle {
    private val INSTANCE = DynamicBundle(JcefBundle::class.java, JCEF_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = JCEF_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = JCEF_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// JetBrainsAcademyWelcomeScreenBundle
// ============================================================================
@NonNls
private const val JET_BRAINS_ACADEMY_WELCOME_SCREEN_BUNDLE = "messages.JetBrainsAcademyWelcomeScreenBundle"

internal object JetBrainsAcademyWelcomeScreenBundle {
    private val INSTANCE = DynamicBundle(JetBrainsAcademyWelcomeScreenBundle::class.java, JET_BRAINS_ACADEMY_WELCOME_SCREEN_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = JET_BRAINS_ACADEMY_WELCOME_SCREEN_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = JET_BRAINS_ACADEMY_WELCOME_SCREEN_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// JewelIntUIBundle
// ============================================================================
@NonNls
private const val JEWEL_INT_UIBUNDLE = "messages.JewelIntUIBundle"

internal object JewelIntUIBundle {
    private val INSTANCE = DynamicBundle(JewelIntUIBundle::class.java, JEWEL_INT_UIBUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = JEWEL_INT_UIBUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = JEWEL_INT_UIBUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// JourneysBundle
// ============================================================================
@NonNls
private const val JOURNEYS_BUNDLE = "messages.JourneysBundle"

internal object JourneysBundle {
    private val INSTANCE = DynamicBundle(JourneysBundle::class.java, JOURNEYS_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = JOURNEYS_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = JOURNEYS_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// JpsBuildBundle
// ============================================================================
@NonNls
private const val JPS_BUILD_BUNDLE = "messages.JpsBuildBundle"

internal object JpsBuildBundle {
    private val INSTANCE = DynamicBundle(JpsBuildBundle::class.java, JPS_BUILD_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = JPS_BUILD_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = JPS_BUILD_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// JsonBundle
// ============================================================================
@NonNls
private const val JSON_BUNDLE = "messages.JsonBundle"

internal object JsonBundle {
    private val INSTANCE = DynamicBundle(JsonBundle::class.java, JSON_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = JSON_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = JSON_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// JUnitBundle
// ============================================================================
@NonNls
private const val JUNIT_BUNDLE = "messages.JUnitBundle"

internal object JUnitBundle {
    private val INSTANCE = DynamicBundle(JUnitBundle::class.java, JUNIT_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = JUNIT_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = JUNIT_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// JvmAnalysisBundle
// ============================================================================
@NonNls
private const val JVM_ANALYSIS_BUNDLE = "messages.JvmAnalysisBundle"

internal object JvmAnalysisBundle {
    private val INSTANCE = DynamicBundle(JvmAnalysisBundle::class.java, JVM_ANALYSIS_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = JVM_ANALYSIS_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = JVM_ANALYSIS_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// K2HighlightingBundle
// ============================================================================
@NonNls
private const val K2HIGHLIGHTING_BUNDLE = "messages.K2HighlightingBundle"

internal object K2HighlightingBundle {
    private val INSTANCE = DynamicBundle(K2HighlightingBundle::class.java, K2HIGHLIGHTING_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = K2HIGHLIGHTING_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = K2HIGHLIGHTING_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// KeyMapBundle
// ============================================================================
@NonNls
private const val KEY_MAP_BUNDLE = "messages.KeyMapBundle"

internal object KeyMapBundle {
    private val INSTANCE = DynamicBundle(KeyMapBundle::class.java, KEY_MAP_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = KEY_MAP_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = KEY_MAP_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// KotlinBaseAnalysisBundle
// ============================================================================
@NonNls
private const val KOTLIN_BASE_ANALYSIS_BUNDLE = "messages.KotlinBaseAnalysisBundle"

internal object KotlinBaseAnalysisBundle {
    private val INSTANCE = DynamicBundle(KotlinBaseAnalysisBundle::class.java, KOTLIN_BASE_ANALYSIS_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = KOTLIN_BASE_ANALYSIS_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = KOTLIN_BASE_ANALYSIS_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// KotlinBaseCodeInsightBundle
// ============================================================================
@NonNls
private const val KOTLIN_BASE_CODE_INSIGHT_BUNDLE = "messages.KotlinBaseCodeInsightBundle"

internal object KotlinBaseCodeInsightBundle {
    private val INSTANCE = DynamicBundle(KotlinBaseCodeInsightBundle::class.java, KOTLIN_BASE_CODE_INSIGHT_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = KOTLIN_BASE_CODE_INSIGHT_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = KOTLIN_BASE_CODE_INSIGHT_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// KotlinBaseCompilerConfigurationUiBundle
// ============================================================================
@NonNls
private const val KOTLIN_BASE_COMPILER_CONFIGURATION_UI_BUNDLE = "messages.KotlinBaseCompilerConfigurationUiBundle"

internal object KotlinBaseCompilerConfigurationUiBundle {
    private val INSTANCE = DynamicBundle(KotlinBaseCompilerConfigurationUiBundle::class.java, KOTLIN_BASE_COMPILER_CONFIGURATION_UI_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = KOTLIN_BASE_COMPILER_CONFIGURATION_UI_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = KOTLIN_BASE_COMPILER_CONFIGURATION_UI_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// KotlinBaseFacetBundle
// ============================================================================
@NonNls
private const val KOTLIN_BASE_FACET_BUNDLE = "messages.KotlinBaseFacetBundle"

internal object KotlinBaseFacetBundle {
    private val INSTANCE = DynamicBundle(KotlinBaseFacetBundle::class.java, KOTLIN_BASE_FACET_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = KOTLIN_BASE_FACET_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = KOTLIN_BASE_FACET_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// KotlinBaseFe10CodeInsightBundle
// ============================================================================
@NonNls
private const val KOTLIN_BASE_FE10CODE_INSIGHT_BUNDLE = "messages.KotlinBaseFe10CodeInsightBundle"

internal object KotlinBaseFe10CodeInsightBundle {
    private val INSTANCE = DynamicBundle(KotlinBaseFe10CodeInsightBundle::class.java, KOTLIN_BASE_FE10CODE_INSIGHT_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = KOTLIN_BASE_FE10CODE_INSIGHT_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = KOTLIN_BASE_FE10CODE_INSIGHT_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// KotlinBaseFe10HighlightingBundle
// ============================================================================
@NonNls
private const val KOTLIN_BASE_FE10HIGHLIGHTING_BUNDLE = "messages.KotlinBaseFe10HighlightingBundle"

internal object KotlinBaseFe10HighlightingBundle {
    private val INSTANCE = DynamicBundle(KotlinBaseFe10HighlightingBundle::class.java, KOTLIN_BASE_FE10HIGHLIGHTING_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = KOTLIN_BASE_FE10HIGHLIGHTING_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = KOTLIN_BASE_FE10HIGHLIGHTING_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// KotlinBaseHighlightingBundle
// ============================================================================
@NonNls
private const val KOTLIN_BASE_HIGHLIGHTING_BUNDLE = "messages.KotlinBaseHighlightingBundle"

internal object KotlinBaseHighlightingBundle {
    private val INSTANCE = DynamicBundle(KotlinBaseHighlightingBundle::class.java, KOTLIN_BASE_HIGHLIGHTING_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = KOTLIN_BASE_HIGHLIGHTING_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = KOTLIN_BASE_HIGHLIGHTING_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// KotlinBaseInjectionBundle
// ============================================================================
@NonNls
private const val KOTLIN_BASE_INJECTION_BUNDLE = "messages.KotlinBaseInjectionBundle"

internal object KotlinBaseInjectionBundle {
    private val INSTANCE = DynamicBundle(KotlinBaseInjectionBundle::class.java, KOTLIN_BASE_INJECTION_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = KOTLIN_BASE_INJECTION_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = KOTLIN_BASE_INJECTION_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// KotlinBasePlatformsBundle
// ============================================================================
@NonNls
private const val KOTLIN_BASE_PLATFORMS_BUNDLE = "messages.KotlinBasePlatformsBundle"

internal object KotlinBasePlatformsBundle {
    private val INSTANCE = DynamicBundle(KotlinBasePlatformsBundle::class.java, KOTLIN_BASE_PLATFORMS_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = KOTLIN_BASE_PLATFORMS_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = KOTLIN_BASE_PLATFORMS_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// KotlinBasePluginBundle
// ============================================================================
@NonNls
private const val KOTLIN_BASE_PLUGIN_BUNDLE = "messages.KotlinBasePluginBundle"

internal object KotlinBasePluginBundle {
    private val INSTANCE = DynamicBundle(KotlinBasePluginBundle::class.java, KOTLIN_BASE_PLUGIN_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = KOTLIN_BASE_PLUGIN_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = KOTLIN_BASE_PLUGIN_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// KotlinBaseProjectStructureBundle
// ============================================================================
@NonNls
private const val KOTLIN_BASE_PROJECT_STRUCTURE_BUNDLE = "messages.KotlinBaseProjectStructureBundle"

internal object KotlinBaseProjectStructureBundle {
    private val INSTANCE = DynamicBundle(KotlinBaseProjectStructureBundle::class.java, KOTLIN_BASE_PROJECT_STRUCTURE_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = KOTLIN_BASE_PROJECT_STRUCTURE_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = KOTLIN_BASE_PROJECT_STRUCTURE_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// KotlinBasePsiBundle
// ============================================================================
@NonNls
private const val KOTLIN_BASE_PSI_BUNDLE = "messages.KotlinBasePsiBundle"

internal object KotlinBasePsiBundle {
    private val INSTANCE = DynamicBundle(KotlinBasePsiBundle::class.java, KOTLIN_BASE_PSI_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = KOTLIN_BASE_PSI_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = KOTLIN_BASE_PSI_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// KotlinBaseScriptingBundle
// ============================================================================
@NonNls
private const val KOTLIN_BASE_SCRIPTING_BUNDLE = "messages.KotlinBaseScriptingBundle"

internal object KotlinBaseScriptingBundle {
    private val INSTANCE = DynamicBundle(KotlinBaseScriptingBundle::class.java, KOTLIN_BASE_SCRIPTING_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = KOTLIN_BASE_SCRIPTING_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = KOTLIN_BASE_SCRIPTING_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// KotlinBundle
// ============================================================================
@NonNls
private const val KOTLIN_BUNDLE = "messages.KotlinBundle"

internal object KotlinBundle {
    private val INSTANCE = DynamicBundle(KotlinBundle::class.java, KOTLIN_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = KOTLIN_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = KOTLIN_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// KotlinCodeInsightBundle
// ============================================================================
@NonNls
private const val KOTLIN_CODE_INSIGHT_BUNDLE = "messages.KotlinCodeInsightBundle"

internal object KotlinCodeInsightBundle {
    private val INSTANCE = DynamicBundle(KotlinCodeInsightBundle::class.java, KOTLIN_CODE_INSIGHT_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = KOTLIN_CODE_INSIGHT_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = KOTLIN_CODE_INSIGHT_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// KotlinCompletionImplK2Bundle
// ============================================================================
@NonNls
private const val KOTLIN_COMPLETION_IMPL_K2BUNDLE = "messages.KotlinCompletionImplK2Bundle"

internal object KotlinCompletionImplK2Bundle {
    private val INSTANCE = DynamicBundle(KotlinCompletionImplK2Bundle::class.java, KOTLIN_COMPLETION_IMPL_K2BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = KOTLIN_COMPLETION_IMPL_K2BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = KOTLIN_COMPLETION_IMPL_K2BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// KotlinDebuggerCoreBundle
// ============================================================================
@NonNls
private const val KOTLIN_DEBUGGER_CORE_BUNDLE = "messages.KotlinDebuggerCoreBundle"

internal object KotlinDebuggerCoreBundle {
    private val INSTANCE = DynamicBundle(KotlinDebuggerCoreBundle::class.java, KOTLIN_DEBUGGER_CORE_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = KOTLIN_DEBUGGER_CORE_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = KOTLIN_DEBUGGER_CORE_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// KotlinDebuggerCoroutinesBundle
// ============================================================================
@NonNls
private const val KOTLIN_DEBUGGER_COROUTINES_BUNDLE = "messages.KotlinDebuggerCoroutinesBundle"

internal object KotlinDebuggerCoroutinesBundle {
    private val INSTANCE = DynamicBundle(KotlinDebuggerCoroutinesBundle::class.java, KOTLIN_DEBUGGER_COROUTINES_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = KOTLIN_DEBUGGER_COROUTINES_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = KOTLIN_DEBUGGER_COROUTINES_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// KotlinDebuggerEvaluationBundle
// ============================================================================
@NonNls
private const val KOTLIN_DEBUGGER_EVALUATION_BUNDLE = "messages.KotlinDebuggerEvaluationBundle"

internal object KotlinDebuggerEvaluationBundle {
    private val INSTANCE = DynamicBundle(KotlinDebuggerEvaluationBundle::class.java, KOTLIN_DEBUGGER_EVALUATION_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = KOTLIN_DEBUGGER_EVALUATION_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = KOTLIN_DEBUGGER_EVALUATION_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// KotlinDebuggerFeedbackSurveyBundle
// ============================================================================
@NonNls
private const val KOTLIN_DEBUGGER_FEEDBACK_SURVEY_BUNDLE = "messages.KotlinDebuggerFeedbackSurveyBundle"

internal object KotlinDebuggerFeedbackSurveyBundle {
    private val INSTANCE = DynamicBundle(KotlinDebuggerFeedbackSurveyBundle::class.java, KOTLIN_DEBUGGER_FEEDBACK_SURVEY_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = KOTLIN_DEBUGGER_FEEDBACK_SURVEY_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = KOTLIN_DEBUGGER_FEEDBACK_SURVEY_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// KotlinDevBundle
// ============================================================================
@NonNls
private const val KOTLIN_DEV_BUNDLE = "messages.KotlinDevBundle"

internal object KotlinDevBundle {
    private val INSTANCE = DynamicBundle(KotlinDevBundle::class.java, KOTLIN_DEV_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = KOTLIN_DEV_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = KOTLIN_DEV_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// KotlinFormatterMinimalBundle
// ============================================================================
@NonNls
private const val KOTLIN_FORMATTER_MINIMAL_BUNDLE = "messages.KotlinFormatterMinimalBundle"

internal object KotlinFormatterMinimalBundle {
    private val INSTANCE = DynamicBundle(KotlinFormatterMinimalBundle::class.java, KOTLIN_FORMATTER_MINIMAL_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = KOTLIN_FORMATTER_MINIMAL_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = KOTLIN_FORMATTER_MINIMAL_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// KotlinGradleCodeInsightCommonBundle
// ============================================================================
@NonNls
private const val KOTLIN_GRADLE_CODE_INSIGHT_COMMON_BUNDLE = "messages.KotlinGradleCodeInsightCommonBundle"

internal object KotlinGradleCodeInsightCommonBundle {
    private val INSTANCE = DynamicBundle(KotlinGradleCodeInsightCommonBundle::class.java, KOTLIN_GRADLE_CODE_INSIGHT_COMMON_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = KOTLIN_GRADLE_CODE_INSIGHT_COMMON_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = KOTLIN_GRADLE_CODE_INSIGHT_COMMON_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// KotlinGradleScriptingBundle
// ============================================================================
@NonNls
private const val KOTLIN_GRADLE_SCRIPTING_BUNDLE = "messages.KotlinGradleScriptingBundle"

internal object KotlinGradleScriptingBundle {
    private val INSTANCE = DynamicBundle(KotlinGradleScriptingBundle::class.java, KOTLIN_GRADLE_SCRIPTING_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = KOTLIN_GRADLE_SCRIPTING_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = KOTLIN_GRADLE_SCRIPTING_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// KotlinGroovyBundle
// ============================================================================
@NonNls
private const val KOTLIN_GROOVY_BUNDLE = "messages.KotlinGroovyBundle"

internal object KotlinGroovyBundle {
    private val INSTANCE = DynamicBundle(KotlinGroovyBundle::class.java, KOTLIN_GROOVY_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = KOTLIN_GROOVY_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = KOTLIN_GROOVY_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// KotlinIdeaBundle
// ============================================================================
@NonNls
private const val KOTLIN_IDEA_BUNDLE = "messages.KotlinIdeaBundle"

internal object KotlinIdeaBundle {
    private val INSTANCE = DynamicBundle(KotlinIdeaBundle::class.java, KOTLIN_IDEA_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = KOTLIN_IDEA_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = KOTLIN_IDEA_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// KotlinIdeaCompletionBundle
// ============================================================================
@NonNls
private const val KOTLIN_IDEA_COMPLETION_BUNDLE = "messages.KotlinIdeaCompletionBundle"

internal object KotlinIdeaCompletionBundle {
    private val INSTANCE = DynamicBundle(KotlinIdeaCompletionBundle::class.java, KOTLIN_IDEA_COMPLETION_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = KOTLIN_IDEA_COMPLETION_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = KOTLIN_IDEA_COMPLETION_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// KotlinIdeaCoreBundle
// ============================================================================
@NonNls
private const val KOTLIN_IDEA_CORE_BUNDLE = "messages.KotlinIdeaCoreBundle"

internal object KotlinIdeaCoreBundle {
    private val INSTANCE = DynamicBundle(KotlinIdeaCoreBundle::class.java, KOTLIN_IDEA_CORE_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = KOTLIN_IDEA_CORE_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = KOTLIN_IDEA_CORE_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// KotlinIdeaGradleBundle
// ============================================================================
@NonNls
private const val KOTLIN_IDEA_GRADLE_BUNDLE = "messages.KotlinIdeaGradleBundle"

internal object KotlinIdeaGradleBundle {
    private val INSTANCE = DynamicBundle(KotlinIdeaGradleBundle::class.java, KOTLIN_IDEA_GRADLE_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = KOTLIN_IDEA_GRADLE_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = KOTLIN_IDEA_GRADLE_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// KotlinIdeaReplBundle
// ============================================================================
@NonNls
private const val KOTLIN_IDEA_REPL_BUNDLE = "messages.KotlinIdeaReplBundle"

internal object KotlinIdeaReplBundle {
    private val INSTANCE = DynamicBundle(KotlinIdeaReplBundle::class.java, KOTLIN_IDEA_REPL_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = KOTLIN_IDEA_REPL_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = KOTLIN_IDEA_REPL_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// KotlinInspectionsBundle
// ============================================================================
@NonNls
private const val KOTLIN_INSPECTIONS_BUNDLE = "messages.KotlinInspectionsBundle"

internal object KotlinInspectionsBundle {
    private val INSTANCE = DynamicBundle(KotlinInspectionsBundle::class.java, KOTLIN_INSPECTIONS_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = KOTLIN_INSPECTIONS_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = KOTLIN_INSPECTIONS_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// KotlinInspectionsFe10Bundle
// ============================================================================
@NonNls
private const val KOTLIN_INSPECTIONS_FE10BUNDLE = "messages.KotlinInspectionsFe10Bundle"

internal object KotlinInspectionsFe10Bundle {
    private val INSTANCE = DynamicBundle(KotlinInspectionsFe10Bundle::class.java, KOTLIN_INSPECTIONS_FE10BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = KOTLIN_INSPECTIONS_FE10BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = KOTLIN_INSPECTIONS_FE10BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// KotlinInternalBundle
// ============================================================================
@NonNls
private const val KOTLIN_INTERNAL_BUNDLE = "messages.KotlinInternalBundle"

internal object KotlinInternalBundle {
    private val INSTANCE = DynamicBundle(KotlinInternalBundle::class.java, KOTLIN_INTERNAL_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = KOTLIN_INTERNAL_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = KOTLIN_INTERNAL_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// KotlinJ2KBundle
// ============================================================================
@NonNls
private const val KOTLIN_J2KBUNDLE = "messages.KotlinJ2KBundle"

internal object KotlinJ2KBundle {
    private val INSTANCE = DynamicBundle(KotlinJ2KBundle::class.java, KOTLIN_J2KBUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = KOTLIN_J2KBUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = KOTLIN_J2KBUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// KotlinJ2KK2Bundle
// ============================================================================
@NonNls
private const val KOTLIN_J2KK2BUNDLE = "messages.KotlinJ2KK2Bundle"

internal object KotlinJ2KK2Bundle {
    private val INSTANCE = DynamicBundle(KotlinJ2KK2Bundle::class.java, KOTLIN_J2KK2BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = KOTLIN_J2KK2BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = KOTLIN_J2KK2BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// KotlinJpsBundle
// ============================================================================
@NonNls
private const val KOTLIN_JPS_BUNDLE = "messages.KotlinJpsBundle"

internal object KotlinJpsBundle {
    private val INSTANCE = DynamicBundle(KotlinJpsBundle::class.java, KOTLIN_JPS_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = KOTLIN_JPS_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = KOTLIN_JPS_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// KotlinJUnitBundle
// ============================================================================
@NonNls
private const val KOTLIN_JUNIT_BUNDLE = "messages.KotlinJUnitBundle"

internal object KotlinJUnitBundle {
    private val INSTANCE = DynamicBundle(KotlinJUnitBundle::class.java, KOTLIN_JUNIT_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = KOTLIN_JUNIT_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = KOTLIN_JUNIT_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// KotlinJvmBundle
// ============================================================================
@NonNls
private const val KOTLIN_JVM_BUNDLE = "messages.KotlinJvmBundle"

internal object KotlinJvmBundle {
    private val INSTANCE = DynamicBundle(KotlinJvmBundle::class.java, KOTLIN_JVM_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = KOTLIN_JVM_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = KOTLIN_JVM_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// KotlinJvmDecompilerBundle
// ============================================================================
@NonNls
private const val KOTLIN_JVM_DECOMPILER_BUNDLE = "messages.KotlinJvmDecompilerBundle"

internal object KotlinJvmDecompilerBundle {
    private val INSTANCE = DynamicBundle(KotlinJvmDecompilerBundle::class.java, KOTLIN_JVM_DECOMPILER_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = KOTLIN_JVM_DECOMPILER_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = KOTLIN_JVM_DECOMPILER_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// KotlinJvmDecompilerDeprecatedMessagesBundle
// ============================================================================
@NonNls
private const val KOTLIN_JVM_DECOMPILER_DEPRECATED_MESSAGES_BUNDLE = "messages.KotlinJvmDecompilerDeprecatedMessagesBundle"

internal object KotlinJvmDecompilerDeprecatedMessagesBundle {
    private val INSTANCE = DynamicBundle(KotlinJvmDecompilerDeprecatedMessagesBundle::class.java, KOTLIN_JVM_DECOMPILER_DEPRECATED_MESSAGES_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = KOTLIN_JVM_DECOMPILER_DEPRECATED_MESSAGES_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = KOTLIN_JVM_DECOMPILER_DEPRECATED_MESSAGES_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// KotlinK2RefactoringsBundle
// ============================================================================
@NonNls
private const val KOTLIN_K2REFACTORINGS_BUNDLE = "messages.KotlinK2RefactoringsBundle"

internal object KotlinK2RefactoringsBundle {
    private val INSTANCE = DynamicBundle(KotlinK2RefactoringsBundle::class.java, KOTLIN_K2REFACTORINGS_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = KOTLIN_K2REFACTORINGS_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = KOTLIN_K2REFACTORINGS_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// KotlinLessonsBundle
// ============================================================================
@NonNls
private const val KOTLIN_LESSONS_BUNDLE = "messages.KotlinLessonsBundle"

internal object KotlinLessonsBundle {
    private val INSTANCE = DynamicBundle(KotlinLessonsBundle::class.java, KOTLIN_LESSONS_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = KOTLIN_LESSONS_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = KOTLIN_LESSONS_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// KotlinLineMarkersBundle
// ============================================================================
@NonNls
private const val KOTLIN_LINE_MARKERS_BUNDLE = "messages.KotlinLineMarkersBundle"

internal object KotlinLineMarkersBundle {
    private val INSTANCE = DynamicBundle(KotlinLineMarkersBundle::class.java, KOTLIN_LINE_MARKERS_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = KOTLIN_LINE_MARKERS_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = KOTLIN_LINE_MARKERS_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// KotlinLineMarkersSharedBundle
// ============================================================================
@NonNls
private const val KOTLIN_LINE_MARKERS_SHARED_BUNDLE = "messages.KotlinLineMarkersSharedBundle"

internal object KotlinLineMarkersSharedBundle {
    private val INSTANCE = DynamicBundle(KotlinLineMarkersSharedBundle::class.java, KOTLIN_LINE_MARKERS_SHARED_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = KOTLIN_LINE_MARKERS_SHARED_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = KOTLIN_LINE_MARKERS_SHARED_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// KotlinLiveTemplatesBundle
// ============================================================================
@NonNls
private const val KOTLIN_LIVE_TEMPLATES_BUNDLE = "messages.KotlinLiveTemplatesBundle"

internal object KotlinLiveTemplatesBundle {
    private val INSTANCE = DynamicBundle(KotlinLiveTemplatesBundle::class.java, KOTLIN_LIVE_TEMPLATES_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = KOTLIN_LIVE_TEMPLATES_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = KOTLIN_LIVE_TEMPLATES_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// KotlinMavenBundle
// ============================================================================
@NonNls
private const val KOTLIN_MAVEN_BUNDLE = "messages.KotlinMavenBundle"

internal object KotlinMavenBundle {
    private val INSTANCE = DynamicBundle(KotlinMavenBundle::class.java, KOTLIN_MAVEN_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = KOTLIN_MAVEN_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = KOTLIN_MAVEN_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// KotlinMigrationBundle
// ============================================================================
@NonNls
private const val KOTLIN_MIGRATION_BUNDLE = "messages.KotlinMigrationBundle"

internal object KotlinMigrationBundle {
    private val INSTANCE = DynamicBundle(KotlinMigrationBundle::class.java, KOTLIN_MIGRATION_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = KOTLIN_MIGRATION_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = KOTLIN_MIGRATION_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// KotlinMlCompletionBundle
// ============================================================================
@NonNls
private const val KOTLIN_ML_COMPLETION_BUNDLE = "messages.KotlinMlCompletionBundle"

internal object KotlinMlCompletionBundle {
    private val INSTANCE = DynamicBundle(KotlinMlCompletionBundle::class.java, KOTLIN_ML_COMPLETION_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = KOTLIN_ML_COMPLETION_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = KOTLIN_ML_COMPLETION_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// KotlinNativeBundle
// ============================================================================
@NonNls
private const val KOTLIN_NATIVE_BUNDLE = "messages.KotlinNativeBundle"

internal object KotlinNativeBundle {
    private val INSTANCE = DynamicBundle(KotlinNativeBundle::class.java, KOTLIN_NATIVE_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = KOTLIN_NATIVE_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = KOTLIN_NATIVE_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// KotlinNewProjectWizardBundle
// ============================================================================
@NonNls
private const val KOTLIN_NEW_PROJECT_WIZARD_BUNDLE = "messages.KotlinNewProjectWizardBundle"

internal object KotlinNewProjectWizardBundle {
    private val INSTANCE = DynamicBundle(KotlinNewProjectWizardBundle::class.java, KOTLIN_NEW_PROJECT_WIZARD_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = KOTLIN_NEW_PROJECT_WIZARD_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = KOTLIN_NEW_PROJECT_WIZARD_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// KotlinNewProjectWizardUIBundle
// ============================================================================
@NonNls
private const val KOTLIN_NEW_PROJECT_WIZARD_UIBUNDLE = "messages.KotlinNewProjectWizardUIBundle"

internal object KotlinNewProjectWizardUIBundle {
    private val INSTANCE = DynamicBundle(KotlinNewProjectWizardUIBundle::class.java, KOTLIN_NEW_PROJECT_WIZARD_UIBUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = KOTLIN_NEW_PROJECT_WIZARD_UIBUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = KOTLIN_NEW_PROJECT_WIZARD_UIBUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// KotlinNJ2KBundle
// ============================================================================
@NonNls
private const val KOTLIN_NJ2KBUNDLE = "messages.KotlinNJ2KBundle"

internal object KotlinNJ2KBundle {
    private val INSTANCE = DynamicBundle(KotlinNJ2KBundle::class.java, KOTLIN_NJ2KBUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = KOTLIN_NJ2KBUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = KOTLIN_NJ2KBUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// KotlinNJ2KServicesBundle
// ============================================================================
@NonNls
private const val KOTLIN_NJ2KSERVICES_BUNDLE = "messages.KotlinNJ2KServicesBundle"

internal object KotlinNJ2KServicesBundle {
    private val INSTANCE = DynamicBundle(KotlinNJ2KServicesBundle::class.java, KOTLIN_NJ2KSERVICES_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = KOTLIN_NJ2KSERVICES_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = KOTLIN_NJ2KSERVICES_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// KotlinParcelizeBundle
// ============================================================================
@NonNls
private const val KOTLIN_PARCELIZE_BUNDLE = "messages.KotlinParcelizeBundle"

internal object KotlinParcelizeBundle {
    private val INSTANCE = DynamicBundle(KotlinParcelizeBundle::class.java, KOTLIN_PARCELIZE_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = KOTLIN_PARCELIZE_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = KOTLIN_PARCELIZE_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// KotlinPluginUpdaterBundle
// ============================================================================
@NonNls
private const val KOTLIN_PLUGIN_UPDATER_BUNDLE = "messages.KotlinPluginUpdaterBundle"

internal object KotlinPluginUpdaterBundle {
    private val INSTANCE = DynamicBundle(KotlinPluginUpdaterBundle::class.java, KOTLIN_PLUGIN_UPDATER_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = KOTLIN_PLUGIN_UPDATER_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = KOTLIN_PLUGIN_UPDATER_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// KotlinPreferencesBundle
// ============================================================================
@NonNls
private const val KOTLIN_PREFERENCES_BUNDLE = "messages.KotlinPreferencesBundle"

internal object KotlinPreferencesBundle {
    private val INSTANCE = DynamicBundle(KotlinPreferencesBundle::class.java, KOTLIN_PREFERENCES_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = KOTLIN_PREFERENCES_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = KOTLIN_PREFERENCES_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// KotlinProjectConfigurationBundle
// ============================================================================
@NonNls
private const val KOTLIN_PROJECT_CONFIGURATION_BUNDLE = "messages.KotlinProjectConfigurationBundle"

internal object KotlinProjectConfigurationBundle {
    private val INSTANCE = DynamicBundle(KotlinProjectConfigurationBundle::class.java, KOTLIN_PROJECT_CONFIGURATION_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = KOTLIN_PROJECT_CONFIGURATION_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = KOTLIN_PROJECT_CONFIGURATION_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// KotlinReferenceIndexBundle
// ============================================================================
@NonNls
private const val KOTLIN_REFERENCE_INDEX_BUNDLE = "messages.KotlinReferenceIndexBundle"

internal object KotlinReferenceIndexBundle {
    private val INSTANCE = DynamicBundle(KotlinReferenceIndexBundle::class.java, KOTLIN_REFERENCE_INDEX_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = KOTLIN_REFERENCE_INDEX_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = KOTLIN_REFERENCE_INDEX_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// KotlinRunConfigurationsBundle
// ============================================================================
@NonNls
private const val KOTLIN_RUN_CONFIGURATIONS_BUNDLE = "messages.KotlinRunConfigurationsBundle"

internal object KotlinRunConfigurationsBundle {
    private val INSTANCE = DynamicBundle(KotlinRunConfigurationsBundle::class.java, KOTLIN_RUN_CONFIGURATIONS_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = KOTLIN_RUN_CONFIGURATIONS_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = KOTLIN_RUN_CONFIGURATIONS_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// KotlinSerializationBundle
// ============================================================================
@NonNls
private const val KOTLIN_SERIALIZATION_BUNDLE = "messages.KotlinSerializationBundle"

internal object KotlinSerializationBundle {
    private val INSTANCE = DynamicBundle(KotlinSerializationBundle::class.java, KOTLIN_SERIALIZATION_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = KOTLIN_SERIALIZATION_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = KOTLIN_SERIALIZATION_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// KotlinStyleBundle
// ============================================================================
@NonNls
private const val KOTLIN_STYLE_BUNDLE = "messages.KotlinStyleBundle"

internal object KotlinStyleBundle {
    private val INSTANCE = DynamicBundle(KotlinStyleBundle::class.java, KOTLIN_STYLE_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = KOTLIN_STYLE_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = KOTLIN_STYLE_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// LangBundle
// ============================================================================
@NonNls
private const val LANG_BUNDLE = "messages.LangBundle"

internal object LangBundle {
    private val INSTANCE = DynamicBundle(LangBundle::class.java, LANG_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = LANG_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = LANG_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// LangCoreBundle
// ============================================================================
@NonNls
private const val LANG_CORE_BUNDLE = "messages.LangCoreBundle"

internal object LangCoreBundle {
    private val INSTANCE = DynamicBundle(LangCoreBundle::class.java, LANG_CORE_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = LANG_CORE_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = LANG_CORE_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// LanguageAndRegionBundle
// ============================================================================
@NonNls
private const val LANGUAGE_AND_REGION_BUNDLE = "messages.LanguageAndRegionBundle"

internal object LanguageAndRegionBundle {
    private val INSTANCE = DynamicBundle(LanguageAndRegionBundle::class.java, LANGUAGE_AND_REGION_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = LANGUAGE_AND_REGION_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = LANGUAGE_AND_REGION_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// LayoutInspectorBundle
// ============================================================================
@NonNls
private const val LAYOUT_INSPECTOR_BUNDLE = "messages.LayoutInspectorBundle"

internal object LayoutInspectorBundle {
    private val INSTANCE = DynamicBundle(LayoutInspectorBundle::class.java, LAYOUT_INSPECTOR_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = LAYOUT_INSPECTOR_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = LAYOUT_INSPECTOR_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// LayoutlibBundle
// ============================================================================
@NonNls
private const val LAYOUTLIB_BUNDLE = "messages.LayoutlibBundle"

internal object LayoutlibBundle {
    private val INSTANCE = DynamicBundle(LayoutlibBundle::class.java, LAYOUTLIB_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = LAYOUTLIB_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = LAYOUTLIB_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// LintBundle
// ============================================================================
@NonNls
private const val LINT_BUNDLE = "messages.LintBundle"

internal object LintBundle {
    private val INSTANCE = DynamicBundle(LintBundle::class.java, LINT_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = LINT_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = LINT_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// LLDBBundle
// ============================================================================
@NonNls
private const val LLDBBUNDLE = "messages.LLDBBundle"

internal object LLDBBundle {
    private val INSTANCE = DynamicBundle(LLDBBundle::class.java, LLDBBUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = LLDBBUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = LLDBBUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// LocalHistoryBundle
// ============================================================================
@NonNls
private const val LOCAL_HISTORY_BUNDLE = "messages.LocalHistoryBundle"

internal object LocalHistoryBundle {
    private val INSTANCE = DynamicBundle(LocalHistoryBundle::class.java, LOCAL_HISTORY_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = LOCAL_HISTORY_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = LOCAL_HISTORY_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// LocalizationFeedbackMessagesBundle
// ============================================================================
@NonNls
private const val LOCALIZATION_FEEDBACK_MESSAGES_BUNDLE = "messages.LocalizationFeedbackMessagesBundle"

internal object LocalizationFeedbackMessagesBundle {
    private val INSTANCE = DynamicBundle(LocalizationFeedbackMessagesBundle::class.java, LOCALIZATION_FEEDBACK_MESSAGES_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = LOCALIZATION_FEEDBACK_MESSAGES_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = LOCALIZATION_FEEDBACK_MESSAGES_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// LocalProviderBundle
// ============================================================================
@NonNls
private const val LOCAL_PROVIDER_BUNDLE = "messages.LocalProviderBundle"

internal object LocalProviderBundle {
    private val INSTANCE = DynamicBundle(LocalProviderBundle::class.java, LOCAL_PROVIDER_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = LOCAL_PROVIDER_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = LOCAL_PROVIDER_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// LogcatBundle
// ============================================================================
@NonNls
private const val LOGCAT_BUNDLE = "messages.LogcatBundle"

internal object LogcatBundle {
    private val INSTANCE = DynamicBundle(LogcatBundle::class.java, LOGCAT_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = LOGCAT_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = LOGCAT_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// ManifestBundle
// ============================================================================
@NonNls
private const val MANIFEST_BUNDLE = "messages.ManifestBundle"

internal object ManifestBundle {
    private val INSTANCE = DynamicBundle(ManifestBundle::class.java, MANIFEST_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = MANIFEST_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = MANIFEST_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// MarkdownBundle
// ============================================================================
@NonNls
private const val MARKDOWN_BUNDLE = "messages.MarkdownBundle"

internal object MarkdownBundle {
    private val INSTANCE = DynamicBundle(MarkdownBundle::class.java, MARKDOWN_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = MARKDOWN_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = MARKDOWN_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// MarkdownImagesBundle
// ============================================================================
@NonNls
private const val MARKDOWN_IMAGES_BUNDLE = "messages.MarkdownImagesBundle"

internal object MarkdownImagesBundle {
    private val INSTANCE = DynamicBundle(MarkdownImagesBundle::class.java, MARKDOWN_IMAGES_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = MARKDOWN_IMAGES_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = MARKDOWN_IMAGES_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// McpHostBundle
// ============================================================================
@NonNls
private const val MCP_HOST_BUNDLE = "messages.McpHostBundle"

internal object McpHostBundle {
    private val INSTANCE = DynamicBundle(McpHostBundle::class.java, MCP_HOST_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = MCP_HOST_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = MCP_HOST_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// MdnBundle
// ============================================================================
@NonNls
private const val MDN_BUNDLE = "messages.MdnBundle"

internal object MdnBundle {
    private val INSTANCE = DynamicBundle(MdnBundle::class.java, MDN_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = MDN_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = MDN_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// MicroservicesBundle
// ============================================================================
@NonNls
private const val MICROSERVICES_BUNDLE = "messages.MicroservicesBundle"

internal object MicroservicesBundle {
    private val INSTANCE = DynamicBundle(MicroservicesBundle::class.java, MICROSERVICES_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = MICROSERVICES_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = MICROSERVICES_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// MicroservicesJvmUrlBundle
// ============================================================================
@NonNls
private const val MICROSERVICES_JVM_URL_BUNDLE = "messages.MicroservicesJvmUrlBundle"

internal object MicroservicesJvmUrlBundle {
    private val INSTANCE = DynamicBundle(MicroservicesJvmUrlBundle::class.java, MICROSERVICES_JVM_URL_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = MICROSERVICES_JVM_URL_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = MICROSERVICES_JVM_URL_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// MinimapBundle
// ============================================================================
@NonNls
private const val MINIMAP_BUNDLE = "messages.MinimapBundle"

internal object MinimapBundle {
    private val INSTANCE = DynamicBundle(MinimapBundle::class.java, MINIMAP_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = MINIMAP_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = MINIMAP_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// MlCompletionBundle
// ============================================================================
@NonNls
private const val ML_COMPLETION_BUNDLE = "messages.MlCompletionBundle"

internal object MlCompletionBundle {
    private val INSTANCE = DynamicBundle(MlCompletionBundle::class.java, ML_COMPLETION_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = ML_COMPLETION_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = ML_COMPLETION_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// ModalCommitBundle
// ============================================================================
@NonNls
private const val MODAL_COMMIT_BUNDLE = "messages.ModalCommitBundle"

internal object ModalCommitBundle {
    private val INSTANCE = DynamicBundle(ModalCommitBundle::class.java, MODAL_COMMIT_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = MODAL_COMMIT_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = MODAL_COMMIT_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// ModuleMapBundle
// ============================================================================
@NonNls
private const val MODULE_MAP_BUNDLE = "messages.ModuleMapBundle"

internal object ModuleMapBundle {
    private val INSTANCE = DynamicBundle(ModuleMapBundle::class.java, MODULE_MAP_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = MODULE_MAP_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = MODULE_MAP_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// NavBarFrontendBundle
// ============================================================================
@NonNls
private const val NAV_BAR_FRONTEND_BUNDLE = "messages.NavBarFrontendBundle"

internal object NavBarFrontendBundle {
    private val INSTANCE = DynamicBundle(NavBarFrontendBundle::class.java, NAV_BAR_FRONTEND_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = NAV_BAR_FRONTEND_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = NAV_BAR_FRONTEND_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// NetworkInspectorBundle
// ============================================================================
@NonNls
private const val NETWORK_INSPECTOR_BUNDLE = "messages.NetworkInspectorBundle"

internal object NetworkInspectorBundle {
    private val INSTANCE = DynamicBundle(NetworkInspectorBundle::class.java, NETWORK_INSPECTOR_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = NETWORK_INSPECTOR_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = NETWORK_INSPECTOR_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// OCBundle
// ============================================================================
@NonNls
private const val OCBUNDLE = "messages.OCBundle"

internal object OCBundle {
    private val INSTANCE = DynamicBundle(OCBundle::class.java, OCBUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = OCBUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = OCBUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// OCDebuggerBundle
// ============================================================================
@NonNls
private const val OCDEBUGGER_BUNDLE = "messages.OCDebuggerBundle"

internal object OCDebuggerBundle {
    private val INSTANCE = DynamicBundle(OCDebuggerBundle::class.java, OCDEBUGGER_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = OCDEBUGGER_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = OCDEBUGGER_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// OCGenerateBundle
// ============================================================================
@NonNls
private const val OCGENERATE_BUNDLE = "messages.OCGenerateBundle"

internal object OCGenerateBundle {
    private val INSTANCE = DynamicBundle(OCGenerateBundle::class.java, OCGENERATE_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = OCGENERATE_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = OCGENERATE_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// OCInspectionsBundle
// ============================================================================
@NonNls
private const val OCINSPECTIONS_BUNDLE = "messages.OCInspectionsBundle"

internal object OCInspectionsBundle {
    private val INSTANCE = DynamicBundle(OCInspectionsBundle::class.java, OCINSPECTIONS_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = OCINSPECTIONS_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = OCINSPECTIONS_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// OCInteractiveBundle
// ============================================================================
@NonNls
private const val OCINTERACTIVE_BUNDLE = "messages.OCInteractiveBundle"

internal object OCInteractiveBundle {
    private val INSTANCE = DynamicBundle(OCInteractiveBundle::class.java, OCINTERACTIVE_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = OCINTERACTIVE_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = OCINTERACTIVE_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// OCRefactoringBundle
// ============================================================================
@NonNls
private const val OCREFACTORING_BUNDLE = "messages.OCRefactoringBundle"

internal object OCRefactoringBundle {
    private val INSTANCE = DynamicBundle(OCRefactoringBundle::class.java, OCREFACTORING_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = OCREFACTORING_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = OCREFACTORING_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// OptionsBundle
// ============================================================================
@NonNls
private const val OPTIONS_BUNDLE = "messages.OptionsBundle"

internal object OptionsBundle {
    private val INSTANCE = DynamicBundle(OptionsBundle::class.java, OPTIONS_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = OPTIONS_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = OPTIONS_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// PerformanceTestingBundle
// ============================================================================
@NonNls
private const val PERFORMANCE_TESTING_BUNDLE = "messages.PerformanceTestingBundle"

internal object PerformanceTestingBundle {
    private val INSTANCE = DynamicBundle(PerformanceTestingBundle::class.java, PERFORMANCE_TESTING_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = PERFORMANCE_TESTING_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = PERFORMANCE_TESTING_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// PlatformEditorBundle
// ============================================================================
@NonNls
private const val PLATFORM_EDITOR_BUNDLE = "messages.PlatformEditorBundle"

internal object PlatformEditorBundle {
    private val INSTANCE = DynamicBundle(PlatformEditorBundle::class.java, PLATFORM_EDITOR_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = PLATFORM_EDITOR_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = PLATFORM_EDITOR_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// PluginFreezeBundle
// ============================================================================
@NonNls
private const val PLUGIN_FREEZE_BUNDLE = "messages.PluginFreezeBundle"

internal object PluginFreezeBundle {
    private val INSTANCE = DynamicBundle(PluginFreezeBundle::class.java, PLUGIN_FREEZE_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = PLUGIN_FREEZE_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = PLUGIN_FREEZE_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// PluginPageFeedbackMessagesBundle
// ============================================================================
@NonNls
private const val PLUGIN_PAGE_FEEDBACK_MESSAGES_BUNDLE = "messages.PluginPageFeedbackMessagesBundle"

internal object PluginPageFeedbackMessagesBundle {
    private val INSTANCE = DynamicBundle(PluginPageFeedbackMessagesBundle::class.java, PLUGIN_PAGE_FEEDBACK_MESSAGES_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = PLUGIN_PAGE_FEEDBACK_MESSAGES_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = PLUGIN_PAGE_FEEDBACK_MESSAGES_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// PolySymbolsBundle
// ============================================================================
@NonNls
private const val POLY_SYMBOLS_BUNDLE = "messages.PolySymbolsBundle"

internal object PolySymbolsBundle {
    private val INSTANCE = DynamicBundle(PolySymbolsBundle::class.java, POLY_SYMBOLS_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = POLY_SYMBOLS_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = POLY_SYMBOLS_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// PrattBundle
// ============================================================================
@NonNls
private const val PRATT_BUNDLE = "messages.PrattBundle"

internal object PrattBundle {
    private val INSTANCE = DynamicBundle(PrattBundle::class.java, PRATT_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = PRATT_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = PRATT_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// PredictionServicesBundle
// ============================================================================
@NonNls
private const val PREDICTION_SERVICES_BUNDLE = "messages.PredictionServicesBundle"

internal object PredictionServicesBundle {
    private val INSTANCE = DynamicBundle(PredictionServicesBundle::class.java, PREDICTION_SERVICES_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = PREDICTION_SERVICES_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = PREDICTION_SERVICES_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// ProblemsViewBundle
// ============================================================================
@NonNls
private const val PROBLEMS_VIEW_BUNDLE = "messages.ProblemsViewBundle"

internal object ProblemsViewBundle {
    private val INSTANCE = DynamicBundle(ProblemsViewBundle::class.java, PROBLEMS_VIEW_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = PROBLEMS_VIEW_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = PROBLEMS_VIEW_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// ProcessHandshakeBundle
// ============================================================================
@NonNls
private const val PROCESS_HANDSHAKE_BUNDLE = "messages.ProcessHandshakeBundle"

internal object ProcessHandshakeBundle {
    private val INSTANCE = DynamicBundle(ProcessHandshakeBundle::class.java, PROCESS_HANDSHAKE_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = PROCESS_HANDSHAKE_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = PROCESS_HANDSHAKE_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// ProjectBundle
// ============================================================================
@NonNls
private const val PROJECT_BUNDLE = "messages.ProjectBundle"

internal object ProjectBundle {
    private val INSTANCE = DynamicBundle(ProjectBundle::class.java, PROJECT_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = PROJECT_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = PROJECT_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// ProjectConceptBundle
// ============================================================================
@NonNls
private const val PROJECT_CONCEPT_BUNDLE = "messages.ProjectConceptBundle"

internal object ProjectConceptBundle {
    private val INSTANCE = DynamicBundle(ProjectConceptBundle::class.java, PROJECT_CONCEPT_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = PROJECT_CONCEPT_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = PROJECT_CONCEPT_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// ProjectModelBundle
// ============================================================================
@NonNls
private const val PROJECT_MODEL_BUNDLE = "messages.ProjectModelBundle"

internal object ProjectModelBundle {
    private val INSTANCE = DynamicBundle(ProjectModelBundle::class.java, PROJECT_MODEL_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = PROJECT_MODEL_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = PROJECT_MODEL_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// PropertiesBundle
// ============================================================================
@NonNls
private const val PROPERTIES_BUNDLE = "messages.PropertiesBundle"

internal object PropertiesBundle {
    private val INSTANCE = DynamicBundle(PropertiesBundle::class.java, PROPERTIES_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = PROPERTIES_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = PROPERTIES_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// QueryParserMessages
// ============================================================================
@NonNls
private const val QUERY_PARSER_MESSAGES = "messages.QueryParserMessages"

internal object QueryParserMessages {
    private val INSTANCE = DynamicBundle(QueryParserMessages::class.java, QUERY_PARSER_MESSAGES)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = QUERY_PARSER_MESSAGES) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = QUERY_PARSER_MESSAGES) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// QuickFixBundle
// ============================================================================
@NonNls
private const val QUICK_FIX_BUNDLE = "messages.QuickFixBundle"

internal object QuickFixBundle {
    private val INSTANCE = DynamicBundle(QuickFixBundle::class.java, QUICK_FIX_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = QUICK_FIX_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = QUICK_FIX_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// RagIndexer
// ============================================================================
@NonNls
private const val RAG_INDEXER = "messages.RagIndexer"

internal object RagIndexer {
    private val INSTANCE = DynamicBundle(RagIndexer::class.java, RAG_INDEXER)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = RAG_INDEXER) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = RAG_INDEXER) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// RefactoringBundle
// ============================================================================
@NonNls
private const val REFACTORING_BUNDLE = "messages.RefactoringBundle"

internal object RefactoringBundle {
    private val INSTANCE = DynamicBundle(RefactoringBundle::class.java, REFACTORING_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = REFACTORING_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = REFACTORING_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// RefactorJBundle
// ============================================================================
@NonNls
private const val REFACTOR_JBUNDLE = "messages.RefactorJBundle"

internal object RefactorJBundle {
    private val INSTANCE = DynamicBundle(RefactorJBundle::class.java, REFACTOR_JBUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = REFACTOR_JBUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = REFACTOR_JBUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// RegExpBundle
// ============================================================================
@NonNls
private const val REG_EXP_BUNDLE = "messages.RegExpBundle"

internal object RegExpBundle {
    private val INSTANCE = DynamicBundle(RegExpBundle::class.java, REG_EXP_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = REG_EXP_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = REG_EXP_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// RelaxngBundle
// ============================================================================
@NonNls
private const val RELAXNG_BUNDLE = "messages.RelaxngBundle"

internal object RelaxngBundle {
    private val INSTANCE = DynamicBundle(RelaxngBundle::class.java, RELAXNG_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = RELAXNG_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = RELAXNG_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// RemoteBundle
// ============================================================================
@NonNls
private const val REMOTE_BUNDLE = "messages.RemoteBundle"

internal object RemoteBundle {
    private val INSTANCE = DynamicBundle(RemoteBundle::class.java, REMOTE_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = REMOTE_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = REMOTE_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// RemoteDevUtilBundle
// ============================================================================
@NonNls
private const val REMOTE_DEV_UTIL_BUNDLE = "messages.RemoteDevUtilBundle"

internal object RemoteDevUtilBundle {
    private val INSTANCE = DynamicBundle(RemoteDevUtilBundle::class.java, REMOTE_DEV_UTIL_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = REMOTE_DEV_UTIL_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = REMOTE_DEV_UTIL_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// RemoteProviderBundle
// ============================================================================
@NonNls
private const val REMOTE_PROVIDER_BUNDLE = "messages.RemoteProviderBundle"

internal object RemoteProviderBundle {
    private val INSTANCE = DynamicBundle(RemoteProviderBundle::class.java, REMOTE_PROVIDER_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = REMOTE_PROVIDER_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = REMOTE_PROVIDER_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// RenderingBundle
// ============================================================================
@NonNls
private const val RENDERING_BUNDLE = "messages.RenderingBundle"

internal object RenderingBundle {
    private val INSTANCE = DynamicBundle(RenderingBundle::class.java, RENDERING_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = RENDERING_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = RENDERING_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// RuntimeBundle
// ============================================================================
@NonNls
private const val RUNTIME_BUNDLE = "messages.RuntimeBundle"

internal object RuntimeBundle {
    private val INSTANCE = DynamicBundle(RuntimeBundle::class.java, RUNTIME_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = RUNTIME_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = RUNTIME_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// SamplesBrowserBundle
// ============================================================================
@NonNls
private const val SAMPLES_BROWSER_BUNDLE = "messages.SamplesBrowserBundle"

internal object SamplesBrowserBundle {
    private val INSTANCE = DynamicBundle(SamplesBrowserBundle::class.java, SAMPLES_BROWSER_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = SAMPLES_BROWSER_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = SAMPLES_BROWSER_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// ScriptDebuggerBundle
// ============================================================================
@NonNls
private const val SCRIPT_DEBUGGER_BUNDLE = "messages.ScriptDebuggerBundle"

internal object ScriptDebuggerBundle {
    private val INSTANCE = DynamicBundle(ScriptDebuggerBundle::class.java, SCRIPT_DEBUGGER_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = SCRIPT_DEBUGGER_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = SCRIPT_DEBUGGER_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// SettingsSyncBundle
// ============================================================================
@NonNls
private const val SETTINGS_SYNC_BUNDLE = "messages.SettingsSyncBundle"

internal object SettingsSyncBundle {
    private val INSTANCE = DynamicBundle(SettingsSyncBundle::class.java, SETTINGS_SYNC_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = SETTINGS_SYNC_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = SETTINGS_SYNC_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// SharedStreamDebuggerBundle
// ============================================================================
@NonNls
private const val SHARED_STREAM_DEBUGGER_BUNDLE = "messages.SharedStreamDebuggerBundle"

internal object SharedStreamDebuggerBundle {
    private val INSTANCE = DynamicBundle(SharedStreamDebuggerBundle::class.java, SHARED_STREAM_DEBUGGER_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = SHARED_STREAM_DEBUGGER_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = SHARED_STREAM_DEBUGGER_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// ShBundle
// ============================================================================
@NonNls
private const val SH_BUNDLE = "messages.ShBundle"

internal object ShBundle {
    private val INSTANCE = DynamicBundle(ShBundle::class.java, SH_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = SH_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = SH_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// SmlBundle
// ============================================================================
@NonNls
private const val SML_BUNDLE = "messages.SmlBundle"

internal object SmlBundle {
    private val INSTANCE = DynamicBundle(SmlBundle::class.java, SML_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = SML_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = SML_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// SmlIjBundle
// ============================================================================
@NonNls
private const val SML_IJ_BUNDLE = "messages.SmlIjBundle"

internal object SmlIjBundle {
    private val INSTANCE = DynamicBundle(SmlIjBundle::class.java, SML_IJ_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = SML_IJ_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = SML_IJ_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// SmRunnerBundle
// ============================================================================
@NonNls
private const val SM_RUNNER_BUNDLE = "messages.SmRunnerBundle"

internal object SmRunnerBundle {
    private val INSTANCE = DynamicBundle(SmRunnerBundle::class.java, SM_RUNNER_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = SM_RUNNER_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = SM_RUNNER_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// SpellCheckerBundle
// ============================================================================
@NonNls
private const val SPELL_CHECKER_BUNDLE = "messages.SpellCheckerBundle"

internal object SpellCheckerBundle {
    private val INSTANCE = DynamicBundle(SpellCheckerBundle::class.java, SPELL_CHECKER_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = SPELL_CHECKER_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = SPELL_CHECKER_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// SplittingTabsBundle
// ============================================================================
@NonNls
private const val SPLITTING_TABS_BUNDLE = "messages.SplittingTabsBundle"

internal object SplittingTabsBundle {
    private val INSTANCE = DynamicBundle(SplittingTabsBundle::class.java, SPLITTING_TABS_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = SPLITTING_TABS_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = SPLITTING_TABS_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// SSRBundle
// ============================================================================
@NonNls
private const val SSRBUNDLE = "messages.SSRBundle"

internal object SSRBundle {
    private val INSTANCE = DynamicBundle(SSRBundle::class.java, SSRBUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = SSRBUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = SSRBUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// StatisticsBundle
// ============================================================================
@NonNls
private const val STATISTICS_BUNDLE = "messages.StatisticsBundle"

internal object StatisticsBundle {
    private val INSTANCE = DynamicBundle(StatisticsBundle::class.java, STATISTICS_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = STATISTICS_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = STATISTICS_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// StreamDebuggerBundle
// ============================================================================
@NonNls
private const val STREAM_DEBUGGER_BUNDLE = "messages.StreamDebuggerBundle"

internal object StreamDebuggerBundle {
    private val INSTANCE = DynamicBundle(StreamDebuggerBundle::class.java, STREAM_DEBUGGER_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = STREAM_DEBUGGER_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = STREAM_DEBUGGER_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// StreamingBundle
// ============================================================================
@NonNls
private const val STREAMING_BUNDLE = "messages.StreamingBundle"

internal object StreamingBundle {
    private val INSTANCE = DynamicBundle(StreamingBundle::class.java, STREAMING_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = STREAMING_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = STREAMING_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// StructureViewBundle
// ============================================================================
@NonNls
private const val STRUCTURE_VIEW_BUNDLE = "messages.StructureViewBundle"

internal object StructureViewBundle {
    private val INSTANCE = DynamicBundle(StructureViewBundle::class.java, STRUCTURE_VIEW_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = STRUCTURE_VIEW_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = STRUCTURE_VIEW_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// StudioGeminiBundle
// ============================================================================
@NonNls
private const val STUDIO_GEMINI_BUNDLE = "messages.StudioGeminiBundle"

internal object StudioGeminiBundle {
    private val INSTANCE = DynamicBundle(StudioGeminiBundle::class.java, STUDIO_GEMINI_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = STUDIO_GEMINI_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = STUDIO_GEMINI_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// SvnBundle
// ============================================================================
@NonNls
private const val SVN_BUNDLE = "messages.SvnBundle"

internal object SvnBundle {
    private val INSTANCE = DynamicBundle(SvnBundle::class.java, SVN_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = SVN_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = SVN_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// SvnDeprecatedMessagesBundle
// ============================================================================
@NonNls
private const val SVN_DEPRECATED_MESSAGES_BUNDLE = "messages.SvnDeprecatedMessagesBundle"

internal object SvnDeprecatedMessagesBundle {
    private val INSTANCE = DynamicBundle(SvnDeprecatedMessagesBundle::class.java, SVN_DEPRECATED_MESSAGES_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = SVN_DEPRECATED_MESSAGES_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = SVN_DEPRECATED_MESSAGES_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// SymbolPickerBundle
// ============================================================================
@NonNls
private const val SYMBOL_PICKER_BUNDLE = "messages.SymbolPickerBundle"

internal object SymbolPickerBundle {
    private val INSTANCE = DynamicBundle(SymbolPickerBundle::class.java, SYMBOL_PICKER_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = SYMBOL_PICKER_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = SYMBOL_PICKER_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// SyntaxRuntimeBundle
// ============================================================================
@NonNls
private const val SYNTAX_RUNTIME_BUNDLE = "messages.SyntaxRuntimeBundle"

internal object SyntaxRuntimeBundle {
    private val INSTANCE = DynamicBundle(SyntaxRuntimeBundle::class.java, SYNTAX_RUNTIME_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = SYNTAX_RUNTIME_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = SYNTAX_RUNTIME_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// TaskApiBundle
// ============================================================================
@NonNls
private const val TASK_API_BUNDLE = "messages.TaskApiBundle"

internal object TaskApiBundle {
    private val INSTANCE = DynamicBundle(TaskApiBundle::class.java, TASK_API_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = TASK_API_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = TASK_API_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// TaskBundle
// ============================================================================
@NonNls
private const val TASK_BUNDLE = "messages.TaskBundle"

internal object TaskBundle {
    private val INSTANCE = DynamicBundle(TaskBundle::class.java, TASK_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = TASK_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = TASK_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// TemplatesBundle
// ============================================================================
@NonNls
private const val TEMPLATES_BUNDLE = "messages.TemplatesBundle"

internal object TemplatesBundle {
    private val INSTANCE = DynamicBundle(TemplatesBundle::class.java, TEMPLATES_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = TEMPLATES_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = TEMPLATES_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// TerminalBundle
// ============================================================================
@NonNls
private const val TERMINAL_BUNDLE = "messages.TerminalBundle"

internal object TerminalBundle {
    private val INSTANCE = DynamicBundle(TerminalBundle::class.java, TERMINAL_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = TERMINAL_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = TERMINAL_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// TerminalDeprecatedMessagesBundle
// ============================================================================
@NonNls
private const val TERMINAL_DEPRECATED_MESSAGES_BUNDLE = "messages.TerminalDeprecatedMessagesBundle"

internal object TerminalDeprecatedMessagesBundle {
    private val INSTANCE = DynamicBundle(TerminalDeprecatedMessagesBundle::class.java, TERMINAL_DEPRECATED_MESSAGES_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = TERMINAL_DEPRECATED_MESSAGES_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = TERMINAL_DEPRECATED_MESSAGES_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// TestngBundle
// ============================================================================
@NonNls
private const val TESTNG_BUNDLE = "messages.TestngBundle"

internal object TestngBundle {
    private val INSTANCE = DynamicBundle(TestngBundle::class.java, TESTNG_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = TESTNG_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = TESTNG_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// TestRunnerBundle
// ============================================================================
@NonNls
private const val TEST_RUNNER_BUNDLE = "messages.TestRunnerBundle"

internal object TestRunnerBundle {
    private val INSTANCE = DynamicBundle(TestRunnerBundle::class.java, TEST_RUNNER_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = TEST_RUNNER_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = TEST_RUNNER_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// TextMateBundle
// ============================================================================
@NonNls
private const val TEXT_MATE_BUNDLE = "messages.TextMateBundle"

internal object TextMateBundle {
    private val INSTANCE = DynamicBundle(TextMateBundle::class.java, TEXT_MATE_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = TEXT_MATE_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = TEXT_MATE_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// TomlBundle
// ============================================================================
@NonNls
private const val TOML_BUNDLE = "messages.TomlBundle"

internal object TomlBundle {
    private val INSTANCE = DynamicBundle(TomlBundle::class.java, TOML_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = TOML_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = TOML_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// ToolsBundle
// ============================================================================
@NonNls
private const val TOOLS_BUNDLE = "messages.ToolsBundle"

internal object ToolsBundle {
    private val INSTANCE = DynamicBundle(ToolsBundle::class.java, TOOLS_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = TOOLS_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = TOOLS_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// TurboCompleteKotlin
// ============================================================================
@NonNls
private const val TURBO_COMPLETE_KOTLIN = "messages.TurboCompleteKotlin"

internal object TurboCompleteKotlin {
    private val INSTANCE = DynamicBundle(TurboCompleteKotlin::class.java, TURBO_COMPLETE_KOTLIN)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = TURBO_COMPLETE_KOTLIN) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = TURBO_COMPLETE_KOTLIN) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// TypeMigrationBundle
// ============================================================================
@NonNls
private const val TYPE_MIGRATION_BUNDLE = "messages.TypeMigrationBundle"

internal object TypeMigrationBundle {
    private val INSTANCE = DynamicBundle(TypeMigrationBundle::class.java, TYPE_MIGRATION_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = TYPE_MIGRATION_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = TYPE_MIGRATION_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// TypoFixingBundle
// ============================================================================
@NonNls
private const val TYPO_FIXING_BUNDLE = "messages.TypoFixingBundle"

internal object TypoFixingBundle {
    private val INSTANCE = DynamicBundle(TypoFixingBundle::class.java, TYPO_FIXING_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = TYPO_FIXING_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = TYPO_FIXING_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// UIBundle
// ============================================================================
@NonNls
private const val UIBUNDLE = "messages.UIBundle"

internal object UIBundle {
    private val INSTANCE = DynamicBundle(UIBundle::class.java, UIBUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = UIBUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = UIBUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// UrlAssistBundle
// ============================================================================
@NonNls
private const val URL_ASSIST_BUNDLE = "messages.UrlAssistBundle"

internal object UrlAssistBundle {
    private val INSTANCE = DynamicBundle(UrlAssistBundle::class.java, URL_ASSIST_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = URL_ASSIST_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = URL_ASSIST_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// UsageViewBundle
// ============================================================================
@NonNls
private const val USAGE_VIEW_BUNDLE = "messages.UsageViewBundle"

internal object UsageViewBundle {
    private val INSTANCE = DynamicBundle(UsageViewBundle::class.java, USAGE_VIEW_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = USAGE_VIEW_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = USAGE_VIEW_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// UtilBundle
// ============================================================================
@NonNls
private const val UTIL_BUNDLE = "messages.UtilBundle"

internal object UtilBundle {
    private val INSTANCE = DynamicBundle(UtilBundle::class.java, UTIL_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = UTIL_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = UTIL_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// UtilUiBundle
// ============================================================================
@NonNls
private const val UTIL_UI_BUNDLE = "messages.UtilUiBundle"

internal object UtilUiBundle {
    private val INSTANCE = DynamicBundle(UtilUiBundle::class.java, UTIL_UI_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = UTIL_UI_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = UTIL_UI_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// VcsBundle
// ============================================================================
@NonNls
private const val VCS_BUNDLE = "messages.VcsBundle"

internal object VcsBundle {
    private val INSTANCE = DynamicBundle(VcsBundle::class.java, VCS_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = VCS_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = VCS_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// VcsFrontendBundle
// ============================================================================
@NonNls
private const val VCS_FRONTEND_BUNDLE = "messages.VcsFrontendBundle"

internal object VcsFrontendBundle {
    private val INSTANCE = DynamicBundle(VcsFrontendBundle::class.java, VCS_FRONTEND_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = VCS_FRONTEND_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = VCS_FRONTEND_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// VcsLogBundle
// ============================================================================
@NonNls
private const val VCS_LOG_BUNDLE = "messages.VcsLogBundle"

internal object VcsLogBundle {
    private val INSTANCE = DynamicBundle(VcsLogBundle::class.java, VCS_LOG_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = VCS_LOG_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = VCS_LOG_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// VcsProductivityFeatures
// ============================================================================
@NonNls
private const val VCS_PRODUCTIVITY_FEATURES = "messages.VcsProductivityFeatures"

internal object VcsProductivityFeatures {
    private val INSTANCE = DynamicBundle(VcsProductivityFeatures::class.java, VCS_PRODUCTIVITY_FEATURES)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = VCS_PRODUCTIVITY_FEATURES) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = VCS_PRODUCTIVITY_FEATURES) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// VMOptionsBundle
// ============================================================================
@NonNls
private const val VMOPTIONS_BUNDLE = "messages.VMOptionsBundle"

internal object VMOptionsBundle {
    private val INSTANCE = DynamicBundle(VMOptionsBundle::class.java, VMOPTIONS_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = VMOPTIONS_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = VMOPTIONS_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// WearDwfBundle
// ============================================================================
@NonNls
private const val WEAR_DWF_BUNDLE = "messages.WearDwfBundle"

internal object WearDwfBundle {
    private val INSTANCE = DynamicBundle(WearDwfBundle::class.java, WEAR_DWF_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = WEAR_DWF_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = WEAR_DWF_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// WearWhsBundle
// ============================================================================
@NonNls
private const val WEAR_WHS_BUNDLE = "messages.WearWhsBundle"

internal object WearWhsBundle {
    private val INSTANCE = DynamicBundle(WearWhsBundle::class.java, WEAR_WHS_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = WEAR_WHS_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = WEAR_WHS_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// WorkspaceModelIdeBundle
// ============================================================================
@NonNls
private const val WORKSPACE_MODEL_IDE_BUNDLE = "messages.WorkspaceModelIdeBundle"

internal object WorkspaceModelIdeBundle {
    private val INSTANCE = DynamicBundle(WorkspaceModelIdeBundle::class.java, WORKSPACE_MODEL_IDE_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = WORKSPACE_MODEL_IDE_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = WORKSPACE_MODEL_IDE_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// WorkspaceModelJpsBundle
// ============================================================================
@NonNls
private const val WORKSPACE_MODEL_JPS_BUNDLE = "messages.WorkspaceModelJpsBundle"

internal object WorkspaceModelJpsBundle {
    private val INSTANCE = DynamicBundle(WorkspaceModelJpsBundle::class.java, WORKSPACE_MODEL_JPS_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = WORKSPACE_MODEL_JPS_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = WORKSPACE_MODEL_JPS_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// WSLBundle
// ============================================================================
@NonNls
private const val WSLBUNDLE = "messages.WSLBundle"

internal object WSLBundle {
    private val INSTANCE = DynamicBundle(WSLBundle::class.java, WSLBUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = WSLBUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = WSLBUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// XDebuggerBundle
// ============================================================================
@NonNls
private const val XDEBUGGER_BUNDLE = "messages.XDebuggerBundle"

internal object XDebuggerBundle {
    private val INSTANCE = DynamicBundle(XDebuggerBundle::class.java, XDEBUGGER_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = XDEBUGGER_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = XDEBUGGER_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// XmlAnalysisBundle
// ============================================================================
@NonNls
private const val XML_ANALYSIS_BUNDLE = "messages.XmlAnalysisBundle"

internal object XmlAnalysisBundle {
    private val INSTANCE = DynamicBundle(XmlAnalysisBundle::class.java, XML_ANALYSIS_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = XML_ANALYSIS_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = XML_ANALYSIS_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// XmlBundle
// ============================================================================
@NonNls
private const val XML_BUNDLE = "messages.XmlBundle"

internal object XmlBundle {
    private val INSTANCE = DynamicBundle(XmlBundle::class.java, XML_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = XML_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = XML_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// XmlCoreBundle
// ============================================================================
@NonNls
private const val XML_CORE_BUNDLE = "messages.XmlCoreBundle"

internal object XmlCoreBundle {
    private val INSTANCE = DynamicBundle(XmlCoreBundle::class.java, XML_CORE_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = XML_CORE_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = XML_CORE_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// XmlDomBundle
// ============================================================================
@NonNls
private const val XML_DOM_BUNDLE = "messages.XmlDomBundle"

internal object XmlDomBundle {
    private val INSTANCE = DynamicBundle(XmlDomBundle::class.java, XML_DOM_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = XML_DOM_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = XML_DOM_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// XmlParserBundle
// ============================================================================
@NonNls
private const val XML_PARSER_BUNDLE = "messages.XmlParserBundle"

internal object XmlParserBundle {
    private val INSTANCE = DynamicBundle(XmlParserBundle::class.java, XML_PARSER_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = XML_PARSER_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = XML_PARSER_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// XmlPsiBundle
// ============================================================================
@NonNls
private const val XML_PSI_BUNDLE = "messages.XmlPsiBundle"

internal object XmlPsiBundle {
    private val INSTANCE = DynamicBundle(XmlPsiBundle::class.java, XML_PSI_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = XML_PSI_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = XML_PSI_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// XmlSyntaxBundle
// ============================================================================
@NonNls
private const val XML_SYNTAX_BUNDLE = "messages.XmlSyntaxBundle"

internal object XmlSyntaxBundle {
    private val INSTANCE = DynamicBundle(XmlSyntaxBundle::class.java, XML_SYNTAX_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = XML_SYNTAX_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = XML_SYNTAX_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// XmlUiBundle
// ============================================================================
@NonNls
private const val XML_UI_BUNDLE = "messages.XmlUiBundle"

internal object XmlUiBundle {
    private val INSTANCE = DynamicBundle(XmlUiBundle::class.java, XML_UI_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = XML_UI_BUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = XML_UI_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

// ============================================================================
// YAMLBundle
// ============================================================================
@NonNls
private const val YAMLBUNDLE = "messages.YAMLBundle"

internal object YAMLBundle {
    private val INSTANCE = DynamicBundle(YAMLBundle::class.java, YAMLBUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = YAMLBUNDLE) key: String,
        vararg params: Any
    ): String = INSTANCE.getMessage(key, *params)

    fun lazyMessage(
        @PropertyKey(resourceBundle = YAMLBUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> = INSTANCE.getLazyMessage(key, *params)
}

