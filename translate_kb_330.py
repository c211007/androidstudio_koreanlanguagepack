import json
import os

translated_keys = {
  "dom.quickfix.add.element.name": "<{0}> 요소 추가",
  "dom.quickfix.add.attribute.name": "\"{0}\" 속성 추가",
  "dom.quickfix.add.element.family": "속성/요소 추가",
  "dom.quickfix.create.new.element.name": "새 {0} ''{1}'' 생성",
  "dom.quickfix.create.new.element.family": "새 요소 생성",
  "dom.quickfix.create.new.element.choose.file.title": "파일 선택",
  "dom.quickfix.remove.element.name": "<{0}> 요소 제거",
  "dom.quickfix.remove.attribute.name": "\"{0}\" 속성 제거",
  "dom.quickfix.remove.element.family": "속성/요소 제거",
  "dom.quickfix.define.attribute.text": "{0} 속성 정의",
  "dom.quickfix.define.attribute.family": "속성 정의",
  "dom.quickfix.insert.required.tag.family": "필수 하위 태그 삽입",
  "dom.quickfix.insert.required.tag.text": "필수 하위 태그 {0} 삽입",
  "dom.inspections.invalid.value.quotation": "''{0}''에 대한 잘못된 인용",
  "dom.inspections.identity.in.other.file": "이름이 같은 {0}이(가) ''{1}'' 파일에 이미 있습니다.",
  "dom.inspections.identity": "이름이 같은 {0}이(가) 이미 존재합니다.",
  "dom.inspections.value.must.be.identifier": "값은 식별자여야 합니다.",
  "dom.inspections.value.must.not.be.empty": "값은 비워둘 수 없습니다.",
  "dom.inspections.attribute.0.should.be.defined": "''{0}'' 속성을 정의해야 합니다.",
  "dom.inspections.child.tag.0.should.be.defined": "''{0}'' 하위 태그를 정의해야 합니다",
  "dom.usage.type": "XML 설명자(descriptor)에서",
  "dom.converter.cannot.convert.default": "잘못된 값: ''{0}''",
  "dom.converter.unknown.enum.value": "알 수 없는 enum 값 ''{0}''",
  "dom.converter.format.exception": "''{0}'' 문자열을 대상 클래스 ''{1}''(으)로 변환할 수 없습니다.",
  "dom.converter.format.exception.empty.string": "빈 문자열을 대상 클래스 ''{0}''(으)로 변환할 수 없습니다.",
  "dom.converter.value.should.be.integer": "값은 정수여야 합니다.",
  "dom.action.remove": "제거(&E)",
  "dom.action.remove.elements": "{0} 제거(&E)",
  "dom.action.edit": "편집",
  "dom.action.add": "추가",
  "dom.dialog.message.remove.elements": "{0}을(를) 제거하시겠습니까?",
  "dom.tree.children.contain.errors": "하위 항목에 오류가 있습니다.",
  "dom.tree.remove.xml.element.dialog.title": "제거",
  "caption.component.label.unknown": "알 수 없음",
  "big.text.control.window.title": "텍스트",
  "action.DomCollectionControl.Remove.text": "제거",
  "action.DomCollectionControl.Edit.text": "편집",
  "action.DomCollectionControl.Add.text": "추가"
}

file_path = "c:/Users/klanary/Desktop/vscode 모음/android_korean/androidstudio_koreanlanguagepack/missing_translations/missing_keys_korean.json"
with open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)

file_found = False
for item in data["new_files"]:
    if item["filename"] == "XmlDomBundle.properties":
        item["keys"].update(translated_keys)
        file_found = True
        break

if not file_found:
    data["new_files"].append({
        "filename": "XmlDomBundle.properties",
        "keys": translated_keys
    })

with open(file_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("XmlDomBundle translated successfully.")