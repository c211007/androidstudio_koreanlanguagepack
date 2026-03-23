#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Korean Language Pack Generator
Generates Korean translation properties files from extracted_keys and extracted_bundles
"""

import os
import re
from collections import defaultdict

# Common Korean translations dictionary
KOREAN_TRANSLATIONS = {
    # ═══════════════════════════════════════════════════════════════════════════
    # 버튼 (Buttons)
    # ═══════════════════════════════════════════════════════════════════════════
    "Yes": "예",
    "&Yes": "예(&Y)",
    "No": "아니오",
    "&No": "아니오(&N)",
    "Cancel": "취소",
    "&Cancel": "취소(&C)",
    "OK": "확인",
    "Help": "도움말",
    "Apply": "적용",
    "&Apply": "적용(&A)",
    "Close": "닫기",
    "&Close": "닫기(&C)",
    "Delete": "삭제",
    "Add": "추가",
    "&Add": "추가(&A)",
    "Remove": "제거",
    "Edit": "편집",
    "Accept": "수락",
    "Decline": "거절",
    "Submit": "제출",
    "Save": "저장",
    "&Save": "저장(&S)",
    "Save All": "모두 저장",
    "Open": "열기",
    "&Open": "열기(&O)",
    "New": "새로 만들기",
    "Copy": "복사",
    "Cut": "잘라내기",
    "Paste": "붙여넣기",
    "Undo": "실행 취소",
    "Redo": "다시 실행",
    "Refresh": "새로고침",
    "Rerun": "다시 실행",
    "Run": "실행",
    "Stop": "중지",
    "Pause": "일시정지",
    "Resume": "재개",
    "Retry": "재시도",
    "Skip": "건너뛰기",
    "Finish": "완료",
    "Next": "다음",
    "Previous": "이전",
    "Back": "뒤로",
    "Forward": "앞으로",
    "Browse": "찾아보기",
    "Search": "검색",
    "Find": "찾기",
    "Replace": "바꾸기",
    "&Replace": "바꾸기(&R)",
    "Select": "선택",
    "Select All": "모두 선택",
    "Clear": "지우기",
    "Clear All": "모두 지우기",
    "Reset": "초기화",
    "Restore": "복원",
    "Update": "업데이트",
    "Install": "설치",
    "Uninstall": "제거",
    "Enable": "활성화",
    "Disable": "비활성화",
    "Start": "시작",
    "Build": "빌드",
    "Rebuild": "다시 빌드",
    "Clean": "정리",
    "Compile": "컴파일",
    "Debug": "디버그",
    "Test": "테스트",
    "Deploy": "배포",
    "Sync": "동기화",
    "Import": "가져오기",
    "Export": "내보내기",
    "Create": "생성",
    "Generate": "생성",
    "Configure": "구성",
    "Settings": "설정",
    "Preferences": "환경 설정",
    "Options": "옵션",
    "Properties": "속성",
    "Details": "세부 정보",
    "Information": "정보",
    "Info": "정보",
    "View": "보기",
    "Show": "표시",
    "Hide": "숨기기",
    "Expand": "확장",
    "Collapse": "축소",
    "Zoom In": "확대",
    "Zoom Out": "축소",
    "Minimize": "최소화",
    "&Minimize": "최소화(&M)",
    "Maximize": "최대화",
    "Filter": "필터",
    "Sort": "정렬",
    "Group": "그룹",
    "Move": "이동",
    "Rename": "이름 바꾸기",
    "Duplicate": "복제",
    "Clone": "복제",
    "Merge": "병합",
    "Split": "분할",
    "Toggle": "전환",
    "Reload": "다시 로드",
    "Overwrite": "덮어쓰기",
    "Reuse": "재사용",
    "Revert": "되돌리기",
    "Exclude": "제외",
    "Include": "포함",
    "Set": "설정",
    "Get": "가져오기",
    "Continue": "계속",
    "Con&tinue": "계속(&T)",
    "Yes for &All": "모두 예(&A)",
    "All": "모두",
    "None": "없음",
    "Run All": "모두 실행",
    "Abort": "중단",
    "Ignore": "무시",
    "Don't Save": "저장 안 함",
    "Discard": "버리기",
    "Keep": "유지",
    "Proceed": "진행",
    "Try Again": "다시 시도",
    "Fix": "수정",
    "Preview": "미리보기",
    "Print": "인쇄",
    "Send": "보내기",
    "Download": "다운로드",
    "Upload": "업로드",
    "Connect": "연결",
    "Disconnect": "연결 끊기",
    "Login": "로그인",
    "Logout": "로그아웃",
    "Sign In": "로그인",
    "Sign Out": "로그아웃",
    "Register": "등록",

    # ═══════════════════════════════════════════════════════════════════════════
    # 타이틀 / 레이블 (Titles / Labels)
    # ═══════════════════════════════════════════════════════════════════════════
    "Error": "오류",
    "Warning": "경고",
    "Confirmation": "확인",
    "Name": "이름",
    "Kind": "종류",
    "Type": "유형",
    "Module": "모듈",
    "Project": "프로젝트",
    "File": "파일",
    "Folder": "폴더",
    "Directory": "디렉터리",
    "Path": "경로",
    "Source": "소스",
    "Target": "대상",
    "Destination": "대상",
    "Root": "루트",
    "Source root": "소스 루트",
    "Prefix": "접두사",
    "Suffix": "접미사",
    "General": "일반",
    "Advanced": "고급",
    "Basic": "기본",
    "Custom": "사용자 정의",
    "Default": "기본값",
    "Input": "입력",
    "Output": "출력",
    "Console": "콘솔",
    "Terminal": "터미널",
    "Lambda": "람다",
    "Pull up": "끌어올리기",
    "Nothing here": "여기에 아무것도 없습니다",
    "No data": "데이터 없음",
    "Loading": "로딩 중",
    "Services": "서비스",
    "Hide Others": "다른 항목 숨기기",
    "Show All": "모두 표시",
    "Quit": "종료",
    "Exit": "종료",
    "File | Settings": "파일 | 설정",
    "Edit application settings": "애플리케이션 설정 편집",
    "Edit application preferences": "애플리케이션 환경 설정 편집",
    "Do nothing": "아무것도 하지 않음",
    "Description": "설명",
    "Location": "위치",
    "Size": "크기",
    "Date": "날짜",
    "Time": "시간",
    "Status": "상태",
    "Version": "버전",
    "Author": "작성자",
    "License": "라이선스",
    "Language": "언어",
    "Encoding": "인코딩",
    "Format": "형식",
    "Content": "내용",
    "Title": "제목",
    "Summary": "요약",
    "Result": "결과",
    "Results": "결과",
    "Count": "개수",
    "Total": "총계",
    "Average": "평균",
    "Minimum": "최소값",
    "Maximum": "최대값",
    "Current": "현재",
    "Parent": "상위",
    "Child": "하위",
    "Level": "레벨",
    "Priority": "우선순위",
    "Category": "범주",
    "Tag": "태그",
    "Label": "레이블",
    "Note": "노트",
    "Comment": "주석",
    "Remark": "비고",
    "Hint": "힌트",
    "Tip": "팁",
    "Example": "예제",
    "Sample": "샘플",
    "Template": "템플릿",
    "Pattern": "패턴",
    "Rule": "규칙",
    "Policy": "정책",
    "Scope": "범위",
    "Range": "범위",
    "Limit": "제한",
    "Threshold": "임계값",
    "Timeout": "시간 초과",
    "Delay": "지연",
    "Interval": "간격",
    "Duration": "기간",
    "Period": "기간",

    # ═══════════════════════════════════════════════════════════════════════════
    # 상태 메시지 (Status Messages)
    # ═══════════════════════════════════════════════════════════════════════════
    "Performing Modification": "수정 중",
    "Please wait": "잠시 기다려 주세요",
    "Processing": "처리 중",
    "Initializing": "초기화 중",
    "Analyzing": "분석 중",
    "Building": "빌드 중",
    "Compiling": "컴파일 중",
    "Indexing": "인덱싱 중",
    "Searching": "검색 중",
    "Downloading": "다운로드 중",
    "Uploading": "업로드 중",
    "Connecting": "연결 중",
    "Synchronizing": "동기화 중",
    "Updating": "업데이트 중",
    "Installing": "설치 중",
    "Configuring": "구성 중",
    "Validating": "유효성 검사 중",
    "Completed": "완료됨",
    "Failed": "실패",
    "Success": "성공",
    "Successful": "성공",
    "Cancelled": "취소됨",
    "Aborted": "중단됨",
    "Pending": "대기 중",
    "In Progress": "진행 중",
    "Ready": "준비됨",
    "Unknown": "알 수 없음",
    "N/A": "해당 없음",
    "True": "참",
    "False": "거짓",
    "Enabled": "활성화됨",
    "Disabled": "비활성화됨",
    "Active": "활성",
    "Inactive": "비활성",
    "Online": "온라인",
    "Offline": "오프라인",
    "Connected": "연결됨",
    "Disconnected": "연결 끊김",
    "Available": "사용 가능",
    "Unavailable": "사용 불가",
    "Running": "실행 중",
    "Stopped": "중지됨",
    "Paused": "일시정지됨",
    "Waiting": "대기 중",
    "Queued": "대기열",
    "Finished": "완료됨",
    "Done": "완료",
    "Not Found": "찾을 수 없음",
    "Not Available": "사용할 수 없음",
    "No Results": "결과 없음",
    "No Items": "항목 없음",
    "Empty": "비어 있음",
    "Invalid": "유효하지 않음",
    "Valid": "유효함",
    "Modified": "수정됨",
    "Unmodified": "수정되지 않음",
    "Changed": "변경됨",
    "Unchanged": "변경되지 않음",
    "Saved": "저장됨",
    "Unsaved": "저장되지 않음",

    # ═══════════════════════════════════════════════════════════════════════════
    # 에디터 / 코드 관련 (Editor / Code)
    # ═══════════════════════════════════════════════════════════════════════════
    "Code": "코드",
    "Editor": "편집기",
    "Syntax": "구문",
    "Inspection": "검사",
    "Refactor": "리팩터링",
    "Refactoring": "리팩터링",
    "Extract": "추출",
    "Inline": "인라인",
    "Introduce": "도입",
    "Change Signature": "시그니처 변경",
    "Safe Delete": "안전하게 삭제",
    "Find Usages": "사용처 찾기",
    "Highlight Usages": "사용처 강조",
    "Go to": "이동",
    "Navigate": "탐색",
    "Navigate to": "다음으로 이동",
    "Jump to": "이동",
    "Declaration": "선언",
    "Implementation": "구현",
    "Definition": "정의",
    "Type Definition": "유형 정의",
    "Super Method": "상위 메서드",
    "Class": "클래스",
    "Interface": "인터페이스",
    "Method": "메서드",
    "Function": "함수",
    "Variable": "변수",
    "Constant": "상수",
    "Field": "필드",
    "Property": "속성",
    "Parameter": "매개변수",
    "Argument": "인수",
    "Return": "반환",
    "Exception": "예외",
    "String": "문자열",
    "Number": "숫자",
    "Boolean": "논리값",
    "Array": "배열",
    "List": "목록",
    "Map": "맵",
    "Object": "객체",
    "Instance": "인스턴스",
    "Reference": "참조",
    "Pointer": "포인터",
    "Value": "값",
    "Key": "키",
    "Index": "인덱스",
    "Element": "요소",
    "Item": "항목",
    "Member": "멤버",
    "Context": "컨텍스트",
    "Namespace": "네임스페이스",
    "Package": "패키지",
    "Public": "공개",
    "Private": "비공개",
    "Protected": "보호됨",
    "Internal": "내부",
    "Static": "정적",
    "Final": "최종",
    "Abstract": "추상",
    "Virtual": "가상",
    "Override": "재정의",
    "Deprecated": "사용 중단",
    "Annotation": "어노테이션",
    "Attribute": "속성",
    "Modifier": "수정자",
    "Keyword": "키워드",
    "Operator": "연산자",
    "Expression": "표현식",
    "Statement": "명령문",
    "Block": "블록",
    "Branch": "분기",
    "Loop": "루프",
    "Condition": "조건",
    "Snippet": "스니펫",
    "Live Template": "라이브 템플릿",
    "Postfix Completion": "후위 완성",
    "Code Completion": "코드 완성",
    "Auto Import": "자동 가져오기",
    "Optimize Imports": "가져오기 최적화",
    "Format Code": "코드 서식 지정",
    "Reformat": "서식 다시 지정",
    "Indent": "들여쓰기",
    "Tab": "탭",
    "Space": "공백",
    "Line": "줄",
    "Column": "열",
    "Caret": "캐럿",
    "Cursor": "커서",
    "Selection": "선택",
    "Highlight": "강조",
    "Fold": "접기",
    "Unfold": "펼침",
    "Word Wrap": "자동 줄 바꿈",
    "Soft Wrap": "부드러운 줄 바꿈",
    "Show Line Numbers": "줄 번호 표시",
    "Show Whitespace": "공백 표시",
    "Show Indent Guides": "들여쓰기 안내선 표시",
    "Breakpoint": "중단점",
    "Bookmark": "북마크",
    "TODO": "할 일",
    "FIXME": "수정 필요",

    # ═══════════════════════════════════════════════════════════════════════════
    # 버전 관리 (Version Control / Git)
    # ═══════════════════════════════════════════════════════════════════════════
    "Version Control": "버전 관리",
    "VCS": "VCS",
    "Git": "Git",
    "Commit": "커밋",
    "Push": "푸시",
    "Pull": "풀",
    "Fetch": "페치",
    "Rebase": "리베이스",
    "Stash": "스태시",
    "Cherry Pick": "체리 픽",
    "Checkout": "체크아웃",
    "Remote": "원격",
    "Origin": "오리진",
    "Upstream": "업스트림",
    "Local": "로컬",
    "Changes": "변경 사항",
    "Staged": "스테이징됨",
    "Unstaged": "스테이징되지 않음",
    "Untracked": "추적되지 않음",
    "Added": "추가됨",
    "Deleted": "삭제됨",
    "Renamed": "이름 변경됨",
    "Moved": "이동됨",
    "Copied": "복사됨",
    "Conflict": "충돌",
    "Resolve": "해결",
    "Diff": "비교",
    "Compare": "비교",
    "History": "기록",
    "Log": "로그",
    "Blame": "블레임",
    "Annotate": "주석 달기",
    "Repository": "저장소",
    "Working Directory": "작업 디렉터리",
    "Staging Area": "스테이징 영역",
    "HEAD": "HEAD",
    "Detached HEAD": "분리된 HEAD",
    "Merge Conflict": "병합 충돌",
    "Accept Yours": "내 것 수락",
    "Accept Theirs": "상대 것 수락",
    "Accept Both": "둘 다 수락",

    # ═══════════════════════════════════════════════════════════════════════════
    # Android 관련 (Android)
    # ═══════════════════════════════════════════════════════════════════════════
    "Android": "Android",
    "Device": "기기",
    "Emulator": "에뮬레이터",
    "AVD": "AVD",
    "SDK": "SDK",
    "NDK": "NDK",
    "Gradle": "Gradle",
    "APK": "APK",
    "AAB": "AAB",
    "ABI": "ABI",
    "Activity": "액티비티",
    "Fragment": "프래그먼트",
    "Service": "서비스",
    "Receiver": "리시버",
    "Provider": "프로바이더",
    "Intent": "인텐트",
    "Bundle": "번들",
    "Manifest": "매니페스트",
    "Layout": "레이아웃",
    "Resource": "리소스",
    "Drawable": "드로어블",
    "Style": "스타일",
    "Theme": "테마",
    "Menu": "메뉴",
    "Animation": "애니메이션",
    "Color": "색상",
    "Dimension": "치수",
    "Asset": "에셋",
    "Raw": "원시",
    "XML": "XML",
    "Logcat": "Logcat",
    "Release": "릴리스",
    "Variant": "변형",
    "Flavor": "플레이버",
    "Build Type": "빌드 유형",
    "Sign": "서명",
    "Lint": "Lint",
    "ProGuard": "ProGuard",
    "R8": "R8",
    "Profiler": "프로파일러",
    "Memory": "메모리",
    "CPU": "CPU",
    "Network": "네트워크",
    "Energy": "에너지",
    "Inspector": "인스펙터",
    "Layout Inspector": "레이아웃 인스펙터",
    "Database Inspector": "데이터베이스 인스펙터",
    "Network Inspector": "네트워크 인스펙터",
    "App Inspector": "앱 인스펙터",
    "Device Explorer": "기기 탐색기",
    "Device Manager": "기기 관리자",
    "Pair": "페어링",
    "Wear": "Wear",
    "Watch": "워치",
    "TV": "TV",
    "Auto": "오토",
    "Compose": "Compose",
    "Jetpack": "Jetpack",
    "AndroidX": "AndroidX",
    "Support Library": "지원 라이브러리",
    "Material Design": "머티리얼 디자인",
    "ConstraintLayout": "ConstraintLayout",
    "RecyclerView": "RecyclerView",
    "ViewModel": "ViewModel",
    "LiveData": "LiveData",
    "Room": "Room",
    "Navigation": "네비게이션",
    "WorkManager": "WorkManager",
    "Data Binding": "데이터 바인딩",
    "View Binding": "뷰 바인딩",
    "Kotlin": "Kotlin",
    "Java": "Java",
    "Coroutines": "코루틴",
    "Flow": "Flow",
    "Hilt": "Hilt",
    "Dagger": "Dagger",

    # ═══════════════════════════════════════════════════════════════════════════
    # 대화 상자 제목 (Dialog Titles)
    # ═══════════════════════════════════════════════════════════════════════════
    "Confirm": "확인",
    "Question": "질문",
    "About": "정보",
    "Registration": "등록",
    "Activation": "활성화",
    "Welcome": "환영합니다",
    "Getting Started": "시작하기",
    "What's New": "새로운 기능",
    "Tip of the Day": "오늘의 팁",
    "Keyboard Shortcuts": "키보드 단축키",
    "Quick Start": "빠른 시작",
    "New Project": "새 프로젝트",
    "Open Project": "프로젝트 열기",
    "Import Project": "프로젝트 가져오기",
    "Export Project": "프로젝트 내보내기",
    "Project Structure": "프로젝트 구조",
    "Module Settings": "모듈 설정",
    "SDK Manager": "SDK 관리자",
    "Plugin Manager": "플러그인 관리자",
    "Plugins": "플러그인",
    "Marketplace": "마켓플레이스",
    "Installed": "설치됨",
    "Updates": "업데이트",

    # ═══════════════════════════════════════════════════════════════════════════
    # UI 요소 (UI Elements)
    # ═══════════════════════════════════════════════════════════════════════════
    "Toolbar": "도구 모음",
    "Status Bar": "상태 표시줄",
    "Navigation Bar": "탐색 모음",
    "Tool Window": "도구 창",
    "Side Panel": "측면 패널",
    "Bottom Panel": "하단 패널",
    "Panel": "패널",
    "Pane": "창",
    "Window": "창",
    "Dialog": "대화 상자",
    "Popup": "팝업",
    "Tooltip": "도구 설명",
    "Notification": "알림",
    "Message": "메시지",
    "Alert": "경고",
    "Banner": "배너",
    "Badge": "배지",
    "Icon": "아이콘",
    "Image": "이미지",
    "Text": "텍스트",
    "Button": "버튼",
    "Checkbox": "확인란",
    "Radio Button": "라디오 버튼",
    "Dropdown": "드롭다운",
    "Combobox": "콤보 상자",
    "List Box": "목록 상자",
    "Text Field": "텍스트 필드",
    "Text Area": "텍스트 영역",
    "Slider": "슬라이더",
    "Spinner": "스피너",
    "Progress Bar": "진행 표시줄",
    "Tree": "트리",
    "Table": "테이블",
    "Grid": "그리드",
    "Splitter": "분할자",
    "Separator": "구분자",
    "Scroll Bar": "스크롤 막대",
    "Header": "헤더",
    "Footer": "푸터",
    "Sidebar": "사이드바",
    "Main Content": "메인 콘텐츠",
    "Breadcrumb": "경로",
    "Link": "링크",
    "Hyperlink": "하이퍼링크",

    # ═══════════════════════════════════════════════════════════════════════════
    # 메뉴 (Menus)
    # ═══════════════════════════════════════════════════════════════════════════
    "File": "파일",
    "Edit": "편집",
    "View": "보기",
    "Navigate": "탐색",
    "Code": "코드",
    "Analyze": "분석",
    "Refactor": "리팩터링",
    "Build": "빌드",
    "Run": "실행",
    "Tools": "도구",
    "VCS": "VCS",
    "Window": "창",
    "Help": "도움말",
    "Recent Files": "최근 파일",
    "Recent Projects": "최근 프로젝트",
    "Recent Locations": "최근 위치",
    "Favorites": "즐겨찾기",
    "Bookmarks": "북마크",

    # ═══════════════════════════════════════════════════════════════════════════
    # 파일 작업 (File Operations)
    # ═══════════════════════════════════════════════════════════════════════════
    "New File": "새 파일",
    "New Folder": "새 폴더",
    "New Directory": "새 디렉터리",
    "Open File": "파일 열기",
    "Open Folder": "폴더 열기",
    "Save File": "파일 저장",
    "Save As": "다른 이름으로 저장",
    "Close File": "파일 닫기",
    "Close All": "모두 닫기",
    "Close Others": "다른 항목 닫기",
    "Rename File": "파일 이름 바꾸기",
    "Delete File": "파일 삭제",
    "Move File": "파일 이동",
    "Copy File": "파일 복사",
    "Copy Path": "경로 복사",
    "Copy Filename": "파일 이름 복사",
    "Reveal in Finder": "Finder에서 표시",
    "Reveal in Explorer": "탐색기에서 표시",
    "Open in Terminal": "터미널에서 열기",

    # ═══════════════════════════════════════════════════════════════════════════
    # 검색 / 찾기 (Search / Find)
    # ═══════════════════════════════════════════════════════════════════════════
    "Find in Files": "파일에서 찾기",
    "Find in Path": "경로에서 찾기",
    "Replace in Files": "파일에서 바꾸기",
    "Replace in Path": "경로에서 바꾸기",
    "Find Usages": "사용처 찾기",
    "Find Next": "다음 찾기",
    "Find Previous": "이전 찾기",
    "Search Everywhere": "전체 검색",
    "Go to Class": "클래스로 이동",
    "Go to File": "파일로 이동",
    "Go to Symbol": "심볼로 이동",
    "Go to Line": "줄로 이동",
    "Go to Declaration": "선언으로 이동",
    "Go to Implementation": "구현으로 이동",
    "Go to Type Declaration": "유형 선언으로 이동",
    "Match Case": "대소문자 구분",
    "Whole Words": "전체 단어",
    "Regex": "정규식",
    "In Selection": "선택 영역에서",
    "In Project": "프로젝트에서",
    "In Module": "모듈에서",
    "In Directory": "디렉터리에서",
    "In Scope": "범위에서",

    # ═══════════════════════════════════════════════════════════════════════════
    # 디버그 / 실행 (Debug / Run)
    # ═══════════════════════════════════════════════════════════════════════════
    "Run Configuration": "실행 구성",
    "Debug Configuration": "디버그 구성",
    "Edit Configurations": "구성 편집",
    "Run with Coverage": "커버리지 실행",
    "Step Over": "단계 건너뛰기",
    "Step Into": "단계 진입",
    "Step Out": "단계 나가기",
    "Force Step Into": "강제 단계 진입",
    "Run to Cursor": "커서까지 실행",
    "Evaluate Expression": "표현식 평가",
    "View Breakpoints": "중단점 보기",
    "Mute Breakpoints": "중단점 음소거",
    "Watches": "감시",
    "Variables": "변수",
    "Frames": "프레임",
    "Threads": "스레드",
    "Console Output": "콘솔 출력",
    "Application Output": "애플리케이션 출력",

    # ═══════════════════════════════════════════════════════════════════════════
    # 오류 메시지 (Error Messages)
    # ═══════════════════════════════════════════════════════════════════════════
    "An error occurred": "오류가 발생했습니다",
    "Operation failed": "작업 실패",
    "Cannot complete operation": "작업을 완료할 수 없습니다",
    "File not found": "파일을 찾을 수 없습니다",
    "Directory not found": "디렉터리를 찾을 수 없습니다",
    "Permission denied": "권한이 거부되었습니다",
    "Access denied": "접근이 거부되었습니다",
    "Invalid input": "잘못된 입력",
    "Invalid value": "잘못된 값",
    "Invalid format": "잘못된 형식",
    "Invalid path": "잘못된 경로",
    "Invalid name": "잘못된 이름",
    "Connection failed": "연결 실패",
    "Connection timeout": "연결 시간 초과",
    "Network error": "네트워크 오류",
    "Server error": "서버 오류",
    "Unknown error": "알 수 없는 오류",
    "Unexpected error": "예기치 않은 오류",
    "Out of memory": "메모리 부족",
    "Disk full": "디스크 공간 부족",
    "Read error": "읽기 오류",
    "Write error": "쓰기 오류",
    "Parse error": "구문 분석 오류",
    "Syntax error": "구문 오류",
    "Compilation error": "컴파일 오류",
    "Runtime error": "런타임 오류",
    "Exception": "예외",
    "Stack overflow": "스택 오버플로",
    "Null pointer": "널 포인터",
    "Index out of bounds": "인덱스 범위 초과",
    "Division by zero": "0으로 나눔",
    "Type mismatch": "유형 불일치",
    "Missing dependency": "누락된 종속성",
    "Circular dependency": "순환 종속성",
    "Duplicate entry": "중복 항목",
    "Already exists": "이미 존재함",
    "Not initialized": "초기화되지 않음",
    "Not configured": "구성되지 않음",
    "Not supported": "지원되지 않음",
    "Not implemented": "구현되지 않음",
    "Deprecated": "사용 중단됨",
    "Obsolete": "구식",
}


def load_properties(file_path):
    """Load properties file and return as dict"""
    properties = {}
    if not os.path.exists(file_path):
        return properties

    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            if '=' in line:
                key, value = line.split('=', 1)
                properties[key.strip()] = value.strip()
    return properties


def load_keys(file_path):
    """Load keys file and return as list"""
    keys = []
    if not os.path.exists(file_path):
        return keys

    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line:
                keys.append(line)
    return keys


def translate_value(value):
    """Simple translation using dictionary lookup"""
    # Direct match
    if value in KOREAN_TRANSLATIONS:
        return KOREAN_TRANSLATIONS[value]

    # Remove ... or ellipsis and try again
    clean_value = value.replace("\\u2026", "").replace("…", "").replace("...", "").strip()
    if clean_value in KOREAN_TRANSLATIONS:
        translated = KOREAN_TRANSLATIONS[clean_value]
        if "\\u2026" in value or "…" in value or "..." in value:
            translated += "..."
        return translated

    # Return original if no translation found
    return value


def unicode_escape(s):
    """Keep UTF-8 characters as-is (no Unicode escape)"""
    return s


def categorize_key(key):
    """Categorize a key based on its prefix/pattern"""
    key_lower = key.lower()

    if key_lower.startswith('button.') or '.button.' in key_lower:
        return "BUTTONS"
    elif key_lower.startswith('action.') or '.action.' in key_lower:
        return "ACTIONS"
    elif key_lower.startswith('title.') or '.title.' in key_lower:
        return "TITLES"
    elif key_lower.startswith('label.') or '.label.' in key_lower:
        return "LABELS"
    elif key_lower.startswith('message.') or '.message.' in key_lower or key_lower.startswith('msg.'):
        return "MESSAGES"
    elif key_lower.startswith('error.') or '.error.' in key_lower:
        return "ERRORS"
    elif key_lower.startswith('warning.') or '.warning.' in key_lower:
        return "WARNINGS"
    elif key_lower.startswith('dialog.') or '.dialog.' in key_lower:
        return "DIALOGS"
    elif key_lower.startswith('menu.') or '.menu.' in key_lower:
        return "MENUS"
    elif key_lower.startswith('tooltip.') or '.tooltip.' in key_lower:
        return "TOOLTIPS"
    elif key_lower.startswith('status.') or '.status.' in key_lower:
        return "STATUS"
    elif key_lower.startswith('progress.') or '.progress.' in key_lower:
        return "PROGRESS"
    elif key_lower.startswith('notification.') or '.notification.' in key_lower:
        return "NOTIFICATIONS"
    elif key_lower.startswith('settings.') or '.settings.' in key_lower or key_lower.startswith('config.'):
        return "SETTINGS"
    elif key_lower.startswith('text.') or '.text.' in key_lower:
        return "TEXT"
    elif key_lower.startswith('hint.') or '.hint.' in key_lower:
        return "HINTS"
    elif key_lower.startswith('placeholder.') or '.placeholder.' in key_lower:
        return "PLACEHOLDERS"
    elif key_lower.startswith('description.') or '.description.' in key_lower:
        return "DESCRIPTIONS"
    elif key_lower.startswith('group.') or '.group.' in key_lower:
        return "GROUPS"
    elif key_lower.startswith('tab.') or '.tab.' in key_lower:
        return "TABS"
    elif key_lower.startswith('tree.') or '.tree.' in key_lower:
        return "TREE"
    elif key_lower.startswith('column.') or '.column.' in key_lower:
        return "COLUMNS"
    elif key_lower.startswith('checkbox.') or '.checkbox.' in key_lower:
        return "CHECKBOXES"
    elif key_lower.startswith('radio.') or '.radio.' in key_lower:
        return "RADIO_BUTTONS"
    elif key_lower.startswith('combo.') or '.combo.' in key_lower or key_lower.startswith('dropdown.'):
        return "DROPDOWNS"
    elif key_lower.startswith('link.') or '.link.' in key_lower:
        return "LINKS"
    elif key_lower.startswith('icon.') or '.icon.' in key_lower:
        return "ICONS"
    elif key_lower.startswith('name.') or '.name.' in key_lower:
        return "NAMES"
    else:
        return "OTHER"


CATEGORY_ORDER = [
    "BUTTONS",
    "ACTIONS",
    "MENUS",
    "TITLES",
    "LABELS",
    "NAMES",
    "TEXT",
    "DESCRIPTIONS",
    "HINTS",
    "PLACEHOLDERS",
    "MESSAGES",
    "ERRORS",
    "WARNINGS",
    "NOTIFICATIONS",
    "STATUS",
    "PROGRESS",
    "DIALOGS",
    "TOOLTIPS",
    "SETTINGS",
    "TABS",
    "GROUPS",
    "TREE",
    "COLUMNS",
    "CHECKBOXES",
    "RADIO_BUTTONS",
    "DROPDOWNS",
    "LINKS",
    "ICONS",
    "OTHER",
]

CATEGORY_NAMES_KO = {
    "BUTTONS": "버튼 (Buttons)",
    "ACTIONS": "액션 (Actions)",
    "MENUS": "메뉴 (Menus)",
    "TITLES": "제목 (Titles)",
    "LABELS": "레이블 (Labels)",
    "NAMES": "이름 (Names)",
    "TEXT": "텍스트 (Text)",
    "DESCRIPTIONS": "설명 (Descriptions)",
    "HINTS": "힌트 (Hints)",
    "PLACEHOLDERS": "플레이스홀더 (Placeholders)",
    "MESSAGES": "메시지 (Messages)",
    "ERRORS": "오류 (Errors)",
    "WARNINGS": "경고 (Warnings)",
    "NOTIFICATIONS": "알림 (Notifications)",
    "STATUS": "상태 (Status)",
    "PROGRESS": "진행 (Progress)",
    "DIALOGS": "대화상자 (Dialogs)",
    "TOOLTIPS": "툴팁 (Tooltips)",
    "SETTINGS": "설정 (Settings)",
    "TABS": "탭 (Tabs)",
    "GROUPS": "그룹 (Groups)",
    "TREE": "트리 (Tree)",
    "COLUMNS": "열 (Columns)",
    "CHECKBOXES": "체크박스 (Checkboxes)",
    "RADIO_BUTTONS": "라디오 버튼 (Radio Buttons)",
    "DROPDOWNS": "드롭다운 (Dropdowns)",
    "LINKS": "링크 (Links)",
    "ICONS": "아이콘 (Icons)",
    "OTHER": "기타 (Other)",
}


def generate_korean_properties(keys, original_props, bundle_name):
    """Generate Korean properties from keys and original properties"""
    lines = []

    # Header with rules
    lines.append("# ╔═══════════════════════════════════════════════════════════════════════════════╗")
    lines.append(f"# ║  {bundle_name} - Korean Translation")
    lines.append("# ║  Android Studio 한국어 언어팩")
    lines.append("# ╠═══════════════════════════════════════════════════════════════════════════════╣")
    lines.append("# ║  수정 시 유의사항 (Translation Guidelines)")
    lines.append("# ║  ─────────────────────────────────────────────────────────────────────────────")
    lines.append("# ║  1. 키(key)는 절대 변경하지 마세요. = 왼쪽 부분은 수정 금지!")
    lines.append("# ║     Do NOT modify keys (text before =)")
    lines.append("# ║")
    lines.append("# ║  2. {0}, {1}, {2} 같은 플레이스홀더는 그대로 유지하세요.")
    lines.append("# ║     Keep placeholders like {0}, {1}, {2} unchanged")
    lines.append("# ║     예: \"파일 {0}을(를) 저장했습니다\" (O)")
    lines.append("# ║         \"파일을 저장했습니다\" (X) - {0} 누락")
    lines.append("# ║")
    lines.append("# ║  3. &문자는 키보드 단축키입니다. 적절한 한글 자음에 맞게 변경하세요.")
    lines.append("# ║     & marks keyboard shortcuts. Adjust to Korean if appropriate")
    lines.append("# ║     예: \"&Save\" → \"저장(&S)\" 또는 \"저장(&ㅈ)\"")
    lines.append("# ║")
    lines.append("# ║  4. ... (말줄임표)는 추가 작업이 필요함을 의미합니다. 유지하세요.")
    lines.append("# ║     Keep ... (ellipsis) as it indicates additional action needed")
    lines.append("# ║")
    lines.append("# ║  5. 특수문자 앞에는 백슬래시(\\\\)를 붙여야 합니다.")
    lines.append("# ║     Escape special characters with backslash")
    lines.append("# ║     예: 콜론(:) → \\\\:  등호(=) → \\\\=")
    lines.append("# ║")
    lines.append("# ║  6. 한글은 자동으로 유니코드로 변환됩니다.")
    lines.append("# ║     Korean characters are automatically converted to Unicode")
    lines.append("# ║")
    lines.append("# ║  7. 주석(#으로 시작하는 줄)은 번역에 영향을 주지 않습니다.")
    lines.append("# ║     Comments (lines starting with #) don't affect translation")
    lines.append("# ╚═══════════════════════════════════════════════════════════════════════════════╝")
    lines.append("")

    # Categorize keys
    categorized = defaultdict(list)
    for key in keys:
        if key in original_props:
            category = categorize_key(key)
            categorized[category].append(key)

    # Generate output by category
    for category in CATEGORY_ORDER:
        if category not in categorized or not categorized[category]:
            continue

        category_name = CATEGORY_NAMES_KO.get(category, category)
        lines.append("")
        lines.append(f"# ═══════════════════════════════════════════════════════════════════════════════")
        lines.append(f"# {category_name}")
        lines.append(f"# ═══════════════════════════════════════════════════════════════════════════════")

        for key in sorted(categorized[category]):
            value = original_props[key]
            translated = translate_value(value)
            escaped_value = unicode_escape(translated)
            lines.append(f"{key}={escaped_value}")

    lines.append("")
    lines.append("# ═══════════════════════════════════════════════════════════════════════════════")
    lines.append("# End of file")
    lines.append("# ═══════════════════════════════════════════════════════════════════════════════")

    return '\n'.join(lines)


def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    keys_dir = os.path.join(base_dir, 'extracted_keys')
    intellij_bundles = os.path.join(base_dir, 'extracted_bundles', 'intellij', 'messages')
    android_bundles = os.path.join(base_dir, 'extracted_bundles', 'android', 'messages')
    output_dir = os.path.join(base_dir, 'src', 'main', 'resources', 'messages')

    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Get all key files
    key_files = [f for f in os.listdir(keys_dir) if f.endswith('_keys.txt')]

    print(f"Found {len(key_files)} key files")

    for key_file in key_files:
        bundle_name = key_file.replace('_keys.txt', '')

        # Load keys
        keys = load_keys(os.path.join(keys_dir, key_file))
        if not keys:
            print(f"Skipping {bundle_name} - no keys found")
            continue

        # Find original properties file
        original_file = None
        for bundle_dir in [intellij_bundles, android_bundles]:
            potential_file = os.path.join(bundle_dir, f'{bundle_name}.properties')
            if os.path.exists(potential_file):
                original_file = potential_file
                break

        if not original_file:
            print(f"Warning: No original properties file found for {bundle_name}")
            continue

        # Load original properties
        original_props = load_properties(original_file)

        # Generate Korean properties
        korean_content = generate_korean_properties(keys, original_props, bundle_name)

        # Write output file (without _ko suffix, just Bundle.properties)
        output_file = os.path.join(output_dir, f'{bundle_name}.properties')
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(korean_content)

        print(f"Generated {bundle_name}.properties ({len(keys)} keys)")

    print(f"\nDone! Generated files in {output_dir}")


if __name__ == '__main__':
    main()
