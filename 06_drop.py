import numpy as np
arr = np.array([1,2,3,np.nan,5,6,7,np.nan])
arr = arr[~np.isnan(arr)]
print(arr)