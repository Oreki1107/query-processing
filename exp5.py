import pandas as pd
import matplotlib.pyplot as plt

# Sample trading volume data
data = {
    'Date': pd.date_range(start='2024-01-01', periods=10),
    'Volume': [1000, 1500, 1300, 1800, 1700, 1600, 2000, 2100, 1900, 2200]
}

df = pd.DataFrame(data)
df.set_index('Date', inplace=True)

# Plot bar graph
df['Volume'].plot(kind='bar', title='Trading Volume', xlabel='Date', ylabel='Volume')
plt.show()
