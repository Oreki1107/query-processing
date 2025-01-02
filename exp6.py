import pandas as pd
import matplotlib.pyplot as plt

# Sample data
data = {
    'Stock_Price': [100, 102, 105, 107, 110, 108, 111, 115, 117, 120],
    'Volume': [1000, 1500, 1300, 1800, 1700, 1600, 2000, 2100, 1900, 2200]
}

df = pd.DataFrame(data)

# Scatter plot
df.plot.scatter(x='Stock_Price', y='Volume', title='Volume vs Stock Price')
plt.show()
