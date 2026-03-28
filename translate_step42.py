import json
import os

file_path = "missing_translations/missing_keys_korean.json"
with open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)

bundle_name = "JavaSyntaxBundle.properties"

translations = {
  "annotation.name.is.missing": "'name=value' 형식의 어노테이션 속성이 필요합니다",
  "bound.not.expected": "예상치 못한 경계",
  "catch.without.try": "'try' 없는 'catch'",
  "class.literal.expected": ".class가 필요합니다",
  "feature.assertions": "단언(Assertion)",
  "feature.enums": "열거형(Enum)",
  "feature.generics": "제네릭(Generic)",
  "feature.annotations": "어노테이션",
  "feature.override.interface": "인터페이스의 @Override",
  "feature.static.imports": "정적 임포트(Static import)",
  "feature.for.each": "For-each 루프",
  "feature.varargs": "가변 인자 메서드(Varargs)",
  "feature.hex.fp.literals": "16진수 부동 소수점 리터럴",
  "feature.diamond.types": "다이아몬드 타입",
  "feature.multi.catch": "다중 catch(Multi-catch)",
  "feature.try.with.resources": "Try-with-resources",
  "feature.binary.literals": "2진수 리터럴",
  "feature.underscores.in.literals": "리터럴 내 밑줄",
  "feature.string.switch": "'switch' 문의 문자열",
  "feature.objects.class": "java.util.Objects API",
  "feature.stream.and.optional.api": "Stream 및 Optional API",
  "feature.advanced.collection.api": "컬렉션의 람다 메서드",
  "feature.with.initial": "ThreadLocal.withInitial()",
  "feature.extension.methods": "확장 메서드",
  "feature.method.references": "메서드 참조",
  "feature.lambda.expressions": "람다 표현식",
  "feature.type.annotations": "타입 어노테이션",
  "feature.repeating.annotations": "반복 어노테이션",
  "feature.type.receivers": "수신자 매개변수",
  "feature.intersections.in.casts": "캐스트의 교차 타입",
  "feature.static.interface.calls": "정적 인터페이스 메서드 호출",
  "feature.effectively.final": "실질적 final(effectively final) 변수",
  "feature.try.with.resources.refs": "리소스 참조",
  "feature.modules": "모듈",
  "feature.auto.root.modules": "모든 API 익스포트 모듈은 암시적으로 루트 모듈이 됩니다",
  "feature.private.interface.methods": "프라이빗 인터페이스 메서드",
  "feature.utf8.property.files": "UTF-8 인코딩의 프로퍼티 파일",
  "feature.collection.factories": "컬렉션 팩토리 메서드",
  "feature.lvti": "로컬 변수 타입 추론",
  "feature.var.lambda.parameter": "람다 매개변수의 'var'"
}

found = False
for file_entry in data:
    if file_entry["filename"] == bundle_name:
        file_entry.setdefault("keys", {}).update(translations)
        found = True
        break

if not found:
    data.append({
        "filename": bundle_name,
        "keys": translations
    })

with open(file_path, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

print(f"Updated {bundle_name} (Keys 1-40)")