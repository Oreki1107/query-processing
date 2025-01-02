import pandas as pd
import numpy as np

# Create DataFrame with NaN values
df = pd.DataFrame({
    'A': [1, 2, np.nan],
    'B': [4, np.nan, 6],
    'C': [7, 8, 9]
})

# Replace NaN with a specific value
df.fillna(0, inplace=True)

print(df)
