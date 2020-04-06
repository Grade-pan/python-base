import numpy as np

a = np.arange(24).reshape(3, 2, 4) + 10
for val in a:
    print('item:', val)

# N维枚举
for i, val in np.ndenumerate(a):
    if sum(i) % 5 == 0:
        print(i, val)
