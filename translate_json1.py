import json

ko_dict = {
  "json.array": "배열",
  "json.object": "객체",
  "json.property": "속성",
  "syntax.error.missing.closing.quote": "닫는 따옴표가 없습니다.",
  "syntax.error.illegal.escape.sequence": "잘못된 이스케이프 시퀀스입니다.",
  "syntax.error.illegal.unicode.escape.sequence": "잘못된 유니코드 이스케이프 시퀀스입니다.",
  "syntax.error.illegal.floating.point.literal": "잘못된 부동 소수점 리터럴입니다.",
  "syntax.error.control.char.in.string": "문자열 리터럴에는 제어 문자 ''{0}''이(가) 허용되지 않습니다.",
  "json.inspection.group": "JSON 및 JSON5",
  "inspection.compliance.name": "JSON 표준 준수",
  "inspection.compliance5.name": "JSON5 표준 준수",
  "inspection.compliance.msg.comments": "JSON 표준에서는 주석을 허용하지 않습니다.",
  "inspection.compliance.msg.single.quoted.strings": "JSON 표준에서는 작은따옴표로 묶인 문자열을 허용하지 않습니다.",
  "inspection.compliance.msg.bad.token": "JSON 표준에서는 이러한 토큰을 허용하지 않습니다.",
  "inspection.compliance.msg.illegal.property.key": "JSON 표준에서는 속성 키로 큰따옴표로 묶인 문자열만 허용합니다.",
  "inspection.compliance.msg.trailing.comma": "JSON 표준에서는 후행 쉼표를 허용하지 않습니다.",
  "inspection.compliance.msg.multiple.top.level.values": "JSON 표준에서는 최상위 값을 하나만 허용합니다.",
  "inspection.compliance.option.comments": "주석에 대해 경고",
  "inspection.compliance.option.multiple.top.level.values": "여러 최상위 값에 대해 경고",
  "inspection.compliance.option.trailing.comma": "후행 쉼표에 대해 경고",
  "inspection.compliance.option.nan.infinity": "NaN 및 무한/음의 무한대 숫자 값에 대해 경고",
  "inspection.duplicate.keys.name": "객체 리터럴의 중복 키",
  "inspection.duplicate.keys.msg.duplicate.keys": "객체에 중복 키 ''{0}''이(가) 포함되어 있습니다.",
  "formatter.align.properties.caption": "정렬",
  "formatter.align.properties.none": "정렬 안 함",
  "formatter.align.properties.on.colon": "콜론 기준",
  "formatter.align.properties.on.value": "값 기준",
  "formatter.space_within_braces.label": "중괄호",
  "formatter.space_before_colon.label": "':' 앞",
  "formatter.space_after_colon.label": "':' 뒤",
  "formatter.trailing_comma.label": "후행 쉼표",
  "formatter.wrapping_arrays.label": "배열",
  "formatter.objects.label": "객체",
  "quickfix.add.double.quotes.desc": "큰따옴표로 래핑",
  "surround.with.object.literal.desc": "객체 리터럴",
  "surround.with.array.literal.desc": "배열 리터럴",
  "surround.with.quotes.desc": "따옴표",
  "json.template.context.type": "JSON",
  "json.copy.to.clipboard": "클립보드에 {0} 복사",
  "action.ConsoleView.ShowAsJsonAction.text": "JSON으로 표시"
}

with open('missing_translations/missing_keys_korean.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

filename = "JsonBundle.properties"
found = False
for file_entry in data.get('new_files', []):
    if file_entry['filename'] == filename:
        file_entry['keys'].update(ko_dict)
        found = True
        break
if not found:
    data.setdefault('new_files', []).append({"filename": filename, "keys": ko_dict})

print(f"Updated {filename} (Keys 1-40)")

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
