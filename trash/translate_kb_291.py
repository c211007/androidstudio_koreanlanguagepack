import json

translations = {
  "action.name.integrate.scope": "{0} 통합(&G)",
  "action.display.name.integrate.scope": "{0} 통합",
  "update.files.scope.name": "파일",
  "update.directory.scope.name": "디렉터리",
  "update.file.scope.name": "파일",
  "update.directories.scope.name": "디렉터리",
  "update.project.scope.name": "프로젝트",
  "dialog.title.changes.browser": "변경 사항 브라우저",
  "code.smells.error.messages.tab.name": "코드 분석",
  "commit.checks.error.indexing": "현재 코드 분석을 할 수 없습니다.",
  "commit.checks.error.indexing.message": "{0}이(가) 백그라운드에서 색인을 업데이트하는 동안에는 커밋 검사를 수행할 수 없습니다.\\n\n   검사를 실행하지 않고 변경 사항을 커밋하거나, 색인이 빌드될 때까지 기다릴 수 있습니다.",
  "searching.for.code.smells.processing.file.progress.text": "{0} 처리 중",
  "searching.for.code.smells.freezing.process": "체크인 전 코드 분석",
  "checking.code.smells.progress.title": "코드 분석 수행 중",
  "before.commit.files.contain.code.smells.edit.them.confirm.text": "{0}개의 파일에 문제가 포함되어 있습니다.\\n\n   {1,choice, 0#오류가 없고|1#1개의 오류가 있고|2#{1}개의 오류가 있고} {2,choice, 0#경고가|1#1개의 경고가|2#{2}개의 경고가} 발견되었습니다.\\n\n   검토하시겠습니까?",
  "before.commit.file.contains.code.smells.edit.them.confirm.text": "{0} 파일에 문제가 포함되어 있습니다.\\n\n   {1,choice, 0#오류가 없고|1#1개의 오류가 있고|2#{1}개의 오류가 있고} {2,choice, 0#경고가|1#1개의 경고가|2#{2}개의 경고가} 발견되었습니다.\\n\n   검토하시겠습니까?",
  "code.smells.review.button": "코드 분석 검토(&R)",
  "todo.in.new.review.button": "TODO 검토(&R)",
  "before.checkin.standard.options.check.smells": "코드 분석(&A)",
  "before.checkin.options.check.smells.profile": "''{0}'' 프로필로 코드 분석(&A)",
  "before.checkin.options.check.smells.choose.profile": "프로필 선택",
  "before.checkin.waiting.for.smart.mode": "스마트 모드 대기 중…",
  "before.checkin.new.todo.check": "TODO 확인({0})",
  "before.checkin.new.todo.check.no.filter": "TODO 확인",
  "before.checkin.cleanup.code": "정리(&L)",
  "before.checkin.cleanup.code.profile": "''{0}'' 프로필로 정리(&L)",
  "before.checkin.post.commit.error.dumb.mode": "현재 코드 분석을 할 수 없습니다.",
  "before.checkin.error.unknown": "커밋을 검사할 수 없습니다.",
  "before.checkin.error.internal": "커밋을 검사할 수 없습니다: 내부 오류",
  "before.checkin.error.in.plugin": "커밋을 검사할 수 없습니다: ''{0}'' 플러그인 오류",
  "before.commit.run.configuration.failed": "''{0}''이(가) 종료 코드 {1}(으)로 실패했습니다.",
  "before.commit.run.configuration.tests.failed": "''{0}'' - {1}",
  "before.commit.run.configuration.failed.to.start": "''{0}''을(를) 시작하지 못했습니다.",
  "before.commit.run.configuration.failed.edit.configuration": "실행 구성 편집",
  "before.commit.run.configuration.no.configuration.selected.checkbox": "실행 구성",
  "changes.nodetitle.unversioned.files": "버전 관리되지 않는 파일",
  "changes.nodetitle.locally.deleted.files": "로컬에서 삭제된 파일",
  "changes.nodetitle.modified.without.editing": "체크아웃 없이 수정됨",
  "changes.nodetitle.ignored.files": "무시된 파일",
  "changes.nodetitle.locked.folders": "잠긴 작업 복사본 폴더",
  "changes.nodetitle.locked.folders.tooltip": "일부 폴더가 잠겨 있어 VCS 작업이 허용되지 않습니다. 정리를 수행해야 합니다.",
  "changes.nodetitle.logicallt.locked.folders": "명시적으로 잠긴 파일",
  "changes.nodetitle.switched.files": "전환된 파일",
  "changes.nodetitle.switched.roots": "루트 전환",
  "changes.nodetitle.filter.pending": "필터링되지 않음",
  "changes.nodetitle.filtered.out": "필터링에서 제외됨",
  "changes.nodetitle.updating": "업데이트 중…",
  "changes.nodetitle.untracked.updating.delayed": "파일 스캔 중에는 버전 관리되지 않는 파일을 사용할 수 없습니다.",
  "changes.nodetitle.have.outdated.files": "일부 파일이 서버에서 변경되었습니다.",
  "changes.nodetitle.empty.changelist.name": "<이름 없음>"
}

with open("missing_translations/missing_keys_korean.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for file_info in data.get("new_files", []):
    if file_info.get("filename") == "VcsBundle.properties":
        keys_dict = file_info.get("keys", file_info.get("properties", {}))
        keys_dict.update(translations)
        file_info["keys"] = keys_dict
        break

with open("missing_translations/missing_keys_korean.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)
