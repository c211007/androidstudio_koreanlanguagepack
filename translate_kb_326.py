import json
import os

translated_keys = {
  "xml.inspections.unbound.prefix": "바인딩되지 않은 네임스페이스 접두사",
  "xml.inspections.wrong.root.element": "잘못된 루트 요소",
  "xml.inspections.global": "XML 강조 표시",
  "xml.inspections.group.name": "XML",
  "xml.inspections.check.tag.empty.body": "빈 요소 내용",
  "xml.inspections.check.file.with.xerces": "외부 유효성 검사 실패",
  "xml.inspections.check.dtd.references": "해결되지 않은 DTD 참조",
  "xml.inspections.unresolved.entity.reference": "해결되지 않은 엔티티 참조 {0}",
  "xml.inspections.unresolved.element.reference": "해결되지 않은 DTD 요소 참조 {0}",
  "xml.inspections.duplicate.id": "중복된 'id' 속성",
  "xml.inspections.invalid.id": "해결되지 않은 'id' 참조",
  "xml.inspections.unused.schema": "사용되지 않는 스키마 선언",
  "xml.inspections.path.resolve": "해결되지 않은 파일 참조",
  "xml.inspections.unresolved": "해결되지 않은 참조",
  "xml.inspections.default.attribute.value": "기본값이 있는 중복 속성",
  "xml.inspections.deprecated": "사용 중단된(deprecated) 기호",
  "xml.inspections.required.attributes.display.name": "누락된 필수 속성",
  "xml.intention.add.xsi.schema.location.for.external.resource": "'xsi:schemaLocation' 속성 추가",
  "xml.intention.create.xml.declaration": "XML 요소 선언 생성",
  "xml.intention.fetch.name": "외부 리소스 가져오기",
  "xml.intention.fetch.progress.fetching.resource": "리소스 가져오는 중",
  "xml.intention.fetch.error.fetching.resource": "{0}을(를) 가져올 수 없습니다.",
  "xml.intention.fetch.error.fetching.title": "가져오는 중 오류 발생",
  "xml.intention.fetch.error.fetching.dependent.resource": "종속 리소스를 가져올 수 없습니다.",
  "xml.intention.fetch.error.invalid.url.title": "잘못된 URL",
  "xml.intention.fetch.error.invalid.url.no.xml.file.at.location": "지정된 위치에 XML이 없습니다: \\n{0}",
  "xml.intention.fetch.error.invalid.url.message": "지정된 URL을 확인하세요: \\n{0}",
  "xml.intention.fetch.progress.fetching": "{0} 가져오는 중",
  "xml.intention.ignore.external.resource.text": "외부 리소스 무시",
  "xml.intention.insert.namespace.prefix.name": "네임스페이스 접두사 삽입",
  "xml.intention.insert.namespace.prefix.command": "네임스페이스 접두사 삽입",
  "xml.intention.manually.setup.external.resource": "수동으로 외부 리소스 설정",
  "xml.intention.reset.to.default.namespace.name": "기본 네임스페이스로 초기화",
  "xml.intention.reset.to.default.namespace.command": "기본 네임스페이스로 초기화",
  "xml.intention.split.tag.text": "현재 태그 분할",
  "xml.intention.split.tag.family": "현재 태그 분할",
  "xml.javadoc.tag.name.message": "태그 이름",
  "xml.javadoc.description.message": "설명",
  "xml.javadoc.version.message": "버전",
  "xml.javadoc.enumeration.value.message": "열거형(Enumeration) 값",
  "xml.javadoc.complex.type.message": "복합형(Complex type)",
  "xml.lookup.choose.color": "색상 선택...",
  "xml.map.resource.dialog.label.file": "파일(&F):",
  "xml.map.resource.dialog.label.uri": "URI(&U):",
  "xml.map.resource.dialog.border.title.project.schemas": "프로젝트 스키마(&S)",
  "xml.options.label.catalog.property.file": "카탈로그 속성 파일:",
  "xml.options.border.title.bem": "BEM",
  "xml.progress.changing.to.default.namespace": "기본 네임스페이스로 변경 중",
  "xml.quickfix.unescaped.xml.character.family": "이스케이프 문자",
  "xml.quickfix.unescaped.xml.character.text": "''{0}'' 이스케이프"
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

print("Batch 2 translated successfully.")