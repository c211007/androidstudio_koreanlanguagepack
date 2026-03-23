#!/bin/bash
# Android Studio Properties Key Extractor
# 모든 properties 파일에서 키 값을 추출하고 분석합니다

WORK_DIR="c:\Users\klanary\Desktop\vscode 모음\android_korean\androidstudio_koreanlanguagepack"
OUTPUT_DIR="$WORK_DIR/extracted_keys"

mkdir -p "$OUTPUT_DIR"

echo "=========================================="
echo "Android Studio Properties Key Extractor"
echo "=========================================="
echo ""

# IntelliJ Platform 번들 키 추출
echo "[1/4] IntelliJ Platform 번들 키 추출 중..."
find "$WORK_DIR/extracted_bundles/intellij/messages" -name "*.properties" | while read file; do
    basename=$(basename "$file" .properties)
    echo "  Processing: $basename"
    grep -E "^[a-zA-Z0-9._\-]+=" "$file" | \
        sed 's/=.*//' | \
        sort > "$OUTPUT_DIR/${basename}_keys.txt"
    count=$(wc -l < "$OUTPUT_DIR/${basename}_keys.txt")
    echo "    → $count keys extracted"
done

# Android 번들 키 추출
echo ""
echo "[2/4] Android 번들 키 추출 중..."
find "$WORK_DIR/extracted_bundles/android/messages" -name "*.properties" | while read file; do
    basename=$(basename "$file" .properties)
    echo "  Processing: $basename"
    grep -E "^[a-zA-Z0-9._\-]+=" "$file" | \
        sed 's/=.*//' | \
        sort > "$OUTPUT_DIR/${basename}_keys.txt"
    count=$(wc -l < "$OUTPUT_DIR/${basename}_keys.txt")
    echo "    → $count keys extracted"
done

# 모든 키 병합
echo ""
echo "[3/4] 모든 키 병합 중..."
cat "$OUTPUT_DIR"/*_keys.txt | sort -u > "$OUTPUT_DIR/all_keys.txt"
total_keys=$(wc -l < "$OUTPUT_DIR/all_keys.txt")
echo "  총 고유 키 개수: $total_keys"

# 키 명명 규칙 분석
echo ""
echo "[4/4] 키 명명 규칙 분석 중..."
cat > "$OUTPUT_DIR/key_patterns.txt" << 'EOF'
===========================================
Android Studio Properties 키 명명 규칙
===========================================

1. 액션 관련 (Actions)
   - action.<ActionId>.text = 메뉴/버튼에 표시되는 텍스트
   - action.<ActionId>.description = 도구 설명 (tooltip)
   예: action.NewProject.text=새 프로젝트...

2. 그룹 관련 (Groups)
   - group.<GroupId>.text = 메뉴 그룹 이름
   예: group.FileMenu.text=파일(&F)

3. 일반 메시지
   - <기능>.<메시지유형> 형식
   예: cannot.resolve.color.literal.error=Cannot resolve color ''{0}''

4. 인텐션 (Intention Actions)
   - <기능>.intention.text = 인텐션 액션 텍스트
   예: add.string.resource.intention.text=Extract string resource

5. 다이얼로그/창 제목
   - <기능>.dialog.title = 다이얼로그 제목
   - <기능>.command.name = 명령 이름
   예: new.resource.dialog.title=New Resource File

6. 설정 관련
   - <카테고리>.<항목> 형식
   예: android.run.configuration.type.name=Android App

7. 오류/경고 메시지
   - <문제>.error = 오류 메시지
   - <문제>.warning = 경고 메시지
   예: package.not.found.error=Package is not specified

8. 도구 창 (Tool Windows)
   - action.Activate<ToolWindow>ToolWindow.text = 도구 창 활성화
   예: action.ActivateLogcatToolWindow.text=Logcat

9. 레벨/상태 표시
   - <상태>.level.title = 레벨 제목
   예: error.level.title=Error

10. 리소스 관련
    - <리소스타입>.resource.<액션> 형식
    예: create.value.resource.quickfix.name=Create value resource...

EOF

cat "$OUTPUT_DIR/key_patterns.txt"

# 키 패턴 통계
echo ""
echo "=========================================="
echo "키 패턴 통계"
echo "=========================================="
echo "action.* 패턴: $(grep -c '^action\.' "$OUTPUT_DIR/all_keys.txt") 개"
echo "group.* 패턴: $(grep -c '^group\.' "$OUTPUT_DIR/all_keys.txt") 개"
echo "*.error 패턴: $(grep -c '\.error$' "$OUTPUT_DIR/all_keys.txt") 개"
echo "*.warning 패턴: $(grep -c '\.warning$' "$OUTPUT_DIR/all_keys.txt") 개"
echo "*.text 패턴: $(grep -c '\.text$' "$OUTPUT_DIR/all_keys.txt") 개"
echo "*.title 패턴: $(grep -c '\.title$' "$OUTPUT_DIR/all_keys.txt") 개"
echo "*.description 패턴: $(grep -c '\.description$' "$OUTPUT_DIR/all_keys.txt") 개"
echo "*.intention.* 패턴: $(grep -c '\.intention\.' "$OUTPUT_DIR/all_keys.txt") 개"

echo ""
echo "=========================================="
echo "완료!"
echo "=========================================="
echo "결과 파일 위치: $OUTPUT_DIR"
echo "- all_keys.txt: 모든 고유 키 목록"
echo "- key_patterns.txt: 키 명명 규칙 설명"
echo "- *_keys.txt: 각 번들별 키 목록"
