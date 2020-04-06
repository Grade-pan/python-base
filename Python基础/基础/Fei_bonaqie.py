# -*- coding: UTF-8 -*-

# Filename:Fei_bonaqie.py
# author by : PXY
a = 0
b = 1
c = 0
x = int(input('请输入数列项数:'))
try:
    print('斐波那契数列的前{0}项如下'.format(x))
    print(0)
    while x > 1:
        a = b
        b = c
        c = a + b
        x = x - 1
        print(c)
except ValueError:
    pass
