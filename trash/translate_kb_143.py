import json

ko_dict = {
  "action.CIDR.Lang.ObjC.ExtractProtocol.description": "새로운 프로토콜로 멤버 추출",
  "action.CIDR.Lang.ObjC.ExtractSubclass.text": "하위 클래스\\u2026",
  "action.CIDR.Lang.ObjC.ExtractSubclass.description": "새로운 하위 클래스로 멤버 추출",
  "action.CIDR.Lang.ObjC.ExtractBlock.text": "블록 매개변수\\u2026",
  "action.CIDR.Lang.ObjC.ExtractBlock.description": "블록 매개변수 추출",
  "action.CIDR.Lang.Cpp.ExtractLambda.text": "람다 매개변수\\u2026",
  "action.CIDR.Lang.Cpp.ExtractLambda.description": "람다 매개변수 추출",
  "action.CIDR.Lang.IntroduceTypedef.text": "Typedef\\u2026",
  "action.CIDR.Lang.IntroduceTypedef.description": "Typedef 도입",
  "action.CIDR.Lang.IntroduceDefine.text": "정의\\u2026",
  "action.CIDR.Lang.IntroduceDefine.description": "정의 도입",
  "action.CIDR.Lang.IntroduceParameter.text": "매개변수\\u2026",
  "action.CIDR.Lang.IntroduceParameter.description": "매개변수 도입",
  "action.CIDR.Lang.ObjC.IntroduceProperty.text": "프로퍼티\\u2026",
  "action.CIDR.Lang.ObjC.IntroduceProperty.description": "프로퍼티 도입",
  "action.CIDR.Lang.ObjC.IntroduceIvar.text": "인스턴스 변수\\u2026",
  "action.CIDR.Lang.ObjC.IntroduceIvar.description": "인스턴스 변수 도입",
  "action.CIDR.Lang.IntroduceConstant.text": "상수\\u2026",
  "action.CIDR.Lang.IntroduceConstant.description": "상수 도입",
  "action.CIDR.Lang.IntroduceVariable.text": "변수\\u2026",
  "action.CIDR.Lang.IntroduceVariable.description": "변수 도입",
  "action.CIDR.Lang.SwitchHeaderSourceDebug.text": "디버그 헤더/소스",
  "action.CIDR.Lang.SwitchHeaderSource.text": "헤더/소스",
  "action.CIDR.Lang.Wrap.By.Pragma.Region": "#pragma region...endregion",
  "action.CIDR.Lang.goto.definition.declaration": "정의/선언으로 이동",
  "action.CIDR.Lang.goto.definition.declaration.tooltip": "정의/선언으로 이동",
  "action.CIDR.Lang.goto.super.definition": "상위 정의(&U)",
  "action.CIDR.Lang.goto.definition": "정의(&E)",
  "action.CIDR.Lang.QualifiedNames.text": "정규화된 이름 그룹화",
  "action.CIDR.Lang.QualifiedNames.description": "정규화된 이름 그룹화",
  "loading.module.maps": "모듈 맵 로드 중\\u2026",
  "saving.module.maps": "모듈 맵 저장 중\\u2026",
  "building.module.maps": "모듈 맵 빌드 중\\u2026",
  "processing.module.maps": "모듈 맵 처리 중\\u2026",
  "loading.headers.search.roots": "헤더 검색 루트 로드 중\\u2026",
  "goto.symbol": "이동",
  "goto.symbol.ellipsis": "이동\\u2026",
  "goto.related.symbol.name1": "정의로 이동",
  "goto.related.symbol.name2": "''{1}''의 {0}(으)로 이동",
  "goto.related.symbol.name3": "{0}의 사전 정의로 이동",
  "goto.related.symbol.name4": "{0}의 정의로 이동",
  "goto.related.symbol.name5": "{0}의 선언으로 이동",
  "goto.related.symbol.name6": "관련된 {0}(으)로 이동",
  "goto.related.symbol.name1.tooltip": "정의로 이동",
  "goto.related.symbol.name2.tooltip": "''{1}''의 {0}(으)로 이동",
  "goto.related.symbol.name3.tooltip": "{0}의 사전 정의로 이동",
  "goto.related.symbol.name4.tooltip": "{0}의 정의로 이동",
  "goto.related.symbol.name5.tooltip": "{0}의 선언으로 이동",
  "goto.related.symbol.name6.tooltip": "관련된 {0}(으)로 이동",
  "goto.super.type.name1": "{1}의 상위 {0}(으)로 이동"
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
