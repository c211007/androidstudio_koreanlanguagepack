import json

translations = {
  "search.template.problem": "구조적 검색: {0}",
  "search.script.problem": "구조적 검색 스크립트에서 예외가 발생했습니다: {0}",  
  "complete.match.variable.name": "전체 일치",
  "template.in.use.title": "''{0}'' 템플릿이 이미 사용 중",
  "user.defined.group.name": "사용자 정의",
  "structural.search.group.name": "구조적 검색",
  "edit.metadata.button": "메타데이터 수정\\u2026",
  "add.pattern.action": "템플릿 추가",
  "templates.title": "템플릿:",
  "meta.data.dialog.title": "구조적 검색 검사",
  "inspection.name.label": "검사 이름:",
  "problem.descriptor.label": "문제 툴팁(매크로 #ref를 사용하여 강조표시된 코드 삽입):",
  "description.label": "설명:",
  "suppress.id.label": "ID 표시 안함:",
  "no.description.message": "설명이 제공되지 않음",
  "name.must.not.be.empty.warning": "이름은 비워 둘 수 없습니다.",
  "inspection.with.name.exists.warning": "이름이 ''{0}''인 검사가 이미 존재합니다.",
  "suppress.id.must.match.regex.warning": "표시 안함 ID는 정규표현식 [a-zA-Z_0-9.-]+와 일치해야 합니다.",
  "suppress.id.in.use.warning": "표시 안함 ID ''{0}''은(는) 이미 다른 검사에서 사용 중입니다.",
  "button.replace": "바꾸기",
  "popup.content.directory": "디렉터리가 아님",
  "command.name.adjust.line.indent": "줄 들여쓰기 조정",
  "command.name.live.search.template.builder": "라이브 검색 템플릿 빌더",  
  "tooltip.preconfigured.search.patterns": "<p>사전 구성된 검색 템플릿은 {0}(으)로 자동 완성할 수 있습니다.<p>제공된 템플릿은 대상 템플릿의 컨텍스트를 제한하는 데 사용됩니다.",
  "status.bar.text.results.found.in.current.file": "현재 파일에서 {0}개 결과를 찾았습니다.",
  "predefined.template.xml.tag": "XML 태그",
  "predefined.template.xml.attribute": "XML 속성",
  "predefined.template.html.attribute": "HTML 속성",
  "predefined.template.xml.attribute.value": "XML 속성 값",
  "predefined.template.html.attribute.value": "HTML 속성 값",
  "predefined.template.xml.html.tag.value": "XML/HTML 태그 값",
  "predefined.template.ul.or.ol": "<ul> 또는 <ol>",
  "predefined.template.li.not.contained.in.ul.or.ol": "<li>가 <ul> 또는 <ol>에 포함되지 않음",
  "predefined.template.xml.tag.without.specific.attribute": "특정 속성이 없는 XML 태그",
  "pattern.context.class.member": "클래스 멤버",
  "pattern.context.default": "기본값",
  "file.type.pattern.context": "{0} - {1}",
  "replace.configuration.display.text": "{0} \\u21E8 {1}",
  "inspection.tree.create.inspection.search.template": "구조적 검색 템플릿을 사용하여\\u2026",
  "inspection.tree.create.inspection.replace.template": "구조적 바꾸기 템플릿을 사용하여\\u2026",
  "inspection.tree.group.description": "도구 모음에서 + 버튼을 사용하여 새 구조적 검색 검사를 만듭니다.<br>\n구조적 검색 검사는 지정된 검색 템플릿과 일치하는 코드 스니펫을 강조표시합니다. 바꾸기 템플릿을 추가하여 빠른 수정을 제공할 수 있습니다.<br><br>\n<a href=\"action://ssr.profile.action.provider.add.group\">사용자 지정 구조적 검색 검사 추가\\u2026</a>"      
}

with open("missing_translations/missing_keys_korean.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for file_info in data.get("new_files", []):
    if file_info.get("filename") == "SSRBundle.properties":
        keys_dict = file_info.get("keys", file_info.get("properties", {}))
        keys_dict.update(translations)
        file_info["keys"] = keys_dict
        break

with open("missing_translations/missing_keys_korean.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)
