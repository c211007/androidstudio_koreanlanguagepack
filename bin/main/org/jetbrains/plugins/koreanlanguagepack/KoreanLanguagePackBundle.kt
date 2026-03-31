package org.jetbrains.plugins.koreanlanguagepack

import org.jetbrains.annotations.Nls
import org.jetbrains.annotations.NonNls
import org.jetbrains.annotations.PropertyKey
import java.util.function.Supplier
/**
 * Android Studio 한국어 언어팩 번들 관리자
 * 
 * 이 객체는 messages/ 폴더 내의 모든 .properties 파일에 대한
 * 통합 액세스를 제공합니다.
 * 
 * 사용 예시:
 * ```kotlin
 * // 단일 번들 메시지 가져오기
 * val msg = KoreanLanguagePackBundle.message("ActionsBundle", "action.key")
 * 
 * // 지연 로드 메시지 가져오기
 * val lazyMsg = KoreanLanguagePackBundle.lazyMessage("IdeBundle", "ide.key")
 * 
 * // 특정 번들 인스턴스 가져오기
 * val bundle = KoreanLanguagePackBundle.getBundle("KotlinBundle")
 * ```
 */
object KoreanLanguagePackBundle {
    
    @NonNls
    private const val BUNDLE_PATH_PREFIX = "messages."
    
    // 번들 캐시 - 각 번들은 최초 접근 시 로드됨
    private val bundleCache = mutableMapOf<String, DynamicBundle>()
    
    /**
     * 사전 정의된 주요 번들 목록
     * plugin.xml에 등록된 번들들 중 핵심 번들
     */
    @NonNls
    val CORE_BUNDLES = listOf(
        // Core IDE
        "ActionsBundle",
        "ApplicationBundle", 
        "IdeBundle",
        "EditorBundle",
        "CodeInsightBundle",
        
        // Android
        "AndroidBundle",
        "AndroidLintBundle",
        
        // Languages
        "JavaBundle",
        "KotlinBundle",
        "GroovyBundle",
        
        // VCS
        "GitBundle",
        "VcsBundle",
        
        // UI
        "UIBundle",
        "OptionsBundle"
    )
    
    /**
     * 특정 번들에서 메시지를 가져옵니다.
     * 
     * @param bundleName 번들 이름 (예: "ActionsBundle", "AndroidBundle")
     * @param key 메시지 키
     * @param params 메시지 파라미터
     * @return 번역된 메시지 문자열
     */
    @Nls
    fun message(
        @NonNls bundleName: String,
        @NonNls key: String,
        vararg params: Any
    ): String {
        return getBundle(bundleName).getMessage(key, *params)
    }
    
    /**
     * 특정 번들에서 메시지를 가져옵니다. (안전한 버전)
     * 키가 없으면 null을 반환합니다.
     * 
     * @param bundleName 번들 이름
     * @param key 메시지 키
     * @param params 메시지 파라미터
     * @return 번역된 메시지 또는 null
     */
    @Nls
    fun messageOrNull(
        @NonNls bundleName: String,
        @NonNls key: String,
        vararg params: Any
    ): String? {
        return try {
            getBundle(bundleName).getMessage(key, *params)
        } catch (e: Exception) {
            null
        }
    }
    
    /**
     * 특정 번들에서 지연 로드 메시지를 가져옵니다.
     * 
     * @param bundleName 번들 이름
     * @param key 메시지 키
     * @param params 메시지 파라미터
     * @return Supplier로 래핑된 지연 로드 메시지
     */
    fun lazyMessage(
        @NonNls bundleName: String,
        @NonNls key: String,
        vararg params: Any
    ): Supplier<@Nls String> {
        return getBundle(bundleName).getLazyMessage(key, *params)
    }
    
    /**
     * 특정 번들의 DynamicBundle 인스턴스를 가져옵니다.
     * 캐시된 인스턴스를 반환하거나, 없으면 새로 생성합니다.
     * 
     * @param bundleName 번들 이름 (예: "ActionsBundle")
     * @return DynamicBundle 인스턴스
     */
    @Synchronized
    fun getBundle(@NonNls bundleName: String): DynamicBundle {
        return bundleCache.getOrPut(bundleName) {
            DynamicBundle(
                KoreanLanguagePackBundle::class.java,
                "$BUNDLE_PATH_PREFIX$bundleName"
            )
        }
    }
    
    /**
     * 번들이 존재하는지 확인합니다.
     * 
     * @param bundleName 번들 이름
     * @return 번들이 존재하면 true
     */
    fun hasBundle(@NonNls bundleName: String): Boolean {
        return try {
            val resourcePath = "/$BUNDLE_PATH_PREFIX$bundleName.properties".replace(".", "/")
            KoreanLanguagePackBundle::class.java.getResource(resourcePath) != null
        } catch (e: Exception) {
            false
        }
    }
    
    /**
     * 캐시된 모든 번들을 지웁니다.
     * 테스트나 리로드 시 사용합니다.
     */
    @Synchronized
    fun clearCache() {
        bundleCache.clear()
    }
    
    /**
     * 현재 캐시된 번들 이름 목록을 반환합니다.
     */
    fun getCachedBundleNames(): Set<String> = bundleCache.keys.toSet()
}

// 편의를 위한 확장 함수들

/**
 * ActionsBundle에서 메시지를 가져오는 편의 함수
 */
@Nls
fun actionsMessage(@NonNls key: String, vararg params: Any): String =
    KoreanLanguagePackBundle.message("ActionsBundle", key, *params)

/**
 * AndroidBundle에서 메시지를 가져오는 편의 함수
 */
@Nls
fun androidMessage(@NonNls key: String, vararg params: Any): String =
    KoreanLanguagePackBundle.message("AndroidBundle", key, *params)

/**
 * IdeBundle에서 메시지를 가져오는 편의 함수
 */
@Nls
fun ideMessage(@NonNls key: String, vararg params: Any): String =
    KoreanLanguagePackBundle.message("IdeBundle", key, *params)

/**
 * KotlinBundle에서 메시지를 가져오는 편의 함수
 */
@Nls
fun kotlinMessage(@NonNls key: String, vararg params: Any): String =
    KoreanLanguagePackBundle.message("KotlinBundle", key, *params)
