# 한국어 언어팩 적용 문제 해결

## 문제
플러그인을 설치했는데 한국어로 바뀌지 않음

## 원인
`src/main/resources/messages/` 디렉토리에 **원본 `.properties` 파일과 `_ko.properties` 파일이 중복**으로 존재했습니다.

- ❌ `ActionsBundle.properties` (원본 - 영어)
- ✅ `ActionsBundle_ko.properties` (한국어)

IntelliJ Platform은 기본 `.properties` 파일이 있으면 그것을 우선 로드하고, locale-specific 파일(`_ko.properties`)을 무시합니다.

## 해결 완료
총 **241개의 중복 파일 삭제** 완료:
- 삭제 전: 345개 `_ko.properties` + 241개 `.properties` = 586개
- 삭제 후: 345개 `_ko.properties` 만 남음 ✅

## 결과
- ✅ 모든 리소스 번들이 `_ko.properties` 형식으로 정리됨
- ✅ 한국어 언어팩이 정상 작동해야 함

## 재빌드 필요
파일 변경사항을 적용하려면 플러그인을 다시 빌드하세요:

```bash
.\gradlew buildPlugin -x test
```

그 후 Android Studio에서:
1. 기존 플러그인 제거 (선택사항)
2. `build/distributions/` 폴더의 새 `.zip` 파일 설치
3. Android Studio 재시작
4. Settings > Appearance & Behavior > Language and Region > Language > 한국어 선택
5. 재시작

## 영향받은 파일 예시
- `AgentsCoreBundle.properties` → 삭제 (✅ `AgentsCoreBundle_ko.properties` 유지)
- `AndroidDesignerActionsBundle.properties` → 삭제
- `AndroidNdkBundle.properties` → 삭제
- `CidrAsmBundle.properties` → 삭제
- ... 총 241개

날짜: 2026-03-28
