import json

translations = {
  "interesting.category": "Java/흥미로운 템플릿",
  "predefined.configuration.method.calls": "메서드 호출",
  "predefined.configuration.struts.1.1.actions": "Struts 1.1 작업",
  "predefined.configuration.ejb.interface": "EJB 인터페이스",
  "predefined.configuration.servlets": "서블릿",
  "predefined.configuration.unboxing.in.method.calls": "메서드 호출의 언박싱",
  "predefined.configuration.boxing.in.method.calls": "메서드 호출의 박싱",  
  "predefined.configuration.unboxing.in.declarations": "선언의 언박싱",
  "predefined.configuration.boxing.in.declarations": "선언의 박싱",  
  "predefined.configuration.any.unboxing": "언박싱된 표현식",
  "predefined.configuration.any.boxing": "박싱된 표현식",
  "predefined.configuration.filters": "수정자",
  "predefined.configuration.session.ejb": "세션 EJB",
  "predefined.configuration.fields.variables.read": "읽은 필드/변수",    
  "predefined.configuration.symbol": "기호",
  "predefined.configuration.inner.classes": "내부 클래스",
  "predefined.configuration.junit.test.cases": "JUnit 테스트 케이스",
  "predefined.configuration.ifs": "If문",
  "predefined.configuration.anonymous.classes": "익명 클래스",
  "predefined.configuration.local.classes": "로컬 클래스",
  "predefined.configuration.javadoc.tags": "Javadoc 태그",
  "predefined.configuration.all.methods.of.the.class.within.hierarchy": "클래스의 모든 메서드(계층 구조 내)",
  "predefined.configuration.similar.methods.structure": "유사한 메서드 구조",
  "predefined.configuration.class.implements.two.interfaces": "두 인터페이스를 구현하는 클래스",
  "predefined.configuration.bean.info.classes": "Bean 정보 클래스",
  "predefined.configuration.all.expressions.of.some.type": "일부 유형의 모든 표현식",
  "predefined.configuration.variables.of.generic.types": "제네릭 유형의 변수",
  "predefined.configuration.diamond.operators": "다이아몬드 연산자",
  "predefined.configuration.method.returns.bounded.wildcard": "바인딩된 와일드카드를 반환하는 메서드",
  "predefined.configuration.generic.constructors": "제네릭 생성자",      
  "predefined.configuration.comments": "주석",
  "predefined.configuration.fields_variables.with.given.name.pattern.updated": "지정된 이름 패턴으로 업데이트된 필드/변수",
  "predefined.configuration.trys": "Try문",
  "predefined.configuration.try.without.resources": "리소스 및 catch 블록이 없는 Try 문",
  "predefined.configuration.switch.with.branches": "분기가 적은 Switch 문 및 표현식",
  "predefined.configuration.labeled.break": "라벨이 지정된 break 문",
  "predefined.configuration.double.checked.locking": "이중 검사 잠금",  
  "predefined.configuration.block.dcls": "블록 선언",
  "predefined.configuration.pattern.matching.instanceof": "패턴 일치 instanceof",
  "predefined.configuration.methods.of.the.class": "생성자 및 메서드",
  "predefined.configuration.deprecated.methods": "지원 중단된 메서드",
  "predefined.configuration.instanceof": "Instanceof",
  "predefined.configuration.implementors.of.interface.within.hierarchy": "인터페이스의 구현자(계층 구조 내)",
  "predefined.configuration.generic.casts": "제네릭 캐스트",
  "predefined.configuration.field.selections": "필드 선택",
  "predefined.configuration.fields.of.the.class": "클래스의 필드",
  "predefined.configuration.array.access": "배열 액세스",
  "predefined.configuration.usage.of.derived.type.in.cast": "캐스트에 파생된 유형 사용",
  "predefined.configuration.annotated.methods": "주석이 달린 메서드",
  "predefined.configuration.not.annotated.methods": "주석이 달리지 않은 메서드"     
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
