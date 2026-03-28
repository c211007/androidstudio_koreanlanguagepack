import json
from pathlib import Path

def update_missing_keys():
    file_path = Path("missing_translations/missing_keys_korean.json")

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    ko_dict = {
        "relaxng.gutter.go-to-overridden-define": "재정의된 정의로 이동",
        "relaxng.gutter.go-to-overriding-defines": "재정의하는 정의로 이동",
        "filetype.relaxng.compact-syntax.description": "RELAX NG 컴팩트 구문",
        "relaxng.inspection.group-name": "RELAX NG",
        "relaxng.inspection.unresolved-reference.name": "확인할 수 없는 참조",
        "relaxng.inspection.unused-define.message": "참조되지 않은 정의",
        "relaxng.inspection.unused-define.name": "사용되지 않은 정의",
        "relaxng.message-viewer.warning.message": "{0}이(가) 아직 실행 중입니다. 그래도 닫으시겠습니까?",
        "relaxng.message-viewer.warning.title": "{0} 실행 중",
        "relaxng.message-viewer.tab-title.convert-schema": "스키마 변환",
        "relaxng.message-viewer.tab-title.validate-relax-ng": "RELAX NG 유효성 검사",
        "relaxng.parse.error.equals-expected": "=가 필요합니다.",
        "relaxng.parse.error.equals-orequals-or-andequals-expected": "=, |= 또는 \\\\&=가 필요합니다.",
        "relaxng.parse.error.identifier-expected": "식별자가 필요합니다.",
        "relaxng.parse.error.lbrace-expected": "{가 필요합니다.",
        "relaxng.parse.error.literal-expected": "리터럴이 필요합니다.",
        "relaxng.parse.error.name-class-expected": "이름 클래스가 필요합니다.",
        "relaxng.parse.error.namespace-expected": "'namespace'가 필요합니다.",
        "relaxng.parse.error.namespace-uri-or-inherit-expected": "네임스페이스 URI 또는 'inherit'가 필요합니다.",
        "relaxng.parse.error.pattern-expected": "패턴이 필요합니다.",
        "relaxng.parse.error.rbrace-expected": "}가 필요합니다.",
        "relaxng.parse.error.rparen-expected": ")가 필요합니다.",
        "relaxng.parse.error.uri-literal-expected": "URI 리터럴이 필요합니다.",
        "relaxng.quickfix.create-declaration.name": "{0} 선언 ''{1}'' 생성",
        "relaxng.quickfix.create-pattern.family": "패턴 생성",
        "relaxng.quickfix.create-pattern.name": "패턴 ''{0}'' 생성",
        "relaxng.quickfix.remove-define": "정의 제거",
        "relaxng.suppress.action.name": "{0}에 대해 억제",
        "relaxng.symbol.pattern-definition": "패턴 정의",
        "action.ConvertSchemaAction.text": "스키마 변환...",
        "action.ConvertSchemaAction.description": "선택한 스키마 문서(RNG, RNC, XSD, DTD)를 다른 형식으로 변환합니다.",
        "prefix": "접두사",
        "xml.validate.no.errors.detected.status.message": "오류가 감지되지 않았습니다."
    }

    filename = "RelaxngBundle.properties"
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
