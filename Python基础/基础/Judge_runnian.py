# -*- coding: UTF-8 -*-

# Filename:JudgeNumber.py
# author by : PXY

a = int(input('请输入年份:'))
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print('{0}是闰年'.format(a))
else:
    print('{0}不是闰年'.format(a))
