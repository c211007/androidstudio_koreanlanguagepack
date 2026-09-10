# -*- coding: utf-8 -*-
"""
missing_translations/missing_action_texts.json 에 있는, plugin.xml에 인라인으로
박혀있던 action/group text=/description= 들을 번역해서 ActionsBundle.properties 끝에 추가한다.

주의: main()(ActionsBundle.properties에 실제로 쓰는 부분)은 이미 한 번 실행되어 반영됐다.
다시 실행하면 같은 줄이 중복으로 append된다. 이 파일에서 지금도 계속 쓰이는 건
main()이 아니라 아래 TRANSLATIONS 딕셔너리 그 자체다 — generate_action_override_kotlin.py가
이걸 그대로 읽어서 InlineActionTextOverrides.kt를 만든다. (ActionsBundle.properties에 넣는
방식 자체는 인라인 텍스트 액션에는 안 통한다는 게 나중에 밝혀졌다 — TRANSLATION_MECHANISM.md
경로 B 참고. 그래도 키가 이미 반영돼 있어서 되돌릴 필요는 없다.)
"""
import json
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# 이 파일은 <repo_root>/tools/translation/ 안에 있으므로 두 단계 위가 REPO_ROOT다.
REPO_ROOT = os.path.dirname(os.path.dirname(SCRIPT_DIR))
MISSING_PATH = os.path.join(REPO_ROOT, "missing_translations", "missing_action_texts.json")
ACTIONS_BUNDLE_PATH = os.path.join(REPO_ROOT, "src", "main", "resources", "messages", "ActionsBundle.properties")

# id -> (번역된 text 또는 None, 번역된 description 또는 None)
TRANSLATIONS = {
    # core
    "Jcef.ContextMenuGroup": ("JCEF 프런트엔드 작업", None),
    "CreateAllServicesAndExtensions": ("모든 서비스 및 확장 생성", None),
    "DropAnError": ("오류 발생시키기", "SHIFT를 누르고 있으면 예외가 연속으로 발생합니다"),
    "DropAnErrorWithAttachments": ("첨부 파일이 있는 오류 발생시키기", "SHIFT를 누르고 있으면 여러 첨부 파일이 생성됩니다"),
    "DropPluginError": ("임의의 플러그인에서 오류 발생시키기", "SHIFT를 누르고 있으면 서드파티 플러그인에서만 발생합니다"),
    "DropAnOutOfMemoryError": ("OutOfMemoryError 발생시키기", "SHIFT를 누르고 있으면 Metaspace에서 OOME가 발생합니다"),
    "PrintModulesAndEntitySources": ("모듈 및 엔티티 소스를 로그에 출력", None),
    "ShowPoweredProgress": ("Powered Progress 표시", None),
    "ShowWorkspaceFileState": ("워크스페이스 파일 상태 표시", None),

    # Kotlin
    "ReactivePostOpenProjectActionsAction": ("Kotlin 프로젝트 열기 후 작업", None),

    # android
    "Adtui.ZoomInAction": ("확대", "미리보기 확대"),
    "Adtui.ZoomOutAction": ("축소", "미리보기 축소"),
    "Adtui.ZoomToActualAction": ("실제 크기로 보기(100%)", "미리보기를 실제 크기로 표시"),
    "Adtui.ZoomToFitAction": ("화면에 맞추기", "미리보기를 화면 크기에 맞춤"),
    "Adtui.ZoomResetAction": ("확대/축소 재설정", "확대/축소 수준을 기본값으로 재설정"),
    "com.android.tools.adtui.webp.WebpSupportTestAction": ("WebP 지원 테스트 작업", None),
    "com.android.screenshottest.action.UpdateReferenceImagesAction": ("참조 이미지 추가/업데이트", "거터 아이콘에서 참조 이미지를 추가/업데이트합니다"),
    "com.android.screenshottest.action.UpdateReferenceImagesInClassAction": ("참조 이미지 추가/업데이트", "클래스 내 모든 스크린샷 테스트의 참조 이미지를 추가/업데이트합니다"),
    "com.android.screenshottest.action.UpdateReferenceImagesInDirectoryAction": ("참조 이미지 추가/업데이트", "디렉터리 내 모든 스크린샷 테스트의 참조 이미지를 추가/업데이트합니다"),
    "com.android.screenshottest.action.UpdateReferenceImagesFromTestPanelAction": ("참조 이미지 업데이트...", None),
    "Android.AdbDevicePairing": ("Wi-Fi로 기기 페어링", "Wi-Fi를 통해 기기를 연결할 수 있는 기기 페어링 대화상자를 엽니다"),
    "android.device.reservation.extend": ("예약 연장", "기기 예약을 연장합니다"),
    "android.device.reservation.end": ("기기 반환 및 초기화", "예약을 종료하고 기기를 반환합니다"),
    "GoToRelatedDaggerItemsAction": ("관련 Dagger 항목으로 이동", None),
    "Project.CallGraph": ("문맥별 호출 경로", None),
    "Project.InterproceduralThreadAnnotations": ("프로시저 간 스레드 어노테이션 검사기", None),
    "IntelliJ.HelpTopics": ("IntelliJ IDEA 도움말", None),
    "UserInvokedHeapDumpSnapshot": ("메모리 사용량 분석", None),
    "Internal.Android.FreezeTools": ("정지(Freeze)", None),
    "DeadlockUIThread": ("Lock으로 UI 스레드 교착 상태 생성", None),
    "DeadlockUIThreadWithTimeout": ("Lock으로 UI 스레드 교착 상태 생성(10초 제한 시간)", None),
    "DeadlockUIThreadWithSynchronized": ("Synchronized로 UI 스레드 교착 상태 생성", None),
    "DeadlockUIThreadWithReadAction": ("읽기 작업으로 UI 스레드 교착 상태 생성", None),
    "CollectMemoryUsageStatistics": ("Studio 구성 요소 메모리 사용량 통계 수집", None),
    "Internal.JavaFlightRecorder": ("Java Flight Recorder", None),
    "FreezeUI": ("UI 정지", None),
    "DumpJFR": ("JFR 기록 덤프", None),
    "ImportApkAction": ("APK 프로파일링 또는 디버그...", None),
    "ResetUserIdAction": ("데이터 공유 사용자 식별자 재설정", "데이터 공유 사용자 식별자 재설정"),
    "Android.ExportProjectZip": ("ZIP 파일로 내보내기...", None),
    "Android.CreateResourcesActionGroup": ("Android 리소스 파일", None),
    "AndroidToolsGroup": ("Android", None),
    "ResourceExplorer.open": ("리소스 관리자", None),
    "Android.ValidateEssentialPlugins": ("필수 플러그인 검증", None),
    "Android.DisableAllPlugins": ("모든 플러그인 비활성화", None),
    "StatisticsViewer": ("통계 뷰어 표시", None),
    "IdeaNewProject": ("IDEA 새 프로젝트...", None),
    "IdeaNewModule": ("IDEA 새 모듈...", None),
    "AndroidConnectDebuggerAction": ("Android 프로세스에 디버거 연결", "Android 프로세스에 디버거 연결"),
    "AndroidModularizeAction": ("모듈화...", "클래스와 관련 리소스를 다른 모듈로 이동합니다"),
    "AndroidUnusedResourceAction": ("사용하지 않는 리소스 제거...", "사용하지 않는 리소스를 제거합니다"),
    "AndroidExtractStyleAction": ("스타일...(&Y)", "레이아웃에서 스타일 관련 속성을 추출하여 새 스타일로 만듭니다"),
    "AndroidExtractAsIncludeAction": ("레이아웃...(&L)", "하나 이상의 뷰를 별도의 레이아웃으로 추출합니다"),
    "AndroidInlineStyleReferenceAction": ("스타일 인라인화...(&S)", "Android 스타일을 인라인 처리합니다"),
    "AndroidInlineIncludeAction": ("레이아웃 인라인화...(&L)", "포함된 Android 레이아웃을 인라인 처리합니다"),
    "AndroidFindStyleApplicationsAction": ("가능한 곳에 스타일 사용...(&W)", "가능한 곳에서 속성을 Android 스타일 참조로 대체합니다"),
    "AndroidAddRTLSupport": ("가능한 곳에 RTL 지원 추가...", "가능한 곳에 오른쪽에서 왼쪽으로(RTL) 지원을 추가합니다"),
    "InferAnnotations": ("어노테이션 추론...", None),
    "com.android.tools.idea.actions.HideAndroidBannerAction": ("Android 배너 숨기기", "Gradle 프로젝트 알림 배너를 닫습니다"),
    "action.android.restore.file": ("앱 데이터 복원", "파일에서 앱 데이터를 복원합니다"),
    "action.android.backup": ("앱 데이터 백업", "앱 데이터를 파일로 백업합니다"),
    "action.android.backup.foreground.app": ("앱 데이터 백업", "앱 데이터를 파일로 백업합니다"),
    "action.android.restore.group": ("앱 데이터 복원", "파일에서 앱 데이터를 복원합니다"),
    "action.android.restore": ("앱 데이터 복원", "파일에서 앱 데이터를 복원합니다"),
    "com.android.build.attribution.ui.OpenBuildAnalyzerAction": (None, "빌드 분석기 열기(보고서를 표시하려면 빌드가 성공해야 함)"),
    "com.android.build.attribution.ui.OpenBuildAnalyzerResultsAction": (None, "이전 빌드 결과로 빌드 분석기 열기"),
    "DeveloperServices.ConnectionAssistant": ("기기 연결 문제 해결", "기기 연결 디버그를 도와줍니다"),
    "WelcomeScreen.RunDeviceManager2": ("가상 기기 관리자", None),
    "GoogleLoginV2.LoginService": ("Google 로그인 V2", None),
    "com.android.tools.idea.layoutinspector.toggle.layout.inspector.action": ("레이아웃 검사기 전환", "이 기기에 대한 레이아웃 검사를 켜거나 끕니다"),
    "Logcat.LogcatActions": ("Logcat", None),
    "Logcat.ToggleViewFormat": ("Logcat 형식 전환", "표준 보기와 축소 보기를 전환합니다"),
    "Logcat.ClearLogcat": ("Logcat 패널 지우기", "Logcat 패널과 기기의 logcat 버퍼를 지웁니다"),
    "Logcat.PauseResumeLogcat": ("Logcat 일시정지/재개", "Logcat 패널을 일시정지하거나 재개합니다"),
    "Logcat.RestartLogcat": ("Logcat 재시작", "Logcat 모니터링을 재시작합니다"),
    "Logcat.ToggleSoftWrap": ("자동 줄바꿈", "Logcat 메시지의 자동 줄바꿈을 전환합니다"),
    "ShowMarketingDialog": ("마케팅 대화상자 표시", None),
    "RunningDevices": ("실행 중인 기기", None),
    "AvailableDevices": ("사용 가능한 기기", None),
    "SelectMultipleDevices": ("여러 기기 선택...", None),
    "DeviceAndSnapshotComboBox": ("기기 선택", None),
    "InspectPlayPolicyCode": ("Play 정책 인사이트 검사...", None),
    "Android.ChooseProfileConfiguration": ("프로파일링...", "구성을 선택하고 프로파일링합니다"),
    "Android.BuildApkOrBundle": ("앱 번들 또는 APK 생성", None),
    "AndroidMigrateToResourceNamespacesAction": ("리소스 네임스페이스로 마이그레이션...", "리소스 네임스페이스로 마이그레이션합니다"),
    "AndroidMigrateToNonTransitiveRClassesAction": ("비전이적 R 클래스로 마이그레이션...", "프로젝트가 비전이적(Non-Transitive) R 클래스를 사용하도록 마이그레이션합니다"),
    "AndroidMigrateBuildConfigFromGradlePropertiesToDsl": ("BuildConfig를 Gradle 빌드 파일로 마이그레이션", "필요한 모듈에서만 buildConfig를 활성화합니다"),
    "AndroidMigrateResValuesFromGradlePropertiesToDsl": ("ResValues를 Gradle 빌드 파일로 마이그레이션", "필요한 모듈에서만 resValues를 활성화합니다"),
    "AndroidMigrateToDefaultTargetSdkToCompileSdkValueIfUnset": ("TargetSdk를 CompileSdk로 기본 설정", "현재 동작을 유지하면서 프로젝트의 targetSdk를 compileSdk로 기본 설정하도록 마이그레이션합니다"),
    "AndroidX.BaselineProfile.RunGenerate": ("전체 앱 베이스라인 프로필 생성", "선택한 앱의 베이스라인 프로필을 생성합니다. 생성은 항상 앱 단위로 수행되며 단일 메서드나 클래스에 대해서는 수행할 수 없습니다."),
    "IgnoreGradleChanges": ("Gradle 변경사항 무시", "Gradle 변경사항을 무시하고 동기화 알림을 숨깁니다"),
    "AgpUpgrade": ("AGP 업그레이드 어시스턴트...", "프로젝트의 Android Gradle 플러그인(AGP) 종속성을 업그레이드합니다"),
    "GoogleCloudTools.SampleImport": ("샘플 가져오기...", None),
    "WelcomeScreen.GoogleCloudTools.SampleImport": ("Android 코드 샘플 가져오기", None),
    "android.device.power.button": ("전원", "기기의 전원 버튼을 누릅니다"),
    "android.device.power.and.volume.up.button": ("전원 + 볼륨 올리기(전원 메뉴)", "기기의 전원 버튼과 볼륨 올리기 버튼을 동시에 누릅니다"),
    "android.device.volume.up.button": ("볼륨 올리기", "기기의 볼륨 올리기 버튼을 누릅니다"),
    "android.device.volume.down.button": ("볼륨 내리기", "기기의 볼륨 내리기 버튼을 누릅니다"),
    "android.device.rotate.left": ("왼쪽으로 회전", "기기를 반시계 방향으로 90도 회전합니다"),
    "android.device.rotate.right": ("오른쪽으로 회전", "기기를 시계 방향으로 90도 회전합니다"),
    "android.device.postures": ("접기/펼치기", "기기가 정의한 상태 중 하나를 선택하여 앱의 반응을 테스트합니다"),
    "android.emulator.virtual.sensors": ("가상 센서", "기기의 가상 센서 컨트롤을 표시합니다"),
    "android.device.wear1.button": ("버튼 1", "기기의 첫 번째 버튼을 누릅니다"),
    "android.device.wear2.button": ("버튼 2", "기기의 두 번째 버튼을 누릅니다"),
    "android.device.sleep": ("손바닥 제스처", "기기의 손바닥(Palm) 제스처를 시뮬레이션합니다"),
    "android.emulator.tilt": ("기울이기", "기기의 기울이기(Tilt) 제스처를 시뮬레이션합니다"),
    "android.emulator.glasses1.button": ("카메라", "기기의 카메라 버튼을 누릅니다"),
    "android.emulator.glasses2.button": ("디스플레이", "기기의 디스플레이 버튼을 누릅니다"),
    "android.device.back.button": ("뒤로", "기기의 뒤로 버튼을 누릅니다"),
    "android.device.home.button": ("홈", "기기의 홈 버튼을 누릅니다"),
    "android.device.overview.button": ("개요", "기기의 개요 버튼을 누릅니다"),
    "android.streaming.xr.interaction": ("앱과 상호작용", "마우스와 키보드로 실행 중인 앱과 상호작용합니다"),
    "android.streaming.xr.hand.tracking": ("손 추적", "마우스로 손 추적을 시뮬레이션합니다. 방향키로 시야 방향을 제어합니다."),
    "android.streaming.xr.eye.tracking": ("시선 추적", "마우스로 시선 추적을 시뮬레이션합니다. 방향키로 시야 방향을 제어합니다."),
    "android.streaming.xr.view.direction": ("시야 방향", "마우스 드래그와 방향키로 시야 방향을 제어합니다. WASDQE 키로 가상 공간에서의 위치를 제어합니다."),
    "android.streaming.xr.location.in.space.xy": ("좌우/상하 이동", "마우스를 드래그하면 가상 공간에서 좌우/상하로 이동합니다. 방향키로 시야 방향을, WASDQE 키로 가상 공간에서의 위치를 제어합니다."),
    "android.streaming.xr.location.in.space.z": ("앞뒤 이동", "마우스를 세로로 드래그하면 가상 공간에서 앞뒤로 이동합니다."),
    "android.streaming.xr.recenter": ("시야 재설정", "시야를 기본값으로 재설정합니다"),
    "android.streaming.xr.passthrough": ("패스스루 전환", "패스스루를 켜거나 끕니다"),
    "android.device.screenshot": ("스크린샷 찍기", "기기에서 스크린샷을 가져옵니다"),
    "android.device.screen.record": ("화면 녹화", "기기 화면의 동영상을 녹화합니다"),
    "android.emulator.display.mode.phone": ("휴대폰", "일반적인 휴대폰 크기에 맞게 디스플레이 크기를 변경합니다"),
    "android.emulator.display.mode.foldable": ("폴더블", "일반적인 폴더블 기기 크기에 맞게 디스플레이 크기를 변경합니다"),
    "android.emulator.display.mode.tablet": ("태블릿", "일반적인 태블릿 크기에 맞게 디스플레이 크기를 변경합니다"),
    "android.emulator.snapshots": ("스냅샷", "에뮬레이터 스냅샷을 생성, 로드, 이름 변경 또는 삭제합니다"),
    "android.streaming.hardware.input": ("하드웨어 입력", "키보드와 마우스 이벤트를 기기로 투명하게 전달하도록 설정합니다"),
    "android.emulator.extended.controls": ("확장 컨트롤", "에뮬레이터 확장 컨트롤을 표시합니다"),
    "android.streaming.ui.settings": ("기기 UI 바로가기", "자주 쓰는 Android 설정으로 가는 바로가기입니다"),
    "android.streaming.benchmark": ("스트리밍 기기 벤치마크", "내장 에뮬레이터 또는 실제 기기 미러링의 성능을 측정합니다"),
    "android.emulator.display.mode": ("디스플레이 모드", "디스플레이 모드를 선택합니다"),
    "ImportWatchFaceStudioFileAction": ("Watch Face Studio 파일 가져오기...", None),
    "android.device.wear.whs": ("Wear Health Services", "Wear Health Services 패널을 엽니다"),

    # cidr-debugger
    "CIDR.Debugger.CidrMemoryToggleDebugInlaysAction": ("메모리 문서에 디버그 인레이 표시", None),
    "CIDR.Debugger.CidrToggleGdbMiFrameVariablesAction": ("GDB: GDB/MI 변수 보기 표시", None),

    # design-tools
    "Android.Designer.ComposeIssueNotificationAction": ("문제 패널 전환", "문제 패널의 표시 여부를 전환합니다"),
    "LayoutEditor.HelpAssistant": ("도움말 패널 표시", "레이아웃 편집기의 도움말 패널을 표시/숨김"),
    "LayoutEditor.HelpAssistant.Full": ("도움말 패널 표시", "레이아웃 편집기의 도움말 패널을 표시/숨김"),
    "LayoutEditor.HelpAssistant.ConstraintLayout": ("Constraint Layout 도움말 패널", "Constraint Layout 편집기의 도움말 패널을 만듭니다"),
    "LayoutEditor.HelpAssistant.MotionLayout": ("Motion Layout 도움말 패널", "Motion Layout 편집기의 도움말 패널을 만듭니다"),
    "Android.Designer.ForceRefreshPreview": ("레이아웃 강제 새로고침", "미리보기를 새로고침합니다"),
    "Android.Designer.IssueNotificationAction": ("문제 패널 전환", "문제 패널의 표시 여부를 전환합니다"),
    "Android.Designer.LayoutEditorActions": ("레이아웃 편집기", None),
    "Android.Designer.SwitchLayoutQualifier": ("레이아웃 한정자 전환", "현재 레이아웃의 한정자를 전환하거나 새로 만듭니다"),
    "Android.Designer.SwitchDesignMode": ("디자인 모드 전환", "디자인, 블루프린트, 디자인+블루프린트 모드를 순환하며 전환합니다"),
    "Android.Designer.ToggleDeviceOrientation": ("기기 방향 전환", "미리보기 방향을 세로와 가로 사이에서 전환합니다"),
    "Android.Designer.ToggleDeviceNightMode": ("기기 야간 모드 전환", "미리보기의 야간 모드를 켜거나 끕니다"),
    "Android.Designer.NextDevice": ("다음 기기 미리보기", "기기 메뉴에서 다음 기기로 변경합니다"),
    "Android.Designer.PreviousDevice": ("이전 기기 미리보기", "기기 메뉴에서 이전 기기로 변경합니다"),
    "Android.Designer.IssuePanel.SeverityFilter": ("보기 옵션", None),
    "Android.Designer.IssuePanel.ToggleIssueDetailAction": ("문제 세부정보 표시", None),
    "Android.Designer.IssuePanel.QuickFixes": ("빠른 수정 표시", None),
    "Android.Designer.IssuePanel.CopyIssueDescription": ("문제 설명 복사", None),
    "NavEditor.HelpAssistant": ("도움말 패널 표시", "탐색 편집기의 도움말 패널을 표시합니다"),
    "Android.Designer.NavEditorActions": ("탐색 편집기", None),
    "Android.Designer.AssignStartDestination": ("시작 대상 지정", "탐색 그래프의 시작점을 지정합니다"),
    "Android.Designer.AddDeepLink": ("딥 링크 추가", "선택한 항목에 딥 링크를 추가합니다"),
    "Android.Designer.AddAction": ("작업 추가", "선택한 항목에 작업을 추가합니다"),
    "Android.Designer.AutoArrange": ("자동 정렬", "항목을 다시 정렬합니다"),

    # firebase
    "DeveloperServices.Firebase": ("Firebase", "앱에 Firebase 추가"),

    # gemini
    "AndroidUnusedDependenciesAction": ("AI로 모든 라이브러리 업데이트", "프로젝트 종속성을 업데이트합니다"),
    "sml.GenerateReadmeAction": ("README 생성", "선택한 파일에 대한 README를 마크다운으로 생성합니다"),
    "sml.AnalyzeThreadSafety": ("스레드 안전성 분석", "선택한 파일의 스레드 안전성 상태를 분석합니다"),
    "com.android.studio.ml.npa.RunNewProjectAgentAction": ("새 프로젝트 에이전트 실행", None),
    "sml.studiobot.rag.internal.group": ("RAG 내부 작업", None),
    "aiplugin.mcp.client.listTools": ("MCP 도구 목록", "MCP 도구 목록"),
    "aiplugin.custom.transform": ("에디터 내 프롬프트 열기", None),
    "aiplugin.custom.transform.finishchanges": ("변경 완료", None),
    "aiplugin.chat.explaintthis": ("이것 설명하기", None),
    "aiplugin.chat.addtocontext": ("현재 파일을 채팅 컨텍스트에 추가", None),
    "com.google.tools.intellij.aiplugin.action.SelectGcpProjectAction": ("Gemini Code Assist 프로젝트 선택...", "Gemini Code Assist 클라우드 프로젝트를 선택합니다"),
    "com.google.tools.intellij.aiplugin.recitation.IgnorePromptRecitationAction": ("코드 참조 무시", None),
    "AcceptSuggestionAction": ("선택한 제안 수락", None),
    "sml.studiobot.quick.edit": ("빠른 편집", "인라인 AI 편집기를 엽니다"),
    "sml.SuggestCommitMessageAction": ("커밋 메시지 제안", "변경사항을 요약하여 커밋 메시지를 제안합니다"),
    "aiplugin.agents.planning.editor.internal.planningModeEditorDialog": ("계획 모드 편집기 프로토타입 대화상자", None),

    # java
    "UastInternal": ("UAST", None),
    "DumpUastLog": ("UAST 트리 덤프", None),
    "DumpUastLogByElement": ("PsiElement별 UAST 트리 덤프", None),

    # performanceTesting
    "SimulateFreeze": ("정지 상태 시뮬레이션", None),

    # targetsdkversion-upgrade-assistant
    "DeveloperServices.TargetSDKVersionUpgradeAssistant": ("Android SDK 업그레이드 어시스턴트", "최신 Android SDK로 업그레이드하도록 도와줍니다!"),

    # test-recorder
    "GoogleCloudTesting.TestRecorder": ("Espresso 테스트 녹화", "선택한 구성에 대한 Espresso 테스트를 녹화합니다"),
    "GoogleCloudTesting.RoboScriptRecorder": ("Robo 스크립트 녹화", "선택한 구성에 대한 Robo 스크립트를 녹화합니다"),

    # url-assistant
    "DeveloperServices.UrlAssistant": ("App Links 어시스턴트", "App Links 어시스턴트를 엽니다"),

    # vcs-github
    "Github.Break.Api.Requests": ("GitHub API 요청 중단", None),
}


def escape_value(v):
    return v.replace("\\", "\\\\")


def main():
    with open(MISSING_PATH, encoding="utf-8") as f:
        missing = json.load(f)

    lines_to_add = []
    not_translated = []
    seen_keys = set()
    for r in missing:
        rid = r["id"]
        if rid not in TRANSLATIONS:
            not_translated.append(rid)
            continue
        text_ko, desc_ko = TRANSLATIONS[rid]
        if r["text"] is not None:
            if text_ko is None:
                not_translated.append(rid + " (text 누락)")
            elif r["key_text"] not in seen_keys:
                seen_keys.add(r["key_text"])
                lines_to_add.append(f"{r['key_text']}={escape_value(text_ko)}")
        if r["description"] is not None:
            if desc_ko is None:
                not_translated.append(rid + " (description 누락)")
            elif r["key_description"] not in seen_keys:
                seen_keys.add(r["key_description"])
                lines_to_add.append(f"{r['key_description']}={escape_value(desc_ko)}")

    if not_translated:
        print("번역이 빠진 항목:")
        for x in not_translated:
            print(" -", x)

    with open(ACTIONS_BUNDLE_PATH, "a", encoding="utf-8") as f:
        f.write("\n\n# ---- Android/Compose/NDK 등 다른 플러그인이 plugin.xml에 인라인 text=/description= 으로 박아넣은 액션 번역 ----\n")
        for line in lines_to_add:
            f.write(line + "\n")

    print(f"\n{len(lines_to_add)}줄 추가 완료 -> {ACTIONS_BUNDLE_PATH}")


if __name__ == "__main__":
    main()
