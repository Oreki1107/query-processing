import pandas as pd

# Sample DataFrame
df = pd.DataFrame({
    'school_code': ['S001', 'S002', 'S001', 'S002'],
    'age': [14, 15, 16, 14]
})

# Group by school_code
grouped = df.groupby('school_code')

print(type(grouped))
