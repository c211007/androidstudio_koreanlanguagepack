import json

ko_dict = {
  "add.constructor.parameters.from.superclass": "상위 클래스에서 생성자 매개변수 추가",
  "surround.with.array.of": "arrayOf(...)로 묶기",
  "surround.with.star.0": "*{0}(...)로 묶기",
  "surround.with.0": "{0}(...)로 묶기",
  "surround.with.lambda": "람다로 묶기",
  "surround.with.null.check": "null 검사로 묶기",
  "convert.too.long.character.literal.to.string": "너무 긴 문자 리터럴을 문자열로 변환",
  "replace.array.of.boxed.with.array.of.primitive": "boxed 배열을 기본형 배열로 바꾸기",
  "migrate.unsupported.yield.syntax": "지원되지 않는 yield 구문 마이그레이션",
  "wrap.with": "[]로 묶기",
  "wrap.with.array.literal": "배열 리터럴로 묶기",
  "wrap.with.collection.literal.call": "컬렉션 리터럴 호출로 묶기",
  "wrap.element.with.0.call": "요소를 ''{0}()'' 호출로 묶기",
  "replace.with.0.call": "''{0}()'' 호출로 바꾸기",
  "wrap.with.let.call": "'?.let { ... }' 호출로 묶기",
  "change.to.0": "''{0}''(으)로 변경",
  "change.to.correct.long.suffix.l": "올바른 long 접미사 'L'로 변경",
  "change.to.correct.primitive.type": "올바른 기본 유형으로 변경",
  "0.from.1": "{1}의 {0}",
  "checking.data.classes": "데이터 클래스 확인 중",
  "checking.data.class.0.of.1": "데이터 클래스 확인 중: {1} 중 {0}\\u2026",
  "difference.found.for.data.class.0.found.1.2": "데이터 클래스 {0}에 대한 차이가 발견되었습니다. {1}개의 사용 항목이 발견되었지만 {2}개가 예상되었습니다.",
  "title.error": "오류",
  "analyzed.0.classes.no.difference.found": "{0}개의 클래스를 분석했습니다. 차이가 없습니다.",
  "title.success": "성공",
  "can.t.finish.while.indexing.is.in.progress": "인덱싱이 진행 중인 동안에는 완료할 수 없습니다.",
  "progress.finding.implicit.nothing.s": "암시적 nothing 검색 중",
  "scanning.files.0.fo.1.file.2.occurrences.found": "파일 검색 중: {1} 파일 중 {0}. {2}개의 발생 항목 발견",
  "implicit.nothing.s": "암시적 Nothing",
  "not.found.in.0.files": "{0}개 파일에서 찾을 수 없습니다.",
  "titile.not.found": "찾을 수 없음",
  "search.for.not.property.candidates": "속성이 아닌 후보 검색",
  "enter.package.fqname": "패키지 FqName 입력",
  "searching.for.not.property.candidates": "속성이 아닌 후보 검색 중",
  "step.1.collecting.0.1.2": "1단계: 수집 중 {0}:{1}:{2}",
  "step.2.0.of.1": "2단계: {1} 중 {0}",
  "step.3.0.of.1": "3단계: {1} 중 {0}",
  "title.done": "완료",
  "revert.applied.imports.command": "적용된 가져오기 되돌리기",
  "delete.0": "{0} 삭제",
  "replace.if.expression.with.elvis.expression": "'if' 표현식을 엘비스 표현식으로 바꾸기",
  "report.also.on.statement": "문에 대해서도 보고",
  "if.then.foldable.to": "If-Then을 '?:'로 접을 수 있음",
  "replace.if.expression.with.safe.access.expression": "'if' 표현식을 안전한 액세스 표현식으로 바꾸기",
  "remove.redundant.if.expression": "중복 'if' 표현식 제거",
  "replace.if.expression.with.safe.cast.expression": "'if' 표현식을 안전한 캐스트 표현식으로 바꾸기",
  "simplify.foldable.if.then": "접을 수 있는 if-then 간소화",
  "foldable.if.then": "접을 수 있는 if-then",
  "introduce.when.subject": "'when' 주체(subject) 도입",
  "when.with.subject.should.be.used": "주체(subject)가 있는 'when'을 사용해야 합니다."
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

print(f"Updated {filename} (Keys 1041-1090)")

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
