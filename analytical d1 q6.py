#Problem 6: Convert Series to DataFrame with reset_index()

import pandas as pd

# Define the function
def series_to_dataframe(series):
    return series.reset_index()

# Example usage
s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
print(series_to_dataframe(s))
