import json
import os

translated_keys = {
  "xml.intention.remove.unused.namespace.location": "사용되지 않는 네임스페이스 위치 제거",
  "xml.quickfix.escape.character": "''{0}''을(를) ''{1}''(으)로 이스케이프",
  "xml.quickfix.change.root.element.to": "루트 태그 이름을 {0}(으)로 변경",
  "xml.quickfix.change.attribute.value.family": "속성 값 변경",
  "xml.quickfix.change.attribute.value": "값을 {0}(으)로 변경",
  "xml.quickfix.declare.id.in.comment": "주석 어노테이션에 잘못된 ID 선언",
  "xml.quickfix.remove.attribute.family": "속성 제거",
  "xml.quickfix.remove.attribute.text": "{0} 속성 제거",
  "xml.quickfix.remove.extra.closing.tag": "추가 닫는 태그 제거",
  "xml.quickfix.remove.tag.family": "태그 제거(하위 항목 유지)",
  "xml.quickfix.remove.tag.text": "{0} 태그 제거",
  "xml.quickfix.remove.unused.namespace.decl": "사용되지 않는 네임스페이스 선언 제거",
  "xml.quickfix.schema.create.attribute.group": "{0} 속성 그룹 생성",
  "xml.quickfix.schema.create.attribute": "{0} 속성 생성",
  "xml.quickfix.schema.create.complex.type": "{0} 복합형 생성",
  "xml.quickfix.schema.create.element": "{0} 요소 생성",
  "xml.quickfix.schema.create.group": "{0} 그룹 생성",
  "xml.quickfix.schema.create.simple.type": "{0} 단순형 생성",
  "xml.options.label.regexp": "정규식(Regexp):"
}

file_path = "c:/Users/klanary/Desktop/vscode 모음/android_korean/androidstudio_koreanlanguagepack/missing_translations/missing_keys_korean.json"
with open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)

file_found = False
for item in data["new_files"]:
    if item["filename"] == "XmlAnalysisBundle.properties":
        item["keys"].update(translated_keys)
        file_found = True
        break

if not file_found:
    data["new_files"].append({
        "filename": "XmlAnalysisBundle.properties",
        "keys": translated_keys
    })

with open(file_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Batch 2 translated successfully.")