import numpy as np

x = np.array([[[0, 1, 2],
               [3, 4, 5],
               [6, 7, 8]],
              [[9, 10, 11],
               [12, 13, 14],
               [15, 16, 17]],
              [[18, 19, 20],
               [21, 22, 23],
               [24, 25, 26]], ])
print(x.var(axis=2, dtype=np.float64))  # 指定轴的方差
print(x.mean(axis=2, dtype=np.float64))  # 指定轴的平均值
print(x.std(axis=2))  # 指定轴的标准差
print(x.prod(axis=2))  # 返回指定轴元素的乘积
print(x.cumprod(axis=2))  # 返回指定轴元素的累积乘积
print(x.__lt__(9))  # 小于9赋值为True
print(x.__le__(9))  # 小于等于9赋值为True
x.__gt__(9)  # 大于9赋值为True
x.__ge__(9)  # 大于等于9赋值为True
x.__eq__(9)  # 等于9赋值为True
x.__ne__(9)  # 不等于9赋值为True
