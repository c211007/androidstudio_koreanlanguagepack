import json
with open('missing_translations/missing_keys_korean.json', 'r', encoding='utf-8') as f:
    ko_data = json.load(f)

translations = {
  "replace.constructor.builder.optional.setter.table.title": "선택적(Optional) Setter",
  "replace.constructor.builder.default.value.table.title": "기본값",
  "replace.constructor.builder.setter.name.table.title": "Setter 이름",
  "replace.constructor.builder.field.name.table.title": "필드 이름",
  "replace.constructor.builder.parameter.table.title": "매개변수",
  "replace.constructor.builder.select.builder.class.chooser.title": "빌더(Builder) 클래스 선택",
  "replace.constructor.builder.error.invalid.builder.qualified.class.name": "''{0}''은(는) 유효한 정규화된 클래스 이름이 아닙니다",
  "replace.constructor.builder.error.invalid.builder.package.name": "''{0}''은(는) 유효한 패키지 이름이 아닙니다",
  "replace.constructor.builder.error.invalid.builder.class.name": "''{0}''은(는) 유효한 클래스 이름이 아닙니다",
  "replace.constructor.builder.error.builder.class.cannot.be.the.same": "{0} 클래스는 자체적인 빌더(Builder) 클래스가 될 수 없습니다.",
  "replace.constructor.builder.error.invalid.setter.name": "''{0}''은(는) 유효한 setter 이름이 아닙니다",
  "replace.constructor.builder.error.invalid.field.name": "''{0}''은(는) 유효한 필드 이름이 아닙니다",
  "replace.constructor.builder.error.no.constructors": "현재 클래스에는 빌더로 교체할 생성자가 없습니다.",
  "replace.constructor.builder.error.caret.position": "캐럿은 생성자를 빌더로 교체할 클래스 내부에 위치해야 합니다.",
  "replace.constructor.builder.error.no.constructor.chain": "{0}의 생성자는 단순한 체인을 형성하지 않습니다.",
  "replace.constructor.builder.error.class.with.chosen.name.already.exist": "{0} 클래스가 {1} 패키지에 이미 있습니다.",
  "replace.constructor.builder.error.selected.class.was.not.found": "기존 빌더 클래스 {0}을(를) 찾을 수 없습니다.",
  "replace.constructor.factory.error.invalid.factory.method.name": "''{0}''은(는) 유효한 팩터리 메서드 이름이 아닙니다",
  "replace.constructor.factory.error.factory.method.already.exists": "팩터리 메서드 {0}이(가) 이미 존재하며, 새로 만든 것 대신 사용됩니다.",
  "java.safe.delete.empty.callee.text": "호출된 측(Callee) 텍스트가 여기에 표시됩니다.",
  "java.safe.delete.caller.text": "호출 측(Caller) 텍스트가 호출된 측(callee)을 강조하여 여기에 표시됩니다.",
  "push.up.super.class.signature.conflict": "슈퍼 클래스의 {0}은(는) {1}의 {2} 메서드와 충돌합니다",
  "push.up.abstract.accessibility.in.subclass.conflict": "{0}은(는) 하위 클래스에서 접근할 수 없는 {1}을(를) 사용합니다.",
  "push.up.abstract.accessible.from.the.subclass.conflict": "{0}을(를) 하위 클래스에서 접근할 수 없기 때문에 추상화(abstract)로 만들 수 없습니다.",
  "push.down.unrelated.defaults.conflict": "{0}이(가) {1} 및 {2}에서 관련 없는 디폴트(defaults)를 상속합니다",
  "move.member.write.access.in.interface.conflict": "{0}에 쓰기(write)가 일어나지만, 인터페이스는 상수만 포함할 수 있습니다.",
  "dialog.message.enum.constant.0.won.t.be.compilable.in.1": "{0}을(를) {1}(으)로 이동하면 컴파일할 수 없습니다.",
  "dialog.message.non.constant.will.not.be.compilable.in.interface": "상수가 아닌 {0}은(는) 인터페이스로 이동하면 컴파일할 수 없습니다.",
  "dialog.message.static.class.initializers.are.not.allowed.in.interfaces": "인터페이스에서는 정적(static) 클래스 초기화가 허용되지 않습니다.",
  "refactor.only.current.method.choice": "현재 메서드만 리팩터링",
  "refactor.base.method.choice": "기본 {0, choice, 0#메서드|1#메서드} 리팩터링",
  "automatic.parameter.renamer.entity.name": "매개변수",
  "automatic.overload.renamer.entity.name": "오버로드",
  "extract.method.checkbox.annotate": "어노테이션",
  "extract.method.checkbox.make.static": "정적(static)으로 만들기",
  "extract.method.checkbox.make.static.and.pass.fields": "정적(static)으로 만들고 필드 전달",
  "extract.method.link.label.more.options": "옵션 더 보기",
  "extract.method.progress.search.duplicates": "중복 검색 중",
  "extract.method.progress.replace.duplicates": "중복 교체 중",
  "dialog.message.field.doesnt.have.initializer": "필드 {0}에 초기화자(initializer)가 없습니다"
}

ko_error_bundle = next((x for x in ko_data['new_files'] if x['filename'] == 'JavaRefactoringBundle.properties'), None)
ko_error_bundle['keys'].update(translations)
ko_error_bundle['key_count'] = len(ko_error_bundle['keys'])

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(ko_data, f, ensure_ascii=False, indent=2)

print("Updated JavaRefactoringBundle part 20")