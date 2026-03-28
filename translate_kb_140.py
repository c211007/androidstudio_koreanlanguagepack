import json

ko_dict = {
  "usage.method.search.message.find.usages": "{0}\\n\\n기본 {1}의 사용 범위를 찾으시겠습니까?",
  "usage.delete.out.of.project.title": "경고",
  "usage.delete.out.of.project.message": "{0} 리팩터링을 진행하시겠습니까?",
  "usage.overrides.message": "{0}이(가) {2}에서 {1}을(를) 재정의합니다.",
  "usage.overrides.out.of.project.message": "{0}이(가) 프로젝트 외부에 있는 {2}에서 {1}을(를) 재정의합니다.",
  "usage.include.property.checkbox.text": "{0} 포함",
  "usage.include.ivar.checkbox.text": "{0} 포함",
  "usage.include.derived.classes.checkbox.text": "파생 클래스 포함",
  "switch.header.source.popup.title": "헤더/소스로 이동",
  "switch.header.source.no.results": "관련 파일 없음",
  "configurable.OCGenerateCodeConfigurable.display.name": "코드 생성",
  "abstract.extract.dialog.class.name": "{0} 이름:",
  "abstract.extract.dialog.unable.create.file": "파일을 생성할 수 없음",
  "browse.include.hierarchy.action": "계층 구조 가져오기",
  "escalate.visibility": "가시성 상향 조정",
  "escalate.visibility.description": "다음 멤버의 가시성을 상향 조정하시겠습니까?",
  "dump.file.symbol.stats": "파일 심볼 통계",
  "dump.symbol.stats": "심볼 통계",
  "highlighter.change.file.length.limit": "최대 파일 길이 변경",
  "highlighter.change.file.length.limit.input": "{0} 파일의 새 최대 길이를 문자 단위로 입력하세요",
  "highlighter.max.file.length.title": "최대 파일 길이",
  "if.responds.to.surround.error.hint": "선택한 코드에 메시지 보내기 표현식이 없습니다.",
  "quickfixes.import.symbol": "심볼 가져오기",
  "quickfixes.make.function.virtual": "함수를 가상으로 만들기",
  "quickfixes.make.property.dynamic": "{0}을(를) @dynamic으로 만들기",
  "quickfixes.synthesize": "{0} 합성",
  "move.dialog.move.members.to.class": "클래스(기존 또는 새 클래스)로 멤버 이동:",
  "move.dialog.move.declarations.to.file": "파일(기존 또는 새 파일)로 선언 이동:",
  "move.dialog.put.to.namespace": "네임스페이스(기존 또는 새 네임스페이스)에 넣기:",
  "move.dialog.move.declarations": "선언 이동",
  "move.dialog.destination": "대상:",
  "move.dialog.target.file.does.not.exist": "대상 파일 ''{0}''이(가) 아직 없습니다.",
  "move.dialog.create.new.file": "새 파일 생성",
  "move.dialog.create.new.class": "새 클래스 생성",
  "move.processor.skip": "건너뛰기",
  "push.down.members.dialog": "{0}의 멤버를 다음으로 푸시 다운:",
  "push.down.dialog.searching.inheritors": "상속자 검색 중",
  "resolve.show.related.contexts": "관련 컨텍스트만 표시",
  "resolve.show.all.contexts": "모든 컨텍스트 표시\\u2026",
  "symbol.table.activity.building.symbols": "심볼 빌드 중\\u2026",
  "symbol.table.activity.collecting.files": "파일 수집 중\\u2026",
  "symbol.table.activity.loading.symbols": "심볼 로드 중\\u2026",
  "symbol.table.activity.updating.symbols": "심볼 업데이트 중\\u2026",
  "symbol.table.activity.loading.header.maps": "헤더 맵 로드 중\\u2026",
  "symbol.table.dump.stats.action": "{0}에 통계가 기록되었습니다.",
  "action.CIDR.DebugDumpBuildingSymbols.text": "C/C++: 심볼 빌드 상태 덤프",
  "action.CIDR.Lang.Format.Extractor.text": "코드 포맷 추출",
  "action.CIDR.Lang.DropPsiForOpenedFiles.text": "열린 파일의 PSI 삭제",
  "action.CIDR.Lang.RemoveBodiesAndComments.text": "함수 본문 및 주석 제거",
  "action.CIDR.Lang.DumpFileSymbolStats.text": "파일 심볼 통계 덤프"
}

with open("missing_translations/missing_keys_korean.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for item in data:
    if item["filename"] == "OCBundle.properties":
        item["ko"].update(ko_dict)
        print("Updated OCBundle.properties")
        break

with open("missing_translations/missing_keys_korean.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)
