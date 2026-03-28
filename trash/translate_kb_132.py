import json
from pathlib import Path

def update_missing_keys():
    file_path = Path("missing_translations/missing_keys_korean.json")
    
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    ko_dict = {
        "navigation.import.hierarchy.previous.occurence": "이전 파일로 이동",
        "navigation.goto.please.wait": "잠시 기다려주세요\\u2026",
        "navigation.goto.resolving.target": "대상 확인 중\\u2026",
        "naming.convention.title": "명명 규칙",
        "naming.convention.header.guard.style.help": "다음과 같은 미리 정의된 변수를 사용할 수 있습니다.<br><b>${PROJECT_NAME}</b>, <b>${PROJECT_REL_PATH}</b>, <b>${FILE_NAME}</b>, <b>${EXT}</b> 및 <b>${UUID}</b>.<br><i>편집기/파일 및 코드 템플릿</i>(<i>파일 탭</i>)의 모든 미리 정의된 변수도<br>사용할 수 있습니다(<b>${USER}</b>, <b>${DATE}</b> 등).",
        "naming.convention.entity.kind": "엔티티 종류",
        "naming.convention.visibility": "가시성",
        "naming.convention.specifier": "지정자",
        "naming.convention.entity.any": "모두",
        "naming.convention.entity.namespace": "네임스페이스",
        "naming.convention.entity.macro": "매크로",
        "naming.convention.entity.class": "클래스",
        "naming.convention.entity.struct": "구조체(Struct)",
        "naming.convention.entity.enumeration": "열거형(Enum)",
        "naming.convention.entity.union": "공용체(Union)",
        "naming.convention.entity.typedef": "Typedef",
        "naming.convention.entity.global.function": "전역 함수",
        "naming.convention.entity.global.variable": "전역 변수",
        "naming.convention.entity.class.member.function": "클래스 멤버 함수",
        "naming.convention.entity.struct.member.function": "구조체 멤버 함수",
        "naming.convention.entity.class.member.field": "클래스 멤버 필드",
        "naming.convention.entity.struct.member.field": "구조체 멤버 필드",
        "naming.convention.entity.enumerator": "열거자",
        "naming.convention.entity.parameter": "매개변수",
        "naming.convention.entity.local.variable": "로컬 변수",
        "naming.convention.prefix": "접두사",
        "naming.convention.suffix": "접미사",
        "refactoring.convertIvarUsagesToProperties": "ivar 사용을 프로퍼티로 변환(&C)",
        "refactoring.ambiguous": "모호한 함수는 리팩터링할 수 없습니다.",
        "refactoring.changeSignature.destructor": "소멸자는 리팩터링할 수 없습니다.",
        "title.function.return.type.group": "함수 반환 형식 다음",
        "title.function.top.return.type": "전역 및 네임스페이스 범위에서",
        "title.function.nontop.return.type": "클래스 범위에서",
        "title.function.parameters.group": "함수 선언 매개변수",
        "title.function.call.arguments.group": "함수 호출 인수",
        "title.template.decl.class.group": "템플릿 클래스 선언",
        "title.template.decl.func.group": "템플릿 함수 선언",
        "title.template.parameters.group": "템플릿 선언 매개변수",
        "title.template.call.arguments.group": "템플릿 인스턴스화 인수",
        "title.ctor.init.list.group": "생성자 초기화 목록",
        "title.superclass.list.group": "기본 클래스 목록",
        "title.shift.operators.group": "'<<', '>>' 연산자",
        "title.capture.list.group": "람다 캡처 목록",
        "title.structured.binding.list.group": "구조적 바인딩 목록",
        "wrapping.new.line.after.lt": "'<' 다음에 새 줄",
        "wrapping.gt.on.new.line": "'>'를 새 줄에 배치",
        "wrapping.align.multiline.parentheses": "여러 줄 괄호 맞춤",
        "wrapping.align.multiline.brackets": "여러 줄 대괄호 맞춤",
        "wrapping.align.multiline.lt.gt": "여러 줄 '<', '>' 맞춤",
        "wrapping.keep.simple.case.inline": "간단한 경우를 한 줄로 유지"
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
