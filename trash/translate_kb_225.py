import json

translations = {
  "hats.dialog.contact.signup": "예일 경우 여기에서 가입해 주세요.",
  "hats.dialog.satisfaction.very.dissatisfied": "매우 불만족",
  "hats.dialog.satisfaction.somewhat.dissatisfied": "다소 불만족",    
  "hats.dialog.satisfaction.neither": "보통",     
  "hats.dialog.satisfaction.somewhat.satisfied": "다소 만족",
  "hats.dialog.satisfaction.very.satisfied": "매우 만족",
  "hats.dialog.recommend.likely": "적극적으로 추천할 생각임",
  "hats.dialog.recommend.unlikely": "전혀 추천할 생각 없음",
  "hats.dialog.response.character.count.message.remaining": "{0}자 남음",
  "hats.dialog.response.character.count.message.over": "{0}자 초과",   
  "hats.dialog.response.character.count.message.default": "500자 남음",
  "hats.dialog.text.add.comments": "의견 추가",
  "ai.companion.code.generation.action.name": "코드 생성",
  "ai.companion.code.generation.tooltip.name": "Gemini {0}(으)로 코드 생성", 
  "ai.companion.code.generation.error.empty.suggestion.text": "생성된 제안이 없습니다. 컨텍스트를 더 제공해 주세요.",
  "ai.companion.code.generation.error.citation.block.text": "생성된 코드에 차단된 라이선스 콘텐츠가 포함되어 있습니다. 요청을 다른 말로 바꿔 다시 시도해 주세요.",   
  "ai.companion.code.generation.error.diff.block.text": "코드 변경사항을 파싱하지 못해 자동으로 수락할 수 없습니다. 제안된 변경사항을 수동으로 검토하고 적용해 주세요.",
  "ai.companion.code.generation.error.other.text": "제안을 찾을 수 없습니다. 다시 시도해 주세요.",
  "ai.companion.code.generation.progress.message": "제안 생성 중...",  
  "action.sml.studiobot.custom.transform.text": "편집기 내 프롬프트 열기...",     
  "action.sml.studiobot.generate.code.text": "편집기 내 프롬프트 열기...",        
  "ai.companion.code.transform.finishchanges.name": "변경 완료",
  "ai.companion.code.transform.finishchanges.accept.all.text": "모두 수락",    
  "ai.companion.code.transform.finishchanges.accept.all.description": "편집기에서 모든 변경사항 수락",
  "ai.companion.code.transform.finishchanges.reject.all.text": "모두 거부",    
  "ai.companion.code.transform.finishchanges.reject.all.description": "편집기에서 모든 변경사항 거부",
  "sml.studiobot.ask.transform.dialog.title": "Gemini Code Assist 편집기 내 프롬프트",
  "sml.studiobot.ask.transform.dialog.message": "명령어를 사용하려면 /를 입력하거나 Gemini Code Assist와 채팅하세요.",
  "sml.studiobot.ask.generate.dialog.title": "Gemini Code Assist 편집기 내 프롬프트",
  "sml.studiobot.ask.generate.dialog.message": "명령어를 사용하려면 /를 입력하거나 Gemini Code Assist와 채팅하세요.",
  "sml.studiobot.ask.transform.dialog.disclaimer": "Google의 생각과는 다르게 부정확하거나 불쾌감을 주는 정보가 표시될 수 있습니다. 생성된 코드는 주의해서 사용하세요.",
  "aiplugin.error.title.text": "Gemini 응답을 가져오는 중 오류가 발생했습니다.",
  "aiplugin.error.aborted.text": "작업이 중단되었습니다. 예기치 않은 오류인 경우 보고서를 제출해 주세요.",
  "aiplugin.error.already.exists.text": "이미 존재하는 오류가 발생했습니다. 보고서를 제출해 주세요.",
  "aiplugin.error.client.side.rate.limit.text": "시간당 대화 제한을 초과했습니다. 나중에 다시 시도해 주세요.",
  "aiplugin.error.data.loss.text": "예기치 않은 오류가 발생했습니다. 보고서를 제출해 주세요.",
  "aiplugin.error.deadline.exceeded.text": "요청이 할당된 시간을 초과했습니다. 인터넷 연결 상태를 확인해 주세요.",
  "aiplugin.error.failed.precondition.text": "전제 조건 확인에 실패했습니다. 설정이 올바른지 확인해 주세요.",
  "aiplugin.error.internal.text": "Gemini Code Assist를 사용할 수 없습니다. 프록시 설정을 확인하고 다시 시도해 주세요.",
  "aiplugin.error.invalid.argument.text": "잘못된 인수 오류가 발생했습니다. 보고서를 제출해 주세요.",
  "aiplugin.error.network.text": "Gemini Code Assist에 연결할 수 없습니다. 네트워크 설정을 확인해 주세요.",
  "aiplugin.error.not.found.text": "예상한 리소스를 찾을 수 없습니다. 다시 시도하거나 보고서를 제출해 주세요.",
  "aiplugin.error.out.of.range.text": "범위를 벗어나는 오류가 발생했습니다. 보고서를 제출해 주세요.",
  "aiplugin.error.permission.denied.text": "현재 Gemini Code Assist가 사용 설정되지 않았습니다. 구성된 프로젝트 ID가 올바른지, Gemini Google Cloud API가 사용 설정되어 있는지 확인하세요.",
  "aiplugin.error.permission.denied.security.policy.violated.text": "조직의 정책으로 인해 Gemini Code Assist를 사용할 수 없습니다. 관리자에게 문의하여 안내에 따라 VPC 서비스 제어 구성을 업데이트하세요.",        
  "aiplugin.error.permission.denied.ssl.required.text": "이 작업을 수행하려면 SSL이 필요합니다. 설정에서 API 엔드포인트를 확인해 주세요.",
  "aiplugin.error.permission.denied.service.disabled.text": "현재 Gemini Code Assist가 사용 설정되지 않았습니다. 선택한 프로젝트에 Gemini Google Cloud API가 사용 설정되어 있는지 확인하세요.",
  "aiplugin.error.permission.denied.user.lacking.permissions.text": "현재 Gemini Code Assist가 사용 설정되지 않았습니다. 구성된 프로젝트 ID가 올바른지, 필요한 권한이 부여되었는지 확인하세요.",
  "aiplugin.error.permission.denied.project.not.found.or.deleted": "프로젝트를 찾을 수 없습니다. 구성된 프로젝트 ID가 올바른지 확인하거나 다른 프로젝트를 선택하세요.",
  "aiplugin.error.resource.exhausted.text.userDefinedProject": "서버에 리소스 소진 오류가 발생했습니다. 발급된 요청 수가 할당량에 도달했기 때문일 수 있습니다."
}

with open("missing_translations/missing_keys_korean.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for file_info in data.get("new_files", []):
    if file_info.get("filename") == "SmlIjBundle.properties":
        keys_dict = file_info.get("keys", file_info.get("properties", {}))
        keys_dict.update(translations)
        file_info["keys"] = keys_dict
        break

with open("missing_translations/missing_keys_korean.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)
