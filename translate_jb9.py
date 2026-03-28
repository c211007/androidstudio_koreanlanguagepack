import json
import os

file_path = 'missing_translations/missing_keys_korean.json'
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

bundle_name = 'JavaBundle.properties'
translations = {
    'inspection.redundant.unmodifiable.call.description': '수정할 수 없는(unmodifiable) 컬렉션 래퍼의 중복 사용',
    'inspection.redundant.unmodifiable.call.unwrap.argument.quickfix': '인자 래핑 해제(Unwrap)',
    'completion.override.implement.methods': '메서드 재정의/구현(Override/Implement)…',
    'lambda.tree.node.presentation': '람다(Lambda)',
    'inspection.meaningless.record.annotation.description': '의미 없는 레코드 어노테이션',
    'inspection.meaningless.record.annotation.message.method.and.parameter': '어노테이션이 영향을 미치지 않음: 대상이 METHOD 및 PARAMETER이지만 접근자(accessor)와 표준(canonical) 생성자가 모두 명시적으로 선언되었습니다',
    'inspection.meaningless.record.annotation.message.method': '어노테이션이 영향을 미치지 않음: 대상이 METHOD이지만 해당 접근자(accessor)가 명시적으로 선언되었습니다',
    'inspection.meaningless.record.annotation.message.parameter': '어노테이션이 영향을 미치지 않음: 대상이 PARAMETER이지만 표준(canonical) 생성자가 명시적으로 선언되었습니다',
    'header.method.to.be.converted': '변환할 메서드',
    'accessible.name.change.modifier': '제어자(Modifier) 변경',
    'usages.telescope': '{0,choice, 0#사용 위치 없음|1#사용 위치 1개|2#사용 위치 {0,number}개}',
    'label.jvm.method.name': 'JVM 메서드 이름',
    'label.jvm.field.name': 'JVM 필드 이름',
    'label.jvm.class.name': 'JVM 클래스 이름',
    'link.configure.classes.excluded.from.completion': '코드 완성(completion)에서 제외된 클래스 구성',
    'progress.title.detect.overridden.methods': '재정의하는(overriding) 메서드 확인',
    'intention.name.iterate.over': '{0}에 대해 반복(Iterate)',
    'advanced.settings.group.compiler': '컴파일러(Compiler)',
    'advanced.setting.compiler.lower.process.priority': '더 낮은 우선순위로 컴파일 실행',
    'advanced.setting.compiler.lower.process.priority.description': 'Windows의 경우 IDLE 우선순위로, Linux/macOS의 경우 nice 수준을 10으로 설정하여 외부 JPS 프로세스를 실행합니다.',
    'advanced.setting.compiler.automake.allow.when.app.running': '개발된 애플리케이션이 현재 실행 중이더라도 auto-make를 시작하도록 허용',
    'advanced.setting.compiler.automake.allow.when.app.running.description': '자동으로 시작된 make는 애플리케이션에 필요한 일부 클래스를 삭제할 수도 있습니다.',
    'advanced.setting.compiler.unified.ic.implementation': '통합된 Java/Kotlin 증분 컴파일(incremental compilation) 구현 활성화',
    'advanced.setting.compiler.unified.ic.implementation.description': '외부 JPS 프로세스는 Java 및 Kotlin이 생성한 바이트코드를 모두 처리할 수 있는 새로운 증분 컴파일 구현을 사용하게 됩니다.',
    'advanced.setting.compiler.inMemoryLogger': '빌드 실패 시 상세한 디버그 로그 보고서 수집',
    'advanced.setting.compiler.inMemoryLogger.description': '디버깅 및 문제 해결을 돕기 위해 실패한 빌드의 상세 로그를 저장합니다. 로그는 다른 빌드 로그와 함께 저장됩니다.',
    'advanced.settings.group.java': 'Java',
    'advanced.setting.code.vision.java.minimal.usages': 'Code Vision: 인레이 힌트(inlay hints)를 표시하는 데 필요한 최소 사용 수',
    'advanced.setting.java.completion.qualifier.as.argument': '한정자(qualifier)를 첫 번째 인자로 사용하는 정적(static) 메서드에 대한 코드 완성 활성화',
    'advanced.setting.java.sdkmanrc.watcher': '프로젝트를 열 때 구성 파일(\'.sdkmanrc\', \'.tool-versions\', …)의 변경 사항 수신 시작',
    'dialog.title.check.functional.interface.candidates': '함수형 인터페이스 후보 확인…',
    'popup.title.select.target.code.block': '대상 코드 블록 선택',
    'target.code.block.presentable.text': '포함하는 블록',
    'conflict.message.method.will.override.method.base.class': '이름이 바뀐 {0}이(가) 기본 {1}의 메서드를 재정의(override)하게 됩니다',
    'progress.title.looking.for.jdk': 'JDK 찾는 중…',
    'dialog.title.check.configuration': '구성 확인…',
    'dialog.message.template.not.found': '템플릿을 찾을 수 없습니다',
    'dialog.message.template.not.applicable': '템플릿을 적용할 수 없습니다',
    'dialog.message.class.not.found': '템플릿 클래스 \'\'{0}\'\'을(를) 찾을 수 없습니다',
    'notification.content.was.set.up': '프로젝트에 JDK \'\'{0}\'\'이(가) 설정되었습니다'
}

found = False
for file_entry in data['new_files']:
    if file_entry['filename'] == bundle_name:
        file_entry.setdefault('keys', {}).update(translations)
        found = True
        break
if not found:
    data['new_files'].append({'filename': bundle_name, 'keys': translations})

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

print(f'Updated {bundle_name} (Keys 281-320)')
