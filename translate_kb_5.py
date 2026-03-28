import json

ko_dict = {
  "unwrap.parameter": "''{0}'' 인수 ''{1}'' 래핑 해제",
  "remove.else": "''{0}''에서 else 제거",
  "unwrap.else": "''{0}''에서 else 래핑 해제",
  "override.declaration.x.in.y": "{1}의 {0}",
  "override.declaration.x.implements.y": "{0}이(가) {1}을(를) 구현합니다.",
  "override.declaration.x.overrides.y.in.class.list": "{0}이(가) 다음 클래스/인터페이스의 선언을 재정의합니다: {1} 기본 선언을 {2}하시겠습니까?",
  "override.declaration.unused.overriding.methods.title": "사용되지 않는 재정의 멤버",
  "override.declaration.choose.to.delete": "<html>삭제할 메서드를 재정의하는 사용되지 않는 멤버가 있습니다. 함께 삭제할 항목을 선택하세요:</html>",
  "override.declaration.member": "멤버",
  "override.declaration.delete.multiple.parameters": "{0}은(는) 메서드 계층 구조의 일부입니다. 여러 매개변수를 삭제하시겠습니까?",
  "hierarchy.legend.member.is.defined.in.class": "멤버가 클래스에 정의됨",
  "hierarchy.legend.member.defined.in.superclass": "멤버가 클래스에는 정의되지 않았지만 상위 클래스에 정의됨",
  "hierarchy.legend.member.should.be.defined": "클래스가 추상 클래스가 아니므로 멤버를 정의해야 함",
  "intention.change.package.text": "패키지 변경",
  "intention.extract.declarations.from.file.text": "현재 파일에서 선언 추출",
  "intention.extract.declarations.from.file.text.details": "현재 파일에서 ''{0}'' {1, choice, 0#|1#및 서브클래스 }추출",
  "intention.wrap.in.with.context": "호출을 'withContext'로 래핑",
  "intention.flow.on.dispatchers.io": "'Dispatchers.IO' 기반 Flow",
  "intention.switch.context.to.dispatchers.io": "'Dispatchers.IO' 컨텍스트로 전환",
  "intention.error.cannot.create.class.message": "''{0}'' 클래스를 생성할 수 없습니다.",
  "intention.error.cannot.create.class.title": "클래스 생성 실패",
  "intention.create.test.dialog.kotlin": "Kotlin",
  "intention.collection.concatenation.to.build.collection.call.family.name": "컬렉션 빌더로 변환",
  "copy.paste.select.imports.to.remove.dialog": "제거할 가져오기 선택",
  "copy.paste.select.imports.to.remove.text": "<html>붙여넣은 코드 조각에 새 컨텍스트에서 액세스할 수 없는 요소가 사용되었습니다. 필요한 가져오기가 추가되었습니다.<br/>추가된 가져오기 중에서 파일에서 제거할 항목을 선택하세요.</html>",
  "copy.paste.reference.notification": "가져오기 {0}개가 추가되었습니다.<p><span><a href=''show''>추가된 가져오기 검토...</a></span>",
  "kotlin.external.compiler.updates.notification.group.name": "사용할 수 있는 Kotlin 외부 컴파일러 업데이트",
  "code.insight.workspace.settings.title": "Kotlin",
  "quick.doc.text.enum.ordinal": "열거형 상수 서수: {0}",
  "quick.doc.text.tailrec": "'tailrec'은 함수를 <a href=\"https://kotlinlang.org/docs/reference/functions.html#tail-recursive-functions\">꼬리 재귀</a>로 표시합니다(컴파일러가 재귀를 반복으로 대체할 수 있도록 허용).",
  "quick.doc.text.lateinit": "'lateinit'을 사용하면 <a href=\"https://kotlinlang.org/docs/reference/properties.html#late-initialized-properties-and-variables\">생성자 외부에서 null이 아닌 속성</a>을 초기화할 수 있습니다.",
  "quick.doc.no.documentation": "사용 가능한 문서 없음",
  "quick.doc.section.deprecated": "지원 중단됨:",
  "quick.doc.section.replace.with": "대체 항목:",
  "quick.doc.section.java.declaration": "Java 선언:",
  "action.j2k.name": "Java를 Kotlin으로 변환",
  "action.j2k.task.name": "Java에서 Kotlin으로 파일 변환",
  "action.j2k.correction.investigate": "오류 조사",
  "action.j2k.correction.proceed": "변환 계속 진행",
  "action.j2k.correction.required": "이 변환을 수행한 후 프로젝트의 나머지 코드 일부를 수정해야 할 수 있습니다. 해당 코드를 찾아 수정하시겠습니까?",
  "action.j2k.correction.errors.single": "''{0}''에 구문 오류가 있어 변환 결과가 올바르지 않을 수 있습니다.",
  "action.j2k.correction.errors.multiple": "''{0}'' 및 다른 {1}개의 Java 파일에 구문 오류가 있어 변환 결과가 올바르지 않을 수 있습니다.",
  "action.j2k.error.cant.save.result": "변환 결과를 저장하지 못했습니다: {0}",
  "action.j2k.error.cant.find.document": "''{0}'' 문서를 찾을 수 없습니다.",
  "action.j2k.error.read.only": "파일 ''{0}''이(가) 읽기 전용입니다.",
  "action.j2k.error.nothing.to.convert": "변환할 항목 없음:<br>쓰기 가능한 Java 파일을 찾을 수 없습니다.",
  "formatter.settings.title": "Kotlin 포맷터 설정",
  "action.generate.functions.already.defined": "클래스 {1}에 함수 {0}이(가) 이미 정의되어 있습니다. 삭제하고 진행하시겠습니까?",
  "action.generate.equals.choose.equals": "'equals()'에 포함할 속성 선택",
  "action.generate.equals.choose.hashcode": "'hashCode()'에 포함할 속성 선택"
}

with open('missing_translations/missing_keys_korean.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

filename = "KotlinBundle.properties"
found = False
for file_entry in data.get('new_files', []):
    if file_entry['filename'] == filename:
        file_entry['keys'].update(ko_dict)
        found = True
        break
if not found:
    data.setdefault('new_files', []).append({"filename": filename, "keys": ko_dict})

print(f"Updated {filename} (Keys 241-290)")

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
