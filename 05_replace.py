import numpy as np
myList = [[1, 2, 3, 4],[3, 4, 5, 6], [5, 6, 7, 8]]
arr = np.array(myList, dtype='float')
arr[1,1] = np.nan
arr[1,2] = np.inf
nan_mask = np.isnan(arr)
arr[nan_mask] = np.repeat(-1, np.size(nan_mask[nan_mask>0]))
inf_mask = np.isinf(arr)
arr[inf_mask] = np.repeat(-1, np.size(inf_mask[inf_mask>0]))
print(arr)