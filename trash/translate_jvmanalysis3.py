import json

ko_dict = {
  "jvm.inspections.source.unsafe.to.sink.flow.preview.propagate": "전파 트리 표시",
  "jvm.inspections.source.unsafe.to.sink.flow.propagate.safe.family": "전파 트리",
  "jvm.inspections.source.unsafe.to.sink.flow.propagate.safe.text": "여기에서 전파 트리 표시",
  "jvm.inspections.source.unsafe.to.sink.flow.propagate.safe.preview": "안전한 어노테이션의 전파를 확인할 수 있는 도구 창을 엽니다.",
  "jvm.inspections.source.unsafe.to.sink.flow.propagate.safe.toolwindow.title": "안전하지 않은 멤버",
  "jvm.inspections.source.unsafe.to.sink.flow.propagate.safe.toolwindow.annotate": "제외된 항목 이외 모두 어노테이션 지정",
  "jvm.inspections.source.unsafe.to.sink.flow.propagate.safe.toolwindow.unsafe.flow": "안전하지 않은 흐름",
  "propagated.from": "전파 원인:",
  "propagated.to": "전파 대상:",
  "jvm.inspections.source.unsafe.to.sink.flow.qualifier.cleaner.arguments": "인수",
  "jvm.inspections.source.unsafe.to.sink.flow.qualifier.cleaner.classes": "클래스",
  "jvm.inspections.source.unsafe.to.sink.flow.qualifier.cleaner.methods": "메서드",
  "jvm.inspections.source.unsafe.to.sink.flow.qualifier.cleaner.table": "한정자를 정리할 메서드:",
  "jvm.inspections.source.unsafe.to.sink.flow.qualifier.cleaner.comment": "이러한 메서드는 한정자를 'untainted'로 표시합니다(인수는 쉼표로 분리해야 함).",
  "jvm.inspections.source.unsafe.to.sink.flow.untainted.parameters": "오염되지 않은 매개변수:",
  "jvm.inspections.source.unsafe.to.sink.flow.untainted.parameters.comment": "이 매개변수에는 '@Untainted' 어노테이션이 있는 것으로 간주됩니다.",
  "jvm.inspections.source.unsafe.to.sink.flow.tainted.parameters": "오염된 매개변수:",
  "jvm.inspections.source.unsafe.to.sink.flow.tainted.parameters.comment": "이 매개변수에는 '@Tainted' 어노테이션이 있는 것으로 간주됩니다.",
  "jvm.inspections.source.unsafe.to.sink.flow.index.parameter": "매개변수 색인",
  "jvm.inspections.source.unsafe.to.sink.flow.place.class.column.title": "컨텍스트의 클래스 이름",
  "jvm.inspections.source.unsafe.to.sink.flow.place.method.column.title": "컨텍스트의 메서드 이름 정규식",
  "jvm.inspections.source.unsafe.to.sink.flow.not.number": "숫자가 아님",
  "jvm.inspections.source.unsafe.to.sink.flow.tainted.annotations": "오염된 어노테이션:",
  "jvm.inspections.source.unsafe.to.sink.flow.tainted.annotations.comment": "이 어노테이션은 분석 중에 '@Tainted' 어노테이션으로 사용됩니다.",
  "jvm.inspections.source.unsafe.to.sink.flow.untainted.annotations": "오염되지 않은 어노테이션:",
  "jvm.inspections.source.unsafe.to.sink.flow.untainted.annotations.comment": "이 어노테이션은 분석 중에 '@Untainted' 어노테이션으로 사용됩니다. 이 목록의 첫 번째 어노테이션이 클래스 경로에 있는 경우 전파에 사용됩니다.",
  "jvm.inspections.source.unsafe.to.sink.flow.untainted.methods": "오염되지 않은 메서드:",
  "jvm.inspections.source.unsafe.to.sink.flow.untainted.methods.comment": "이 메서드는 안전한 객체만 반환하는 것으로 간주됩니다.",
  "jvm.inspections.source.unsafe.to.sink.flow.tainted.methods": "오염된 메서드:",
  "jvm.inspections.source.unsafe.to.sink.flow.tainted.methods.comment": "이 메서드는 안전하지 않은 객체만 반환하는 것으로 간주됩니다.",
  "jvm.inspections.source.unsafe.to.sink.flow.untainted.fields": "오염되지 않은 필드:",
  "jvm.inspections.source.unsafe.to.sink.flow.untainted.fields.comment": "이 필드에는 안전한 객체만 포함된 것으로 간주됩니다.",
  "jvm.inspections.source.unsafe.to.sink.flow.untainted.fields.name": "필드 이름",
  "jvm.inspections.source.unsafe.to.sink.flow.safe.class": "안전한 클래스:",
  "jvm.inspections.source.unsafe.to.sink.flow.safe.class.comment": "이 클래스에는 안전하지 않은 데이터가 포함될 수 없습니다.",
  "jvm.inspections.source.unsafe.to.sink.flow.untainted.process.as.qualifier.arguments": "수신자와 인수가 오염되지 않은 경우 외부 메서드가 오염되지 않은 것으로 간주",
  "jvm.inspections.source.unsafe.to.sink.flow.untainted.process.as.qualifier.arguments.comment": "이 옵션을 활성화하면 외부 메서드의 수신자와 인수가 안전한 경우 현재 클래스 외부의 외부 메서드를 안전한 것으로 간주합니다. 일부 경우에는 적용할 수 없지만 상태 비저장 클래스에는 유용할 수 있습니다. 그렇지 않으면 모든 외부 메서드가 안전하지 않은 것으로 간주됩니다.",
  "jvm.inspections.source.unsafe.to.sink.flow.check.warn.if.complex": "확인하기에 사례가 너무 복잡한 경우 보고",
  "jvm.inspections.source.unsafe.to.sink.flow.show.unknown.object": "알 수 없는 객체 보고",
  "jvm.inspections.source.unsafe.to.sink.flow.show.unsafe.object": "안전하지 않은 객체 보고"
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

print(f"Updated {filename} (Keys 81-120)")

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
