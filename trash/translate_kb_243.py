import json

translations = {
  "subversion.executable.notification.title": "Subversion 명령줄 클라이언트를 사용할 수 없음",
  "subversion.executable.notification.description": "Subversion 실행 파일의 경로가 잘못된 것 같습니다.",
  "subversion.executable.too.old": "Subversion 명령줄 클라이언트 버전이 너무 오래되었습니다({0}).",
  "subversion.executable.notification.cant.run.in.safe.mode": "안전 모드에서는 Svn 명령을 실행할 수 없습니다.",
  "subversion.roots.detection.errors.found.description": "Subversion 작업 사본을 검색하는 중에 오류를 발견했습니다.",
  "subversion.roots.detection.errors.found.action.text": "해결",
  "action.Subversion.BrowseSVNRepository.text": "Subversion 저장소 찾아보기(_W)\\u2026",
  "action.Subversion.BrowseSVNRepository.description": "Subversion 저장소를 찾습니다.",
  "group.SubversionFilePopupGroup.text": "Subversion(_S)",
  "group.IgnoreChoicesGroup.text": "무시",
  "group.RevertIgnoreChoicesGroup.text": "무시 목록에서 삭제",
  "action.Subversion.UndoIgnore.text": "선택한 파일 이름",
  "action.Subversion.UndoIgnore.description": "폴더 무시 목록에서 파일 이름/마스크를 삭제합니다.",
  "action.Subversion.Ignore.ExactMatch.text": "선택한 파일 이름",
  "action.Subversion.Ignore.ExactMatch.description": "선택한 모든 파일의 이름을 폴더 무시 목록에 추가합니다.",
  "action.Subversion.Ignore.MatchExtension.description": "{0} 마스크를 폴더 무시 목록에 추가합니다.",
  "action.Subversion.SetProperty.text": "속성 설정(_T)\\u2026",
  "action.Subversion.SetProperty.description": "파일 또는 디렉터리에 버전이 지정된 속성을 설정합니다.",
  "action.Subversion.ShowProperties.text": "속성 편집(_P)",
  "action.name.show.properties": "속성 표시",
  "action.Subversion.PropertiesView.AddProperty.text": "속성 추가",
  "action.Subversion.PropertiesView.AddProperty.description": "새 속성을 추가합니다.",
  "action.Subversion.PropertiesView.EditProperty.text": "속성 편집",        
  "action.Subversion.PropertiesView.EditProperty.description": "선택한 속성 값을 편집합니다.",
  "action.Subversion.PropertiesView.EditKeywords.text": "키워드 편집",        
  "action.Subversion.PropertiesView.EditKeywords.description": "svn:keywords 속성을 관리합니다.",
  "action.Subversion.PropertiesView.DeleteProperty.text": "속성 삭제",    
  "action.Subversion.PropertiesView.DeleteProperty.description": "선택한 속성을 삭제합니다.",
  "action.Subversion.PropertiesView.FollowSelection.text": "선택 항목 따르기",  
  "action.Subversion.PropertiesView.FollowSelection.description": "선택 항목을 따릅니다.",
  "action.Subversion.PropertiesView.Refresh.text": "새로고침",
  "action.Subversion.PropertiesView.Refresh.description": "속성을 다시 로드합니다.",  
  "action.Subversion.PropertiesView.Close.text": "닫기",
  "action.Subversion.PropertiesView.Close.description": "이 도구 창을 닫습니다.",
  "toolwindow.stripe.SVN_Properties": "SVN 속성",
  "column.name.property.name": "이름",
  "column.name.property.value": "값",
  "error.can.not.set.property": "속성을 설정할 수 없음: {0}",
  "dialog.title.svn.keywords": "SVN 키워드",
  "label.select.keywords.to.set": "설정할 키워드 선택: ",
  "action.Subversion.Resolve.text": "텍스트 충돌 해결(_S)\\u2026",
  "action.Subversion.Resolve.description": "파일에 대한 텍스트 충돌을 해결합니다.",     
  "action.Subversion.MarkResolved.text": "해결됨으로 표시(_M)\\u2026",
  "action.Subversion.MarkResolved.description": "텍스트 및 속성 충돌을 해결됨으로 표시합니다.",
  "action.Subversion.Clenaup.text": "정리(_E)",
  "action.Subversion.Clenaup.description": "잠긴 디렉터리를 잠금 해제하고 완료되지 않은 나머지 작업을 모두 실행합니다.",
  "action.Subversion.Copy.text": "브랜치 또는 태그(_B)\\u2026",
  "action.Subversion.Copy.description": "선택한 파일 또는 디렉터리를 새 저장소 위치로 복사합니다.",
  "action.Subversion.Lock.text": "잠금(_L)\\u2026",
  "action.Subversion.Lock.description": "파일 잠금"
}

with open("missing_translations/missing_keys_korean.json", "r", encoding="utf-8") as f:
    data = json.load(f)

found = False
for file_info in data.get("new_files", []):
    if file_info.get("filename") == "SvnBundle.properties":
        keys_dict = file_info.get("keys", file_info.get("properties", {}))
        keys_dict.update(translations)
        file_info["keys"] = keys_dict
        found = True
        break

if not found:
    data.setdefault("new_files", []).append({
        "filename": "SvnBundle.properties",
        "keys": translations
    })

with open("missing_translations/missing_keys_korean.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)
