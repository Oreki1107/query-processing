import pandas as pd

# Sample sales data
data = {
    'Item': ['Television', 'Desk', 'Cell Phone'],
    'Sale_amt': [113810, 250, 6075]
}

df = pd.DataFrame(data)

# Pivot table
pivot = df.pivot_table(values='Sale_amt', aggfunc=['max', 'min'])
print(pivot)
