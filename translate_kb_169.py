import json
from pathlib import Path

def update_missing_keys():
    file_path = Path("missing_translations/missing_keys_korean.json")

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    ko_dict = {
        "terms.property": "속성",
        "duplicate.property.key.error.message": "중복된 속성 키",
        "filetype.properties.description": "속성",
        "rename.bundle.enter.new.resource.bundle.base.name.prompt.text": "새 리소스 번들 기본 이름 입력",
        "rename.bundle.enter.new.resource.bundle.section.name.prompt.text": "새 리소스 번들 섹션 이름 입력",
        "rename.resource.bundle.dialog.title": "리소스 번들 이름 바꾸기",
        "rename.resource.bundle.section.dialog.title": "리소스 번들 섹션 이름 바꾸기",
        "properties.files.inspection.group.display.name": "속성 파일",
        "unused.property.inspection.display.name": "사용되지 않는 속성",
        "searching.for.property.key.progress.text": "{0} 검색 중",
        "unused.property.problem.descriptor.name": "사용되지 않는 속성",
        "unused.property.problem.descriptor.name.offline": "사용되지 않는 속성 ''{0}''",
        "remove.property.quick.fix.name": "속성 제거",
        "no.property.selected.panel.label": "<html><body><center>값을 편집하려면 왼쪽에서 속성 이름을 선택하세요.</center></body></html>",
        "select.property.separator.dialog.text": "구분자 선택",
        "select.property.separator.dialog.title": "속성 키 구분자",
        "select.separator.action.with.empty.separator.name": "기타...",
        "filetype.resourcebundle.description": "리소스 번들",
        "filetype.resourcebundle.display.name": "리소스 번들",
        "property.key.expected.parsing.error.message": "속성 키가 필요합니다.",
        "project.view.resource.bundle.tree.node.text": "리소스 번들 ''{0}''",
        "structure.view.group.by.prefixes.action.name": "접두사 기준",
        "structure.view.group.by.prefixes.action.description": "공통 키 접두사를 기준으로 속성을 그룹화합니다.",
        "unresolved.property.key": "속성 키를 확인할 수 없습니다.",
        "unused.property.suppress.for.property": "이 속성에 대해 표시 안 함",
        "unused.property.suppress.for.file": "전체 파일에 대해 표시 안 함",
        "i18nize.dialog.title": "하드코딩된 문자열 국제화",
        "i18nize.multiple.strings.dialog.title": "하드코딩된 문자열 국제화",
        "action.I18nize.text": "국제화(&Z)...",
        "action.I18nize.description": "Java 문자열 리터럴 또는 JSP 텍스트를 국제화된 표현식으로 교체합니다.",
        "i18nize.cant.create.properties.file.because.its.name.is.associated": "파일 이름이 {1}와(과) 연결되어 있어 ''{0}'' 속성 파일을 생성할 수 없습니다.",
        "i18nize.error.creating.properties.file": "속성 파일 생성 오류",
        "i18nize.empty.file.path": "속성 파일 경로를 지정하세요.",
        "i18nize.dialog.property.file.chooser.title": "속성 파일 선택",
        "i18nize.dialog.searching.for.already.existing.properties": "이미 존재하는 속성 검색 중...",
        "i18nize.dialog.error.property.already.defined.message": "''{1}'' 파일에 ''{0}'' 속성이 이미 존재합니다. 값을 덮어쓰시겠습니까?",
        "i18nize.dialog.error.property.already.defined.title": "속성이 이미 존재함",
        "i18n.quickfix.property.panel.title": "속성 정보",
        "i18n.quickfix.property.panel.update.all.files.in.bundle.checkbox": "리소스 번들의 모든 속성 파일 업데이트(&R)",
        "i18n.quickfix.property.panel.properties.file.label": "속성 파일(&P):",
        "i18n.quickfix.property.panel.property.value.label": "속성 값(&V):",
        "i18n.quickfix.property.panel.property.key.label": "속성 키(&K):",
        "i18n.message.empty": "비어 있음",
        "radio.button.create.new.property": "새 속성 생성(&N)",
        "radio.button.use.existing.property": "기존 속성 사용(&S)",
        "quickfix.i18n.command.name": "국제화",
        "create.property.quickfix.text": "속성 생성",
        "unescape": "이스케이프 해제",
        "trail.spaces.property.inspection.display.name": "속성에 후행 공백 표시",
        "use.ellipsis.property.inspection.display.name": "줄임표 대신 점 3개 사용"
    }

    filename = "PropertiesBundle.properties"
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
