import json

translations = {
  "add.filter.title": "수정자 추가",
  "add.filter.label": "수정자 추가",
  "add.script.label": "스크립트 추가",
  "count.label": "개수={0}",
  "default.label": "\\u00A0기본값",
  "max.label": "최대=",
  "min.label": "최소=",
  "reference.label": "참조=",
  "reference.0.label": "참조={0}",
  "script.label": "스크립트=",
  "script.0.label": "스크립트={0}",
  "text.label": "텍스트=",
  "text.0.label": "텍스트={0}",
  "type.label": "유형=",
  "type.0.label": "유형={0}",
  "context.label": "컨텍스트=",
  "context.0.label": "컨텍스트={0}",
  "within.hierarchy.label": ", 계층 구조 내",
  "whole.words.label": ", 단어 단위",
  "within.type.hierarchy.check.box": "유형 계층 구조 내",
  "regex.check.box": "정규 표현식",
  "no.filters.whole.template.label": "전체 템플릿에 추가된\\n수정자가 없음",
  "no.filters.for.0.label": "${0}$에 추가된\\n수정자가 없음",
  "no.script.for.0.label": "${0}$에 추가된\\n스크립트가 없음",
  "filters.for.whole.template.title": "전체 템플릿의 수정자:",      
  "filters.for.0.title": "${0}$의 수정자:",
  "type.filter.help.text": "<p>일치하는 표현식의 유형을 제공된 \"|\"로 구분된 패턴과 대조하여 확인합니다. <p>패턴을 반전하려면 \"!\"를 사용하세요.",
  "text.filter.help.text": "<p>일치하는 텍스트를 제공된 패턴과 대조하여 확인합니다. <p>패턴을 반전하려면 \"!\"를 사용하세요. <p>정규 표현식이 지원됩니다.",
  "script.filter.match.variable.help.text": "<p>GroovyScript IntelliJ API를 사용하여 검색 결과를 수정합니다. \n  지정된 스크립트가 <code>false</code>를 반환하면 찾은 요소가 검색 결과에 포함되지 않습니다. \n  비불리언 스크립트 결과는 불리언으로 변환됩니다. <p>사용 가능한 변수: {0}",       
  "script.filter.replacement.variable.help.text": "<p>고급 이름 바꾸기, 다시 쓰기 또는 리팩터링을 위해 \n  GroovyScript Intellij API를 사용하여 사용자 지정 바꾸기를 만듭니다. 바꿀 때 바꾸기 템플릿의 변수가 지정된 스크립트의 String 결과로 바뀝니다. \n  <p>사용 가능한 변수: {0}",
  "reference.filter.help.text": "<p>참조된 요소를 제공된 템플릿과 대조하여 확인합니다.",
  "invert.filter": "수정자 반전",
  "structural.replace.title": "구조적 바꾸기",
  "shorten.fully.qualified.names.checkbox": "정규화된 이름 줄이기(&Q)",   
  "replacement.template.label": "템플릿 바꾸기:",
  "preview.replacement.button": "바꾸기 미리보기(&P)",
  "do.replace.all.button": "모두 바꾸기(&A)",
  "replace.selected.button": "선택 항목 바꾸기(&R)",
  "draft.template.node": "초안 템플릿",
  "expressions.category": "Java/표현식",
  "recent.category": "최근",
  "user.defined.category": "저장된 템플릿",
  "project.templates.category": "프로젝트 템플릿",
  "xml_html.category": "XML//HTML",
  "generics.category": "Java/제네릭",
  "misc.category": "Java/기타",
  "metadata.category": "Java/주석, Javadoc 및 메타데이터",
  "class.category": "Java/클래스 기반",
  "operators.category": "Java/연산자",
  "j2ee.category": "Java/Java EE"
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
