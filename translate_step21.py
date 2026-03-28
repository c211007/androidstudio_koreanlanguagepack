import json
with open('missing_translations/missing_keys_korean.json', 'r', encoding='utf-8') as f:
    ko_data = json.load(f)

translations = {
  "class.is.abstract": "{0}은(는) 추상(abstract) 클래스입니다.",
  "class.is.anonymous.warning.message": "익명 클래스는 하위 클래스를 가질 수 없으므로 리팩터링을 수행할 수 없습니다",
  "class.is.final.warning.message": "클래스가 final이므로 리팩터링을 수행할 수 없습니다",
  "class.is.interface": "{0}은(는) 인터페이스입니다.",
  "class.is.never.used": "클래스가 사용되지 않습니다",
  "class.name.prompt": "클래스 이름(&N):",
  "collect.overloads": "오버로드 수집\\u2026",
  "comments.elements.header": "주석, 문자열 및 코드가 아닌 파일 {0}에서 발생 항목 발견",
  "constructor.being.refactored.is.used.in.initializer.of.0": "리팩터링 중인 생성자가 {0}의 초기화자에서 사용되고 있습니다. 내부 클래스 {1}의 비정적(non-static) 팩터리는 이 컨텍스트에서 사용할 수 없습니다. 결과 코드가 컴파일되지 않습니다.",
  "constructor.description": "{0} 생성자",
  "constructor.with.builder.new.setter.prefix.dialog.message": "새 setter 접두사:",
  "constructor.with.builder.parameters.to.pass.to.the.builder.title": "빌더(Builder)에 전달할 매개변수",
  "constructor.with.builder.rename.setters.prefix.action.name": "Setter 접두사 이름 변경",
  "convert.anonymous.to.inner.action.name": "익명을 내부로 변환(Convert Anonymous to Inner)\\u2026",
  "convert.local.to.inner.action.name": "지역(Local)을 내부로 변환(Convert Local to Inner)\\u2026",
  "convert.anonymous.to.inner.fix.name": "익명 클래스를 내부 클래스로 변환",
  "convert.local.to.inner.fix.name": "지역 클래스를 내부 클래스로 변환",
  "convert.anonymous.or.local.to.inner.fix.name": "익명 또는 지역 클래스를 내부 클래스로 변환",
  "convert.local.to.field.title": "지역을 필드로 변환(Convert Local to Field)",
  "convert.to.instance.method.title": "인스턴스 메서드로 변환(Convert To Instance Method)",
  "convertToInstanceMethod.all.reference.type.parameters.are.not.in.project": "인스턴스 메서드의 대상 클래스를 찾을 수 없습니다: 프로젝트의 클래스를 참조하는 타입을 가진 메서드 매개변수를 찾을 수 없습니다.",
  "convertToInstanceMethod.all.reference.type.parameters.have.unknown.types": "인스턴스 메서드의 대상 클래스를 찾을 수 없습니다: 메서드 매개변수 타입을 알 수 없습니다.",
  "convertToInstanceMethod.method.is.not.static": "{0} 메서드가 정적(static)이 아닙니다",
  "convertToInstanceMethod.no.default.ctor": "추가로 포함된 클래스에 기본 생성자가 없습니다.",
  "convertToInstanceMethod.no.parameters.with.reference.type": "참조 타입인 매개변수가 없습니다.",
  "convert.to.record.title": "레코드 클래스로 변환(Convert To Record Class)",
  "convert.to.record.accessor.more.accessible": "{0}은(는) {1}입니다. 레코드로 변환하면 해당 암시적 접근자 메서드(accessor method)가 {2}이(가) 됩니다.",
  "convert.to.record.ctor.more.accessible": "{0}은(는) {1}입니다. 레코드로 변환하면 해당 암시적 정규(canonical) 레코드 생성자가 {2}이(가) 됩니다.",
  "copy.class.clone.0.1": "{0} {1} 클론",
  "copy.class.copy.0.1": "{0} {1} 복사",
  "copy.handler.clone.class": "클래스 클론",
  "copy.handler.copy.class": "클래스 복사",
  "copy.handler.copy.class.with.dialog": "클래스 복사\\u2026",
  "copy.handler.copy.classes.with.dialog": "클래스(복수) 복사\\u2026",
  "current.class": "현재 클래스",
  "dataflow.to.here.expand.progress": "모든 노드 확장 중\\u2026 {0}",
  "dataflow.to.here.group.by.leaf.action.description": "null이 이 표현식으로 전달될 수 있는지 확인합니다.",
  "dataflow.to.here.group.by.leaf.action.text": "말단(Leaf) 표현식 null 허용 여부별 그룹화{0, choice, 1#|2#  (분석 진행 중)}",
  "dataflow.to.here.variable.dereferenced.tooltip": "변수 역참조(dereferenced)됨",
  "declare.final": "final 선언(&F)"
}

ko_error_bundle = next((x for x in ko_data['new_files'] if x['filename'] == 'JavaRefactoringBundle.properties'), None)
ko_error_bundle['keys'].update(translations)
ko_error_bundle['key_count'] = len(ko_error_bundle['keys'])

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(ko_data, f, ensure_ascii=False, indent=2)

print("Updated JavaRefactoringBundle part 4")