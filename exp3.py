import pandas as pd

# Sample data
data = {
    'JOB_ID': ['AD_PRES', 'AD_VP', 'AD_ASST', 'FI_MGR'],
    'JOB_TITLE': ['President', 'Administration Vice President', 'Administration Assistant', 'Finance Manager'],
    'MIN_SALARY': [20080, 15000, 3000, 8200],
    'MAX_SALARY': [40000, 30000, 6000, 16000]
}

df = pd.DataFrame(data)

# Sort by JOB_TITLE descending
df_sorted = df.sort_values(by='JOB_TITLE', ascending=False)

print(df_sorted)
