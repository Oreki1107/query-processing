import pandas as pd
import numpy as np

# Create DataFrame with NaN values
df = pd.DataFrame({
    'A': [1, 2, np.nan],
    'B': [4, np.nan, 6],
    'C': [7, 8, 9]
})

# Detect missing values
print(df.isna())
