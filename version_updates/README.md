# Version Updates

이 디렉토리는 Android Studio 및 플러그인 업데이트에 따른 properties 파일 변경사항을 관리하기 위한 폴더입니다.

## 폴더 구조

```
version_updates/
├── android_studio/     # Android Studio 버전별 변경사항
└── plugins/            # 플러그인별 변경사항
```

## 사용 방법

### Android Studio 업데이트 시

1. `android_studio/` 폴더로 이동
2. 새 버전에 해당하는 폴더 생성 (예: `2024.1.1/`)
3. 변경된 properties 파일들을 해당 폴더에 저장
4. `CHANGELOG.md`에 변경사항 기록

### 플러그인 추가/업데이트 시

1. `plugins/` 폴더로 이동
2. 플러그인 이름으로 폴더 생성 (예: `kotlin-plugin/`)
3. 해당 플러그인에서 추가된 properties 파일들을 저장
4. `README.md`에 플러그인 정보 및 적용 방법 기록

## 워크플로우

1. **새 버전 감지**
   - Android Studio 업데이트 또는 플러그인 설치 감지

2. **Properties 파일 추출**
   - 새로운 버전/플러그인의 jar 파일에서 properties 파일 추출
   - `scripts/extract_keys.py`를 사용하여 새로운 키 확인

3. **차이점 비교**
   - 기존 파일과 비교하여 추가/변경/삭제된 키 식별
   - 변경사항을 해당 버전 폴더에 저장

4. **번역 업데이트**
   - 새로 추가된 키에 대한 한국어 번역 작성
   - 기존 번역 파일에 병합

5. **테스트 및 배포**
   - 플러그인 빌드 및 테스트
   - 버전 태그 생성 및 배포

## 자동화 스크립트

향후 추가될 스크립트들:
- `check_version.py` - Android Studio 버전 확인
- `extract_new_keys.py` - 새로운 키 추출
- `merge_translations.py` - 번역 병합
- `generate_diff.py` - 버전 간 차이점 생성

## 참고사항

- 각 버전/플러그인 폴더에는 반드시 `README.md` 파일을 포함해야 합니다.
- 변경사항은 명확하게 문서화되어야 합니다.
- 원본 파일과 번역 파일을 모두 보관합니다.
