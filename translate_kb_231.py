import json

translations = {
  "SplittingTabsToolWindow.newTab": "새 탭",
  "SplittingTabsToolWindow.close": "닫기",
  "SplittingTabsToolWindow.moveTabLeft": "탭을 왼쪽으로 이동",
  "SplittingTabsToolWindow.moveTabRight": "탭을 오른쪽으로 이동",
  "SplittingTabsToolWindow.renameTab": "탭 이름 바꾸기"
}

with open("missing_translations/missing_keys_korean.json", "r", encoding="utf-8") as f:
    data = json.load(f)

found = False
for file_info in data.get("new_files", []):
    if file_info.get("filename") == "SplittingTabsBundle.properties":
        keys_dict = file_info.get("keys", file_info.get("properties", {}))
        keys_dict.update(translations)
        file_info["keys"] = keys_dict
        found = True
        break

if not found:
    data.setdefault("new_files", []).append({
        "filename": "SplittingTabsBundle.properties",
        "keys": translations
    })

with open("missing_translations/missing_keys_korean.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)
