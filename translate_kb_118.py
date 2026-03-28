import json
from pathlib import Path

def update_missing_keys():
    file_path = Path("missing_translations/missing_keys_korean.json")
    
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    ko_dict = {
        "markdown.settings.stylesheet.path.validation.error": "파일을 로드하지 못했습니다.",
        "markdown.settings.stylesheet.path.outside.project.error": "파일이 현재 프로젝트에 속하지 않습니다.",
        "markdown.settings.stylesheet.path.disabled.for.default.project": "기본 프로젝트에 대해 사용자 지정 스타일시트 경로를 설정할 수 없습니다.",
        "markdown.notification.unsafe.stylesheet.title": "안전하지 않은 사용자 지정 스타일시트",
        "markdown.notification.unsafe.stylesheet.load.error.text": "사용자 지정 스타일시트를 로드하지 못했습니다. 대신 기본 스타일시트가 사용됩니다.",
        "markdown.notification.unsafe.stylesheet.outside.project.text": "사용자 지정 스타일시트가 현재 프로젝트 외부에 있으며 로드되지 않습니다. 대신 기본 스타일시트가 사용됩니다.",
        "dialog.message.tried.to.use.preview.panel.provider": "미리보기 패널 제공업체({0})를 사용하려고 시도했지만 사용할 수 없습니다. 기본값으로 되돌리는 중입니다.",
        "action.Markdown.ImportFromDocx.text": "Word 문서 가져오기\\u2026",
        "markdown.import.from.docx.dialog.title": "Word 문서를 Markdown으로 가져오기",
        "markdown.import.dialog.ok.button": "가져오기",
        "markdown.import.docx.convert.task.title": "Microsoft Word에서 Markdown으로 변환",
        "markdown.import.export.dialog.new.name.label": "이름:",
        "markdown.import.export.dialog.create.directory": "디렉터리 만들기",
        "markdown.import.export.dialog.target.directory": "대상 디렉터리 선택",
        "markdown.import.export.dialog.target.directory.description": "파일이 이 디렉터리에 생성됩니다.",
        "markdown.import.export.dialog.target.directory.label": "위치:",
        "action.Markdown.Export.text": "Markdown 파일을 다음으로 내보내기\\u2026",
        "markdown.export.from.docx.dialog.title": "Markdown 내보내기",
        "markdown.export.dialog.ok.button": "내보내기",
        "markdown.export.dialog.filetype.label": "형식:",
        "markdown.export.success.msg": "{0}을(를) 성공적으로 내보냈습니다.",
        "markdown.export.failure.msg": "{0}을(를) 내보내지 못했습니다.",
        "markdown.export.validation.failure.msg": "{0}(으)로 변환은 Markdown 미리보기가 열려 있는 경우에만 가능합니다.",
        "markdown.export.to.docx.failure.msg": "Microsoft Word로 내보낼 수 없습니다: Pandoc을 찾을 수 없습니다.",
        "markdown.export.to.html.save.images.checkbox": "이미지 저장 위치:",
        "markdown.export.images.not.found.msg": "파일의 이미지 {0}을(를) 찾을 수 없습니다.",
        "markdown.export.style.not.found.msg": "파일의 스타일 {0}을(를) 찾을 수 없습니다.",
        "markdown.export.dialog.checkbox.tooltip": "비활성화하면 이미지가 HTML 파일에 삽입됩니다.",
        "markdown.export.task": "Markdown을 {0}(으)로 내보내기",
        "group.Markdown.Tools.text": "Markdown",
        "action.Markdown.ConfigurePandoc.text": "Pandoc 구성\\u2026",
        "markdown.intention.category": "Markdown",
        "markdown.rename.dialog.title": "바인딩된 문서 이름 바꾸기",
        "markdown.rename.dialog.description": "다음 이름의 파일 이름을 다음으로 바꾸기:",
        "markdown.rename.entity.name": "Markdown 문서",
        "markdown.rename.factory.option.name": "바인딩된 문서 이름 바꾸기",
        "markdown.runner.launch.command": "''{0}'' 실행",
        "markdown.runner.launch.block": "블록 실행",
        "markdown.runner.launch.line": "줄 실행",
        "action.Markdown.OpenDevtools.text": "현재 Markdown 미리보기를 위한 개발자 도구 창 열기",
        "action.Markdown.InsertEmptyTable.text": "표 삽입",
        "action.Markdown.InsertEmptyTable.insert.popup.text": "표",
        "action.Markdown.Table.InsertTableColumn.InsertBefore.text": "왼쪽에 열 삽입",
        "action.Markdown.Table.InsertTableColumn.InsertAfter.text": "오른쪽에 열 삽입",
        "action.Markdown.Table.SelectCurrentColumn.SelectContentCells.text": "열 셀 선택",
        "action.Markdown.Table.RemoveCurrentColumn.text": "열 제거",
        "group.Markdown.Table.ColumnAlignmentActions.text": "열 맞춤 설정",
        "group.Markdown.TableColumnActions.ColumnAlignmentActions.Popup.text": "열 맞춤",
        "action.Markdown.Table.SetColumnAlignment.Left.text": "왼쪽 맞춤",
        "action.Markdown.Table.SetColumnAlignment.Center.text": "가운데 맞춤"
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
