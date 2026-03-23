# Android Studio 버전 변경 이력

이 파일은 Android Studio의 각 버전별 변경사항을 추적합니다.

## 형식

각 버전 항목은 다음 형식을 따릅니다:

```markdown
## [버전] - YYYY-MM-DD

### Added (추가됨)
- 새로 추가된 기능이나 키

### Changed (변경됨)
- 수정된 기능이나 키

### Removed (제거됨)
- 삭제된 기능이나 키

### Translation Status (번역 상태)
- 번역 진행 상황
```

---

## 작업 예정

### [2024.1.1] - TBD

- 버전 업데이트 대기중

---

## 예시

### [2024.1.0] - 2024-01-15

#### Added
- 새로운 AI 코드 완성 기능 관련 20개 키 추가 (ActionsBundle)
- `AiAssistantBundle.properties` 번들 추가 (150 keys)
- Gemini 통합 관련 메시지 추가 (IdeBundle)

#### Changed
- 빌드 관련 메시지 10개 개선 (BuildBundle)
- 디버거 UI 텍스트 일관성 개선 (XDebuggerBundle)
- 설정 화면 레이블 명확화 (OptionsBundle)

#### Removed
- 더 이상 사용되지 않는 레거시 기능 5개 키 제거
- 구버전 Android Lint 메시지 삭제

#### Translation Status
- ✅ 새로운 키 번역 완료 (170/170)
- ✅ 변경된 키 검토 완료
- ✅ 테스트 완료
- ✅ 플러그인 배포 완료 (v1.2.0)

---

## 기록 가이드

1. **날짜**: 실제 버전이 릴리즈된 날짜 사용
2. **Added**: 새로 생긴 기능과 관련된 키만 기록
3. **Changed**: 의미나 맥락이 변경된 키만 기록 (오타 수정은 제외)
4. **Removed**: 완전히 제거된 키만 기록
5. **Translation Status**: 해당 버전 작업의 완료 상태 체크리스트

## 참고

- Android Studio 공식 릴리즈 노트: https://developer.android.com/studio/releases
- IntelliJ Platform 변경 이력: https://www.jetbrains.com/idea/whatsnew/
