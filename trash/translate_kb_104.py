import json
from pathlib import Path

def update_missing_keys():
    file_path = Path("missing_translations/missing_keys_korean.json")
    
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    ko_dict = {
        "run.configuration.error.no.module": "모듈이 지정되지 않았습니다.",
        "run.configuration.error.no.main.class": "메인 클래스가 지정되지 않았습니다.",
        "run.configuration.error.run.class.should.be.defined": "''{0}'' 구성에 대해 실행 클래스가 정의되어야 합니다.",
        "run.configuration.error.class.not.found": "''{1}'' 모듈에서 ''{0}'' 클래스를 찾을 수 없습니다.",
        "run.configuration.error.class.no.main.method": "''{0}'' 클래스에 ''main()'' 메서드가 없습니다.",
        "run.configuration.error.main.not.found.top.level": "''{0}'' 패키지에서 최상위 함수 ''main()''을 찾을 수 없습니다.",
        "script.choose.file": "스크립트 파일 선택",
        "could.not.find.script.file.0": "스크립트 파일을 찾을 수 없습니다: {0}",
        "file.was.not.specified": "파일이 지정되지 않았습니다.",
        "run.kotlin.script": "Kotlin 스크립트 실행",
        "name.kotlin.script": "Kotlin 스크립트",
        "language.name.kotlin": "Kotlin",
        "dialog.message.script.file.was.not.specified": "스크립트 파일이 지정되지 않았습니다.",
        "dialog.message.script.file.was.not.found.in.project": "프로젝트에서 스크립트 파일을 찾을 수 없습니다.",
        "compile.kotlin.scratch.file": "Kotlin 스크래치 파일 컴파일",
        "configuration.title.script.file": "스크립트 파일"
    }
    
    filename = "KotlinRunConfigurationsBundle.properties"
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
