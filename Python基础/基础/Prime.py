# -*- coding: UTF-8 -*-

# Filename:Prime.py
# author by : PXY
a = int(input('请输入一个大于等于2的数:'))
if (a == 2 or a == 3 or a == 5 or a == 7) or (a % 2 != 0 and a % 3 != 0 and a % 5 != 0 and a % 7 != 0):
    print('{0}是质数'.format(a))
else:
    print('{0}不是质数'.format(a))
