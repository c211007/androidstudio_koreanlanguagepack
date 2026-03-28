import json

ko_dict = {
  "qdoc.padding": "패딩",
  "qdoc.value": "값",
  "qdoc.value.range": "값 범위",
  "qdoc.possible.values": "가능한 값",
  "qdoc.byte.0": "{0, choice, 1#바이트|2#바이트}",
  "qdoc.copy": "복사",
  "qdoc.move": "이동",
  "qdoc.construction": "생성",
  "qdoc.assignment": "할당",
  "qdoc.on.cppreference": "cppreference.com의 \"{0}\"",
  "formatter.item.allman.braces": "Allman 중괄호",
  "formatter.item.kr.braces": "K&R 중괄호",
  "formatter.item.whitesmiths.braces": "Whitesmiths 중괄호",
  "formatter.item.stroustrup.braces": "Stroustrup",
  "formatter.title.code.generation": "코드 생성",
  "settings.title.objective.c.class.order": "Objective-C 클래스 순서",
  "settings.prefix.must.start.with.letter.or.symbol": "접두사는 문자 또는 '_' 기호로 시작해야 합니다.",
  "settings.hint.choice.prefix.suffix.must.contain.only.letters.or.digits.or.symbols": "{0, choice, 0#접두사|1#접미사}는 문자나 숫자 또는 ''_'' 기호만 포함해야 합니다.",
  "settings.title.naming.convention": "명명 규칙",
  "settings.naming.convention": "명명 규칙",
  "resolve.contexts.all.contexts": "모든 프로젝트 컨텍스트가 나열되었습니다.",
  "resolve.contexts.available": "사용 가능한 확인 컨텍스트",
  "resolve.contexts.current.file": "현재 {0} 파일은 ''{1}''의 컨텍스트에서 확인됩니다.",
  "resolve.contexts.file.resolved.in": "선택한 컨텍스트에서 파일이 확인됩니다.",
  "resolve.contexts.create.json.hint": "현재 빌드 시스템은 지원되지 않습니다. ‘c_cpp_properties.json’에서 종속 요소를 설정하거나 CMake를 구성하세요.",
  "resolve.contexts.loading": "확인 컨텍스트 로드 중\\u2026",
  "resolve.contexts.name": "확인 컨텍스트",
  "resolve.contexts.no.context": "<컨텍스트 없음>",
  "resolve.contexts.prefix.no.context": "현재 파일의 확인 컨텍스트가 없습니다.",
  "resolve.contexts.prefix.unsupported.build.system.context": "현재 빌드 시스템은 지원되지 않습니다. ''{0}''의 종속 요소를 통해 코드가 확인됩니다.",
  "resolve.contexts.unsupported.build.system.no.json.context": "없음",
  "resolve.contexts.prefix.unsupported.build.system.no.json.context": "현재 빌드 시스템은 지원되지 않습니다. ‘c_cpp_properties.json’에서 종속 요소를 설정하거나 CMake를 구성하세요.",
  "resolve.contexts.prefix": "컨텍스트",
  "resolve.contexts.unindexed.contexts": "색인이 생성되지 않은 컨텍스트",
  "hmap.description": "{0} 헤더 맵",
  "search.scope.project.source.files": "프로젝트 소스 파일",
  "search.scope.project.non.source.files": "프로젝트 비소스 파일",
  "header.search.root.custom.headers": "사용자 지정 헤더",
  "header.search.root.frameworks": "프레임워크",
  "header.search.root.explicit.frameworks": "명시적 프레임워크",
  "find.usages.unknown.type": "알 수 없음",
  "switch.header.source.separator.headers": "헤더",
  "switch.header.source.separator.sources": "소스",
  "new.definition.dialog.title.create.new.constructor": "새 생성자 만들기",
  "new.definition.dialog.title.create.new.function": "새 함수 생성",
  "new.definition.button.create": "생성",
  "new.definition.dialog.title.create.new.method": "새 메서드 생성",
  "action.context.file.name": "''{0}'' 파일",
  "oc.declare.members.implementation.undeclared": "구현(선언되지 않음)",
  "dialog.message.some.members.are.defined": "일부 멤버가 정의됨"
}

with open("missing_translations/missing_keys_korean.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for item in data.get("new_files", []):
    if item["filename"] == "OCBundle.properties":
        item["keys"].update(ko_dict)
        print("Updated OCBundle.properties")
        break

with open("missing_translations/missing_keys_korean.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
