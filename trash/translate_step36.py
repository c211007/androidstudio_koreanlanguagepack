import json
with open('missing_translations/missing_keys_korean.json', 'r', encoding='utf-8') as f:
    ko_data = json.load(f)

translations = {
  "wrap.return.value.inner.class.name": "이름(&M)",
  "wrap.return.value.new.class.name": "이름(&N)",
  "wrap.return.value.new.class.package.name": "패키지 이름(&P)",
  "wrap.return.value.use.existing.class": "기존 클래스 사용(&U)",
  "wrap.return.value.wrapper.field": "래퍼(wrapper) 필드(&F)",
  "replace.inside.current.lambda": "현재 람다 내부에 변수 생성",
  "replace.as.separate.operation": "''{0}'' 작업으로 추출",
  "replace.all.occurrences.changes.semantics": "모든 {0}개 항목 바꾸기 (주의: 의미(semantics)가 변경됩니다!)",
  "replace.all.read.and.write": "읽기 및 쓰기 발생 모두 바꾸기 (주의: 의미가 변경됩니다!)",
  "replace.all.and.extract": "모든 {0}개 항목을 바꾸고 ''{1}'' 작업으로 추출",
  "replace.lambda.chain.detected": "람다 체인 감지됨",
  "replace.occurrences.inside.statement": "{2, choice, 1#|2#외부 }''{1}'' 블록 내의 {0}개 항목 바꾸기",
  "extract.method.object": "메서드 객체 추출",
  "replace.constructor.with.builder": "생성자를 빌더(Builder)로 교체",
  "replace.constructor.with.builder.text": "생성자를 빌더로 교체",
  "type.migration.error.hint.title": "타입 마이그레이션",
  "extract.method.dialog.separator.parameters": "매개변수(&P)",
  "extract.method.conflict.parameter": "충돌하는 매개변수 이름: {0}",
  "extract.method.conflict.variable": "이름이 {0}인 변수가 선택한 범위(scope)에 이미 정의되어 있습니다",
  "extract.method.error.annotation.value": "어노테이션 값에서 메서드를 추출할 수 없습니다",
  "extract.method.error.local.class.defined.outside": "선택한 코드 조각이 해당 조각 외부에 정의된 로컬 클래스를 사용하므로 메서드를 추출할 수 없습니다",
  "extract.method.error.local.class.used.outside": "선택한 코드 조각이 해당 조각 외부에서 사용되는 로컬 클래스를 정의하므로 메서드를 추출할 수 없습니다",
  "extract.method.error.local.class.variable.used.outside": "선택한 코드 조각이 해당 조각 외부에서 사용되는 로컬 클래스 타입의 변수를 정의하므로 메서드를 추출할 수 없습니다",
  "extract.method.error.make.static": "정적(static)으로 만들지 못했습니다",
  "extract.method.preview.node.invalid.prefix": "잘못된 ",
  "suggest.signature.preview.method.call.prefix": "메서드 호출:",
  "suggest.signature.preview.title.before": "이전",
  "suggest.signature.preview.after.title": "이후",
  "removing.redundant.imports.progress.title": "불필요한 import 제거 중",
  "introduce.parameter.object.error.class.does.not.exist": "''{0}''이(가) 존재하지 않습니다",
  "introduce.parameter.object.error.invalid.qualified.parameter.class.name": "''{0}''은(는) 잘못된 정규화된 매개변수 클래스 이름입니다",
  "introduce.parameter.object.error.invalid.parameter.class.package.name": "''{0}''은(는) 잘못된 매개변수 클래스의 패키지 이름입니다",
  "introduce.parameter.object.error.invalid.parameter.class.name": "''{0}''은(는) 잘못된 매개변수 클래스 이름입니다",
  "introduce.parameter.object.error.inner.class.already.exist": "이름이 ''{0}''인 내부 클래스가 이미 존재합니다",
  "introduce.parameter.object.error.invalid.inner.class.name": "''{0}''은(는) 잘못된 내부 클래스 이름입니다",
  "introduce.parameter.object.error.no.field.associated.found": "{0}와(과) 연관된 필드를 찾을 수 없습니다",
  "introduce.parameter.object.error.existing.class.misses.compatible.constructor": "기존 클래스에 호환되는 생성자가 없습니다",
  "introduce.parameter.object.error.created.class.wont.be.accessible": "생성된 클래스에 접근할 수 없습니다",
  "introduce.parameter.object.error.file.already.exits": "파일이 이미 존재합니다: {0}",
  "replace.constructor.builder.error.identifier.invalid": "식별자 ''{0}''이(가) 잘못되었습니다"
}

ko_error_bundle = next((x for x in ko_data['new_files'] if x['filename'] == 'JavaRefactoringBundle.properties'), None)
ko_error_bundle['keys'].update(translations)
ko_error_bundle['key_count'] = len(ko_error_bundle['keys'])

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(ko_data, f, ensure_ascii=False, indent=2)

print("Updated JavaRefactoringBundle part 19")