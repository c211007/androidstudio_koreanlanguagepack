import json
from pathlib import Path

def update_missing_keys():
    file_path = Path("missing_translations/missing_keys_korean.json")
    
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    ko_dict = {
        "markdown.plugin.name": "Markdown",
        "markdown.editor.name": "Markdown 분할 편집기",
        "markdown.editor.preview.name": "Markdown HTML 미리보기",
        "markdown.editor.colors.text": "텍스트",
        "markdown.editor.colors.bold": "스타일//굵은 텍스트",
        "markdown.editor.colors.bold_marker": "스타일//굵은 마커",
        "markdown.editor.colors.italic": "스타일//기울임꼴 텍스트",
        "markdown.editor.colors.italic_marker": "스타일//기울임꼴 마커",
        "markdown.editor.colors.strikethrough": "스타일//취소선",
        "markdown.editor.colors.explicit_link": "링크//명시적 링크",
        "markdown.editor.colors.header_level_1": "헤더//1차 레벨 헤더",
        "markdown.editor.colors.header_level_2": "헤더//2차 레벨 헤더",
        "markdown.editor.colors.header_level_3": "헤더//3차 레벨 헤더",
        "markdown.editor.colors.header_level_4": "헤더//4차 레벨 헤더",
        "markdown.editor.colors.header_level_5": "헤더//5차 레벨 헤더",
        "markdown.editor.colors.header_level_6": "헤더//6차 레벨 헤더",
        "markdown.editor.colors.code_span": "코드//코드 범위",
        "markdown.editor.colors.code_span_marker": "코드//코드 범위 마커",
        "markdown.editor.colors.code_block": "코드//코드 블록",
        "markdown.editor.colors.code_fence": "코드//코드 펜스",
        "markdown.editor.colors.blockquote": "블록 인용구//블록 인용구",
        "markdown.editor.colors.hrule": "수평 눈금자",
        "markdown.editor.colors.table_separator": "표 구분 기호",
        "markdown.editor.colors.reference_link": "링크//참조 링크",
        "markdown.editor.colors.auto_link": "링크//자동 링크",
        "markdown.editor.colors.unordered_list": "목록//순서 없는 목록",
        "markdown.editor.colors.ordered_list": "목록//순서 있는 목록",
        "markdown.editor.colors.list_item": "목록//목록 항목",
        "markdown.editor.colors.link_definition": "링크//링크 정의",
        "markdown.editor.colors.html_block": "HTML//HTML 블록",
        "markdown.editor.colors.inline_html": "HTML//인라인 HTML",
        "markdown.editor.colors.blockquote_marker": "블록 인용구//블록 인용구 마커",
        "markdown.editor.colors.list_marker": "목록//목록 마커",
        "markdown.editor.colors.header_marker": "헤더//헤더 마커",
        "markdown.editor.colors.image": "링크//이미지",
        "markdown.editor.colors.link_text": "링크//링크 텍스트",
        "markdown.editor.colors.link_label": "링크//링크 레이블",
        "markdown.editor.colors.link_destination": "링크//링크 대상",
        "markdown.editor.colors.link_title": "링크//링크 제목",
        "markdown.editor.colors.definition_list": "정의 목록//정의 목록",
        "markdown.editor.colors.definition_list_marker": "정의 목록//정의 마커",
        "markdown.editor.colors.definition": "정의 목록//정의",
        "markdown.editor.colors.term": "정의 목록//용어",
        "markdown.settings.name": "Markdown",
        "markdown.settings.css.title.name": "사용자 지정 CSS",
        "markdown.settings.preview.extensions.name": "Markdown 확장:",
        "markdown.settings.default.layout": "기본 레이아웃:",
        "markdown.settings.preview.font.size": "미리보기 글꼴 크기:",
        "markdown.settings.preview.auto.scroll.checkbox": "편집기와 미리보기에서 스크롤 동기화",
        "markdown.settings.no.providers": "사용 가능한 미리보기 제공업체가 없습니다."
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
