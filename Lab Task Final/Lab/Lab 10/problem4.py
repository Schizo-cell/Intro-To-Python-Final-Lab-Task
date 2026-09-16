# 22-48920-3

import numpy as np

a = np.array([1, 2, 3, 4, 5])
b = np.array([1, 9, 3, 8, 5])

positions = np.where(a == b)
print(positions)