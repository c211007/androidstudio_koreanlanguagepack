import json

ko_dict = {
  "command.name.replace.type": "유형 바꾸기",
  "java.completion.tag": "{0, choice, 1#태그:|2#태그:}",
  "intention.family.name.dismiss": "무시",
  "intention.family.name.ignore.project": "이 프로젝트에서 다시 표시하지 않음",
  "fix.move.to.source.root": "소스 루트로 이동",
  "warning.java.file.outside.source.root": "Java 파일이 모듈 소스 루트 외부에 있으므로 컴파일되지 않습니다.",
  "inspection.message.snippet.file.not.found": "스니펫 파일 ''{0}''을(를) 찾을 수 없습니다.",
  "inspection.message.snippet.region.not.found": "영역을 찾을 수 없습니다.",
  "javadoc.snippet.not.found": "스니펫을 찾을 수 없음: {0}",
  "javadoc.snippet.region.not.found": "영역을 찾을 수 없음: {0}",
  "javadoc.snippet.error.unknown.enum.value": "@{0}: 알 수 없는 {1} ''{2}''; {3}만 지원됩니다.",
  "javadoc.snippet.error.markup.tag.expected": "마크업 태그 또는 속성이 필요합니다.",
  "javadoc.snippet.error.unsupported.attribute": "@{0}: 지원되지 않는 속성: ''{1}''",
  "javadoc.snippet.error.duplicate.attribute": "@{0}: 중복 속성: ''{1}''",
  "javadoc.snippet.error.missing.required.attribute": "@{0}: ''{1}'' 속성이 누락되었습니다.",
  "javadoc.snippet.error.both.substring.and.regex": "@{0}: 정규식 또는 하위 문자열 중 하나를 지정해야 하지만 둘 다 지정할 수는 없습니다.",
  "javadoc.snippet.error.malformed.regular.expression": "@{0}: 형식이 잘못된 정규식: {1}",
  "javadoc.snippet.error.malformed.replacement": "@{0}: 형식이 잘못된 정규식 대체 ''{1}'': {2}",
  "javadoc.snippet.error.regex.too.complex": "@{0}: 너무 복잡한 정규식 ''{1}''",
  "intention.family.name.synchronize.inline.snippet": "인라인 스니펫 동기화",
  "inspection.message.external.snippet.differs.from.inline.snippet": "외부 스니펫이 인라인 스니펫과 다릅니다.",
  "package.chooser.modal.progress.title": "패키지 검색 중…",
  "convert.number.hex": "16진수",
  "convert.number.binary": "2진수",
  "convert.number.octal": "8진수",
  "convert.number.decimal": "10진수",
  "convert.number.plain.format": "일반 형식",
  "convert.number.scientific.format": "과학적 표기법",
  "delete.initializer.completely": "초기화자 완전히 삭제",
  "delete.assignment.completely": "할당 완전히 삭제",
  "popup.title.remove.unused.variable": "사용하지 않는 변수 제거",
  "intention.family.name.extract.possible.side.effects": "가능한 부작용 추출",
  "intention.family.name.delete.possible.side.effects": "가능한 부작용 삭제",
  "intention.extract.set.from.comparison.chain.replace.only.this": "이 항목만 바꾸기",
  "intention.extract.set.from.comparison.chain.replace.all": "모든 항목 바꾸기",
  "intention.text.replace.all.delete.import": "모두 바꾸고 가져오기 삭제",
  "intention.text.replace.this.occurrence.keep.import": "이 항목을 바꾸고 가져오기 유지",
  "popup.title.choose.target.class": "대상 클래스 선택",
  "tooltip.incorrect.file.template": "잘못된 ''{0}'' 파일 템플릿",
  "label.ignored.exceptions": "무시된 예외:"
}

with open('missing_translations/missing_keys_korean.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for file_entry in data['new_files']:
    if file_entry['filename'] == 'JavaBundle.properties':
        file_entry['keys'].update(ko_dict)
        print("Updated JavaBundle.properties (Keys 441-480)")
        break

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
