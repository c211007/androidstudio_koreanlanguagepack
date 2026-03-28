import json
import os

translated_keys = {
  "html.inspections.extra.closing.tag.for.empty.element": "빈 요소에 대한 닫는 태그가 중복됩니다.",
  "html.inspections.element.missing.end.tag": "\\\\&lt;#ref\\\\&gt; 요소에 끝 태그가 없습니다.",
  "html.inspections.attribute.is.not.boolean": "{0} 속성은 부울(boolean)이 아닙니다.",
  "html.inspections.check.empty.script.message": "빈 태그는 일부 브라우저에서 작동하지 않습니다.",
  "html.inspections.check.empty.script.tag.fix.message": "태그 확장",
  "html.inspections.unknown.tag.attribute.checkbox.title": "사용자 지정 HTML 태그 속성:",
  "html.inspections.unknown.tag.boolean.attribute.checkbox.title": "사용자 지정 HTML 부울 태그 속성:",
  "html.inspections.unknown.tag.checkbox.title": "사용자 지정 HTML 태그:",
  "html.quickfix.family": "HTML 수정",
  "html.quickfix.switch.to.html5": "HTML5 언어 수준으로 전환",
  "html.quickfix.rename.attribute.family": "속성 이름 변경",
  "html.quickfix.rename.attribute.text": "속성 이름을 {0}(으)로 변경",
  "html.quickfix.add.closing.tag": "닫는 태그 추가",
  "html.quickfix.add.custom.html.attribute": "사용자 지정 HTML 속성에 {0} 추가",
  "html.quickfix.add.custom.html.boolean.attribute": "사용자 지정 HTML 부울 속성에 {0} 추가",
  "html.quickfix.add.custom.html.tag": "사용자 지정 HTML 태그에 {0} 추가",
  "html.quickfix.add.named.closing.tag": "</{0}> 추가",
  "html.quickfix.add.optional.html.attribute": "필수 아님 HTML 속성에 {0} 추가",
  "xml.dtd.create.entity.intention.name": "{0} 엔티티 선언 생성",
  "xml.dtd.create.dtd.element.intention.name": "{0} 요소 선언 생성",
  "xml.inspections.element.is.not.allowed.here": "여기에 {0} 요소가 허용되지 않습니다.",
  "xml.inspections.element.must.be.declared": "{0} 요소를 선언해야 합니다.",
  "xml.inspections.duplicate.attribute": "중복 속성 {0}",
  "xml.inspections.attribute.is.not.allowed.here": "여기에 {0} 속성이 허용되지 않습니다.",
  "xml.inspections.attribute.should.be.preceded.with.space": "속성과 이전 속성 사이에 공백이 있어야 합니다.",
  "xml.inspections.cdata.end.should.not.appear.in.content": "CDATA 섹션의 끝을 표시하는 데 사용되지 않는 한 콘텐츠에 문자 시퀀스 ']]>'가 나타나서는 안 됩니다.",
  "xml.inspections.xml.declaration.should.precede.all.document.content": "XML 선언은 모든 문서 콘텐츠보다 앞에 와야 합니다.",
  "xml.inspections.duplicate.id.reference": "중복 ID 참조",
  "xml.inspections.element.doesnt.have.required.attribute": "{0} 요소에 필수 속성 {1}이(가) 없습니다.",
  "xml.inspections.invalid.id.reference": "잘못된 ID 참조",
  "xml.inspections.redundant.default.attribute.value.assignment": "중복된 기본 속성 값 할당",
  "xml.inspections.tag.has.wrong.closing.tag.name": "시작 태그에 잘못된 닫는 태그가 있습니다.",
  "xml.inspections.tag.should.have.one.of.following.attributes.0": "태그에는 다음 속성 중 하나가 있어야 합니다: {0}",
  "xml.inspections.the.attribute.is.marked.as.deprecated": "해당 속성은 사용 중단(deprecated)으로 표시되었습니다.",
  "xml.inspections.the.tag.is.marked.as.deprecated": "해당 태그는 사용 중단(deprecated)으로 표시되었습니다.",
  "xml.inspections.unbound.namespace": "''{0}'' 네임스페이스가 바운드되지 않았습니다.",
  "xml.inspections.unbound.namespace.no.param": "네임스페이스가 바운드되지 않았습니다.",
  "xml.inspections.unescaped.xml.character": "이스케이프되지 않은 XML 문자",
  "xml.inspections.unknown.html.tag": "알 수 없는 HTML 태그 {0}",
  "xml.inspections.wrong.closing.tag.name": "잘못된 닫는 태그 이름",
  "xml.inspections.wrong.root.element": "잘못된 루트 요소",
  "xml.inspections.tag.empty.body": "XML 태그의 본문이 비어 있습니다.",
  "xml.inspections.unused.schema.declaration": "네임스페이스 선언이 사용되지 않습니다.",
  "xml.inspections.unused.schema.location": "네임스페이스 위치가 사용되지 않습니다.",
  "xml.inspections.attribute.unused": "''{0}'' 속성이 사용되지 않습니다.",
  "xml.inspections.attribute.unused.because.other.attribute.present": "''{1}'' 속성이 있으므로 ''{0}'' 속성은 사용되지 않습니다.",
  "xml.inspections.all.attributes.unused.because.an.attribute.present": "{0} 속성이 있으므로 해당 속성은 사용되지 않습니다.",
  "xml.intention.rename.end.tag": "끝 태그 ''{0}''을(를) ''{1}''(으)로 이름 변경",
  "xml.intention.rename.start.tag": "시작 태그 ''{0}''을(를) ''{1}''(으)로 이름 변경",
  "xml.intention.replace.tag.empty.body.with.empty.end": "빈 태그 축소"
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

print("Batch 1 translated successfully.")