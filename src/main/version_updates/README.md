# Android Studio 한국어 번역 플러그인 버전 업데이트 워크플로우

이 폴더는 Android Studio의 새 버전이 출시되었을 때 번역 플러그인을 업데이트하는 전체 워크플로우를 관리합니다.

## 사용 방법

### 메인 스크립트 실행

```bash
cd src/main/version_updates
python workflow_manager.py
```

대화형 메뉴가 나타나며, 다음 작업들을 순차적으로 수행할 수 있습니다.

## 워크플로우 단계

### 1. Android Studio 버전 확인 및 플러그인 버전 수정

- Android Studio 설치 경로에서 현재 버전 확인
- gradle.properties 파일의 플러그인 버전 정보 업데이트
- platformVersion, pluginVersion, pluginSinceBuild 등을 수정

### 2. Android Studio에서 Properties Key 재추출

- 사용자 입력: Android Studio 설치 경로를 절대 경로로 입력
- Android Studio의 모든 JAR 파일을 검색
- messages/ 폴더의 .properties 파일들을 추출
- temp_extracted/studio_YYYYMMDD_HHMMSS/ 폴더에 저장

### 3. 재추출한 Key와 기존 Key 비교 및 차이점 확인

- temp_extracted/의 최신 추출본과 extracted_bundles/의 기존 파일 비교
- 완전히 새로운 파일, 누락된 키, 변경된 키 확인
- 결과를 missing_translations/ 폴더에 저장

### 4. 번역본 백업 후 병합

- 백업 생성: messages_backups/backup_YYYYMMDD_HHMMSS/
- 번역한 키들을 기존 파일에 병합
- 새 파일이 있으면 _ko.properties 파일 생성

### 5. 이전 백업으로 롤백

- 문제 발생 시 이전 백업으로 복원

## 주의사항

- 작업 4 실행 전 반드시 현재 플러그인이 정상 작동하는지 확인하세요
- Android Studio 경로는 반드시 절대 경로로 입력하세요
