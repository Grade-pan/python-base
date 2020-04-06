# -*- coding: UTF-8 -*-

# Filename:JieCheng.py
# author by : PXY

def JC(a):
    if a == 1 or a == 0:
        return 1
    if a < 0:
        return '负数没有阶乘'
    else:
        return a * JC(a - 1)


a = int(input('请输入:'))
print(JC(a))
