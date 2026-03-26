#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
missing_keys.json 번역 스크립트 (간소화 버전)
사용법: python simple_translator.py
"""

import json
import sys
from pathlib import Path


def translate_simple(text):
    """간단한 번역 함수"""
    # 짧은 번역 사전
    trans = {
        "Running": "실행 중", "Ran": "실행됨",
        "Reading": "읽는 중", "Read": "읽음",
        "Editing": "편집 중", "Edited": "편집됨",
        "Creating": "생성 중", "Created": "생성됨",
        "Deleting": "삭제 중", "Deleted": "삭제됨",
        "Analyzing": "분석 중", "Analyzed": "분석됨",
        "Searching": "검색 중", "Searched": "검색됨",
        "Finding": "찾는 중", "Found": "찾음",
        "Listing": "목록 표시 중", "Listed": "목록 표시됨",
        "Identifying": "식별 중", "Identified": "식별됨",
        "Executing": "실행 중", "Executed": "실행됨",
        "Notifying": "알림 중", "Notified": "알림됨",
        "Asking": "질문 중", "Asked": "질문함",
        "Waiting": "대기 중",
        "Agent Change": "에이전트 변경",
        "the user": "사용자",
        "your answer": "답변",
        "current file": "현재 파일",
        "VCS roots": "VCS 루트",
        "VCS root for file": "파일의 VCS 루트",
        "Auto-approving": "자동 승인 중",
        "UI Tools": "UI 도구",
        "Track Pad": "트랙 패드",
        "Resource Usage": "리소스 사용량",
        "View Mode": "보기 모드",
        "Editor View Mode": "편집기 보기 모드",
        "Default": "기본값",
        "Essentials": "필수",
        "Preview Settings": "미리보기 설정",
        "Enable live updates": "실시간 업데이트 사용",
        "Debugger": "디버거",
        "Hybrid/Auto Debugger": "하이브리드/자동 디버거",
        "smart step into": "스마트 단계별 실행",
        "Line Breakpoints": "라인 중단점",
        "Error": "오류", "error": "오류",
        "Failed": "실패", "failed": "실패",
        "Cannot": "할 수 없음",
        "not supported": "지원되지 않음",
        "not implemented": "구현되지 않음",
        "Invalid": "잘못됨",
        "not found": "찾을 수 없음",
        "Unknown": "알 수 없음",
        "Assembly language file": "어셈블리 언어 파일",
    }
    
    if not text:
        return text
    
    # 너무 긴 텍스트는 그대로 반환 (해시, URL 등)
    if len(text) > 50:
        return text
    
    # 전체 일치
    if text in trans:
        return trans[text]
    
    # 부분 번역
    result = text
    for eng, kor in sorted(trans.items(), key=lambda x: -len(x[0])):
        if eng in result:
            result = result.replace(eng, kor)
    
    return result


def main():
    base_dir = Path(__file__).parent
    input_path = base_dir / "missing_translations" / "missing_keys.json"
    output_path = base_dir / "missing_translations" / "missing_keys_translated_ko.json"
    
    print(f"파일 로드 중: {input_path}")
    with open(input_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    total = 0
    translated = 0
    
    print("번역 중...")
    if "new_files" in data:
        file_count = len(data["new_files"])
        for idx, file_entry in enumerate(data["new_files"], 1):
            if idx % 50 == 1:
                print(f"  {idx}/{file_count} 파일 처리 중...")
            
            keys = file_entry.get("keys", {})
            for key, value in keys.items():
                total += 1
                new_val = translate_simple(value)
                if new_val != value:
                    translated += 1
                keys[key] = new_val
    
    print(f"\n번역 완료:")
    print(f"  전체: {total:,}개")
    print(f"  번역: {translated:,}개 ({translated*100//total if total else 0}%)")
    
    print(f"\n저장 중: {output_path}")
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print("완료!")
    return 0


if __name__ == "__main__":
    sys.exit(main())
