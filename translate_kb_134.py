import json
from pathlib import Path

def update_missing_keys():
    file_path = Path("missing_translations/missing_keys_korean.json")
    
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    ko_dict = {
        "space.within.structured.binding.list.brackets": "구조적 바인딩 목록 대괄호",
        "space.within.empty.lambda.capture.list.brackets": "빈 람다 캡처 목록 대괄호",
        "space.within.catch.parentheses.oc": "'@catch' 괄호",
        "space.within.synchronized.parentheses.oc": "'@synchronized' 괄호",
        "space.within.protocols.brackets.oc": "프로토콜 목록 대괄호",
        "space.within.property.attributes.parentheses.oc": "'@property' 속성 괄호",
        "space.within.method.return.type.parentheses.oc": "메서드 반환 형식 괄호",
        "space.within.method.parameter.type.parentheses.oc": "메서드 매개변수 형식 괄호",
        "space.within.send.message.brackets.oc": "메시지 보내기 대괄호",
        "space.within.template.declaration": "템플릿 선언 안",
        "space.within.template.inst": "템플릿 인스턴스화 안",
        "space.within.class": "클래스/구조체 안",
        "space.before.initialization.lists.colon": "생성자 초기화 목록 콜론 앞",
        "space.after.initialization.lists.colon": "생성자 초기화 목록 콜론 뒤",
        "space.before.lt.template": "'<' 앞",
        "space.before.function.call.parentheses": "함수 호출 괄호",
        "space.before.function.parentheses": "함수 선언 괄호",
        "space.before.class.lbrace": "클래스/구조체 왼쪽 중괄호",
        "space.before.method.lbrace": "함수 왼쪽 중괄호",
        "space.before.method.lbrace.oc": "메서드/함수 왼쪽 중괄호",
        "space.before.namespace.lbrace": "네임스페이스 왼쪽 중괄호",
        "space.before.init.list.lbrace": "초기화 목록 왼쪽 중괄호",
        "space.before.export.lbrace": "모듈 내보내기 영역 왼쪽 중괄호",
        "space.before.superclass.colon": "기본 클래스 콜론 앞",
        "space.before.pointer.in.declaration": "선언의 '*' 앞",
        "space.before.reference.in.declaration": "선언의 '\\\\&' 앞",
        "space.before.catch.parentheses.oc": "'@catch' 괄호 앞",
        "space.before.try.lbrace.oc": "'@try' 왼쪽 중괄호 앞",
        "space.before.catch.lbrace.oc": "'@catch' 왼쪽 중괄호 앞",
        "space.before.finally.lbrace.oc": "'@finally' 왼쪽 중괄호 앞",
        "space.before.synchronized.lbrace.oc": "'@synchronized' 왼쪽 중괄호 앞",
        "space.before.catch.keyword.oc": "'@catch' 키워드 앞",
        "space.before.finally.keyword.oc": "'@finally' 키워드 앞",
        "space.before.synchronized.parentheses.oc": "'@synchronized' 괄호 앞",
        "space.before.autorelease.pool.lbrace.oc": "'@autoreleasepool' 왼쪽 중괄호 앞",
        "space.before.category.parentheses.oc": "카테고리 괄호 앞",
        "space.before.protocols.brackets.oc": "프로토콜 목록 대괄호 앞",
        "space.before.chained.send.message.oc": "체인된 메시지 보내기 앞",
        "space.before.property.attributes.parentheses.oc": "'@property' 속성 괄호 앞",
        "space.before.dictionary.literal.colon": "비트 필드의 콜론 앞",
        "space.before.dictionary.literal.colon.oc": "사전 리터럴 'key\\:value' 쌍 및 비트 필드의 콜론 앞",
        "space.before.colon.in.foreach": "`for` 콜론 앞",
        "space.after.colon.in.foreach": "`for` 콜론 뒤",
        "space.after.superclass.colon": "기본 클래스 콜론 뒤",
        "space.after.structures.rbrace": "구조체의 오른쪽 중괄호 뒤",
        "space.after.pointer.in.declaration": "선언의 '*' 뒤",
        "space.after.reference.in.declaration": "선언의 '\\\\&' 뒤",
        "space.after.reference.in.rvalue": "역참조 및 주소 연산자 뒤",
        "space.after.method.return.type.parentheses.oc": "메서드 반환 형식 괄호 뒤",
        "space.after.method.parameter.type.parentheses.oc": "메서드 매개변수 형식 괄호 뒤"
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
