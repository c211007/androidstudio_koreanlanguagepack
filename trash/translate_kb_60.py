import json
from pathlib import Path

def update_missing_keys():
    file_path = Path("missing_translations/missing_keys_korean.json")
    
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    ko_dict = {
        "kotlin.debugger.feedback.notification.request.title": "Kotlin 코드 디버깅에 대한 피드백을 공유해 주세요",
        "kotlin.debugger.feedback.system.info.number.debugger.usages": "디버거 사용 횟수:",
        "kotlin.debugger.feedback.dialog.top.title": "피드백",
        "kotlin.debugger.feedback.dialog.title": "Kotlin 코드 디버깅에 대한 피드백을 공유해 주세요",
        "kotlin.debugger.feedback.question.1.title": "{0}에서 Kotlin 코드를 디버깅한 경험을 어떻게 평가하시나요?",
        "kotlin.debugger.feedback.question.2.title": "지난 3개월 동안 Kotlin 디버깅 경험이 어떻게 달라졌나요?",
        "kotlin.debugger.feedback.question.2.option.1": "이전보다 개선됨",       
        "kotlin.debugger.feedback.question.2.option.2": "동일함",
        "kotlin.debugger.feedback.question.2.option.3": "더 나빠짐",
        "kotlin.debugger.feedback.question.2.option.4": "이전에 {0}에서 Kotlin 디버거를 사용한 적이 없습니다.",
        "kotlin.debugger.feedback.question.3.title": "Kotlin 디버깅 개선을 위한 제안 사항을 공유해 주세요.",
        "kotlin.debugger.notification.thanks.feedback.content": "Kotlin 디버거를 개선하는 데 도움을 주셔서 감사합니다!",
        "kotlin.debugger.feedback.notification.test.name": "Kotlin 디버거 피드백 테스트 작업 표시"
    }
    
    filename = "KotlinDebuggerFeedbackSurveyBundle.properties"
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
