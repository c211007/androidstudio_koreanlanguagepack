import json
from pathlib import Path

def update_missing_keys():
    file_path = Path("missing_translations/missing_keys_korean.json")
    
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    ko_dict = {
        "markdown.image.file.drop.handler.drop.command.name": "이미지 끌어다 놓기",
        "markdown.insert.image.dialog.title": "이미지 삽입",
        "markdown.configure.image.dialog.browse.image.title": "이미지 선택",
        "markdown.configure.image.dialog.screen.reader.text.panel.title": "화면 판독기 텍스트",
        "markdown.configure.image.dialog.path.label": "경로:",
        "markdown.configure.image.dialog.width.label": "너비:",
        "markdown.configure.image.dialog.height.label": "높이:",
        "markdown.configure.image.dialog.convert.to.html.label": "HTML로 변환",
        "markdown.configure.image.dialog.title.label": "제목:",
        "markdown.configure.image.dialog.description.label": "설명:",
        "markdown.configure.image.text": "이미지 구성",
        "markdown.configure.image.title.text": "이미지 구성",
        "markdown.configure.image.line.marker.update.html.image.attributes.command.name": "HTML 이미지 속성 업데이트",
        "markdown.configure.image.line.marker.convert.html.to.markdown.command.name": "HTML 이미지를 Markdown으로 변환",
        "markdown.configure.image.line.marker.presentation": "이미지 구성({0})",
        "markdown.configure.markdown.image.line.marker.provider.name": "Markdown 이미지 구성",
        "markdown.configure.html.image.line.marker.provider.name": "HTML 이미지 구성",
        "action.org.intellij.plugins.markdown.ui.actions.styling.InsertImageAction.text": "이미지 삽입",
        "action.org.intellij.plugins.markdown.ui.actions.styling.InsertImageAction.insert.popup.text": "이미지",
        "action.org.intellij.plugins.markdown.ui.actions.styling.InsertImageAction.description": "캐럿 위치에 이미지를 삽입합니다.",
        "markdown.intention.category": "Markdown"
    }
    
    filename = "MarkdownImagesBundle.properties"
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
