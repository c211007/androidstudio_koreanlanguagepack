import json
from pathlib import Path

def update_missing_keys():
    file_path = Path("missing_translations/missing_keys_korean.json")

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    ko_dict = {
        "fix.single.character.string.to.char.literal.text": "{0}을(를) {1}(으)로 변경({2} 리터럴로)",
        "fix.single.character.string.to.char.literal.family": "리터럴 타입 수정",
        "change.to.append.family": "StringBuilder append 수정",
        "change.to.append.text": "''{0}''(으)로 변경",
        "convert.to.string.family": "문자 리터럴 수정",
        "convert.to.string.text": "문자열 리터럴로 변환",
        "initialize.final.field.in.constructor.name": "생성자에서 초기화",
        "initialize.final.field.in.constructor.choose.dialog.title": "초기화를 추가할 생성자 선택",
        "remove.redundant.arguments.text": "''{0}''을(를) 호출하기 위한 중복 인수 {1, choice, 1#개|1<개} 제거",
        "remove.redundant.arguments.family": "중복 인수 제거",
        "remove.redundant.str.processor": "중복 'STR' 프로세서 제거",
        "replace.with.list.access.text": "목록 액세스로 교체",
        "add.qualifier": "한정자 추가",
        "add.qualifier.original.class.chooser.title": "원본 클래스",
        "annotations.fix": "어노테이션",
        "add.missing.annotation.parameters.fix": "누락된 어노테이션 매개변수 추가 - {0}",
        "add.missing.annotation.single.parameter.fix": "누락된 어노테이션 매개변수 ''{0}'' 추가",
        "add.method.qualifier.fix.text": "메서드에 한정자 ''{0}'' 추가",
        "add.method.qualifier.fix.family": "메서드 한정자 추가",
        "collection.addall.can.be.replaced.with.constructor.fix.options.dialog.title": "확인할 클래스 추가",
        "collection.addall.can.be.replaced.with.constructor.fix.options.label": "확인할 클래스:",
        "collection.addall.can.be.replaced.with.constructor.fix.description": "'#ref()' 호출을 매개변수화된 생성자 호출로 교체할 수 있습니다.",
        "collection.addall.can.be.replaced.with.constructor.fix.family.name": "'addAll()/putAll()' 호출을 매개변수화된 생성자 호출로 교체",
        "collection.addall.can.be.replaced.with.constructor.fix.name": "''{0}()'' 호출을 매개변수화된 생성자 호출로 교체",
        "add.exception.from.field.initializer.to.constructor.throws.text": "생성자 {0, choice, 0#시그니처|1#시그니처|2#시그니처}에 예외 추가",
        "add.exception.from.field.initializer.to.constructor.throws.family.text": "생성자 시그니처에 예외 추가",
        "java.8.map.api.inspection.fix.text": "''{0}'' 메서드 호출로 교체",
        "java.8.map.api.inspection.description": "단일 ''Map.{0}'' 메서드 호출로 교체할 수 있습니다.",
        "java.8.map.api.inspection.fix.family.name": "단일 Map 메서드 호출로 교체",
        "java.8.collection.removeif.inspection.description": "루프를 'Collection.removeIf'로 교체할 수 있습니다.",
        "java.8.collection.removeif.inspection.fix.name": "루프를 'Collection.removeIf'로 교체",
        "java.8.list.sort.inspection.description": "Collections.sort를 List.sort로 교체할 수 있습니다.",
        "java.8.list.sort.inspection.fix.name": "List.sort로 교체",
        "java.8.list.replaceall.inspection.description": "루프를 'List.replaceAll'로 교체할 수 있습니다.",
        "java.8.list.replaceall.inspection.fix.name": "루프를 'List.replaceAll'로 교체",
        "wrap.with.optional.parameter.text": "''java.util.Optional''을 사용하여 {0, choice, 1#1번째|2#2번째|3#3번째|4#{0,number}번째} 인수 래핑",
        "wrap.with.optional.single.parameter.text": "'java.util.Optional'을 사용하여 래핑",
        "move.file.to.source.root.text": "소스 루트로 파일 이동",
        "delete.return.fix.family": "return 삭제",
        "delete.return.fix.text": "return {0} 삭제",
        "delete.return.fix.side.effects.text": "return {0} 삭제 및 부작용 추출",
        "delete.reference.fix.text": "참조 삭제",
        "delete.unreachable.statement.fix.text": "도달할 수 없는 구문 삭제",
        "extract.side.effects.convert.to.if": "부작용을 'if' 구문으로 추출",
        "extract.side.effects": "{0, choice, 1#부작용|2#부작용들} 추출",
        "extract.side.effects.family.name": "부작용을 추출하는 구문 삭제",
        "module.info.add.directive.family.name": "module-info.java에 지시문 추가",
        "module.info.add.requires.name": "module-info.java에 ''requires {0}'' 지시문 추가",
        "module.info.add.exports.name": "module-info.java에 ''exports {0}'' 지시문 추가",
        "module.info.add.opens.name": "module-info.java에 ''opens {0}'' 지시문 추가"
    }

    filename = "QuickFixBundle.properties"
    found = False
    for file_entry in data.get('new_files', []):
        if file_entry['filename'] == filename:
            file_entry['keys'].update(ko_dict)
            found = True
            break
    if not found:
        data.setdefault('new_files', []).append({"filename": filename, "keys": ko_dict})

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"Updated {filename}")

if __name__ == "__main__":
    update_missing_keys()
