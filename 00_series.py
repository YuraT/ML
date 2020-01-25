import numpy as np
import pandas as pd
my_series = pd.Series([1, 2, 3, "string", 6.9], index=["A", "B", "C", "D", "E"])
print(my_series)
print(my_series["D"])