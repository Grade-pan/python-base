import matplotlib
import numpy as np
from matplotlib import pyplot as plt

x = np.arange(-np.pi, np.pi)
y_sin = np.sin(3 * x) + np.sin(5 * x)
plt.title('fuliye')
plt.plot(x, y_sin)
plt.show()
