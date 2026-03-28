import json

ko_dict = {
  "action.CIDR.Lang.DumpSymbolStats.text": "일반 심볼 통계 덤프",
  "action.CIDR.Lang.CompactSymbols.text": "심볼 업데이트/압축",
  "action.CIDR.Lang.ImportsHierarchy.text": "가져오기 계층 구조",
  "action.CIDR.Lang.ObjC.GenerateSharedInstance.text": "+sharedInstance",
  "action.CIDR.Lang.ObjC.GenerateSharedInstance.description": "공유된 인스턴스 생성",
  "action.CIDR.Lang.ObjC.GenerateDescription.text": "-description\\u2026",
  "action.CIDR.Lang.ObjC.GenerateDescription.description": "클래스 멤버에서 -description 생성",
  "action.CIDR.Lang.ObjC.GenerateIsEqualAndHash.text": "-isEqual: 및 -hash\\u2026",
  "action.CIDR.Lang.ObjC.GenerateIsEqualAndHash.description": "클래스 멤버에서 -isEqual: 및 -hash 생성",
  "action.CIDR.Lang.ObjC.GenerateCopy.text": "-copyWithZone:\\u2026",
  "action.CIDR.Lang.ObjC.GenerateCopy.description": "클래스 멤버에서 -copyWithZone: 생성",
  "action.CIDR.Lang.ObjC.GenerateEncode.text": "-init/encodeWithCoder:\\u2026",
  "action.CIDR.Lang.ObjC.GenerateEncode.description": "클래스 멤버에서 -encodeWithCoder: 및 initWithCoder: 생성",
  "action.CIDR.Lang.ObjC.GenerateInitWith.text": "-initWith\\u2026",
  "action.CIDR.Lang.ObjC.GenerateInitWith.description": "클래스 멤버에서 -initWith... 생성",
  "action.CIDR.Lang.Cpp.GenerateDefinitions.text": "정의 생성\\u2026",
  "action.CIDR.Lang.Cpp.GenerateDefinitions.description": "정의 생성",
  "action.CIDR.Lang.Cpp.GenerateStreamOutputOperator.text": "스트림 출력 연산자",
  "action.CIDR.Lang.Cpp.GenerateStreamOutputOperator.description": "스트림 출력 연산자 생성",
  "action.CIDR.Lang.Cpp.GenerateRelationalOperators.text": "관계 연산자",
  "action.CIDR.Lang.Cpp.GenerateRelationalOperators.description": "관계 연산자 생성",
  "action.CIDR.Lang.Cpp.GenerateEqualityOperators.text": "동등 연산자",
  "action.CIDR.Lang.Cpp.GenerateEqualityOperators.description": "동등 연산자 생성",
  "action.CIDR.Lang.Cpp.GenerateGetterAndSetter.text": "Getter 및 Setter",
  "action.CIDR.Lang.Cpp.GenerateGetterAndSetter.description": "필드의 Getter 및 Setter 함수 생성",
  "action.CIDR.Lang.Cpp.GenerateSetter.text": "Setter",
  "action.CIDR.Lang.Cpp.GenerateSetter.description": "필드의 Setter 함수 생성",
  "action.CIDR.Lang.Cpp.GenerateGetter.text": "Getter",
  "action.CIDR.Lang.Cpp.GenerateGetter.description": "필드의 Getter 함수 생성",
  "action.CIDR.Lang.Cpp.GenerateDestructor.text": "소멸자",
  "action.CIDR.Lang.Cpp.GenerateDestructor.description": "소멸자 생성",
  "action.CIDR.Lang.Cpp.GenerateConstructor.text": "생성자",
  "action.CIDR.Lang.Cpp.GenerateConstructor.description": "클래스 멤버에서 생성자 생성",
  "action.CIDR.Lang.ObjC.Synthesize.text": "@synthesize\\u2026",
  "action.CIDR.Lang.ObjC.Synthesize.description": "Synthesize 및 인스턴스 변수 생성(선택 사항)",
  "action.CIDR.Lang.ObjC.DeclareMembers.text": "멤버 선언\\u2026",
  "action.CIDR.Lang.ObjC.DeclareMembers.description": "인터페이스 또는 전용 카테고리에 클래스 멤버 선언",
  "action.CIDR.Lang.ObjC.ConvertToIvar.text": "인스턴스 변수로 변환\\u2026",
  "action.CIDR.Lang.ObjC.ConvertToIvar.description": "프로퍼티를 인스턴스 변수로 변환",
  "action.CIDR.Lang.ObjC.ConvertToProperty.text": "프로퍼티로 변환\\u2026",
  "action.CIDR.Lang.ObjC.ConvertToProperty.description": "인스턴스 변수를 프로퍼티로 변환",
  "action.CIDR.Lang.ObjC.ConvertToBlock.text": "블록으로 변환\\u2026",
  "action.CIDR.Lang.ObjC.ConvertToBlock.description": "블록으로 변환",
  "action.CIDR.Lang.ObjC.ConvertToFunction.text": "함수로 변환\\u2026",
  "action.CIDR.Lang.ObjC.ConvertToFunction.description": "함수로 변환",
  "action.CIDR.Lang.ObjC.ConvertToMethod.text": "메서드로 변환\\u2026",
  "action.CIDR.Lang.ObjC.ConvertToMethod.description": "메서드로 변환",
  "action.CIDR.Lang.ObjC.ExtractCategory.text": "카테고리\\u2026",
  "action.CIDR.Lang.ObjC.ExtractCategory.description": "새로운 카테고리로 멤버 추출",
  "action.CIDR.Lang.ObjC.ExtractProtocol.text": "프로토콜\\u2026"
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
