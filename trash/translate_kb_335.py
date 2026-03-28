import json
import os

translated_keys = {
  "filetype.yaml.description": "YAML",
  "color.settings.yaml.name": "YAML",
  "color.settings.yaml.key": "키",
  "color.settings.yaml.string": "문자열",
  "color.settings.yaml.dstring": "큰따옴표 문자열",
  "color.settings.yaml.scalar.list": "'|' 블록",
  "color.settings.yaml.scalar.text": "'>' 블록",
  "color.settings.yaml.text": "텍스트",
  "color.settings.yaml.sign": "기호: 중괄호, 쉼표 등",
  "color.settings.yaml.comment": "주석",
  "color.settings.yaml.anchor": "앵커/별칭",
  "settings.comment.label": "주석",
  "new.name.conflicts.with": "키가 기존 키인 ''{0}''과(와) 충돌합니다.",
  "rename.same.name": "같은 이름",
  "rename.invalid.name": "''{0}''은(는) 유효한 키 이름이 아닙니다.",
  "yaml.smartkeys.option.paste": "붙여넣기 시 키 시퀀스 자동 확장",
  "YamlUnknownKeysInspectionBase.unknown.key": "여기에는 ''{0}'' 키가 올 수 없습니다.",
  "YamlMissingKeysInspectionBase.missing.keys": "필수 키 누락: ''{0}''",
  "YamlMissingKeysInspectionBase.add.missing.keys.quickfix.name": "누락된 키 추가",
  "YamlNonEditableKeysInspectionBase.noneditable.key": "''{0}'' 키는 사용자가 수정할 수 없습니다.",
  "YamlDeprecatedKeysInspectionBase.deprecated.key": "''{0}'' 키는 더 이상 사용되지 않습니다.",
  "YamlDeprecatedKeysInspectionBase.deprecated.value": "''{0}'' 값은 더 이상 사용되지 않습니다.",
  "YAMLDuplicatedKeysInspection.duplicated.key": "''{0}'' 키가 중복되었습니다.",
  "YAMLDuplicatedKeysInspection.remove.key.quickfix.name": "키 제거",
  "YAMLDuplicatedKeysInspection.merge.quickfix.name": "중복된 섹션 병합",
  "YamlNonEditableKeyInspectionBase.strip.noneditable.keys.quickfix.name": "파일에서 편집할 수 없는 키 모두 제거",
  "YamlUnknownValuesInspectionBase.error.value.is.required": "값이 필요합니다.",
  "YamlUnknownValuesInspectionBase.error.array.is.required": "배열이 필요합니다.",
  "YamlUnknownValuesInspectionBase.error.array.not.allowed": "단일 값이 필요합니다.",
  "YamlEnumType.validation.error.value.unknown": "여기에는 ''{0}'' 값이 올 수 없습니다.",
  "YamlEnumType.validation.warning.value.deprecated": "''{0}'' 값은 더 이상 사용되지 않습니다.",
  "YamlBooleanType.validation.error.quoted.value": "부울(Boolean) 값이 필요합니다.",
  "YamlMetaClass.error.scalar.value": "여기에는 스칼라 값이 허용되지 않습니다.",
  "YamlScalarType.error.scalar.value": "스칼라 값이 필요합니다.",
  "YamlIntegerType.error.integer.value": "정수 값이 필요합니다.",
  "YamlNumberType.error.numeric.value": "숫자 값이 필요합니다.",
  "parsing.error.sequence.item.expected": "시퀀스 항목이 필요합니다",
  "YAMLStructureViewDocument.element.name": "YAML 문서",
  "YAMLStructureViewSequenceItem.element.name": "시퀀스 항목",
  "YAMLParser.invalid.header.symbols": "잘못된 블록 스칼라 헤더입니다",
  "YAMLParser.multiple.anchors": "여러 개의 앵커는 허용되지 않습니다",
  "YAMLParser.multiple.tags": "여러 개의 태그는 허용되지 않습니다",
  "YAMLLanguageCodeStyleSettingsProvider.label.before": "':' 앞",
  "YAMLLanguageCodeStyleSettingsProvider.align.options.no": "정렬하지 않음",
  "YAMLLanguageCodeStyleSettingsProvider.align.options.colon": "콜론 기준",
  "YAMLLanguageCodeStyleSettingsProvider.align.options.value": "값 기준",
  "YAMLLanguageCodeStyleSettingsProvider.align.values": "맵의 값 정렬",
  "YAMLLanguageCodeStyleSettingsProvider.group.sequence.value": "시퀀스 값",
  "YAMLLanguageCodeStyleSettingsProvider.sequence.on.new.line": "시퀀스를 새 줄에 배치",
  "YAMLLanguageCodeStyleSettingsProvider.block.mapping.on.new.line": "블록 매핑을 새 줄에 배치"
}

file_path = "c:/Users/klanary/Desktop/vscode 모음/android_korean/androidstudio_koreanlanguagepack/missing_translations/missing_keys_korean.json"
with open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)

file_found = False
for item in data["new_files"]:
    if item["filename"] == "YAMLBundle.properties":
        item["keys"].update(translated_keys)
        file_found = True
        break

if not file_found:
    data["new_files"].append({
        "filename": "YAMLBundle.properties",
        "keys": translated_keys
    })

with open(file_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("YAMLBundle batch 1 translated successfully.")