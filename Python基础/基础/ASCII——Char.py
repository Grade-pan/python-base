# -*- coding: UTF-8 -*-

# Filename:ASCII和字符相互转换.py
# author by : PXY
a = input('请输入一个字符:')
b = int(input('请输入一个ASCII码:'))
print('{0}对应的ASCII为{1}'.format(a, ord(a)))
print('{0}对应的字符为{1}'.format(b, chr(b)))
