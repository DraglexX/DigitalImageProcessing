import numpy as np

arr = np.arange(5)
a = np.tile(arr, (5,1))
b = a.transpose()
print(b)
