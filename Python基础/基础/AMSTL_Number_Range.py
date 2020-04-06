# -*- coding: UTF-8 -*-

# Filename:阿姆斯特朗数.py
# author by : PXY
# 输入
A_min = int(input('请输入下限:'))
A_max = int(input('请输入上限:'))
# 遍历
for x in range(A_min, A_max + 1):
    Sum = len(str(x))
    Sum1 = 0
    b = x
    # 计算
    c = Sum
    while c >= 1:
        y = x % 10
        x = x // 10
        Sum1 = Sum1 + y ** Sum
        c = c - 1
    # 输出
    if Sum1 + x ** Sum == b:
        print(b)
