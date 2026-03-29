# Scripts 디렉토리

이 폴더에는 프로젝트 관리를 위한 유틸리티 스크립트들이 포함되어 있습니다.

## 버전 관리 스크립트

### `check_version.py`
- **용도**: Android Studio 버전 확인 및 호환성 체크
- **사용법**: `python scripts/check_version.py`
- **설명**: 설치된 Android Studio 버전을 확인하고 현재 플러그인과의 호환성을 체크합니다.

### `extract_from_jar.py`
- **용도**: JAR 파일에서 properties 파일 추출
- **사용법**: `python scripts/extract_from_jar.py <Android Studio 경로> -o <출력폴더> [-v]`
- **설명**: Android Studio나 플러그인의 jar 파일에서 properties 파일을 자동으로 추출합니다.
- **예시**:
  ```bash
  # Windows
  python scripts/extract_from_jar.py "C:\Program Files\Android\Android Studio" -o extracted_properties -v

  # macOS
  python scripts/extract_from_jar.py "/Applications/Android Studio.app" -o extracted_properties

  # Linux
  python scripts/extract_from_jar.py /opt/android-studio -o extracted_properties
  ```

### `compare_versions.py`
- **용도**: 두 버전의 properties 파일 비교
- **사용법**: `python scripts/compare_versions.py <이전버전> <새버전> [-o 출력폴더] [-v]`
- **설명**: 버전 간 추가/변경/삭제된 키를 분석하고 리포트를 생성합니다.
- **예시**:
  ```bash
  python scripts/compare_versions.py \
    extracted_bundles/intellij/messages \
    version_updates/android_studio/2024.1.1/bundles \
    -o version_updates/android_studio/2024.1.1 \
    -v
  ```

## 번역 관련 스크립트

### `generate_translations.py`
- **용도**: AI를 사용하여 properties 파일을 자동 번역
- **사용법**: `python scripts/generate_translations.py`
- **설명**: 영어 원문을 한국어로 번역하여 properties 파일을 생성합니다.

### `quick_translate.py`
- **용도**: 빠른 번역 작업
- **사용법**: `python scripts/quick_translate.py`
- **설명**: 단순한 번역 작업을 빠르게 수행합니다.

### `restore_to_english.py`
- **용도**: 모든 properties 파일을 영어 원문으로 복원
- **사용법**: `python scripts/restore_to_english.py`
- **설명**: `extracted_bundles`의 원본 파일을 사용하여 모든 번역을 초기화합니다.

## 키 추출 스크립트

### `extract_keys.py`
- **용도**: properties 파일에서 키 목록 추출
- **사용법**: `python scripts/extract_keys.py`
- **설명**: 모든 properties 파일의 키를 분석하고 통계를 생성합니다.

### `extract_keys.sh`
- **용도**: Shell 스크립트를 사용한 키 추출
- **사용법**: `./scripts/extract_keys.sh`
- **설명**: Bash를 사용하여 키를 추출합니다.

## 유니코드 변환 스크립트

### `convert_to_unicode_escape.py`
- **용도**: 한글을 유니코드 이스케이프 시퀀스로 변환
- **사용법**: `python scripts/convert_to_unicode_escape.py`
- **설명**: properties 파일의 한글을 `\uXXXX` 형태로 변환합니다.

### `convert_from_unicode_escape.py`
- **용도**: 유니코드 이스케이프 시퀀스를 한글로 변환
- **사용법**: `python scripts/convert_from_unicode_escape.py`
- **설명**: `\uXXXX` 형태를 읽을 수 있는 한글로 변환합니다.

## 템플릿 및 프로젝트 관리

### `create_templates.py`
- **용도**: properties 파일 템플릿 생성
- **사용법**: `python scripts/create_templates.py`
- **설명**: 새로운 properties 파일 템플릿을 생성합니다.

### `cleanup_project.py`
- **용도**: 프로젝트 정리
- **사용법**: `python scripts/cleanup_project.py`
- **설명**: 불필요한 파일이나 임시 파일을 정리합니다.

## 워크플로우 예시

### Android Studio 업데이트 시

1. **버전 확인**
   ```bash
   python scripts/check_version.py
   ```

2. **Properties 파일 추출**
   ```bash
   python scripts/extract_from_jar.py "C:\Program Files\Android\Android Studio" -o temp_extracted -v
   ```

3. **버전 비교**
   ```bash
   python scripts/compare_versions.py \
     extracted_bundles/intellij/messages \
     temp_extracted \
     -o version_updates/android_studio/2024.1.1
   ```

4. **번역 작업**
   ```bash
   # 새로운 키만 번역
   python scripts/generate_translations.py --keys-only version_updates/android_studio/2024.1.1/added_keys.txt
   ```

### 플러그인 추가 시

1. **플러그인 properties 추출**
   ```bash
   python scripts/extract_from_jar.py ~/.AndroidStudio/config/plugins/Kotlin -o version_updates/plugins/kotlin-plugin/bundles
   ```

2. **번역 작업**
   ```bash
   python scripts/generate_translations.py --dir version_updates/plugins/kotlin-plugin/bundles
   ```

## 참고사항

- 모든 Python 스크립트는 프로젝트 루트 디렉토리에서 실행해야 합니다.
- 스크립트 실행 전에 필요한 의존성이 설치되어 있는지 확인하세요.
- `-v` 또는 `--verbose` 옵션으로 상세 출력을 활성화할 수 있습니다.
- `-h` 또는 `--help` 옵션으로 각 스크립트의 도움말을 확인할 수 있습니다.

