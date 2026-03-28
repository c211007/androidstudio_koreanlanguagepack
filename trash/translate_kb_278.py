import json

translations = {
  "change.class.parameter.incorrect.type.error.hint": "잘못된 유형",
  "change.class.type.parameter.family.name": "클래스 타입 매개변수 변경",
  "convert.to.atomic.family.name": "원자적(atomic)으로 변환",
  "convert.to.longadder.family.name": "'LongAdder'로 변환",
  "convert.to.threadlocal.family.name": "'ThreadLocal'로 변환",
  "guava.functional.primitives.can.be.replaced.by.java.api.problem.description": "Guava의 함수형 기본 타입을 Java API로 바꿀 수 있습니다.",
  "inspection.guava.erase.option": "변환된 함수에서 @javax.annotations.Nullable 지우기",
  "inspection.guava.method.chains.option": "메서드 체인 보고",
  "inspection.guava.return.types.option": "반환 유형 보고",
  "inspection.guava.variables.option": "변수 보고",
  "migrate.fix.text": "<html>''{0}'' 유형을 ''{1}''(으)로 마이그레이션</html>",
  "migrate.guava.to.java.family.name": "Guava 타입을 Java로 마이그레이션",
  "migrate.method.chain.fix.text": "메서드 체인 유형을 ''{0}''(으)로 마이그레이션",
  "inspection.guava.name": "Guava의 함수형 기본 타입을 Java로 바꿀 수 있음"
}

with open("missing_translations/missing_keys_korean.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for file_info in data.get("new_files", []):
    if file_info.get("filename") == "TypeMigrationBundle.properties":
        keys_dict = file_info.get("keys", file_info.get("properties", {}))
        keys_dict.update(translations)
        file_info["keys"] = keys_dict
        break
else:
    data.setdefault("new_files", []).append({
        "filename": "TypeMigrationBundle.properties",
        "keys": translations
    })

with open("missing_translations/missing_keys_korean.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)
