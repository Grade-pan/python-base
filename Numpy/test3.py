import numpy as np

x = np.array([1, 2, 3, 4, 5, 6])
print(x.data)
dt1 = np.dtype('i4')  # 32-bit signed integer
dt2 = np.dtype('f8')  # 64-bit floating-point number
dt3 = np.dtype('c16')  # 128-bit complex floating-point number
dt4 = np.dtype('a25')  # 25-length zero-terminated bytes
dt5 = np.dtype('U25')  # 25-character string
print(dt1, dt2, dt3, dt4, dt5)