import json

ko_dict = {
  "show.dependencies": "종속성 표시",
  "dialog.message.are.you.sure.you.want.to.delete.this.library": "이 라이브러리를 정말 삭제하시겠습니까?",
  "x.more.problems": "{0}개의 문제 더 보기…",
  "label.build.process.configuration": "빌드 프로세스 구성",
  "label.x.unloaded.modules": "언로드된 모듈 {0}개",
  "label.unloaded.module": "언로드된 모듈 ''{0}''",
  "dialog.message.module.name": "모듈 이름:",
  "dialog.title.extract.module.from.package": "패키지에서 모듈 추출",
  "progress.title.extract.module.from.package": "''{0}'' 패키지를 별도의 모듈로 추출하는 중",
  "progress.step.extract.module.collecting.used.classes": "''{0}''에서 사용된 클래스 수집하는 중",
  "progress.step.extract.module.building.dependencies": "새 모듈의 종속성 구성 중",
  "progress.step.extract.module.collecting.dependent.modules": "''{0}''에 종속된 모듈 수집하는 중",
  "progress.step.extract.module.analyzing.dependent.modules": "종속된 모듈 분석하는 중",
  "progress.step.extract.module.preparing.to.extract": "별도의 모듈 추출 준비 중",
  "progress.step.extract.module.extracting": "새 모듈 생성 중",
  "button.text.extract.module": "추출",
  "checkbox.move.classes.to.separate.source.root": "클래스를 별도의 소스 루트로 이동:",
  "dialog.title.specify.path.to.new.source.root": "새 소스 루트 경로 지정",
  "dialog.comment.compile.modules": "참조를 찾기 위해 프로젝트가 컴파일됩니다.",
  "dialog.message.failed.to.extract.module": "모듈을 추출하지 못했습니다: {0}",
  "select": "선택",
  "intellij.idea.module.file.iml": "Intellij IDEA 모듈 파일(*.iml)",
  "directory.with.existing.sources": "<b>기존 소스</b>가 있는 디렉터리",
  "label.existing.library.will.be.used": "<b>{0}</b> 라이브러리가 사용됩니다.",
  "progress.text.searching.for.libraries": "라이브러리를 검색하는 중입니다. 잠시 기다려 주세요.",
  "progress.text.searching.for.modules": "모듈을 검색하는 중입니다. 잠시 기다려 주세요.",
  "checkbox.create.source.root": "소스 루트 생성(&C):",
  "label.project.format1": "프로젝트 형식:",
  "label.additional.libraries.and.frameworks": "추가 라이브러리 및 프레임워크(&F):",
  "checkbox.create.project.from.template": "템플릿에서 프로젝트 생성(&T)",
  "button.add": "추가(&A)",
  "button.edit": "편집(&E)",
  "button.remove": "제거(&R)",
  "button.test": "테스트(&T)",
  "button.add2": "추가(&D)",
  "button.edit2": "편집",
  "button.remove2": "제거",
  "button.reload.description": "{0}에서 로컬 Maven 데이터 다시 로드",
  "popup.reload.success.result": "{0} 라이브러리를 성공적으로 다시 로드했습니다.",
  "popup.reload.failed.result": "{0} 라이브러리 다시 로드 실패"
}

with open('missing_translations/missing_keys_korean.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for file_entry in data['new_files']:
    if file_entry['filename'] == 'JavaUiBundle.properties':
        file_entry['keys'].update(ko_dict)
        print("Updated JavaUiBundle.properties (Keys 561-600)")
        break

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
