#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
missing_keys.json을 한국어로 번역하는 스크립트
Translation Guidelines에 따라 자동 번역을 수행합니다.
"""

import json
import re
from pathlib import Path


def translate_key_value(key: str, value: str) -> str:
    """
    영어 키-값을 한국어로 번역합니다.
    
    Translation Guidelines:
    1. {0}, {1}, {2} 같은 플레이스홀더는 그대로 유지
    2. _(언더바) 뒤 문자는 단축키 - 한국어 번역 뒤 괄호에 넣기
    3. ... (말줄임표) 유지
    4. 특수문자 앞에 백슬래시 사용
    """
    
    # 번역 사전 (주요 용어들)
    translations = {
        # 파일 작업
        "Agent Change": "에이전트 변경",
        "Asking the user": "사용자에게 질문 중",
        "Asked the user": "사용자에게 질문함",
        "Waiting for your answer": "답변 대기 중",
        "Deleting": "삭제 중",
        "Deleted": "삭제됨",
        "Reading": "읽는 중",
        "Read": "읽음",
        "Editing": "편집 중",
        "Edited": "편집됨",
        "Running git": "git 실행 중",
        "Ran git": "git 실행됨",
        "Finding declaration of": "선언 찾는 중",
        "Searched for declaration of": "선언 검색됨",
        "MCP": "MCP",
        "Notifying the user": "사용자에게 알림 중",
        "Notified the user": "사용자에게 알림",
        "Reading URL": "URL 읽는 중",
        "Read URL": "URL 읽음",
        "Searching the web": "웹 검색 중",
        "Searched the web": "웹 검색됨",
        "Analyzing": "분석 중",
        "Analyzed": "분석됨",
        "Analyzing current file": "현재 파일 분석 중",
        "Analyzed current file": "현재 파일 분석됨",
        "Searching for files matching": "파일 검색 중",
        "Searched for files matching": "파일 검색됨",
        "Grepping for": "Grep 검색 중",
        "Grepped for": "Grep 검색됨",
        "Finding usages of": "사용처 찾는 중",
        "Found usages of": "사용처 찾음",
        "Executing": "실행 중",
        "Executed": "실행됨",
        "Creating a plan": "계획 작성 중",
        "Created a plan": "계획 작성됨",
        "Marking step as complete": "단계를 완료로 표시 중",
        "Marked step as complete": "단계를 완료로 표시함",
        "Finding declaration of": "선언 찾는 중",
        "Found declaration of": "선언 찾음",
        "Listing files in": "파일 목록 표시 중",
        "Listed files in": "파일 목록 표시됨",
        "Identifying VCS roots": "VCS 루트 식별 중",
        "Identifying VCS root for file": "파일의 VCS 루트 식별 중",
        "Identified VCS roots": "VCS 루트 식별됨",
        "Identified VCS root for file": "파일의 VCS 루트 식별됨",
        "Auto-approving": "자동 승인 중",
        
        # UI Tools
        "UI Tools": "UI 도구",
        "Track Pad": "트랙 패드",
        "Magnify zooming (pinch) sensitivity": "확대/축소(핀치) 민감도",
        "Resource Usage": "리소스 사용량",
        "Show split mode if file contains preview annotation": "파일에 미리보기 주석이 포함된 경우 분할 모드 표시",
        "View Mode": "보기 모드",
        "Editor View Mode": "편집기 보기 모드",
        "Resource": "리소스",
        "Default": "기본값",
        "Essentials": "필수",
        "Kotlin": "Kotlin",
        "Preview Settings": "미리보기 설정",
        "Enable live updates": "실시간 업데이트 사용",
        "Preview will preserve resources by inflating previews on demand, and disabling live updates and preview modes.": "미리보기는 필요할 때만 미리보기를 생성하고 실시간 업데이트 및 미리보기 모드를 비활성화하여 리소스를 절약합니다.",
        "Store Current Layout": "현재 레이아웃 저장",
        "Paste (with new IDs)": "붙여넣기(새 ID 사용)",
        "Paste Views from Clipboard and generate new IDs": "클립보드에서 뷰를 붙여넣고 새 ID 생성",
        "Paste with existing IDs": "기존 ID로 붙여넣기",
        "Paste Views from Clipboard and keep the IDs unchanged": "클립보드에서 뷰를 붙여넣고 ID를 변경하지 않음",
        
        # Debugger
        "A&lways do smart step into (Java and Kotlin)": "항상 스마트 단계별 실행 사용(Java 및 Kotlin)(_L)",
        "Hybrid/Auto Debugger": "하이브리드/자동 디버거",
        
        # Build info
        "buildNumber": "빌드 번호",
        "version": "버전",
        "distributionId": "배포 ID",
        "distributionShortName": "배포 단축 이름",
        "distributionName": "배포 이름",
        "Apache Maven": "Apache Maven",
        "Maven": "Maven",
    }
    
    # 번역 적용
    result = value
    for eng, kor in translations.items():
        # 전체 매칭 우선
        if value == eng:
            return kor
        # 부분 매칭
        result = result.replace(eng, kor)
    
    # 플레이스홀더 {0}, {1}, {2} 등은 그대로 유지됨
    # \\u2026 (ellipsis) 유니코드도 그대로 유지됨
    
    return result


def process_json_file(input_path: Path, output_path: Path):
    """JSON 파일을 읽어서 번역하고 저장합니다."""
    
    print(f"Reading {input_path}...")
    with open(input_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    print(f"Translating...")
    total_keys = 0
    translated_keys = 0
    
    # new_files 배열의 각 파일 처리
    if "new_files" in data:
        for file_entry in data["new_files"]:
            filename = file_entry.get("filename", "")
            keys = file_entry.get("keys", {})
            
            print(f"  Processing {filename} ({len(keys)} keys)...")
            
            for key, value in keys.items():
                total_keys += 1
                translated_value = translate_key_value(key, value)
                if translated_value != value:
                    translated_keys += 1
                keys[key] = translated_value
    
    print(f"\nTranslation complete:")
    print(f"  Total keys: {total_keys}")
    print(f"  Translated keys: {translated_keys}")
    print(f"  Unchanged keys: {total_keys - translated_keys}")
    
    print(f"\nWriting to {output_path}...")
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print("Done!")


def main():
    """메인 함수"""
    base_dir = Path(__file__).parent
    input_file = base_dir / "missing_translations" / "missing_keys.json"
    output_file = base_dir / "missing_translations" / "missing_keys_translated.json"
    
    if not input_file.exists():
        print(f"Error: {input_file} not found!")
        return 1
    
    process_json_file(input_file, output_file)
    return 0


if __name__ == "__main__":
    exit(main())
