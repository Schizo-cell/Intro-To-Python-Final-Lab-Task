#22-48920-3

import numpy as np

arr = np.array([3, -2, 5, -8, 0, -1])
arr[arr < 0] = 0
print(arr)
