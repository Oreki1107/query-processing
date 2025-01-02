#Problem 2: Find Positions of Local Maxima in Pandas Series

import pandas as pd

# Define the function
def find_positions(series):
    positions = []
    for i in range(1, len(series) - 1):
        if series[i] > series[i - 1] and series[i] > series[i + 1]:
            positions.append(i)
    return positions

# Example usage
s = pd.Series([1, 3, 7, 1, 2, 6, 0, 1])
print("Positions of local maxima:", find_positions(s))
