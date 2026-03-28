import json
from pathlib import Path

def update_missing_keys():
    file_path = Path("missing_translations/missing_keys_korean.json")
    
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    ko_dict = {
        "command.0.to.execute": "실행할 <{0}>",
        "title.build.and.restart": "빌드 및 다시 시작",
        "build.module.0.and.restart": "모듈 ''{0}'' 빌드 및 다시 시작",
        "cannot.find.project": "프로젝트를 찾을 수 없습니다.",
        "choose.context.module": "컨텍스트 모듈 선택\\u2026",
        "icon.tool.tip.executed.command": "실행된 명령어",
        "icon.tool.tip.history.of.executed.commands": "실행된 명령어 내역", 
        "icon.tool.tip.input.line": "입력 줄",
        "icon.tool.tip.result": "결과",
        "icon.tool.tip.runtime.exception": "런타임 예외",
        "icon.tool.tip.system.help": "시스템 도움말",
        "icon.tool.tip.waiting.for.input": "입력 대기 중\\u2026",
        "icon.tool.tip.write.your.commands.here": "여기에 명령어를 작성하세요.",
        "message.type.error": "오류:",
        "message.type.info": "정보:",
        "message.type.warning": "경고:",
        "name.kotlin.repl": "Kotlin REPL (실험적 기능)",
        "kotlin.repl.configuration.error": "Kotlin REPL 구성 오류",
        "no.modules.were.found": "모듈을 찾을 수 없습니다.",
        "project.not.found": "프로젝트를 찾을 수 없습니다.",
        "there.were.compilation.errors.in.module.0": "모듈 {0}에 컴파일 오류가 있습니다.",
        "you.re.running.the.repl.with.outdated.classes": "오래된 클래스로 REPL을 실행하고 있습니다:\\u0020",
        "constructor.title.0.in.module.1": "{0} (모듈 {1})",
        "build.module.0.and.restart1": "모듈 ''{0}''을(를) 빌드하고 다시 시작합니다.",
        "internal.error.occurred.please.send.report.to.developers": "내부 오류가 발생했습니다. 개발자에게 보고서를 보내주세요.\\n",
        "progress.starting.repl": "REPL 시작 중\\u2026",
        "kotlin.repl.is.experimental": "Kotlin IDE REPL 지원은 실험적 기능입니다. 속도가 느리거나 불안정할 수 있습니다. 문제는 https://youtrack.jetbrains.com/issues/KTIJ 에 보고해 주세요."
    }
    
    filename = "KotlinIdeaReplBundle.properties"
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
