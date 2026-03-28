import json
with open('missing_translations/missing_keys_korean.json', 'r', encoding='utf-8') as f:
    ko_data = json.load(f)

translations = {
  "declare.generated.annotations": "애너테이션 생성(&G)",
  "declare.static.checkbox": "정적(static) 선언(&S)",
  "declare.static.pass.fields.checkbox": "정적(static) 선언 (필드를 매개변수로 전달)(&S)",
  "declare.var.type": "var 타입 선언(&V)",
  "declare.varargs.checkbox": "가변 인수(varargs) 선언(&A)",
  "default.visibility.border.title": "기본 가시성",
  "delete.variable.declaration": "변수 선언 삭제(&D)",
  "destination.directory.does.not.correspond.to.any.package": "대상 디렉터리가 어떤 패키지와도 일치하지 않습니다",
  "destination.package": "대상 패키지(&P):",
  "different.name.expected": "다른 이름이 필요합니다",
  "directory.0.already.contains.1.named.2": "{0} 디렉터리에\\n이미 이름이 ''{2}''인 {1}이(가) 포함되어 있습니다",
  "directory.0.already.contains.a.file.named.1": "{0} 디렉터리에\\n이미 이름이 ''{1}''인 파일이 포함되어 있습니다",
  "do.not.replace": "바꾸지 않음(&N)",
  "do.not.show.this.message.in.the.future": "나중에 이 메시지 다시 표시 안 함(&D)",
  "do.you.want.to.process.overriding.methods.with.covariant.return.type": "공변(covariant) 반환 타입이 있는 재정의(override)된 메서드를\\n처리하시겠습니까?",
  "dialog.message.overriding.methods.with.weaken.visibility": "재정의하는 메서드의 가시성(visibility)도 ''{0}''(으)로 축소하시겠습니까?",
  "edit.migration.entry.title": "클래스/패키지 마이그레이션 규칙 편집",
  "edit.migration.map.title.new": "새 마이그레이션 맵",
  "edit.migration.map.title.existing": "마이그레이션 맵 편집",
  "edit.migration.map.ok.button": "저장",
  "element.will.no.longer.be.accessible": "{1}에서 {0}에 더 이상 액세스할 수 없게 됩니다",
  "encapsulate.fields..encapsulated.fields.visibility.border.title": "캡슐화된 필드의 가시성",
  "encapsulate.fields..package.local.radio": "패키지 지역(Package local)(&C)",
  "encapsulate.fields.accessors.visibility.border.title": "접근자의 가시성",
  "encapsulate.fields.command.name": "{0}의 필드 캡슐화",
  "encapsulate.fields.encapsulate.border.title": "캡슐화",
  "encapsulate.fields.existed.accessor.hidden": "생성된 접근자에 의해 숨겨지는 {0}이(가) 이미 존재합니다",
  "encapsulate.fields.existed.accessor.hides.generated": "{1}에 대해 생성될 접근자를 숨길 {0}이(가) 이미 존재합니다",
  "encapsulate.fields.expression.type.is.used": "결과 타입이 사용 중일 때 후위/전위(postfix/prefix) 표현식을 진행할 수 없습니다",
  "encapsulate.fields.field.column.name": "필드",
  "encapsulate.fields.fields.to.be.encapsulated": "캡슐화할 필드",
  "encapsulate.fields.fields.to.encapsulate.border.title": "캡슐화할 필드",
  "encapsulate.fields.get.access.checkbox": "가져오기 접근(&G)",
  "encapsulate.fields.getter.column.name": "Getter",
  "encapsulate.fields.getter.exists": "반환 타입만 getter {1}와(과) 다른 {0} 메서드가 이미 존재합니다",
  "encapsulate.fields.no.target": "캡슐화할 항목을 찾을 수 없습니다",
  "encapsulate.fields.nothing.todo.warning.message": "클래스에 캡슐화할 필드가 없습니다",
  "encapsulate.fields.private.radio": "Private(&I)",
  "encapsulate.fields.protected.radio": "Protected(&T)",
  "encapsulate.fields.refactoring.cannot.be.applied.to.interface": "필드 캡슐화 리팩터링은 인터페이스에 적용할 수 없습니다"
}

ko_error_bundle = next((x for x in ko_data['new_files'] if x['filename'] == 'JavaRefactoringBundle.properties'), None)
ko_error_bundle['keys'].update(translations)
ko_error_bundle['key_count'] = len(ko_error_bundle['keys'])

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(ko_data, f, ensure_ascii=False, indent=2)

print("Updated JavaRefactoringBundle part 5")