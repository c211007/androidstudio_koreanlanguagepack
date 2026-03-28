import json
from pathlib import Path

def update_missing_keys():
    file_path = Path("missing_translations/missing_keys_korean.json")
    
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    ko_dict = {
        "wrapping.keep.simple.methods.in.one.line": "간단한 함수를 한 줄로",
        "wrapping.keep.simple.methods.in.one.line.oc": "간단한 메서드 및 함수를 한 줄로",
        "wrapping.keep.simple.blocks.in.one.line": "간단한 람다를 한 줄로",
        "wrapping.keep.simple.blocks.in.one.line.oc": "간단한 블록 및 람다를 한 줄로",
        "wrapping.keep.nested.namespaces.in.one.line": "중첩된 네임스페이스를 한 줄로 유지",
        "wrapping.keep.directive.at.first.column": "첫 번째 열에 지시문 유지",
        "wrapping.brace.placement.class.declaration": "클래스 및 구조체에",
        "wrapping.property.declaration.oc": "@property 선언",
        "wrapping.try.statement": "'try' 문",
        "wrapping.catch.on.new.line": "'catch'를 새 줄에",
        "wrapping.array.initializer": "초기화 목록",
        "wrapping.array.initializer.oc": "컬렉션 리터럴 및 초기화 목록",
        "wrapping.align.multiline.fields.groups": "변수 그룹",
        "wrapping.align.in.columns": "열에 맞춤",
        "wrapping.structures.in.one.line": "클래스 및 구조체를 한 줄로",
        "wrapping.before.brace.namespace": "네임스페이스에",
        "wrapping.ternary.short.inline": "'a ?\\: b'에서 줄바꿈 없는 '?\\:'",
        "wrapping.try.statement.oc": "'@try' 문",
        "wrapping.catch.on.new.line.oc": "'@catch'를 새 줄에",
        "wrapping.finally.on.new.line.oc": "'@finally'를 새 줄에",
        "wrapping.array.initializer.lbrace.on.next.line.oc": "'{', '[' 다음에 새 줄",
        "wrapping.array.initializer.rbrace.on.next.line.oc": "'}', ']'를 새 줄에 배치",
        "wrapping.method.brace.placement": "메서드에",
        "wrapping.function.brace.placement": "함수에",
        "wrapping.block.brace.placement": "람다에",
        "wrapping.block.brace.placement.oc": "블록 및 람다에",
        "wrapping.method.parameters.align.by.colons": "콜론 기준으로 맞춤",
        "wrapping.method.call.arguments.special.dictionary.pairs.treatment": "특수 NSDictionary 초기화 처리",
        "wrapping.indent.template.body.if.wrapped": "줄바꿈할 경우 템플릿 본문 들여쓰기",
        "wrapping.new.line.after.colon": "':' 다음에 새 줄",
        "wrapping.new.line.before.colon": "':'를 새 줄에 배치",
        "wrapping.new.line.never": "안 함",
        "wrapping.new.line.always": "항상",
        "wrapping.new.line.if.long": "길 경우",
        "align.dictionary.values": "사전 값을 열에 맞춤",
        "align.init.list.values": "초기화 목록 값을 열에 맞춤",
        "space.within.empty.code.blocks": "빈 코드 중괄호",
        "space.within.template": "<...> 안",
        "space.within.empty.diamond": "빈 <> 안",
        "space.within.template.double.gt": "템플릿에서 >> 연결 방지",
        "space.within.bracket": "배열 대괄호",
        "space.within.array.initializer.braces": "초기화 목록 중괄호",
        "space.within.array.empty.initializer.braces": "빈 초기화 목록 중괄호",
        "space.within.array.initializer.braces.oc": "컬렉션 리터럴 및 초기화 목록 중괄호",
        "space.within.array.empty.initializer.braces.oc": "빈 컬렉션 리터럴 및 초기화 목록 중괄호",
        "space.within.function.declaration.parentheses": "함수 선언 괄호",
        "space.within.empty.function.declaration.parentheses": "빈 함수 선언 괄호",
        "space.within.function.call.parentheses": "함수 호출 괄호",
        "space.within.empty.function.call.parentheses": "빈 함수 호출 괄호",
        "space.within.lambda.capture.list.brackets": "람다 캡처 목록 대괄호"
    }
    
    filename = "OCBundle.properties"
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
