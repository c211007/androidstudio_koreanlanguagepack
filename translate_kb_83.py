import json
from pathlib import Path

def update_missing_keys():
    file_path = Path("missing_translations/missing_keys_korean.json")
    
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    ko_dict = {
        "configure.kotlin.progress.title": "Kotlin 구성",
        "welcome.promo.start.tour.java": "Java 투어 시작",
        "welcome.promo.start.tour.kotlin": "Kotlin 투어 시작",
        "kotlin.onboarding.invoke.intention.for.warning.1": "방금 버그를 수정했지만, 이 코드를 더 깔끔하게 만들 수 있습니다. \n  IntelliJ IDEA는 개선할 수 있는 코드 줄을 강조 표시하고 노란색 전구를 추가합니다.",
        "kotlin.onboarding.invoke.intention.for.warning.2": "경고를 미리 보고 빠른 수정을 적용하려면 {0}을(를) 누르세요.",
        "kotlin.onboarding.invoke.intention.for.warning.balloon": "사용 가능한 빠른 수정을 표시하려면 {0}을(를) 누르세요.",
        "kotlin.onboarding.select.fix": "{0} 빠른 수정을 적용하세요. 사용하지 않는 로컬 변수를 제거합니다.",
        "kotlin.onboarding.invoke.intention.for.code": "의도 액션은 시간을 절약하고 코딩을 더 쉽게 만들어줍니다. 의도 액션을 사용하여 문자열 연결 형식을 다시 지정해 보겠습니다. \n  가능한 옵션을 표시하려면 {0}을(를) 누르세요.",
        "kotlin.onboarding.invoke.intention.for.code.balloon": "사용 가능한 의도 액션을 표시하려면 {0}을(를) 누르세요.",
        "kotlin.onboarding.apply.intention": "{0}을(를) 선택하고 {1}을(를) 누르세요.",
        "kotlin.basic.completion.choose.item": "강조 표시된 {0} 항목을 선택하여 함수 호출을 완료하고 캐럿을 괄호 안으로 이동하세요.",
        "kotlin.refactoring.menu.inline.property.eng": "이제 {0} 변수의 단일 사용을 그것을 정의하는 표현식으로 대체해 보겠습니다. \n  {1}을(를) 누르고 리팩터링 메뉴를 <strong>ipr</strong>(<strong>i</strong>nline <strong>pr</strong>operty)로 필터링할 수 있습니다. \n  이 항목을 선택하거나 {2}을(를) 누르세요.",
        "kotlin.refactoring.menu.confirm.constant": "상수에 사용할 새 이름을 선택하고 입력하세요. 그런 다음 {0}을(를) 눌러 확인합니다."
    }
    
    filename = "KotlinLessonsBundle.properties"
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
