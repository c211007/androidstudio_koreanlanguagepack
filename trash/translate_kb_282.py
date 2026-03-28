import json

translations = {
  "manual.fix.path.nohost": "앱 링크의 인텐트 필터는 경로를 지정할 경우 호스트도 지정해야 합니다.",
  "manual.fix.path": "이 링크의 인텐트 필터는 <data> 태그에 경로(path)를 지정합니다. 경로는 \"/\"로 시작해야 합니다.",
  "manual.fix.path.prefix": "이 링크의 인텐트 필터는 <data> 태그에 pathPrefix를 지정합니다. 이는 \"/\"로 시작해야 합니다.",
  "manual.fix.path.pattern": "이 링크의 인텐트 필터는 <data> 태그에 pathPattern을 지정합니다. 이는 \".*\" 또는 \"/\"로 시작해야 합니다.",
  "manual.fix.duplicate": "앱에 동일한 해석된 URL 패턴을 가진 링크가 하나 이상 있습니다. 각 URL은 하나의 액티비티에만 일치해야 하므로, 이러한 중복은 오류일 가능성이 높습니다. 아래를 클릭하여 ইন텐트 필터를 올바르게 정의하는 방법에 대해 자세히 알아보고 중복된 링크를 확인하세요.",
  "manual.fix.duplicate.link": "중복: {0}",
  "manual.fix.order": "순서(order)는 정수여야 합니다.",
  "manual.fix.priority": "우선순위(priority)는 정수여야 합니다.",
  "manual.fix.port": "포트는 0에서 65535(포함) 사이의 정수여야 합니다.",
  "url.assistant.toolwindow.title": "앱 링크 도우미",
  "url.assistant.toolwindow.smalltitle": "Android 앱 링크 지원",
  "url.assistant.open.action.id": "DeveloperServices.UrlAssistant",
  "url.assistant.editor.title": "URL 매핑 편집기",
  "url.assistant.panel.description": "URL에서 액티비티로의 매핑을 추가, 업데이트 또는 삭제하려면 아래 URL 매핑 테이블을 사용하세요.\\n\nURL 매퍼는 적절한 URL 인텐트 필터를 포함하도록 AndroidManifest.xml 파일을 업데이트합니다.",
  "url.assistant.preview.instruction": "관련 AndroidManifest.xml 파일에 추가된 URL 인텐트 필터의 미리보기를 보려면 위 테이블에서 행을 선택하세요.",
  "url.assistant.edit.run.configuration": "실행 구성 편집...",
  "url.assistant.preview.title": "미리보기",
  "url.malformed": "URL 형식이 잘못되었습니다. 입력한 값을 다시 확인하세요.",
  "check.url.mapping.instruction": "URL이 액티비티에 매핑되는지 확인하려면 URL을 입력하세요.",
  "check.url.mapping.fail": "이 URL은 매핑된 액티비티가 없습니다.",
  "check.url.mapping.result": "이 URL은 <a href='#'>{0}</a>(으)로 매핑됩니다.",
  "check.url.mapping.malformed": "URL이 유효하지 않습니다. 다시 확인하세요.",
  "check.url.mapping.open.fail": "액티비티 파일을 찾을 수 없습니다.",
  "check.url.mapping.activity.file.not.found": "액티비티 파일을 찾을 수 없습니다.",
  "check.url.mapping.test.url.added": "URL이 이미 테스트 URL로 추가되었습니다.",
  "check.url.mapping.add.test.url.fail": "테스트 URL을 추가하지 못했습니다.",
  "manifest.need.refactor": "기존 앱 링크 중 일부는 URL 매핑 편집기에 표시할 수 없습니다.\n  이 항목들을 표시하고 편집하기 위해 AndroidManifest 파일을 리팩터링하시겠습니까?",
  "manifest.need.refactor.title": "리팩터링 필요",
  "manifest.parsing.error": "AndroidManifest 파일에 오류가 있습니다. 수정하고 다시 시도하세요.",
  "dialog.error.title": "오류",
  "add.url.dialog.title": "URL 매핑 추가",
  "add.url.dialog.show.advanced": "고급 표시",
  "add.url.dialog.hide.advanced": "고급 숨기기",
  "add.url.host.hint": "호스트를 입력하세요. 예: www.google.com",
  "add.url.mimetype.hint": "예: image/*",
  "add.url.invalid.input.dialog.title": "잘못된 입력",
  "add.url.invalid.input.scheme": "스킴은 http 또는 https여야 합니다.",
  "add.url.invalid.input.host": "호스트 이름이 유효하지 않습니다. 입력한 값을 다시 확인하세요.",
  "add.url.invalid.input.port": "포트는 0에서 65535 사이여야 합니다.",
  "add.url.invalid.input.order": "순서(order)는 정수여야 합니다.",
  "add.url.generating": "인텐트 필터 생성 중",
  "add.url.path.start.with.slash": "{0}은(는) \\\"/\\\"로 시작해야 합니다.",
  "add.url.from.this.url": "이 URL로 생성",
  "add.url.how.it.works.text": "작동 방식",
  "add.url.how.it.works.url": "https://developer.android.com/guide/topics/manifest/data-element.html",
  "add.url.path.hint": "경로를 입력하세요. 예: /myPath",
  "add.url.path.prefix.hint": "pathPrefix를 입력하세요. 예: /myPathPrefix",
  "add.url.path.pattern.hint": "URL 패턴을 입력하세요. 예: /[a-z]+",
  "dal.title": "웹사이트 연결",
  "dal.panel.title": "웹사이트 연결 선언"
}

with open("missing_translations/missing_keys_korean.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for file_info in data.get("new_files", []):
    if file_info.get("filename") == "UrlAssistBundle.properties":
        keys_dict = file_info.get("keys", file_info.get("properties", {}))
        keys_dict.update(translations)
        file_info["keys"] = keys_dict
        break

with open("missing_translations/missing_keys_korean.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)
