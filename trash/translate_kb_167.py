import json
from pathlib import Path

def update_missing_keys():
    file_path = Path("missing_translations/missing_keys_korean.json")

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    ko_dict = {
        "web.inspection.message.attribute.does.not.accept.value": "{0}은(는) 값을 허용하지 않습니다.",
        "web.inspection.message.attribute.value.no.valid": "{0}은(는) {1}에 대해 유효한 값이 아닙니다. 예상됨: {2}",
        "web.inspection.message.segment.missing": "누락된 {0}",
        "web.inspection.message.segment.unrecognized-identifier": "인식할 수 없는 {0}",
        "web.inspection.message.segment.duplicated": "중복된 {0}",
        "web.inspection.message.segment.default-subject": "이름",
        "web.inspection.message.deprecated.symbol.explanation": "더 나은 대안은 문서를 참조하세요.",
        "web.inspection.message.deprecated.symbol.since": "#ref은(는) {0}부터 더 이상 사용되지 않습니다.",
        "web.inspection.message.deprecated.symbol.message": "#ref은(는) 더 이상 사용되지 않습니다.",
        "web.inspection.message.obsolete.symbol.since": "#ref은(는) {0}부터 사용되지 않습니다.",
        "web.inspection.message.obsolete.symbol.message": "#ref은(는) 사용되지 않습니다.",
        "mdn.documentation.section.status.Since": "이후",
        "mdn.documentation.section.status.DeprecatedSince": "이후로 사용되지 않음",
        "mdn.documentation.section.status.ObsoleteSince": "이후로 폐기됨",
        "mdn.documentation.section.status.Experimental": "실험적",
        "mdn.documentation.section.status.Deprecated": "더 이상 사용되지 않음",
        "mdn.documentation.section.status.Obsolete": "페기됨",
        "mdn.documentation.section.isRequired": "필수",
        "mdn.documentation.section.defaultValue": "기본값",
        "mdn.documentation.section.library": "라이브러리",
        "mdn.documentation.section.pattern": "패턴"
    }

    filename = "PolySymbolsBundle.properties"
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
