import json
from pathlib import Path

def update_missing_keys():
    file_path = Path("missing_translations/missing_keys_korean.json")

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    ko_dict = {
        "tooltip.matches": "정규식과 예제가 일치합니다!",
        "tooltip.more.input.expected": "더 많은 예제 입력이 필요합니다.",
        "tooltip.no.match": "정규식과 예제가 일치하지 않습니다.",
        "tooltip.pattern.is.too.complex": "정규식 패턴이 너무 복잡합니다.",
        "warning.duplicate.character.0.inside.character.class": "문자 클래스 내에 중복된 문자 ''{0}''이(가) 있습니다.",
        "warning.duplicate.predefined.character.class.0.inside.character.class": "문자 클래스 내에 중복된 사전 정의된 문자 클래스 ''{0}''이(가) 있습니다."
    }

    filename = "RegExpBundle.properties"
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
