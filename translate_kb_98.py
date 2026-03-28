import json
from pathlib import Path

def update_missing_keys():
    file_path = Path("missing_translations/missing_keys_korean.json")
    
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    ko_dict = {
        "parcelize.fix.annotate.containing.class.with.parcelize": "포함하는 클래스에 '@Parcelize' 주석 달기",
        "parcelize.fix.add.ignored.on.parcel.annotation": "'@IgnoredOnParcel' 주석 추가",
        "parcelize.fix.add.empty.primary.constructor": "빈 기본 생성기 추가",
        "parcelize.fix.add.parcelable.supertype": "'Parcelable' 상위 타입 추가",
        "parcelize.fix.remove.redundant.type.parceler.annotation": "중복된 '@TypeParceler' 주석 제거",
        "parcelize.fix.migrate.to.parceler.companion.object": "'Parceler' 동반 객체로 마이그레이션",
        "parcelize.fix.remove.custom.creator.property": "사용자 지정 'CREATOR' 속성 제거",
        "parcelize.fix.remove.custom.write.to.parcel.function": "사용자 지정 'writeToParcel()' 함수 제거"
    }
    
    filename = "KotlinParcelizeBundle.properties"
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
