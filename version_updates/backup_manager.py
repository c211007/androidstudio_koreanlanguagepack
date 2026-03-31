#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
백업 및 롤백 관리 스크립트

src/main/resources/messages 디렉토리의 백업 생성 및 복원을 관리합니다.
"""

import os
import shutil
from pathlib import Path
from datetime import datetime


def get_messages_dir():
    """messages 디렉토리 경로 가져오기"""
    project_root = Path(__file__).parent.parent.parent.parent  # src/main/version_updates → main → src → root
    messages_dir = project_root / "src" / "main" / "resources" / "messages"
    return messages_dir


def get_backup_dir():
    """백업 디렉토리 경로 가져오기"""
    project_root = Path(__file__).parent.parent.parent.parent  # src/main/version_updates → main → src → root
    backup_base = project_root / "src" / "main" / "resources" / "messages_backups"
    backup_base.mkdir(parents=True, exist_ok=True)
    return backup_base


def create_backup(description=""):
    """현재 messages 디렉토리 백업 생성"""
    messages_dir = get_messages_dir()

    if not messages_dir.exists():
        raise FileNotFoundError(f"messages 디렉토리를 찾을 수 없습니다: {messages_dir}")

    # 백업 디렉토리 생성
    backup_base = get_backup_dir()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_name = f"backup_{timestamp}"
    if description:
        # 파일명으로 사용 가능한 문자만 남기기
        safe_desc = "".join(c for c in description if c.isalnum() or c in (' ', '-', '_')).strip()
        safe_desc = safe_desc.replace(' ', '_')
        backup_name += f"_{safe_desc}"

    backup_path = backup_base / backup_name

    print(f"백업 생성 중...")
    print(f"  원본: {messages_dir}")
    print(f"  백업: {backup_path}")

    try:
        # 디렉토리 전체 복사
        shutil.copytree(messages_dir, backup_path)

        # 백업 정보 파일 생성
        info_file = backup_path / "_backup_info.txt"
        with open(info_file, 'w', encoding='utf-8') as f:
            f.write(f"백업 생성 일시: {datetime.now()}\n")
            f.write(f"원본 경로: {messages_dir}\n")
            if description:
                f.write(f"설명: {description}\n")
            f.write(f"\n파일 수: {len(list(backup_path.glob('*.properties')))}\n")

        print(f"✅ 백업 완료: {backup_path}")
        return backup_path

    except Exception as e:
        print(f"❌ 백업 생성 실패: {e}")
        raise


def list_backups():
    """백업 목록 조회"""
    backup_base = get_backup_dir()

    if not backup_base.exists():
        return []

    backups = []
    for backup_dir in backup_base.iterdir():
        if backup_dir.is_dir() and backup_dir.name.startswith('backup_'):
            info_file = backup_dir / "_backup_info.txt"

            # 백업 정보 읽기
            date_str = ""
            description = ""
            file_count = 0

            if info_file.exists():
                try:
                    with open(info_file, 'r', encoding='utf-8') as f:
                        for line in f:
                            if line.startswith('백업 생성 일시:'):
                                date_str = line.split(':', 1)[1].strip()
                            elif line.startswith('설명:'):
                                description = line.split(':', 1)[1].strip()
                            elif line.startswith('파일 수:'):
                                file_count = int(line.split(':')[1].strip())
                except:
                    pass

            if not date_str:
                # 디렉토리 이름에서 타임스탬프 추출
                try:
                    timestamp_part = backup_dir.name.split('_')[1] + '_' + backup_dir.name.split('_')[2]
                    date_obj = datetime.strptime(timestamp_part, "%Y%m%d_%H%M%S")
                    date_str = date_obj.strftime("%Y-%m-%d %H:%M:%S")
                except:
                    date_str = "Unknown"

            backups.append({
                'name': backup_dir.name,
                'path': backup_dir,
                'date': date_str,
                'description': description,
                'file_count': file_count
            })

    # 최신순으로 정렬
    backups.sort(key=lambda x: x['name'], reverse=True)

    return backups


def restore_backup(backup_path):
    """백업 복원"""
    backup_path = Path(backup_path)
    messages_dir = get_messages_dir()

    if not backup_path.exists():
        raise FileNotFoundError(f"백업을 찾을 수 없습니다: {backup_path}")

    print(f"\n백업 복원 중...")
    print(f"  백업: {backup_path}")
    print(f"  대상: {messages_dir}")

    try:
        # 기존 messages 디렉토리 삭제
        if messages_dir.exists():
            print(f"  기존 디렉토리 삭제 중...")
            shutil.rmtree(messages_dir)

        # 백업에서 복원
        print(f"  백업 파일 복사 중...")
        shutil.copytree(backup_path, messages_dir)

        # _backup_info.txt 파일은 제거
        info_file = messages_dir / "_backup_info.txt"
        if info_file.exists():
            info_file.unlink()

        print(f"✅ 복원 완료!")
        print(f"  복원된 파일 수: {len(list(messages_dir.glob('*.properties')))}")

    except Exception as e:
        print(f"❌ 복원 실패: {e}")
        raise


def delete_backup(backup_path):
    """백업 삭제"""
    backup_path = Path(backup_path)

    if not backup_path.exists():
        raise FileNotFoundError(f"백업을 찾을 수 없습니다: {backup_path}")

    try:
        shutil.rmtree(backup_path)
        print(f"✅ 백업 삭제 완료: {backup_path.name}")
    except Exception as e:
        print(f"❌ 백업 삭제 실패: {e}")
        raise


def main():
    """테스트용 메인 함수"""
    print("=" * 80)
    print("백업 관리 테스트")
    print("=" * 80)

    # 백업 목록 조회
    backups = list_backups()

    if backups:
        print(f"\n현재 백업 목록 ({len(backups)}개):\n")
        for i, backup in enumerate(backups, 1):
            print(f"{i}. {backup['name']}")
            print(f"   날짜: {backup['date']}")
            if backup['description']:
                print(f"   설명: {backup['description']}")
            print(f"   파일 수: {backup['file_count']}")
            print()
    else:
        print("\n백업이 없습니다.")


if __name__ == "__main__":
    main()
