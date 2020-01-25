import numpy as np
np.random.seed(100)
a = np.random.randint(0, 5, 10)
indicesList = np.unique(a, return_index=True)[1]
a = np.repeat(True, np.size(a))
a[indicesList] = np.repeat(False, np.size(a[indicesList]))
print("Array: ", a)