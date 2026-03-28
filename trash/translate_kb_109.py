import json
from pathlib import Path

def update_missing_keys():
    file_path = Path("missing_translations/missing_keys_korean.json")
    
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    ko_dict = {
        "android.lint.inspections.trim.lambda": "trim()과 불필요한 람다 사용됨",
        "android.lint.inspections.unknown.nullness": "알 수 없는 Nullness",
        "android.lint.inspections.unnecessary.array.init": "불필요한 배열 초기화",
        "android.lint.inspections.use.toml.instead": "대신 TOML 버전 카탈로그 사용",
        "android.lint.inspections.use.value.of": "new 대신 valueOf를 사용해야 함",
        "android.lint.inspections.using.http": "HTTPS 대신 HTTP 사용 중",
        "android.lint.inspections.visible.for.tests": "테스트에만 표시됨",
        "android.lint.inspections.week.based.year": "주 기반 연도",
        "android.lint.inspections.wrong.comment.type": "잘못된 댓글 유형",
        "android.inspections.group.name": "Android",
        "android.lint.inspections.subgroup.name": "Lint",
        "android.lint.inspections.group.name": "Android Lint",
        "android.lint.inspections.wrong.gradle.method": "잘못된 Gradle 메서드가 호출됨",
        "android.lint.fix.add.android.prefix": "Android 접두사 추가",
        "android.lint.fix.replace.with.zero.dp": "크기 속성을 0dp로 교체",
        "android.lint.fix.remove.attribute": "속성 제거",
        "android.lint.fix.convert.to.dp": "\"dp\"(으)로 변환...",
        "android.lint.fix.set.to.wrap.content": "크기 속성을 'wrap_content'로 교체",
        "android.lint.fix.remove.unnecessary.view": "불필요한 뷰 제거",
        "android.lint.fix.replace.with.suggested.characters": "제안된 문자로 교체",
        "android.lint.fix.add.target.api": "@TargetApi({0}) 주석 추가",
        "android.lint.fix.add.requires.api": "@RequiresApi({0}) 주석 추가",
        "android.lint.fix.suppress.lint.api.annotation": "주석으로 {0} 억제",
        "android.lint.fix.suppress.lint.api.comment": "댓글로 {0} 억제",
        "android.lint.fix.suppress.lint.api.attr": "억제: tools:ignore=\"{0}\" 속성 추가",
        "android.lint.fix.replace.namespace": "자동 리소스 네임스페이스로 바꾸기",
        "android.lint.fix.open.firebase.assistant": "Firebase Assistant 열기",
        "android.lint.quickfixes.family": "Android Lint 빠른 수정"
    }
    
    filename = "LintBundle.properties"
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
