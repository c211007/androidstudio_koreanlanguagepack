import json
from pathlib import Path

def update_missing_keys():
    file_path = Path("missing_translations/missing_keys_korean.json")

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    ko_dict = {
        "sh.livetemplate.description.rm": "파일 또는 디렉토리 제거",
        "sh.livetemplate.description.find": "파일 또는 디렉토리 찾기",
        "sh.livetemplate.description.heredoc": "여러 줄 문자열",
        "sh.livetemplate.description.xargs": "표준 입력에서 명령어 실행",
        "sh.livetemplate.description.system.info.linux": "Linux 시스템 정보",
        "sh.livetemplate.description.system.info.mac": "Mac OS 시스템 정보",
        "sh.livetemplate.description.system.kernel.info": "커널 정보",
        "sh.livetemplate.description.array.create": "배열 생성",
        "sh.livetemplate.description.array.all": "모든 배열 요소",
        "sh.livetemplate.description.array.at.index": "인덱스의 요소",
        "sh.livetemplate.description.array.length": "배열 길이",
        "sh.livetemplate.description.array.delete": "배열 삭제",
        "sh.livetemplate.description.array.delete.at": "배열에서 삭제",
        "sh.livetemplate.description.array.set.element": "인덱스에 배열 요소 설정",
        "sh.livetemplate.description.array.add": "배열의 끝에 새 항목 추가",
        "sh.livetemplate.description.array.iteration": "배열 반복",
        "sh.livetemplate.description.if": "If 문",
        "sh.livetemplate.description.elif": "Elif 표현식",
        "sh.livetemplate.description.select": "Select 표현식",
        "sh.livetemplate.description.case": "Case 문",
        "sh.livetemplate.description.for": "인덱스에 의한 For 루프",
        "sh.livetemplate.description.while": "조건에 의한 While 루프",
        "sh.livetemplate.description.until": "조건에 의한 Until 루프",
        "sh.livetemplate.description.function": "함수 정의",
        "sh.livetemplate.description.string.equal": "문자열이 같음",
        "sh.livetemplate.description.string.not.equal": "문자열이 같지 않음",
        "sh.livetemplate.description.string.is.empty": "문자열이 비어 있음",
        "sh.livetemplate.description.string.not.empty": "문자열이 비어 있지 않음",
        "sh.livetemplate.description.number.equal": "숫자가 같음",
        "sh.livetemplate.description.number.not.equal": "숫자가 같지 않음",
        "sh.livetemplate.description.number.less": "숫자가 더 작음",
        "sh.livetemplate.description.number.less.or.equal": "숫자가 작거나 같음",
        "sh.livetemplate.description.number.greater": "숫자가 더 큼",
        "sh.livetemplate.description.number.greater.or.equal": "숫자가 크거나 같음",
        "sh.livetemplate.description.file.exists": "파일이 존재함",
        "sh.livetemplate.description.file.not.empty": "파일이 비어 있지 않음",
        "sh.livetemplate.description.file.readable": "읽기 가능한 파일",
        "sh.livetemplate.description.file.writable": "쓰기 가능한 파일",
        "sh.livetemplate.description.file.executable": "실행 가능한 파일",
        "sh.livetemplate.description.file.equals": "파일이 같음",
        "sh.livetemplate.description.file.newer": "최신 파일",
        "sh.livetemplate.description.file.older": "오래된 파일",
        "sh.livetemplate.description.path.exists": "경로가 존재함",
        "sh.livetemplate.description.directory.exists": "디렉토리가 존재함",
        "sh.livetemplate.description.command.exists": "명령어가 존재함",
        "sh.update": "업데이트",
        "sh.install": "설치",
        "sh.no.thanks": "아니요",
        "sh.skip.version": "이 버전 건너뛰기",
        "sh.download": "다운로드"
    }

    filename = "ShBundle.properties"
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
