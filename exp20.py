import pandas as pd

# Sample DataFrame
df = pd.DataFrame({
    'Text': ['apple pie', 'banana shake', 'cherry tart']
})

# Find substring index
df['Index'] = df['Text'].str.find('pie')
print(df)
