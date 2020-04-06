import numpy as np

a = np.arange(8)
b = np.arange(16).reshape(2, 8)
# 一起打印出一维和二维数组
for x, y in np.nditer([a, b]):
    print("%d:%d" % (x, y), ' ', end='')


def square(a, out=None):
    it = np.nditer([a, out],
                   flags=['external_loop', 'buffered'],
                   op_flags=[['readonly'],
                             ['writeonly', 'allocate', 'no_broadcast']])
    with it:
        for x, y in it:
            y[...] = x * x
        return it.operands[1]
