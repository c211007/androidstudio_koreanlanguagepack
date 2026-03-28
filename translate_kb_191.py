import json
from pathlib import Path

def update_missing_keys():
    file_path = Path("missing_translations/missing_keys_korean.json")

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    ko_dict = {
        "form.preview.title": "폼 미리보기",
        "form.menu.preview": "미리보기",
        "form.menu.preview.mnemonic": "P",
        "form.menu.file.exit": "종료",
        "form.menu.laf": "모양 및 느낌",
        "form.menu.laf.mnemonic": "L",
        "form.menu.view.pack": "압축(Pack)",
        "error.cannot.change.look.feel": "모양 및 느낌(LookAndFeel)을 변경할 수 없습니다.\\n이유: {0}",
        "error.title": "오류",
        "junit.runner.error": "오류: {0}",
        "junit.class.not.found": "클래스를 찾을 수 없습니다: \"{0}\"",
        "junit.cannot.instantiate.tests": "테스트를 인스턴스화할 수 없습니다: {0}",
        "junit.class.not.derived": "{0}이(가) TestCase에서 파생되지 않았습니다. 메서드 이름을 지정하지 마세요.",
        "junit.suite.must.be.static": "''{0}.suite()'' 메서드는 정적(static)이어야 합니다.",
        "junit.failed.to.invoke.suite": "suite()를 호출하지 못했습니다: {0}",
        "junit.method.not.found": "''{0}'' 메서드를 찾을 수 없습니다.",
        "tests.found.in.package": "패키지 ''{1}''에서 테스트 클래스 {0}개가 발견되었습니다."
    }

    filename = "RuntimeBundle.properties"
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
