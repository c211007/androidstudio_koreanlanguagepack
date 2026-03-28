import json

ko_dict = {
  "remove.explicit.supertype.qualification": "명시적 상위 유형(supertype) 한정자 제거",
  "remove.explicit.type.arguments": "명시적 유형 인수 제거",
  "remove.explicit.type.specification": "명시적 유형 지정 제거",
  "remove.explicit.type.specification.from.0": "''{0}''에서 명시적 유형 지정 제거",
  "remove.indices.in.for.loop": "'for' 루프의 indices 제거",
  "index.is.not.used.in.the.loop.body": "인덱스가 루프 본문에서 사용되지 않습니다.",
  "remove.return.0": "return@{0} 제거",
  "remove.labeled.return.from.last.expression.in.a.lambda": "람다의 마지막 표현식에서 레이블이 지정된 반환(return) 제거",
  "remove.redundant.calls.of.the.conversion.method": "중복된 변환 메서드 호출 제거",
  "redundant.call.of.the.conversion.method": "중복된 변환 메서드 호출",
  "remove.single.expression.string.template": "단일 표현식 문자열 템플릿 제거",
  "redundant.string.template": "중복된 문자열 템플릿",
  "rename.class.to.0": "클래스 이름을 {0}(으)로 바꾸기",
  "rename.class.to.containing.file.name": "클래스 이름을 포함하는 파일 이름으로 바꾸기",
  "rename.file.to.0.1": "파일 이름을 {0}.{1}(으)로 바꾸기",
  "rename.file.to.match.top.level.class.name": "파일 이름을 최상위 클래스 이름과 일치하도록 바꾸기",
  "replace.0.with": "''{0}()''을(를) ''+=''(으)로 바꾸기",
  "replace.with1": "'+='로 바꾸기",
  "replace.explicit.parameter.0.with.it": "명시적 매개변수 ''{0}''을(를) ''it''(으)로 바꾸기",
  "replace.it.with.explicit.parameter": "'it'을 명시적 매개변수로 바꾸기",
  "replace.with.0.1.2": "{0}[{1}] ?: {2}(으)로 바꾸기",
  "replace.with.indexing.and.elvis.operator": "인덱싱 및 elvis 연산자로 바꾸기",
  "map.get.or.default.can.be.replaced.with.indexing.and.elvis.operator": "'map.getOrDefault()'를 인덱싱 및 elvis 연산자로 바꿀 수 있습니다.",
  "replace.size.check.with.isnotempty": "크기 확인을 'isNotEmpty'로 바꾸기",
  "replace.size.check.with.0": "크기 확인을 ''{0}''(으)로 바꾸기",
  "replace.size.zero.check.with.isempty": "크기가 0인지 확인하는 코드를 'isEmpty'로 바꾸기",
  "replace.with.parameter.name": "'_'를 매개변수 이름으로 바꾸기",
  "replace.with.ordinary.assignment": "일반 할당으로 바꾸기",
  "replace.with.explicit.type": "'_'를 명시적 유형으로 바꾸기",
  "replace.with.underscore": "명시적 유형을 '_'로 바꾸기",
  "simplify.boolean.expression": "부울 표현식 간소화",
  "specify.all.remaining.arguments.by.name": "나머지 모든 인수를 이름으로 지정",
  "specify.remaining.required.arguments.by.name": "나머지 필수 인수를 이름으로 지정",
  "specify.explicit.lambda.signature": "명시적 람다 서명 지정",
  "specify.all.types.explicitly.in.destructuring.declaration": "구조 분해(destructuring) 선언에서 모든 유형을 명시적으로 지정",
  "cannot.infer.type.for.this.declaration": "이 선언의 유형을 유추할 수 없습니다.",
  "split.if.into.two": "'if'를 두 개로 분할",
  "flip.0": "''{0}'' 뒤집기(Flip)",
  "flip.binary.expression": "이항 표현식 뒤집기(Flip)",
  "flip.equals": "'equals' 뒤집기(Flip)",
  "replace.with.infix.function.call": "중위(infix) 함수 호출로 바꾸기",
  "convert.to.ordinary.string.literal": "일반 문자열 리터럴로 변환",
  "convert.to.raw.string.literal": "원시(raw) 문자열 리터럴로 변환",
  "remove.underscores": "밑줄(_) 제거",
  "add.underscores": "밑줄(_) 추가",
  "excluded.methods": "제외된 메서드:",
  "use.of.getter.method.instead.of.property.access.syntax": "속성 접근 구문 대신 getter 메서드 사용",
  "use.of.setter.method.instead.of.property.access.syntax": "속성 접근 구문 대신 setter 메서드 사용",
  "use.property.access.syntax": "속성 접근 구문 사용",
  "use.property.access.syntax.option.report.non.trivial.accessors": "사소하지 않은 접근자(non-trivial accessors) 보고"
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

print(f"Updated {filename} (Keys 1541-1590)")

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
