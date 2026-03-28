import json
from pathlib import Path

def update_missing_keys():
    file_path = Path("missing_translations/missing_keys_korean.json")
    
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    ko_dict = {
        "inspection.migration.title": "코드 마이그레이션",
        "inspection.migration.profile.name": "마이그레이션",
        "configuration.migration.text.detected.migration": "감지된 마이그레이션:",
        "configuration.migration.text.language.version": "언어 버전: {0}에서 {1}(으)로",
        "configuration.migration.text.api.version": "API 버전: {0}에서 {1}(으)로",
        "configuration.migration.title.kotlin.migration": "Kotlin 마이그레이션",
        "configuration.migration.text.update.your.code.to.replace.deprecated": "코드를 업데이트하여 사용되지 않는 언어 및 라이브러리 기능 사용을 지원되는 구성으로 바꿉니다.",
        "configuration.migration.text.scan.for.deprecations": "사용 중단 사항 스캔",
        "kotlin.external.compiler.updates.notification.content.0": "Kotlin 버전 {0}을(를) 사용할 수 있습니다.",
        "kotlin.external.compiler.updates.notification.learn.what.is.new.action": "새로운 기능 알아보기"
    }
    
    filename = "KotlinMigrationBundle.properties"
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
