import json

ko_dict = {
  "text.0.to.inline": "인라인할 {0}",
  "text.0.uses.1.which.is.not.accessible.from.2": "{0}이(가) {2}에서 접근할 수 없는 {1}을(를) 사용합니다.",
  "text.0.uses.1.which.will.be.inaccessible.after.move": "{0}이(가) 이동 후에 접근할 수 없는 {1}을(를) 사용합니다.",
  "text.0.uses.1.which.will.not.be.accessible.from.subclass": "{0}이(가) 하위 클래스에서 접근할 수 없는 {1}을(를) 사용합니다.",
  "text.0.uses.internal.1.which.will.be.inaccessible.after.move": "{0}이(가) 이동 후에 접근할 수 없는 내부 {1}을(를) 사용합니다.",
  "text.0.will.be.shadowed.by.1": "{0}이(가) {1}에 의해 가려집니다.",
  "text.0.will.clash.with.existing.1.in.2": "이름 변경 후 {0}이(가) {2}의 기존 {1}과(와) 충돌합니다.",
  "text.0.will.no.longer.be.accessible.after.signature.change": "{0}은(는) 서명 변경 후 더 이상 접근할 수 없습니다.",
  "text.all.declarations.must.belong.to.the.same.directory.or.class": "모든 선언은 동일한 디렉터리 또는 클래스에 속해야 합니다.",
  "text.anonymous": "[익명]",
  "text.at.least.one.file.must.be.selected": "하나 이상의 멤버를 선택해야 합니다.",
  "text.callee.text.would.be.shown.here": "호출 수신자 텍스트가 여기에 표시됩니다.",
  "text.caller.text.with.highlighted.callee.call.would.be.shown.here": "호출 수신자 호출이 강조 표시된\\n호출자 텍스트가 여기에 표시됩니다.",
  "text.cannot.create.target.directory.0": "대상 디렉터리 {0}을(를) 만들 수 없습니다.",
  "text.cannot.determine.source.directory": "소스 디렉터리를 확인할 수 없습니다.",
  "text.cannot.find.package.corresponding.to.0": "{0}에 해당하는 패키지를 찾을 수 없습니다.",
  "text.cannot.find.target.package.name": "대상 패키지 이름을 찾을 수 없습니다.",
  "text.cannot.move.for.current.project": "현재 프로젝트를 이동할 수 없습니다.",
  "text.cannot.move.inner.class.0.into.itself": "중첩 클래스 {0}을(를) 자체로 이동할 수 없습니다.",
  "text.cannot.move.to.original.file": "원래 파일로 이동할 수 없습니다.",
  "text.cannot.move.expect.actual.declaration.to.file": "expect/actual 선언을 파일로 이동할 수 없습니다.",
  "text.change.file.package.to.0": "파일의 패키지를 ''{0}''(으)로 변경",
  "text.choose.containing.file": "포함하는 파일 선택",
  "text.class.0.already.contains.member.1": "{0}에 이미 {1}이(가) 포함되어 있습니다.",
  "text.class.0.already.exists.in.package.1": "패키지 {1}에 {0} 클래스가 이미 존재합니다.",
  "text.class.0.already.exists.in.the.target.scope": "대상 범위에 {0} 클래스가 이미 존재합니다.",
  "text.class.0.is.final": "{0}이(가) final입니다.",
  "text.constructor": "생성자",
  "text.convert._it_.to.explicit.lambda.parameter": "'it'을 명시적 람다 매개변수로 변환",
  "text.create.destructuring.declaration": "구조 분해 선언 만들기",
  "text.create.single.variable": "단일 변수 만들기",
  "text.declaration": "선언",
  "text.declarations.clash.move.0.destination.1.declared.in.scope.2": "다음 선언이 충돌합니다: 범위 {2}에 선언된 이동할 {0} 및 대상 {1}",
  "text.default.value": "\\ // 기본값 = {0}",
  "text.destination.class.should.be.kotlin.class": "대상 클래스는 Kotlin 클래스여야 합니다.",
  "text.do.you.want.to.rename.0.as.well": "{0}()의 이름도 바꾸시겠습니까?",
  "text.do.you.want.to.rename.base.property.from.0": "{0}에서 기본 속성의 이름을 바꾸시겠습니까?",
  "text.do.you.want.to.rename.base.property": "기본 속성의 이름을 바꾸시겠습니까?",
  "text.duplicating.local.variable": "지역 변수 ''{0}'' 중복 중",
  "text.duplicating.parameter": "매개변수 ''{0}'' 중복 중",
  "text.duplicating.property": "속성 ''{0}'' 중복 중",
  "change.signature.conflict.text.kotlin.default.value.in.non.kotlin.files": "기본 Kotlin 호출 값이 다른 언어에서 잘못된 코드로 이어질 수 있습니다.",
  "change.signature.conflict.text.kotlin.default.parameter.in.non.kotlin.files": "기본 매개변수가 다른 언어에서 지원되지 않을 수 있습니다.",
  "text.explicit.receiver.is.already.present.in.call.element.0": "호출 요소에 명시적 수신자가 이미 존재합니다: {0}",
  "text.extract.superclass": "상위 클래스 추출",
  "text.file.0.already.exists.in.1": "{1}에 {0} 파일이 이미 존재합니다.",
  "text.file.name.cannot.be.empty": "파일 이름은 비워둘 수 없습니다.",
  "text.function.already.exists": "함수가 이미 존재합니다: ''{0}''",
  "text.function.in.ticks.0": "함수 ''{0}''",
  "text.function": "함수"
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

print(f"Updated {filename} (Keys 691-740)")

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
