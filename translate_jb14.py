import json

ko_dict = {
  "intention.family.name.add.main.method": "'main' 메서드 추가",
  "intention.sequenced.collection.can.be.used.display.name": "SequencedCollection 메서드를 사용할 수 있습니다.",
  "intention.sequenced.collection.can.be.used.fix.name": "SequencedCollection 메서드 호출로 바꾸기",
  "inspection.mapping.before.count.family.name": "count() 전 매핑 호출",
  "inspection.mapping.before.count.message": "''{0}()'' 호출은 최종 개수를 변경하지 않으므로 최적화되어 제거될 수 있습니다.",
  "unknown.library": "알 수 없는 라이브러리",
  "intention.name.delete.method": "''{0}()'' 메서드 삭제",
  "intention.name.delete.method.title": "''{0}()'' 메서드 삭제",
  "intention.name.delete.method.with.callees": "… 사용된 다른 private 메서드와 함께 삭제",
  "intention.name.delete.method.only": "… 다른 항목은 그대로 둠",
  "intention.family.name.delete.private.method": "private 메서드 삭제",
  "checkbox.check.for.jdk.updates": "JDK 업데이트 확인",
  "intention.family.name.rename.to.ignored": "무시되도록 이름 변경",
  "tooltip.variable.used": "변수 ''{0}''이(가) 사용되었습니다.",
  "command.completion.inline.text": "인라인",
  "command.completion.delete.element.text": "요소 삭제",
  "command.completion.getters.text": "Getter",
  "command.completion.setters.text": "Setter",
  "command.completion.getters.and.setters.text": "Getter 및 Setter",
  "command.completion.generate.getter.setter": "'Getter' 및 'Setter' 생성",
  "command.completion.generate.getter": "'Getter' 생성",
  "command.completion.generate.setter": "'Setter' 생성",
  "command.completion.generate.no.args.constructor.text": "인수 없는 생성자",
  "command.completion.generate.all.args.constructor.text": "모든 인수를 포함하는 생성자",
  "advanced.setting.java.show.irrelevant.templates.in.source.roots": "Java 소스 루트에 관련 없는 새 파일 템플릿 표시",
  "java.test.use.wall.time": "경과 시간(Wall Time) 사용",
  "java.test.overall.time": "전체 시간: {0}",
  "java.test.sum.time": "합계 시간: {0}",
  "error.no.annotation.class.found": "어노테이션 클래스를 찾을 수 없습니다.",
  "preview.api.usage": "{0}은(는) 프리뷰 API이며 향후 릴리스에서 제거될 수 있습니다.",
  "preview.api.usage.reflective": "{0}은(는) 리플렉션 프리뷰 API이며 향후 릴리스에서 제거될 수 있습니다.",
  "todo.0": "todo \"{0}\"",
  "todo.item": "todo 항목",
  "intention.rename.underscore.name": "''{1}'' 형식의 {0} 이름 변경",
  "intention.rename.underscore.popup.title": "선언 선택",
  "intention.rename.underscore.family.name": "이름 없는 변수 이름 변경"
}

with open('missing_translations/missing_keys_korean.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for file_entry in data['new_files']:
    if file_entry['filename'] == 'JavaBundle.properties':
        file_entry['keys'].update(ko_dict)
        print("Updated JavaBundle.properties (Keys 481-520)")
        break

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
