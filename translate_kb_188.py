import json
from pathlib import Path

def update_missing_keys():
    file_path = Path("missing_translations/missing_keys_korean.json")

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    ko_dict = {
        "relaxng.annotator.definition-doesnt-override-anything-from": "정의가 {0}의 어떤 것도 재정의하지 않습니다.",
        "relaxng.annotator.overrides.x.in.y": "{1}의 ''{0}'' 재정의",
        "relaxng.annotator.unresolved-namespace-prefix": "확인할 수 없는 네임스페이스 접두사 ''{0}''",
        "relaxng.annotator.unresolved-pattern-reference": "확인할 수 없는 패턴 참조 ''{0}''",
        "relaxng.convert-schema.action.title.non-xml": "스키마 변환...",
        "relaxng.convert-schema.action.title.xml-files": "XML {0, choice, 1#파일|2#파일}에서 스키마 생성...",
        "relaxng.convert-schema.advanced-options.dialog.title": "고급 변환 옵션",
        "relaxng.convert-schema.advanced-options.dtd.action.remove-entry.description": "항목 제거",
        "relaxng.convert-schema.advanced-options.dtd.border-title.dtd-input": "DTD 입력",
        "relaxng.convert-schema.advanced-options.dtd.border-title.namespace-settings": "네임스페이스 설정",
        "relaxng.convert-schema.advanced-options.dtd.checkbox.generate-start": "시작 생성(&G)",
        "relaxng.convert-schema.advanced-options.dtd.checkbox.inline-attlist": "인라인 속성 목록(&I)",
        "relaxng.convert-schema.advanced-options.dtd.checkbox.strict-any": "엄격한 any(&S)",
        "relaxng.convert-schema.advanced-options.dtd.label.any-name": "any-이름(&N):",
        "relaxng.convert-schema.advanced-options.dtd.label.annotation-prefix": "주석 접두사(&O):",
        "relaxng.convert-schema.advanced-options.dtd.label.attlist-define": "속성 목록 정의(&A):",
        "relaxng.convert-schema.advanced-options.dtd.label.colon-replacement": "콜론 교체(&C):",
        "relaxng.convert-schema.advanced-options.dtd.label.default": "기본값(&D):",
        "relaxng.convert-schema.advanced-options.dtd.label.element-define": "요소 정의(&E):",
        "relaxng.convert-schema.advanced-options.dtd.tooltip.annotation-prefix": "기본값은 RELAX NG DTD 호환성 위원회 사양에서 정의한 대로 접두사가 http://relaxng.org/ns/compatibility/annotations/1.0에 바인딩된 annotation 속성 prefix:defaultValue를 사용하여 표시됩니다. 기본적으로 Trang은 DTD에서 사용된 접두사와 충돌하지 않는 한 접두사로 a를 사용합니다.",
        "relaxng.convert-schema.advanced-options.dtd.tooltip.strict-any": "선언된 모든 요소에 대한 명시적 참조 선택을 사용하여 ANY 콘텐츠 모델의 정확한 의미를 유지합니다. 기본적으로 Trang은 모든 요소를 허용하는 와일드카드를 사용합니다.",
        "relaxng.convert-schema.advanced-options.dtd.tooltip.colon-replacement": "DTD에서 요소 선언 및 속성 목록 선언을 나타내는 데 사용되는 정의 이름을 구성할 때 요소 이름의 콜론을 문자로 바꿉니다. Trang은 DTD의 각 요소 선언 및 attlist 선언에 대한 정의를 생성합니다. 정의 이름은 요소 이름을 기반으로 합니다. RELAX NG에서 정의 이름에는 콜론을 포함할 수 없습니다. 그러나 DTD에서 요소 이름에는 콜론이 포함될 수 있습니다. 기본적으로 Trang은 먼저 접두사가 없는 요소 이름을 사용하려고 시도합니다. 이로 인해 충돌이 발생하는 경우 콜론을 올바른 이름 문자로 바꿉니다(먼저 마침표 사용 시도).",
        "relaxng.convert-schema.advanced-options.dtd.tooltip.element-define": "요소 이름에서 요소 선언을 나타내는 정의 이름을 구성하는 방법을 지정합니다. 이름 패턴에는 정확히 하나의 퍼센트 문자가 포함되어야 합니다. 이 퍼센트 문자는 (콜론 교체 후) 요소의 이름으로 바뀌고 결과는 정의의 이름으로 사용됩니다.",
        "relaxng.convert-schema.advanced-options.dtd.tooltip.inline-attlist": "속성 목록 선언에 대한 정의를 생성하지 않고 대신 속성 목록 선언에 선언된 속성을 요소 선언에 대해 생성된 정의로 이동하도록 지정합니다. 이는 출력 모듈이 xsd인 경우의 기본 동작입니다. 그렇지 않은 경우 기본 동작은 -i no-inline-attlist 매개변수에 설명되어 있습니다.",
        "relaxng.convert-schema.advanced-options.dtd.tooltip.any-name": "콘텐츠 모델이 ANY로 DTD에 선언된 요소의 콘텐츠에 대해 생성된 정의 이름을 지정합니다.",
        "relaxng.convert-schema.advanced-options.dtd.tooltip.generate-start": "Trang이 시작 요소를 생성해야 하는지 여부를 지정합니다. DTD는 문서 요소로 허용되는 요소를 나타내지 않습니다. Trang은 정의되었지만 참조되지 않은 모든 요소를 문서 요소로 허용하는 것으로 가정합니다.",
        "relaxng.convert-schema.advanced-options.dtd.tooltip.attlist-define": "요소 이름에서 속성 목록 선언을 나타내는 정의 이름을 구성하는 방법을 지정합니다. 이름 패턴에는 정확히 하나의 퍼센트 문자가 포함되어야 합니다. 이 퍼센트 문자는 (콜론 교체 후) 요소의 이름으로 바뀌고 결과는 정의의 이름으로 사용됩니다.",
        "relaxng.convert-schema.advanced-options.xsd.border-title.w3c-xml-schema-output": "W3C XML Schema 출력",
        "relaxng.convert-schema.advanced-options.xsd.checkbox.disable-abstract-elements": "추상 요소 비활성화(&D)",
        "relaxng.convert-schema.advanced-options.xsd.label.any-attribute-process-contents": "any-속성 콘텐츠 처리(&N)",
        "relaxng.convert-schema.advanced-options.xsd.label.any-process-contents": "any-콘텐츠 처리(&A)",
        "relaxng.convert-schema.advanced-options.xsd.tooltip.any-attribute-process-contents": "모든 어트리뷰트 요소의 processContents 어트리뷰트에 대한 값을 지정합니다.\n기본값은 skip(RELAX NG 시맨틱에 해당)입니다.",
        "relaxng.convert-schema.advanced-options.xsd.tooltip.any-process-contents": "모든 요소의 processContents 어트리뷰트에 대한 값을 지정합니다.\n입력 형식이 dtd(이 경우 기본값은 DTD 시맨틱에 해당하는 strict)가 아닌 한, 기본값은 skip(RELAX NG 시맨틱에 해당)입니다.",
        "relaxng.convert-schema.advanced-options.xsd.tooltip.disable-abstract-elements": "생성된 XML 스키마에서 추상 요소 및 대체 그룹의 사용을 비활성화합니다.\n주석 어트리뷰트를 사용하여 이를 제어할 수도 있습니다.",
        "relaxng.convert-schema.dialog.file-exists.message": "''{0}'' 파일이 이미 존재합니다. 덮어쓰시겠습니까?",
        "relaxng.convert-schema.dialog.file-exists.title": "출력 파일 존재",
        "relaxng.convert-schema.dialog.title": "스키마 파일 변환",
        "relaxng.convert-schema.settings.border-title.output-destination": "출력 대상",
        "relaxng.convert-schema.settings.border-title.output-options": "출력 옵션",
        "relaxng.convert-schema.settings.border-title.output-type": "출력 유형",
        "relaxng.convert-schema.settings.destination.message": "생성된 파일이 저장될 대상을 선택하세요",
        "relaxng.convert-schema.settings.destination.title": "스키마 변환 대상",
        "relaxng.convert-schema.settings.label.encoding": "인코딩(&E):",
        "relaxng.convert-schema.settings.label.indent": "들여쓰기(&I):",
        "relaxng.convert-schema.settings.label.line-length": "줄 길이(&L):",
        "relaxng.convert-schema.settings.radio-button.dtd": "&DTD",
        "relaxng.convert-schema.settings.radio-button.relax-ng-compact-syntax": "RELAX NG - 컴팩트 구문(&C)",
        "relaxng.convert-schema.settings.radio-button.relax-ng-xml-syntax": "RELAX NG - XML 구문(&R)",
        "relaxng.convert-schema.settings.radio-button.w3c-xml-schema": "W3C XML Schema(&S)",
        "relaxng.gutter.is-overridden": "재정의됨"
    }

    filename = "RelaxngBundle.properties"
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
