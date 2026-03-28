import json

ko_dict = {
  "remove.variable": "변수 제거",
  "remove.variable.0": "변수 ''{0}'' 제거",
  "remove.redundant.initializer": "중복 초기화자 제거",
  "remove.redundant.label": "중복 레이블 제거",
  "remove.single.lambda.parameter.declaration": "단일 람다 매개변수 선언 제거",
  "remove.supertype": "상위 유형 제거",
  "remove.0.variance.from.1": "''{1}''에서 ''{0}'' 변성 제거",
  "remove.parameter.0": "매개변수 ''{0}'' 제거",
  "remove.redundant.assignment": "중복 할당 제거",
  "remove.redundant.assignment.title": "중복 할당 제거",
  "extract.side.effects": "부작용(side effect) 추출",
  "delete.assignment.completely": "할당 완전히 삭제",
  "there.are.possible.side.effects.found.in.expressions.assigned.to.the.variable.0": "변수 ''{0}''에 할당된 표현식에 부작용이 있을 수 있습니다.<br>수행 가능한 작업:<br>-\\\\&nbsp;전체 할당 <b>제거</b>, 또는<br>-\\\\&nbsp;할당 오른쪽을 자체 문으로 <b>변환</b>.<br>",
  "remove.redundant.cast": "중복 캐스트 제거",
  "remove.redundant.elvis.operator": "중복 엘비스 연산자 제거",
  "remove.redundant.is.check": "중복 'is' 검사 제거",
  "remove.val.or.var.from.parameter": "매개변수에서 'val' 또는 'var' 제거",
  "remove.0.from.parameter": "매개변수에서 ''{0}'' 제거",
  "remove.else.branch": "else 분기 제거",
  "remove.branch": "분기 제거",
  "remove.condition": "조건 제거",
  "rename.identifier.fix.text": "이름 바꾸기",
  "rename.to.0": "''{0}''(으)로 이름 바꾸기",
  "rename.parameter.to.match.overridden.method": "재정의된 메서드와 일치하도록 매개변수 이름 바꾸기",
  "rename.to.underscore": "_(으)로 이름 바꾸기",
  "rename.0.to.explicitly.ignore.return.value": "명시적으로 반환 값을 무시하도록 변수 ''{0}''의 이름 바꾸기",
  "replace.with.safe.this.call": "안전한 호출(this?.)로 바꾸기",
  "replace.with.safe.call": "안전한 호출(?.)로 바꾸기",
  "replace.scope.function.with.safe.call": "범위 함수를 안전한 호출(?.)로 바꾸기",
  "replace.with.dot.call": "점 호출로 바꾸기",
  "replace.invalid.positioned.arguments.for.annotation": "주석에 대해 잘못 배치된 인수 바꾸기",
  "replace.jvmfield.with.const": "'@JvmField'를 'const'로 바꾸기",
  "replace.modifier": "한정자 바꾸기",
  "update.obsolete.label.syntax": "사용되지 않는 레이블 구문 업데이트",
  "replace.with.label.0.at": "레이블 {0}@로 바꾸기",
  "replace.cast.with.call.to.to.0": "캐스트를 ''to{0}()'' 호출로 바꾸기",
  "replace.cast.with.primitive.conversion.method": "캐스트를 기본 변환 메서드로 바꾸기",
  "replace.with.array.call": "배열 호출로 바꾸기",
  "remove.expression.target": "EXPRESSION 대상 제거",
  "change.existent.retention.to.source": "기존 보존을 SOURCE로 변경",
  "add.source.retention": "SOURCE 보존 추가",
  "round.using.0": "{0}()을(를) 사용하여 반올림",
  "simplify.0.to.1": "''{0}''을(를) ''{1}''(으)로 간소화",
  "simplify.comparison": "비교 간소화",
  "specify.override.for.0.explicitly": "''{0}''에 대한 재정의를 명시적으로 지정",
  "specify.override.explicitly": "재정의를 명시적으로 지정",
  "specify.return.type.explicitly": "반환 유형을 명시적으로 지정",
  "specify.type.explicitly": "유형을 명시적으로 지정",
  "add.constructor.parameters.from.0.1": "{0}{1}에서 생성자 매개변수 추가",
  "change.to.constructor.invocation": "생성자 호출로 변경"
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

print(f"Updated {filename} (Keys 991-1040)")

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
