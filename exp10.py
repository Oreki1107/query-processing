import pandas as pd
import numpy as np

# Create DataFrame with random values
df = pd.DataFrame(np.random.randn(10, 4), columns=['A', 'B', 'C', 'D'])

# Highlight negative numbers
df.style.applymap(lambda x: 'color: red' if x < 0 else 'color: black')
