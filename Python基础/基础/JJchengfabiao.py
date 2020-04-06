# -*- coding: UTF-8 -*-

# Filename:JJchengfabiao.py
# author by : PXY
for i in range(1, 10):
    for j in range(1, i + 1):
        print('{0}x{1}={2}\t'.format(j, i, i * j), end='')  # end=''表示循环中不换行，默认为end='\n'
    print()
