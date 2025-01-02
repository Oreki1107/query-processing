import pandas as pd

# Sample sales data
data = {
    'Region': ['East', 'Central'],
    'Manager': ['Martha', 'Hermann'],
    'SalesMan': ['Alexander', 'Luis'],
    'Sale_amt': [113810, 25000]
}

df = pd.DataFrame(data)

# Pivot table
pivot = df.pivot_table(values='Sale_amt', index=['Region', 'Manager', 'SalesMan'], aggfunc='sum')
print(pivot)
