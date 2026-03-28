import json
from pathlib import Path

def update_missing_keys():
    file_path = Path("missing_translations/missing_keys_korean.json")
    
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    ko_dict = {
        "find.usages.type.packageMemberAccess": "패키지 멤버 접근",
        "and.delete.initializer": "\\ 및 초기화자 삭제",
        "change.to.val": "'val'로 변경",
        "change.to.var": "'var'로 변경",
        "redundant.0.modifier": "불필요한 ''{0}'' 수정자",
        "remove.redundant.0.modifier": "불필요한 ''{0}'' 수정자 제거",
        "remove.redundant.modality.modifier": "불필요한 방식(Modality) 수정자 제거",   
        "remove.redundant.visibility.modifier": "불필요한 가시성 수정자 제거",
        "usage.provider.text.property.of.0": "{1}의 {0}",
        "usage.provider.text.unnamed": "<이름 없음>",
        "inspection.unnecessary.opt_in.annotation.display.name": "불필요한 '@OptIn' 주석",
        "inspection.unnecessary.opt_in.redundant.marker": "Opt-in 마커가 불필요합니다: ''{0}''(으)로 표시된 실험적 API가 사용되지 않았습니다.",
        "inspection.unnecessary.opt_in.redundant.annotation": "Opt-in 주석이 불필요합니다: 일치하는 실험적 API가 사용되지 않았습니다.",
        "inspection.unnecessary.opt_in.remove.marker.fix.family.name": "Opt-in 마커 제거",
        "inspection.unnecessary.opt_in.remove.annotation.fix.family.name": "주석 제거",
        "inspection.verbose.nullability.and.emptiness.display.name": "장황한 Null 가능성 및 빈 값 확인",
        "inspection.verbose.nullability.and.emptiness.call": "이후의 확인을 ''{0}()'' 호출로 바꿉니다.",
        "add.return.expression": "'return' 표현식 추가",
        "provide.return.value": "반환 값 제공",
        "wrap.expression.in.parentheses": "표현식을 괄호로 묶기",
        "convert.left.hand.side.to.0": "왼쪽을 ''{0}''(으)로 변환",
        "convert.right.hand.side.to.0": "오른쪽을 ''{0}''(으)로 변환",
        "convert.string.to.character.literal": "문자열을 문자 리터럴로 변환", 
        "inspection.replace.readline.with.readln.display.name": "'readLine'은 'readln' 또는 'readlnOrNull'로 바꿀 수 있습니다.",
        "fix.convert.to.is.array.of.call": "'isArrayOf' 호출로 변환",
        "inspection.message.object.with.manual.tostring.can.be.converted.to.data.object": "수동 'toString'이 있는 'object'는 'data object'로 변환할 수 있습니다.",        
        "inspection.message.sealed.object.can.be.converted.to.data.object": "'sealed' 하위 객체는 'data object'로 변환할 수 있습니다.",
        "convert.to.data.object": "'data object'로 변환",
        "analyzing.members": "멤버 분석 중\\u2026",
        "inspection.convert.object.to.data.object.display.name": "'object'를 'data object'로 변환",
        "inspection.replace.with.string.builder.append.range.display.name": "JVM에서 'StringBuilder.append(CharArray, offset, len)' 호출",
        "progress.title.collect.hierarchy": "''{0}'' 계층 구조 수집 중\\u2026",      
        "inspection.redundant.value.argument.display.name": "불필요한 값 인수",
        "inspection.redundant.value.argument.annotation": "값 인수가 매개변수 ''{0}''의 기본값과 일치합니다.",
        "inspection.filter.is.instance.call.with.class.literal.argument.display.name": "클래스 리터럴 인수가 있는 'filterIsInstance' 호출",
        "inspection.filter.is.instance.call.with.class.literal.argument.quick.fix.text": "클래스 리터럴 인수를 구체화된(Reified) 타입 매개변수로 바꾸기",
        "add.fun.modifier.to.0": "''{0}''에 ''fun'' 수정자 추가",
        "convert.to.nullable.type": "Null 허용 타입으로 변환",
        "add.external.keyword": "External 키워드 추가",
        "interface.should.be.external": "인터페이스는 External이어야 합니다.",
        "class.should.be.external.interface": "클래스는 External 인터페이스여야 합니다.",   
        "object.should.be.external.interface": "객체는 External 인터페이스여야 합니다.", 
        "boolean.property.in.external.interface.should.be.nullable": "External 인터페이스의 부울 프로퍼티는 Null을 허용해야 합니다.",
        "property.in.external.interface.should.be.var": "External 인터페이스의 프로퍼티는 'var'이어야 합니다.",
        "external.interface.contains.val.property.name": "External 인터페이스에 'val' 프로퍼티가 포함되어 있습니다.",
        "external.interface.contains.non.nullable.property.name": "External 인터페이스에 Null을 허용하지 않는 부울 프로퍼티가 포함되어 있습니다.",
        "non.external.classifier.extending.state.or.props.name": "State 또는 Props를 확장하는 Non-external 분류자",
        "highlighter.name.style": "스타일 {0}",
        "highlighter.name.dsl": "Dsl//",
        "notification.text.kotlin.js.compiler.title": "버전 1.8.0 이상에서 Kotlin/JS IR이 안정화되었습니다!"
    }
    
    filename = "KotlinBundle.properties"
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
        
    print(f"Updated KotlinBundle.properties (Keys 2191-2240)")

if __name__ == "__main__":
    update_missing_keys()
