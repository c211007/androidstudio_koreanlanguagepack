import json

ko_dict = {
  "text.move.refactoring.not.available.during.indexing": "이동 리팩터링을 사용할 수 없습니다. 프로젝트를 분석하는 중입니다\\u2026",
  "text.moving.multiple.nested.classes.to.top.level.not.supported": "여러 중첩 클래스를 최상위 수준으로 이동하는 것은 지원되지 않습니다.",
  "text.Name": "이름",
  "text.nested.classes.to.upper.level": "상위 수준으로 중첩 클래스 이동",
  "text.no.elements.to.move.are.selected": "이동할 요소가 선택되지 않았습니다.",
  "text.no.files.to.move": "이동할 파일이 지정되지 않았습니다.",
  "text.no.name.provided.for.type.alias": "유형 별칭의 이름이 제공되지 않았습니다.",
  "text.no.package.corresponds.to.directory": "이 디렉터리에 해당하는 패키지가 없습니다.",
  "text.non.kotlin.0.will.not.be.affected.by.refactoring": "비 Kotlin {0}은(는) 리팩터링의 영향을 받지 않습니다.",
  "text.overload": "오버로드",
  "text.package.directive.dont.match.file.location": "패키지 지시문이 파일 위치와 일치하지 않습니다.",
  "text.parameter.0": "매개변수 ''{0}''",
  "text.parameter.name": "매개변수 이름(&N):\\u0020",
  "text.parameter.reference.can.t.be.safely.replaced.with.0.since.1.is.ambiguous.in.this.context": "이 컨텍스트에서는 {1}이(가) 모호하므로 매개변수 참조를 {0}(으)로 안전하게 바꿀 수 없습니다.",
  "text.parameter.reference.can.t.be.safely.replaced.with.0.since.target.function.can.t.be.referenced.in.this.context": "이 컨텍스트에서는 대상 함수를 참조할 수 없으므로 매개변수 참조를 {0}(으)로 안전하게 바꿀 수 없습니다.",
  "text.parameter.type": "매개변수 유형(&T):\\u0020",
  "text.parameter": "매개변수",
  "text.parameters": "매개변수(&P)",
  "text.proceed.with.extraction": "어쨌든 추출 진행",
  "text.process.duplicates": "중복 처리",
  "text.processing.file.0": "{0} 처리 중",
  "text.property.in.ticks.0": "속성 ''{0}''",
  "text.property.with.getter": "getter가 있는 속성",
  "text.property.with.initializer": "초기화자가 있는 속성",
  "text.property": "속성",
  "text.property.0": "{0,choice,1#속성|2#속성}",
  "text.pushed.member.will.not.be.available.in.0": "내린 멤버는 ''{0}''에서 사용할 수 없습니다.",
  "text.qualified.call.will.not.be.processed.0": "정규화된 호출은 처리되지 않습니다: {0}",
  "text.receiver.can.t.be.safely.transformed.to.value.argument": "수신자를 값 인수로 안전하게 변환할 수 없습니다: {0}",
  "text.receiver": "수신자",
  "text.refactoring.can.t.be.performed.on.the.selected.code.element": "선택한 코드 요소에 리팩터링을 수행할 수 없습니다.",
  "text.refactoring.is.not.applicable.to.this.code.fragment": "이 코드 조각에는 리팩터링을 적용할 수 없습니다.",
  "text.references.in.code.to.0.1.and.its.declarations": "코드 내의 {0} {1} 및 해당 선언에 대한 참조",
  "text.remove.0.no.longer.used": "더 이상 사용되지 않는 {0} 제거",
  "text.remove.question": "'?' 제거",
  "text.remove": "제거",
  "text.rename.as.part.of.phrase": "이름 바꾸기",
  "text.rename.is.not.applicable.to.secondary.constructors": "보조 생성자에는 이름 바꾸기를 적용할 수 없습니다.",
  "text.rename.is.not.applicable.to.synthetic.declarations": "합성 선언에는 이름 바꾸기를 적용할 수 없습니다.",
  "text.rename.is.not.applicable.to.compiler.plugin.generated.declarations": "컴파일러 플러그인이 생성한 선언에는 이름 바꾸기를 적용할 수 없습니다.",
  "text.rename.not.applicable.to.backing.field.reference": "지원 필드 참조에는 이름 바꾸기를 적용할 수 없습니다.",
  "text.rename.not.applicable.to.dynamically.invoked.methods": "동적으로 호출된 멤버에는 이름 바꾸기를 적용할 수 없습니다.",
  "text.rename.overloads.title": "오버로드 이름 바꾸기",
  "title.rename.overloads.to": "오버로드 이름 바꾸기:",
  "text.rename.parameters.title": "매개변수 이름 바꾸기",
  "title.rename.warning": "이름 바꾸기 경고",
  "text.0.1.must.be.moved.with.sealed.parent.class.and.all.its.subclasses": "{0} ''{1}''은(는) 봉인된 상위 클래스 및 모든 하위 클래스와 함께 이동해야 합니다.",
  "text.sealed.class.0.must.be.moved.with.all.its.subclasses": "봉인된 클래스 ''{0}''은(는) 모든 하위 클래스와 함께 이동해야 합니다.",
  "text.sealed.broken.hierarchy.none.in.target": "''{0}''의 봉인된 계층 구조가 분할됩니다. 모듈 ''{2}''의 패키지 ''{1}''에 상주하는 멤버가 없습니다: {3}.",
  "text.sealed.broken.hierarchy.still.in.source": "''{0}''의 봉인된 계층 구조가 분할됩니다. 모듈 ''{2}''의 패키지 ''{1}''에 여전히 해당 멤버가 포함됩니다: {3}."
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

print(f"Updated {filename} (Keys 741-790)")

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
