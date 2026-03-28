import json
with open('missing_translations/missing_keys_korean.json', 'r', encoding='utf-8') as f:
    ko_data = json.load(f)

translations = {
  "move.class.to.inner.move.to.self.error": "클래스를 자기 자신 안으로 이동할 수 없습니다",
  "move.class.to.inner.nonstatic.error": "클래스를 정적(static)이 아닌 내부 클래스로 이동할 수 없습니다",
  "move.class.to.inner.find.target.class.progress": "대상 클래스 찾는 중...",
  "move.classes": "클래스 이동...",
  "move.classes.and.packages": "클래스 및 패키지 이동...",
  "move.classes.command": "{0}을(를) {1} 패키지로 이동하는 중",
  "move.classes.destination.make.inner": "다음의 내부 클래스로 만들기(&M)",
  "move.classes.destination.package.prompt": "대상 패키지:",
  "move.classes.destination.to.package": "패키지로(&G)",
  "move.classes.invalid.package.name.warning.message": "잘못된 패키지 이름",
  "move.classes.or.packages.title": "이동",
  "move.classes.or.packages.different.modules.exports.conflict": "모듈 {1}에서 모듈 {2}로 {0}을(를) 이동하면 해당 모듈에 대한 접근이 숨겨질 수 있습니다",
  "move.classes.or.packages.new.module.exports.conflict": "{0} 패키지의 exports/opens 문을 변경하면 같은 패키지 내의 다른 타입 및 멤버에 대한 접근 권한이 부여됩니다",
  "move.classes.or.packages.unused.exports.notification.title": "모듈 {0,choice, 1#descriptor|2#descriptors}에서<br>\\n사용되지 않는 exports/opens를 찾았습니다",
  "move.classes.or.packages.unused.exports.action.name": "사용되지 않는 exports/opens 삭제",
  "move.classes.or.packages.unused.exports.command.name": "사용되지 않는 Exports/Opens 삭제 중",
  "move.enum.constant.cb": "가능한 경우 Enum 상수로 이동(&E)",
  "move.files.regrouping.command.name": "재그룹화 중...",
  "move.files.to.new.directory.prompt": "대상 디렉터리:",
  "move.inner.class.action.name": "내부 클래스 이동...",
  "move.inner.class.command": "내부 클래스 {0} 이동하는 중",
  "move.inner.class.to.another.class": "내부 클래스 {0}을(를) 다른 클래스로 이동(&M)",
  "move.inner.class.to.be.moved": "이동할 클래스",
  "move.inner.class.to.upper.level": "내부 클래스 {0}을(를) 상위 수준으로 이동(&I)",
  "move.inner.class.to.upper.level.preview": "내부 클래스 ''{0}''을(를) 선택한 패키지의 최상위 수준으로 이동합니다.",
  "move.inner.class.to.upper.level.or.another.class.preview": "내부 클래스 ''{0}''을(를) 선택한 패키지의 최상위 수준 또는 다른 클래스로 이동합니다.",
  "move.class.to.new.file.or.make.inner.class.preview": "''{0}'' 클래스를 원하는 패키지의 새 파일로 이동하거나 기존 클래스의 내부 클래스로 변환합니다.",
  "move.inner.class.to.upper.level.action.name": "내부 클래스를 상위 수준으로 이동...",
  "move.instance.method.delegate.title": "인스턴스 메서드 이동...",
  "move.instance.method.elements.header": "인스턴스 메서드 이동",
  "move.instance.method.handler.make.method.static": "''{0}'' 메서드를 정적(static)으로 만든 다음 이동하시겠습니까?",
  "move.members.action.name": "멤버 이동...",
  "move.method.enter.a.valid.name.for.parameter": "매개변수의 유효한 이름을 입력하세요",
  "move.method.is.not.supported.for.0": "{0}에 대해서는 인스턴스 메서드 이동이 지원되지 않습니다",
  "move.method.is.not.supported.for.constructors": "생성자에 대해서는 메서드 이동이 지원되지 않습니다",
  "move.method.is.not.supported.for.generic.classes": "제네릭 클래스에 대해서는 메서드 이동이 지원되지 않습니다",
  "move.method.is.not.supported.for.non.project.methods": "프로젝트 외부 메서드에 대해서는 메서드 이동이 지원되지 않습니다",
  "move.method.this.parameter.label": "''{0}.this'' 매개변수 이름을 선택하세요",
  "move.methods.panel.title": "추출된 클래스로 이동할 메서드(&M)",
  "move.methods.used.in.extracted.block.only": "추출된 블록에 사용된 메서드만 이동"
}

ko_error_bundle = next((x for x in ko_data['new_files'] if x['filename'] == 'JavaRefactoringBundle.properties'), None)
ko_error_bundle['keys'].update(translations)
ko_error_bundle['key_count'] = len(ko_error_bundle['keys'])

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(ko_data, f, ensure_ascii=False, indent=2)

print("Updated JavaRefactoringBundle part 13")