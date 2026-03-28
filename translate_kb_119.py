import json
from pathlib import Path

def update_missing_keys():
    file_path = Path("missing_translations/missing_keys_korean.json")
    
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    ko_dict = {
        "action.Markdown.Table.SetColumnAlignment.Right.text": "오른쪽 맞춤",
        "action.Markdown.Table.SwapColumns.SwapWithLeftColumn.text": "왼쪽으로 열 이동",
        "action.Markdown.Table.SwapColumns.SwapWithRightColumn.text": "오른쪽으로 열 이동",
        "action.Markdown.Table.SwapRows.SwapWithAbove.text": "위로 행 이동",
        "action.Markdown.Table.SwapRows.SwapWithBelow.text": "아래로 행 이동",
        "action.Markdown.Table.InsertRow.InsertAbove.text": "위에 행 삽입",
        "action.Markdown.Table.InsertRow.InsertBelow.text": "아래에 행 삽입",
        "action.Markdown.Table.SelectRow.text": "행 선택",
        "action.Markdown.Table.RemoveCurrentRow.text": "행 제거",
        "group.Markdown.TableContextMenuGroup.text": "표",
        "markdown.incorrect.table.formatting.inspection.name": "잘못된 표 서식",
        "markdown.incorrect.table.formatting.inspection.description": "표의 형식이 올바르지 않습니다.",
        "markdown.incorrect.table.formatting.inspection.local.cell.description": "셀의 형식이 올바르지 않습니다.",
        "markdown.no.table.borders.inspection.name": "표에 측면 테두리가 없음",
        "markdown.no.table.borders.inspection.description": "호환성을 위해, 모든 표 행에는 시작과 끝에 테두리(파이프 기호)가 있어야 합니다.",
        "markdown.fix.table.borders.intention.text": "표 테두리 수정",
        "markdown.reformat.table.intention.text": "표 서식 재지정",
        "markdown.fix.cell.alignment.intention.text": "셀 맞춤 수정",
        "markdown.insert.table.column.intention.family": "열 삽입",
        "markdown.insert.table.column.to.the.left.intention.text": "왼쪽에 열 삽입",
        "markdown.insert.table.column.to.the.right.intention.text": "오른쪽에 열 삽입",
        "markdown.remove.column.intention.text": "열 제거",
        "markdown.remove.row.intention.text": "행 제거",
        "markdown.set.column.alignment.intention.text": "열 맞춤 설정",
        "markdown.set.column.alignment.intention.popup.text": "열 맞춤 설정",
        "markdown.table.inlay.kind.name": "표 인레이",
        "markdown.table.inlay.kind.description": "표 주위의 수평 및 수직 막대. 열 및 행 작업을 제공합니다.",
        "action.Markdown.Insert.text": "삽입\\u2026",
        "markdown.untrusted.project.dialog.text": "\n  소스를 신뢰할 수 없는 경우 안전 모드를 유지하세요.\\n\\n\n  Markdown 파일에서 코드 블록 실행을 활성화하면 전체 프로젝트 로드, 실행 또는 빌드에도 동의하는 것으로 간주되며, \n  이때 빌드 스크립트에서 잠재적으로 악의적인 코드가 실행될 수 있습니다.",
        "action.Markdown.Extensions.CleanupExternalFiles.text": "Markdown 확장 외부 파일 정리\\u2026",
        "action.Markdown.Extensions.CleanupExternalFiles.description": "모든 Markdown 확장의 외부 파일을 정리합니다.",
        "Markdown.Extensions.CleanupExternalFiles.task.title": "확장 외부 파일 정리",
        "Markdown.Extensions.CleanupExternalFiles.notification.title": "외부 파일 정리",
        "Markdown.Extensions.CleanupExternalFiles.notification.text": "확장 외부 파일이 성공적으로 정리되었습니다.",
        "markdown.browse.external.link.open.confirmation.dialog.title": "링크 열기",
        "markdown.browse.external.link.open.confirmation.dialog.text": "{0}을(를) 여시겠습니까?",
        "markdown.browse.external.link.open.confirmation.dialog.do.not.ask.again.text": "''{0}://'' 링크에 대해 다시 묻지 않음",
        "markdown.browse.external.link.failed.notification.title": "외부 링크를 엽니다.",
        "markdown.browse.external.link.failed.notification.content": "외부 링크를 열지 못했습니다: {0}",
        "advanced.setting.markdown.hide.floating.toolbar": "플로팅 툴바 숨기기",
        "advanced.setting.markdown.squash.multiple.dashes.in.header.anchors": "헤더 앵커에서 여러 대시 스쿼시",
        "markdown.header.level.popup.normal.action.text": "일반",
        "markdown.header.level.popup.title.action.text": "제목",
        "markdown.header.level.popup.subtitle.action.text": "부제목",
        "markdown.header.level.popup.heading.action.text": "제목 {0}",
        "markdown.header.level.popup.heading.action.secondary.text": "(H{0})",
        "markdown.create.list.popup.unordered.action.text": "순서가 없는 목록",
        "markdown.create.list.popup.ordered.action.text": "순서가 있는 목록",
        "markdown.create.list.popup.checkmark.action.text": "체크 표시 목록",
        "action.Markdown.Styling.SetHeaderLevel.text": "헤더 스타일 설정"
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
