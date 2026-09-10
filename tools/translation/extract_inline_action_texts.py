#!/usr/bin/env python3
"""
Android Studio에 번들된 모든 플러그인 jar 안의 plugin.xml(및 포함된 xml 조각)을 뒤져서
key= 없이 text=/description= 을 인라인으로 박아넣은 <action>/<group> 요소를 찾아낸다.

이런 액션들은 action.<id>.text / action.<id>.description (그룹은 group.<id>.text/description)
키로 오버라이드할 수 있는데, 지금까지 이 프로젝트는 .properties 파일끼리만 키를 비교했기 때문에
plugin.xml에 박힌 인라인 텍스트는 애초에 감지 대상이 아니었다.

이 스크립트는:
1. 지정된 Android Studio 설치 디렉토리의 모든 plugins/*/lib/*.jar (+ 옵션으로 core lib/*.jar) 를 스캔
2. 각 jar 안의 .xml 파일들(단순 확장자 기준, plugin.xml 뿐 아니라 xi:include로 쪼개진 조각 xml도 포함)을 파싱
3. <action id=... text="...">, <group id=... text="...">를 찾아 action.<id>.text / group.<id>.text 키 계산
   (description= 이 있으면 action.<id>.description / group.<id>.description 도 계산)
4. src/main/resources/messages/*.properties 전체에서 이미 그 키가 있는지 대조
5. 없는 것만 missing_translations/missing_action_texts.json 으로 저장하고 요약 출력
"""
import glob
import json
import os
import re
import sys
import zipfile
from xml.etree import ElementTree as ET

# 이 파일은 <repo_root>/tools/translation/ 안에 있으므로 두 단계 위가 REPO_ROOT다.
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
MESSAGES_DIR = os.path.join(REPO_ROOT, "src", "main", "resources", "messages")
OUT_PATH = os.path.join(REPO_ROOT, "missing_translations", "missing_action_texts.json")


def find_as_install_dir():
    pattern = "C:/Users/*/.gradle/caches/*/transforms/*/transformed/android-studio-*"
    matches = [p for p in glob.glob(pattern) if os.path.isdir(p)]
    if not matches:
        return None
    # 가장 최근에 수정된 것 사용
    matches.sort(key=lambda p: os.path.getmtime(p), reverse=True)
    return matches[0]


def load_existing_keys():
    keys = set()
    for path in glob.glob(os.path.join(MESSAGES_DIR, "*.properties")):
        try:
            with open(path, encoding="utf-8") as f:
                lines = f.readlines()
        except Exception:
            continue
        i = 0
        while i < len(lines):
            line = lines[i].rstrip("\r\n")
            while line.endswith("\\") and i + 1 < len(lines):
                line = line[:-1] + lines[i + 1].rstrip("\r\n")
                i += 1
            stripped = line.strip()
            if stripped and not stripped.startswith("#") and not stripped.startswith("!"):
                m = re.match(r"([^=:\s]+)\s*[=:]", stripped)
                if m:
                    keys.add(m.group(1).strip())
            i += 1
    return keys


def iter_plugin_jars(as_dir, include_core=True):
    jars = []
    plugins_dir = os.path.join(as_dir, "plugins")
    for root, _dirs, files in os.walk(plugins_dir):
        for fn in files:
            if fn.endswith(".jar"):
                jars.append(os.path.join(root, fn))
    if include_core:
        lib_dir = os.path.join(as_dir, "lib")
        for fn in os.listdir(lib_dir) if os.path.isdir(lib_dir) else []:
            if fn.endswith(".jar"):
                jars.append(os.path.join(lib_dir, fn))
    return jars


def plugin_name_from_jar_path(as_dir, jar_path):
    rel = os.path.relpath(jar_path, as_dir)
    parts = rel.split(os.sep)
    if parts[0] == "plugins" and len(parts) > 1:
        return parts[1]
    return "(core)"


ACTION_TAGS = {"action", "group"}


def scan_xml_bytes(xml_bytes, source_label, results, seen_ids):
    try:
        text = xml_bytes.decode("utf-8", errors="replace")
        # xi:include 등 네임스페이스 처리 문제를 피하려고 정규식 기반으로 태그만 훑는다
        root = ET.fromstring(text)
    except Exception:
        return
    for el in root.iter():
        tag = el.tag.split("}")[-1]
        if tag not in ACTION_TAGS:
            continue
        el_id = el.get("id")
        if not el_id:
            continue
        text_attr = el.get("text")
        desc_attr = el.get("description")
        if not text_attr and not desc_attr:
            continue
        prefix = "action" if tag == "action" else "group"
        key_text = f"{prefix}.{el_id}.text"
        key_desc = f"{prefix}.{el_id}.description"
        dedup_key = (key_text, source_label)
        if dedup_key in seen_ids:
            continue
        seen_ids.add(dedup_key)
        results.append({
            "id": el_id,
            "tag": tag,
            "text": text_attr,
            "description": desc_attr,
            "key_text": key_text,
            "key_description": key_desc if desc_attr else None,
            "source": source_label,
        })


def scan_jar(jar_path, plugin_name, results, seen_ids):
    try:
        with zipfile.ZipFile(jar_path) as zf:
            for name in zf.namelist():
                if not name.endswith(".xml"):
                    continue
                # 흔한 무의미 xml(파일 인덱스 등)은 건너뛰되, plugin.xml 및 조각들은 포함
                try:
                    data = zf.read(name)
                except Exception:
                    continue
                if b"<action" not in data and b"<group" not in data:
                    continue
                scan_xml_bytes(data, f"{plugin_name}:{os.path.basename(jar_path)}:{name}", results, seen_ids)
    except zipfile.BadZipFile:
        pass


def main():
    as_dir = find_as_install_dir()
    if not as_dir:
        print("Android Studio 설치 디렉토리를 못 찾았습니다. 경로를 인자로 넘겨주세요.")
        sys.exit(1)
    print(f"Android Studio dir: {as_dir}")

    existing_keys = load_existing_keys()
    print(f"기존 번역 키 개수: {len(existing_keys)}")

    jars = iter_plugin_jars(as_dir, include_core=True)
    print(f"스캔할 jar 개수: {len(jars)}")

    results = []
    seen_ids = set()
    for i, jar_path in enumerate(jars):
        plugin_name = plugin_name_from_jar_path(as_dir, jar_path)
        scan_jar(jar_path, plugin_name, results, seen_ids)
        if (i + 1) % 200 == 0:
            print(f"  ...{i + 1}/{len(jars)} jar 처리, 지금까지 발견 {len(results)}개")

    print(f"인라인 text=/description= 액션·그룹 총 발견: {len(results)}개 (중복 id 포함)")

    # id 기준으로 합치기 (여러 jar에 같은 id가 중복 등록될 수 있음)
    by_id = {}
    for r in results:
        by_id.setdefault(r["key_text"], r)

    missing = []
    for key_text, r in by_id.items():
        missing_text = key_text not in existing_keys
        missing_desc = r["key_description"] is not None and r["key_description"] not in existing_keys
        if missing_text or missing_desc:
            missing.append(r)

    missing.sort(key=lambda r: r["source"])

    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        json.dump(missing, f, ensure_ascii=False, indent=2)

    print(f"고유 action/group id: {len(by_id)}개")
    print(f"번역 누락(키 없음): {len(missing)}개")
    print(f"결과 저장: {OUT_PATH}")

    # 플러그인별 요약
    from collections import Counter
    plugin_counts = Counter(r["source"].split(":")[0] for r in missing)
    print("\n플러그인별 누락 개수 (상위 30개):")
    for name, cnt in plugin_counts.most_common(30):
        print(f"  {name}: {cnt}")


if __name__ == "__main__":
    main()
