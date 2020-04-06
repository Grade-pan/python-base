# -*- coding: UTF-8 -*-

# Filename:JudgeNumber.py
# author by : PXY
import unicodedata


def is_Number(s):
    # 测试字符
    try:
        float(s)
        return True
    except ValueError:
        pass
    # 测试文字
    try:
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        return False


print(is_Number('๒'))
