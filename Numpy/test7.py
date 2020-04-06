import numpy as np

# 创建矩阵
a = np.arange(9).reshape(3, 3)
x1 = np.diag(np.diag(a))  # 提取对角线或构造对角线数组
print(x1)
print('*' * 50)

x2 = np.diagflat([[1, 2], [3, 4]])  # 使用展平的输入作为对角线创建二维数组。
print(x2)
print('*' * 50)

x3 = np.tri(3, 3, 0, dtype=int)  # 在给定对角线处及以下且在其他位置为零的数组。即下三角为1。
print(x3)
print('*' * 50)

x4 = np.tril([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]], -1)  # 矩阵的下三角，-2即以7,11为对角线。-1以4,8,12为对角线
print(x4)
print('*' * 50)

x5 = np.triu([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]], -1)  # 矩阵的上三角，参考下三角
print(x5)
print('*' * 50)

x = np.array([1, 2, 3, 5])  # 生成范德蒙矩阵
# 输出矩阵的列是输入向量的幂。幂的顺序由递增的布尔参数确定。具体来说，当增加为False时，第i个输出列是逐元素提高到的幂的输入向量。
# 每行中具有几何级数的矩阵以Alexandre-Theophile Vandermonde的名字命名。N - i - 1
x6 = np.vander(x)
print(x6)
print('*' * 50)

# 构造块矩阵
A = np.mat('1 1; 1 1')
B = np.mat('2 2; 2 2')
C = np.mat('3 4; 5 6')
D = np.mat('7 8; 9 0')
x7 = np.bmat([[A, B], [C, D]])
print(x7)
print('*' * 50)

x8 = np.bmat(np.r_[np.c_[A, B], np.c_[C, D]])
print(x8)
print('*' * 50)

x9 = np.bmat('A,B; C,D')
print(x9)
print('*' * 50)
