import json
from pathlib import Path

def update_missing_keys():
    file_path = Path("missing_translations/missing_keys_korean.json")
    
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    ko_dict = {
        "android.lint.inspections.accidental.octal": "의도치 않은 8진수",
        "android.lint.inspections.assertion.side.effect": "부작용이 있는 어설션",
        "android.lint.inspections.bad.hostname.verifier": "안전하지 않은 HostnameVerifier",
        "android.lint.inspections.bidi.spoofing": "양방향 텍스트 스푸핑",
        "android.lint.inspections.build.list.adds": "buildList에서 누락된 add 호출",
        "android.lint.inspections.check.result": "결과 무시 중",
        "android.lint.inspections.default.locale": "대소문자 변환에 암시적 기본 로케일 사용됨",
        "android.lint.inspections.discouraged.api": "권장하지 않는 API 사용",
        "android.lint.inspections.easter.egg": "코드에 이스터 에그 포함됨",
        "android.lint.inspections.empty.super.call": "빈 상위 메서드 호출",
        "android.lint.inspections.expensive.assertion": "비용이 많이 드는 어설션",
        "android.lint.inspections.file.ends.with.ext": "파일 확장자에 파일 endsWith 사용",
        "android.lint.inspections.gradle.dependency": "사용되지 않는 Gradle 종속성",
        "android.lint.inspections.gradle.deprecated.configuration": "지원 중단된 Gradle 구성",
        "android.lint.inspections.gradle.dynamic.version": "Gradle 동적 버전",
        "android.lint.inspections.gradle.ide.error": "Gradle IDE 지원 문제",
        "android.lint.inspections.gradle.path": "Gradle 경로 문제",
        "android.lint.inspections.ignore.without.reason": "이유 없는 @Ignore",
        "android.lint.inspections.implicit.sam.instance": "암시적 SAM 인스턴스",
        "android.lint.inspections.java.plugin.language.level": "명시적 Java 언어 레벨이 제공되지 않음",
        "android.lint.inspections.jcenter.repository.obsolete": "JCenter Maven 저장소가 읽기 전용입니다",
        "android.lint.inspections.kotlin.property.access": "Kotlin 속성 액세스",
        "android.lint.inspections.lambda.last": "마지막의 람다 매개변수",
        "android.lint.inspections.lint.baseline.fixed": "기준선 문제 해결됨",
        "android.lint.inspections.lint.baseline": "기준선 적용됨",
        "android.lint.inspections.local.suppress": "잘못된 요소에 @SuppressLint 사용됨",
        "android.lint.inspections.member.extension.conflict": "멤버 및 확장의 적용 가능한 후보 충돌",
        "android.lint.inspections.merge.marker": "코드에 병합 마커 포함됨",
        "android.lint.inspections.missing.super.call": "상위 호출 누락됨",
        "android.lint.inspections.newer.version.available": "사용할 수 있는 최신 라이브러리 버전 있음",
        "android.lint.inspections.no.hard.keywords": "하드 Kotlin 키워드 없음",
        "android.lint.inspections.no.op": "NoOp 코드",
        "android.lint.inspections.not.constructor": "생성기가 아님",
        "android.lint.inspections.not.interpolated": "잘못된 보간",
        "android.lint.inspections.open.for.testing": "테스트에서만 API 확장 허용됨",
        "android.lint.inspections.property.escape": "잘못된 속성 이스케이프",
        "android.lint.inspections.proxy.password": "일반 텍스트 형식의 프록시 비밀번호",
        "android.lint.inspections.range": "범위 벗어남",
        "android.lint.inspections.restricted.api": "제한된 API",
        "android.lint.inspections.return.this": "메서드는 this를 반환해야 함",
        "android.lint.inspections.secret.in.source": "소스 코드의 보안 비밀",
        "android.lint.inspections.secure.random": "SecureRandom에 고정 시드 사용됨",
        "android.lint.inspections.shift.flags": "위험한 플래그 상수 선언",
        "android.lint.inspections.similar.gradle.dependency": "여러 버전 Gradle 종속성",
        "android.lint.inspections.simple.date.format": "날짜 형식의 암시적 로케일",
        "android.lint.inspections.sqlite.string": "TEXT 대신 STRING을 사용 중",
        "android.lint.inspections.stop.ship": "코드에 STOPSHIP 마커 포함됨",
        "android.lint.inspections.support.annotation.usage": "잘못된 지원 주석 사용",
        "android.lint.inspections.suspicious.indentation": "의심스러운 들여쓰기",
        "android.lint.inspections.text.concat.space": "텍스트 연결에 공백이 누락되었나요?"
    }
    
    filename = "LintBundle.properties"
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
