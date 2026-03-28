import json

translations = {
  "predefined.configuration.type.text": "{0} 검색 템플릿",
  "predefined.configuration.type.text.user.defined": "{0} 검색 템플릿, 사용자 정의됨",
  "invalid.regular.expression": "잘못된 정규 표현식: {0}",
  "unlimited.placeholder": "무제한",
  "min.occurs.tooltip.message": "[{0},{1}]",
  "text.tooltip.message": "텍스트{0,choice,0#=|1#\\u2260}{1}{2,choice,0#|1#, 단어 단위}{3,choice,0#|1#, 계층 구조 내}",
  "hierarchy.tooltip.message": "계층 구조 내",
  "exprtype.tooltip.message": "유형{0,choice,0#=|1#\\u2260}{1}{2,choice,0#|1#, 계층 구조 내}",
  "script.tooltip.message": "스크립트",
  "reference.target.tooltip.message": "참조{0,choice,0#=|1#\\u2260}{1}",   
  "replacement.variable.is.not.defined.message": "알 수 없는 검색 변수 ''{0}''이(가) 있거나 바꾸기 변수 ''{0}''에 스크립트가 없습니다.",
  "replacement.variable.is.not.valid": "바꾸기 변수 ''{0}''에 스크립트 코드 문제가 있습니다. {1}",
  "replacement.template.is.not.expression.error.message": "표현식을 비표현식으로 바꿀 수 없습니다.",
  "replacement.not.supported.for.filetype": "{0} 파일 유형은 바꾸기가 지원되지 않습니다.",
  "search.template.is.not.expression.error.message": "비표현식을 표현식으로 바꿀 수 없습니다.",
  "modify.editor.content.command.name": "편집기 콘텐츠 수정",
  "option.is.not.recognized.error.message": "''{0}'' 제약 조건을 인식할 수 없습니다.",
  "error.only.one.target.allowed": "대상은 하나만 허용됩니다.",
  "error.condition.only.on.first.variable.reference": "제약 조건은 변수의 첫 번째 참조에서만 허용됩니다.",
  "error.two.different.type.constraints": "서로 다른 두 개의 유형 제약 조건",     
  "error.incorrect.regexp.constraint": "잘못된 정규식 제약 조건: {1}에 대한 {0}",
  "error.expected.character": "작은따옴표 뒤에 문자가 필요합니다.",
  "error.overflow": "값 오버플로",
  "error.expected.digit": "숫자가 필요합니다.",
  "error.expected.brace1": "숫자, '}' 또는 ','가 필요합니다.",
  "error.expected.brace2": "숫자 또는 '}'가 필요합니다.",
  "error.empty.quantifier": "빈 수량자",
  "error.expected.condition": "''{0}'' 뒤에 제약 조건이 필요합니다.",
  "error.expected.condition.name": "제약 조건 이름 누락",
  "error.expected.value": "''{0}''이(가) 필요합니다.",
  "error.unexpected.value": "예기치 않은 ''{0}''",
  "invalid.modifier.type": "잘못된 수정자 유형 {0}",
  "error.argument.expected": "''{0}'' 제약 조건에 인수가 필요합니다.",
  "error.cannot.invert": "''{0}'' 제약 조건을 반전할 수 없습니다.",
  "error.only.applicable.to.complete.match": "''{0}'' 제약 조건은 전체 일치에만 적용 가능합니다.",
  "error.bad.character.literal": "잘못된 문자 리터럴",
  "error.bad.literal": "잘못된 리터럴",
  "error.pattern.recursively.references.itself": "템플릿이 자신을 재귀적으로 참조합니다.",
  "error.configuration.0.not.found": "''{0}'' 템플릿을 찾을 수 없습니다.",
  "error.script.constraint.for.0.has.problem.1": "{0}의 스크립트 제약 조건에 {1} 문제가 있습니다.",
  "error.in.groovy.parser": "Groovy 파서 오류",
  "SSRInspection.family.name": "구조적으로 바꾸기",
  "SSRInspection.display.name": "구조적 검색 검사",
  "SSRInspection.add.search.template.button": "구조적 검색 검사 추가\\u2026",
  "SSRInspection.add.replace.template.button": "구조적 바꾸기 검사 추가\\u2026",
  "overwrite.message": "이름이 같은 템플릿이 이미 있습니다. 바꾸면 현재 내용을 덮어씁니다.",
  "overwrite.title": "\"{0}\"이(가) 있습니다. 바꾸시겠습니까?",
  "template.in.use.message": "''{0}'' 템플릿은 ''{1}'' 템플릿에서 사용합니다. 정말 삭제하시겠습니까?",
  "ssr.will.not.find.anything": "지정된 템플릿이 ''{0}'' 범위의 항목과 일치하는 항목이 없습니다.",
  "inspection.script.problem": "구조적 검색 검사 템플릿 ''{1}''의 {0}\\n"
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
