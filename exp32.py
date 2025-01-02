import matplotlib.pyplot as plt
import numpy as np

# Random Data
x = np.random.rand(50)
y = np.random.rand(50)

# Scatter Plot
plt.scatter(x, y, color='purple')
plt.title('Random Scatter Plot')
plt.show()
