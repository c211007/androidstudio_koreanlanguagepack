import json
from pathlib import Path

def update_missing_keys():
    file_path = Path("missing_translations/missing_keys_korean.json")

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    ko_dict = {
        "enable.dialog.error.no.provider": "설정 제공자 {0}을(를) 사용할 수 없습니다.",
        "enable.dialog.error.cant.check": "설정 제공자 {0}을(를) 초기화할 수 없습니다.",
        "disable.dialog.title": "백업 및 동기화 비활성화 확인",
        "disable.dialog.text": "이렇게 하면 현재 설치의 백업 및 동기화가 비활성화되며,<br>{0} 계정에 저장된 데이터는 그대로 유지됩니다.<br>이 변경 사항은 즉시 적용됩니다.",
        "disable.dialog.remove.data.box": "{0} 계정에서 데이터를 제거하고 모든 IDE에 대해 비활성화합니다.",
        "disable.dialog.disable.button": "비활성화",
        "disable.active.sync.title": "활성 동기화 비활성화 확인",
        "disable.active.sync.message": "활성 계정을 변경하기 전에 기존 동기화를 비활성화해야 합니다. 현재 활성화된 동기화를 비활성화하시겠습니까?",
        "disable.remove.data.title": "서버 데이터 제거 중...",
        "disable.remove.data.failure": "<icon src='AllIcons.General.Error'>\\\\&nbsp;서버에서 데이터를 제거하지 못했습니다: {0}. 백업 및 동기화가 로컬에서 비활성화되었지만 여전히 서버에 데이터가 있을 수 있습니다. 나중에 다시 시도하거나 지원팀에 문의하세요.",
        "status.action.settings.sync": "백업 및 동기화...",
        "status.action.settings.sync.is.off": "꺼짐",
        "status.action.settings.sync.is.on": "켜짐",
        "status.action.settings.sync.failed": "실패",
        "status.action.settings.sync.pending.action": "작업 필요",
        "logout.link.text": "{0} 계정 로그아웃...",
        "plugins.bundled": "번들 플러그인",
        "subcategory.config.link": "구성",
        "settings.jba.plugin.required.text": "플러그인 페이지에서 JetBrains \"백업 및 동기화\" 플러그인을 다운로드하세요.",
        "settings.jba.plugin.required.title": "플러그인 다운로드 필요",
        "settings.jba.plugin.download": "플러그인 다운로드 중",
        "settings.category.ui.editor.font": "편집기 글꼴",
        "settings.sync.info.message": "UI, 코드 및 시스템 설정, 키맵, 플러그인 및 도구를 동기화합니다.",
        "settings.sync.select.provider.message": "백업 및 동기화를 활성화하려면 설정 데이터를 저장하고 처리할 제공자를 선택하세요.",
        "settings.sync.select.provider.or": "또는",
        "sync.restart.notification.title": "설정 동기화 후 다시 시작해야 함",
        "sync.notification.restart.message.plugin.install": "플러그인 {0,choice,1#개|2#개}를 설치하려면 IDE를 다시 시작하세요: {1}{0,choice,3#...}",
        "sync.notification.restart.message.plugin.enable": "플러그인 {0,choice,1#개|2#개}를 활성화하려면 IDE를 다시 시작하세요: {1}{0,choice,3#...}",
        "sync.notification.restart.message.plugin.disable": "플러그인 {0,choice,1#개|2#개}를 비활성화하려면 IDE를 다시 시작하세요: {1}{0,choice,3#...}",
        "sync.notification.restart.message.list.title": "다음 작업을 완료하려면 IDE를 다시 시작하세요:",
        "sync.notification.restart.message.list.entry.plugin.install": "플러그인 설치 {0,choice,1#개|2#개}: {1}{0,choice,3#...}",
        "sync.notification.restart.message.list.entry.plugin.enable": "플러그인 활성화 {0,choice,1#개|2#개}: {1}{0,choice,3#...}",
        "sync.notification.restart.message.list.entry.plugin.disable": "플러그인 비활성화 {0,choice,1#개|2#개}: {1}{0,choice,3#...}",
        "sync.restart.notification.submessage.plugins": "{0}개 플러그인: {1}...",
        "sync.restart.notification.action": "{0} 다시 시작",
        "sync.status.enabled": "백업 및 동기화가 활성화되었습니다.",
        "sync.status.will.enable": "<icon src='AllIcons.General.History'>\\\\&nbsp;보류 중, \"{0}\"을(를) 클릭하여 동기화를 시작하세요.",
        "sync.status.disabled": "백업 및 동기화가 비활성화되었습니다.",
        "sync.status.will.disable": "백업 및 동기화가 비활성화됩니다.",
        "sync.status.action.required": "작업이 필요합니다: {0}",
        "sync.status.action.required.comment": "보류 중, \"{0}\"을(를) 클릭하여 {1}을(를) 하세요.",
        "sync.status.failed": "동기화 실패: {0}",
        "sync.status.login.message": "백업 및 동기화를 활성화하려면 로그인하세요.",
        "sync.status.last.sync.message": "<icon src='AllIcons.General.GreenCheckmark'>\\\\&nbsp;{0}에 동기화됨",
        "sync.login.message": "로그인 중...",
        "sync.status.login.not.available": "백업 및 동기화를 활성화하려면 설치하세요.",
        "sync.status.restart.required": "백업 및 동기화를 활성화하려면 {0}을(를) 다시 시작하세요.",
        "sync.status.restart.ide.button": "다시 시작",
        "sync.notification.git.state.restore.failed.title": "설정 상태를 복원하지 못했습니다.",
        "sync.notification.git.state.restore.failed.text": "IDE에 몇 가지 문제가 있을 수 있습니다. <a href=\"https://youtrack.jetbrains.com/IDEA/\">YouTrack</a>에 문의하고 분석을 위해 <a href=\"https://intellij-support.jetbrains.com/hc/en-us/articles/9102205110546\">로그 및 설정</a>을 첨부해 주세요."
    }

    filename = "SettingsSyncBundle.properties"
    found = False
    for file_entry in data.get('new_files', []):
        if file_entry['filename'] == filename:
            file_entry['keys'].update(ko_dict)
            found = True
            break
    if not found:
        data.setdefault('new_files', []).append({"filename": filename, "keys": ko_dict})

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"Updated {filename}")

if __name__ == "__main__":
    update_missing_keys()
