# -*- coding: UTF-8 -*-

# Filename:进制转换.py
# author by : PXY
# 获取用户输入十进制数
a = int(input('请输入十进制数:'))
# 转换为列表形式
a_bin = list(bin(a))
a_oct = list(oct(a))
a_hex = list(hex(a))
# 获取列表长度
a_bin_len = len(a_bin)
a_oct_len = len(a_oct)
a_hex_len = len(a_hex)

# 计算
i = 2
print('%d转换为二进制如下:' % a)
while a_bin_len > 2:
    print(a_bin[i], end='')
    i = i + 1
    a_bin_len = a_bin_len - 1

print()
print('%d转换为八进制如下:' % a)
i = 2
while a_oct_len > 2:
    print(a_oct[i], end='')
    i = i + 1
    a_oct_len = a_oct_len - 1

print()
print('%d转换为十六进制如下:' % a)
i = 2
while a_hex_len > 2:
    print(a_hex[i], end='')
    i = i + 1
    a_hex_len = a_hex_len - 1
