#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
스크립트를 실행하기 위한 래퍼
"""

import os
import sys

# 현재 디렉토리 변경
os.chdir(r'c:\Users\klanary\Desktop\vscode 모음\android_korean\androidstudio_koreanlanguagepack')

# fix_headers.py 파일 실행
exec(open('fix_headers.py').read())
