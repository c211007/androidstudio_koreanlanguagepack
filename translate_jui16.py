import json

ko_dict = {
  "button.reset.defaults": "기본값으로 재설정",
  "label.files.to.download": "다운로드할 파일(&F):",
  "label.copy.downloaded.files.to": "다운로드한 파일을 복사할 위치(&T):",
  "checkbox.download.javadocs": "Javadocs 다운로드(&J)",
  "checkbox.download.sources": "소스 다운로드(&S)",
  "checkbox.copy.library.files.to": "다음에 라이브러리 파일 복사(&C):",
  "label.name": "이름(&N):",
  "label.loading.available.versions": "사용 가능한 버전 로드 중(&L)…",
  "button.reload": "다시 로드(&R)",
  "label.version": "버전(&V):",
  "checkbox.download.javadocs2": "Javadocs 다운로드(&J)",
  "download.javadocs": "Javadocs 다운로드",
  "checkbox.download.annotations": "어노테이션 다운로드(&N)",
  "download.sources": "소스 다운로드",
  "label.failed.to.load.versions": "버전을 로드하지 못했습니다.",
  "label.maven": "Maven:",
  "button.configure": "구성(&C)…",
  "button.create": "생성(&C)…",
  "radio.button.download": "다운로드(&D)",
  "radio.button.use.library": "라이브러리 사용(&U):",
  "label.label": "레이블",
  "label.loading.versions": "버전 로드 중…",
  "radio.button.set.up.library.later": "나중에 라이브러리 설정(&L)",
  "label.use.library": "라이브러리 사용:",
  "button.edit3": "편집(&E)…",
  "checkbox.sources": "소스(&S)",
  "checkbox.transitive.dependencies": "전이적 종속성(&T)",
  "checkbox.annotations": "어노테이션(&N)",
  "label.description": "설명",
  "checkbox.download.to": "다운로드 위치:",
  "checkbox.include.transitive.dependencies": "전이적 종속성 포함(&T)",
  "label.info": "정보",
  "checkbox.javadocs": "Javadocs(&D)",
  "checkbox.show.content.of.elements": "요소의 콘텐츠 표시",
  "label.select.artifact.type": "아티팩트 유형 선택(&T):",
  "label.cannot.load.artifact": "아티팩트를 로드할 수 없음",
  "item.name.with.module": "{0}(모듈 {1})",
  "refresh.library.roots.action.name": "라이브러리 루트 새로고침",
  "project.structure.title": "프로젝트",
  "project.structure.comment": "모든 모듈의 기본 설정입니다. 필요한 경우 모듈 페이지에서 각 모듈에 대한 이러한 매개변수를 구성합니다."
}

with open('missing_translations/missing_keys_korean.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for file_entry in data['new_files']:
    if file_entry['filename'] == 'JavaUiBundle.properties':
        file_entry['keys'].update(ko_dict)
        print("Updated JavaUiBundle.properties (Keys 601-640)")
        break

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
