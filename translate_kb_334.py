import json
import os

translated_keys = {
  "title.xml": "XML",
  "comments": "주석",
  "checkbox.uniform.indent": "<style> 및 <script> 태그 내에서 HTML 들여쓰기 사용",
  "preserve": "유지",
  "remove.keep.with.tags": "제거(태그와 함께 유지)",
  "add.new.lines": "새 줄 추가",
  "checkbox.keep.white.spaces": "공백 유지",
  "checkbox.align.attributes": "속성 정렬",
  "checkbox.wrap.text": "텍스트 줄 바꿈",
  "checkbox.spaces.around.equals.in.attribute": "속성에서 \"=\" 주위",
  "checkbox.spaces.around.tag.name": "태그 이름 뒤",
  "checkbox.spaces.in.empty.tag": "빈 태그 내",
  "editbox.keep.blank.lines": "빈 줄 유지:",
  "checkbox.keep.line.breaks.in.text": "텍스트 내 줄 바꿈 유지",
  "checkbox.keep.line.breaks": "줄 바꿈 유지",
  "xml.code.style.border.title.cdata": "CDATA",
  "xml.code.style.checkbox.keep.whitespace.inside": "내부 공백 유지",
  "xml.code.style.label.whitespace.around": "주위 공백:",
  "label.lines": "줄",
  "label.or.if.tag.size.more.than": "또는 태그 크기가 다음보다 큰 경우",
  "label.insert.new.line.before": "다음 앞에 새 줄 삽입:",
  "label.remove.new.line.before": "다음 앞의 새 줄 제거:",
  "label.do.not.indent.children.of": "다음의 하위 항목을 들여쓰지 않음:",
  "inline.elements": "인라인 요소:",
  "label.keep.white.spaces.inside": "내부 공백 유지:",
  "don.t.break.if.inline.content": "인라인 콘텐츠인 경우 줄 바꿈 안 함:",
  "generated.quote.enforce.format": "포맷 시 강제 적용",
  "html.label.new.line.before.first.attribute": "첫 번째 속성 앞에 새 줄(&F):",
  "html.label.new.line.after.last.attribute": "마지막 속성 뒤에 새 줄(&L):",
  "checkbox.align.text": "텍스트 정렬"
}

file_path = "c:/Users/klanary/Desktop/vscode 모음/android_korean/androidstudio_koreanlanguagepack/missing_translations/missing_keys_korean.json"
with open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)

file_found = False
for item in data["new_files"]:
    if item["filename"] == "XmlUiBundle.properties":
        item["keys"].update(translated_keys)
        file_found = True
        break

if not file_found:
    data["new_files"].append({
        "filename": "XmlUiBundle.properties",
        "keys": translated_keys
    })

with open(file_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("XmlUiBundle translated successfully.")