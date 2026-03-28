import json
from pathlib import Path

def update_missing_keys():
    file_path = Path("missing_translations/missing_keys_korean.json")

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    ko_dict = {
        "remove.override.fix.family": "override 제거",
        "remove.override.fix.text": "메서드 선언에서 override 어노테이션 제거",
        "remove.annotation.fix.family": "어노테이션 제거",
        "remove.annotation.fix.text": "''@{0}'' 어노테이션 제거",
        "fix.update.modifier.change.this": "이 메서드만 변경",
        "fix.update.modifier.change.inheritors": "이 메서드와 상속자 변경",
        "move.class.in.extend.list.family": "Extend 목록에서 클래스 이동",
        "move.bound.class.to.front.fix.text": "바운드 ''{0}''을(를) 타입 매개변수 ''{1}''의 바운드 목록 시작 부분으로 이동",
        "move.catch.up.family": "'catch' 위로 이동",
        "move.catch.up.text": "''{0}''의 catch를 ''{1}'' 앞으로 이동",
        "move.class.to.separate.file.family": "별도 파일로 클래스 이동",
        "move.class.to.separate.file.text": "클래스 ''{0}''을(를) ''{0}.java''(으)로 이동",
        "move.class.to.package.family": "패키지로 이동",
        "move.class.to.package.text": "패키지 ''{0}''(으)로 이동",
        "move.class.0.to.package.text": "{0} ''{1}''을(를) 패키지 ''{2}''(으)로 이동",
        "negation.broader.scope.family": "더 넓은 범위의 부정",
        "negation.broader.scope.text": "''!({0})''(으)로 변경",
        "optimize.imports.fix": "가져오기 최적화",
        "remove.qualifier.fix": "한정자 제거",
        "remove.unused.element.family": "사용하지 않는 {0} 제거",
        "rename.wrong.reference.family": "잘못된 참조 이름 바꾸기",
        "rename.wrong.reference.text": "참조 이름 바꾸기",
        "reuse.variable.declaration.family": "이전 변수 재사용",
        "reuse.variable.declaration.text": "이전 변수 ''{0}'' 재사용",
        "navigate.variable.declaration.family": "변수 선언으로 이동",
        "navigate.variable.declaration.text": "이전에 선언된 변수 ''{0}''(으)로 이동",
        "navigate.duplicate.element.text": "중복된 {0}(으)로 이동",
        "show.duplicate.elements.family": "중복 표시",
        "show.duplicate.elements.text": "''{0}'' 중복 표시",
        "show.duplicate.elements.popup.title": "중복 선택",
        "show.duplicate.elements.navigate.family": "중복으로 이동",
        "show.duplicate.elements.navigate.text": "{0}번째 줄",
        "safe.delete.family": "안전한 삭제",
        "safe.delete.text": "''{0}'' 안전하게 삭제",
        "setup.jdk.location.family": "JDK 위치 설정",
        "setup.jdk.location.text": "JDK 설정",
        "side.effects.warning.dialog.title": "부작용 발견",
        "simplify.boolean.expression.family": "부울 표현식 간소화",
        "simplify.boolean.expression.text": "''{0}''을(를) {1}(으)로 간소화",
        "fix.super.method.return.type.family": "슈퍼 메서드 반환 타입 수정",
        "fix.super.method.return.type.text": "''{0}''이(가) ''{1}''을(를) 반환하게 만들기",
        "surround.with.try.catch.fix": "try/catch로 둘러싸기",
        "make.final.family": "Final로 만들기",
        "fix.variable.type.family": "변수 타입 수정",
        "fix.variable.type.text": "{0} ''{1}'' 타입을 ''{2}''(으)로 변경",
        "fix.receiver.parameter.type.family": "수신자 매개변수 타입 수정",
        "fix.receiver.parameter.type.text": "둘러싸는 클래스 타입으로 변경",
        "fix.receiver.parameter.name.family": "수신자 매개변수의 이름 수정",
        "wrap.expression.using.static.accessor.family": "표현식 래핑",
        "wrap.expression.using.static.accessor.text": "''{0}()''을(를) 사용하여 래핑"
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
