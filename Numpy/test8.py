import numpy as np

print('-' * 50)
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
x = np.ravel(a)  # 返回一个连续的扁平数组。
print(x)
print('-' * 50)

x1 = a.flatten()  # 返回折叠成一维的数组副本。
print(x1)
print('-' * 50)

x2 = np.moveaxis(a, 0, 1)  # 将数组的轴移到新位置。类似于数组的转置
print(x2)
print('-' * 50)

x3 = np.swapaxes(a, 1, 0)  # 互换数组的两个轴，axis0表示沿行方向的轴，即垂直方向，axis1表示沿列方向的轴，即水平方向
print(x3)
print('-' * 50)
