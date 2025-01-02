import matplotlib.pyplot as plt
import numpy as np

# Random Data
x = np.random.rand(50)
y = np.random.rand(50)
sizes = np.random.rand(50) * 1000

# Scatter Plot
plt.scatter(x, y, s=sizes, alpha=0.5, color='green')
plt.title('Scatter Plot with Different Sizes')
plt.show()
