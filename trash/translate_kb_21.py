import json

ko_dict = {
  "fix.with.asdynamic": "'asDynamic'으로 수정",
  "migrate.type.parameter.list.syntax": "유형 매개변수 목록 구문 마이그레이션",
  "replace.deprecated.symbol.usage": "더 이상 사용되지 않는 기호 사용 항목 바꾸기",
  "replace.with.0": "''{0}''(으)로 바꾸기",
  "there.is.own.replacewith.on.0.that.is.used.through.this.alias.please.replace.usages.first": "이 별칭을 통해 사용되는 ''{0}''에 자체 ''ReplaceWith''가 있습니다. 먼저 사용 항목을 바꾸세요.",
  "replace.deprecated.symbol.usage.in.whole.project": "전체 프로젝트에서 더 이상 사용되지 않는 기호 사용 항목 바꾸기",
  "applying.0": "''{0}'' 적용 중",
  "replace.usages.of.0.in.whole.project": "전체 프로젝트에서 ''{0}'' 사용 항목 바꾸기",
  "replace.with.publishedapi.bridge.call": "@PublishedApi 브리지 호출로 바꾸기",
  "replace.with.generated.publishedapi.bridge.call.0": "생성된 @PublishedApi 브리지 호출 ''{0}''(으)로 바꾸기",
  "convert.sealed.subclass.to.object.fix.family.name": "봉인된 하위 클래스를 객체로 변환",
  "progress.looking.up.sealed.subclass.usage": "봉인된 하위 클래스 사용 항목 검색 중\\u2026",
  "generate.identity.equals.fix.family.name": "ID로 equals \\\\& hashCode 생성",
  "change.type.of.0.to.1": "{0}의 유형을 ''{1}''(으)로 변경",
  "change.type.to.0": "유형을 ''{0}''(으)로 변경",
  "base.property.0": "기본 속성 {0}",
  "make.0": "{0} 만들기",
  "make.0.1.explicitly": "명시적으로 ''{0}'' {1} 만들기",
  "make.0.explicitly": "명시적으로 {0} 만들기",
  "use.inherited.visibility": "상속된 가시성 사용",
  "replace.with.in.when": "when에서 ','를 '||'로 바꾸기",
  "remove.0": "''.{0}'' 제거",
  "remove.conversion.from.kclass.to.class": "'KClass'에서 'Class'로의 변환 제거",
  "convert.from.class.to.kclass": "'Class'를 'KClass'로 변환",
  "convert.to.0": "{0}(으)로 변환",
  "replace.with.arrayof": "'arrayOf'로 바꾸기",
  "convert.expression.to.0.by.inserting.1": "''.{1}''을(를) 삽입하여 표현식을 ''{0}''(으)로 변환",
  "convert.extension.property.initializer.to.getter": "확장 속성 초기화자를 getter로 변환",
  "convert.supertype.to.0": "상위 유형을 ''{0}''(으)로 변환",
  "convert.extension.function.type.to.regular.function.type": "확장 함수 유형을 일반 함수 유형으로 변환",
  "convert.to.notnull.delegate": "notNull 대리자로 변환",
  "convert.to.anonymous.object": "익명 객체로 변환",
  "select.loop.statement.to.label": "레이블을 지정할 루프 문 선택",
  "select.lambda.to.label": "레이블을 지정할 람다 선택",
  "create.label": "레이블 만들기",
  "create.label.0": "레이블 {0}@ 만들기",
  "convert.member.to.extension": "멤버를 확장으로 변환",
  "replace.annotation": "주석 바꾸기",
  "replace.annotation.with.0": "주석을 {0}(으)로 바꾸기",
  "add.initializer": "초기화자 추가",
  "move.to.constructor.parameters": "생성자 매개변수로 이동",
  "initialize.with.constructor.parameter": "생성자 매개변수로 초기화",
  "initialize.with.constructor.parameter.analyzing.existing.variables": "기존 변수 분석 중\\u2026",
  "inline.type.parameter": "인라인 유형 매개변수",
  "insert.explicit.delegation.call": "명시적 위임 호출 삽입",
  "the.anonymous.object": "익명 객체",
  "text.implement": "구현",
  "text.extend": "확장",
  "let.0.1": "{0} {1} 허용",
  "let.type.implement.interface": "유형이 인터페이스를 구현하도록 허용"
}

with open('missing_translations/missing_keys_korean.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

filename = "KotlinBundle.properties"
found = False
for file_entry in data.get('new_files', []):
    if file_entry['filename'] == filename:
        file_entry['keys'].update(ko_dict)
        found = True
        break
if not found:
    data.setdefault('new_files', []).append({"filename": filename, "keys": ko_dict})

print(f"Updated {filename} (Keys 891-940)")

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
