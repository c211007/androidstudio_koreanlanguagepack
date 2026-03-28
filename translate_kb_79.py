import json
from pathlib import Path

def update_missing_keys():
    file_path = Path("missing_translations/missing_keys_korean.json")
    
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    ko_dict = {
        "exception.occurs.during.run.scratch.action": "스크래치 실행 작업 중 예외 발생",
        "there.were.compilation.errors.in.module.0": "모듈 {0}에 컴파일 오류가 있습니다.",
        "other.scratch.file.execution.is.in.progress": "다른 스래치 파일 실행이 진행 중입니다.",
        "exception.occurred.during.run.scratch.action1": "스크래치 실행 작업 중 예외가 발생했습니다.",
        "couldn.t.extract.line.info.from.line.0": "다음 줄에서 줄 정보를 추출할 수 없습니다: {0}",
        "couldn.t.compile.0": "{0}을(를) 컴파일할 수 없습니다.",
        "couldn.t.find.ktfile.for.current.editor": "현재 편집기에 대한 KtFile을 찾을 수 없습니다.",
        "couldn.t.get.scratch.execution.result.stopped.by.timeout.0.ms": "스크래치 실행 결과를 가져올 수 없습니다 - 시간 초과로 중지됨 ({0}ms)",
        "running.kotlin.scratch": "Kotlin 스크래치 실행 중\\u2026",
        "couldn.t.execute.statement.0": "문을 실행할 수 없습니다: {0}",
        "couldn.t.stop.repl.process": "REPL 프로세스를 중지할 수 없습니다.",
        "presentable.name.kotlin.jvm": "Kotlin/JVM",
        "fix.0.in.current.module": "현재 모듈의 {0}",
        "fix.0.in.the.project": "프로젝트의 {0}",
        "enable.feature.family": "{0,choice,0#모듈|1#프로젝트}의 {1,choice,0#API 버전|1#언어 버전} 올리기",
        "enable.feature.text": "{0,choice,0#모듈|1#프로젝트}의 {1,choice,0#API 버전|1#언어 버전}을 {2}(으)로 설정",
        "list.item.no.module": "<모듈 없음>",
        "bytecode.toolwindow.label.jvm.target": "JVM 대상:",
        "notification.group.configure.kotlin.in.project": "Kotlin 프로젝트 구성 필요",
        "progress.title.run.scratch": "스크래치 파일 실행 중",
        "command.name.processing.kotlin.scratch.output": "Kotlin 스크래치 출력 처리",
        "progress.title.compiling.kotlin.scratch": "스크래치 파일 컴파일 중"
    }
    
    filename = "KotlinJvmBundle.properties"
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
