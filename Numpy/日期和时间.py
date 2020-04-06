import numpy as np

# time = np.arange('2005-02', '2005-05', dtype='datetime64[D]')
# print(time)

print(np.datetime64('2019-11') + np.timedelta64(3000, 'D'))
print(np.timedelta64(1, 'W') / np.timedelta64(1, 'D'))
print(np.timedelta64(1, 'W') % np.timedelta64(10, 'D'))
print(np.busday_offset('2011-06-23', 1))
print(np.busday_offset('2011-06-23', 2))
print(np.busday_offset('2019-11-07', 2))  # 只会显示工作日时间
# 当输入日期落在周末或假日时， busday_offset首先应用规则将日期滚动到有效的工作日，然后应用偏移量。
# 默认规则是'raise'，它只会引发异常。最常用的规则是“前进”和“后退”。
print(np.busday_offset('2011-06-25', 0, roll='forward'))
print(np.busday_offset('2011-06-25', 0, roll='backward'))
print(np.busday_offset('2019-11-07', 0, roll='forward', weekmask='Sun'))  # 接下来的第0+1个星期日
# 查看是否是有效日期:即是否是工作日
a = np.arange(np.datetime64('2011-07-11'), np.datetime64('2011-07-18'))
print(np.is_busday(a))

# 查询指定日期内有效日期
print(np.busday_count(np.datetime64('2019-11-07'), np.datetime64('2019-11-25')))
print(np.sin(12))