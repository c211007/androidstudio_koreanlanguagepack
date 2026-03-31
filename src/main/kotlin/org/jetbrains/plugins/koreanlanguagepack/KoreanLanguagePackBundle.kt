package org.jetbrains.plugins.koreanlanguagepack

import com.intellij.DynamicBundle
import org.jetbrains.annotations.Nls
import org.jetbrains.annotations.NonNls
import org.jetbrains.annotations.PropertyKey
import java.util.function.Supplier

/**
 * Android Studio 한국어 언어팩 - ActionsBundle 번들
 * 
 * JetBrains 공식 가이드에 따른 구현:
 * https://plugins.jetbrains.com/docs/intellij/internationalization.html
 */
@NonNls
private const val ACTIONS_BUNDLE = "messages.ActionsBundle"

internal object ActionsBundle {
    private val INSTANCE = DynamicBundle(ActionsBundle::class.java, ACTIONS_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = ACTIONS_BUNDLE) key: String,
        vararg params: Any
    ): String {
        return INSTANCE.getMessage(key, *params)
    }

    fun lazyMessage(
        @PropertyKey(resourceBundle = ACTIONS_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> {
        return INSTANCE.getLazyMessage(key, *params)
    }
}

/**
 * Android Studio 한국어 언어팩 - AndroidBundle 번들
 */
@NonNls
private const val ANDROID_BUNDLE = "messages.AndroidBundle"

internal object AndroidBundle {
    private val INSTANCE = DynamicBundle(AndroidBundle::class.java, ANDROID_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = ANDROID_BUNDLE) key: String,
        vararg params: Any
    ): String {
        return INSTANCE.getMessage(key, *params)
    }

    fun lazyMessage(
        @PropertyKey(resourceBundle = ANDROID_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> {
        return INSTANCE.getLazyMessage(key, *params)
    }
}

/**
 * Android Studio 한국어 언어팩 - IdeBundle 번들
 */
@NonNls
private const val IDE_BUNDLE = "messages.IdeBundle"

internal object IdeBundle {
    private val INSTANCE = DynamicBundle(IdeBundle::class.java, IDE_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = IDE_BUNDLE) key: String,
        vararg params: Any
    ): String {
        return INSTANCE.getMessage(key, *params)
    }

    fun lazyMessage(
        @PropertyKey(resourceBundle = IDE_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> {
        return INSTANCE.getLazyMessage(key, *params)
    }
}

/**
 * Android Studio 한국어 언어팩 - KotlinBundle 번들
 */
@NonNls
private const val KOTLIN_BUNDLE = "messages.KotlinBundle"

internal object KotlinBundle {
    private val INSTANCE = DynamicBundle(KotlinBundle::class.java, KOTLIN_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = KOTLIN_BUNDLE) key: String,
        vararg params: Any
    ): String {
        return INSTANCE.getMessage(key, *params)
    }

    fun lazyMessage(
        @PropertyKey(resourceBundle = KOTLIN_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> {
        return INSTANCE.getLazyMessage(key, *params)
    }
}

/**
 * Android Studio 한국어 언어팩 - JavaBundle 번들
 */
@NonNls
private const val JAVA_BUNDLE = "messages.JavaBundle"

internal object JavaBundle {
    private val INSTANCE = DynamicBundle(JavaBundle::class.java, JAVA_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = JAVA_BUNDLE) key: String,
        vararg params: Any
    ): String {
        return INSTANCE.getMessage(key, *params)
    }

    fun lazyMessage(
        @PropertyKey(resourceBundle = JAVA_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> {
        return INSTANCE.getLazyMessage(key, *params)
    }
}

/**
 * Android Studio 한국어 언어팩 - GitBundle 번들
 */
@NonNls
private const val GIT_BUNDLE = "messages.GitBundle"

internal object GitBundle {
    private val INSTANCE = DynamicBundle(GitBundle::class.java, GIT_BUNDLE)

    @Nls
    fun message(
        @PropertyKey(resourceBundle = GIT_BUNDLE) key: String,
        vararg params: Any
    ): String {
        return INSTANCE.getMessage(key, *params)
    }

    fun lazyMessage(
        @PropertyKey(resourceBundle = GIT_BUNDLE) key: String,
        vararg params: Any
    ): Supplier<@Nls String> {
        return INSTANCE.getLazyMessage(key, *params)
    }
}
