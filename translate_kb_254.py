import json

translations = {
  "label.working.copy.url": "URL:",
  "label.working.copy.format": "형식:",
  "link.change.format": "변경",
  "label.working.copy.depth": "깊이:",
  "link.fix.depth": "수정",
  "label.working.copy.root": "작업 사본 루트",
  "label.nested.copy.type.external": "외부",
  "label.nested.copy.type.switched": "전환됨",
  "label.nested.copy.type.inner": "중첩됨",
  "dialog.title.convert.working.copy.format": "작업 사본 형식 변환",    
  "progress.title.convert.working.copy.format": "작업 사본 형식 변환 중",  
  "progress.text.converting.working.copy.format": "{0} 형식의 작업 사본을 {1}에서 {2}(으)로 변환 중",
  "progress.details.upgraded.path": "{0} 경로 업그레이드됨",
  "dialog.message.invalid.working.copy.root": "잘못된 작업 사본 루트: {0}", 
  "dialog.title.can.not.invoke.action": "{0}을(를) 호출할 수 없음",
  "dialog.title.set.working.copy.infinity.depth": "작업 사본 무한 깊이 설정",
  "dialog.message.set.working.copy.infinity.depth": "''infinity'' 깊이로 ''{0}''에 체크아웃하려고 합니다.\\n\n  그러면 작업 사본도 HEAD 리비전으로 업데이트됩니다.",
  "action.name.configure.branches": "분기 구성",
  "action.name.merge.from": "다음에서 병합",
  "action.name.merge.from.ellipsis": "다음에서 병합…",
  "notification.content.can.not.access.working.copy.database": "svn 작업 사본 데이터베이스에 액세스하는 동안 몇 가지 오류가 발생했습니다.",
  "notification.content.single.root.unsupported.format": "''{0}'' 루트가 지원되지 않는 Subversion 형식일 수 있습니다.",
  "notification.content.multiple.roots.unsupported.format": "일부 루트가 지원되지 않는 Subversion 형식일 수 있습니다.",
  "committed.changes.action.enable.merge.highlighting": "통합 항목 강조 표시", 
  "committed.changes.action.enable.merge.highlighting.description.text": "이 옵션은 1.5 버전을 사용하는 SVN 저장소 및 작업 사본에서만 사용할 수 있습니다.",   
  "committed.changes.action.merge.highlighting.refresh.text": "새로고침",        
  "committed.changes.action.merge.highlighting.refresh.description": "병합된 리비전 정보 새로고침",
  "dialog.Subversion.select.working.copy.title": "작업 사본 경로 구성",
  "dialog.Subversion.select.working.copy.wcopy.list.title": "알려진 작업 사본",
  "action.Subversion.cleanup.progress.title": "Subversion 정리",
  "progress.text.performing.path.cleanup": "''{0}'' 정리 수행 중…", 
  "progress.title.cleanup.project": "프로젝트 정리",
  "action.Subversion.cleanup.error.message": "''{0}'' 정리를 수행하는 중 오류 발생: {1}",
  "action.Subversion.integrate.difference.option.use.ancestry.text": "조상 사용(&U)",
  "use.idea.proxy.as.default": "Subversion의 기본값으로 {0} 일반 프록시 설정 사용",
  "use.idea.proxy.as.default.label.text": "HTTP 프록시만 기본값으로 사용할 수 있습니다.",
  "navigate.to.idea.proxy.settings": "일반 프록시 설정으로 이동",      
  "dialog.message.switch.target.not.copy.current": "전환 대상 URL이 현재 항목의 사본이 아닙니다.\\n\n  계속하시겠습니까?",
  "dialog.title.switch.target.problem": "대상 전환 문제",
  "tab.repository.merge.panel.filter.plus": "통합된 항목 필터링",
  "tab.repository.merge.panel.filter.minus": "통합되지 않은 항목 필터링",       
  "tab.repository.merge.panel.filter.others": "기타 필터링",
  "browse.changes.settings.stop.on.copy": "복사 중지(&S)",
  "action.mark.list.as.merged.text": "병합됨으로 표시",
  "action.mark.list.as.merged.description": "선택한 리비전을 병합됨으로 표시하되, 실제로 병합하지는 않습니다.",
  "action.mark.list.as.not.merged.text": "병합되지 않음으로 표시",
  "action.mark.list.as.not.merged.description": "선택한 리비전을 병합되지 않음으로 표시하되, svn:mergeinfo 이외의 것은 변경하지 않습니다.",
  "label.depth.text": "깊이(&D):",
  "label.depth.description": "기존 \"재귀(recursive)\" 옵션을 대체합니다. \"재귀\"=false는 \"직접(immediates)\"와 동일하고, \"재귀\"=true는 \"무한(infinity)\"과 동일합니다.",
  "label.working.copy": "작업 사본"
}

with open("missing_translations/missing_keys_korean.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for file_info in data.get("new_files", []):
    if file_info.get("filename") == "SvnBundle.properties":
        keys_dict = file_info.get("keys", file_info.get("properties", {}))
        keys_dict.update(translations)
        file_info["keys"] = keys_dict
        break

with open("missing_translations/missing_keys_korean.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)
