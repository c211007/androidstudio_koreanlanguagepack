import json

ko_dict = {
  "jvm.inspections.blocking.method.consider.suspend.context.non.blocking": "Kotlin 일시 중단 컨텍스트를 블로킹되지 않음으로 간주",
  "jvm.inspections.blocking.method.consider.unknown.context.nonblocking": "알 수 없는 컨텍스트를 블로킹되지 않음으로 간주",
  "jvm.inspections.api.no.extension.display.name": "클래스, 인터페이스 또는 메서드를 확장해서는 안 됨",
  "jvm.inspections.api.no.extension.class.description": "''{0}'' 클래스를 확장해서는 안 됩니다.",
  "jvm.inspections.api.no.extension.interface.implement.description": "''{0}'' 인터페이스를 구현해서는 안 됩니다.",
  "jvm.inspections.api.no.extension.interface.extend.description": "''{0}'' 인터페이스를 확장해서는 안 됩니다.",
  "jvm.inspections.api.no.extension.method.overriding.description": "''{0}'' 메서드를 재정의해서는 안 됩니다.",
  "jvm.inspections.api.no.extension.on.invalid.target.method.description": "''{0}'' 메서드가 ''@ApiStatus.NonExtendable''(으)로 표시되어 있지만 재정의할 수 없습니다.",
  "jvm.inspections.api.no.extension.on.redundant.target.method.description": "'@ApiStatus.NonExtendable' 어노테이션이 중복됩니다.",
  "jvm.inspections.api.no.extension.on.invalid.target.class.description": "{0} ''{1}''이(가) ''@ApiStatus.NonExtendable''(으)로 표시되어 있지만 확장할 수 없습니다.",
  "jvm.inspections.api.override.only.display.name": "메서드를 재정의할 수만 있음",
  "jvm.inspections.api.override.only.description": "''{0}'' 메서드를 재정의할 수만 있습니다.",
  "jvm.inspections.api.override.only.on.invalid.method.description": "''{0}'' 메서드가 ''@ApiStatus.OverrideOnly''(으)로 표시되어 있지만 재정의할 수 없습니다.",
  "jvm.inspections.api.override.only.on.invalid.method.redundant.description": "'@ApiStatus.OverrideOnly' 어노테이션이 중복됩니다.",
  "jvm.inspections.api.override.only.on.invalid.class.description": "{0} ''{1}''이(가) ''@ApiStatus.OverrideOnly''(으)로 표시되어 있지만 확장하거나 자의 메서드를 재정의할 수 없습니다.",
  "jvm.inspections.equals.hashcode.called.on.url.display.name": "'URL' 객체에서 'equals()' 또는 'hashCode()' 호출",
  "jvm.inspections.equals.hashcode.called.on.url.problem.descriptor": "URL 객체에서 ''{0}'' 호출",
  "jvm.inspections.collection.contains.url.problem.descriptor": "''{0}''에는 URL 객체가 포함될 수 있습니다. #loc",
  "jvm.inspections.dependency.display.name": "잘못된 패키지 종속성",
  "jvm.inspections.dependency.edit.rules.text": "\"{0}\" 종속성 규칙 편집",
  "jvm.inspections.dependency.edit.rules.family": "종속성 규칙 편집",
  "jvm.inspections.dependency.violator.problem.descriptor": "''{0}.'' 종속성 규칙을 위반했습니다.",
  "jvm.inspections.dependency.on.internal.display.name": "내부 패키지에 대한 잘못된 종속성",
  "inspection.message.illegal.dependency.module.doesn.t.export": "잘못된 종속성: ''{0}'' 모듈이 ''{1}'' 패키지를 내보내지 않습니다.",
  "jvm.inspections.source.to.sink.flow.display.name": "안전하지 않은 문자열이 안전한 메서드에 전달됨",
  "jvm.inspections.source.to.sink.flow.passed.unsafe": "안전하지 않은 문자열이 안전한 매개변수로 사용되었습니다.",
  "jvm.inspections.source.to.sink.flow.passed.unknown": "알 수 없는 문자열이 안전한 매개변수로 사용되었습니다.",
  "jvm.inspections.source.to.sink.flow.returned.unsafe": "안전한 메서드에서 안전하지 않은 문자열이 반환되었습니다.",
  "jvm.inspections.source.to.sink.flow.returned.unknown": "안전한 메서드에서 알 수 없는 문자열이 반환되었습니다.",
  "jvm.inspections.source.to.sink.flow.assigned.unsafe": "안전하지 않은 문자열이 안전한 변수에 할당되었습니다.",
  "jvm.inspections.source.to.sink.flow.assigned.unknown": "알 수 없는 문자열이 안전한 변수에 할당되었습니다.",
  "jvm.inspections.source.to.sink.flow.common.unsafe": "안전하지 않은 문자열이 안전한 컨텍스트에서 사용되었습니다.",
  "jvm.inspections.source.to.sink.flow.common.unknown": "알 수 없는 문자열이 안전한 컨텍스트에서 사용되었습니다.",
  "jvm.inspections.source.to.sink.flow.too.complex": "컨텍스트가 안전한지 확인하기에 문자열이 너무 복잡합니다.",
  "jvm.inspections.source.unsafe.to.sink.flow.mark.as.safe.family": "유효성 검사가 필요한 것으로 표시",
  "jvm.inspections.source.unsafe.to.sink.flow.mark.as.safe.text": "요소를 유효성 검사가 필요한 것으로 표시",
  "jvm.inspections.source.unsafe.to.sink.flow.mark.as.safe.command.name": "유효성 검사가 필요한 것으로 표시",
  "jvm.inspections.source.unsafe.to.sink.flow.preview": "'@Untainted' 어노테이션 추가",
  "jvm.inspections.source.unsafe.to.sink.flow.config": "''{0}'' 요소에 대한 검사 설정에 유효하지 않은 어노테이션이 추가됩니다.",
  "jvm.inspections.source.unsafe.to.sink.flow.impossible": "''{0}'' 요소에 대해서는 Untainted 어노테이션이 지원되지 않습니다. 요소는 건너뜁니다."
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

print(f"Updated {filename} (Keys 41-80)")

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
