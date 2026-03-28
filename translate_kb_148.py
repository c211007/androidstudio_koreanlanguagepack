import json

ko_dict = {
  "action.com.jetbrains.cidr.lang.modulemap.RebuildModuleMapsInternalAction.text": "모듈 맵 다시 빌드",
  "oc.resolve.widget.display.name": "OC 확인 컨텍스트 패널",
  "c.cpp.0.code.folding": "{0} 코드 접기",
  "livetemplate.description.iter": "범위 반복(C++11)",
  "livetemplate.description.itit": "begin/end 멤버 함수를 사용하여 반복",
  "livetemplate.description.for": "색인이 생성된 for(;;) 루프"
}

with open("missing_translations/missing_keys_korean.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for item in data.get("new_files", []):
    if item["filename"] == "OCBundle.properties":
        item["keys"].update(ko_dict)
        print("Updated OCBundle.properties")
        break

with open("missing_translations/missing_keys_korean.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
