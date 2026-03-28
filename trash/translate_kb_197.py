import json
from pathlib import Path

def update_missing_keys():
    file_path = Path("missing_translations/missing_keys_korean.json")

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    ko_dict = {
        "sh.code.style.binary.ops.like.and.may.start.a.line": "이항 연산자 뒤 줄바꿈 허용",
        "sh.code.style.choose.path": "Shfmt 경로 선택:",
        "sh.code.style.download.link": "shfmt 포매터 다운로드",
        "sh.code.style.keep.column.alignment.padding": "열 정렬 패딩 유지",
        "sh.code.style.minify.program.to.reduce.its.size": "크기를 줄이기 위해 프로그램 축소",
        "sh.code.style.unix.line.separator": "Unix 줄 구분 기호(\\\\n) 사용",
        "sh.code.style.redirect.operators.will.be.followed.by.a.space": "리디렉션 연산자 뒤에 공백 추가",
        "sh.code.style.switch.cases.will.be.indented": "case 문 들여쓰기",
        "sh.disable.inspection.text": "검사 {0} 비활성화",
        "sh.explain.command.to.explain": "설명할 명령어",
        "sh.explain.inspection.text": "셸 설명",
        "sh.explain.message.nothing.to.explain": "설명할 항목 없음",
        "sh.explain.title.nothing.to.explain": "설명할 항목 없음",
        "sh.fmt.cannot.download": "shfmt 포매터를 다운로드할 수 없습니다. 수동으로 설치하세요.",
        "sh.fmt.cannot.update": "shfmt 포매터를 업데이트할 수 없습니다. 이전 버전으로 롤백했습니다.",
        "sh.fmt.formatter": "Shfmt 포매터",
        "sh.fmt.indent.label": "들여쓰기",
        "sh.fmt.update.question": "셸 스크립트 포매터를 \"{0}\"에서 \"{1}\"(으)로 업데이트하시겠습니까?",
        "sh.fmt.install.question": "셸 스크립트 포매터를 설치하시겠습니까?",
        "sh.fmt.success.update": "셸 스크립트 포매터가 성공적으로 업데이트되었습니다.",
        "sh.fmt.success.install": "셸 스크립트 포매터가 성공적으로 설치되었습니다.",
        "sh.fmt.missing.formatter": "포매터 누락",
        "sh.parser.expected.similar.close.bracket": "유사한 닫는 대괄호가 필요합니다.",
        "sh.path.label": "경로:",
        "sh.rename.all.occurrences": "모든 항목 이름 바꾸기",
        "sh.rename.occurence": "{0} 이름 바꾸기",
        "sh.shell.script": "셸 스크립트",
        "notification.group.shell.script": "사용 가능한 셸 스크립트 도구",
        "intention.shell.script": "셸 스크립트",
        "filetype.sh.shell.script.description": "셸 스크립트",
        "sh.shellcheck.download.label.text": "shellcheck 다운로드",
        "sh.shellcheck.cannot.download": "shellcheck를 다운로드할 수 없습니다. 수동으로 설치하세요.",
        "sh.shellcheck.cannot.update": "shellcheck를 업데이트할 수 없습니다. 이전 버전으로 롤백했습니다.",
        "sh.shellcheck.path.label": "Shellcheck 경로 선택:",
        "sh.shellcheck.install.question": "셸 스크립트를 확인하기 위해 shellcheck를 설치하시겠습니까?",
        "sh.shellcheck.update.question": "shellcheck를 \"{0}\"에서 \"{1}\"(으)로 업데이트하시겠습니까?",
        "sh.shellcheck.success.install": "Shellcheck가 성공적으로 설치되었습니다.",
        "sh.shellcheck.success.update": "Shellcheck가 성공적으로 업데이트되었습니다.",
        "sh.shellcheck.missing": "\\ shellcheck 누락",
        "sh.suppress.inspection": "{0} 억제",
        "sh.unnamed.element.presentable.name": "<이름 없음>",
        "sh.label.download.shfmt.formatter": "shfmt 포매터 다운로드",
        "sh.label.choose.interpreter": "인터프리터 선택",
        "sh.label.choose.script.working.directory": "스크립트 작업 디렉토리 선택",
        "sh.label.choose.shell.script": "셸 스크립트 선택",
        "action.ShGenerateUntilLoop.text": "Until 루프",
        "action.ShGenerateUntilLoop.description": "until 루프를 생성합니다.",
        "action.ShGenerateWhileLoop.text": "While 루프",
        "action.ShGenerateWhileLoop.description": "while 루프를 생성합니다.",
        "action.ShGenerateForLoop.text": "For 루프"
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
