import json

ko_dict = {
  "action.generate.secondary.constructor.choose.properties": "생성자로 초기화할 속성 선택",
  "action.generate.secondary.constructor.error.already.exists": "생성자가 이미 있습니다.",
  "action.generate.test.support.choose.framework": "프레임워크 선택",
  "command.generate.test.support.generate.test.function": "테스트 함수 생성",
  "action.generate.test.support.choose.test.name": "테스트 이름 선택:",
  "action.generate.test.support.edit.template": "템플릿 편집",
  "action.generate.test.support.error.no.template.found": "{0}:{1}의 템플릿을 찾을 수 없습니다.",
  "action.generate.test.support.error.cant.convert.java.template": "Java 템플릿을 Kotlin으로 변환할 수 없습니다.",
  "action.generate.test.support.error.cant.generate.method": "메서드를 생성할 수 없습니다: {0}",
  "action.generate.tostring.name": "'toString()' 생성",
  "action.generate.super.type": "상위 유형 명시적으로 지정",
  "action.generate.tostring.template.single": "단일 템플릿",
  "action.generate.tostring.template.single.with.super": "super 호출이 있는 단일 템플릿",
  "action.generate.tostring.template.multiple": "연결이 있는 다중 템플릿",
  "action.generate.tostring.template.multiple.with.super": "연결 및 super 호출이 있는 다중 템플릿",
  "action.generate.tostring.choose.implementation": "구현 선택:",
  "action.generate.tostring.choose.implementation.mnemonic": "i",
  "action.generate.tostring.generate.super.call": "super.toString() 호출 생성",
  "action.generate.tostring.generate.super.call.mnemonic": "s",
  "action.Kotlin.NewFile.text": "Kotlin 클래스/파일",
  "action.Kotlin.NewFile.description": "새 Kotlin 클래스 또는 파일을 생성합니다.",
  "action.Kotlin.NewScript.text": "Kotlin 스크립트",
  "action.Kotlin.NewScript.description": "새 Kotlin 스크립트 또는 워크시트 생성합니다.",
  "action.new.file.dialog.title": "새 Kotlin 클래스/파일",
  "action.new.script.dialog.title": "새 Kotlin 스크립트 파일",
  "action.new.script.dialog.script": "새 Kotlin 스크립트",
  "action.new.file.dialog.file.title": "파일",
  "action.new.file.dialog.class.title": "클래스",
  "action.new.file.dialog.data.class.title": "데이터 클래스",
  "action.new.file.dialog.sealed.class.title": "Sealed 클래스",
  "action.new.file.dialog.annotation.title": "주석",
  "action.new.file.dialog.interface.title": "인터페이스",
  "action.new.file.dialog.sealed.interface.title": "Sealed 인터페이스",
  "action.new.file.dialog.enum.title": "열거형(Enum) 클래스",
  "action.new.file.dialog.object.title": "객체",
  "action.new.file.error.empty.name": "이름은 비워둘 수 없습니다.",
  "action.new.file.error.empty.name.part": "이름의 일부는 비워 둘 수 없습니다.",
  "action.new.script.name": "Kotlin 스크립트",
  "breadcrumbs.tooltip.indexing": "색인 생성 중…",
  "copy.paste.resolve.pasted.references": "붙여넣은 참조 확인",
  "copy.paste.restore.pasted.references": "붙여넣은 참조 복원",
  "copy.paste.restore.pasted.references.capitalized": "붙여넣은 참조 복원",
  "type.provider.anonymous.object": "익명 객체",
  "type.provider.unknown.type": "유형을 알 수 없음",
  "type.provider.smart.cast.from": "({0}에서 스마트 변환됨)",
  "type.provider.no.expression.found": "표현식을 찾을 수 없음",
  "optimize.imports.collect.unused.imports": "사용되지 않는 가져오기 수집 중",
  "optimize.imports.task.removing.redundant.imports": "중복된 가져오기 제거 중",
  "kdoc.section.title.receiver": "수신자",
  "kdoc.section.title.parameters": "매개변수"
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

print(f"Updated {filename} (Keys 291-340)")

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
