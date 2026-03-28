import json

translations = {
  "sml.studiobot.settings.sandbox.networkAccess": "네트워크 액세스 허용",       
  "sml.studiobot.settings.sandbox.skipShellConfirmWithSandbox": "샌드박스가 사용 설정된 경우 셸 명령어 확인을 요구하지 않음",
  "sml.studiobot.settings.sandbox.wrapperCommand": "래퍼(Wrapper) 명령어",
  "sml.studiobot.settings.sandbox.wrapperCommand.comment": "예: docker run --rm -v $SANDBOX_ROOT:/work -w /work alpine",
  "sml.studiobot.settings.sandbox.type.macos": "기본 제공 macOS 샌드박스(sandbox-exec)",
  "sml.studiobot.settings.sandbox.type.runtime": "Anthropic 샌드박스 런타임",   
  "sml.studiobot.settings.sandbox.runtimePath": "샌드박스 런타임 경로",
  "sml.studiobot.settings.sandbox.runtimePath.comment.html": "sandbox-runtime 실행 파일 경로(일반적으로 'npm install -g @anthropic-ai/sandbox-runtime'을 통해 설치됨). <a href=\"https://github.com/anthropic-experimental/sandbox-runtime\">설치 안내</a>",
  "sml.studiobot.settings.sandbox.type.docker": "Docker 컨테이너",
  "sml.studiobot.settings.sandbox.dockerImage": "Docker 이미지",
  "sml.studiobot.settings.sandbox.dockerImage.comment": "명령어를 실행할 경량 이미지(예: alpine, ubuntu:latest)",
  "sml.studiobot.settings.sandbox.type.bubblewrap": "Bubblewrap(Linux)",       
  "sml.studiobot.settings.sandbox.type.custom": "맞춤 래퍼 명령어",       
  "sml.studiobot.settings.sandbox.executableNotFound": "경고: 시스템 경로에서 실행 파일 ''{0}''을(를) 찾을 수 없습니다.",
  "sml.studiobot.settings.sandbox.specifyCommand": "명령어를 지정해 주세요",  
  "sml.studiobot.settings.sandbox.specifyPath": "경로를 지정해 주세요",        
  "sml.studiobot.settings.sandbox.allowReadOutsideSandbox": "에이전트 권한 설정에서 허용하는 경우 샌드박스 외부의 파일 액세스 허용",
  "sml.studiobot.settings.sandbox.allowReadOutsideSandbox.comment": "(시스템 폴더와 같은 몇몇 디렉터리에 대한 읽기는 이미 허용되어 있으며, 임시 폴더에 대한 쓰기도 허용됩니다. 또한 파일 형식 검사를 수행하지 않으며 모든 파일이 포함됩니다.)",
  "sml.studiobot.settings.sandbox.noFileSupportHint": "참고: 이 샌드박스 전략은 \"샌드박스 외부 읽기 허용\" 설정을 지원하지 않습니다. 래퍼 명령어나 환경에서 추가 파일 액세스를 수동으로 구성해야 합니다.",
  "sml.studiobot.settings.modelProviders.library.title": "모델 제공업체",     
  "sml.studiobot.settings.modelProviders.display.name": "모델 제공업체",      
  "sml.studiobot.settings.modelProviders.addModelProvider.addButton": "추가",    
  "sml.studiobot.settings.modelProviders.addModelProvider.removeButton": "삭제",
  "sml.studiobot.settings.modelProviders.addModelProvider.addLocalModelProviderAction": "로컬 제공업체",
  "sml.studiobot.settings.modelProviders.addModelProvider.addRemoteModelProviderAction": "타사 원격 제공업체",
  "sml.studiobot.settings.modelProviders.addModelProvider.apikey.title": "API 키:",
  "sml.studiobot.settings.modelProviders.modelinfo.models.title": "사용 가능한 모델",
  "sml.studiobot.settings.modelProviders.modelinfo.models.refresh.button": "새로고침",
  "sml.studiobot.settings.modelProviders.modelinfo.models.refresh.progressTitle": "사용 가능한 모델을 가져오는 중",
  "sml.studiobot.settings.modelProviders.modelinfo.models.refresh.error.title": "모델 새로고침 실패",
  "sml.studiobot.settings.modelProviders.modelinfo.models.refresh.error.message": "나중에 다시 시도해 주세요.",
  "sml.studiobot.settings.modelProviders.modelinfo.models.lastUpdated": "마지막 업데이트: {0}",
  "sml.studiobot.settings.modelProviders.modelinfo.models.name": "이름",        
  "sml.studiobot.settings.modelProviders.modelinfo.models.enabled": "사용",  
  "sml.studiobot.settings.modelProviders.aistudio.info": "<head></head><p>결제를 사용 설정하고 Gemini API의 유료 등급을 사용하면 더 높은 비율 제한의 이점을 누릴 수 있으며, 프롬프트와 응답이 Google 제품을 개선하는 데 사용되지 않습니다.</p>",
  "sml.studiobot.settings.modelProviders.aistudio.info.link": "자세히 알아보기",     
  "sml.studiobot.settings.modelProviders.removemodelprovider.title": "모델 제공업체를 삭제하시겠습니까?",
  "sml.studiobot.settings.modelProviders.removemodelprovider.description": "선택한 모델 제공업체를 삭제하시겠습니까?",
  "sml.studiobot.settings.modelProviders.removemodelprovider.ok": "확인",
  "sml.studiobot.settings.modelProviders.removemodelprovider.cancel": "취소", 
  "sml.studiobot.settings.modelProviders.error.empty.name": "제공업체 이름은 비워둘 수 없습니다.",
  "sml.studiobot.settings.modelProviders.error.duplicate.name": "제공업체 이름은 고유해야 합니다.",
  "sml.studiobot.render.toolcall.status.inprogress": "렌더링 진행 중...",   
  "sml.studiobot.render.toolcall.status.fail": "렌더링 실패.",
  "sml.studiobot.render.toolcall.status.success": "렌더링 완료!",
  "sml.studiobot.render.toolcall.expand.description": "렌더링 도구 호출 응답 표시",
  "sml.studiobot.render.toolcall.header.text": "렌더링 {0}",
  "sml.studiobot.error.no.model.selected.title.text": "모델이 선택되지 않았습니다.",     
  "sml.studiobot.error.no.model.selected.message.text": "목록에서 모델을 선택해 주세요.",
  "sml.studiobot.settings.modelProviders.modelinfo.models.releaseDate.title": "출시일"
}

with open("missing_translations/missing_keys_korean.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for file_info in data.get("new_files", []):
    if file_info.get("filename") == "SmlBundle.properties":
        file_info["keys"].update(translations)
        break

with open("missing_translations/missing_keys_korean.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)
