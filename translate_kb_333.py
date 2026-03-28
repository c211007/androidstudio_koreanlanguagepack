import json
import os

translated_keys = {
  "xml.parsing.absent.root.tag": "유효한 XML 문서에는 루트 태그가 있어야 합니다.",
  "xml.parsing.attribute.value.expected": "속성 값이 필요합니다",
  "xml.parsing.bad.character": "잘못된 문자",
  "xml.parsing.closing.tag.is.not.done": "닫는 태그가 유효하지 않습니다.",
  "xml.parsing.closing.tag.matches.nothing": "일치하는 닫는 태그가 없습니다.",
  "xml.parsing.closing.tag.name.missing": "닫는 태그 이름이 없습니다.",
  "xml.parsing.expected.attribute.eq.sign": "=가 필요합니다",
  "xml.parsing.named.element.is.not.closed": "{0} 요소가 닫히지 않았습니다.",
  "xml.parsing.multiple.root.tags": "여러 루트 태그",
  "xml.parsing.processing.instruction.name.expected": "처리 지침 이름이 필요합니다",
  "xml.parsing.tag.name.expected": "태그 이름이 필요합니다",
  "xml.parsing.tag.start.is.not.closed": "태그 시작이 닫히지 않았습니다.",
  "xml.parsing.top.level.element.is.not.completed": "최상위 수준 요소가 완료되지 않았습니다.",
  "xml.parsing.unclosed.attribute.value": "속성 값이 닫히지 않았습니다.",
  "xml.parsing.unescaped.ampersand.or.nonterminated.character.entity.reference": "이스케이프되지 않은 \\& 또는 종료되지 않은 문자/엔티티 참조",
  "xml.parsing.unexpected.end.of.file": "예기치 않은 파일 끝",
  "xml.parsing.unexpected.token": "예기치 않은 토큰",
  "xml.parsing.unexpected.tokens": "예기치 않은 토큰들",
  "xml.parsing.unterminated.processing.instruction": "처리 지침이 종료되지 않았습니다.",
  "xml.parsing.way.too.unbalanced": "불균형한 태그가 너무 많습니다. 태그 균형 맞추기 시도를 중단합니다."
}

file_path = "c:/Users/klanary/Desktop/vscode 모음/android_korean/androidstudio_koreanlanguagepack/missing_translations/missing_keys_korean.json"
with open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)

file_found = False
for item in data["new_files"]:
    if item["filename"] == "XmlSyntaxBundle.properties":
        item["keys"].update(translated_keys)
        file_found = True
        break

if not file_found:
    data["new_files"].append({
        "filename": "XmlSyntaxBundle.properties",
        "keys": translated_keys
    })

with open(file_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("XmlSyntaxBundle translated successfully.")