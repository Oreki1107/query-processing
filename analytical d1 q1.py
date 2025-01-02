#Problem 1: Euclidean Distance Between Two Pandas Series


import pandas as pd
import numpy as np

# Define the function
def euclidean_distance(series1, series2):
    array1 = series1.to_numpy()
    array2 = series2.to_numpy()
    return np.sqrt(np.sum((array1 - array2) ** 2))

# Example usage
s1 = pd.Series([1, 2, 3])
s2 = pd.Series([4, 5, 6])
print("Euclidean Distance:", euclidean_distance(s1, s2))
