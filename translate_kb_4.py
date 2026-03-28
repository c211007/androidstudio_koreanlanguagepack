import json

ko_dict = {
  "fix.move.file.to.package.text": "{0}(으)로 파일 이동",
  "fix.change.package.family": "파일의 패키지를 디렉터리와 일치하도록 변경",
  "fix.change.package.text": "파일의 패키지를 {0}(으)로 변경",
  "fix.move.to.sealed.family": "계층 구조 멤버를 sealed 클래스 부모의 패키지/모듈로 이동",
  "fix.move.to.sealed.text": "{0}을(를) {1}의 패키지/모듈로 이동",
  "fix.add.annotation.with.arguments.text.copy": "''{1}''에서 ''{2}''(으)로 ''@{0}'' 주석 복사",
  "fix.receiver.shadowed.by.context.add.explicit.receiver.family": "명시적 수신자 추가",
  "fix.receiver.shadowed.by.context.add.explicit.receiver.this": "'this'를 수신자로 사용",
  "fix.receiver.shadowed.by.context.add.explicit.receiver.surround.with": "'with(this) { ... }'로 둘러싸기",
  "fix.receiver.shadowed.by.context.add.explicit.receiver.context": "''{0}''을(를) 수신자로 사용",
  "fix.receiver.shadowed.by.context.add.explicit.receiver.surround.with.context": "''with({0}) '{' ... '}'''로 둘러싸기",
  "action.add.import.chooser.title": "가져오기",
  "goto.super.chooser.function.title": "상위 함수 선택",
  "goto.super.chooser.property.title": "상위 속성 선택",
  "goto.super.chooser.class.title": "상위 클래스 또는 인터페이스 선택",
  "action.GotoSuperProperty.text": "상위 속성으로 이동(_u)",
  "action.GotoSuperProperty.MainMenu.text": "상위 속성(_u)",
  "action.GotoSuperProperty.description": "현재 속성이 재정의하거나 구현하는 속성의 선언으로 이동",
  "action.GotoSuperClass.text": "상위 클래스로 이동(_o)",
  "action.GotoSuperClass.MainMenu.text": "상위 클래스(_o)",
  "action.GotoSuperInterface.text": "상위 인터페이스로 이동(_u)",
  "action.GotoSuperInterface.MainMenu.text": "상위 인터페이스(_u)",
  "inspection.unused.receiver.parameter": "수신자 매개변수가 사용되지 않음",
  "fix.add.explicit.coroutine.scope.receiver": "명시적 'this' 수신자 추가",
  "fix.add.explicit.receiver.family": "명시적 수신자 추가",
  "fix.unused.receiver.parameter.remove": "중복 수신자 매개변수 제거",
  "fix.create.from.usage.family": "사용에서 생성",
  "fix.create.from.usage.local.variable": "지역 변수 ''{0}'' 생성",
  "fix.create.from.usage.property": "속성 ''{0}'' 생성",
  "fix.create.from.usage.abstract.property": "추상 속성 ''{0}'' 생성",
  "fix.create.from.usage.extension.property": "확장 속성 ''{0}'' 생성",
  "fix.replace.with.declaring.java.class": "'declaringJavaClass'로 대체",
  "overridden.marker.implementations.multiple": "구현 포함",
  "overridden.marker.implementation": "다음에 구현됨:",
  "overridden.marker.overrides.multiple": "하위 클래스에서 재정의됨",
  "overridden.marker.overrides": "다음에 재정의됨:",
  "notification.navigation.to.overriding.classes": "인덱스 업데이트 중에는 재정의하는 클래스로 이동할 수 없습니다.",
  "tooltip.implements.function": "다음 위치에서 함수 구현:",
  "tooltip.overrides.function": "다음 위치에서 함수 재정의:",
  "tooltip.implements.property": "다음 위치에서 속성 구현:",
  "tooltip.overrides.property": "다음 위치에서 속성 재정의:",
  "searching.for.overriding.methods": "재정의하는 메서드 검색 중",
  "tooltip.is.subclassed.by": "다음의 하위 클래스:",
  "tooltip.is.implemented.by": "다음에 의해 구현됨:",
  "overridden.marker.implementations.choose.implementation.title": "{0} 구현 선택",
  "overridden.marker.implementations.choose.implementation.find.usages": "{0} 속성 재정의",
  "overridden.marker.overrides.choose.implementation.title": "{0} 상위 구현 선택",
  "overridden.marker.overrides.choose.implementation.find.usages": "{0} 상위 구현",
  "remove.expression": "''{0}'' 제거",
  "unwrap.expression": "''{0}'' 래핑 해제"
}

with open('missing_translations/missing_keys_korean.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

filename = "KotlinBundle.properties"
found = False
for file_entry in data.get('new_files', []):
    if file_entry['filename'] == filename:
        file_entry['keys'].update(ko_dict)
        found = True
        break
if not found:
    data.setdefault('new_files', []).append({"filename": filename, "keys": ko_dict})

print(f"Updated {filename} (Keys 191-240)")

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
