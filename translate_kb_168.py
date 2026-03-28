import json
from pathlib import Path

def update_missing_keys():
    file_path = Path("missing_translations/missing_keys_korean.json")

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    ko_dict = {
        "prediction.services.settings.title": "다음 편집 예측",
        "prediction.services.settings.enable.title": "다음 편집 예측 사용",
        "prediction.services.settings.policy.title": "집계 정책:",
        "prediction.services.settings.policy.comment": "제안을 검토 가능한 컨트롤로 그룹화하는 방법을 결정합니다.",
        "prediction.services.settings.delay.title": "자동 제안 지연 시간:",
        "prediction.services.settings.delay.comment": "제안을 트리거하기 전 대기할 밀리초입니다.",
        "prediction.services.settings.max.documents.title": "최대 문서 수:",
        "prediction.services.settings.max.changes.title": "문서당 최대 변경 수:",
        "prediction.services.settings.ignore.outdated.title": "오래된 제안 무시",
        "prediction.services.settings.show.within.lines": "다음 줄 이내에 자동 표시:",
        "prediction.services.settings.show.within.lines.comment": "캐럿 기준 이 줄 수 내의 제안이 자동으로 표시됩니다.",
        "prediction.services.settings.model.title": "모델 선택",
        "prediction.services.jump.to.suggestion": "위로 이동하려면 {0} (줄 {1})",
        "prediction.services.scroll.to.active.suggestion": "활성 제안으로 편집기 스크롤",
        "prediction.services.hint.accept": "수락하려면",
        "prediction.services.hint.move": "이곳으로 이동하려면",
        "prediction.services.hint.show": "표시하려면"
    }

    filename = "PredictionServicesBundle.properties"
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
