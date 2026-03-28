import json
import os

translated_keys = {
  "changes.nodetitle.empty.changelist.name": "<빈 이름>",
  "shelve.default.path.rendering": "<프로젝트 루트>",
  "changes.nodetitle.changecount": "{0,choice, 0#파일 없음|1#1개의 파일|2#{0}개의 파일}",
  "changes.nodetitle.directory.changecount": "{0,choice, 0#디렉토리 없음|1#1개의 디렉토리|2#{0}개의 디렉토리}",
  "changes.nodetitle.directory.file.changecount": "{0,choice, 0#디렉토리 없음|1#1개의 디렉토리|2#{0}개의 디렉토리} 및 {1,choice, 0#파일 없음|1#1개의 파일|2#{1}개의 파일}"
}

file_path = "c:/Users/klanary/Desktop/vscode 모음/android_korean/androidstudio_koreanlanguagepack/missing_translations/missing_keys_korean.json"
with open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)

for item in data["new_files"]:
    if item["filename"] == "VcsFrontendBundle.properties":
        item["keys"].update(translated_keys)
        break

with open(file_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("VcsFrontendBundle translated successfully.")