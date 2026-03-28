import json

ko_dict = {
  "jvm.inspections.group.name": "JVM 언어",
  "jvm.inspections.test.frameworks.group.name": "테스트 프레임워크",
  "jvm.inspections.logging.frameworks.group.name": "로깅",
  "jvm.inspections.unstable.api.usage.display.name": "불안정한 API 사용",
  "jvm.inspections.unstable.api.usage.annotations.list": "불안정한 API 어노테이션:",
  "jvm.inspections.unstable.api.usage.ignore.inside.imports": "가져오기 내 무시",
  "jvm.inspections.unstable.api.usage.ignore.declared.inside.this.project": "이 프로젝트에 선언된 API 무시",
  "jvm.inspections.unstable.api.usage.api.is.marked.unstable.itself": "''{0}''이(가) @{1}(으)로 불안정하게 표시되었습니다.",
  "jvm.inspections.unstable.api.usage.api.is.declared.in.unstable.api": "''{0}''은(는) @{3}(으)로 표시된 불안정한 {1} ''{2}''에 선언되었습니다.",
  "jvm.inspections.unstable.api.usage.overridden.method.is.marked.unstable.itself": "재정의된 ''{0}'' 메서드가 @{1}(으)로 불안정하게 표시되었습니다.",
  "jvm.inspections.unstable.api.usage.overridden.method.is.declared.in.unstable.api": "재정의된 ''{0}'' 메서드는 @{3}(으)로 표시된 불안정한 {1} ''{2}''에 선언되었습니다.",
  "jvm.inspections.unstable.api.usage.unstable.type.is.used.in.signature.of.referenced.api": "''{0}''의 시그니처가 @{3}(으)로 표시된 불안정한 {1} ''{2}''을(를) 참조하므로 불안정합니다.",
  "jvm.inspections.usages.of.obsolete.api.display.name": "ApiStatus.@Obsolete의 사용",
  "jvm.inspections.usages.of.obsolete.api.description": "오래된 API가 사용되었습니다.",
  "jvm.inspections.scheduled.for.removal.future.version": "향후 버전",
  "jvm.inspections.scheduled.for.removal.predefined.version": "버전 {0}",
  "jvm.inspections.scheduled.for.removal.api.is.marked.itself": "''{0}''은(는) {1}에서 제거될 예정입니다.",
  "jvm.inspections.scheduled.for.removal.api.is.declared.in.marked.api": "''{0}''은(는) {3}에서 제거될 예정인 {1} ''{2}''에 선언되었습니다.",
  "jvm.inspections.scheduled.for.removal.method.overridden.marked.itself": "재정의된 ''{0}'' 메서드는 {1}에서 제거될 예정입니다.",
  "jvm.inspections.scheduled.for.removal.method.overridden.declared.in.marked.api": "재정의된 ''{0}'' 메서드는 {3}에서 제거될 예정인 {1} ''{2}''에 선언되었습니다.",
  "jvm.inspections.scheduled.for.removal.scheduled.for.removal.type.is.used.in.signature.of.referenced.api": "''{0}''의 시그니처가 {3}에서 제거될 예정인 {1} ''{2}''을(를) 참조하므로 제거될 예정입니다.",
  "jvm.inspections.unstable.type.used.in.signature.display.name": "불안정한 유형이 시그니처에서 사용되었습니다.",
  "jvm.inspections.unstable.type.used.in.class.signature.description": "클래스의 선언이 불안정한 ''{1}'' 유형을 참조하므로 ''@{0}'' 어노테이션으로 표시해야 합니다.",
  "jvm.inspections.unstable.type.used.in.method.signature.description": "메서드의 시그니처가 불안정한 ''{1}'' 유형을 참조하므로 ''@{0}'' 어노테이션으로 표시해야 합니다.",
  "jvm.inspections.unstable.type.used.in.field.signature.description": "필드의 유형이 불안정한 ''{1}'' 유형을 참조하므로 ''@{0}'' 어노테이션으로 표시해야 합니다.",
  "jvm.inspections.missing.deprecated.annotation.on.scheduled.for.removal.api.display.name": "제거될 예정인 API에 '@Deprecated' 어노테이션 누락됨",
  "jvm.inspections.missing.deprecated.annotation.on.scheduled.for.removal.api.description": "제거될 예정인 API도 '@Deprecated' 어노테이션으로 표시해야 합니다.",
  "jvm.inspections.must.already.be.removed.api.display.name": "API가 이미 제거되었어야 합니다.",
  "jvm.inspections.must.already.be.removed.api.earlier.version.description": "API가 버전 {0}에 제거되었어야 하는데 현재 버전은 {1}입니다.",
  "jvm.inspections.must.already.be.removed.api.current.version.description": "API가 현재 버전인 {0}에서 제거되어야 합니다.",
  "jvm.inspections.blocking.method.problem.descriptor": "블로킹되지 않는 컨텍스트에서 블로킹 가능성이 있는 호출로 인해 스레드 기아가 발생할 수 있습니다.",
  "jvm.inspections.blocking.method.problem.wildcard.descriptor": "{0}에서 블로킹 가능성이 있는 호출로 인해 스레드 기아가 발생할 수 있습니다.",
  "jvm.inspections.blocking.method.in.implicit.ctr.problem.descriptor": "블로킹되지 않는 컨텍스트의 암시적 생성자 호출에서 블로킹 가능성이 있는 호출로 인해 스레드 기아가 발생할 수 있습니다.",
  "jvm.inspections.blocking.method.in.implicit.ctr.problem.wildcard.descriptor": "{0}의 암시적 생성자 호출에서 블로킹 가능성이 있는 호출로 인해 스레드 기아가 발생할 수 있습니다.",
  "jvm.inspections.blocking.method.display.name": "블로킹되지 않는 컨텍스트에서 발생할 수 있는 블로킹 호출",
  "jvm.inspections.blocking.method.annotation.blocking": "블로킹 어노테이션:",
  "jvm.inspections.blocking.method.annotation.non-blocking": "논블로킹 어노테이션:",
  "jvm.inspections.blocking.method.annotation.configure.add.blocking.title": "블로킹 어노테이션 추가",
  "jvm.inspections.blocking.method.annotation.configure.add.non-blocking.title": "논블로킹 어노테이션 추가",
  "jvm.inspections.blocking.method.consider.unknown.context.blocking": "알 수 없는 컨텍스트를 블로킹으로 간주"
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

print(f"Updated {filename} (Keys 1-40)")

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
