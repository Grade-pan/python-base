from matplotlib import pyplot as plt
import numpy as np

# 频率分布图
a = np.array([22, 87, 5, 43, 56, 73, 55, 54, 11, 20, 51, 5, 79, 31, 27, 120])
plt.hist(a, bins=[0, 20, 40, 60, 80, 100, 120])
plt.title("histogram")
plt.show()
