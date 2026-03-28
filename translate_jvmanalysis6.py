import json

ko_dict = {
  "jvm.inspections.system.get.property.display.name": "'System.getProperty(str)' 호출을 단순화할 수 있음",
  "jvm.inspections.system.get.property.problem.descriptor": "''{0}''에 대해 <code>#ref</code> 호출을 단순화할 수 있습니다",
  "jvm.options.general.color.descriptor.logging.string.placeholder": " 로그 문자열//자리 표시자",
  "can.t.build.uast.tree.for.file": "파일에 대한 UAST 트리를 빌드할 수 없습니다.",
  "title.uast": "UAST",
  "current.version": "현재 버전",
  "dialog.title.choose.annotation": "{0} 선택",
  "jvm.inspections.dependency.intention.description": "범위 간의 종속성 규칙을 구성하기 위한 대화상자를 엽니다.",
  "jvm.class.filter.choose.calls": "유사한 로그 호출:",
  "inspection.suppression.annotation.display.name": "검사 억제 어노테이션",
  "inspection.suppression.annotation.problem.descriptor": "어노테이션이 {0}을(를) 억제함 #loc",
  "inspection.suppression.comment.problem.descriptor": "주석이 {0}을(를) 억제함 #loc",
  "ignored.suppressions": "무시된 억제:",
  "remove.suppress.comment.fix.family.name": "//{0} 제거",
  "allow.suppressions.fix.family.name": "억제 허용",
  "allow.suppressions.fix.text": "이러한 억제 허용",
  "group.advanced.settings.jvm": "JVM 언어",
  "advanced.setting.process.console.output.to.find.class.names": "터미널 출력을 처리하여 클래스 이름을 찾고 강조 표시",
  "inspection.empty.method.display.name": "빈 메서드",
  "inspection.empty.method.delete.quickfix": "불필요한 메서드 삭제",
  "inspection.empty.method.problem.descriptor": "메서드가 상위 메서드만 호출합니다.",
  "inspection.empty.method.problem.descriptor1": "빈 메서드가 빈 메서드를 재정의합니다.",
  "inspection.empty.method.problem.descriptor2": "메서드가 비어 있습니다.",
  "inspection.empty.method.problem.descriptor3": "메서드와 모든 파생 메서드가 비어 있습니다.",
  "inspection.empty.method.problem.descriptor4": "이 메서드의 모든 구현이 비어 있습니다.",
  "checkbox.comments.and.javadoc.count.as.content": "주석과 javadoc을 콘텐츠로 포함"
}

with open('missing_translations/missing_keys_korean.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

filename = "JvmAnalysisBundle.properties"
found = False
for file_entry in data.get('new_files', []):
    if file_entry['filename'] == filename:
        file_entry['keys'].update(ko_dict)
        found = True
        break
if not found:
    data.setdefault('new_files', []).append({"filename": filename, "keys": ko_dict})

print(f"Updated {filename} (Keys 201-226)")

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
