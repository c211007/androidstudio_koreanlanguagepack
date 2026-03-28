import json

ko_dict = {
  "symbol.kind.name.lowercase.enum.constant": "열거형 상수",
  "symbol.kind.name.lowercase.field": "필드",
  "symbol.kind.name.lowercase.function": "함수",
  "symbol.kind.name.lowercase.constructor": "생성자",
  "symbol.kind.name.lowercase.parameter": "매개변수",
  "symbol.kind.name.lowercase.global.variable": "전역 변수",
  "symbol.kind.name.lowercase.built.in.symbol": "기본 제공 심볼",
  "symbol.kind.name.lowercase.local.variable": "로컬 변수",
  "symbol.kind.name.lowercase.exception.variable": "예외 변수",
  "symbol.kind.name.lowercase.implementation": "구현",
  "symbol.kind.name.lowercase.instance.variable": "인스턴스 변수",
  "symbol.kind.name.lowercase.interface": "인터페이스",
  "symbol.kind.name.lowercase.label": "레이블",
  "symbol.kind.name.lowercase.macro": "매크로",
  "symbol.kind.name.lowercase.macro.parameter": "매크로 매개변수",
  "symbol.kind.name.lowercase.import": "가져오기",
  "symbol.kind.name.lowercase.compatibility.alias": "호환성 별칭",
  "symbol.kind.name.lowercase.method1": "메서드",
  "symbol.kind.name.lowercase.block": "블록",
  "symbol.kind.name.lowercase.lambda": "람다",
  "symbol.kind.name.lowercase.property": "프로퍼티",
  "symbol.kind.name.lowercase.synthesize.statement": "synthesize 구문",
  "symbol.kind.name.lowercase.protocol": "프로토콜",
  "symbol.kind.name.lowercase.struct": "구조체",
  "symbol.kind.name.lowercase.union": "공용체",
  "symbol.kind.name.lowercase.enum": "열거형",
  "symbol.kind.name.lowercase.namespace": "네임스페이스",
  "symbol.kind.name.lowercase.type.parameter": "타입 매개변수",
  "symbol.kind.name.lowercase.template.parameter": "템플릿 매개변수",
  "symbol.kind.name.lowercase.using": "using",
  "symbol.kind.name.lowercase.localized.string": "현지화된 문자열",
  "symbol.kind.name.lowercase.expression": "표현식",
  "symbol.kind.name.lowercase.generic.parameter": "제네릭 매개변수",
  "symbol.kind.name.lowercase.concept": "개념",
  "symbol.kind.name.lowercase.keyword": "키워드",
  "symbol.kind.name.lowercase.file": "파일",
  "symbol.kind.name.lowercase.folder": "폴더",
  "symbol.kind.name.lowercase.default": "심볼",
  "command.name.codestylesettings.extractor": "코드 스타일 설정 추출기",
  "symbol.kind.name.uppercase.destructor": "소멸자",
  "symbol.kind.name.uppercase.class": "클래스",
  "symbol.kind.name.lowercase.destructor": "소멸자",
  "symbol.kind.name.lowercase.class": "클래스",
  "popup.title.element.found.singular": "{0} ({1}개의 요소 발견됨)",
  "popup.title.elements.found.plural": "{0} ({1}개의 요소 발견됨)",
  "popup.title.element.found.so.far.singular": "{0} (지금까지 {1}개의 요소 발견됨)",
  "popup.title.elements.found.so.far.plural": "{0} (지금까지 {1}개의 요소 발견됨)",
  "resource.language.unknown": "알 수 없음",
  "cache.downloader.updating.progress.title": "캐시 업데이트",
  "icon.tooltip.const.decl": "상수 {0}"
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
