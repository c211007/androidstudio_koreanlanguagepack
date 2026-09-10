# Android Studio Korean Language Pack
test제외빌드방법:  .\gradlew buildPlugin -x test
![Build](https://github.com/c211007/androidstudio_koreanlanguagepack/workflows/Build/badge.svg)
[![Version](https://img.shields.io/jetbrains/plugin/v/MARKETPLACE_ID.svg)](https://plugins.jetbrains.com/plugin/MARKETPLACE_ID)
[![Downloads](https://img.shields.io/jetbrains/plugin/d/MARKETPLACE_ID.svg)](https://plugins.jetbrains.com/plugin/MARKETPLACE_ID)

## Overview

Complete Korean (한국어) localization plugin for **Android Studio**. Translates the entire UI including menus, dialogs, settings, and tooltips to provide a seamless Korean language experience.

## Features

- ✅ **Full UI Translation** - Menus, dialogs, preferences, and settings in Korean
- ✅ **Seamless Integration** - Works with all Android Studio versions (2025.2+)
- ✅ **Easy Installation** - One-click install from JetBrains Marketplace
- ✅ **Regular Updates** - Synchronized with Android Studio releases

## Localization Progress

- [x] **v1.0** - Core menus and basic UI (File, Edit, View, Build, Run menus)
- [ ] **v1.1** - Settings/Preferences tabs
- [ ] **v1.2** - Dialog messages and tooltips
- [ ] **v2.0** - Complete Android Studio UI coverage

## Development Checklist

- [x] Set up IntelliJ Platform Plugin Template
- [x] Add Android Studio module dependencies
- [x] Configure Korean resource bundles (messages_ko.properties)
- [ ] Implement core UI translations
- [ ] Test in Android Studio environment
- [ ] Publish to JetBrains Marketplace
- [ ] Set up CI/CD pipeline
- [ ] Community contribution guidelines

<!-- 아래 두 HTML 주석 마커 사이의 내용은 빌드 시 build.gradle.kts가 그대로 읽어서
     plugin.xml의 description과 마켓플레이스 상세 페이지에 그대로 노출한다.
     마커 줄이나 이 안내문 줄을 지우지 말고, 마커 사이에는 순수 텍스트 한 줄만 둘 것
     (마크다운 서식은 변환 없이 그대로 노출되므로 쓰지 말 것).
     주의: 마켓플레이스 검증기가 앞부분(대략 첫 40자) 구간에 한글 등 비라틴 문자가
     섞여 있으면 "must start with Latin characters" 오류를 낸다. 한글은 절대 넣지 말 것. -->
<!-- Plugin description -->
Complete Korean localization for Android Studio UI, including menus, dialogs, settings, and tooltips. Provides a seamless experience for Korean developers using Android Studio.
<!-- Plugin description end -->

## 개발자용 문서

- [번역이 적용되는 원리와 조사 과정](docs/TRANSLATION_MECHANISM.md) — 왜 일부 메뉴만 번역이 안 됐는지, IntelliJ 플랫폼에서 텍스트가 화면에 나오는 3가지 경로와 각각의 대응 방법을 정리한 문서

## Installation

- Using the IDE built-in plugin system:

  <kbd>Settings/Preferences</kbd> > <kbd>Plugins</kbd> > <kbd>Marketplace</kbd> > <kbd>Search for "androidstudio_koreanlanguagepack"</kbd> >
  <kbd>Install</kbd>

- Using JetBrains Marketplace:

  Go to [JetBrains Marketplace](https://plugins.jetbrains.com/plugin/MARKETPLACE_ID) and install it by clicking the <kbd>Install to ...</kbd> button in case your IDE is running.

  You can also download the [latest release](https://plugins.jetbrains.com/plugin/MARKETPLACE_ID/versions) from JetBrains Marketplace and install it manually using
  <kbd>Settings/Preferences</kbd> > <kbd>Plugins</kbd> > <kbd>⚙️</kbd> > <kbd>Install plugin from disk...</kbd>

- Manually:

  Download the [latest release](https://github.com/c211007/androidstudio_koreanlanguagepack/releases/latest) and install it manually using
  <kbd>Settings/Preferences</kbd> > <kbd>Plugins</kbd> > <kbd>⚙️</kbd> > <kbd>Install plugin from disk...</kbd>


---
Plugin based on the [IntelliJ Platform Plugin Template][template].

[template]: https://github.com/JetBrains/intellij-platform-plugin-template
[docs:plugin-description]: https://plugins.jetbrains.com/docs/intellij/plugin-user-experience.html#plugin-description-and-presentation
