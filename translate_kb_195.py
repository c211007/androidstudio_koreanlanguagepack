import json
from pathlib import Path

def update_missing_keys():
    file_path = Path("missing_translations/missing_keys_korean.json")

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    ko_dict = {
        "sync.notification.size.exceed.title": "설정 아카이브의 크기가 제한을 초과했습니다.",
        "sync.notification.size.exceed.text": "IDE 또는 설치된 플러그인에 문제가 있을 수 있습니다. <a href=\"https://youtrack.jetbrains.com/IDEA/\">YouTrack</a>에 문의하고 분석을 위해 <a href=\"https://intellij-support.jetbrains.com/hc/en-us/articles/9102205110546\">로그 및 설정</a>을 첨부해 주세요.",
        "sync.notification.do.not.ask.again": "다시 묻지 않음",
        "settings.cross.product.sync": "다음에서 설정 동기화:",
        "settings.cross.product.sync.choice.only.this.product": "{0} 인스턴스 전용",
        "settings.cross.product.sync.choice.all.products": "JetBrains IDE 제품 및 Android 스튜디오",
        "settings.cross.product.sync.choice.all.products.android": "Android 스튜디오 및 JetBrains IDE 제품",
        "settings.warning.sync.cannot.be.enabled.label": "Settings Repository가 구성된 경우 백업 및 동기화를 활성화할 수 없습니다.",
        "installing.plugins.indicator": "백업 및 동기화에서 플러그인 설치 중",
        "history.dialog.title": "백업 및 동기화 내역",
        "history.error.message": "백업 및 동기화 저장소를 찾을 수 없습니다.",
        "history.tab.name": "내역",
        "toolwindow.stripe.Settings_Sync_History": "백업 및 동기화 내역",
        "ui.toolwindow.editor.diff.tab.title": "설정 차이: {0}",
        "ui.toolwindow.node.remote": "원격 변경",
        "ui.toolwindow.node.local": "로컬 변경",
        "ui.toolwindow.reset.tooltip.text": "이 상태로 재설정",
        "ui.toolwindow.reset.tooltip.description": "설정 상태가 선택한 변경 사항으로 재설정됩니다. 모든 변경 사항은 설정 내역에서 계속 사용할 수 있습니다.",
        "ui.toolwindow.undo.tooltip.text": "이 변경 사항 실행 취소 ({0,choice,1#개|2#개})",
        "ui.toolwindow.restored.from.date.text": "{0}에서 복원됨",
        "ui.toolwindow.restored.to.hash.text": "해시 {0}으(로) 복원됨",
        "ui.toolwindow.time.today": "오늘 {0}",
        "ui.toolwindow.time.yesterday": "어제 {0}",
        "ui.toolwindow.time.date": "{0}, {1}",
        "ui.toolwindow.change.category.system": "시스템",
        "ui.toolwindow.change.category.code": "코드 설정",
        "ui.toolwindow.change.category.plugins": "플러그인",
        "ui.toolwindow.change.category.keymap": "키맵",
        "ui.toolwindow.change.category.tools": "도구",
        "ui.toolwindow.change.category.ui": "UI 설정",
        "ui.toolwindow.change.category.other": "기타",
        "settings.repository.unbundled.notification.title": "Settings Repository 플러그인 번들이 해제되었습니다.",
        "settings.repository.unbundled.notification.description": "수동으로 설치하거나 JetBrains 클라우드 서버를 통해 백업 및 동기화를 시도할 수 있습니다.",
        "settings.repository.unbundled.notification.action.install.settings.repository": "Settings Repository 설치",
        "settings.repository.unbundled.notification.action.use.new.settings.sync": "백업 및 동기화 사용",
        "install.plugin.failed.no.compatible.notification.error.message": "{0}에 대해 호환되는 최신 플러그인을 찾을 수 없습니다.",
        "settings.group.sync.state.disable.locally": "로컬에서 끄기",
        "promotion.in.settings.text": "백업 및 동기화는 간편한 백업과 원활한 작업 환경을 위해 모든 기기에서 설정을 저장합니다.",
        "promotion.in.settings.header": "설정 백업",
        "promotion.in.settings.open": "백업 및 동기화로 이동",
        "promotion.in.settings.skip": "건너뛰기"
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
