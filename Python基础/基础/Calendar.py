# -*- coding: UTF-8 -*-

# Filename:生成日历.py
# '{:<5}'设置输出格式，<代表左对齐，>代表右对齐,^代表居中,:x代表间距长度,x根据需求取值
# 一月暂时不能计算
# author by : PXY
import calendar
from datetime import datetime

import time

year = int(input('请输入年份:    '))
month = int(input('请输入月份:   '))


def J_year(x):
    return calendar.isleap(x)


def J_month(x, y):
    if x == 2:
        if J_year(y):
            return 29
        else:
            return 28
    if x == 1 or x == 3 or x == 5 or x == 7 or x == 8 or x == 10 or x == 12:
        return 31
    if x == 4 or x == 6 or x == 9 or x == 11:
        return 30


month_len = J_month(month, year)
month_list = ['January ', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
              'November', 'December']
print('         {0}   {1}         '.format(year, month_list[month - 1]))
Week_list = ['MO', 'TU', 'WE', 'TH', 'FR', 'SA', 'SU']
year_str = str(year)
month_str = str(month)
day_str = str(1)
date_str = year_str + '-' + month_str + '-' + day_str
# 标准时间
date1 = '0001-1-7'
date1 = time.strptime(date1, '%Y-%m-%d')
date2 = time.strptime(date_str, '%Y-%m-%d')
date1 = datetime(date1[0], date1[1], date1[2])
date2 = datetime(date2[0], date2[1], date2[2])
# 计算相差天数，类型为datetime.timedelta
Dec_str = date2 - date1
Total_Seconds = abs(Dec_str.total_seconds())
Total_Days = Total_Seconds / (24 * 60 * 60)
Remainder_Weeks = (Total_Days - 1) % 7
for i in range(0, len(Week_list)):
    print('{:<5}'.format(Week_list[i]), end='')
print()
# 前一个月的日历显示
for i in range(J_month(month - 1, year) - int(Remainder_Weeks) + 1, J_month(month - 1, year) + 1):
    print('{:<5}'.format(i), end='')
# 本月的日历显示
for i in range(1, month_len + 1):
    if (i + int(Remainder_Weeks)) % 7 != 0:
        print('{:<5}'.format(i), end='')
    if (i + int(Remainder_Weeks)) % 7 == 0:
        print('{:<5}'.format(i), end='')
        print()
