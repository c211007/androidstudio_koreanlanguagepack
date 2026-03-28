import json
from pathlib import Path

def update_missing_keys():
    file_path = Path("missing_translations/missing_keys_korean.json")
    
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    ko_dict = {
        "markdown.settings.preview.providers.label": "미리보기 렌더링 엔진:",
        "markdown.settings.external.css.path.label": "다음에서 로드:",
        "markdown.settings.custom.css.text.label": "CSS 규칙:",
        "markdown.settings.group.documents.in.project.tree": "이름은 같지만 확장자가 다른 문서 그룹화(.md, .html, .docx, .pdf)",
        "markdown.settings.smart.keys.comment": "<a>스마트 키 설정</a>에서 편집기 내 지원을 구성하세요.",
        "markdown.settings.pandoc.name": "Pandoc 설정",
        "markdown.settings.pandoc.executable.label": "Pandoc 실행 파일 경로:",
        "markdown.settings.pandoc.executable.test": "테스트",
        "markdown.settings.pandoc.executable.auto": "자동 감지됨: {0}",
        "markdown.settings.pandoc.executable.version.process": "Pandoc 버전 식별 중",
        "markdown.settings.pandoc.executable.default.error.msg": "Pandoc 실행 파일을 찾을 수 없습니다.",
        "markdown.settings.pandoc.executable.success.msg": "지정된 {0} 버전을 사용 중입니다.",
        "markdown.settings.pandoc.executable.error.msg": "지정된 실행 파일 \"{0}\"을(를) 실행할 수 없습니다.",
        "markdown.settings.pandoc.executable.run.in.safe.mode": "안전 모드에서는 Pandoc 명령을 실행할 수 없습니다.",
        "markdown.settings.pandoc.resource.path.label": "Microsoft Word 이미지를 다음 위치에 저장:",
        "markdown.style.settings.blank.lines.around.header": "헤더 주위",
        "markdown.style.settings.blank.lines.around.block.elements": "블록 요소 주위",
        "markdown.style.settings.blank.lines.between.paragraphs": "단락 사이",
        "markdown.style.settings.spacing.force.one.space": "하나의 공백 강제",
        "markdown.style.settings.spacing.between.words": "단어 사이",
        "markdown.style.settings.spacing.after.header.symbol": "헤더 기호 다음",
        "markdown.style.settings.spacing.after.list.marker": "목록 마커 다음",
        "markdown.style.settings.spacing.after.blockquote.marker": "블록 인용구 마커 다음",
        "markdown.style.settings.text.wrapping": "긴 텍스트 줄바꿈",
        "markdown.style.settings.text.wrapping.inside.blockquotes": "블록 인용구 안의 텍스트 줄바꿈",
        "markdown.style.settings.group.when.reformatting": "서식 재지정 시",
        "markdown.style.settings.line.breaks.inside.text.blocks": "텍스트 블록 안의 줄바꿈 유지",
        "markdown.style.settings.insert.quote.arrows": "블록 인용 화살표 삽입",
        "markdown.style.settings.format.tables": "표 서식 지정",
        "markdown.unresolved.file.inspection.name": "해결되지 않은 파일 참조",
        "markdown.inspection.group.ruby.name": "Markdown",
        "markdown.unresolved.header.reference.inspection.name": "해결되지 않은 헤더 참조",
        "markdown.unresolved.header.reference.inspection.text": "앵커 {0}을(를) 해결할 수 없습니다.",
        "markdown.unresolved.link.label.inspection.name": "해결되지 않은 링크 레이블",
        "markdown.unresolved.link.label.inspection.text": "링크 레이블 {0}을(를) 해결할 수 없습니다.",
        "markdown.folding.atx.1.name": "h1",
        "markdown.folding.atx.2.name": "h2",
        "markdown.folding.atx.3.name": "h3",
        "markdown.folding.atx.4.name": "h4",
        "markdown.folding.atx.5.name": "h5",
        "markdown.folding.atx.6.name": "h6",
        "markdown.folding.ordered.list.name": "순서가 있는 목록",
        "markdown.folding.unordered.list.name": "순서가 없는 목록",
        "markdown.folding.block.quote.name": "블록 인용구",
        "markdown.folding.table.name": "표",
        "markdown.folding.code.fence.name": "코드 펜스",
        "markdown.folding.front.matter.name": "프런트 매터",
        "markdown.folding.table.of.contents.name": "목차",
        "markdown.cannot.resolve.anchor.error.message": "앵커를 해결할 수 없습니다.",
        "markdown.cannot.resolve.anchor.in.file.error.message": "파일의 앵커를 해결할 수 없습니다."
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
