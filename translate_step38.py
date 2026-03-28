import json
with open('missing_translations/missing_keys_korean.json', 'r', encoding='utf-8') as f:
    ko_data = json.load(f)

translations = {
  "dialog.message.replace.duplicates.works.with.constants.only": "중복 교체는 상수에만 작동합니다",
  "dialog.message.caret.should.be.inside.method.or.constant": "캐럿은 메서드나 상수 내부에 위치해야 합니다",
  "inline.object.command.name": "객체 인라인",
  "introduce.variable.no.matching.occurrences": "일치하는 항목이 없습니다",
  "inline.super.no.inheritors.warning.message": "상속자가 없는 클래스는 인라인할 수 없습니다",
  "inline.superclass.foreign.language.conflict.message": "{0}(으)로 인라인할 수 없습니다",
  "field.0.won.t.be.initialized.already.in.class.initializer": "''{0}'' 필드는 클래스 초기화자 내부에서 초기화되지 않습니다",
  "dialog.title.analyze.code.fragment.to.extract": "추출할 코드 분석 중...",
  "move.label.text": "이동:",
  "dialog.title.move.directory.to.source.root": "디렉터리를 소스 루트로 이동",
  "dialog.title.confirm.move": "이동 확인",
  "dialog.message.moving.directories.to": "디렉터리를 ''{0}''(으)로 이동하는 중",
  "progress.title.collect.hierarchy": "''{0}'' 계층 구조 수집 중",
  "introduce.variable.message.change.semantics.warning": "선택한 표현식을 추출하면 주변 표현식의 의미(semantics)가 변경됩니다.",
  "introduce.variable.message.expression.refers.to.pattern.variable.declared.outside": "선택한 표현식이 패턴 변수 ''{0}''을(를) 참조하는데, 이는 범위(scope)에서 벗어나게 됩니다.",
  "introduce.variable.message.cannot.extract.in.implicit.class": "압축된 소스 파일(compact source file)에서는 추출할 수 없습니다.",
  "introduce.variable.message.cannot.extract.variable.in.interface": "인터페이스에서는 변수를 추출할 수 없습니다.",
  "tooltip.cannot.inline.pattern.variable": "패턴 변수는 인라인할 수 없습니다",
  "inline.popup.highlight": "{0}개의 충돌하는 {0, choice, 1#쓰기를|2#쓰기를} 강조 표시합니다",
  "inline.popup.ignore.conflicts": "쓰기를 무시하고 계속 진행",
  "inline.warning.variables.used.in.initializer.are.updated": "안전하지 않은 인라인: 초기화자에서 사용된 변수가 업데이트됩니다",
  "dialog.title.resolving.method.implementation": "메서드 구현 해결 중",
  "dialog.message.confirmation.to.process.only.implementation": "추상 메서드의 구현이 발견되었습니다:<br><br><b>{0}</b><br><br>이 구현을 인라인하시겠습니까?"
}

ko_error_bundle = next((x for x in ko_data['new_files'] if x['filename'] == 'JavaRefactoringBundle.properties'), None)
ko_error_bundle['keys'].update(translations)
ko_error_bundle['key_count'] = len(ko_error_bundle['keys'])

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(ko_data, f, ensure_ascii=False, indent=2)

print("Updated JavaRefactoringBundle part 21 (Final)")