# -*- coding: UTF-8 -*-

# Filename:阿姆斯特朗数.py
# author by : PXY
a = int(input('请输入一个数:'))
b = a
Sum = len(str(a))
Sum1 = 0
for i in range(2, Sum + 1):
    x = a % 10
    a = a // 10
    Sum1 = Sum1 + x ** Sum

if Sum1 + a ** Sum == b:
    print('%d是阿姆斯特朗数' % b)
else:
    print('%d不是阿姆斯特朗数' % b)
