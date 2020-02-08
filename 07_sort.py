import numpy as np
import pandas as pd
labels = ['a','b','c','d','e','f','g','h','i','j']
data = pd.DataFrame({
    'animal': ['cat','cat','snake','dog','dog','cat','snake','cat','dog','dog'],
    'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
    'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'priority': ['yes','yes','no','yes','no','no','no','yes','no','no']}, index = labels)

print("Sorted by animal age: ")
print(data.sort_values(by=['age'], ascending=False))
print("Sorted by visits: ")
print(data.sort_values(by=['visits']))