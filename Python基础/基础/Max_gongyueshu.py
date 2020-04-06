# -*- coding: UTF-8 -*-

# Filename:最大公约数.py
# author by : PXY
# 用datetime函数计算几种不同方法所需的时间
# 用更相减损法、质因数分解法、辗转相除法计算最大公约数
from datetime import datetime

a = int(input('请输入较大的一个数:'))
b = int(input('请输入较小的一个数:'))
a1 = a
b1 = b
a2 = a
b2 = b
a3 = a
b3 = b
a4 = a
b4 = b
# 更相减损法
Time1 = datetime.now()
while a != b:
    c = abs(a - b)
    a = b
    b = c
Time2 = datetime.now()

# 质因数分解法
Time3 = datetime.now()
A_list = [1]
B_list = [1]
# 分解成质因数，因算法水平有限建议不要输入太大的数
m = 2
for i in range(m, a1):
    if a1 % i == 0:
        A_list.append(i)
        a1 = a1 // i
        while a1 % i == 0:
            a1 = a1 // i
            m = i
            A_list.append(i)
    else:
        continue
m = 2
for i in range(m, b1):
    if b1 % i == 0:
        B_list.append(i)
        b1 = b1 // i
        while b1 % i == 0:
            b1 = b1 // i
            m = i
            B_list.append(i)
        else:
            continue
# 计算最大公约数
A_len = len(A_list)
B_len = len(B_list)
Sum = 1
for i in range(0, min(A_len, B_len)):
    if B_list[i] in A_list:
        Sum = Sum * int(B_list[i])
    else:
        continue
Time4 = datetime.now()

# 辗转相除法
Time5 = datetime.now()
c = 1
while a3 % b3 != 0:
    c = a3 % b3
    print(a3, b3, c)
    a3 = b3
    b3 = c
Time6 = datetime.now()
print('有更相减损法得{0}和{1}的最大公约数是{2}'.format(a2, b2, a))
print('有质因数分解法得{0}和{1}的最大公约数是{2}'.format(a2, b2, Sum))
print('有辗转相除法得{0}和{1}的最大公约数是{2}'.format(a4, b4, b3))
print('更相减损法所需要的时间为{0}秒'.format(Time2.timestamp() - Time1.timestamp()))
print('质因数分解法所需要的时间为{0}秒'.format(Time4.timestamp() - Time3.timestamp()))
print('辗转相除法所需要的时间为{0}秒'.format(Time6.timestamp() - Time5.timestamp()))
