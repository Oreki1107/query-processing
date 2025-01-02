import pandas as pd
import numpy as np

# Create a DataFrame with random values
df = pd.DataFrame(np.random.randn(10, 4), columns=['A', 'B', 'C', 'D'])

# Apply custom styles
df.style.set_properties(**{
    'background-color': 'black',
    'color': 'yellow'
})
