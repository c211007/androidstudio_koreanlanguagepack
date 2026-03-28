import json
from pathlib import Path

def update_missing_keys():
    file_path = Path("missing_translations/missing_keys_korean.json")

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    ko_dict = {
        "override.implement.action.context.ivar.not.available.when.overridden": "\n  {0,choice,1#프로퍼티|2#프로퍼티들} {1}의 인스턴스 {0,choice,1#변수|2#변수들}가 사용되지만, \n  해당 접근자가 재정의되면 사용할 수 없게 됩니다. 계속 진행하시겠습니까?",
        "implement.methods.handler.no.members.message": "{0}에 구현할 메서드가 없습니다.",
        "implement.methods.handler.members.chooser.title": "구현할 메서드 선택",
        "override.implement.methods.handler.action.title": "메서드 재정의/구현",
        "override.implement.methods.handler.members.chooser.title": "재정의/구현할 메서드 선택",
        "override.implement.methods.handler.no.members.message": "{0}에 재정의/구현할 메서드가 없습니다.",
        "generate.cpp.handler.no.parents.message": "{0}할 클래스가 없습니다.",
        "generate.cpp.handler.parent.chooser.title": "대상 선택",
        "generate.cpp.handler.inplace.option": "인플레이스 생성(&P)",
        "generate.cpp.handler.show.existing.button": "기존 항목 표시(&S)",
        "generate.cpp.handler.replace.button": "기존 항목 교체(&R)",
        "generate.cpp.handler.add.missing.button": "누락된 항목 추가(&A)",
        "generate.cpp.handler.usages.string": "발생 항목",
        "generate.cpp.handler.usages.cannot.make": "생성을 완료할 수 없습니다. 일부 파일이 변경되었습니다.",
        "override.implement.show.optional.members": "선택적 멤버 표시(&O)",
        "override.implement.show.synthesized.accessors": "합성된(synthesized) 접근자 표시(&S)",
        "class.action.handler.no.members.message": "{0}에 {1}할 멤버가 없습니다.",
        "class.action.handler.invalid.for.selection": "현재 선택 항목에 대해 액션이 유효하지 않습니다.",
        "class.action.handler.action.title": "{0} 생성",
        "declare.action.context.interface": "인터페이스",
        "declare.action.context.private.category": "프라이빗 카터고리",
        "declare.action.context.implementation": "구현(선언하지 않음)",
        "declare.members.handler.action.title": "멤버 선언",
        "declare.members.handler.members.chooser.title": "선언할 멤버 선택",
        "declare.members.handler.no.members.message": "{0}에 선언할 멤버가 없습니다.",
        "generate.constructor.action.title": "생성자 생성",
        "generate.constructor.members.chooser.title": "초기화할 필드 선택",
        "generate.constructor.choose.base.class.constructor": "기본 클래스 생성자 선택",
        "generate.constructor.already.defined.message": "{0} 생성자가 이미 정의되어 있습니다.\\n계속하시겠습니까?",
        "generate.destructor.action.title": "소멸자 생성",
        "generate.destructor.already.defined.message": "소멸자가 이미 정의되어 있습니다.\\n계속하시겠습니까?",
        "generate.cpp.getter.and.setter.action.title": "Getter 및 Setter 생성",
        "generate.cpp.getter.and.setter.members.chooser.title": "{0}할 필드 선택",
        "generate.cpp.getter.action.title": "Getter 생성",
        "generate.cpp.setter.action.title": "Setter 생성",
        "generate.definitions.handler.parent.chooser.title": "클래스/네임스페이스 선택",
        "generate.description.handler.include.member.names": "멤버 이름 포함(&I)",
        "generate.description.handler.action.title": "{0} 생성",
        "generate.encode.handler.action.title": "{0}/{1} 생성",
        "generate.encode.handler.no.members.message": "{0}에 인코딩 가능한 멤버가 없습니다.",
        "generate.initwith.handler.retain.objects": "객체 매개변수 유지(&R)",
        "generate.initwith.handler.use.setters": "프로퍼티 Setter 사용(&U)",
        "generate.initwith.handler.generate.class.constructor": "\"+objectWith...\" 생성(&G)",
        "generate.initwith.handler.action.title": "{0} 생성",
        "generate.initwith.handler.members.chooser.title": "초기화할 멤버 선택",
        "generate.isequal.and.hash.handler.action.title": "{0} 및 {1} 생성",
        "generate.ivars.handler.show.synthesized": "합성된(synthesized) 프로퍼티 표시(&S)",
        "generate.ivars.handler.action.title": "프로퍼티에서 인스턴스 변수 생성",
        "generate.ivars.handler.members.chooser.title": "인스턴스 변수로 만들 프로퍼티 선택",
        "generate.ivars.handler.no.members.message": "{0}에 인스턴스 변수를 생성할 프로퍼티가 없습니다."
    }

    filename = "OCGenerateBundle.properties"
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
