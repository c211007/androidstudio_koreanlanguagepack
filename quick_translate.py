#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""주요 번들 자동 번역 스크립트"""

from pathlib import Path
import re

WORK_DIR = Path(r"c:\Users\klanary\Desktop\vscode 모음\android_korean\androidstudio_koreanlanguagepack")
SRC_DIR = WORK_DIR / "src" / "main" / "resources" / "messages"

# 주요 번역 매핑 (일부만 샘플)
COMMON_TRANSLATIONS = {
    # 공통 액션
    "New": "새",
    "Open": "열기",
    "Close": "닫기",
    "Save": "저장",
    "Save All": "모두 저장",
    "Delete": "삭제",
    "Cut": "잘라내기",
    "Copy": "복사",
    "Paste": "붙여넣기",
    "Undo": "실행 취소",
    "Redo": "다시 실행",
    "Find": "찾기",
    "Replace": "바꾸기",
    "Select All": "모두 선택",

    # 메뉴
    "File": "파일",
    "Edit": "편집",
    "View": "보기",
    "Navigate": "이동",
    "Code": "코드",
    "Refactor": "리팩토링",
    "Build": "빌드",
    "Run": "실행",
    "Tools": "도구",
    "Window": "창",
    "Help": "도움말",

    # 도구 창
    "Project": "프로젝트",
    "Structure": "구조",
    "Favorites": "즐겨찾기",
    "TODO": "TODO",
    "Terminal": "터미널",
    "Problems": "문제",
    "Debug": "디버그",
    "Build": "빌드",

    # 공통 단어
    "Error": "오류",
    "Warning": "경고",
    "Info": "정보",
    "Settings": "설정",
    "Configuration": "구성",
    "General": "일반",
    "Advanced": "고급",
    "Apply": "적용",
    "Cancel": "취소",
    "OK": "확인",
    "Yes": "예",
    "No": "아니요",

    # Android 관련
    "Android": "Android",
    "Activity": "액티비티",
    "Fragment": "프래그먼트",
    "Service": "서비스",
    "Manifest": "매니페스트",
    "Resource": "리소스",
    "Layout": "레이아웃",
    "Gradle": "Gradle",
    "SDK": "SDK",
    "APK": "APK",
    "Module": "모듈",
    "Package": "패키지",
    "Class": "클래스",
}

def simple_translate(text):
    """간단한 번역 (기본 단어만)"""
    result = text
    for eng, kor in COMMON_TRANSLATIONS.items():
        # 단어 경계에서만 매치
        result = re.sub(r'\b' + re.escape(eng) + r'\b', kor, result)
    return result

# ActionsBundle 핵심만 번역
actionsBundle = """# Android Studio 한국어 언어팩 - Actions 번들

# 메인 메뉴
group.FileMenu.text=파일(&F)
group.EditMenu.text=편집(&E)
group.ViewMenu.text=보기(&V)
group.NavigateMenu.text=이동(&N)
group.CodeMenu.text=코드(&C)
group.RefactorMenu.text=리팩토링(&R)
group.BuildMenu.text=빌드(&B)
group.RunMenu.text=실행(&R)
group.ToolsMenu.text=도구(&T)
group.WindowMenu.text=창(&W)
group.HelpMenu.text=도움말(&H)

# 파일 메뉴
action.NewProject.text=새 프로젝트...
action.OpenFile.text=열기...
action.CloseContent.text=닫기
action.CloseAllEditors.text=모두 닫기
action.SaveAll.text=모두 저장
action.SaveDocument.text=저장
action.SaveAs.text=다른 이름으로 저장...
action.ExportSettings.text=설정 내보내기...
action.ImportSettings.text=설정 가져오기...
action.Exit.text=종료

# 편집 메뉴
action.Undo.text=실행 취소
action.$Undo.text=실행 취소
action.Redo.text=다시 실행
action.$Redo.text=다시 실행
action.Cut.text=잘라내기
action.$Cut.text=잘라내기
action.Copy.text=복사
action.$Copy.text=복사
action.Paste.text=붙여넣기
action.$Paste.text=붙여넣기
action.Delete.text=삭제
action.$Delete.text=삭제
action.SelectAll.text=모두 선택
action.$SelectAll.text=모두 선택
action.Find.text=찾기...
action.Replace.text=바꾸기...
action.FindNext.text=다음 찾기
action.FindPrevious.text=이전 찾기
action.FindInPath.text=경로에서 찾기...
action.ReplaceInPath.text=경로에서 바꾸기...

# 뷰 메뉴
action.ActivateProjectToolWindow.text=프로젝트
action.ActivateStructureToolWindow.text=구조
action.ActivateFavoritesToolWindow.text=즐겨찾기
action.ActivateRunToolWindow.text=실행
action.ActivateDebugToolWindow.text=디버그
action.ActivateTODOToolWindow.text=TODO
action.ActivateLogcatToolWindow.text=Logcat
action.ActivateTerminalToolWindow.text=터미널
action.ActivateBuildToolWindow.text=빌드
action.ActivateProblemsViewToolWindow.text=문제
action.ViewToolBar.text=도구 모음
action.ViewStatusBar.text=상태 표시줄
action.ViewNavigationBar.text=탐색 모음
action.ToggleFullScreen.text=전체 화면

# 네비게이션
action.GotoClass.text=클래스로 이동...
action.GotoFile.text=파일로 이동...
action.GotoSymbol.text=심볼로 이동...
action.GotoLine.text=줄로 이동...
action.GotoDeclaration.text=선언으로 이동
action.GotoImplementation.text=구현으로 이동
action.Back.text=뒤로
action.Forward.text=앞으로
action.RecentFiles.text=최근 파일...

# 코드 메뉴
action.CodeCompletion.text=코드 완성
action.SmartTypeCompletion.text=스마트 타입 완성
action.ClassNameCompletion.text=클래스 이름 완성
action.ShowIntentionActions.text=컨텍스트 액션 표시
action.CommentByLineComment.text=줄 주석 토글
action.CommentByBlockComment.text=블록 주석 토글
action.ReformatCode.text=코드 다시 포맷
action.OptimizeImports.text=Import 최적화

# 리팩토링
action.RenameElement.text=이름 바꾸기...
action.ExtractMethod.text=메서드 추출...
action.Inline.text=인라인...
action.SafeDelete.text=안전 삭제...
action.Move.text=이동...

# 빌드
action.CompileProject.text=프로젝트 빌드
action.Compile.text=모듈 빌드
action.Android.SyncProject.text=프로젝트를 Gradle 파일과 동기화
action.Android.GenerateSignedApk.text=서명된 APK 생성...
action.Android.BuildApk.text=APK 빌드
action.Android.BuildBundle.text=Android App Bundle 빌드

# 실행/디버그
action.Run.text=실행
action.RunClass.text=실행...
action.Debug.text=디버그
action.DebugClass.text=디버그...
action.ChooseRunConfiguration.text=실행 구성 선택...
action.ChooseDebugConfiguration.text=디버그 구성 선택...
action.editRunConfigurations.text=실행/디버그 구성 편집...
action.Stop.text=중지
action.Resume.text=계속
action.Pause.text=일시 중지
action.StepOver.text=프로시저 단위 실행
action.StepInto.text=한 단계씩 코드 실행
action.StepOut.text=프로시저 나가기
action.ToggleLineBreakpoint.text=중단점 토글
action.EvaluateExpression.text=식 평가...

# VCS
action.CheckinProject.text=커밋...
action.Vcs.UpdateProject.text=프로젝트 업데이트
action.Vcs.Push.text=푸시...
action.Vcs.Show.Log.text=로그 표시
action.Git.Branches.text=브랜치...
action.Git.Merge.text=병합...
action.Git.Pull.text=풀...
action.Git.Fetch.text=페치

# 도구
action.Android.RunAndroidAvdManager.text=AVD Manager
action.Android.RunAndroidSdkManager.text=SDK Manager

# 에디터
action.EditorCopy.text=복사
action.EditorCut.text=잘라내기
action.EditorPaste.text=붙여넣기
action.EditorDeleteLine.text=줄 삭제
action.EditorDuplicate.text=줄 또는 선택 영역 복제
action.EditorSelectWord.text=선택 영역 확장
action.EditorUnSelectWord.text=선택 영역 축소
action.EditorToggleShowWhitespaces.text=공백 표시
action.EditorToggleShowLineNumbers.text=줄 번호 표시
action.EditorToggleUseSoftWraps.text=자동 줄 바꿈
"""

with open(SRC_DIR / "ActionsBundle_ko.properties", 'w', encoding='utf-8') as f:
    f.write(actionsBundle)

print("[OK] ActionsBundle_ko.properties translated")

# IdeBundle도 샘플 작성 (자주 보이는 메시지들)
ideBundle = """# Android Studio 한국어 언어팩 - IDE 번들

# 공통 버튼
button.ok=확인
button.cancel=취소
button.apply=적용
button.yes=예
button.no=아니요
button.close=닫기
button.browse=찾아보기...
button.add=추가
button.remove=제거
button.edit=편집
button.new=새로 만들기

# 공통 메시지
message.error.title=오류
message.warning.title=경고
message.info.title=정보
message.confirm.title=확인

# 파일 관련
file.chooser.title=파일 선택
directory.chooser.title=디렉토리 선택
error.file.not.found={0} 파일을 찾을 수 없습니다
error.file.read=파일을 읽을 수 없습니다: {0}
error.file.write=파일을 쓸 수 없습니다: {0}
error.directory.create=디렉토리를 생성할 수 없습니다: {0}

# 프로젝트
project.name=프로젝트 이름
project.location=프로젝트 위치
project.sdk=프로젝트 SDK
project.language=언어
project.format=프로젝트 형식

# 설정
settings.page.general=일반
settings.page.appearance=모양 및 동작
settings.page.editor=편집기
settings.page.plugins=플러그인
settings.page.version.control=버전 제어
settings.page.build=빌드, 실행, 배포
settings.page.languages=언어 및 프레임워크
settings.page.tools=도구

# 알림
notification.title.information=정보
notification.title.warning=경고
notification.title.error=오류

# 진행 상황
progress.running=실행 중...
progress.loading=로드 중...
progress.saving=저장 중...
progress.building=빌드 중...
progress.indexing=인덱싱 중...
progress.synchronizing=동기화 중...

# 검색
search.everywhere=모든 곳 검색
search.in.project=프로젝트에서 검색
search.results=검색 결과
search.no.results=결과 없음
"""

with open(SRC_DIR / "IdeBundle_ko.properties", 'w', encoding='utf-8') as f:
    f.write(ideBundle)

print("[OK] IdeBundle_ko.properties translated")

print("\n[COMPLETE] Translation complete! 2 main bundles translated.")
print("Note: Only key items translated, not complete translation.")
print("      Other items will display in English by default.")
