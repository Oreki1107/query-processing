import pandas as pd

# Sample DataFrame
df = pd.DataFrame({
    'school_code': ['S001', 'S002', 'S001', 'S002'],
    'age': [14, 15, 16, 14]
})

# Group and aggregate
result = df.groupby('school_code')['age'].agg(['mean', 'min', 'max'])
print(result)
