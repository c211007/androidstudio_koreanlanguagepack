import json

translations = {
  "configurable.SvnConfigureProxiesComponent.display.name": "HTTP 프록시 구성",
  "value.new.server.group.name": "이름 없음",
  "settings.use.custom.directory": "사용자 지정 구성 디렉터리 사용(&U):",      
  "settings.check.mergeinfo": "병합을 준비할 때 대상 하위 트리에서 svn:mergeinfo 확인",
  "settings.maximum.revisions.number": "어노테이션에서 되돌아볼 최대 리비전 수:",
  "settings.HTTP.timeout": "HTTP 제한 시간:",
  "settings.seconds": "초",
  "settings.SSH.connection.timeout": "SSH 연결 제한 시간:",
  "settings.SSH.read.timeout": "SSH 읽기 제한 시간:",
  "settings.edit.servers.subversion.runtime.configuration.file": "'servers' Subversion 런타임 구성 파일 편집",
  "settings.ssl.protocols": "SSL 프로토콜:",
  "settings.ssl.protocols.all": "모두",
  "settings.ssl.protocols.sslv3": "SSLv3",
  "settings.ssl.protocols.all.tlsv1": "TLSv1",
  "action.DumbAware.SvnConfigureProxiesComponent.text.add": "추가",
  "action.DumbAware.SvnConfigureProxiesComponent.description.add": "추가",       
  "action.DumbAware.SvnConfigureProxiesComponent.text.copy": "복사",
  "action.DumbAware.SvnConfigureProxiesComponent.description.copy": "복사",     
  "action.DumbAware.RepositoryBrowserDialog.text.branch.or.tag": "분기 또는 태그…",
  "action.DumbAware.RepositoryBrowserDialog.text.move.or.rename": "이동 또는 이름 바꾸기(_M)…",
  "svn.properties.viewer": "SVN 속성 뷰어",
  "svn.tree.conflict.viewer": "SVN 트리 충돌 뷰어",
  "svn.phantom.changes.viewer": "SVN 고스트(phantom) 변경 사항 뷰어",
  "label.svn.phantom.change": "기술 레코드",
  "text.svn.phantom.change": "대상 파일이 삭제되었기 때문에 이 변경 사항이 기록되며,\\n\n  일부 상위 디렉터리가 새 위치로 복사(또는 이동)되었습니다.",
  "dialog.title.svn.properties.diff": "SVN 속성 차이(Diff)",
  "progress.title.loading.change.details": "변경 사항 세부정보 로드 중",
  "progress.title.loading.tree.conflict.details": "트리 충돌 세부정보 로드 중",
  "label.svn.properties.changed": "SVN 속성이 변경되었습니다",
  "separator.property.changes": "속성 변경",
  "error.no.branch.point.found.for.target": "{0}에 대한 분기점을 찾을 수 없습니다.",    
  "error.target.not.found.in.paths": "{1}에서 {0}을(를) 찾을 수 없습니다.",
  "error.file.is.not.under.version.control": "{0} 파일이 버전 관리 중이 아닙니다.",
  "error.file.is.not.under.subversion": "{0} 파일이 Subversion 제어 하에 있지 않습니다.",
  "error.can.not.find.file": "파일을 찾을 수 없음: {0}",
  "error.can.not.find.repository.root.for.url": "URL에 대한 저장소 루트를 찾을 수 없음: {0}",
  "error.can.not.find.repository.root.for.url.in.revision": "리비전 {1}에서 URL의 저장소 루트를 찾을 수 없음: {0}",
  "error.could.not.get.info.for.path": "{0}에 대한 정보를 가져올 수 없습니다.",
  "error.could.not.get.head.info.for.url": "{0}에 대한 HEAD 정보를 가져올 수 없습니다.",   
  "error.could.not.get.revision.for.url": "{0}에 대한 리비전을 가져올 수 없습니다.",     
  "error.properties.loading.for.revision.canceled": "리비전 {0}에 대한 속성 로드가 취소되었습니다.",
  "error.can.not.access.file.base.revision.contents.administrative.area.is.locked": "파일 기본 리비전 콘텐츠에 액세스할 수 없습니다. 관리 영역이 잠겨 있습니다.", 
  "error.url.is.not.absolute": "{0}이(가) 절대 경로가 아닙니다.",
  "error.url.is.not.hierarchical": "{0}이(가) 계층 구조가 아닙니다.",
  "error.url.could.not.contain.query": "{0}에 쿼리를 포함할 수 없습니다.",
  "error.url.could.not.contain.fragment": "{0}에 프래그먼트를 포함할 수 없습니다.",     
  "error.can.not.delete.file": "파일을 삭제할 수 없음: {0}",
  "error.can.not.create.directory": "디렉터리를 생성할 수 없음: {0}",
  "error.could.not.determine.revision.number.for.file.and.revision": "파일 {0} 및 리비전 {1}의 리비전 번호를 결정할 수 없습니다.",
  "error.could.not.find.start.quote": "시작 따옴표를 찾을 수 없습니다."
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
