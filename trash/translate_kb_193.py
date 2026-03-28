import json
from pathlib import Path

def update_missing_keys():
    file_path = Path("missing_translations/missing_keys_korean.json")

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    ko_dict = {
        "action.settingsSync.manualPush.text": "설정 푸시",
        "action.settingsSync.history.text": "백업 및 동기화 내역",
        "settingsSync.errors.notificationGroup": "백업 및 동기화 메시지",
        "notification.title.push.error": "설정을 동기화할 수 없습니다.",
        "notification.title.update.error": "서버에서 설정을 가져올 수 없습니다.",
        "notification.title.update.no.such.file": "서버에 설정 파일이 없습니다.",
        "progress.title.updating.settings.from.server": "서버에서 설정 업데이트 중...",
        "notification.title.apply.error": "설정을 적용할 수 없습니다.",
        "action.SettingsSyncStatusAction.text": "백업 및 동기화",
        "action.SettingsSyncOpenSettingsAction.text": "백업 및 동기화...",
        "title.settings.sync": "백업 및 동기화",
        "configurable.what.to.sync.label": "동기화할 항목 구성:",
        "settings.category.ui.name": "UI 설정",
        "settings.category.comment.ui.code.system.name": "\\u2022 UI, 코드 및 시스템 설정",
        "settings.category.ui.description": "테마, 편집기 글꼴, 도구 모음 및 알림 포함",
        "settings.category.keymap.name": "키맵",
        "settings.category.comment.keymap": "\\u2022 키맵",
        "settings.category.keymap.description": "",
        "settings.category.code.name": "코드 설정",
        "settings.category.code.description": "코드 스타일, 파일 유형 및 라이브 템플릿 포함",
        "settings.category.plugins.name": "플러그인",
        "settings.category.comment.plugins": "\\u2022 플러그인",
        "settings.category.plugins.description": "",
        "settings.category.tools.name": "도구",
        "settings.category.comment.tools": "\\u2022 도구",
        "settings.category.tools.description": "버전 관리 및 디버거 포함",
        "settings.category.system.name": "시스템 설정",
        "settings.category.system.description": "",
        "config.button.login": "JetBrains 계정으로 로그인...",
        "config.button.enable": "백업 및 동기화 활성화:",
        "enable.dialog.select.what.to.sync": "동기화할 설정",
        "enable.dialog.enable.sync.action": "백업 및 동기화 활성화",
        "enable.dialog.source.option.title": "설정 소스 선택",
        "enable.dialog.source.option.text": "이 계정에는 이미 기존 설정이 있습니다. 앞으로 동기화의 기준으로 사용할 설정을 선택하세요.",
        "enable.dialog.sync.local.settings": "계정으로 설정 푸시",
        "enable.dialog.sync.local.settings.option": "로컬 설정을 사용하고 계정 저장소에 업로드합니다.",
        "enable.dialog.sync.local.settings.text": "계정에 저장된 설정을 로컬 설정으로 덮어씁니다.",
        "enable.dialog.get.settings.from.account": "계정에서 설정 가져오기",
        "enable.dialog.get.settings.from.account.option": "계정 저장소의 설정을 사용합니다.",
        "enable.dialog.get.settings.from.account.text": "로컬 설정을 계정에 있는 설정으로 덮어씁니다.",
        "enable.dialog.change": "변경",
        "enable.sync.check.server.data.progress": "서버 데이터 확인 중...",
        "enable.sync.get.from.server.progress": "서버에서 설정 가져오는 중...",
        "enable.sync.push.to.server.progress": "서버로 설정 푸시하는 중...",
        "enable.sync.add.account": "계정 추가...",
        "enable.sync.choose.data.provider.title": "상태 제공자 선택",
        "enable.sync.provider.already.logged.in": "이미 {0} 계정으로 로그인되어 있습니다.",
        "enable.sync.choose.data.provider.login.button": "로그인...",
        "enable.sync.choose.data.provider.text": "데이터를 저장하고 처리할 상태 제공자를 선택하세요.",
        "enable.dialog.error.no.user": "사용 가능한 사용자가 없습니다."
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
