import json
from pathlib import Path

def update_missing_keys():
    file_path = Path("missing_translations/missing_keys_korean.json")
    
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    ko_dict = {
        "classpath.add.reflection": "클래스 경로에 'kotlin-reflect.jar' 추가",      
        "classpath.add.script.runtime": "클래스 경로에 'kotlin-script-runtime.jar' 추가",
        "classpath.add.kotlin.test": "클래스 경로에 'kotlin-test.jar' 추가",        
        "text.was.modified": "{0}이(가) 수정되었습니다.",
        "scratch.clear.button": "결과 지우기",
        "scratch.inlay.output.mode.title": "인레이 출력 모드\\n\\n출력은 표현식 바로 옆 코드 편집기에 표시됩니다. 짧은 한 줄 출력에 적합합니다.",
        "scratch.inlay.output.mode.description": "인레이 출력 모드",
        "scratch.side.panel.output.mode.title": "측면 패널 출력 모드\\n\\n출력이 별도의 패널에 표시됩니다. 출력이 길거나 여러 줄인 경우에 유용합니다.", 
        "scratch.side.panel.output.mode.description": "측면 패널 출력 모드",       
        "scratch.module.combobox": "모듈의 클래스 경로 사용",
        "scratch.run.button": "스크래치 파일 실행",
        "scratch.run.from.here.button": "여기서부터 스크래치 실행",
        "scratch.stop.button": "스크래치 실행 중지",
        "scratch.is.repl.checkbox": "REPL 사용",
        "scratch.is.repl.checkbox.description": "Kotlin REPL에서 실행합니다. 스크래치 끝에 추가된 새 표현식만 실행합니다.",
        "scratch.is.interactive.checkbox": "대화형 모드",
        "scratch.is.interactive.checkbox.description": "입력을 중지하고 {0}초 후에 실행됩니다.",
        "scratch.make.before.run.checkbox": "실행 전 모듈 Make",
        "scratch.make.before.run.checkbox.description": "스크래치를 실행하기 전에 {0} 모듈을 Make합니다. 이 범위에서는 컴파일된 코드만 도달할 수 있습니다.",
        "frameworks.remove.conflict.title": "프레임워크 충돌",
        "frameworks.remove.conflict.question": "현재 모듈이 이미 ''{0}'' 프레임워크로 구성되어 있습니다.\\n제거하시겠습니까?",
        "library.label.jvm": "Kotlin 런타임",
        "library.label.javascript": "Kotlin JS 라이브러리",
        "library.no.kotlin.library.title": "지정된 Kotlin 런타임 없음",
        "library.no.kotlin.library.question": "Kotlin 런타임 라이브러리 없이 계속하시겠습니까?",
        "there.aren.t.configurators.available": "사용 가능한 구성 도구가 없습니다.",
        "all.modules.with.kotlin.files.are.configured": "Kotlin 파일이 있는 모든 모듈이 구성되었습니다.",
        "lookup.project.configurators.progress.text": "프로젝트 구성 도구 찾는 중\\u2026",
        "libraries.for.the.following.platform.are.also.present.in.the.module.dependencies.0": "다음 플랫폼용 라이브러리도 모듈 종속성에 있습니다: {0}",
        "label.missed.libraries.text": "모듈 종속성 목록에서 ''{0}'' 라이브러리를 찾을 수 없습니다.",
        "no.target.platforms.selected": "선택된 대상 플랫폼이 없습니다.",
        "presentable.name.kotlin.js": "Kotlin/\\u200BJS",
        "this.java.file.is.outside.of.java.source.roots.and.won.t.be.added.to.the.classpath": "이 .java 파일은 Java 소스 루트 외부에 있으며 클래스 경로에 추가되지 않습니다.",
        "kotlin.bytecode.decompiler": "Kotlin 바이트코드 디컴파일러",
        "failed.to.decompile.0.1": "{0} 디컴파일 실패: {1}",
        "button.text.decompile": "디컴파일",
        "checkbox.text.assertions": "어설션(Assertions)",
        "checkbox.text.optimization": "최적화",
        "checkbox.text.inline": "인라인",
        "checkbox.text.offsets": "오프셋 표시",
        "cannot.compile.0.to.bytecode": "{0}을(를) 바이트코드로 컴파일할 수 없습니다.",
        "create.backup.for.debugging.kotlin.incremental.compilation": "Kotlin 증분 컴파일 디버깅을 위한 백업 만들기",
        "creating.backup.for.debugging.kotlin.incremental.compilation": "Kotlin 증분 컴파일 디버깅을 위한 백업을 만드는 중",
        "creating.patch.0": "패치 {0} 생성 중",
        "copying.logs": "로그 복사 중",
        "copying.project.s.system.dir": "프로젝트의 시스템 디렉토리 복사 중",
        "scanning.project.dir.0": "프로젝트 디렉토리 스캔 중: {0}",
        "adding.file.to.backup.0": "백업에 파일 추가 중: {0}",
        "created.backup": "백업을 생성했습니다.",
        "successfully.created.backup.0": "성공적으로 백업 {0}을(를) 생성했습니다."
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
