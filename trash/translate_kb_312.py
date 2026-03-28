import json
import os

translated_keys = {
  "activity.name.apply.patch": "패치 적용",
  "activity.name.unshelve": "선반에서 빼기",
  "commit.from.gutter.placeholder": "이 변경 사항을 커밋",
  "diff.title.revision.tooltip": "[{0}] {1}<br/><br/>작성자: {2}, 날짜: {3}",
  "action.Vcs.Commit.CloseDialog.text": "커밋 대화 상자 닫기",
  "group.ChangesView.ViewOptions.text": "보기 옵션"
}

file_path = "c:/Users/klanary/Desktop/vscode 모음/android_korean/androidstudio_koreanlanguagepack/missing_translations/missing_keys_korean.json"
with open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)

for item in data["new_files"]:
    if item["filename"] == "VcsBundle.properties":
        item["keys"].update(translated_keys)
        break

with open(file_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Batch 25 translated successfully.")