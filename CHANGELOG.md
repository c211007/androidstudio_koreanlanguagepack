<!-- Keep a Changelog guide -> https://keepachangelog.com -->

# androidstudio_koreanlanguagepack Changelog

## [Unreleased]

## [2.0.0]
### Added
- Runtime action-text override system for menus/tool windows whose text is hardcoded in plugin.xml or recomputed on every `update()` call (these could not be translated through resource bundles alone)
- Diagnostic scanner that reports any remaining untranslated action/group text at runtime

### Fixed
- Large number of previously-untranslated menu items across Android, Compose, NDK, Gradle, Git, and debugger-related actions

## [1.0.0]
### Added
- Initial scaffold created from [IntelliJ Platform Plugin Template](https://github.com/JetBrains/intellij-platform-plugin-template)
