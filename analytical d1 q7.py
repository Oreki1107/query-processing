#Problem 7: Stack Series Vertically and Horizontally Using pd.concat()

import pandas as pd

# Sample Series
s1 = pd.Series([1, 2, 3])
s2 = pd.Series([4, 5, 6])

# Vertical Stacking
vertical_stack = pd.concat([s1, s2], axis=0)
print("Vertical Stack:\n", vertical_stack)

# Horizontal Stacking
horizontal_stack = pd.concat([s1, s2], axis=1)
print("Horizontal Stack:\n", horizontal_stack)