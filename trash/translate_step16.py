import json
with open('missing_translations/missing_keys_korean.json', 'r', encoding='utf-8') as f:
    ko_data = json.load(f)

translations = {
  "import.statement.identifier.or.asterisk.expected.": "식별자 또는 '*'가 필요합니다",
  "java.terms.anonymous.class.base.ref": "익명 {0}",
  "javadoc.exception.tag.class.is.not.throwable": "{0} 클래스는 Throwable의 하위 클래스가 아닙니다",
  "javadoc.exception.tag.exception.is.not.thrown": "{1} 메서드에서 {0}을(를) throw하도록 선언되지 않았습니다",
  "javadoc.exception.tag.wrong.tag.value": "잘못된 태그 값입니다",
  "javadoc.param.tag.parameter.name.expected": "매개변수 이름이 필요합니다",
  "javadoc.param.tag.type.parameter.gt.expected": "'>'가 필요합니다",
  "javadoc.param.tag.type.parameter.name.expected": "타입 매개변수 이름이 필요합니다",
  "javadoc.ref.tag.class.ref.expected": "클래스 참조가 필요합니다",
  "javadoc.value.field.required": "@value 태그는 필드를 참조해야 합니다",
  "javadoc.value.field.with.initializer.required": "@value 태그는 상수 초기화자가 있는 필드를 참조해야 합니다",
  "javadoc.value.static.field.required": "@value 태그는 정적 필드를 참조해야 합니다",
  "javadoc.value.tag.jdk15.required": "JDK 1.4 이전 버전을 사용하는 경우 @value 태그에 인수를 사용할 수 없습니다",
  "jdk.1.3.language.level.description": "1.3 - 기본 Java(Plain old Java)",
  "jdk.1.4.language.level.description": "1.4 - 'assert' 키워드",
  "jdk.1.5.language.level.description": "5 - 'enum' 키워드, 제네릭(generics), 오토박싱(autoboxing) 등",
  "jdk.1.6.language.level.description": "6 - 인터페이스의 @Override",
  "jdk.1.7.language.level.description": "7 - 다이아몬드, ARM, 다중 catch(multi-catch) 등",
  "jdk.1.8.language.level.description": "8 - 람다(Lambdas), 타입 애너테이션 등",
  "jdk.1.9.language.level.description": "9 - 모듈(Modules), 인터페이스의 private 메서드 등",
  "jdk.10.language.level.description": "10 - 지역 변수 타입 추론(Local variable type inference)",
  "jdk.11.language.level.description": "11 - 람다 매개변수에 대한 지역 변수 구문",
  "jdk.12.language.level.description": "12 - 새로운 언어 기능 없음",
  "jdk.13.language.level.description": "13 - 새로운 언어 기능 없음",
  "jdk.14.language.level.description": "14 - Switch 표현식",
  "jdk.15.language.level.description": "15 - 텍스트 블록",
  "jdk.16.language.level.description": "16 - 레코드(Records), 패턴, 지역 열거형 및 인터페이스",
  "jdk.17.language.level.description": "17 - 봉인된(Sealed) 타입, 항상 엄격한 부동 소수점 시맨틱",
  "jdk.18.language.level.description": "18 - JavaDoc 스니펫",
  "jdk.19.language.level.description": "19 - 새로운 언어 기능 없음",
  "jdk.20.language.level.description": "20 - 새로운 언어 기능 없음",
  "jdk.21.language.level.description": "21 - 레코드 패턴, switch의 패턴 매칭",
  "jdk.21.preview.language.level.description": "21 (미리보기) - 문자열 템플릿, 이름 없는 클래스 및 인스턴스 main 메서드 등",
  "jdk.22.language.level.description": "22 - 이름 없는 변수 및 패턴",
  "jdk.22.preview.language.level.description": "22 (미리보기) - super() 이전의 구문, 문자열 템플릿(2차 미리보기) 등",
  "jdk.X.language.level.description": "X - 실험적 기능",
  "jdk.unsupported.preview.language.level.description": "{0} (미리보기) - 지원되지 않음",
  "local.class.preposition": "지역(local)",
  "method.context.display": "{1}의 {0}()",
  "node.abstract.flag.tooltip": "추상(Abstract)"
}

ko_error_bundle = next((x for x in ko_data['new_files'] if x['filename'] == 'JavaPsiBundle.properties'), None)
ko_error_bundle['keys'].update(translations)
ko_error_bundle['key_count'] = len(ko_error_bundle['keys'])

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(ko_data, f, ensure_ascii=False, indent=2)

print("Updated JavaPsiBundle.properties part 5")