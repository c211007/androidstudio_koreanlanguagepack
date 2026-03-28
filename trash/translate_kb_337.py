import json
import os

translated_keys = {
  "YAMLFoldingSettings.use.abbreviation": "접힌 키와 값을 다음으로 제한",
  "YAMLFoldingSettings.abbreviation.units.of.measurement": "{0,choice,1#자|2#자}"
}

file_path = "c:/Users/klanary/Desktop/vscode 모음/android_korean/androidstudio_koreanlanguagepack/missing_translations/missing_keys_korean.json"
with open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)

file_found = False
for item in data["new_files"]:
    if item["filename"] == "YAMLBundle.properties":
        item["keys"].update(translated_keys)
        file_found = True
        break

if not file_found:
    data["new_files"].append({
        "filename": "YAMLBundle.properties",
        "keys": translated_keys
    })

with open(file_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("YAMLBundle final batch translated successfully.")