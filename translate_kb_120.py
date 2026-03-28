import json
from pathlib import Path

def update_missing_keys():
    file_path = Path("missing_translations/missing_keys_korean.json")
    
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    ko_dict = {
        "action.Markdown.Styling.CreateOrChangeList.text": "목록 만들기 또는 변경",
        "markdown.floating.toolbar.customizable.group.name": "Markdown 편집기 플로팅 툴바",
        "action.Markdown.GenerateTableOfContents.text": "목차 생성",
        "action.Markdown.GenerateTableOfContents.insert.popup.text": "목차",
        "action.Markdown.GenerateTableOfContents.update.text": "목차 업데이트",
        "markdown.incorrectly.numbered.list.item.inspection.name": "번호가 잘못 지정된 목록 항목",
        "markdown.incorrectly.numbered.list.item.inspection.text": "항목 번호가 잘못 지정되었습니다. 항목 번호 {0}이(가) 예상되지만 {1}이(가) 지정되었습니다.",
        "markdown.fix.list.items.numbering,quick.fix.text": "목록 항목 번호 매기기 수정",
        "notification.group.markdown": "Markdown",
        "markdown.outdated.table.of.contents.inspection.name": "오래된 목차 섹션",
        "markdown.outdated.table.of.contents.inspection.description": "이 목차 섹션은 문서의 실제 구조와 일치하지 않습니다.",
        "markdown.outdated.table.of.contents.quick.fix.name": "목차 섹션 업데이트",
        "markdown.link.destination.with.spaces.inspection.name": "링크에는 공백이 포함되어서는 안 됨",
        "markdown.link.destination.with.spaces.inspection.description": "서로 다른 도구 간의 일관성을 보장하기 위해 링크에는 공백이 포함되어서는 안 됩니다.",
        "markdown.link.destination.with.spaces.quick.fix.name": "다음으로 바꾸기: {0}",
        "markdown.notification.mermaid.advertisement.title": "플러그인 제안",
        "markdown.notification.mermaid.advertisement.text": "Mermaid 플러그인을 사용하여 확장된 Mermaid.js 언어 지원 및 편집 지원을 받으세요.",
        "markdown.notification.mermaid.advertisement.remind.later.action.text": "나중에 알림",
        "markdown.notification.mermaid.advertisement.ignore.action.text": "다시 표시하지 않음",
        "markdown.notification.mermaid.advertisement.install.action.text": "Mermaid 플러그인 설치",
        "markdown.line.marker.mermaid.advertisement.tooltip.text": "Mermaid 플러그인 설치",
        "markdown.smart.keys.configurable.name": "Markdown",
        "markdown.smart.keys.configurable.tables.group.name": "표",
        "markdown.smart.keys.configurable.tables.reformat.on.type": "입력 시 표 서식 재지정",
        "markdown.smart.keys.configurable.tables.insert.html.line.break": "표 셀 안에 새 줄 대신 HTML 줄바꿈('<br/>') 삽입",
        "markdown.smart.keys.configurable.tables.insert.new.row": "Shift+Enter를 사용하여 새 표 행 삽입",
        "markdown.smart.keys.configurable.tables.use.cell.navigation": "Tab/Shift+Tab을 사용하여 표 셀 탐색",
        "markdown.smart.keys.configurable.lists.group.name": "목록",
        "markdown.smart.keys.configurable.lists.adjust.indentation.on.type": "입력 시 들여쓰기 조정",
        "markdown.smart.keys.configurable.lists.smart.enter.backspace": "스마트 Enter 및 Backspace 사용",
        "markdown.smart.keys.configurable.lists.renumber.lists": "입력 시 목록 번호 다시 매기기",
        "markdown.smart.keys.configurable.lists.numbering": "목록 번호 매기기:",
        "markdown.smart.keys.configurable.lists.numbering.sequential": "순차적으로",
        "markdown.smart.keys.configurable.lists.numbering.all.ones": "'1.'로 시작",
        "markdown.smart.keys.configurable.lists.numbering.previous.number": "이전 번호 사용",
        "markdown.smart.keys.configurable.other.group.name": "기타",
        "markdown.smart.keys.configurable.other.file.drop": "드래그 앤 드롭으로 이미지나 파일에 대한 링크 삽입",
        "markdown.code.folding.configurable.collapse.front.matter": "프런트 매터 축소",
        "markdown.code.folding.configurable.collapse.links": "링크 축소",
        "markdown.code.folding.configurable.collapse.tables": "표 축소",
        "markdown.code.folding.configurable.collapse.code.fences": "코드 펜스 축소",
        "markdown.code.folding.configurable.collapse.table.of.contents": "목차 축소",
        "markdown.html.anchor.symbol.presentation.container.text": "앵커",
        "markdown.dumb.mode.navigation.is.not.available.notification.text": "탐색을 사용할 수 없습니다. 프로젝트를 분석하는 중\\u2026",
        "group.Markdown.Preview.FontSize.text": "미리보기 글꼴 크기",
        "action.Markdown.Preview.IncreaseFontSize.text": "미리보기 글꼴 크기 늘리기",
        "action.Markdown.Preview.DecreaseFontSize.text": "미리보기 글꼴 크기 줄이기",
        "action.Markdown.Preview.ResetFontSize.text": "미리보기 글꼴 크기 재설정",
        "action.Markdown.Preview.AdjustFontSize.text": "글꼴 크기 조정\\u2026",
        "action.Markdown.Preview.Find.text": "찾기\\u2026"
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
