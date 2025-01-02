import matplotlib.pyplot as plt
import numpy as np

# Random Data
x = np.random.rand(50)
y = np.random.rand(50)

# Scatter Plot with Empty Circles
plt.scatter(x, y, edgecolor='blue', facecolor='none')
plt.title('Scatter Plot with Empty Circles')
plt.show()
