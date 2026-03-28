import json

ko_dict = {
  "fork.mode.label": "포크 모드(&F):",
  "fork.mode.name": "포크 모드",
  "async.stack.trace.for.exceptions.name": "예외에 대한 비동기 스택 추적 인쇄",
  "repeat.label": "반복(&R):",
  "repeat.name": "반복",
  "repeat.count.label": "반복 횟수(&R):",
  "search.scope.name": "테스트 검색",
  "search.scope.project": "전체 프로젝트",
  "search.scope.module": "단일 모듈",
  "search.scope.module.deps": "모듈 종속성 전반",
  "test.group": "테스트",
  "category.label": "카테고리",
  "change.list.label": "변경 목록",
  "directory.label": "디렉터리",
  "pattern.label": "패턴",
  "tag.expression.label": "태그 표현식",
  "uniqueid.label": "고유 ID",
  "action.AddToISuite.text": "JUnit 패턴 모음에 추가",
  "action.excludeFromSuite.text": "모음에서 제외",
  "action.text.test.unknown.target": "알 수 없음",
  "action.text.test.category": "{0}의 테스트",
  "action.text.test.tags": "{0}의 테스트",
  "unused.declaration.junit.test.entry.point": "JUnit 테스트 케이스",
  "test.discovery.by.all.changes.combo.item": "전체",
  "module.does.not.exists": "''{1}'' 프로젝트에 ''{0}'' 모듈이 없습니다.",
  "junit.configuration.description": "JUnit 테스트 구성",
  "junit.configuration.class.label": "클래스(&C):",
  "no.pattern.error.message": "선택된 패턴이 없습니다.",
  "junit.configuration.method.label": "메서드(&E):",
  "default.junit.config.name.whole.project": "전체 프로젝트",
  "default.junit.config.name.all.in.module": "{0}의 전체",
  "default.junit.configuration.name": "<이름-없음>",
  "default.junit.config.name.all.in.package.in.module": "{1}의 {0}",
  "default.junit.config.name.temp.suite": "임시 모음",
  "default.junit.config.name.tags": "태그({0})",
  "default.junit.config.empty.category": "잘못됨",
  "default.junit.config.name.category": "@Category({0})",
  "junit.configuration.in.single.module.radio": "단일 모듈 내(&I)",
  "no.test.class.specified.error.text": "테스트 클래스가 지정되지 않았습니다.",
  "directory.not.found.error.message": "''{0}'' 디렉터리를 찾을 수 없습니다."
}

with open('missing_translations/missing_keys_korean.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

filename = "JUnitBundle.properties"
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
