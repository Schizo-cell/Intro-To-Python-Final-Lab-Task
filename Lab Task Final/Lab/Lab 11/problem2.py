#22-48920-3

import numpy as np

arr = np.array([2, 5, 2, 8, 2, 9])
item = 2
n = 3

positions = np.where(arr == item)[0]
print(positions[n-1])
