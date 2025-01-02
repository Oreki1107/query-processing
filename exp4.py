import pandas as pd
import matplotlib.pyplot as plt

# Sample stock data
data = {
    'Date': pd.date_range(start='2024-01-01', periods=10),
    'Stock_Price': [100, 102, 105, 107, 110, 108, 111, 115, 117, 120]
}

df = pd.DataFrame(data)
df.set_index('Date', inplace=True)

# Plot line graph
df['Stock_Price'].plot(title='Historical Stock Prices', xlabel='Date', ylabel='Price')
plt.show()
