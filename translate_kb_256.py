import json

translations = {
  "quick.merge.variants.merge.all.explanation": "병합되지 않은 모든 리비전이 병합됩니다.\\n\n  Subversion은 로컬 사본에 기록된 svn:mergeinfo 속성을 사용하여 병합되지 않은 리비전을 찾습니다.",
  "quick.merge.variants.quick.select": "빠른 수동 선택",
  "quick.merge.variants.quick.select.explanation": "병합된 리비전과 병합되지 않은 리비전을 포함하여 대상 분기의 모든 리비전을 표시합니다.\\n\n  수동으로 선택하기 위해 사용됩니다. 속도가 매우 빠릅니다.",    
  "quick.merge.variants.pre.select": "사전 필터로 선택",
  "quick.merge.variants.pre.select.explanation": "관련 분기 중 하나가 다른 분기에서 복사된 위치를 찾습니다.\\n\n  아직 병합되지 않은 리비전만 선택하도록 로드합니다. 실행 시간이 오래 걸릴 수 있습니다.",
  "progress.title.merging.all.from.branch": "{0}에서 모두 병합 중",
  "progress.title.merging.all.from.branch.reintegrate": "{0}에서 모두 병합 중(재통합)",
  "progress.title.shelving.local.changes.before.merge": "병합 전 로컬 변경 사항 선반에 넣는 중",
  "progress.title.checking.repository.capabilities": "저장소 기능 확인 중",
  "progress.title.loading.recent.branch.revisions": "최근 {0} 리비전 로드 중",
  "progress.title.looking.for.branch.origin": "분기 출처 찾는 중",      
  "progress.title.filtering.branch.revisions": "{0} 리비전 필터링 중",       
  "progress.title.calculating.copy.revision": "복사 리비전 계산 중",      
  "progress.text.collecting.merge.information": "병합 정보 수집 중", 
  "progress.text.collecting.not.merged.revisions": "병합되지 않은 리비전 수집 중",
  "progress.details.merging.changelist.range": "변경 목록 {0} 병합 중",     
  "error.could.not.parse.merge.info": "{0}을(를) 파싱할 수 없습니다.",
  "action.Subversion.SelectAllRevisions.text": "모두 선택",
  "action.Subversion.SelectAllRevisions.description": "모두 선택",
  "action.Subversion.UnselectAllRevisions.text": "모두 선택 취소",
  "action.Subversion.UnselectAllRevisions.description": "모두 선택 취소",
  "button.merge.selected": "선택 항목 병합",
  "button.merge.all": "모두 병합",
  "dialog.title.select.merge.variant": "병합 변형(Variant) 선택",
  "dialog.message.merge.with.switched.paths.in.working.copy": "작업 사본에 전환된 경로가 있습니다. 계속하시겠습니까?",
  "dialog.message.merge.confirm.reintegrate": "변경 사항을 재통합하려고 합니다.<br><br>\n 그러면 ''{0}'' 분기를 <b>더 이상 향후 작업에 사용할 수 없게 됩니다</b>.<br>\n 새 트렁크({1})의 변경 사항을 올바르게 흡수할 수 없으며,<br>\n 이 분기를 트렁크에 다시 제대로 재통합할 수도 없습니다.<br><br>\n 계속하시겠습니까?",
  "dialog.message.merge.intersects.with.local.changes.prompt": "병합 변경 사항과 교차하는 로컬 변경 사항이 있습니다.\\n\n 계속하시겠습니까?",
  "dialog.message.merge.potentially.intersects.with.local.changes.prompt": "병합 변경 사항과 교차할 가능성이 있는 로컬 변경 사항이 있습니다.\\n\n 계속하시겠습니까?",
  "tab.title.merge.local.changes.intersection": "{0}, 로컬 변경 사항 교차",
  "label.merge.local.changes.intersection": "다음 파일에 병합 변경 사항과 교차하는 로컬 변경 사항이 있습니다.",
  "notification.content.merge.start.was.not.found": "병합 시작 지점을 찾을 수 없습니다.", 
  "notification.content.can.not.merge.from.self": "자신에게서 병합할 수 없습니다.",     
  "notification.content.everything.is.up.to.date": "모든 항목이 최신 상태입니다.",  
  "operation.merge": "병합",
  "button.load.quantity": "+{0}개 로드",
  "label.already.merged": "이미 병합됨",
  "dialog.title.merge.from.branch": "{0}에서 병합",
  "label.merge.all.from.branch": "{0}에서 모두 병합",
  "label.merge.all.from.branch.reintegrate": "{0}에서 모두 병합(재통합)",
  "label.merge.all.from.branch.at.revision": "{1}의 {0}에서 모두 병합",       
  "label.merge.all.from.branch.at.revision.reintegrate": "{1}의 {0}에서 모두 병합(재통합)",
  "label.skipped.changelists": "건너뛴 변경 목록: {0}",
  "label.changelists.merging.faced.problems": "다음 변경 목록 병합 중 문제가 발생했습니다.\\n\n  {0}",
  "label.merged.from.branch": "{0}에서 병합됨",
  "merge.chunk.changelist.description": "{0} [리비전 {1}에서]",
  "progress.title.getting.base.and.theirs.revisions.content": "기본 리비전 및 다른 수정본 리비전 콘텐츠 가져오는 중",
  "progress.title.creating.patch.for.theirs.changes": "다른 수정본의 변경 사항에 대한 패치 생성 중",
  "progress.title.accepting.working.state": "작업 상태 수락 중",
  "progress.title.adding.file.to.subversion": "Subversion에 {0} 추가 중",       
  "progress.title.applying.binary.changes": "바이너리 변경 사항 적용 중"
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
