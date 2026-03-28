import json
from pathlib import Path

def update_missing_keys():
    file_path = Path("missing_translations/missing_keys_korean.json")

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    ko_dict = {
        "action.ShGenerateForLoop.description": "for 루프를 생성합니다.",
        "action.runShellFileAction.text": "파일 실행",
        "action.runShellFileAction.description": "터미널에서 현재 셸 파일을 실행합니다.",
        "sh.color.function.declaration": "함수 선언",
        "sh.color.conditional.operators": "조건부 연산자",
        "sh.color.commands.subshell.command": "명령어//서브셸 명령어",
        "sh.color.commands.generic.command": "명령어//일반 명령어",
        "sh.color.redirection": "리디렉션",
        "sh.color.backquotes": "백틱(Backquotes)",
        "sh.color.braces.square.brackets": "대괄호/중괄호//대괄호([ ])",
        "sh.color.braces.curly.brackets": "대괄호/중괄호//중괄호({ })",
        "sh.color.braces.parentheses": "대괄호/중괄호//괄호(( ))",
        "sh.color.here.documents.end": "Here 문서 끝",
        "sh.color.here.documents.start": "Here 문서 시작",
        "sh.color.here.documents": "Here 문서",
        "sh.color.shebang.comment": "Shebang 주석",
        "sh.color.line.comment": "줄 주석",
        "sh.color.raw.string": "원시(Raw) 문자열",
        "sh.color.string": "문자열",
        "sh.color.variables.composed.variable": "변수//합성된 변수",
        "sh.color.variables.variable.declaration": "변수//변수 선언",
        "sh.color.variables.variable.usage": "변수//변수 사용",
        "sh.color.keyword": "키워드",
        "sh.color.number": "숫자",
        "sh.run.interpreter.options": "인터프리터 옵션:",
        "sh.run.interpreter.path": "인터프리터 경로:",
        "sh.run.interpreter": "인터프리터",
        "sh.run.interpreter.not.found": "인터프리터를 찾을 수 없습니다.",
        "sh.run.interpreter.should.be.executable": "인터프리터는 실행 파일이어야 합니다.",
        "sh.run.working.dir": "작업 디렉토리:",
        "sh.run.working.dir.not.found": "작업 디렉토리를 찾을 수 없습니다.",
        "sh.run.script.options": "스크립트 옵션:",
        "sh.run.script.path": "스크립트 경로:",
        "sh.run.script.not.found": "셸 스크립트를 찾을 수 없습니다.",
        "sh.run.execute.terminal": "터미널에서 실행",
        "sh.run.environment.variables": "환경 변수:",
        "sh.run.execute.script.text": "스크립트 텍스트",
        "sh.run.execute.script.text.title": "스크립트 텍스트:",
        "sh.run.execute.script.file": "스크립트 파일",
        "sh.run.execute": "실행:",
        "sh.livetemplate.description.fori": "목록의 For 루프",
        "sh.livetemplate.description.cmd": "명령어 대체",
        "sh.livetemplate.description.cmd.success.check": "명령어 성공 확인",
        "sh.livetemplate.description.tar.compress": "tar 압축",
        "sh.livetemplate.description.tar.decompress": "tar 압축 풀기",
        "sh.livetemplate.description.mkdir": "디렉토리 생성",
        "sh.livetemplate.description.git.branch.create": "브랜치 생성",
        "sh.livetemplate.description.git.push": "원격에 브랜치 푸시",
        "sh.livetemplate.description.git.commit": "변경 사항 커밋",
        "sh.livetemplate.description.curl": "Http 요청"
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
