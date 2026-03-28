import json
from pathlib import Path

def update_missing_keys():
    file_path = Path("missing_translations/missing_keys_korean.json")
    
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    ko_dict = {
        "native.gradle.name.short": "Native",
        "gradle.name": "Gradle",
        "error.incompatible.libraries.title": "호환되지 않는 Kotlin/Native 라이브러리", 
        "error.incompatible.libraries": "프로젝트에 연결된 Kotlin/Native {1} 배포판의 라이브러리가 {0,choice,1#1개|2#{0}개} 있습니다: {2}",
        "error.incompatible.libraries.newer": "이러한 라이브러리는 최신 Kotlin/Native 컴파일러로 컴파일되었으므로 IDE에서 읽을 수 없습니다.",
        "error.incompatible.libraries.older": "이러한 라이브러리는 이전 Kotlin/Native 컴파일러로 컴파일되었으므로 IDE에서 읽을 수 없습니다.",
        "error.incompatible.libraries.recipe": "Gradle 빌드 파일을 편집하여 Kotlin Gradle 플러그인 버전 {0}을(를) 사용하세요. 그런 다음 IDE에서 프로젝트를 다시 가져오세요.",
        "error.incompatible.3p.libraries.newer": "프로젝트에 연결된 타사 라이브러리 중 최신 Kotlin/Native 컴파일러로 컴파일되어 IDE에서 읽을 수 없는 라이브러리가 {0,choice,1#1개|2#{0}개} 있습니다:",
        "error.incompatible.3p.libraries.older": "프로젝트에 연결된 타사 라이브러리 중 이전 Kotlin/Native 컴파일러로 컴파일되어 IDE에서 읽을 수 없는 라이브러리가 {0,choice,1#1개|2#{0}개} 있습니다:",
        "error.incompatible.3p.libraries.recipe": "Gradle 빌드 파일을 편집하고 Kotlin/Native {0}과(와) 호환되는 라이브러리 버전을 지정하세요. 그런 다음 IDE에서 프로젝트를 다시 가져오세요.",
        "error.incompatible.user.libraries.newer": "프로젝트에 연결된 라이브러리 중 최신 Kotlin/Native 컴파일러로 컴파일되어 IDE에서 읽을 수 없는 타사 라이브러리가 {0,choice,1#1개|2#{0}개} 있습니다:",    
        "error.incompatible.user.libraries.older": "프로젝트에 연결된 라이브러리 중 이전 Kotlin/Native 컴파일러로 컴파일되어 IDE에서 읽을 수 없는 타사 라이브러리가 {0,choice,1#1개|2#{0}개} 있습니다:",   
        "error.incompatible.user.libraries.recipe": "Gradle 빌드 파일을 편집하여 Kotlin Gradle 플러그인 버전 {0}을(를) 사용하세요. 그런 다음 프로젝트를 다시 빌드하고 IDE에서 다시 가져오세요.",
        "library.name.0.at.1.relative.root": "{1}의 \"{0}\"",
        "auto.configure.kotlin.documentation.gradle.url": "https://kotl.in/configure-kotlin-with-gradle"
    }
    
    filename = "KotlinGradleCodeInsightCommonBundle.properties"
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
