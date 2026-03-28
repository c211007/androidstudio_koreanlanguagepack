import json

ko_dict = {
  "project.structure.name": "이름:",
  "project.structure.sdk": "SDK:",
  "project.structure.compiler.output.comment": "해당 소스에 대한 프로덕션 및 테스트의 모듈 하위 디렉터리에 사용됩니다.",
  "project.structure.compiler.output": "컴파일러 출력:",
  "label.select.project.type.to.configure": "구성할 프로젝트 유형 선택",
  "language.level.combo.supported.versions": "지원되는 버전",
  "language.level.combo.experimental.versions": "실험적 버전",
  "language.level.combo.unsupported.versions": "지원되지 않는 버전",
  "project.or.module.jdk.misconfigured": "{0, choice, 0#프로젝트|1#모듈} JDK가 잘못 구성됨",
  "notification.group.build.script.found": "빌드 스크립트를 찾음",
  "label.bind.remote.repository": "원격 리포지토리 바인딩(&B)",
  "repository.library.utils.library.update.title": "Maven 라이브러리 업데이트",
  "repository.library.utils.notification.content.nothing.to.update": "업데이트할 항목이 없습니다.",
  "repository.library.utils.notification.action.open.project.structure": "프로젝트 구조 대화상자 열기",
  "repository.library.utils.notification.content.libraries.resolve.fail": "라이브러리를 확인할 수 없습니다:<code>{0}</code><br/>{1, choice, 0#|1#및 1개 더. |2#및 {1}개 더. }프로젝트 구조 설정에서 원격 리포지토리 바인딩을 확인하세요.",
  "repository.library.utils.notification.content.libraries.resolve.success": "{0, choice, 0#확인할 항목 없음|1#1개 라이브러리 확인됨|2#{0}개 라이브러리 확인됨}",
  "repository.library.utils.notification.content.libraries.resolve.fail.before.update": "업데이트가 취소되었습니다. 라이브러리를 확인할 수 없습니다. 다음에 대한 라이브러리 바인딩 리포지토리 설정을 확인하세요:<code>{0}</code>",
  "repository.library.utils.notification.content.library.properties.built": "{0, choice, 0#업데이트된 라이브러리 없음.|1#1개의 라이브러리가 성공적으로 업데이트되었습니다: 확장 속성이 빌드되었습니다.|2#{0}개의 라이브러리가 성공적으로 업데이트되었습니다: 확장 속성이 빌드되었습니다.}",
  "repository.library.utils.notification.content.library.bind.repo.guess.failed": "다음에 대한 원격 리포지토리를 추측하지 못했습니다: <code>{0}</code><br/>{1, choice, 0#|1#및 1개 더. |2#및 {1}개 더. }프로젝트 구조 설정에서 원격 리포지토리를 수동으로 선택하세요.",
  "repository.library.utils.notification.content.library.properties.cleared": "{0, choice, 0#업데이트 없음|1#1개의 라이브러리 업데이트됨: 확장 속성이 지워졌습니다.|2#{0}개의 라이브러리 업데이트됨: 확장 속성이 지워졌습니다.}",
  "repository.library.utils.progress.title.building.sha256sum": "Maven 라이브러리 SHA256 체크섬 빌드",
  "repository.library.utils.progress.title.removing.sha256sum": "Maven 라이브러리 SHA256 체크섬 제거",
  "repository.library.utils.progress.title.binding.remote.repos": "Maven 라이브러리 원격 리포지토리 바인딩",
  "repository.library.utils.progress.title.unbinding.remote.repos": "Maven 라이브러리 원격 리포지토리 바인딩 해제",
  "repository.library.utils.progress.title.resolving.all.libraries": "모든 Maven 라이브러리를 확인하는 중",
  "repository.library.utils.progress.title.libraries.changed": "Maven 라이브러리 업데이트",
  "repository.library.utils.progress.text.resolving.before.update": "업데이트 전에 라이브러리 확인하는 중",
  "repository.library.utils.progress.text.computing.properties": "라이브러리의 확장된 속성 계산하는 중",
  "repository.library.utils.progress.text.saving.changes": "라이브러리 변경 사항 저장하는 중",
  "repository.library.utils.progress.text.verifying.resolution.after.update": "업데이트 후 라이브러리 확인 중",
  "repository.library.utils.progress.details.complete.for": "{1}개 중 {0}개 완료",
  "repository.library.utils.progress.checking.resolution": "업데이트된 라이브러리를 확인할 수 있는지 검사 중{1, choice, 0#|1#…}",
  "precompile.library.resolution.start": "{0} Maven 라이브러리 확인하는 중",
  "precompile.library.resolution.failure": "Maven 라이브러리 확인 실패 {0}: {1}",
  "group.JarRepositoryLibraries.text": "JAR 리포지토리 라이브러리(&J)",
  "action.EnableAllRepositoryLibrariesSha256Checksum.text": "모든 라이브러리에 대해 SHA256 체크섬 활성화",
  "action.DisableRepositoryLibrariesSha256Checksum.text": "모든 라이브러리에 대해 SHA256 체크섬 비활성화",
  "action.UnbindRemoteRepositoryForAllRepositoryLibraries.text": "모든 라이브러리에 대해 원격 리포지토리 바인딩 해제",
  "action.GuessRemoteRepositoryForEachRepositoryLibrary.text": "모든 라이브러리에 대해 원격 리포지토리 추측 및 바인딩",
  "action.ResolveAllRepositoryLibraries.text": "모든 Maven 라이브러리 확인"
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
