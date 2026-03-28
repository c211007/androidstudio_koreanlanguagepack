import json
from pathlib import Path

def update_missing_keys():
    file_path = Path("missing_translations/missing_keys_korean.json")
    
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    ko_dict = {
        "markdown.navigate.to.header": "이동할 헤더 선택",
        "markdown.navigate.to.header.no.headers": "이동할 헤더를 찾을 수 없습니다.",
        "markdown.settings.preview.layout.label": "미리보기 레이아웃:",
        "markdown.settings.preview.layout.vertical": "수직으로 분할",
        "markdown.settings.preview.layout.horizontal": "수평으로 분할",
        "markdown.settings.enable.injections": "코드 펜스에 언어 주입",
        "markdown.settings.enable.enhance.editing.experience": "편집기에서 자동 지원",
        "markdown.settings.download.extension.notification.title": "Markdown 확장 파일 다운로드",
        "markdown.settings.download.extension.notification.success.content": "확장 파일이 성공적으로 다운로드되었습니다!",
        "markdown.settings.download.extension.notification.failure.content": "필수 확장 파일 다운로드에 실패했습니다!",
        "markdown.settings.extension.install.label": "설치",
        "markdown.settings.extension.enable.searchable.option.text": "{0} 확장 사용",
        "markdown.settings.notification.title": "Markdown 설정",
        "markdown.extract.link.extract.duplicates.description": "{0}에서 참조 링크로 대체할 수 있는 중복된 링크 {1}개를 감지했습니다. 검토하고 일괄 대체하시겠습니까?",
        "markdown.extract.link.extract.duplicates.warning": "일부 중복 링크에 다른 제목이 있습니다. 대체하는 동안 지워집니다.",
        "markdown.extract.link.extract.link.replace": "링크 바꾸기",
        "markdown.extract.link.refactoring.dialog.title": "중복 바꾸기",
        "markdown.settings.show.problems": "코드 펜스에 문제 표시",
        "markdown.hide.problems.intention.text": "코드 펜스에서 문제 숨기기",
        "markdown.hide.problems.notification.title": "코드 펜스 문제",
        "markdown.hide.problems.notification.content": "Markdown의 펜싱된 코드 블록에 대한 문제 강조 표시가 비활성화되었습니다. 설정의 언어 및 프레임워크 | Markdown 아래에서 활성화할 수 있습니다.",
        "markdown.hide.problems.notification.rollback.action.text": "롤백",
        "markdown.extensions.plantuml.display.name": "PlantUML",
        "markdown.extensions.plantuml.description": "<html>PlantUML은 텍스트 설명에서 다양한 종류의 다이어그램을 생성하기 위한 도구입니다.</html>",
        "markdown.extensions.plantuml.download.line.marker.text": "PlantUML 설치",
        "markdown.settings.commandrunner.text": "Markdown 파일에서 직접 실행할 수 있는 명령 감지",
        "action.org.intellij.plugins.markdown.ui.actions.scrolling.AutoScrollAction.text": "스크롤 동기화",
        "action.org.intellij.plugins.markdown.ui.actions.scrolling.AutoScrollAction.description": "미리보기 패널 스크롤을 편집기와 동기화",
        "group.Markdown.Toolbar.Right.text": "Markdown 편집기 레이아웃 작업",
        "action.org.intellij.plugins.markdown.ui.actions.styling.MarkdownIntroduceLinkReferenceAction.text": "참조로 변환",
        "action.org.intellij.plugins.markdown.ui.actions.styling.MarkdownIntroduceLinkReferenceAction.description": "인라인 링크를 참조 스타일 링크로 변환합니다.",
        "action.Markdown.Styling.CreateLink.text": "링크 만들기",
        "action.Markdown.Styling.CreateLink.insert.popup.text": "링크",
        "action.Markdown.Styling.CreateLink.unwrap.text": "링크 제거",
        "action.Markdown.Styling.CreateLink.description": "선택한 텍스트를 링크로 래핑합니다.",
        "action.Markdown.Styling.CreateLink.unwrap.description": "링크를 일반 텍스트로 래핑 해제합니다.",
        "action.org.intellij.plugins.markdown.ui.actions.styling.HeaderUpAction.text": "헤더 레벨 높이기",
        "action.org.intellij.plugins.markdown.ui.actions.styling.HeaderUpAction.description": "캐럿으로 헤더 레벨을 높입니다.",
        "action.org.intellij.plugins.markdown.ui.actions.styling.HeaderDownAction.text": "헤더 레벨 낮추기",
        "action.org.intellij.plugins.markdown.ui.actions.styling.HeaderDownAction.description": "캐럿으로 헤더 레벨을 낮춥니다.",
        "action.org.intellij.plugins.markdown.ui.actions.styling.ToggleCodeSpanAction.text": "코드",
        "action.org.intellij.plugins.markdown.ui.actions.styling.ToggleCodeSpanAction.description": "텍스트를 인라인 코드 범위로 서식 지정합니다.",
        "action.org.intellij.plugins.markdown.ui.actions.styling.ToggleItalicAction.text": "기울임꼴",
        "action.org.intellij.plugins.markdown.ui.actions.styling.ToggleItalicAction.description": "텍스트를 기울임꼴로 서식 지정합니다(강조).",
        "action.org.intellij.plugins.markdown.ui.actions.styling.ToggleStrikethroughAction.text": "취소선",
        "action.org.intellij.plugins.markdown.ui.actions.styling.ToggleStrikethroughAction.description": "텍스트를 취소선으로 서식 지정합니다.",
        "action.org.intellij.plugins.markdown.ui.actions.styling.ToggleBoldAction.text": "굵게",
        "action.org.intellij.plugins.markdown.ui.actions.styling.ToggleBoldAction.description": "텍스트를 굵게 서식 지정합니다(강한 강조).",
        "group.Markdown.Toolbar.Left.text": "Markdown 편집기 작업",
        "group.Markdown.Toolbar.Floating.text": "Markdown 편집기 플로팅 툴바"
    }
    
    filename = "MarkdownBundle.properties"
    found = False
    for file_entry in data.get('new_files', []):
        if file_entry['filename'] == filename:
            file_entry['keys'].update(ko_dict)
            found = True
            break
    if not found:
        data.setdefault('new_files', []).append({"filename": filename, "keys": ko_dict})
    
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        
    print(f"Updated {filename}")

if __name__ == "__main__":
    update_missing_keys()
