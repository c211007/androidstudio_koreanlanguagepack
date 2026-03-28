import json

ko_dict = {
  "fix.add.argument.name.family": "인수에 이름 추가",
  "fix.add.argument.name.text.generic": "인수에 이름 추가…",
  "fix.add.argument.name.text": "인수에 이름 추가: ''{0}''",
  "fix.add.argument.name.step.choose.parameter.title": "매개변수 이름 선택",
  "fix.create.expect.actual": "expect / actual 선언 생성",
  "fix.create.missing.actual.members": "누락된 실제 멤버 추가",
  "fix.create.missing.actual.declarations": "누락된 실제 선언 추가",
  "fix.create.missing.actual.declarations.title": "누락된 실제 선언 추가",
  "fix.remove.mismatched.annotation.from.expect.declaration.may.change.semantics": "''expect'' 선언에서 불일치하는 주석 ''{0}'' 제거(의미 체계가 변경될 수 있음)",
  "fix.copy.mismatched.annotation.to.actual.declaration.may.change.semantics": "''expect''에서 ''actual'' 선언으로 불일치하는 주석 ''{0}'' 복사(의미 체계가 변경될 수 있음)",
  "fix.replace.mismatched.annotation.args.on.actual.declaration.may.change.semantics": "''actual'' 선언에서 불일치하는 주석 ''{0}''의 인수 대체(의미 체계가 변경될 수 있음)",
  "fix.replace.mismatched.annotation.args.on.expect.declaration.may.change.semantics": "''expect'' 선언에서 불일치하는 주석 ''{0}''의 인수 대체(의미 체계가 변경될 수 있음)",
  "fix.create.declaration.error": "{0} 생성 불가: {1}",
  "fix.create.declaration.error.inaccessible.type": "액세스할 수 없는 유형",
  "fix.create.declaration.error.some.types.inaccessible": "일부 유형에 액세스할 수 없습니다:",
  "fix.add.annotation.family": "주석 추가",
  "fix.add.annotation.text.self": "''@{0}'' 주석 추가",
  "fix.add.annotation.text.declaration": "''{1}''에 ''@{0}'' 주석 추가",
  "fix.add.annotation.text.containing.class": "포함하는 클래스 ''{1}''에 ''@{0}'' 주석 추가",
  "fix.add.annotation.text.containing.file": "포함하는 파일 ''{1}''에 ''@{0}'' 주석 추가",
  "fix.add.annotation.text.constructor": "생성자에 ''@{0}'' 주석 추가",
  "fix.opt_in.annotation.family": "옵트인 기능 사용 주석 처리",
  "fix.opt_in.text.use.statement": "문에 ''{0}'' 옵트인",
  "fix.opt_in.text.use.declaration": "''{1}''에 ''{0}'' 옵트인",
  "fix.opt_in.text.use.constructor": "생성자에 ''{0}'' 옵트인",
  "fix.opt_in.text.use.containing.class": "포함하는 클래스 ''{1}''에 ''{0}'' 옵트인",
  "fix.opt_in.text.use.containing.object": "포함하는 객체 ''{1}''에 ''{0}'' 옵트인",
  "fix.opt_in.text.use.containing.anonymous.object": "포함하는 객체에 ''{0}'' 옵트인",
  "fix.opt_in.text.use.containing.file": "포함하는 파일 ''{1}''에 ''{0}'' 옵트인",
  "fix.opt_in.text.use.module": "모듈 ''{1}''에 ''{0}'' 옵트인",
  "fix.opt_in.text.propagate.declaration": "''{0}'' 옵트인 요구 사항을 ''{1}''에 전파",
  "fix.opt_in.text.propagate.constructor": "''{0}'' 옵트인 요구 사항을 생성자에 전파",
  "fix.opt_in.text.propagate.containing.class": "''{0}'' 옵트인 요구 사항을 포함하는 클래스 ''{1}''에 전파",
  "fix.opt_in.text.propagate.containing.object": "''{0}'' 옵트인 요구 사항을 포함하는 객체 ''{1}''에 전파",
  "fix.opt_in.remove.all.forbidden.targets": "금지된 옵트인 주석 대상 제거",
  "fix.opt_in.remove.forbidden.retention": "금지된 옵트인 주석 보존 제거",
  "fix.opt_in.move.requirement.from.value.parameter.to.property": "값 매개변수에서 속성으로 ''{0}'' 옵트인 요구 사항 이동",
  "fix.opt_in.move.requirement.from.getter.to.property": "getter에서 속성으로 ''{0}'' 옵트인 요구 사항 이동",
  "fix.opt_in.migrate.experimental.annotation.replace": "더 이상 사용되지 않는 '@Experimental' 주석을 '@RequiresOptIn'으로 대체",
  "fix.opt_in.migrate.experimental.annotation.remove": "더 이상 사용되지 않는 '@Experimental' 주석 제거",
  "fix.replace.annotation.family": "주석 대체",
  "fix.replace.annotation.text": "주석을 ''@{0}''(으)로 대체",
  "fix.import": "가져오기",
  "fix.import.kind.0.name.1.and.name.2": "{0} ''{1}'', ''{2}'' 가져오기",
  "fix.import.kind.0.name.1.2": "{0} ''{1}''{2,choice,0#|1# 및 {2}개 더} 가져오기",
  "fix.import.question": "{0}을(를) 가져오시겠습니까?",
  "fix.import.kind.delegate.accessors": "위임 접근자 가져오기",
  "fix.import.kind.component.functions": "구성 요소 함수 가져오기",
  "fix.import.exclude": "자동 가져오기에서 ''{0}'' 제외",
  "fix.move.file.to.package.family": "패키지 일치 디렉터리로 파일 이동"
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

print(f"Updated {filename} (Keys 141-190)")

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
