import json

translations = {
  "studio.bot.google.one.see.available.plans.header": "사용 가능한 요금제 보기",    
  "studio.bot.google.one.see.available.plans.link": "https://one.google.com/u/1/ai?g1_landing_page=75"
}

with open("missing_translations/missing_keys_korean.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for file_info in data.get("new_files", []):
    if file_info.get("filename") == "StudioGeminiBundle.properties":
        keys_dict = file_info.get("keys", file_info.get("properties", {}))
        keys_dict.update(translations)
        file_info["keys"] = keys_dict
        break

with open("missing_translations/missing_keys_korean.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)
