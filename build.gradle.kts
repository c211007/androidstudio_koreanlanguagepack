import org.jetbrains.changelog.markdownToHTML
import org.jetbrains.changelog.Changelog
import org.jetbrains.intellij.platform.gradle.IntelliJPlatformType
import org.jetbrains.intellij.platform.gradle.models.ProductRelease
import java.util.Properties
import java.io.FileInputStream
plugins {

    id("java") // Java support
    id("org.jetbrains.intellij.platform")
    alias(libs.plugins.kotlin) // Kotlin support
    alias(libs.plugins.changelog) // Gradle Changelog Plugin
    alias(libs.plugins.qodana) // Gradle Qodana Plugin
    alias(libs.plugins.kover) // Gradle Kover Plugin
}
group = providers.gradleProperty("pluginGroup").get()
version = providers.gradleProperty("pluginVersion").get()

// Configure project's dependencies
repositories {
    mavenCentral()

    // IntelliJ Platform Gradle Plugin Repositories Extension - read more: https://plugins.jetbrains.com/docs/intellij/tools-intellij-platform-gradle-plugin-repositories-extension.html
    intellijPlatform {
        //releases  마켓플레이스
        defaultRepositories()
    }
}
// gradle.properties의 종속성해결 Dependencies are managed with Gradle version catalog - read more: https://docs.gradle.org/current/userguide/version_catalogs.html
dependencies {
    // IntelliJ Platform Gradle Plugin Dependencies Extension - read more: https://plugins.jetbrains.com/docs/intellij/tools-intellij-platform-gradle-plugin-dependencies-extension.html
    intellijPlatform {
        val type = providers.gradleProperty("platformType")
        val version = providers.gradleProperty("platformVersion")
        
        // Use Android Studio dependency from the web
        androidStudio(version.get())
        bundledPlugin("org.jetbrains.android")
        // Plugin Dependencies. Uses `platformBundledPlugins` property from the gradle.properties file for bundled IntelliJ Platform plugins.
        // bundledPlugins(providers.gradleProperty("platformBundledPlugins").map { it.split(',') })

        // Plugin Dependencies. Uses `platformPlugins` property from the gradle.properties file for plugin from JetBrains Marketplace.
        plugins(providers.gradleProperty("platformPlugins").map { it.split(',') })

        // Module Dependencies. Uses `platformBundledModules` property from the gradle.properties file for bundled IntelliJ Platform modules.
        bundledModules(providers.gradleProperty("platformBundledModules").map { it.split(',') })
        
    }
}

tasks {
  // Set the JVM compatibility versions
    java {
        toolchain {
            languageVersion.set(JavaLanguageVersion.of(21))
        }
    }
    kotlin {
        jvmToolchain(21)
    }
}


// publishPlugin {
//   token.set(providers.environmentVariable("PUBLISH_TOKEN"))
// }추후에추가 

sourceSets {
    main {
        kotlin {
            setSrcDirs(listOf("src/main/kotlin"))
        }
        resources {
            setSrcDirs(listOf("src/main/resources"))
        }
    }
}
// Configure IntelliJ Platform Gradle Plugin - read more: https://plugins.jetbrains.com/docs/intellij/tools-intellij-platform-gradle-plugin-extension.html


// local.properties 파일 읽어오기
val localProperties = Properties()
val localPropertiesFile = rootProject.file("local.properties")
if (localPropertiesFile.exists()) {
    localProperties.load(FileInputStream(localPropertiesFile))
}

tasks {
    signPlugin {
        certificateChainFile.set(file("cert/chain.crt"))
        privateKeyFile.set(file("cert/private.pem"))
        // 파일에 적어둔 비밀번호를 변수로 불러옵니다
        password.set(localProperties.getProperty("PRIVATE_KEY_PASSWORD")) 
    }
}
intellijPlatform{
//    platformPath :intellij플랫폼 경로https://plugins.jetbrains.com/docs/intellij/tools-intellij-platform-gradle-plugin-extension.html#intellijPlatform-productInfo
    buildSearchableOptions=false
    instrumentCode = false
    autoReload=true
}
intellijPlatform {
    pluginConfiguration {
        id="androidstudio.koreanlanguagepack"
        name = providers.gradleProperty("pluginName")
        version = providers.gradleProperty("pluginVersion")
        group = providers.gradleProperty("pluginGroup").get()
        // Extract the <!-- Plugin description --> section from README.md and provide for the plugin's manifest
        // description = providers.fileContents(layout.projectDirectory.file("README.md")).asText.map {
        //     val start = "<!-- Plugin description -->"
        //     val end = "<!-- Plugin description end -->"

        //     with(it.lines()) {
        //         if (!containsAll(listOf(start, end))) {
        //             throw GradleException("Plugin description section not found in README.md:\n$start ... $end")
        //         }
        //         subList(indexOf(start) + 1, indexOf(end)).joinToString("\n").let(::markdownToHTML)
        //     }
        // }

        val changelog = project.changelog // local variable for configuration cache compatibility
        // Get the latest available change notes from the changelog file
        changeNotes = providers.gradleProperty("pluginVersion").map { pluginVersion ->
            with(changelog) {
                renderItem(
                    (getOrNull(pluginVersion) ?: getUnreleased())
                        .withHeader(false)
                        .withEmptySections(false),
                    Changelog.OutputType.HTML,
                )
            }
        }


        ideaVersion {
            sinceBuild = providers.gradleProperty("pluginSinceBuild")
        }

        vendor{
            name="KangJeongMo"
            email="C211007@g.hongik.ac.kr"
            url="https://github.com/c211007/androidstudio_koreanlanguagepack"
        }
    }
//    caching.ides {
//        enabled=true
//        path = layout.projectDirectory.dir(".intellijPlatform/ides")
//        name = { requested -> "${requested.type}-${requested.version}" }
//    }
    publishing {
        //host = ""
        token = providers.environmentVariable("PUBLISH_TOKEN")
        ideServices = false
        hidden = false

        // The pluginVersion is based on the SemVer (https://semver.org) and supports pre-release labels, like 2.1.7-alpha.3
        // Specify pre-release label to publish the plugin in a custom Release Channel automatically. Read more:
        // https://plugins.jetbrains.com/docs/intellij/publishing-plugin.html#specifying-a-release-channel
        channels = providers.gradleProperty("pluginVersion").map { listOf(it.substringAfter('-', "").substringBefore('.').ifEmpty { "default" }) }
    }

//    signing {
//        cliPath = file("/path/to/marketplace-zip-signer-cli.jar")
//        keyStore = file("/path/to/keyStore.ks")
//        keyStorePassword = "..."
//        keyStoreKeyAlias = "..."
//        keyStoreType = "..."
//        keyStoreProviderName = "..."
//        privateKey = "..."
//        privateKeyFile = file("/path/to/private.pem")
//        password = "..."
//        certificateChain = "..."
//        certificateChainFile = file("/path/to/chain.crt")
//    }



    pluginVerification {
        ides {
            val type = providers.gradleProperty("platformType")
            val version = providers.gradleProperty("platformVersion")
            
//            ide(IntelliJPlatformType.AndroidStudio, version.get())
            // local("/.intellijPlatform/ides/${type.get()}-${version.get()}/android-studio")
        }
    }
}

// Configure Gradle Changelog Plugin - read more: https://github.com/JetBrains/gradle-changelog-plugin
changelog {
    groups.empty()
    repositoryUrl = providers.gradleProperty("pluginRepositoryUrl")
    versionPrefix = ""
}

tasks {
    wrapper {
        gradleVersion = providers.gradleProperty("gradleVersion").get()
    }

    publishPlugin {
        dependsOn(patchChangelog)
    }

    // Disable tests as this is a language pack with no test files
    test {
        enabled = false
    }
}
