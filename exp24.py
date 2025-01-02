import pandas as pd
import matplotlib.pyplot as plt

# Sample data
data = {
    'Date': ['10-03-16', '10-04-16', '10-05-16', '10-06-16', '10-07-16'],
    'Close': [772.56, 776.43, 776.47, 776.86, 775.08]
}
df = pd.DataFrame(data)

# Plotting
plt.plot(df['Date'], df['Close'], marker='o')
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.title('Alphabet Inc. Financial Data')
plt.show()
