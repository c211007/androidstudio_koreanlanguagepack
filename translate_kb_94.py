import json
from pathlib import Path

def update_missing_keys():
    file_path = Path("missing_translations/missing_keys_korean.json")
    
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    ko_dict = {
        "onboarding.run.comment": "코드를 실행하려면 {0}을(를) 누르거나 거터의 녹색 화살표 버튼을 클릭하세요.",
        "onboarding.debug.comment.1": "코드 디버깅을 시작하려면 {0}을(를) 누르세요. 중단점 하나가 설정되어 있습니다.",
        "onboarding.debug.comment.2": "하지만 언제든지 {0}을(를) 눌러 추가할 수 있습니다.",
        "onboarding.run.comment.render.1": "코드를 <b>실행</b>하려면 {0}을(를) 누르거나",
        "onboarding.run.comment.render.2": "거터의 {0} 아이콘을 클릭하세요.",
        "onboarding.show.intention.tip.comment.render.1": "강조 표시된 텍스트에 캐럿을 놓고 {0}을(를) 누르면",
        "onboarding.show.intention.tip.comment.render.2": "{0}이(가) 이 문제를 어떻게 수정하도록 제안하는지 확인할 수 있습니다.",
        "onboarding.debug.comment.render.1": "코드 디버깅을 시작하려면 {0}을(를) 누르세요. {1} 중단점 하나가 설정되어 있습니다.",
        "onboarding.debug.comment.render.2": "하지만 언제든지 {0}을(를) 눌러 추가할 수 있습니다."
    }
    
    filename = "KotlinNewProjectWizardBundle.properties"
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
