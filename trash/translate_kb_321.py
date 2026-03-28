import json
import os

translated_keys = {
  "vcs.show.quick.list": "VCS 빠른 목록 표시",
  "vcs.pull.requests": "풀 리퀘스트 표시",
  "vcs.use.integration": "VCS 통합 사용",
  "vcs.compare.file.versions": "파일 버전 비교",
  "vcs.partial.commit": "부분 커밋",
  "vcs.annotate": "Git Blame으로 어노테이션 추가"
}

file_path = "c:/Users/klanary/Desktop/vscode 모음/android_korean/androidstudio_koreanlanguagepack/missing_translations/missing_keys_korean.json"
with open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)

file_found = False
for item in data["new_files"]:
    if item["filename"] == "VcsProductivityFeatures.properties":
        item["keys"].update(translated_keys)
        file_found = True
        break

if not file_found:
    data["new_files"].append({
        "filename": "VcsProductivityFeatures.properties",
        "keys": translated_keys
    })

with open(file_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("VcsProductivityFeatures translated successfully.")