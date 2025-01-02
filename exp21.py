import pandas as pd

# Example DataFrame
data = {'Column1': ['Python', 'Data', 'Frame']}
df = pd.DataFrame(data)

# Swap cases of a column
df['Column1'] = df['Column1'].str.swapcase()
print(df)