import json

translations = {
  "completion.kind.sorter.ml.kotlin": "Kotlin",
  "presentation.tail.for.0.in.1": "\"\\ {1}의 {0}\""
}

with open("missing_translations/missing_keys_korean.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for file_info in data.get("new_files", []):
    if file_info.get("filename") == "TurboCompleteKotlin.properties":
        keys_dict = file_info.get("keys", file_info.get("properties", {}))
        keys_dict.update(translations)
        file_info["keys"] = keys_dict
        break
else:
    data.setdefault("new_files", []).append({
        "filename": "TurboCompleteKotlin.properties",
        "keys": translations
    })

with open("missing_translations/missing_keys_korean.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)
