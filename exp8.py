import pandas as pd

# Sample sales data
data = {
    'Item': ['Television', 'Desk', 'Cell Phone'],
    'Units': [95, 2, 27]
}

df = pd.DataFrame(data)

# Pivot table
pivot = df.pivot_table(values='Units', index='Item', aggfunc='sum')
print(pivot)
