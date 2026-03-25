# Android Studio 버전별 변경사항

이 폴더는 Android Studio의 각 버전별로 추가되거나 변경된 properties 파일을 관리합니다.

## 폴더 구조

```
android_studio/
├── 2024.1.1/           # 버전별 폴더
│   ├── README.md       # 해당 버전의 변경사항 설명
│   ├── new_keys.txt    # 새로 추가된 키 목록
│   ├── modified_keys.txt  # 변경된 키 목록
│   ├── removed_keys.txt   # 삭제된 키 목록
│   └── bundles/        # 변경된 properties 파일들
│       ├── ActionsBundle.properties
│       └── ...
└── CHANGELOG.md        # 전체 버전 변경 이력
```

## 새 버전 추가 방법

### 1. 버전 폴더 생성
```bash
mkdir version_updates/android_studio/2024.1.1
cd version_updates/android_studio/2024.1.1
```

### 2. Android Studio jar 파일에서 properties 추출
```bash
# Android Studio 설치 경로에서 jar 파일 찾기
find /path/to/android-studio -name "*.jar" -exec jar tf {} \; | grep .properties > all_properties.txt

# 특정 jar에서 properties 추출 예시
jar xf resources.jar messages/
```

### 3. 키 차이점 분석
```bash
# scripts 폴더의 도구 사용
python scripts/extract_keys.py --compare --old="../2024.1.0" --new="./bundles" > diff_report.txt
```

### 4. README.md 작성
```markdown
# Android Studio 2024.1.1 변경사항

## 릴리즈 정보
- **버전**: 2024.1.1
- **릴리즈 날짜**: 2024-03-15
- **변경사항**: [공식 릴리즈 노트 링크]

## 주요 변경사항
- 새로운 기능 X 추가로 인한 10개의 새로운 키 추가
- 기존 기능 Y 개선으로 인한 5개의 키 수정

## 번역 작업 상태
- [ ] 새로운 키 번역
- [ ] 수정된 키 검토
- [ ] 테스트 완료
```

### 5. 번역 작업
```bash
# 새로운 키만 추출하여 번역
python scripts/generate_translations.py --keys-only new_keys.txt

# 기존 번역 파일에 병합
python scripts/merge_translations.py --source="./bundles" --target="../../src/main/resources/messages"
```

## 버전 비교

### 이전 버전과 비교
```bash
# 2024.1.0과 2024.1.1 비교
python scripts/generate_diff.py \
  --old="version_updates/android_studio/2024.1.0" \
  --new="version_updates/android_studio/2024.1.1"
```

## CHANGELOG 업데이트

각 버전 작업 완료 후 `CHANGELOG.md`에 다음 형식으로 기록:

```markdown
## [2024.1.1] - 2024-03-15

### Added
- 10개의 새로운 키 추가 (ActionsBundle, IdeBundle)
- 새로운 번들: NewFeatureBundle.properties

### Changed
- 5개의 키 설명 개선
- UI 텍스트 일관성 개선

### Removed
- 더 이상 사용되지 않는 2개의 키 제거
```

## 자동화 스크립트 (향후 개발 예정)

- `check_as_version.py` - Android Studio 버전 자동 감지
- `extract_from_jar.py` - jar 파일에서 properties 자동 추출
- `generate_diff_report.py` - 버전 간 차이점 자동 생성
- `auto_merge.py` - 새로운 번역 자동 병합

## 주의사항

1. **백업**: 병합 전에 항상 현재 번역 파일을 백업하세요.
2. **테스트**: 병합 후 플러그인을 빌드하고 Android Studio에서 테스트하세요.
3. **문서화**: 모든 변경사항을 명확하게 문서화하세요.
4. **키 확인**: 새로운 키가 실제로 사용되는지 확인 후 번역하세요.
