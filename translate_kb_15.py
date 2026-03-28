import json

ko_dict = {
  "label.text.package": "패키지(&A):",
  "label.text.destination": "대상(&D):",
  "label.text.file": "파일(&F):",
  "class.name.prompt": "클래스 이름(&N):",
  "search.for.text.occurrences": "텍스트 일치 항목 검색(&T)",
  "search.in.comments.and.strings": "주석 및 문자열에서 검색(&C)",
  "parameter.name.prompt": "매개변수 이름(&M):",
  "pass.outer.class.instance.as.parameter": "외부 클래스의 인스턴스를 매개변수로 전달(&O)",
  "label.text.type": "유형(&T):",
  "label.text.move.expect.actual.counterparts": "expect/actual 상대 요소 이동(&M)",
  "label.text.visibility": "가시성(&V):",
  "member.info.abstract.0": "abstract {0}",
  "member.info.companion.0": "companion {0}",
  "message.change.signature.is.not.applicable.to.dynamically.invoked.functions": "동적으로 호출된 함수에는 서명 변경을 적용할 수 없습니다.",
  "error.hint.library.declarations.cannot.be.changed": "라이브러리 선언은 변경할 수 없습니다.",
  "error.hint.cannot.modify.0.declaration.from.1.file": "''{1}'' 파일에서 ''{0}'' 선언을 수정할 수 없습니다.",
  "message.do.not.show.for.local.variables.in.future": "나중에 지역 변수에 대해 표시하지 않음",
  "message.text.return.type.cannot.be.resolved": "반환 유형 ''{0}''을(를) 확인할 수 없습니다.\\n계속하시겠습니까?",
  "message.text.property.type.cannot.be.resolved": "속성 유형 ''{0}''을(를) 확인할 수 없습니다.\\n계속하시겠습니까?",
  "message.text.property.receiver.type.cannot.be.resolved": "속성 수신자 유형 ''{0}''을(를) 확인할 수 없습니다.\\n계속하시겠습니까?",
  "message.type.for.cannot.be.resolved": "{1}의 유형 ''{0}''을(를) 확인할 수 없습니다.\\n계속하시겠습니까?",
  "name.extract.interface": "인터페이스 추출",
  "name.introduce.import.alias": "가져오기 별칭 도입",
  "name.introduce.lambda.parameter": "람다 매개변수 도입",
  "name.introduce.parameter1": "매개변수 도입",
  "name.introduce.type.alias": "유형 별칭 도입",
  "title.kdoc.for.abstracts": "추상화를 위한 KDoc",
  "naming.convention.will.be.violated.after.rename": "이름 바꾸기 후 명명 규칙이 위반됩니다.",
  "parameter.name.is.invalid": "매개변수 이름 ''{0}''이(가) 잘못되었습니다.",
  "parameter.type.is.invalid": "매개변수 유형 ''{0}''이(가) 잘못되었습니다.",
  "parameter.types.are.not.denotable": "다음 유형을 대상 범위에서 나타낼 수 없으므로 메서드를 추출할 수 없습니다:",
  "refactoring.move.non.kotlin.file": "대상은 Kotlin 파일이어야 합니다.",
  "refactoring.class.destination": "클래스 대상",
  "refactoring.file.destination": "파일 대상",
  "refactoring.cannot.find.target.class": "대상 클래스를 찾을 수 없습니다.",
  "return.type.is.invalid": "반환 유형이 잘못되었습니다.",
  "searching.usages.of.0.parameter": "''{0}'' 매개변수의 사용 항목 검색 중",
  "selected.code.fragment.has.multiple.exit.points": "선택한 코드 조각에 여러 종료점이 있습니다.",
  "selected.code.fragment.has.multiple.output.values": "선택한 코드 조각에 출력 값이 3개 이상 있습니다:",
  "selected.code.fragment.has.output.values.and.exit.points": "선택한 코드 조각에 출력 값과 대안 종료점이 있습니다.",
  "setter.of.0.will.become.invisible.after.extraction": "추출 후 {0}의 설정자가 보이지 않게 됩니다.",
  "text.0.already.contains.1": "{0}에 {1}이(가) 이미 포함되어 있습니다.",
  "text.0.already.contains.nested.class.1": "{0}에 이름이 {1}인 중첩된 클래스가 이미 포함되어 있습니다.",
  "text.0.already.declared.in.1": "{0}이(가) {1}에 이미 선언되어 있습니다.",
  "text.0.have.no.inheritors.warning": "{0}에 상속자가 없습니다.\\n멤버를 내리면 삭제됩니다. 계속하시겠습니까?",
  "text.0.in.1.will.override.corresponding.member.of.2.after.refactoring": "{1}의 {0}은(는) 리팩터링 후 {2}의 해당 멤버를 재정의합니다.",
  "text.0.inherits.from.1.it.will.not.be.affected.by.refactoring": "{0}이(가) {1}에서 상속합니다.\\n리팩터링의 영향을 받지 않습니다.",
  "text.0.is.invalid.destination.package": "''{0}''은(는) 잘못된 대상 패키지 이름입니다.",
  "text.0.is.not.allowed.in.the.target.context": "''{0}''은(는) 대상 컨텍스트에서 허용되지 않습니다.",
  "text.0.is.not.valid.package.name": "{0}은(는) 유효한 패키지 이름이 아닙니다."
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

print(f"Updated {filename} (Keys 641-690)")

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
