import json
from pathlib import Path

def update_missing_keys():
    file_path = Path("missing_translations/missing_keys_korean.json")

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    ko_dict = {
        "generate.method.handler.declare.in.interface": "인터페이스에 선언(&D)",
        "generate.method.handler.members.chooser.title": "멤버 선택",
        "generate.method.handler.method.already.defined": "{0}이(가) 이미 정의되어 있습니다.\\n기존 메서드를 교체하시겠습니까?",
        "generate.properties.handler.show.synthesized": "합성된(synthesized) 프로퍼티와 사용되는 ivar 표시(&I)",
        "generate.properties.handler.convert.usages": "ivar 사용을 프로퍼티로 변환(&C)",
        "generate.properties.handler.members.chooser.title": "프로퍼티로 만들 인스턴스 변수 선택",
        "generate.properties.handler.action.title": "인스턴스 변수에서 프로퍼티 생성",
        "generate.properties.handler.no.instance.variables": "{0}에 프로퍼티를 생성할 인스턴스 변수가 없습니다.",
        "generate.shared.instance.handler.action.title": "공유된 인스턴스(Shared Instance) 메서드 생성"
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
