import numpy as np

# 创建数组
x = np.zeros((2, 3), np.int8, order='C')
print(x)
print('*' * 50)

x1 = np.eye(3, k=0)
print(x1)
print('*' * 50)

x2 = np.eye(3, k=1)
print(x2)
print('*' * 50)

x3 = np.identity(5)  # 标识数组是一个在主对角线上带有1的正方形数组。
print(x3)
print('*' * 50)

x4 = np.ones((2, 2))  # 返回给定形状和类型的新数组，并填充为1
print(x4)
print('*' * 50)

x5 = np.full((2, 2), 100)  # 返回给定形状和类型的新数组，并用fill_value填充
print(x5)
print('*' * 50)

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # 将输入转换为数组。
x6 = np.asarray(a, order='F')
print(x6.reshape(2, 5))
print('*' * 50)

a = np.array([[1, 2], [3, 4]])  # 将输入解释为矩阵。
x7 = np.asmatrix(a)
print(x7)
print('*' * 50)

x8 = np.linspace(2, 13, num=12, retstep=True)  # 返回指定间隔内的等间隔数字。
print(x8)
print('*' * 50)

x9 = np.logspace(2, 4, num=5, base=2)  # 返回数以对数刻度均匀分布
print(x9)
print('*' * 50)

x10 = np.geomspace(1, 1024, num=11, dtype=int)  # 返回数字以对数刻度（几何级数）均匀分布。
print(x10)
print('*' * 50)

x11 = np.mgrid[0:5, 0:9]  # 返回一个密集的多维“ meshgrid”。
print(x11)
print('*' * 50)

x12 = np.ogrid[0:5, 0:9]  # 返回一个开放的多维“ meshgrid”
print(x12)
