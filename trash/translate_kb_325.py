import json
import os

translated_keys = {
  "emmet.title": "Emmet",
  "emmet.configuration.title": "Emmet",
  "emmet.enable.label": "XML/HTML Emmet 활성화(&E)",
  "emmet.filters.enabled.by.default": "기본적으로 활성화된 필터",
  "emmet.enable.preview": "약어 미리보기 활성화(&A)",
  "emmet.expand.abbreviation.with": "다음으로 약어 확장(&A)",
  "emmet.href.autodetect": " <a> 태그로 텍스트를 감쌀 때 자동 URL 인식 활성화(&U)",
  "emmet.add.edit.point.at.the.end.of.template": "템플릿 끝에 편집 지점 추가(&P)",
  "emmet.bem.class.name.element.separator.label": "클래스 이름의 요소 구분 기호:",
  "emmet.bem.class.name.modifier.separator.label": "클래스 이름의 한정자 구분 기호:",
  "emmet.bem.short.element.prefix.label": "짧은 요소 접두사:",
  "emmet.context.help.tooltip": "Emmet 약어로 HTML 태그를 업데이트합니다.<br/>\\n값을 덮어쓰려면 .class[attribute]를 사용합니다.<br/>\\n값을 추가하려면 .+class[attribute]를 사용합니다.<br/>\\n값을 제거하려면 .-class[attribute]를 사용합니다.<br/>\\n<p/>\\n예를 들어, <code>.+c2[title=Hello]</code> 약어는<br/>\\n<code>\\\\&lt;div class=\"c1\"\\\\&gt;</code>를<br/>\\n<code>\\\\&lt;div class=\"c1 c2\" title=\"Hello\"\\\\&gt;</code>로 업데이트합니다.",
  "emmet.action.surround.error.hint": "현재 컨텍스트에서 Emmet을 사용하여 감싸기를 호출할 수 없습니다.",
  "emmet.filter.trim.line.markers": "줄 마커 자르기",
  "emmet.filter.BEM": "BEM",
  "emmet.filter.escape": "이스케이프",
  "emmet.filter.xsl.tuning": "XSL 튜닝",
  "html.action.new.file.dialog.title": "새 HTML 파일",
  "html.action.new.file.item.html5.file": "HTML 5 파일",
  "html.inspections.unknown.target": "링크에서 해결되지 않은 파일",
  "html.inspections.unknown.anchor": "링크에서 해결되지 않은 조각",
  "html.inspections.extra.closing.tag": "중복 닫는 태그",
  "html.inspections.unknown.tag": "알 수 없는 태그",
  "html.inspections.unknown.attribute": "알 수 없는 속성",
  "html.inspections.unknown.boolean.attribute": "잘못된 부울 속성",
  "html.inspections.missing.closing.tag": "누락된 닫는 태그",
  "html.inspections.wrong.attribute.value": "잘못된 속성 값",
  "html.inspections.group.name": "HTML",
  "html.inspections.group.name.accessibility": "접근성",
  "html.inspections.check.empty.tag": "빈 태그",
  "html.inspections.check.valid.script.tag": "'script' 태그 내용의 형식이 잘못되었습니다.",
  "html.related.linked.files.group": "연결된 파일",
  "html.quickdoc.additional.template": "자세한 내용은 <a href=\"{0}\">MDN 웹사이트</a>에서 확인하세요.",
  "web.editor.configuration.title": "HTML/CSS",
  "xml.action.unwrap.enclosing.tag.name.description": "감싸는 태그 제거: {0}",
  "xml.editor.options.misc.title": "XML/HTML",
  "xml.editor.options.css.title": "CSS",
  "xml.refactor.rename.current.tag": "{0}을(를) 다음으로 이름 변경:",
  "xml.external.resource.dialog.title": "외부 리소스",
  "xml.external.resource.label.uri": "URI:",
  "xml.external.resource.label.path": "경로:",
  "xml.external.resource.column.name.uri": "URI",
  "xml.external.resource.column.name.location": "위치",
  "xml.external.resource.display.name": "스키마 및 DTD",
  "xml.external.resource.label.external.resources": "외부 스키마 및 DTD(&E):",
  "xml.external.resource.label.ignored.resources": "무시된 스키마 및 DTD(&I):",
  "xml.external.resource.empty.text.no.external.resources": "외부 리소스가 없습니다.",
  "xml.external.resource.empty.text.no.ignored.resources": "무시된 리소스가 없습니다.",
  "xml.inspections.cannot.resolve.anchor": "앵커 #{0}을(를) 찾을 수 없습니다.",
  "xml.inspections.cannot.resolve.anchor.in.file": "{1} 파일의 앵커 #{0}을(를) 찾을 수 없습니다."
}

file_path = "c:/Users/klanary/Desktop/vscode 모음/android_korean/androidstudio_koreanlanguagepack/missing_translations/missing_keys_korean.json"
with open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)

file_found = False
for item in data["new_files"]:
    if item["filename"] == "XmlBundle.properties":
        item["keys"].update(translated_keys)
        file_found = True
        break

if not file_found:
    data["new_files"].append({
        "filename": "XmlBundle.properties",
        "keys": translated_keys
    })

with open(file_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Batch 1 translated successfully.")