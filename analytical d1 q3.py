#Problem 3: Replace Missing Spaces with Least Frequent Character

import pandas as pd

# Define the function
def replace_missing_spaces(text):
    char_series = pd.Series(list(text))
    char_counts = char_series.value_counts()
    least_frequent_char = char_counts.idxmin()
    return text.replace(' ', least_frequent_char)

# Example usage
text = "hello world"
print("Modified Text:", replace_missing_spaces(text))
