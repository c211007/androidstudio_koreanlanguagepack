import json
import os

translated_keys = {
  "comments": "주석",
  "disable.emmet": "Emmet 비활성화",
  "edit.emmet.settings": "Emmet 설정 편집",
  "emmet.filter.single.line": "한 줄",
  "checkbox.collapse.xml.tags": "XML 태그",
  "xml.tag.info.no.attributes": "<속성 없음>",
  "intention.color.chooser.dialog": "색상 선택",
  "intention.name.split.attributes": "별도의 줄에 속성 배치",
  "intention.name.join.attributes": "한 줄에 속성 배치",
  "dialog.edit.template.checkbox.xsl.text": "XSL 텍스트",
  "checkbox.collapse.html.style.attribute": "HTML 'style' 속성",
  "label.lines": "줄",
  "emmet.filter.comment.tags": "주석 태그",
  "title.xml": "XML",
  "dialog.edit.template.checkbox.html": "HTML(&H)",
  "action.name.show.history.for.tag": "태그",
  "label.do.not.indent.children.of": "다음의 하위 항목 들여쓰기 안 함:",
  "checkbox.collapse.entities": "XML 엔티티",
  "dialog.edit.template.checkbox.html.text": "HTML 텍스트",
  "dialog.edit.template.checkbox.xml": "XML(&X)",
  "checkbox.collapse.data.uri": "데이터 URI",
  "action.name.show.history.for.text": "텍스트",
  "inspection.javadoc.html.not.required.label.text": "추가 선택적 HTML 속성:",
  "checkbox.uniform.indent": "<style> 및 <script> 태그 내에서 HTML 들여쓰기 사용",
  "hint.text.removed.namespace": "{1, choice, 0#네임스페이스|1#네임스페이스} {0} 제거됨",
  "border.title.xml": "XML",
  "configurable.name.html.css": "HTML/CSS",
  "xml.category": "XML",
  "ignore.ext.resource.preview": "{1}에서 {0}을(를) 무시된 리소스로 등록합니다.",
  "checkbox.enable.completion.html.auto.popup.code.completion.on.typing.in.text": "HTML 텍스트에 입력할 때 태그 이름 코드 자동 완성 팝업 활성화",
  "preserve": "유지",
  "remove.keep.with.tags": "제거(태그와 함께 유지)",
  "add.new.lines": "새 줄 추가"
}

file_path = "c:/Users/klanary/Desktop/vscode 모음/android_korean/androidstudio_koreanlanguagepack/missing_translations/missing_keys_korean.json"
with open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)

for item in data["new_files"]:
    if item["filename"] == "XmlBundle.properties":
        item["keys"].update(translated_keys)
        break

with open(file_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Batch 4 translated successfully.")