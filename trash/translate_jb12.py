import json

ko_dict = {
  "intention.name.upgrade.jdk.to": "JDK를 {0}+(으)로 업그레이드",
  "intention.family.name.box.primitive.in.conditional.branch": "조건부 분기에서 기본값 박싱",
  "environment.key.description.project.jdk": "프로젝트 JDK의 절대 경로",
  "environment.key.description.project.jdk.name": "IDE에 표시되는 프로젝트 JDK의 이름입니다.",
  "progress.title.detecting.jdk": "JDK 감지 중",
  "progress.title.restore.references": "참조 복원 중",
  "increase.language.level.preview.description": "모듈 ''{0}''의 언어 레벨이 ''{1}''(으)로 변경됩니다.",
  "open.settings.dialog.for.module.preview.text": "모듈 ''{0}''의 설정 대화상자 열기",
  "button.add.dependency": "종속성 추가",
  "adds.ext.library.preview": "모듈 ''{1}''에 라이브러리 ''{0}''을(를) 추가합니다.",
  "adds.ext.library.preview.import": "라이브러리 ''{0}''을(를) 모듈 ''{1}''의 종속성에 추가하고 필요한 경우 ''{2}''을(를) 가져옵니다.",
  "adds.module.dependencies.preview": "{0, choice, 1#모듈 ''''{1}''''|2#{2} 중 하나}을(를) 모듈 ''{3}''의 종속성에 추가하고 필요한 경우 해결되지 않은 클래스를 가져옵니다.",
  "adds.library.preview": "{0, choice, 1#라이브러리 ''''{1}''''|2#{2} 중 하나}을(를) 모듈 ''{3}''의 종속성에 추가하고 해결되지 않은 ''{4}''을(를) 가져옵니다.",
  "adds.library.preview.no.import": "{0, choice, 1#라이브러리 ''''{1}''''|2#{2} 중 하나}을(를) 모듈 ''{3}''의 종속성에 추가합니다.",
  "notification.content.added.annotations": "{0}개의 {0, choice, 1#어노테이션이|2#어노테이션이} 추가되었습니다.",
  "java.method.chains.inlay.provider.name": "메서드 체인",
  "java.implicit.types.local.inlay.provider.name": "암시적 유형",
  "java.implicit.types.lambda.inlay.provider.name": "람다 매개변수 유형",
  "intention.make.final.fixer.stream": "스트림 API를 사용하여 ''{0}''을(를) 효과적으로 final로 만들기",
  "intention.make.final.fixer.if": "초기화자를 ''if'' 문으로 이동하여 ''{0}''을(를) 효과적으로 final로 만들기",
  "package.classes": "패키지 클래스:",
  "invert.quickfix.preview": "선택한 부울을 반전하고 새 이름을 선택하는 대화상자를 엽니다.",
  "validator.text.not.valid.class.name": "유효한 클래스 이름이 아님",
  "validator.text.class.not.found": "클래스를 찾을 수 없음",
  "validator.text.no.annotation": "어노테이션이어야 함",
  "validator.text.wrong.superclass": "잘못된 상위 클래스",
  "validator.text.directory.not.found": "디렉터리를 찾을 수 없음",
  "validator.text.not.directory": "디렉터리가 아님",
  "compiler.options": "컴파일러 옵션",
  "vm.option.description.requires": " ({0} 필요)",
  "vm.option.description.option": "옵션:",
  "vm.option.description.category": "범주:",
  "vm.option.description.type": "유형:",
  "vm.option.description.default.value": "기본값:",
  "vm.option.description.description": "설명:",
  "vm.option.description.standard": "표준",
  "vm.option.description.product": "제품",
  "vm.option.description.diagnostic": "진단",
  "vm.option.description.experimental": "실험적",
  "hint.text.not.valid.java.identifier": "유효한 Java 식별자가 아닙니다."
}

with open('missing_translations/missing_keys_korean.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for file_entry in data['new_files']:
    if file_entry['filename'] == 'JavaBundle.properties':
        file_entry['keys'].update(ko_dict)
        print("Updated JavaBundle.properties (Keys 401-440)")
        break

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
