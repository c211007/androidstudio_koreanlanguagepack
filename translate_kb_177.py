import json
from pathlib import Path

def update_missing_keys():
    file_path = Path("missing_translations/missing_keys_korean.json")

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    ko_dict = {
        "wrap.expression.using.static.accessor.text.role": "''{0}()''을(를) 사용하여 {1} 래핑",
        "replace.with.qualifier.text": "한정자로 교체",
        "replace.with.qualifier.text.role": "{0}을(를) 한정자로 교체",
        "side.effect.action.remove": "제거(&R)",
        "side.effect.action.transform": "변환(&T)",
        "side.effect.action.cancel": "취소(&C)",
        "change.parameter.class.family": "매개변수 클래스 변경",
        "change.extends.list.family": "다음에서 클래스 상속",
        "add.class.to.extends.list": "''{0}''이(가) ''{1}''을(를) 상속하게 만들기",
        "remove.class.from.extends.list": "''{0}''이(가) ''{1}''을(를) 상속하지 않게 만들기",
        "add.interface.to.implements.list": "''{0}''이(가) ''{1}''을(를) 구현하게 만들기",
        "remove.interface.from.implements.list": "''{0}''이(가) ''{1}''을(를) 구현하지 않게 만들기",
        "create.field.text": "{0} 필드 만들기",
        "create.property.text": "{0} 속성 만들기",
        "add.constructor.parameter.name": "생성자 매개변수 추가",
        "remove.suppression.action.name": "''{0}'' 억제 제거",
        "remove.suppression.action.family": "억제 제거",
        "remove.qualifier.action.text": "한정자 제거",
        "fix.argument.family": "인수 수정",
        "change.new.operator.type.text": "''{0}''을(를) ''new {1}{2}''(으)로 변경",
        "change.new.operator.type.family": "새 연산자 타입 변경",
        "fix.unused.symbol.injection.family": "종속성 주입 어노테이션에 추가",
        "fix.unused.symbol.injection.text": "''{0}''(으)로 어노테이션된 경우 사용되지 않음 경고 억제",
        "fix.add.write.annotation.text": "''@{0}''(으)로 어노테이션된 필드를 암시적으로 작성된 것으로 간주",
        "fix.add.write.annotation.description": "암시적으로 작성된 필드를 표시하는 어노테이션 목록에 ''@{0}''을(를) 추가합니다.<p>이 목록은 ''진입점 | 예약된 어노테이션'' 아래의 ''사용되지 않는 선언'' 검사 설정에서 편집할 수 있습니다.",
        "fix.add.special.annotation.family": "특수 어노테이션 목록에 추가",
        "fix.add.special.annotation.text": "특수 어노테이션 목록에 ''{0}'' 추가",
        "orderEntry.fix.add.dependency.on.module": "모듈 ''{0}''에 대한 종속성 추가",
        "orderEntry.fix.add.dependency.on.module.choose": "모듈에 대한 종속성 추가...",
        "orderEntry.fix.choose.module.to.add.dependency.on": "종속성을 추가할 모듈 선택",
        "orderEntry.fix.family.add.module.dependency": "모듈 종속성 추가",
        "orderEntry.fix.add.library.to.classpath": "클래스 경로에 라이브러리 ''{0}'' 추가",
        "orderEntry.fix.family.add.library.to.classpath": "클래스 경로에 라이브러리 추가",
        "orderEntry.fix.family.add.library.to.classpath.options": "클래스 경로에 라이브러리 추가...",
        "popup.title.choose.library.to.add.dependency.on": "종속성을 추가할 라이브러리 선택",
        "orderEntry.fix.circular.dependency.warning": "모듈 ''{0}''에 대한 종속성을 추가하면 모듈 ''{1}''과(와) ''{2}'' 사이에 순환 종속성이 발생합니다.\\n그래도 종속성을 추가하시겠습니까?",
        "orderEntry.fix.title.circular.dependency.warning": "순환 종속성 경고",
        "static.import.method.text": "정적 메서드 가져오기",
        "static.import.method.kind.text": "정적 메서드",
        "static.import.method.choose.method.to.import": "가져올 메서드 선택",
        "static.import.constant.text": "정적 상수 가져오기",
        "static.import.constant.kind.text": "정적 상수",
        "add.library.title.dialog": "프로젝트에 ''{0}'' 라이브러리 추가",
        "add.library.title.choose.folder": "디렉터리 선택",
        "add.library.description.choose.folder": "라이브러리를 복사할 디렉터리를 선택하세요.",
        "add.library.error.not.found": "라이브러리 파일 ''{0}''이(가) 존재하지 않습니다.",
        "add.library.error.cannot.copy": "''{0}''을(를) ''{1}''(으)로 복사할 수 없습니다.\\n({2})",
        "add.library.use.bundled.library.radio.button": "{1} 배포판의 ''{0}'' 사용(&U)",
        "add.library.copy.files.to.radio.button": "다음에 ''{0}'' 라이브러리 파일 복사(&C):",
        "permute.arguments": "인수 순열 생성"
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
