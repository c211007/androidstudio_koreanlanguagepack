import json

translations = {
  "structural.replace.preview.dialog.title": "구조적 바꾸기 미리보기",      
  "replace.preview.oktext": "바꾸기(&R)",
  "replacement.code": "바꾸기 코드",
  "structural.search.title": "구조적 검색",
  "search.template": "검색 템플릿:",
  "template.name.label": "템플릿 이름:",
  "save.template.description.button": "현재 템플릿 저장",
  "save.template.title": "현재 템플릿 저장",
  "checkbox.save.in.project": "프로젝트에 저장(VCS를 통해 공유 가능)",     
  "save.template": "템플릿 저장(&A)\\u2026",
  "save.inspection.action.text": "템플릿을 검사로 저장\\u2026",
  "save.template.action.text": "IDE 또는 프로젝트에 템플릿 저장\\u2026",        
  "create.inspection.from.template.action.text": "템플릿에서 검사 만들기\\u2026",
  "remove.template": "저장된 템플릿 삭제",
  "new.template.defaultname": "이름 없음",
  "search.in.injected.checkbox": "주입된 코드(&J)",
  "reformat.checkbox": "서식 다시 지정(&R)",
  "use.static.import.checkbox": "정적 가져오기 사용(&I)",
  "search.target.label": "대상(&T):",
  "filter.button": "수정자 패널 전환",
  "filter.button.description": "변수 수정자 패널을 전환합니다.",
  "templates.button": "기존 템플릿 패널 전환",
  "templates.button.description": "기존 템플릿 패널을 전환합니다.",        
  "pin.button": "검색 후 대화상자 열어 두기",
  "pin.button.description": "검색 후 대화상자를 열어 둡니다.",
  "open.in.new.tab.checkbox": "새 탭에서 결과 열기(&B)",
  "search.dialog.file.type.label": "언어(&L):",
  "import.template.action": "클립보드에서 템플릿 가져오기",
  "export.template.action": "클립보드에 템플릿 내보내기",
  "no.template.found.warning": "클립보드에서 템플릿을 찾을 수 없습니다.",
  "import.template.script.warning.title": "경고: 템플릿에 스크립트가 포함되어 있습니다.", 
  "import.template.script.corrupted": "클립보드에서 손상된 템플릿을 찾았습니다.",
  "import.template.script.warning": "가져온 템플릿에 {1,choice,1#새로운 Groovy 스크립트 수정자가|1<{1}개의 Groovy 스크립트 수정자가} 포함되어 있으며 모든 스크립트는 내부 {0} 전체에 액세스할 수 있습니다. 스크립트가 손상을 유발하지 않는지 확인한 후 이 템플릿을 사용하세요.",
  "switch.to.search.action": "검색으로 전환",
  "switch.to.replace.action": "바꾸기로 전환",
  "looking.in.progress.message": "{0}에서 검색 중",
  "found.progress.message": "항목 {0}개 일치",
  "occurrences.of": "''{0}'' 템플릿과 일치하는 프래그먼트",
  "occurrences.of.0.in.1": "{1} 내의 ''{0}'' 템플릿",
  "replace.occurrences.of.0.with.1.in.2": "{2}의 ''{0}''을(를) ''{1}''(으)로 바꿈",
  "found.occurrences": "{0}에서 일치 항목 찾음",
  "targets.node.text": "구조적 검색 템플릿",
  "this.pattern.is.malformed.message": "지정된 템플릿의 형식이 잘못되었습니다.",   
  "incorrect.pattern.message": "잘못된 템플릿",
  "count.filter.name": "개수",
  "reference.filter.name": "참조",
  "script.filter.name": "스크립트",
  "text.filter.name": "텍스트",
  "type.filter.name": "유형",
  "context.filter.name": "컨텍스트"
}

with open("missing_translations/missing_keys_korean.json", "r", encoding="utf-8") as f:
    data = json.load(f)

found = False
for file_info in data.get("new_files", []):
    if file_info.get("filename") == "SSRBundle.properties":
        keys_dict = file_info.get("keys", file_info.get("properties", {}))
        keys_dict.update(translations)
        file_info["keys"] = keys_dict
        found = True
        break

if not found:
    data.setdefault("new_files", []).append({
        "filename": "SSRBundle.properties",
        "keys": translations
    })

with open("missing_translations/missing_keys_korean.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)
