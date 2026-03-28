import json

ko_dict = {
  "inspection.complex.redundant.let.display.name": "인수 기반의 중복되는 'let' 호출",
  "inspection.simple.redundant.let.display.name": "수신자 기반의 중복되는 'let' 호출",
  "inspection.replace.array.equality.op.with.arrays.equals.display.name": "'==' 및 '!='를 사용한 배열 비교",
  "inspection.suspicious.cascading.if.display.name": "의심스러운 계단식(cascading) 'if' 표현식",
  "inspection.remove.empty.parentheses.from.lambda.call.display.name": "람다가 있는 함수 호출에 불필요한 괄호",
  "inspection.remove.empty.parentheses.from.lambda.call.action.name": "람다가 있는 함수 호출에서 불필요한 괄호 제거",
  "inspection.remove.to.string.in.string.template.display.name": "문자열 템플릿에서 'toString()'에 대한 중복 호출",
  "inspection.remove.single.expression.string.template.display.name": "중복된 문자열 템플릿",
  "inspection.replace.call.with.binary.operator.display.name": "이항 연산자로 바꿀 수 있습니다.",
  "inspection.remove.setter.parameter.type.display.name": "중복되는 setter 매개변수 유형",
  "inspection.convert.reference.to.lambda.display.name": "람다로 바꿀 수 있습니다.",
  "inspection.convert.lambda.to.reference.display.name": "함수 참조로 바꿀 수 있습니다.",
  "inspection.can.be.primary.constructor.property.display.name": "속성이 생성자 매개변수에 명시적으로 할당되었습니다.",
  "inspection.can.unescape.dollar.literal.inspection.display.name": "문자열 리터럴에 중복되는 이스케이프된 달러 문자",
  "inspection.can.unescape.dollar.literal.inspection.problem.description": "문자열에서 이스케이프된 달러 문자를 간소화할 수 있습니다.",
  "replace.with.dollar.literals": "이스케이프된 달러 기호를 리터럴로 바꾸기",
  "inspection.can.convert.to.multi.dollar.string.display.name": "문자열 리터럴에 다중 달러(Multi-dollar) 보간(interpolation)을 사용할 수 있습니다.",
  "inspection.can.convert.to.multi.dollar.string.problem.description": "보간 접두사를 사용하면 문자열을 간소화할 수 있습니다.",
  "add.interpolation.prefix": "보간 접두사 추가",
  "inspection.has.platform.type.display.name": "함수 또는 속성에 플랫폼 유형이 있습니다.",
  "inspection.leaking.this.display.name": "생성자에서 'this' 누수(leaking)",
  "inspection.redundant.if.display.name": "중복되는 'if' 문",
  "inspection.redundant.unit.return.type.display.name": "중복되는 'Unit' 반환 유형",
  "inspection.redundant.unit.return.type.action.name": "중복되는 'Unit' 반환 유형 제거",
  "inspection.redundant.semicolon.display.name": "중복되는 세미콜론",
  "inspection.redundant.modality.modifier.display.name": "중복되는 모달리티(modality) 제어자",
  "inspection.can.be.parameter.display.name": "생성자 매개변수를 속성으로 사용하지 않습니다.",
  "inspection.replace.substring.with.substring.before.display.name": "'substring' 호출을 'substringBefore'로 바꿔야 합니다.",
  "inspection.replace.substring.with.substring.after.display.name": "'substring' 호출을 'substringAfter'로 바꿔야 합니다.",
  "inspection.replace.substring.with.indexing.operation.display.name": "'substring' 호출을 인덱싱 연산자로 바꿔야 합니다.",
  "inspection.replace.substring.with.take.display.name": "'substring' 호출을 'take' 호출로 바꿔야 합니다.",
  "inspection.replace.substring.with.drop.last.display.name": "'substring' 호출을 'dropLast' 호출로 바꿔야 합니다.",
  "inspection.add.variance.modifier.display.name": "유형 매개변수에 'in' 또는 'out' 가변성(variance)이 있을 수 있습니다.",
  "inspection.protected.in.final.display.name": "final 클래스에서 'protected' 가시성은 사실상 'private'입니다.",
  "inspection.array.in.data.class.display.name": "데이터 클래스의 배열 속성",
  "inspection.can.be.val.display.name": "지역 'var'가 수정되지 않으므로 'val'로 선언할 수 있습니다.",
  "inspection.destructure.display.name": "구조 분해(destructuring) 선언 사용",
  "inspection.redundant.visibility.modifier.display.name": "중복되는 가시성 제어자",
  "inspection.equals.or.hash.code.display.name": "'equals()'와 'hashCode()'가 쌍을 이루지 않았습니다.",
  "inspection.conflicting.extension.property.display.name": "합성(synthetic) 속성과 충돌하는 확장 속성",
  "inspection.use.with.index.display.name": "수동으로 증가된 인덱스 변수를 'withIndex()' 사용으로 바꿀 수 있습니다.",
  "inspection.use.with.index.k2.display.name": "수동으로 증가된 인덱스 변수",
  "inspection.use.with.index.k2.problem.description": "수동으로 증가된 인덱스 변수를 'withIndex()' 사용으로 바꿀 수 있습니다.",
  "inspection.loop.to.call.chain.display.name": "루프를 stdlib 연산으로 바꿀 수 있습니다.",
  "inspection.remove.for.loop.indices.display.name": "사용되지 않는 루프 인덱스",
  "inspection.kotlin.deprecation.display.name": "중복되거나 더 이상 사용되지 않는 구문 또는 기호 사용",
  "inspection.package.directory.mismatch.display.name": "패키지 이름이 포함하는(containing) 디렉터리와 일치하지 않습니다.",
  "inspection.k.doc.missing.documentation.display.name": "public 선언을 위한 KDoc 주석 누락",
  "inspection.k.doc.unresolved.reference.display.name": "KDoc에서 확인되지 않은(unresolved) 참조",
  "inspection.unsafe.cast.from.dynamic.display.name": "동적(dynamic) 유형에서 암시적(안전하지 않은) 캐스트"
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

print(f"Updated {filename} (Keys 1891-1940)")

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
