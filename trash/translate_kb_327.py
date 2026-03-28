import json
import os

translated_keys = {
  "xml.schemas.border.title.default.html.language.level": "기본 HTML 언어 수준",
  "xml.schemas.radio.button.html.4.http.www.w3.org.tr.html4.loose.dtd": "HTML 4 (\"http://www.w3.org/TR/html4/loose.dtd\")",
  "xml.schemas.radio.button.html.5": "HTML 5",
  "xml.schemas.radio.button.other.doctype": "기타 doctype:",
  "xml.schemas.radio.button.xml.schema.1.0": "XML Schema 1.0",
  "xml.schemas.radio.button.xml.schema.1.1": "XML Schema 1.1",
  "xml.schemas.border.title.xml.schema.version": "XML Schema 버전",
  "xml.tree.config.files.type": "{0} 파일",
  "xml.validate.tab.content.title": "{0} 유효성 검사",
  "xml.validate.open.message.view.command.name": "메시지 뷰 열기",
  "xml.validate.validation.is.running.terminate.confirmation.text": "유효성 검사를 종료하시겠습니까?",
  "xml.validate.validation.is.running.terminate.confirmation.title": "유효성 검사 실행 중",
  "zen.coding.context.help.tooltip": "텍스트를 Emmet 약어로 생성된 HTML로 감쌉니다. 약어를 확장하고 선택한 콘텐츠를 생성된 스니펫의 마지막 요소에 배치합니다.\\n<p/>\\n<code>$#</code> 자리 표시자를 사용하여 출력 위치를 정의할 수 있습니다.",
  "zen.coding.context.help.link": "docs.emmet.io에서 자세히 알아보기",
  "tag.name.completion.hint": "다른 네임스페이스의 태그를 보려면 {0}을(를) 누르세요.",
  "tag.name.completion.display.name": "태그 이름 자동 완성",
  "configurable.XmlEmmetConfigurable.display.name": "HTML",
  "configurable.XMLCatalogConfigurable.display.name": "XML 카탈로그",
  "configurable.DefaultSchemasConfigurable.display.name": "기본 XML 스키마",
  "auto.import.show.popup": "자동 임포트 툴팁 표시",
  "smart.keys.insert.required.attributes.on.tag.completion": "태그 자동 완성 시 필수 속성 삽입",
  "smart.keys.insert.closing.tag.on.tag.completion": "태그 자동 완성 시 닫는 태그 삽입",
  "smart.keys.insert.required.subtags.on.tag.completion": "태그 자동 완성 시 필수 하위 태그 삽입",
  "smart.keys.start.attribute.on.tag.completion": "태그 완성 시 속성 시작",
  "smart.keys.add.quotes.for.attribute.value.on.typing.equal.and.attribute.completion": "'=' 입력 및 속성 자동 완성 시 속성 값에 따옴표 추가",
  "smart.keys.auto.close.tag.on.typing.less": "'</' 입력 시 태그 자동 닫기",
  "smart.keys.simultaneous.tags.editing": "'<tag></tag>' 동시 편집",
  "smart.keys.select.whole.css.identifiers.on.double.click": "더블 클릭 시 전체 CSS 식별자 선택",
  "settings.enable.html.xml.tag.tree.highlighting": "HTML/XML 태그 트리 강조 표시 활성화",
  "settings.levels.to.highlight": "강조 표시할 수준:",
  "settings.opacity": "불투명도:",
  "xml.catalog.properties.file": "XML 카탈로그 속성 파일",
  "default": "기본값",
  "emmet.preview": "Emmet 미리보기",
  "cannot.show.preview.for.given.abbreviation": "지정된 약어에 대한 미리보기를 표시할 수 없습니다.",
  "rearrange.tag.attributes": "태그 속성 재정렬",
  "rename.xml.tag": "XML 태그 이름 변경",
  "namespace.prefix": "네임스페이스 접두사:",
  "emmet.error": "Emmet 오류",
  "map.external.resource": "외부 리소스 매핑",
  "choose.schema.file": "스키마 파일 선택",
  "convert.text.to.cdata": "텍스트를 CDATA로 변환",
  "convert.cdata.to.text": "CDATA를 텍스트로 변환",
  "no.errors.found": "오류를 찾을 수 없음",
  "xml.text": "XML 텍스트",
  "xml.tag": "XML 태그",
  "change.template.data.language": "템플릿 데이터 언어 변경",
  "xml.actions": "XML 작업",
  "choose.tag.name": "태그 이름 선택",
  "generate.xml.tag": "XML 태그 생성"
}

file_path = "c:/Users/klanary/Desktop/vscode 모음/android_korean/androidstudio_koreanlanguagepack/missing_translations/missing_keys_korean.json"
with open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)

for item in data["new_files"]:
    if item["filename"] == "XmlBundle.properties":
        item["keys"].update(translated_keys)
        break

with open(file_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Batch 3 translated successfully.")