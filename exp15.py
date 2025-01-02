import pandas as pd
import numpy as np

# Create DataFrame with NaN values
df = pd.DataFrame({
    'A': [1, np.nan, np.nan],
    'B': [4, np.nan, 6],
    'C': [7, 8, np.nan]
})

# Keep rows with at least 2 NaN values
filtered_df = df[df.isna().sum(axis=1) >= 2]

print(filtered_df)
