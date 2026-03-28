import json

ko_dict = {
  "convert.to.object.declaration": "object 선언으로 변환",
  "comment": "주석",
  "expression": "표현식",
  "statement": "문",
  "class": "클래스",
  "top.level": "최상위",
  "rethrow.stored.pce.as.a.new.runtime.exception": "저장된 PCE를 새 런타임 예외로 다시 발생(rethrow)",
  "internal.toggle.throwing.cached.pce.title": "내부: 캐시된 PCE 예외 던지기 전환",
  "minimal.line.count": "최소 줄 수",
  "files.to.visit": "방문할 파일",
  "random.seed": "무작위 시드",
  "number.of.attempts.then.files.in.project.0": "시도 횟수 > 프로젝트 내 파일 순, {0}",
  "text.done": "완료",
  "file.lines": "파일 줄",
  "max.functions.to.visit": "방문할 최대 함수 수",
  "move.refactoring.testing": "이동 리팩터링 테스트",
  "compiling.project": "프로젝트 컴파일 중\\u2026",
  "saving.files": "파일 저장 중\\u2026",
  "perform.refactoring": "리팩터링 수행 중\\u2026",
  "update.indices": "인덱스 업데이트 중\\u2026",
  "reset.files": "파일 재설정 중\\u2026",
  "cannot.get.or.create.results.file": "결과 파일을 가져오거나 만들 수 없습니다.",
  "cannot.get.project.root.directory": "프로젝트 루트 디렉터리를 가져올 수 없습니다.",
  "0.try.1.with.2.fails.and.3.verifications": "{0} [{1}번째 시도, {2} 실패, {3} 검증]",
  "test.result.log.file.will.be.placed.here": "여기에 테스트 결과 로그 파일이 배치됩니다.",
  "maximum.count.of.applied.refactoring.before.validity.check": "유효성 검사 전에 적용된 최대 리팩터링 횟수",
  "move.refactoring.test": "이동 리팩터링 테스트",
  "resolve.pasted.references": "붙여넣은 참조 확인(resolve)",
  "create.kotlin.file": "Kotlin 파일 생성",
  "type.alias.0": "타입 별칭 \"{0}\"",
  "type.parameter.0": "타입 매개변수 \"{0}\"",
  "parameter.0": "매개변수 \"{0}\"",
  "property.0": "속성 \"{0}\"",
  "function.01": "함수 \"{0}\"",
  "object.0": "객체 \"{0}\"",
  "interface": "인터페이스",
  "constructor": "생성자",
  "move.reference.into.parentheses": "참조를 괄호 안으로 이동",
  "local.variable": "지역 변수",
  "const.property": "const 속성",
  "private.property": "private 속성",
  "object.or.top.level.property": "객체 또는 최상위 속성",
  "object.private.property": "객체 private 속성",
  "property": "속성",
  "test.function": "테스트 함수",
  "function": "함수",
  "enum.entry": "enum 항목",
  "create.subclass": "하위 클래스 만들기",
  "implement.sealed.class": "sealed 클래스 구현",
  "implement.abstract.class": "abstract 클래스 구현"
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

print(f"Updated {filename} (Keys 1591-1640)")

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
