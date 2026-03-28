import json
from pathlib import Path

def update_missing_keys():
    file_path = Path("missing_translations/missing_keys_korean.json")
    
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    ko_dict = {
        "override.implement.cpp.action.noMember": "{0}에 재정의/구현할 함수가 없습니다.",
        "override.implement.cpp.action.noParent": "재정의/구현할 함수가 없습니다.",
        "override.implement.cpp.action.insertOverride": "\"override\" 속성 삽입(&I)",
        "override.implement.cpp.action.showNonVirtual": "비가상 함수 표시(&N)",
        "override.implement.cpp.action.insertVirtualWithOverride": "\"override\"와 함께 \"virtual\" 속성 삽입",
        "implement.cpp.action.name": "함수 구현\\u2026",
        "implement.cpp.action.memberChooserTitle": "구현할 함수 선택",
        "implement.cpp.action.noMember": "{0}에 구현할 함수가 없습니다.",
        "implement.cpp.action.noParent": "구현할 함수가 없습니다.",
        "changeSignature.usages.cantBeUnnamed": "{0} 매개변수가 사용 중이므로 이름을 해제할 수 없습니다.",
        "changeSignature.usages.cantBeRemoved": "{0} 매개변수가 사용 중이므로 제거할 수 없습니다.",
        "changeSignature.usages.cantConvertSelectorToFuncBlock": "선택자 표현식을 함수/블록으로 변환할 수 없습니다.",
        "changeSignature.usages.cantConvertToBlock": "블록으로 변환할 수 없습니다:",
        "changeSignature.usages.cantConvertLanguage": "{0} 코드의 사용을 변환할 수 없습니다.",
        "changeSignature.usages.noUsagesFound": "사용을 찾을 수 없습니다.",
        "changeSignature.usages.moreThan1Found": "1개 이상의 사용을 찾았습니다.",
        "changeSignature.usages.usageInsideFunction": "함수/메서드 내에서 사용됩니다.",
        "changeSignature.usages.functionHasSeveralDefinitions": "''{0}'' 함수에 여러 정의가 있습니다.",
        "changeSignature.usages.atLeasTwoParams": "적어도 두 개의 매개변수 이름이 ''{0}''입니다.",
        "changeSignature.usages.conflictsWithNewParameter": "{0}이(가) 새 매개변수와 충돌합니다.",
        "changeSignature.usages.unrelatedSelector": "이름이 같은 잠재적으로 관련 없는 선택자의 이름이 바뀝니다.",
        "changeSignature.usages.willConflictWith": "{0}이(가) {1}와(과) 충돌합니다.",
        "changeSignature.usages.willConflictWithMethod": "{0}이(가) {1}의 메서드와 충돌합니다.",
        "changeSignature.targetNotFound": "캐럿은 함수, 메서드 또는 블록에 위치해야 합니다.",
        "changeSignature.dialog.containing.class": "포함하는 클래스:",
        "changeSignature.dialog.callable.type": "호출 가능한 형식:",
        "changeSignature.parameter.selector.part": "선택자 부분:",
        "changeSignature.explicit.constructor.checkbox": "Explicit",
        "changeSignature.const.member.function.checkbox": "Const",
        "changeSignature.constexpr.function.checkbox": "Constexpr(&C)",
        "changeSignature.noexcept.function.checkbox": "Noexcept(&X)",
        "rename.renameAssociatedFiles": "연결된 파일의 이름도 바꾸시겠습니까?",
        "rename.renameContainingFile": "포함하는 파일의 이름도 바꾸시겠습니까?",
        "rename.renameAssociatedClass": "연관된 클래스/구조체의 이름도 바꿉니다.",
        "rename.searchForMacros": "전역 범위에서 (이름이 바뀐 요소를 포함하는) ''{0}'' 매크로의 사용을 검색하시겠습니까?",
        "find.existing.operators.progress.title": "기존 연산자 검색 중",
        "generate.definitions.intention.familyName": "정의 생성",
        "generate.definitions.intention.outsideText": "정의 생성",
        "generate.definitions.intention.inlineText": "내부 정의 생성",
        "generate.definitions.action.name": "정의 생성\\u2026",
        "generate.definitions.action.title": "정의 생성",
        "generate.definitions.action.memberChooserTitle": "정의를 생성할 함수 선택",
        "generate.definitions.action.noParent": "정의를 생성할 함수가 없습니다.",
        "generate.definitions.action.noMembers": "{0}에 정의를 생성할 함수가 없습니다.",
        "generate.definitions.quickfix.inlineText": "{0}에 대한 내부 정의 생성",
        "generate.definitions.quickfix.outsideText": "{0}에 대한 정의 생성",
        "generate.definitions.progress.text": "기존 정의 찾는 중\\u2026",
        "generate.comparison.operators.action.title": "비교 연산자 생성",
        "generate.comparison.operators.action.title.eq": "동등 연산자 생성",
        "generate.comparison.operators.action.title.rel": "관계 연산자 생성"
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
