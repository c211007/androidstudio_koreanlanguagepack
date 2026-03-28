import json
from pathlib import Path

def update_missing_keys():
    file_path = Path("missing_translations/missing_keys_korean.json")

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    ko_dict = {
        "create.resource.bundle.project.locales.title": "프로젝트 로캘",
        "create.resource.bundle.some.of.files.already.exist.error": "일부 파일이 이미 존재합니다.",
        "create.resource.bundle.no.locales.added.error": "추가된 로캘이 없습니다.",
        "create.resource.bundle.base.name.is.empty.error": "기본 이름이 비어 있습니다.",
        "create.resource.bundle.file.with.name.0.already.exist.error": "이름이 ''{0}''인 파일이 이미 존재합니다.",
        "create.resource.bundle.file.name.for.properties.file.0.is.invalid.error": "속성 파일 ''{0}''의 파일 이름이 잘못되었습니다.",
        "create.resource.bundle.add.locales.to.resource.bundle.title": "리소스 번들 {0}에 로캘 추가",
        "create.resource.bundle.action.text": "리소스 번들 만들기",
        "create.resource.bundle.default.locale.presentation": "기본 로캘",
        "properties.sorter.quick.fix.family.name": "리소스 번들 파일 정렬",
        "inspection.alpha.unsorted.properties.file.description": "속성 파일이 알파벳순으로 정렬되지 않았습니다.",
        "remove.trailing.spaces.fix.family.name": "후행 공백 제거",
        "use.ellipsis.fix.family.name": "세 개의 점을 줄임표로 교체",
        "inspection.trailing.spaces.in.property.trailing.spaces.description": "후행 공백",
        "inspection.use.ellipsis.in.property.description": "줄임표 대신 3개의 \"점\" 문자가 사용되었습니다.",
        "replace.key.value.delimiter.quick.fix.family.name": "코드 스타일에 따라 속성 키/값 구분 기호 교체",
        "structure.view.empty.property.presentation": "<property>",
        "group.by.0": "구분자: {0}",
        "group.by.title": "그룹화 기준:",
        "copy.destination.resource.bundle.label": "대상 리소스 번들(&D):",
        "copy.destination.new.name.label": "새 이름(&N):",
        "copy.property.0.label": "속성 {0} 복사",
        "copy.property.name.must.be.not.empty.error": "속성 이름은 비워둘 수 없습니다.",
        "copy.resource.bundles.are.not.matched.title": "리소스 번들이 일치하지 않습니다.",
        "copy.resource.bundles.are.not.matched.message": "소스 및 대상 리소스 번들 속성 파일이 올바르게 일치하지 않습니다. 그래도 속성을 복사하시겠습니까?",
        "align.properties.in.column.code.style.option": "열의 속성 정렬",
        "copy.property.with.name.0.already.exists.conflict": "이름이 ''{0}''인 속성이 이미 존재합니다.",
        "inspection.alpha.unsorted.properties.file.description1": "리소스 번들 ''{0}''의 속성 키가 알파벳순으로 정렬되지 않았습니다.",
        "button.add.all": "모두 추가",
        "label.resource.bundle.base.name": "리소스 번들 기본 이름:",
        "checkbox.use.xml.based.properties.files": "XML 기반 속성 파일 사용",
        "label.analyze.only.property.files.whose.name.matches": "이름이 일치하는 속성 파일만 분석:",
        "intention.category.properties": "속성",
        "copy.property.key.to.clipboard.intention.family.name": "클립보드에 속성 키 복사",
        "copy.property.value.to.clipboard.intention.family.name": "클립보드에 속성 값 복사",
        "predefined.configuration.duplicated.word.in.property.value": "속성 값에 중복된 단어",
        "predefined.configuration.double.single.quote.in.value.without.curly.brace": "속성 값에 { 없이 이중 '",
        "label.analysis.scope": "분석 범위(&A):",
        "ignore.unchanged.properties.text": "변경되지 않은 속성 무시"
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
