import json
import os

translated_keys = {
  "YAMLLanguageCodeStyleSettingsProvider.indent.sequence.value": "시퀀스 값 들여쓰기",
  "YAMLLanguageCodeStyleSettingsProvider.autoinsert.sequence.marker": "Enter 입력 시 하이픈(-) 자동 삽입",
  "YAMLBreadcrumbsInfoProvider.copy.key.to.clipboard": "키를 클립보드에 복사",
  "YAMLElementDescriptionProvider.type.anchor": "앵커",
  "YAMLAnchorRenameProcessor.lost.alias": "별칭이 다른 앵커를 참조하게 됩니다.",
  "YAMLAnchorRenameProcessor.reuse": "동일한 이름의 앵커가 이미 존재합니다.",
  "YAMLAliasResolveNodeProvider.action.name": "별칭이 지정된 하위 트리",
  "YAMLAliasResolveNodeProvider.action.description": "별칭을 확인하고 구조에 참조된 값을 표시합니다.",
  "YAMLKeysSearchEverywhereContributor.group.name": "설정 키",
  "YamlKeyCompletionInsertHandler.insert.value": "값 삽입",
  "YamlKeyCompletionInsertHandler.remove.key": "키 제거",
  "inspections.group.name": "YAML",
  "inspections.unresolved.alias.name": "해결되지 않은 별칭",
  "inspections.unresolved.alias.message": "{0} 별칭을 확인할 수 없습니다",
  "inspections.recursive.alias.name": "재귀적 별칭",
  "inspections.recursive.alias.message": "별칭은 재귀적일 수 없습니다.",
  "inspections.schema.validation.name": "JSON 스키마 유효성 검사",
  "inspections.schema.deprecation.name": "더 이상 사용되지 않는 YAML 키",
  "inspections.schema.deprecation.text": "''{0}'' 키는 더 이상 사용되지 않습니다: {1}",
  "inspections.schema.validation.prefix": "스키마 검사:",
  "inspections.duplicated.keys.name": "중복된 YAML 키",
  "inspections.unused.anchor.name": "사용되지 않는 앵커",
  "inspections.types.mismatch.name": "의심스러운 타입 불일치",
  "inspections.incompatible.types.message": "값의 타입이 ''{0}''인 반면 다른 값은 ''{1}'' 타입을 사용합니다",
  "inspections.incompatible.types.quickfix.wrap.quotes.message": "따옴표로 감싸기",
  "inspections.incompatible.types.quickfix.wrap.all.quotes.message": "시퀀스의 모든 스칼라를 따옴표로 감싸기",
  "inspections.unused.anchor.message": "{0} 앵커가 사용되지 않았습니다.",
  "inspections.unused.anchor.quickfix.name": "앵커 제거",
  "inspections.invalid.child.in.block.mapping": "블록 매핑의 잘못된 하위 요소",
  "inspections.invalid.child.in.block.sequence": "블록 시퀀스의 잘못된 하위 요소",
  "inspections.invalid.list.item.indent": "잘못된 목록 항목 들여쓰기",
  "inspections.invalid.key.indent": "잘못된 블록 매핑 키 들여쓰기",
  "annotator.same.line.composed.value.message": "블록 구성 값을 키와 같은 줄에 지정하는 것은 금지되어 있습니다.",
  "yaml.smartkeys.option.title": "YAML",
  "find.usages.scalar": "스칼라",
  "find.usages.sequence": "시퀀스",
  "find.usages.mapping": "매핑",
  "find.usages.key.value": "키-값",
  "find.usages.document": "문서",
  "find.usages.unnamed": "<이름 없음>",
  "element.presentation.document.type": "YAML 문서",
  "suppress.inspection.key": "''{1}'' 키에 대해 ''{0}'' 억제",
  "suppress.inspection.file": "''{1}'' 파일에 대해 ''{0}'' 억제",
  "yaml.intention.category.name": "YAML",
  "yaml.intention.name.inline.collection": "컬렉션 인라인으로 표시",
  "yaml.intention.name.expand.collection": "컬렉션 확장",
  "yaml.intention.name.expand.all.collections.inside": "내부의 모든 컬렉션 확장",
  "yaml.progress.title.inlining.collection": "컬렉션 인라인화 중\\u2026",
  "yaml.progress.title.expanding.yaml.collection": "yaml 컬렉션을 확장하는 중\\u2026",
  "YAMLFoldingSettings.title": "YAML"
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

print("YAMLBundle batch 2 translated successfully.")