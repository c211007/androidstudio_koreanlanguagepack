import json
from pathlib import Path

def update_missing_keys():
    file_path = Path("missing_translations/missing_keys_korean.json")

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    ko_dict = {
        "sml.studiobot.timeline.agent.tool.singleFileEdit.diffComputed.proposeEdit": "제안된 변경 사항:",
        "sml.studiobot.timeline.agent.tool.singleFileEdit.diff.editorTitle": "변경 사항: {0} ({1})",
        "sml.studiobot.timeline.agent.tool.singleFileEdit.diff.before": "변경 전",     
        "sml.studiobot.timeline.agent.tool.singleFileEdit.diff.after": "변경 후",       
        "sml.studiobot.timeline.agent.tool.singleFileEdit.diff.result.waiting": "사용자가 변경 사항을 수락하거나 거부할 때까지 에이전트가 일시 중지됩니다…",    
        "sml.studiobot.timeline.agent.tool.singleFileEdit.diff.openInEditor": "Diff 편집기에서 열기",
        "sml.studiobot.timeline.agent.tool.askUser.submitButton.text": "제출",      
        "sml.studiobot.timeline.agent.tool.updateDepsRefactoring.running": "종속성 업데이트 리팩터링 시작",
        "sml.studiobot.timeline.agent.tool.updateDepsRefactoring.completed": "종속성 업데이트 리팩터링 완료",
        "sml.studiobot.timeline.agent.tool.gradle.running": "Gradle 빌드 실행 중: {0}",
        "sml.studiobot.timeline.agent.tool.gradle.completed": "Gradle 빌드 실행됨: {0}",
        "sml.studiobot.timeline.agent.tool.gradle.generic.running": "프로젝트 빌드 중",
        "sml.studiobot.timeline.agent.tool.gradle.generic.completed": "프로젝트 빌드됨",
        "sml.studiobot.timeline.agent.tool.gradle.sync.status": "Gradle 프로젝트 동기화 중…",
        "sml.studiobot.timeline.agent.tool.gradle.sync.running": "Gradle 동기화 실행 중…",
        "sml.studiobot.timeline.agent.tool.gradle.sync.completed": "Gradle 동기화 실행됨", 
        "sml.studiobot.timeline.agent.tool.gradle.assembleAll.status": "Gradle 프로젝트 빌드 중…",
        "sml.studiobot.timeline.agent.tool.gradle.assembleAll.running": "모든 하위 프로젝트 어셈블 중",
        "sml.studiobot.timeline.agent.tool.gradle.assembleAll.completed": "모든 하위 프로젝트 어셈블됨",
        "sml.studiobot.timeline.agent.tool.gradle.status": "Gradle 프로젝트 빌드 중…",
        "sml.studiobot.timeline.agent.tool.gradle.getAssembleTask.running": "{0}:{1}의 어셈블 작업 찾는 중…",
        "sml.studiobot.timeline.agent.tool.gradle.getAssembleTask.completed": "{0}:{1}의 어셈블 작업 찾음",
        "sml.studiobot.timeline.agent.tool.gradle.getBuildFileLocation.running": "{0}의 빌드 파일 찾는 중…",
        "sml.studiobot.timeline.agent.tool.gradle.getBuildFileLocation.completed": "{0}의 빌드 파일 찾음",
        "sml.studiobot.timeline.agent.tool.gradle.getSourceFolders.running": "{0}:{1}의 소스 폴더 찾는 중…",
        "sml.studiobot.timeline.agent.tool.gradle.getSourceFolders.completed": "{0}:{1}의 소스 폴더 찾음",
        "sml.studiobot.timeline.agent.tool.gradle.getArtifactFromFile.running": "{0}의 Gradle 아티팩트 찾는 중…",
        "sml.studiobot.timeline.agent.tool.gradle.getArtifactFromFile.completed": "{0}의 Gradle 아티팩트 찾음",
        "sml.studiobot.timeline.agent.tool.gradle.getTestArtifacts.running": "{0}의 테스트 아티팩트 찾는 중…",
        "sml.studiobot.timeline.agent.tool.gradle.getTestArtifacts.completed": "{0}의 테스트 아티팩트 찾음",
        "sml.studiobot.timeline.agent.tool.gradle.getTestTask.running": "{0}:{1}의 테스트 작업 찾는 중…",
        "sml.studiobot.timeline.agent.tool.gradle.getTestTask.completed": "{0}:{1}의 테스트 작업 찾음",
        "sml.studiobot.timeline.agent.tool.gradle.getArtifactConsumers.running": "{0}:{1}의 소비자 찾는 중…",
        "sml.studiobot.timeline.agent.tool.gradle.getArtifactConsumers.completed": "{0}:{1}의 소비자 찾음",
        "sml.studiobot.timeline.agent.tool.gradle.getTopLevelSubProjects.running": "최상위 하위 프로젝트 아티팩트 찾는 중…",
        "sml.studiobot.timeline.agent.tool.gradle.getTopLevelSubProjects.completed": "최상위 하위 프로젝트 아티팩트 찾음",
        "sml.studiobot.timeline.agent.tool.saveSummary.running": "코드베이스 요약 저장 중…",
        "sml.studiobot.timeline.agent.tool.saveSummary.completed": "코드베이스 요약 저장됨",
        "sml.studiobot.timeline.agent.tool.screenshot.running": "스크린샷 찍는 중…",
        "sml.studiobot.timeline.agent.tool.screenshot.completed": "스크린샷 찍음",  
        "sml.studiobot.timeline.agent.tool.releaseNotes.running": "{0}:{1}:{2}–{3}의 릴리스 노트 가져오는 중…",
        "sml.studiobot.timeline.agent.tool.releaseNotes.completed": "{0}:{1}:{2}–{3}의 릴리스 노트 찾음",
        "sml.studiobot.timeline.agent.tool.addLineBreakpoint.running": "{0}:{1}에 중단점 추가하는 중…",
        "sml.studiobot.timeline.agent.tool.addLineBreakpoint.completed": "{0}:{1}에 중단점 추가됨",
        "sml.studiobot.timeline.agent.tool.addLogBreakpoint.running": "{0}:{1}에 로깅 중단점 추가하는 중…",
        "sml.studiobot.timeline.agent.tool.addLogBreakpoint.completed": "{0}:{1}에 로깅 중단점 추가됨",
        "sml.studiobot.timeline.agent.tool.evalExpression.running": "표현식 {0} 평가하는 중…",
        "sml.studiobot.timeline.agent.tool.evalExpression.completed": "표현식 {0} 평가됨",
        "sml.studiobot.timeline.agent.tool.debugStep.running": "디버거({0}) 스텝 이동하는 중…",
        "sml.studiobot.timeline.agent.tool.debugStep.completed": "디버거({0}) 스텝 이동됨"
    }

    filename = "SmlBundle.properties"
    for file_entry in data.get('new_files', []):
        if file_entry['filename'] == filename:
            file_entry['keys'].update(ko_dict)
            break
            
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    update_missing_keys()
