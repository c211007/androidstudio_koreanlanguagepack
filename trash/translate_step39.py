import json
with open('missing_translations/missing_keys_korean.json', 'r', encoding='utf-8') as f:
    ko_data = json.load(f)

translations = {
  "message.state.connecting.and.retrieving.options": "웹 서비스에 연결하여 옵션을 검색하는 중...",
  "message.state.downloading.template": "{0} 템플릿 다운로드 중...",
  "message.state.preparing.template": "템플릿 준비 중...",
  "message.whitespaces.are.not.allowed.here": "여기에 공백 문자는 허용되지 않습니다",
  "message.some.parts.are.not.allowed.here": "'con', 'prn', 'aux', 'nul', 'com0', ..., 'com9' 및 'lpt0', ..., 'lpt9' 부분은 여기에 허용되지 않습니다",
  "message.field.must.be.set": "필드를 설정해야 합니다",
  "message.some.string.is.not.a.valid.package.name": "''{0}''은(는) 올바른 패키지 이름이 아닙니다",
  "message.only.latin.characters.digits.spaces.and.some.other.symbols.are.allowed.here": "라틴 문자, 숫자, 공백, '-', '_' 및 '.'만 여기에 허용됩니다",
  "message.only.latin.characters.digits.and.some.other.symbols.are.allowed.here": "라틴 문자, 숫자, '_', '-' 및 '.'만 여기에 허용됩니다",
  "message.must.not.start.or.end.with.dot": "'.'으로 시작하거나 끝날 수 없습니다",
  "message.must.not.contain.double.dot.sequences": "'..' 시퀀스를 포함할 수 없습니다",
  "message.part.is.incorrect.and.must.start.with.latin.character.or.some.other.symbols": "''{0}'' 부분이 잘못되었습니다. 라틴 문자나 ''_''로 시작해야 합니다",
  "message.only.lowercase.latin.characters.digits.and.some.other.symbols.are.allowed.here": "소문자 라틴 문자, 숫자, '-', '_' 및 '.'만 여기에 허용됩니다",
  "message.must.start.with.lowercase.latin.character": "소문자 라틴 문자로 시작해야 합니다",
  "message.allowed.symbols.for.check.artifact.simple.format": "라틴 문자, 숫자, '-' 및 '_'만 여기에 허용됩니다",
  "message.allows.first.symbol.for.check.artifact.simple.format": "라틴 문자나 '_'로 시작해야 합니다",
  "error.text.with.error.content": "오류: {0}",
  "message.unavailable.dependencies": "선택한 종속성: {0}은(는) 버전 {1}에서 사용할 수 없습니다.",
  "message.no.connection.with.error.content": "''{0}''의 초기화에 실패했습니다.\\nURL, 네트워크 및 프록시 설정을 확인하십시오.\\n\\n오류 메시지:\\n{1}",
  "message.java.version.not.supported.by.sdk": "선택한 Java 버전 {0}은(는) 프로젝트 SDK ''{1}''에서 지원하지 않습니다. \\n  더 낮은 버전의 Java를 선택하거나 더 높은 버전의 SDK를 설정하십시오.\\n\\n\\n  추가 SDK를 다운로드하려면 JDK 드롭다운을 클릭하십시오.",
  "message.java.version.not.supported.by.sdk.for.technology": "{0} 프로젝트에는 최소 Java {1}이(가) 필요합니다. \\n  선택한 SDK ''{2}''은(는) 최대 Java 버전 {3}까지만 지원합니다.\\n\\n\\n  프로젝트에 다른 SDK를 선택하려면 JDK 드롭다운을 클릭하십시오.",
  "message.title.error": "오류",
  "button.tooltip.remove": "제거",
  "button.tooltip.configure": "구성",
  "button.tooltip.retry": "재시도",
  "starter.link.guide": "가이드",
  "starter.link.reference": "참조",
  "starter.link.website": "웹 사이트",
  "starter.link.specification": "사양",
  "starter.generation.error": "모듈 소스를 생성하는 중 오류가 발생했습니다: {0}",
  "title.project.server.url.label": "서버 URL:",
  "title.project.language.label": "언어:",
  "title.project.type.label": "타입:",
  "title.project.build.system.label": "빌드 시스템:",
  "title.project.test.framework.label": "테스트 프레임워크:",
  "title.project.group.label": "그룹:",
  "title.project.artifact.label": "아티팩트:",
  "title.project.package.label": "패키지 이름:",
  "title.project.app.type.label": "애플리케이션 타입:",
  "title.project.packaging.label": "패키징:"
}

ko_error_bundle = next((x for x in ko_data['new_files'] if x['filename'] == 'JavaStartersBundle.properties'), None)
if ko_error_bundle is None:
    ko_error_bundle = {'filename': 'JavaStartersBundle.properties', 'keys': {}, 'key_count': 0}
    ko_data['new_files'].append(ko_error_bundle)

ko_error_bundle['keys'].update(translations)
ko_error_bundle['key_count'] = len(ko_error_bundle['keys'])

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(ko_data, f, ensure_ascii=False, indent=2)

print("Updated JavaStartersBundle part 1")