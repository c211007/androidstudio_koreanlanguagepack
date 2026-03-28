import json

ko_dict = {
  "group.names.gradle": "Gradle",
  "group.path.kotlin.migration": "Kotlin,마이그레이션",
  "group.names.java.interop.issues": "Java 상호 운용성 문제",
  "group.names.kotlin": "Kotlin",
  "group.names.logging": "로깅",
  "group.names.naming.conventions": "명명 규칙",
  "group.names.maven": "Maven",
  "group.names.migration": "마이그레이션",
  "group.names.other.problems": "기타 문제",
  "group.names.probable.bugs": "발생 가능한 버그",
  "group.names.redundant.constructs": "중복 생성자",
  "group.names.style.issues": "스타일 문제",
  "group.names.code.migration": "코드 마이그레이션",
  "group.names.numeric.issues": "숫자 문제",
  "fix.insert.delegation.call": "''{0}()'' 호출 삽입",
  "fix.introduce.non.null.assertion.family": "Null이 아닌 것으로 어설션된 호출 추가",
  "fix.introduce.non.null.assertion.text": "Null이 아닌 것으로 어설션된({0}!!) 호출 추가",
  "fix.remove.non.null.assertion": "불필요한 Non-Null 어설션(!!) 제거",
  "fix.add.annotation.target": "주석 타겟 추가",
  "progress.looking.up.add.annotation.usage": "주석 사용 찾는 중…",
  "fix.add.constructor.parameter": "생성자 매개변수 ''{0}'' 추가",
  "fix.make.data.class": "''{0}'' 데이터 클래스로 만들기",
  "fix.add.default.constructor": "'expect' 클래스에 기본 생성자 추가",
  "fix.add.explicit.import": "명시적 가져오기 추가",
  "fix.add.function.body": "함수 본문 추가",
  "fix.use.fully.qualified.call": "정규화된 호출 사용",
  "wrap.argument.with.parentheses": "괄호로 인수 래핑",
  "fix.add.is.to.when": "''{0}'' 앞에 ''is'' 추가",
  "fix.add.new.line.after.annotations": "주석 다음에 새 줄 추가",
  "fix.make.type.parameter.reified": "{0}을(를) 구체화하고 {1}을(를) 인라인으로 만들기",
  "fix.add.return.last.expression": "마지막 표현식에 'return' 추가",
  "fix.add.return.before.expression": "표현식 앞에 'return' 추가",
  "fix.add.return.before.lambda.expression": "람다 표현식 앞에 'run' 추가",
  "fix.add.semicolon.lambda.expression": "선행 호출을 세미콜론으로 종료",
  "fix.add.spread.operator.after.sam": "'vararg'로 전달되는 배열 앞에 스프레드 연산자 추가",
  "fix.add.else.branch.when": "else 분기 추가",
  "fix.replace.with.assign.function.call": "''{0}'' 호출로 대체",
  "fix.assign.to.property": "속성에 할당",
  "fix.change.mutability.change.to.val": "''{0}''을(를) val로 변경",
  "fix.change.type.argument": "유형 인수를 {0}(으)로 변경"
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

print(f"Updated {filename} (Keys 1-40)")

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
