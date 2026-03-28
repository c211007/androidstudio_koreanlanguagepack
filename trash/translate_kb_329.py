import json
import os

translated_keys = {
  "filetype.dtd.description": "XML 문서 유형 정의(DTD)",
  "filetype.html.description": "HTML",
  "filetype.xhtml.description": "XHTML",
  "filetype.xml.description": "XML",
  "options.xml.display.name": "XML",
  "options.xml.attribute.descriptor.attribute.name": "속성 이름",
  "options.xml.attribute.descriptor.attribute.value": "속성 값",
  "options.xml.attribute.descriptor.comment": "주석",
  "options.xml.attribute.descriptor.descriptor.entity,reference": "엔티티 참조(Entity Reference)",
  "options.xml.attribute.descriptor.matched.tag.name": "일치하는 태그",
  "options.xml.attribute.descriptor.namespace.prefix": "네임스페이스 접두사",
  "options.xml.attribute.descriptor.prologue": "프롤로그",
  "options.xml.attribute.descriptor.tag.data": "태그 데이터",
  "options.xml.attribute.descriptor.tag.name.custom": "사용자 지정 태그 이름",
  "options.xml.attribute.descriptor.tag.name": "태그 이름",
  "options.xml.attribute.descriptor.tag": "태그",
  "options.html.display.name": "HTML",
  "options.html.attribute.descriptor.attribute.name": "속성 이름",
  "options.html.attribute.descriptor.attribute.value": "속성 값",
  "options.html.attribute.descriptor.code": "HTML 코드",
  "options.html.attribute.descriptor.comment": "주석",
  "options.html.attribute.descriptor.entity.reference": "엔티티 참조(Entity reference)",
  "options.html.attribute.descriptor.tag.name": "태그 이름",
  "options.html.attribute.descriptor.tag.tree": "태그 트리(수준 {0})",
  "options.html.attribute.descriptor.tag": "태그"
}

file_path = "c:/Users/klanary/Desktop/vscode 모음/android_korean/androidstudio_koreanlanguagepack/missing_translations/missing_keys_korean.json"
with open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)

file_found = False
for item in data["new_files"]:
    if item["filename"] == "XmlCoreBundle.properties":
        item["keys"].update(translated_keys)
        file_found = True
        break

if not file_found:
    data["new_files"].append({
        "filename": "XmlCoreBundle.properties",
        "keys": translated_keys
    })

with open(file_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("XmlCoreBundle translated successfully.")