import json

translations = {
  "add.commit.message": "커밋 메시지 추가(&A)",
  "commit.message": "커밋 메시지",
  "general": "일반",
  "label.html.available.placeholders.html": "<html>사용 가능한 자리 표시자: {0}</html>",
  "label.undefined": "<정의되지 않음>",
  "lo.gin.anonymously": "익명으로 로그인(&G)",
  "not.youtrack.customer.yet.get.youtrack": "아직 YouTrack 고객이 아니신가요? YouTrack 받기",
  "password": "비밀번호(&P):",
  "pr.oxy.settings": "프록시 설정(&O)…",
  "server.u.rl": "서버 URL(&R):",
  "sh.are.url": "URL 공유(&A)",
  "te.st": "테스트(&S)",
  "use": "사용…",
  "use.domain.login.format.for.ntlm.authentication": "NTLM 인증에 도메인\\\\로그인 형식 사용",
  "use.http.authentication": "HTTP 인증 사용(&H)",
  "use.personal.access.token": "개인 액세스 토큰 사용(&T)",
  "use.prox.y": "프록시 사용(&Y)",
  "userna.me": "사용자 이름(&M):"
}

with open("missing_translations/missing_keys_korean.json", "r", encoding="utf-8") as f:
    data = json.load(f)

found = False
for file_info in data.get("new_files", []):
    if file_info.get("filename") == "TaskApiBundle.properties":
        keys_dict = file_info.get("keys", file_info.get("properties", {}))
        keys_dict.update(translations)
        file_info["keys"] = keys_dict
        found = True
        break

if not found:
    data.setdefault("new_files", []).append({
        "filename": "TaskApiBundle.properties",
        "keys": translations
    })

with open("missing_translations/missing_keys_korean.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)
