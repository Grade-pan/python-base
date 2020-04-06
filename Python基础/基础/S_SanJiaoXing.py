# -*- coding: UTF-8 -*-

# Filename:S_SanJiaoXing.py
# author by : PXY
# 输入
a = float(input('三角形边长:'))
b = float(input('三角形边长:'))
c = float(input('三角形边长:'))
# 计算半周长
S = (a + b + c) / 2
# 计算三角形面积
area = (S * (S - a) * (S - b) * (S - c))
# 输出
print('边长为{0}，{1}，{2}的三角形的面积为:{3}'.format(a, b, c, area))
