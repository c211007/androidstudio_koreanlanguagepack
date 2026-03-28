import json
with open('missing_translations/missing_keys_korean.json', 'r', encoding='utf-8') as f:
    ko_data = json.load(f)

translations = {
  "changeClassSignature.Type.parameter.can.not.be.primitive": "타입 매개변수는 원시 타입일 수 없습니다",
  "changeSignature.validating.title": "검증 중\\u2026",
  "changeSignature.processing.changes.title": "변경 사항 처리 중\\u2026",
  "changeSignature.bound.value.column": "바인딩된 값(Bound Value)",
  "changeSignature.cannot.resolve.return.type": "반환 타입 ''{0}''을(를) 확인할 수 없습니다.\\n계속하시겠습니까?",
  "changeSignature.default.value.column": "기본값(Default Value)",
  "changeSignature.exception.caller.chooser": "새 예외를 전파할 메서드 선택",
  "changeSignature.exceptions.panel.border.title": "예외(Exceptions)",
  "changeSignature.exceptions.wont.propagate": "예외 변경 사항의 재귀적 전파가 수행되지 않습니다",
  "changeSignature.no.return.type": "반환 타입이 지정되지 않았습니다",
  "changeSignature.no.type.for.exception": "예외에 대한 타입을 지정하세요",
  "changeSignature.no.type.for.parameter": "매개변수 ''{1}''에 대한 {0} 타입을 지정하세요",
  "changeSignature.not.throwable.type": "예외에 대한 잘못된 타입 ''{0}'', java.lang.Throwable을 상속(extend)해야 합니다",
  "changeSignature.propagate.exceptions.title": "예외 전파(&X)\\u2026",
  "changeSignature.vararg.not.last": "가변 인수(Vararg) 매개변수는 메서드 시그니처의 마지막에 있어야 합니다",
  "changeSignature.wrong.return.type": "잘못된 반환 타입: ''{0}''",
  "changeSignature.wrong.type.for.exception": "예외에 대한 잘못된 타입: ''{0}''",
  "changeSignature.wrong.type.for.parameter": "매개변수 ''{1}''에 대한 잘못된 타입: ''{0}''",
  "changeSignature.empty.caller.method.text": "여기에 호출자(caller) 메서드 텍스트와 강조된 피호출자(callee) 호출이 표시됩니다",
  "changeSignature.empty.callee.method.text": "여기에 피호출자(callee) 메서드 텍스트가 표시됩니다",
  "changeSignature.contract.converter.external.annotations": "외부 애너테이션의 자동 업데이트는 지원되지 않습니다",
  "changeSignature.contract.converter.mutation.contract": "애너테이션에 변형(mutation) 계약이 포함되어 있습니다",
  "changeSignature.contract.converter.definition.error": "계약 정의 오류: {0}",
  "changeSignature.contract.converter.invalid.clause": "잘못된 계약 조항 ''{0}''",
  "changeSignature.contract.converter.parameter.removed": "매개변수 ''{0}''이(가) 삭제되었지만 계약 조항 ''{1}''이(가) 이에 종속되어 있습니다",
  "changeSignature.contract.converter.invalid.return.reference": "반환 값에 잘못된 참조가 있습니다: {0}",
  "changeSignature.contract.converter.return.parameter.removed": "매개변수 ''{0}''이(가) 삭제되었지만 계약 조항 ''{1}''이(가) 이를 반환합니다",
  "changeSignature.contract.converter.can.not.update.annotation": "@Contract 애너테이션을 자동으로 업데이트할 수 없습니다: {0}",
  "changeSignature.contract.converter.inherited.annotation": "애너테이션이 기본(base) 메서드에서 상속되었습니다",
  "changeSignature.use.any.var": "아무 변수나 사용합니다(Use any var).",
  "checking.conflicts": "충돌 확인 중\\u2026",
  "class.0.already.exists": "{0} 클래스가 이미 존재합니다",
  "class.0.is.not.accessible.from.target.1": "대상 {1}에서 클래스 {0}에 액세스할 수 없습니다",
  "class.0.not.found": "{0} 클래스를 찾을 수 없습니다.",
  "class.body.description": "{0}의 클래스 본문",
  "class.description": "{1, choice, 0#|1#지역(local) }클래스 {0}",
  "class.does.not.exist.in.the.project": "클래스가 프로젝트에 존재하지 않습니다. 새로 생성하시겠습니까?",
  "class.does.not.have.base.classes.or.interfaces": "{0} 클래스에 기본 클래스 또는 인터페이스가 없습니다",
  "class.does.not.have.implicit.default.constructor": "{0} 클래스에 암시적 기본 생성자가 없습니다",
  "class.has.been.successfully.created": "{0} 클래스가 성공적으로 생성되었습니다"
}

ko_error_bundle = next((x for x in ko_data['new_files'] if x['filename'] == 'JavaRefactoringBundle.properties'), None)
ko_error_bundle['keys'].update(translations)
ko_error_bundle['key_count'] = len(ko_error_bundle['keys'])

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(ko_data, f, ensure_ascii=False, indent=2)

print("Updated JavaRefactoringBundle part 3")