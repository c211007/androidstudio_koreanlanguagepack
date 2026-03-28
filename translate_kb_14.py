import json

ko_dict = {
  "error.hint.text.cannot.inline.0.from.a.decompiled.file": "디컴파일된 파일에서 ''{0}''을(를) 인라인할 수 없습니다.",
  "error.text.can.t.change.signature.of.method": "{0} 메서드의 서명을 변경할 수 없습니다.",
  "error.text.can.t.copy.class.to.the.containing.file": "포함하는 파일로 클래스를 복사할 수 없습니다.",
  "error.text.can.t.generate.0.1": "{0}을(를) 생성할 수 없습니다: {1}",
  "error.text.can.t.introduce.lambda.parameter.for.this.expression": "이 표현식의 람다 매개변수를 도입할 수 없습니다.",
  "error.text.can.t.introduce.property.for.this.expression": "이 표현식의 속성을 도입할 수 없습니다.",
  "error.text.can.t.introduce.constant.for.this.expression.because.not.constant": "상수가 아닌 표현식의 상수를 도입할 수 없습니다.",
  "error.text.can.t.introduce.constant.for.this.expression": "이 표현식의 상수를 도입할 수 없습니다.",
  "error.text.different.name.expected": "다른 이름이 예상됨",
  "error.text.expression.has.no.type": "표현식에 유형이 없습니다.",
  "error.text.extraction.from.expect.class.is.not.yet.supported": "expect 클래스에서의 추출은 아직 지원되지 않습니다.",
  "error.text.extraction.from.non.jvm.class.is.not.yet.supported": "비 JVM 클래스에서의 추출은 아직 지원되지 않습니다.",
  "error.text.inline.function.is.not.supported.for.functions.with.multiple.return.statements": "여러 반환 문이 있는 함수에는 인라인 함수가 지원되지 않습니다.",
  "error.text.inline.function.is.not.supported.for.functions.with.return.statements.not.at.the.end.of.the.body": "반환 문이 본문 끝에 있지 않은 함수에는 인라인 함수가 지원되지 않습니다.",
  "error.text.interface.cannot.be.extracted.from.an.annotation.class": "주석 클래스에서 인터페이스를 추출할 수 없습니다.",
  "error.text.introduce.parameter.is.not.available.for.default.value": "기본값에는 매개변수 도입을 사용할 수 없습니다.",
  "error.text.introduce.parameter.is.not.available.inside.of.annotation.entries": "주석 항목 내에서는 매개변수 도입을 사용할 수 없습니다.",
  "error.text.invalid.name": "잘못된 이름",
  "error.text.invalid.parameter.name": "잘못된 매개변수 이름",
  "error.text.invalid.parameter.type": "잘못된 매개변수 유형",
  "error.text.invalid.receiver.type": "잘못된 수신자 유형",
  "error.text.invalid.return.type": "잘못된 반환 유형",
  "error.text.no.type.to.refactor": "리팩터링할 유형이 없습니다.",
  "error.text.refactoring.is.not.applicable.in.the.current.context": "현재 컨텍스트에서는 리팩터링을 적용할 수 없습니다.",
  "error.text.superclass.cannot.be.extracted.from.an.annotation.class": "주석 클래스에서 상위 클래스를 추출할 수 없습니다.",
  "error.text.type.reference.is.expected": "유형 참조가 예상됨",
  "error.types.in.generated.function": "잘못된 반환 유형이 포함된 함수를 생성할 수 없습니다.",
  "error.wrong.caret.position.function.or.constructor.name": "캐럿은 리팩터링할 함수 또는 생성자 이름에 위치해야 합니다.",
  "explicitly.ignore.return.value": "반환 값을 명시적으로 무시",
  "extract.function": "함수 추출",
  "family.name.update.usages.on.declarations.cut.paste": "선언을 잘라내기/붙여넣기할 때 사용 항목 업데이트",
  "function.name.is.invalid": "함수 이름이 잘못되었습니다.",
  "introduce.property": "속성 도입",
  "introduce.type.parameter.to.declaration": "선언에 유형 매개변수 도입",
  "introduce.type.parameter": "유형 매개변수 도입",
  "introduce.variable": "변수 도입",
  "introduce.constant": "상수 도입",
  "label.text.default.receiver.value": "기본 수신자 값(&D):",
  "label.text.destination.directory": "대상 디렉터리(&D):",
  "label.text.file.name": "파일 이름(&n):",
  "label.text.introduce.as": "다음으로 도입(&I):\\u0020",
  "label.text.name": "이름(&N):",
  "label.text.package.name": "패키지 이름(&g):",
  "label.text.source.sets": "소스 세트:",
  "label.text.receiver.type": "수신자 유형(&t):",
  "label.text.target.file.name": "대상 파일 이름:",
  "label.text.to.file": "대상 파일(&f):",
  "label.text.to.package": "대상 패키지(&a):",
  "label.text.to.class": "대상 클래스:",
  "label.text.to.object": "대상 객체:"
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

print(f"Updated {filename} (Keys 591-640)")

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
