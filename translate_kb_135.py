import json
from pathlib import Path

def update_missing_keys():
    file_path = Path("missing_translations/missing_keys_korean.json")
    
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    ko_dict = {
        "space.after.visibility.sign.in.method.declaration.oc": "메서드 선언의 +/- 뒤",
        "space.after.colon.in.selector.oc": "선택자의 콜론 뒤",
        "space.after.cup.in.blocks.oc": "블록의 '^' 뒤",
        "space.after.dictionary.literal.colon": "비트 필드의 콜론 뒤",
        "space.after.dictionary.literal.colon.oc": "사전 리터럴 'key\\:value' 쌍 및 비트 필드의 콜론 뒤",
        "space.between.adjacent.brackets": "동일한 형식의 대괄호 사이에 공백 유지",
        "space.between.operator.punctuator": "'operator' 키워드 및 구두점 사이",
        "space.discharged.short.ternary.operator": "'a ? \\: b'의 '?' 및 '\\:' 사이의 공백",
        "space.around.relational.operators": "관계 연산자(<, >, <=, >=, <=>)",
        "space.around.shift.operators": "시프트 연산자(<<, >>)",
        "space.around.lambda.arrow": "반환 형식의 '->'",
        "space.around.pm.operators": "멤버 포인터 연산자(->, ., ->*, .*)",
        "blank.lines.before.includes": "include 앞:",
        "blank.lines.after.includes": "include 뒤:",
        "blank.lines.around.classes": "클래스/구조체 주위:",
        "blank.lines.after.class.header": "클래스/구조체 헤더 뒤:",
        "blank.lines.around.member.variable": "필드 주위:",
        "blank.lines.around.member.variable.oc": "인스턴스 변수/필드 주위:",
        "blank.lines.around.global.variable": "전역 변수 주위:",
        "blank.lines.around.function.declaration": "함수 선언 주위:",
        "blank.lines.around.function.declaration.oc": "메서드/함수 선언 주위:",
        "blank.lines.around.function.definition": "함수 정의 주위:",
        "blank.lines.around.function.definition.oc": "메서드/함수 정의 주위:",
        "blank.lines.before.function.body": "함수 본문 앞:",
        "blank.lines.before.function.body.oc": "메서드/함수 본문 앞:",
        "completion.press.keyboard.shortcut.for.all.methods.selectors": "모든 메서드 선택자에 대해 {0} 키를 다시 누르세요",
        "completion.press.keyboard.shortcut.to.filter.results.by.type": "형식별로 결과를 필터링하려면 {0} 키를 누르세요",
        "completion.press.keyboard.shortcut.for.non.imported.symbols": "가져오지 않은 기호에 대해 {0} 키를 다시 누르세요",
        "completion.press.keyboard.shortcut.for.global.symbols": "전역 기호에 대해 {0} 키를 다시 누르세요",
        "completion.press.shortcut.again.for.non.public.members": "공용이 아닌 멤버에 대해 {0} 키를 {1, choice, 0#|1#다시 }누르세요",
        "completion.press.shortcut.again.for.non.imported.members": "가져오지 않은 멤버 및 NSObject 카테고리의 멤버에 대해 {0} 키를 {1, choice, 0#|1#다시 }누르세요",
        "collapse.ivars": "인스턴스 변수",
        "collapse.synthesizes": "synthesize 문",
        "collapse.localized.strings": "현지화된 문자열",
        "collapse.multiline.comments": "여러 줄 주석",
        "collapse.block.expressions.oc": "블록 및 람다",
        "collapse.block.expressions": "람다",
        "collapse.conditionally.non-compiled": "조건부로 컴파일되지 않은 코드",
        "collapse.template.param.list": "템플릿 매개변수",
        "collapse.new.line.before.lbrace": "축소된 경우 '{' 앞의 새 줄 대신 공백",
        "color.keyword": "키워드//키워드",
        "color.this.keywords": "키워드//'this' 키워드",
        "color.preprocessor.directive": "전처리기//지시문",
        "color.preprocessor.path": "전처리기//헤더 경로",
        "color.format.string.token": "문자열//문자열 인수의 형식 지정자",
        "color.conditionally.non-compiled": "조건부로 컴파일되지 않은 코드",
        "color.macro.name": "매크로 이름",
        "color.macro.parameter": "매개변수//매크로 매개변수",
        "color.global.variable": "변수//전역",
        "color.extern.variable": "변수//Extern"
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
