# -*- coding: utf-8 -*-
"""
apply_action_translations.py 의 TRANSLATIONS 딕셔너리를 그대로 재사용해서,
ActionManager로 액션 text/description을 직접 덮어쓰는 Kotlin 데이터 파일을 생성한다.

(plugin.xml text= 인라인 액션은 리소스 번들 키 조회 자체가 안 일어나서
 ActionsBundle.properties 오버라이드가 통하지 않으므로, 코드로 직접 덮어써야 함.)
"""
import importlib.util
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# 이 파일은 <repo_root>/tools/translation/ 안에 있으므로 두 단계 위가 REPO_ROOT다.
REPO_ROOT = os.path.dirname(os.path.dirname(SCRIPT_DIR))
OUT_PATH = os.path.join(
    REPO_ROOT, "src", "main", "kotlin", "org", "jetbrains", "plugins",
    "koreanlanguagepack", "InlineActionTextOverrides.kt",
)


def _load_dict(filename, attr):
    spec = importlib.util.spec_from_file_location(attr, os.path.join(SCRIPT_DIR, filename))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return getattr(mod, attr)


def load_translations():
    round1 = _load_dict("apply_action_translations.py", "TRANSLATIONS")
    round2 = _load_dict("action_translations_round2.py", "TRANSLATIONS_ROUND2")

    merged = {}
    for source in (round1, round2):
        for action_id, (text_ko, desc_ko) in source.items():
            existing_text, existing_desc = merged.get(action_id, (None, None))
            merged[action_id] = (
                text_ko if text_ko is not None else existing_text,
                desc_ko if desc_ko is not None else existing_desc,
            )
    return merged


def kt_string_literal(s):
    escaped = s.replace("\\", "\\\\").replace("$", "\\$").replace('"', '\\"')
    return f'"{escaped}"'


def main():
    translations = load_translations()

    lines = []
    lines.append("package org.jetbrains.plugins.koreanlanguagepack")
    lines.append("")
    lines.append("// generate_action_override_kotlin.py 로 자동 생성됨. 직접 수정하지 말 것.")
    lines.append("//")
    lines.append("// Android/Compose/NDK 등 다른 플러그인이 plugin.xml에 text=/description= 을")
    lines.append("// 인라인으로 박아넣은 액션·그룹들의 한국어 번역. 이런 액션은 리소스 번들 키")
    lines.append("// (action.<id>.text)를 통한 오버라이드가 적용되지 않기 때문에")
    lines.append("// InlineActionTextOverrideApplier 가 ActionManager로 직접 텍스트를 덮어쓴다.")
    lines.append("internal val INLINE_ACTION_TEXT_OVERRIDES: Map<String, String> = mapOf(")
    for action_id, (text_ko, _desc_ko) in sorted(translations.items()):
        if text_ko is not None:
            lines.append(f"    {kt_string_literal(action_id)} to {kt_string_literal(text_ko)},")
    lines.append(")")
    lines.append("")
    lines.append("internal val INLINE_ACTION_DESCRIPTION_OVERRIDES: Map<String, String> = mapOf(")
    for action_id, (_text_ko, desc_ko) in sorted(translations.items()):
        if desc_ko is not None:
            lines.append(f"    {kt_string_literal(action_id)} to {kt_string_literal(desc_ko)},")
    lines.append(")")
    lines.append("")

    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"생성 완료: {OUT_PATH}")


if __name__ == "__main__":
    main()
