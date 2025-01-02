import pandas as pd

# Sample DataFrame
df = pd.DataFrame({
    'school_code': ['S001', 'S002', 'S001', 'S002'],
    'class': ['A', 'B', 'A', 'B'],
    'age': [14, 15, 16, 14]
})

# Group by school_code and class
grouped = df.groupby(['school_code', 'class'])
print(grouped.mean())
