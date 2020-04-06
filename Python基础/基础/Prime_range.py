# -*- coding: UTF-8 -*-

# Filename:Prime_range.py
# author by : PXY
amin = int(input('请输入区间下限:'))
amax = int(input('请输入区间上限:'))
for a in range(amin, amax + 1):
    if (a == 2 or a == 3 or a == 5 or a == 7) or (a % 2 != 0 and a % 3 != 0 and a % 5 != 0 and a % 7 != 0):
        print('{0}是质数'.format(a))
