import numpy as np

# 三维数组三个轴（axis）axis=0表示全部，axis=1表示每一列，axis=2表示每一行
x = np.array([[[0, 1, 2],
               [3, 4, 5],
               [6, 7, 8]],
              [[9, 10, 11],
               [12, 13, 14],
               [15, 16, 17]],
              [[18, 19, 20],
               [21, 22, 23],
               [24, 25, 26]], ])
print(x.sum(axis=1))  # 给定轴求和
print(x.max(axis=0))  # 给定轴的最大值值
print(x.argmax(axis=0))  # 给定轴最大值索引
print(x.min(axis=0))  # 给定轴最小值
print(x.argmin(axis=0))  # 给定轴最小值的索引
print(x.ptp(axis=0))  # 给定轴最大值减去最小值的值或者峰峰值
print(x.trace())  # 计算对角线的和
list_shuzu = x.trace()
# 该三维数组有三个二维页面构成，顺序随意。 计算暂时按上述二维数组排列页面
# 第一个对角线值为 x[0,0,0]+x[1,1,0]+x[2,2,0]
# 第二个对角线值为 x[0,0,1]+x[1,1,1]+x[2,2,1]
# 第三个对角线的值为 x[0,0,2]+x[1,1,2]+x[2,2,2]
# 检验结果
First = x[0, 0, 0] + x[1, 1, 0] + x[2, 2, 0]
Second = x[0, 0, 1] + x[1, 1, 1] + x[2, 2, 1]
Third = x[0, 0, 2] + x[1, 1, 2] + x[2, 2, 2]
print('第一个对角线的值: ', First)
print('第二个对角线的值：', Second)
print('第三个对角线的值：', Third)
if First in list_shuzu and Second in list_shuzu and Third in list_shuzu:
    print('检验结果正确')
else:
    print('检验结果不正确')
# 数组转置
y = x.T
First1 = y[0, 0, 0] + y[1, 1, 0] + y[2, 2, 0]
Second1 = y[0, 0, 1] + y[1, 1, 1] + y[2, 2, 1]
Third1 = y[0, 0, 2] + y[1, 1, 2] + y[2, 2, 2]
print(First1, Second1, Third1)
# 转置后对角线和有变化
