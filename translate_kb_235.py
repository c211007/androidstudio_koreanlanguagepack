import json

translations = {
  "predefined.configuration.annotation.declarations": "주석 선언",
  "predefined.configuration.annotations": "주석",
  "predefined.configuration.annotated.class": "주석이 달린 클래스, 인터페이스 및 Enum",
  "predefined.configuration.entity.ejb": "엔티티 EJB",
  "predefined.configuration.generic.methods": "제네릭 메서드",
  "predefined.configuration.cloneable.implementations": "Cloneable 구현",
  "predefined.configuration.xdoclet.metadata": "XDoclet 메타데이터",
  "predefined.configuration.type.var.substitutions.in.instanceof.with.generic.types": "제네릭 유형이 있는 instanceof에서 변수 대체의 유형",
  "predefined.configuration.singletons": "싱글톤",
  "predefined.configuration.switches": "Switche문",
  "predefined.configuration.foreaches": "Foreach 루프",
  "predefined.configuration.interfaces": "인터페이스",
  "predefined.configuration.string.literals": "문자열 리터럴",
  "predefined.configuration.all.inner.classes.within.hierarchy": "모든 내부 클래스(계층 구조 내)",
  "predefined.configuration.direct.subclasses": "직접 서브클래스",
  "predefined.configuration.javadoc.annotated.methods": "Javadoc 주석이 달린 메서드 및 생성자",
  "predefined.configuration.javadoc.annotated.fields": "Javadoc 주석이 달린 필드",
  "predefined.configuration.assignments": "할당",
  "predefined.configuration.casts": "캐스트",
  "predefined.configuration.serializable.classes.and.their.serialization.implementation": "직렬화 가능한 클래스 및 직렬화 구현",        
  "predefined.configuration.annotated.fields": "주석이 달린 필드",
  "predefined.configuration.generic.classes": "제네릭 클래스",
  "predefined.configuration.javadoc.annotated.class": "Javadoc 주석이 달린 클래스",
  "predefined.configuration.constructors.of.the.class": "클래스 생성자",   
  "predefined.configuration.typed.symbol": "유형이 지정된 기호",
  "predefined.configuration.all.fields.of.the.class": "클래스의 모든 필드",  
  "predefined.configuration.instance.fields.of.the.class": "클래스의 인스턴스 필드",
  "predefined.configuration.packagelocal.fields.of.the.class": "패키지 비공개 필드",
  "predefined.configuration.classes": "클래스",
  "predefined.configuration.classes.interfaces.enums": "클래스, 인터페이스 및 Enum",
  "predefined.configuration.new.expressions": "새 표현식",
  "predefined.configuration.lambdas": "람다",
  "predefined.configuration.method.references": "메서드 참조",
  "predefined.configuration.string.concatenations": "피연산자가 많은 문자열 연결",
  "predefined.configuration.deprecated.method.calls": "지원 중단된 메서드 호출",
  "predefined.configuration.methods.with.final.parameters": "final 매개변수가 있는 메서드 및 생성자",
  "predefined.configuration.class.static.blocks": "정적 이니셜라이저",        
  "predefined.configuration.class.instance.initialization.blocks": "인스턴스 이니셜라이저",
  "predefined.configuration.class.any.initialization.blocks": "모든 이니셜라이저",
  "predefined.configuration.logging.without.if": "if 없는 로깅",
  "predefined.configuration.assert.without.description": "설명이 없는 Assert 구문",
  "predefined.configuration.class.with.parameterless.constructors": "매개변수 없는 생성자가 있는 클래스",
  "predefined.configuration.static.fields.without.final": "final이 아닌 정적 필드",
  "predefined.configuration.sample.method.invokation.with.constant.argument": "상수 인수가 있는 샘플 메서드 호출",
  "predefined.configuration.interfaces.having.no.descendants": "구현되거나 확장되지 않은 인터페이스",
  "predefined.configuration.enums": "Enum",
  "predefined.configuration.records": "레코드",
  "predefined.configuration.comments.containing.word": "특정 단어가 포함된 주석",
  "predefined.configuration.xml.attribute.referencing.java.class": "Java 클래스를 참조하는 XML 속성",
  "predefined.configuration.statement.in.if": "if의 문"
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
