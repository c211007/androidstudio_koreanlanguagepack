$baseNames = @('CCorePluginResources', 'CertPathReviewerMessages', 'ChangeGeneratorMessages', 'commonMessages', 'ComposePreviewBundle', 'CoreModelMessages', 'DfsText', 'ErrorPane', 'FastPreview', 'GlancePreviewBundle', 'GoogleLoginBundle', 'JGitText', 'LiveEdit', 'LoginPane', 'message', 'Messages', 'MessagesBundle', 'plugin', 'PreviewBundle', 'RepoText', 'SearchField', 'SettingsModelMessages', 'SshdText', 'strings', 'swingx', 'SWTMessages', 'Texts', 'TipOfTheDay', 'UtilMessages', 'WearBundle')
$ktPath = 'androidstudio_koreanlanguagepack\src\main\kotlin\org\jetbrains\plugins\koreanlanguagepack\KoreanLanguagePackBundle.kt'
$ktLines = [System.IO.File]::ReadAllLines($ktPath)
$ktInsertLines = @()
foreach ($name in $baseNames) {
    if (($ktLines -match "internal object $name ").Count -eq 0) {
        $upperSnake = $name -creplace '([a-z])([A-Z])', '$1_$2'
        $upperSnake = $upperSnake.ToUpper()

        $ktInsertLines += ""
        $ktInsertLines += "// ============================================================================"
        $ktInsertLines += "// $name"
        $ktInsertLines += "// ============================================================================"
        $ktInsertLines += "@NonNls"
        $ktInsertLines += "private const val $($upperSnake)_BUNDLE = "messages.$name""
        $ktInsertLines += ""
        $ktInsertLines += "internal object $name {"
        $ktInsertLines += "    @JvmStatic"
        $ktInsertLines += "    fun message(@PropertyKey(resourceBundle = $($upperSnake)_BUNDLE) key: String, vararg params: Any): @Nls String {"
        $ktInsertLines += "        return DynamicBundle.getMessage($($upperSnake)_BUNDLE, key, *params)"
        $ktInsertLines += "    }"
        $ktInsertLines += ""
        $ktInsertLines += "    @JvmStatic"
        $ktInsertLines += "    fun messagePointer(@PropertyKey(resourceBundle = $($upperSnake)_BUNDLE) key: String, vararg params: Any): Supplier<@Nls String> {"
        $ktInsertLines += "        return DynamicBundle.getLazyMessage($($upperSnake)_BUNDLE, key, *params)"
        $ktInsertLines += "    }"
        $ktInsertLines += "}"
    }
}
if ($ktInsertLines.Count -gt 0) {
    [System.IO.File]::AppendAllLines($ktPath, $ktInsertLines, [System.Text.Encoding]::UTF8)
    Write-Output "KT correctly injected."
}
