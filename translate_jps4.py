import json

ko_dict = {
  "progress.details.extracting.project.caches": "프로젝트 캐시 추출 중",
  "progress.details.extracting.compilation.outputs.for.module": "{0} 모듈에 대한 컴파일 출력 추출 중",
  "progress.details.applying.changes.for.module": "{0} 모듈에 대한 변경 사항 적용 중",
  "progress.text.applying.jps.caches": "JPS 캐시 적용 중…",
  "progress.text.extracting.downloaded.results": "다운로드한 결과 추출 중…",
  "progress.text.calculating.affected.modules": "영향을 받는 모듈 계산 중",
  "progress.download.file.text": "''{1}''에서 ''{0}'' 다운로드 중…",
  "progress.downloading.0.files.text": "{0}개의 파일 다운로드 중…",
  "error.file.download.failed": "''{0}''을(를) 다운로드하지 못했습니다:\\n{1}"
}

with open('missing_translations/missing_keys_korean.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

filename = "JpsBuildBundle.properties"
found = False
for file_entry in data.get('new_files', []):
    if file_entry['filename'] == filename:
        file_entry['keys'].update(ko_dict)
        found = True
        break
if not found:
    data.setdefault('new_files', []).append({"filename": filename, "keys": ko_dict})

print(f"Updated {filename} (Keys 121-129)")

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
