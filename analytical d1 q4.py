#Problem 4: Compute Autocorrelation at a Specified Lag

import pandas as pd
import numpy as np

# Define the function
def compute_autocorrelations(series, lag):
    return series.autocorr(lag=lag)

# Example usage
s = pd.Series(np.random.rand(100))
print("Autocorrelation at lag 1:", compute_autocorrelations(s, 1))
