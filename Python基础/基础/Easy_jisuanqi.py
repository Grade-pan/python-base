# -*- coding: UTF-8 -*-

# Filename:简易计算器.py
# author by : PXY
def add_A(x, y):
    return x + y


def dec_A(x, y):
    return x - y


def Mov_A(x, y):
    return x * y


def div_A(x, y):
    if y == 0:
        return ValueError
    else:
        return x / y


A = int(input('请输入数据1:'))
B = int(input('请输入数据2:'))
C = input('输入计算模式:')
if C == '相加':
    print('{0}+{1}={2}'.format(A, B, add_A(A, B)))
if C == '相减':
    print('{0}-{1}={2}'.format(A, B, dec_A(A, B)))
if C == '相乘':
    print('{0}x{1}={2}'.format(A, B, Mov_A(A, B)))
if C == '相除':
    print('{0}÷{1}={2}'.format(A, B, div_A(A, B)))
