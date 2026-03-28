import json

ko_dict = {
  "dialog.message.all.members.are.defined": "모두 정의됨",
  "tab.title.existing": "기존",
  "label.copy.depth": "깊이",
  "copy.depths.option.deep": "깊은",
  "copy.depths.option.shallow": "얕은",
  "button.generate": "생성",
  "other.categories.and.inherited.members": "기타 카테고리 및 상속된 멤버",
  "action.show.inherited.text": "상속된 항목 표시",
  "action.show.inherited.members.members.in.other.categories.description": "기타 카테고리의 상속된 멤버와 멤버 표시",
  "polymorphic.call": "(다형성 호출)",
  "symbol.kind.name.uppercase.type": "타입",
  "symbol.kind.name.uppercase.enum.constant": "열거형 상수",
  "symbol.kind.name.uppercase.field": "필드",
  "symbol.kind.name.uppercase.function": "함수",
  "symbol.kind.name.uppercase.constructor": "생성자",
  "symbol.kind.name.uppercase.parameter": "매개변수",
  "symbol.kind.name.uppercase.global.variable": "전역 변수",
  "symbol.kind.name.uppercase.built.in.symbol": "기본 제공 심볼",
  "symbol.kind.name.uppercase.local.variable": "로컬 변수",
  "symbol.kind.name.uppercase.exception.variable": "예외 변수",
  "symbol.kind.name.uppercase.implementation": "구현",
  "symbol.kind.name.uppercase.instance.variable": "인스턴스 변수",
  "symbol.kind.name.uppercase.interface": "인터페이스",
  "symbol.kind.name.uppercase.label": "레이블",
  "symbol.kind.name.uppercase.macro": "매크로",
  "symbol.kind.name.uppercase.macro.parameter": "매크로 매개변수",
  "symbol.kind.name.uppercase.import": "가져오기",
  "symbol.kind.name.uppercase.compatibility.alias": "호환성 별칭",
  "symbol.kind.name.uppercase.method1": "메서드",
  "symbol.kind.name.uppercase.block": "블록",
  "symbol.kind.name.uppercase.lambda": "람다",
  "symbol.kind.name.uppercase.property": "프로퍼티",
  "symbol.kind.name.uppercase.synthesize.statement": "Synthesize 구문",
  "symbol.kind.name.uppercase.protocol": "프로토콜",
  "symbol.kind.name.uppercase.struct": "구조체",
  "symbol.kind.name.uppercase.union": "공용체",
  "symbol.kind.name.uppercase.enum": "열거형",
  "symbol.kind.name.uppercase.namespace": "네임스페이스",
  "symbol.kind.name.uppercase.type.parameter": "타입 매개변수",
  "symbol.kind.name.uppercase.template.parameter": "템플릿 매개변수",
  "symbol.kind.name.uppercase.using": "Using",
  "symbol.kind.name.uppercase.localized.string": "현지화된 문자열",
  "symbol.kind.name.uppercase.expression": "표현식",
  "symbol.kind.name.uppercase.generic.parameter": "제네릭 매개변수",
  "symbol.kind.name.uppercase.concept": "개념",
  "symbol.kind.name.uppercase.keyword": "키워드",
  "symbol.kind.name.uppercase.file": "파일",
  "symbol.kind.name.uppercase.folder": "폴더",
  "symbol.kind.name.uppercase.default": "심볼",
  "symbol.kind.name.lowercase.type": "타입"
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
