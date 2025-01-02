import pandas as pd
import numpy as np

# Create a DataFrame with random values
df = pd.DataFrame(np.random.randn(10, 4), columns=['A', 'B', 'C', 'D'])

# Introduce NaN values
df.iloc[1, 2] = np.nan
df.iloc[4, 1] = np.nan

# Highlight NaN values
df.style.applymap(lambda x: 'background-color: yellow' if pd.isna(x) else '')
