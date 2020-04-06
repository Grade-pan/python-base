# -*- coding: UTF-8 -*-

# Filename:ErCiFangChang.py
# 二次方程式 ax**2 + bx + c = 0
# a、b、c 用户提供，为实数，a ≠ 0
# 导入 cmath(复杂数学运算) 模块
# author by : PXY
import cmath

# 输入
a = float(input('请输入'))
b = float(input('请输入'))
c = float(input('请输入'))

# 计算
d = b ** 2 - 4 * a * c

# 两种求解方式
sol1 = (-b - cmath.sqrt(d)) / (2 * a)
sol2 = (-b + cmath.sqrt(d)) / (2 * a)

# 结果
print('结果为 {0} 和 {1}'.format(sol1, sol2))
