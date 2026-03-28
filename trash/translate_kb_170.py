import json
from pathlib import Path

def update_missing_keys():
    file_path = Path("missing_translations/missing_keys_korean.json")

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    ko_dict = {
        "options.properties.attribute.descriptor.property.key": "속성 키",
        "options.properties.attribute.descriptor.property.value": "속성 값",
        "options.properties.attribute.descriptor.key.value.separator": "키/값 구분 기호",
        "options.properties.attribute.descriptor.comment": "주석",
        "options.properties.attribute.descriptor.valid.string.escape": "유효한 문자열 이스케이프",
        "options.properties.attribute.descriptor.invalid.string.escape": "유효하지 않은 유니코드 코드 포인트",
        "resource.bundle.renamer": "리소스 번들 속성 파일 이름 바꾸기",
        "resource.bundle.renamer.dialog.description": "다음 이름의 리소스 번들 속성 파일 이름을 다음으로 변경:",
        "resource.bundle.renamer.entity.name": "리소스 번들",
        "resource.bundle.renamer.option": "연결된 리소스 번들 이름 바꾸기(&R)",
        "combine.properties.files.prompt.text": "번들 기본 이름을 사용하여 속성 파일을 리소스 번들로 결합하기",
        "combine.properties.files.title": "리소스 번들로 결합",
        "alpha.unsorted.properties.file.inspection.display.name": "속성 파일 또는 리소스 번들이 알파벳순으로 정렬되지 않음",
        "trailing.spaces.in.property.inspection.ignore.visible.spaces": "보이는 공백 무시",
        "wrong.property.key.value.delimiter.inspection.display.name": "속성 키/값 구분 기호가 코드 스타일 설정과 일치하지 않습니다.",
        "remove.property.intention.text": "속성 제거",
        "create.resource.bundle.dialog.error": "리소스 번들을 만들 수 없습니다",
        "create.resource.bundle.dialog.action.name": "리소스 번들 ''{0}'' 만들기",
        "create.resource.bundle.dialog.action.title": "리소스 번들",
        "create.resource.bundle.dialog.add.locales.validator.message": "추가할 로캘 코드 입력(로캘을 여러 개 추가하려면 쉼표 구분 기호 사용)",
        "create.resource.bundle.dialog.add.locales.validator.title": "로캘 추가",
        "add.property.files.to.resource.bundle.dialog.action.title": "리소스 번들에 속성 파일 추가",
        "action.EditPropertyValue.text": "속성 값 편집...",
        "duplicate.property.module.scope.option": "모듈",
        "duplicate.property.diff.key.option": "값이 다른 키 복제(&D)",
        "duplicate.property.file.scope.option": "파일",
        "duplicate.property.diff.key.progress.indicator.text": "중복된 속성 키 처리 중: {0}",
        "duplicate.property.project.scope.option": "프로젝트",
        "duplicate.property.value.option": "값 복제(&V)",
        "duplicate.property.value.progress.indicator.text": "중복된 속성 값 처리 중: {0}",
        "duplicate.property.diff.key.problem.descriptor": "값이 다른 중복 속성 키 ''{0}'' #treeend :<br>",
        "inspection.export.results.invalidated.item": "무효화된 항목",
        "duplicate.property.value.problem.descriptor": "키가 있는 중복 속성 값 ''{0}'' #treeend :<br>",
        "duplicate.property.key.problem.descriptor": "값이 있는 중복 속성 키 ''{0}'' #treeend :<br>",
        "duplicate.property.key.progress.indicator.text": "중복된 속성 키 처리 중: {0}",
        "duplicate.property.key.option": "키 복제(&K)",
        "action.DissociateResourceBundleAction.text": "리소스 번들 연결 해제",
        "action.DissociateResourceBundleSingle.text": "리소스 번들 ''{0}'' 연결 해제",
        "action.DissociateResourceBundleMultiple.text": "{0}개의 리소스 번들 연결 해제",
        "combine.properties.files.validation.error": "기본 이름은 ''{0}'' 파일에 대해 유효해야 합니다.",
        "keep.blank.lines.code.style.setting.name": "빈 줄 유지",
        "key.value.delimiter.code.style.settings.name": "키-값 구분 기호",
        "insert.space.around.key.value.delimiter.code.style.settings.name": "키-값 구분 기호 주위에 공백 삽입",
        "properties.files.code.style.node.title": "속성 파일",
        "whitespace.symbol.delimeter.combobox.presentation": "공백 기호",
        "rename.hides.existing.property.conflict": "새 속성 이름 ''{0}''이(가) 기존 속성을 숨깁니다.",
        "create.resource.bundle.add.all.btn.text": "모두 추가",
        "create.resource.bundle.locales.to.add.chooser.title": "추가할 로캘",
        "create.resource.bundle.add.locales.by.suffix.action.text": "접미사별 로캘 추가",
        "create.resource.bundle.invalid.locales.error.text": "잘못된 로캘"
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
